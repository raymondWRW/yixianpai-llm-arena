# -*- coding: utf-8 -*-
"""The ECONOMY agent — 换牌 rolls + hold/absorb as LEARNED per-card decisions.

The two decisions real players win with (user-identified, mined-confirmed):
  · 换牌 ROLLS: banked charges (+2/round, no cap) are DUMPED in the rounds where
    the build's key cards can appear (mined: spend jumps 0.3→2.5/round at R10-14
    when phase 3-4 unlock) — and the timing/targets vary by character.
  · HOLD vs ABSORB: leftover cards can be absorbed now (+1 修为 tempo) or HELD to
    complete future merges / play when their tier comes online (mined: real hands
    grow 1→3-5 exactly at R10+).

Both are per-card binary choices given full context → the same shape as the
placement policy net (context → per-card logit), so we reuse CardPolicyNet with
separate checkpoints. decision = logit > 0 (BCE-calibrated), trained with AWR on
ghost-game rewards (games graded vs the REAL field).

make_agent_policy composes: rolls → placement (existing net) → hold/absorb →
breakthrough, records every decision for training, and supports ε-exploration
plus a scripted heuristic mode (bank-then-dump + hold-keys) to seed good
trajectories into the first iterations' data.
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import economy as E
import env as EV
import merge as M

# policy_net drags in torch (heavy; can even FAIL to load — WinError 1455 small
# paging file — which then breaks every importer of this module). The live bot
# imports econ9→econ but never touches the learned choosers, so torch is loaded
# lazily on first PN use instead of at import time.
PN = None


def _pn():
    global PN
    if PN is None:
        import policy_net as _p
        PN = _p
    return PN


REROLL_CAP = 25          # rule: >25 charges at turn start → MUST roll down to ≤25


def _phase(env, p, cid: int) -> int:
    return env._card_phase(p, cid)


def _forced_spend_down(env, p, card_net=None):
    """Enforce the 25-charge cap: while over it (and holding cards), roll the
    worst card — by card-value if a net is given, else lowest phase / non-merge.
    Runs AFTER the policy's chosen rolls; these are rule-forced, not decisions."""
    while p.rerolls > REROLL_CAP and p.hand:
        hand = list(p.hand)
        if card_net is not None:
            v = _values(card_net, EV.decision_state(env, p), hand,
                        [x for x in p.board if x] + list(p.hand))
            worst = hand[int(v.argmin())]
        else:
            cnt = _pair_counts(p)
            pool = [c for c in hand if cnt[c] < 2] or hand
            worst = min(pool, key=lambda c: _phase(env, p, c))
        if env.reroll(p, worst) is None and worst in p.hand:
            break                                   # bag empty → can't spend down


def _pair_counts(p) -> Counter:
    """id → copies across board+hand (merge-progress bookkeeping)."""
    return Counter([c for c in p.board if c] + list(p.hand))


# ── scripted heuristic (seeds the strategy the user described) ───────────────
def heur_roll(env, p) -> list:
    """Bank early; from R9+ dump charges fishing: roll away sub-tier singles that
    neither sit on the board nor complete a pair."""
    r = env.state.round
    budget = p.rerolls if r >= 9 else (1 if r >= 5 and p.rerolls > 3 else 0)
    if budget <= 0 or not p.hand:
        return []
    cnt = _pair_counts(p)
    board = set(c for c in p.board if c)
    cands = [c for c in p.hand
             if c not in board and cnt[c] < 2 and _phase(env, p, c) < p.realm]
    cands.sort(key=lambda c: _phase(env, p, c))          # worst chaff first
    return cands[:budget]


def heur_hold(env, p, leftovers: list) -> list:
    """Hold future keys: pair-in-progress cards (merge material) and cards of the
    current tier or above; absorb the rest for tempo."""
    cnt = _pair_counts(p)
    hold = [c for c in leftovers
            if (cnt[c] >= 2 and M.can_level(c)) or _phase(env, p, c) >= p.realm]
    return hold[:8]


# ── card-value-driven decisions (LEARNED what-to-look-for, COMPUTED how) ──────
def _pool_ids_probs(p, phase: int):
    """The exact remaining draw pool at `phase` as (ids, probs) — we KNOW the bag."""
    import cards as C
    ids, ws = [], []
    for nm, copies in p.bag.copies.items():
        if copies <= 0 or p.bag.phase.get(nm, 1) > phase:
            continue
        cid = C.name_to_base_id(nm)
        if cid:
            ids.append(cid); ws.append(float(copies))
    tot = sum(ws)
    return ids, [w / tot for w in ws] if tot else []


def _values(card_net, st, ids, set_ids=None):
    """Synergy-aware values: each candidate scored attending over `set_ids`
    (the cards it would play with — board+hand by default)."""
    import card_value as CV
    return CV.card_values(card_net, st, ids, set_ids)


def _expected_improvement(card_net, st, setids, v_cur: float, p, phase: int) -> float:
    """EI of ONE roll on a card worth v_cur, against the LIVE pool at `phase`:
    Σ p(x)·max(0, V(x) − v_cur). This is the sequential-search quantity — a bad
    draw can be rolled again, so a charge buys the UPSIDE of the draw, not its
    average."""
    ids, pr = _pool_ids_probs(p, phase)
    if not ids:
        return 0.0
    v = _values(card_net, st, ids, setids)
    return float(sum(q * max(0.0, float(x) - v_cur) for x, q in zip(v, pr)))


def _base_id(cid: int) -> int:
    return cid - ((cid // 10000) % 100) * 10000


def cv_fish(env, p, card_net, tau: float = 0.005, max_rolls: int = 20,
            protect=None) -> list:
    """SEQUENTIAL fishing (roll → look → roll again) with optimal stopping.

    Each iteration re-values the hand (synergy attention over the LIVE set),
    picks the worst non-protected card, and spends a charge iff the expected
    improvement of one more roll (vs the live pool — copies burn as we go)
    clears that charge's cost: FREE charges (the 25-cap forces them out anyway)
    cost 0; BANKED charges cost the next-phase fishing premium
    max(0, EI_next − EI_now) — bank only when the next tier fishes better.
    A bad replacement is naturally rolled again next iteration; a good one
    raises the floor and stops the loop. 'How much to roll' is emergent."""
    rolled = []
    n_free = max(0, p.rerolls + E.reroll_grant(env.state.round + 1) - REROLL_CAP)
    while p.hand and len(rolled) < max_rolls:
        innate_free = (EV.YiXianEnv.FREE_ROLL_FATE in p.talents
                       and not p.free_roll_used)     # 云雾变幻: this roll is free
        if p.rerolls <= 0 and not innate_free:
            break
        st = EV.decision_state(env, p)
        hand = list(p.hand)
        setids = [c for c in p.board if c] + hand
        ids_now, pr_now = _pool_ids_probs(p, p.phase)
        if not ids_now:
            break
        ids_nx, pr_nx = (_pool_ids_probs(p, p.phase + 1)
                         if (p.realm < 5 and len(rolled) >= n_free) else ([], []))
        all_ids = hand + ids_now + ids_nx
        v = _values(card_net, st, all_ids, setids)                   # ONE forward
        if protect:
            # template OPTIMISM: pieces of the target build are valued as if
            # they already worked — the roll loop actively HUNTS them (mere
            # roll-away protection never collects a combo the net undervalues)
            v = [float(x) + (0.30 if _base_id(c) in protect else 0.0)
                 for x, c in zip(v, all_ids)]
        v_hand = v[:len(hand)]
        v_now = v[len(hand):len(hand) + len(ids_now)]
        v_nx = v[len(hand) + len(ids_now):]
        cnt = _pair_counts(p)
        cands = [(float(v_hand[i]), hand[i]) for i in range(len(hand))
                 if not (cnt[hand[i]] >= 2 and M.can_level(hand[i]))
                 and not (protect and _base_id(hand[i]) in protect)]
        if not cands:
            break
        v_worst, worst = min(cands)
        ei_now = float(sum(q * max(0.0, float(x) - v_worst)
                           for x, q in zip(v_now, pr_now)))
        if innate_free or len(rolled) < n_free:
            oc = 0.0                                  # free roll / use-or-lose charge
        elif ids_nx:
            ei_next = float(sum(q * max(0.0, float(x) - v_worst)
                                for x, q in zip(v_nx, pr_nx)))
            # DESTINY-WEIGHTED banking (user: real players roll lean in phase 3
            # and save for the phase-4 unlock — early losses cost little, late
            # ones decide the game). Values are round-normalized, so a banked
            # charge cashes its improvement at HIGHER stakes: weight the future
            # side by the stakes ratio ~2 rounds out. The ratio is largest in
            # the early-mid game and →1 late (stakes saturate), so saving
            # pressure fades exactly when spending should happen.
            import card_value as _CV
            rnd = env.state.round
            # saving applies from phase 3 on (the user's rule: roll less in
            # phase 3, dump at phase 4) — the OPENING is the opposite: real
            # players burn starting charges to stack a leveled attacker by
            # R2-3, and early saving bled 0.14 winrates at R1-3
            w = _CV.stakes(rnd + 2) / _CV.stakes(rnd) if rnd >= 5 else 1.0
            oc = max(0.0, w * ei_next - ei_now)       # banking premium
        else:
            oc = 0.0
        if ei_now <= oc + tau:
            break                                     # a charge no longer pays
        if env.reroll(p, worst) is None and worst not in p.hand:
            rolled.append(worst)
            break                                     # bag exhausted
        rolled.append(worst)
    return rolled


def cv_hold(env, p, card_net, leftovers: list, tau: float = 0.05,
            protect=None) -> list:
    """Hold what's worth looking for: a leftover stays if its value (or its MERGED
    version's value, discounted by completion odds from the known pool) beats the
    board's weakest fielded card by `tau` — else absorb it for tempo. `protect`:
    base ids held unconditionally (template exploration — collect build pieces)."""
    if not leftovers:
        return []
    if protect:
        kept, rest = [], list(leftovers)
        for c in leftovers:
            if len(kept) < 6 and _base_id(c) in protect:
                kept.append(c)
                rest.remove(c)                      # first copy only (multiset)
        return (kept + cv_hold(env, p, card_net, rest, tau))[:10]
    st = EV.decision_state(env, p)
    board = [c for c in p.board if c]
    setids = board + leftovers
    v_board_min = float(min(_values(card_net, st, board, setids))) if board else 0.35
    v_left = _values(card_net, st, leftovers, setids)
    cnt = _pair_counts(p)
    hold = []
    for c, v in sorted(zip(leftovers, v_left), key=lambda t: -t[1]):
        keep = float(v) > v_board_min + tau
        if not keep and M.can_level(c):
            up = M.level_up(c)
            need_pair = cnt[c] >= 2
            v_up = float(_values(card_net, st, [up], setids)[0])
            odds = 1.0 if need_pair else _copies_left_frac(p, c)
            keep = v_up * odds > v_board_min + tau
        if keep:
            hold.append(c)
    return hold[:10]


def _copies_left_frac(p, cid) -> float:
    """Rough odds of completing the pair: remaining copies of this card in the bag
    (scaled) — 0 copies → 0 (never completing), 2+ → 0.5."""
    import cards as C
    nm = C.id_to_name(cid)
    left = p.bag.copies.get(nm, 0)
    return min(left, 2) * 0.25


def _fuse_pair(p, c, up):
    """Consume two copies of c (board copies first) → one `up`, upgraded in
    place on the board when a copy sat there, else appended to hand."""
    board_idx = [i for i, b in enumerate(p.board) if b == c]
    if board_idx:
        p.board[board_idx[0]] = up
        if len(board_idx) >= 2:
            p.board[board_idx[1]] = 0
        else:
            p.hand.remove(c)
    else:
        p.hand.remove(c)
        p.hand.remove(c)
        p.hand.append(up)


def decide_merges(env, p, card_net=None, explore: float = 0.0, protect=None):
    """EXPLICIT merge decisions before placement (the real game merges by
    stacking a copy onto its duplicate — it's an ACTION, and real boards carry
    UNMERGED duplicates on purpose). For each pair across board+hand: fuse iff
    V(merged) + V(the benched card that fills the freed slot) beats the two
    copies' combined value; without a net, fuse when board slots are binding.
    Cascades (two L2 → L3); +1 cult per merge. Returns merges done."""
    st = None
    merged_n = 0
    while True:
        pool = [c for c in p.board if c] + list(p.hand)
        cnt = Counter(pool)
        pairs = [c for c, n in cnt.items() if n >= 2 and M.can_level(c)
                 and not (protect and _base_id(c) in protect)]   # real builds run
        if not pairs:                                # MULTIPLE L1 engine copies
            return merged_n                          # (汇灵 109% = >1 per board)
        slots = E.unlocked_slots(env.state.round)
        binding = len(pool) > slots
        did = False
        if card_net is not None and st is None:
            st = EV.decision_state(env, p)
        for c in pairs:
            up = M.level_up(c)
            if card_net is not None:
                # SET-LEVEL comparison (user design): fuse only if the projected
                # best board WITH the L2 outplays the one keeping the pair. A
                # self-combo (copy attending its twin) can beat the fuse, and a
                # fuse that breaks the set loses even though V(L2) > V(L1).
                import card_value as CVAL
                fused_pool = list(pool)
                fused_pool.remove(c); fused_pool.remove(c); fused_pool.append(up)

                def _proj(pl):
                    vv = _values(card_net, st, pl, pl)
                    return [x for _, x in sorted(zip([float(t) for t in vv], pl),
                                                 key=lambda t: -t[0])]
                keep_b, fuse_b = _proj(pool), _proj(fused_pool)
                L = min(slots, len(fuse_b))          # equal-size, no mean bias
                sc = CVAL.board_scores(card_net, st, [keep_b[:L], fuse_b[:L]])
                fuse = float(sc[1]) > float(sc[0]) + 0.005
            else:
                fuse = binding
            if explore > 0 and env.state.rng.random() < 0.15:
                fuse = not fuse                      # merge exploration: without it a
                                                     # reluctant net never CREATES the
                                                     # leveled-card data that would fix
                                                     # its own miscalibration
            if fuse:
                _fuse_pair(p, c, up)
                p.cultivation += E.MERGE_CULT
                merged_n += 1
                did = True
                break                                # recompute pool/pairs (cascade)
        if not did:
            return merged_n


def _ctx_score(net, st) -> float:
    """Context-only logit: score the padding card (index 0 = zero embedding), so
    only the state drives it — a cheap learned 'do it now?' head reusing the
    CardPolicyNet machinery (trains with the same {available:[0], chosen} rows)."""
    return float(_pn().score_cards(net, st, [0])[0])


def maybe_push_breakthrough(env, p, card_net=None, push_net=None,
                            explore: float = 0.0, rec=None):
    """The R8 pro pattern (user): EAT part of the board (炼化 board cards) to
    cross the next realm gate NOW — the breakthrough fate then refills the board
    with next-phase cards. Eligible when the cult gap to the next realm is ≤ half
    the board. WHEN to do it is learned (push_net context head); explore flips
    coins so the data contains both timings."""
    if p.realm >= 5:
        return False
    board = [c for c in p.board if c]
    if len(board) < 4:
        return False
    gap = E.CULT_REQ.get(p.realm + 1, 1 << 30) - p.cultivation
    eat_max = len(board) // 2
    if gap <= 0 or gap > eat_max:
        return False                                  # auto-break covers gap<=0
    st = EV.decision_state(env, p)
    rng = env.state.rng
    if explore > 0 and rng.random() < 0.5:
        pushed = rng.random() < 0.5                   # explore both timings
    elif push_net is not None:
        pushed = _ctx_score(push_net, st) > 0
    else:
        pushed = env.state.round >= 7                 # bootstrap: the ~R8 pattern
    if rec is not None:
        rec.setdefault("push", []).append({"pid": p.pid, "state": st,
                                           "available": [0],
                                           "chosen": [0] if pushed else []})
    if not pushed:
        return False
    if card_net is not None:                          # eat the LEAST valuable cards
        v = _values(card_net, st, board, board + list(p.hand))
        order = sorted(range(len(board)), key=lambda i: v[i])
    else:
        order = sorted(range(len(board)), key=lambda i: _phase(env, p, board[i]))
    for i in order[:gap]:
        env.absorb_board(p, board[i])
    env.try_breakthrough(p)                           # break now → fate → refill
    return True


# ── the composed agent policy ─────────────────────────────────────────────────
def make_agent_policy(place_net, roll_net=None, hold_net=None, explore: float = 0.0,
                      heuristic: bool = False, rec=None, search=None, card_net=None,
                      push_net=None, spend_net=None, order: bool = False,
                      deep_order: bool = True, template=None):
    """Full prep policy. roll_net/hold_net None → no rolls / absorb-all unless
    heuristic=True (scripted strategy) or explore flips coins. rec: dict of lists
    ('roll'/'hold'/'place'/'push'/'spend'/'value') — every decision appended as
    {pid, state, available, chosen} for AWR training. search=(k, cap): place with
    the ORACLE SEARCH vs env.field instead of place_net — the grounded expert.
    card_net: a card_value net → roll/hold are COMPUTED from per-card values +
    the known pool (cv_roll/cv_hold) — the 'learn what to look for' mode.
    push_net/spend_net: learned context heads for WHEN to eat-the-board-and-break
    and WHEN to dump the roll bank vs keep banking. template: callable rnd →
    set of BASE ids (a real build to fish toward) — EXPLORATION ONLY: greedy
    single-card fishing can never assemble a combo (a lone 汇灵 without its
    云剑 chain values low and gets rolled away), so template games collect a
    real build's pieces and field them; the Oracle grades the result honestly
    and the value net learns combos from first-person outcomes."""

    def policy(env, p):
        rng = env.state.rng
        tpl = template(env.state.round) if template is not None else None

        # ── 0) breakthrough push? (eat board → break → fate refills) ──
        maybe_push_breakthrough(env, p, card_net=card_net, push_net=push_net,
                                explore=explore, rec=rec)
        slots = E.unlocked_slots(env.state.round)

        # ── 1) 换牌 rolls (before placement) ──
        if p.hand:
            st = EV.decision_state(env, p)
            hand0 = list(p.hand)
            if card_net is not None:
                # SEQUENTIAL fishing (roll → look → roll again, optimal stopping)
                # — executes its own rolls; how-much is emergent from per-charge
                # expected-improvement vs the banking premium.
                rolled = cv_fish(env, p, card_net, protect=tpl)
                if explore > 0 and p.hand and p.rerolls > 0:       # data diversity
                    for _ in range(2):
                        if rng.random() < explore and p.hand and p.rerolls > 0:
                            cid = p.hand[rng.randrange(len(p.hand))]
                            if env.reroll(p, cid) is not None or cid not in p.hand:
                                rolled.append(cid)
            else:
                if heuristic:
                    roll_list = heur_roll(env, p)
                elif roll_net is not None:
                    sc = _pn().score_cards(roll_net, st, hand0)
                    ranked = sorted(zip(hand0, sc), key=lambda t: -t[1])
                    roll_list = [c for c, s in ranked if s > 0]
                else:
                    roll_list = []
                if explore > 0:                   # per-card ε flip (bounded later)
                    keep = [c for c in hand0 if c not in roll_list]
                    roll_list = [c for c in roll_list if rng.random() > explore] + \
                                [c for c in keep if rng.random() < explore]
                rolled = []
                for cid in roll_list:
                    if p.rerolls <= 0:
                        break
                    if env.reroll(p, cid) is not None or cid not in p.hand:
                        rolled.append(cid)
            if rec is not None:
                rec.setdefault("roll", []).append({"pid": p.pid, "state": st,
                                    "available": hand0, "chosen": rolled})
            _forced_spend_down(env, p, card_net)    # 25-cap rule (after choices)

        # ── 1.5) EXPLICIT merges — an ACTION decided BEFORE the search (real
        # boards keep duplicates unmerged on purpose; fuse only when V(merged)
        # + slot-filler beats the two copies). +1 cult per fuse, in place.
        decide_merges(env, p, card_net=card_net, explore=explore, protect=tpl)

        # ── 2) placement (learned net, or the Oracle search vs env.field) ──
        board_ids = [c for c in p.board if c]
        if search is not None:
            import placement as P
            k, cap = search
            me = p.to_fixture(slots)
            # OPPONENT-AWARE: the next battle's opponent is KNOWN when one other
            # player is alive (duels) — their round-open snapshot (= last fielded
            # board + stats). Score candidates against THEM, blended with field
            # samples (they'll change some cards; the blend guards staleness).
            others = [q for q in env.state.players if q.alive and q.pid != p.pid]
            # GHOST duels: the true opponent is the real trajectory, not the
            # other model seat — the runner publishes its last fielded board.
            known = getattr(env, "ghost_known", None)
            if known is None and len(others) == 1:
                known = getattr(env, "round_open_fixtures", {}).get(others[0].pid)
            if known is not None:
                n_field = max(1, k - 2)
                opps = [known, known] + env.field.sample(env.state.round, n_field, rng)
            else:
                opps = env.field.sample(env.state.round, k, rng)
            presc = None
            if card_net is not None:              # net-prune: Oracle only the top few
                st_pl = EV.decision_state(env, p)

                def presc(cands):
                    """SIZE-STRATIFIED prune: the net's board score is a MEAN of
                    card values, so small boards of good cards always out-mean
                    big boards — comparing across sizes with it shrank boards to
                    2 cards. Prune within the largest size (top-4) + best-other
                    (top-2) + the anchor, and let the ORACLE judge across sizes
                    (it knows the real dilution/size tradeoff)."""
                    import numpy as _np
                    import card_value as CV
                    sc = CV.board_scores(card_net, st_pl, [m for _, m in cands])
                    maxlen = max(len(m) for _, m in cands)
                    big = [i for i, (_r, m) in enumerate(cands) if len(m) == maxlen]
                    rest = [i for i in range(len(cands)) if i not in big]
                    keep = sorted(big, key=lambda i: -sc[i])[:4] + \
                           sorted(rest, key=lambda i: -sc[i])[:2] + [0]
                    return [cands[i] for i in sorted(set(keep))]
            extra = None
            if tpl:
                # forced template candidates, Oracle-graded past the prescreen:
                # (1) PURE template pieces (普攻-padded) — a real build is a
                #     coherent whole; junk filler breaks 连云-style chains and
                #     made engine attempts score 0.30 vs the real 0.64, teaching
                #     the net the wrong lesson; (2) pieces topped up with the
                #     best of the rest — fielded once either truly wins.
                avail = board_ids + list(p.hand)
                lvl = lambda c: (c // 10000) % 100
                tp = sorted([c for c in avail if _base_id(c) in tpl], key=lvl,
                            reverse=True)
                rest = sorted([c for c in avail if _base_id(c) not in tpl],
                              key=lvl, reverse=True)
                ok = P._oracle()._concon_ok
                pure, tb = [], []
                for c in tp:
                    if len(pure) < slots and ok(pure + [c], (2, 2, 2)):
                        pure.append(c)
                tb = list(pure)
                for c in rest:
                    if len(tb) >= slots:
                        break
                    if ok(tb + [c], (2, 2, 2)):
                        tb.append(c)
                if tp:
                    extra = [pure, tb] if len(pure) >= 3 else [tb]
            out = P.best_board(me, board_ids, list(p.hand), slots, opps,
                               rnd=env.state.round, cap=cap, automerge=False,
                               prescreen=presc, order=order,
                               deep_order=deep_order, extra_sets=extra)
            board, raw_used = out["board"], out["raw_used"]
            if rec is not None:
                st_rec = EV.decision_state(env, p)
                rec.setdefault("place", []).append({"pid": p.pid, "state": st_rec,
                                     "available": board_ids + list(p.hand),
                                     "chosen": list(raw_used)})
                # COUNTERFACTUAL candidates: the search Oracle-scored 5-7 boards
                # in THIS state — same-state contrasts train the value net far
                # faster than battle outcomes alone (which carry opponent noise).
                for mb, ml, _wr in out.get("scored", []):
                    if mb:
                        import card_value as CVAL2
                        rec.setdefault("cand", []).append(
                            {"pid": p.pid, "state": st_rec, "cards": list(mb),
                             "target": CVAL2.margin_target(ml, env.state.round)})
        else:                                        # net path still automerges
            board, raw_used = EV.learned_board(env, p, place_net, slots)
            p.cultivation += M.merge_gain(raw_used) * E.MERGE_CULT
        p.board = board + [0] * (8 - len(board))
        consumed = list(raw_used)
        for c in board_ids:
            if c in consumed:
                consumed.remove(c)
        for cid in consumed:
            if cid in p.hand:
                p.hand.remove(cid)
        displaced = list(board_ids)                  # board cards the new board
        for c in raw_used:                           # DROPPED go back to hand
            if c in displaced:                       # (real DISPLACE — nothing
                displaced.remove(c)                  # vanishes; absorb/hold next)
        p.hand.extend(displaced)

        # ── 3) hold vs absorb (the economy decision) ──
        leftovers = list(p.hand)
        if leftovers:
            st2 = EV.decision_state(env, p)
            if card_net is not None:
                hold = cv_hold(env, p, card_net, leftovers, protect=tpl)
            elif heuristic:
                hold = heur_hold(env, p, leftovers)
            elif hold_net is not None:
                sc = _pn().score_cards(hold_net, st2, leftovers)
                ranked = sorted(zip(leftovers, sc), key=lambda t: -t[1])
                hold = [c for c, s in ranked if s > 0]
            else:
                hold = []
            if explore > 0:
                keep = [c for c in leftovers if c not in hold]
                hold = [c for c in hold if rng.random() > explore] + \
                       [c for c in keep if rng.random() < explore]
            hold = hold[:10]                      # real hands peak ~5 median; cap
                                                  # blocks the hold-all attractor
            hcnt = Counter(hold)
            for cid in leftovers:
                if hcnt[cid] > 0:
                    hcnt[cid] -= 1                # keep this copy in hand
                else:
                    env.absorb(p, cid)
            if rec is not None:
                rec.setdefault("hold", []).append({"pid": p.pid, "state": st2,
                                    "available": leftovers, "chosen": hold})

        if rec is not None:                       # V baseline sample (post-action)
            rec.setdefault("value", []).append({"pid": p.pid, "state": EV.decision_state(env, p)})
        env.try_breakthrough(p)

    return policy
