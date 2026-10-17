# -*- coding: utf-8 -*-
"""Placement macro-action — pick the best legal board vs the field.

Given the cards a player can commit (current board + hand) and the unlocked slot
count, choose the board (which cards) that maximises expected destiny outcome
against a sample of the field. This is the board sub-decision the RL policy does
NOT learn directly — it's delegated to search (like AlphaZero delegating to a
solver for a sub-game). The learned part is the ECONOMY (which cards to keep for
cultivation, when to break through) that decides WHICH cards reach this search.

Two reuses of the live Oracle search machinery (proxy/oracle_sim):
  · `_my_candidates` — the full card-SET build space (deterministic, unbiased),
  · `_concon_caps`/`_concon_ok` — board legality (≤2 消耗 / ≤2 持续).
All candidates are scored against ONE shared field sample so the comparison is
paired (apples-to-apples), and every (candidate × opponent) pair is batched into a
single parallel Oracle call. Card ORDERING within a set is left canonical for now
(sequencing search is a later refinement — see GAME_MODEL.md).
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent
for _p in (str(_REPO / "proxy"), str(_REPO), str(Path(__file__).resolve().parent)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import merge  # noqa: E402  (selfplay sibling)


def _oracle():
    import oracle_sim
    return oracle_sim


def _default_scorer(pairs, rnd):
    """Exact combat via the Oracle pool. A `scorer` is any callable with this
    signature returning a list of {lifeDamage, win, hpDelta} (or None) per pair —
    swap in battle_score.net_scorer for a fast neural approximation."""
    return _oracle().batch_matchup(pairs, rnd=rnd)


# _my_candidates materialises C(pool, slots) to stride — fine for real in-game
# hands (a few cards) but explodes if the pool is large. Bound the pool so the
# combination count stays sane (C(16,8)=12870) no matter how big a hand grows.
_MAX_POOL = 16
# a set's value depends on its SEQUENCE, so ordering only the unordered-best
# misses qi/combo builds. Rank the top-K sets by their qi-seeded score (cheap),
# then DEEP-order only the top few and pick the winner.
_ORDER_TOPK = 12        # sets to qi-seed-score (rank ordering-dependent builds)
_ORDER_DEEP = 3         # of those, how many to fully deep-order
# pick a couple extra raw cards beyond `slots` so duplicate pairs can MERGE (2→1)
# and the leveled result still leaves room to fill the freed slot.
_MERGE_SLACK = 2

# Tanky punching bag for the ORDERING objective: all-普攻 board, big HP pool —
# my damage into it measures pure loop THROUGHPUT (fuel curve, buff uptime).
_THROUGHPUT_DUMMY = {"characterId": 1000001, "level": 5, "exp": 60,
                     "extraMaxHp": 150, "usedCards": [0] * 8, "unlockGrids": 8,
                     "career": 0, "tipo": 0, "max_tipo": 0, "talents": []}


def candidates(board: list, hand: list, slots: int, cap: int = 24,
               automerge: bool = True) -> list:
    """Legal boards to consider as (raw_used, merged_board) pairs.

    automerge=True (legacy paths): pull up to slots+_MERGE_SLACK raw cards and
    auto-merge duplicate pairs (2×id → id+10000, cascading); over-full results
    are ILLEGAL and discarded (trimming silently vanished cards — the R2
    cult-leak bug). automerge=False (explicit-merge flow): merges were DECIDED
    before the search (econ.decide_merges) — candidates are plain subsets of at
    most `slots` cards, duplicates allowed to stay unmerged (as real boards do)."""
    O = _oracle()
    base = [c for c in board if c]
    hand = [c for c in hand if c]
    room = max(0, _MAX_POOL - len(base))
    hand = hand[:room]                        # STUB: keep first; ideally keep best
    # STRICT caps in self-play (2消耗, 2持续, COMBINED ≤2 — the real rule mined
    # from ~13.7k real boards; (2,2)=4 typed never occurs). No self-calibration
    # here: calibrating from our OWN board would let a rules bug ratchet the cap.
    caps = (2, 2, 2)
    if base or hand:
        # Make the pool LEGAL BY CONSTRUCTION: _my_candidates enumerates only
        # same-size subsets then filters — with a pill-heavy pool (elixirist!)
        # nearly every full-size combo is illegal and candidates starve (the
        # board-ratchet degeneration). Keep at most the COMBINED budget's worth
        # of typed cards in the hand pool (leveled copies first).
        b_nc, b_nt = O._concon(base) if base else (0, 0)
        comb_room = max(0, caps[2] - b_nc - b_nt)
        pills = [c for c in hand if O._concon([c])[0]]
        conts = [c for c in hand if O._concon([c])[1] and c not in pills]
        typed = set(pills) | set(conts)
        pills.sort(key=lambda c: -merge.card_level(c))
        conts.sort(key=lambda c: -merge.card_level(c))
        keep_p = pills[:max(0, min(caps[0] - b_nc, comb_room))]
        keep_t = conts[:max(0, min(caps[1] - b_nt, comb_room - len(keep_p)))]
        hand = [c for c in hand if c not in typed] + keep_p + keep_t
    slack = _MERGE_SLACK if automerge else 0
    budget = min(len(base) + len(hand), slots + slack)
    raw_cands = O._my_candidates(base, hand, budget, cap, caps)
    out, seen = [], set()
    for raw in raw_cands:
        merged = merge.apply_merges(raw) if automerge else list(raw)
        if len(merged) > slots:
            continue
        key = tuple(sorted(merged))
        if merged and key not in seen:
            seen.add(key)
            out.append((list(raw), merged))
    if not out and base:
        base_b = merge.apply_merges(base) if automerge else list(base)
        out = [(list(base), base_b[:slots])]
    return out


def best_ordering(me: dict, board_set: list, opponents: list, rnd: int = 8,
                  deep: bool = True, scorer=None, objective: str = "life") -> tuple:
    """Optimise the SEQUENCE of a fixed card set vs a shared field sample, reusing
    oracle_sim._best_ordering (cyclic hill-climb: rotations + swaps + insertions).
    The board loops 8→1, so combat depends on order; the same set can swing a lot
    between arrangements. Returns (ordered_board, mean_life). Scores every ordering
    against the SAME opponents (paired) and batches the neighborhood via prefetch."""
    O = _oracle()
    score = scorer or _default_scorer
    if len(board_set) < 3 or not opponents:
        return list(board_set), 0.0
    cache: dict = {}
    WIN, TURN_W, MAX_TURNS = 1e6, 50.0, 64.0

    def _val(res):
        """Order value from the Oracle results. objective='win_fast' → win-rate
        ≫ kill-speed (fewer turns among full wins) ≫ 命 margin, matching the set
        objective so the ARRANGEMENT is also chosen to win most / kill fastest.
        Else mean 命 margin.

        The margin term ADDS mean hpDelta to mean lifeDamage: lifeDamage (destiny
        dealt) is the true round objective but it SATURATES — meaningfully
        different arrangements score within ~1 of each other, a gradient too weak
        for the hill-climb to climb (and inside single-sample noise), so ordering
        stalled at a local optimum (verified: a qi source left AFTER its sinks
        cost 10 hpDelta but only 1 lifeDamage — the search couldn't feel it).
        hpDelta (combat dominance) moves ~10x more per arrangement, giving the
        search a real gradient while staying below the speed term's precedence."""
        lifes, hpds, turns, wins, n = [], [], [], 0, 0
        for r in res:
            if not r:
                continue
            n += 1
            lifes.append(float(r.get("lifeDamage", 0) or 0))
            hpds.append(float(r.get("hpDelta", 0) or 0))
            turns.append(float(r.get("turns", MAX_TURNS) or MAX_TURNS))
            if r.get("win"):
                wins += 1
        if n == 0:
            return -1e9
        margin = (sum(lifes) + sum(hpds)) / n        # lifeDamage + hpDelta gradient
        if objective == "win_fast":
            wr = wins / n
            speed = (MAX_TURNS - sum(turns) / n) * TURN_W if wr >= 1.0 - 1e-9 else 0.0
            return wr * WIN + speed + margin
        return margin

    def _mean_life(order):
        me_c = {**me, "usedCards": list(order)}    # ONE object per order so a
        res = score([(me_c, op) for op in opponents], rnd)   # repeated (weighted)
        return _val(res)                            # opponent dedupes in the batch

    def _static_terms(order):
        """Deterministic order-quality terms layered on the Oracle score, with
        strict precedence: QI feasibility (2.5/stall + 0.5/shortfall — a stalled
        arrangement must be clearly beaten, chosen only if nothing else works)
        >> real-play SLOT BIAS (≤0.8 — breaks plateaus the sampled opponents
        can't differentiate; ordering-only data, never trains the net)."""
        try:
            import qi as QI
            import bias as BIAS
            n, short = QI.stall_count(order)
            return -2.5 * n - 0.5 * short + 0.8 * BIAS.order_score(list(order))
        except Exception:
            return 0.0

    def score_order(order):
        key = tuple(order)
        if key not in cache:
            cache[key] = _mean_life(order)
        return cache[key] + _static_terms(key)

    def prefetch(orders):
        todo = [o for o in orders if tuple(o) not in cache]
        if not todo:
            return
        pairs, spans = [], []
        for o in todo:
            s = len(pairs)
            me_c = {**me, "usedCards": list(o)}    # one object per order (dedupe)
            for op in opponents:
                pairs.append((me_c, op))
            spans.append((tuple(o), s, len(pairs)))
        res = score(pairs, rnd)
        for key, s, e in spans:
            cache[key] = _val(res[s:e])

    ordered, val = O._best_ordering(list(board_set), score_order, deep=deep,
                                    prefetch=prefetch)
    return ordered, val


def best_board(me: dict, board: list, hand: list, slots: int, opponents: list,
               rnd: int = 8, cap: int = 24, objective: str = "life",
               order: bool = False, scorer=None, automerge: bool = True,
               prescreen=None, deep_order: bool = True, extra_sets=None) -> dict:
    """Search boards built from board+hand and return the best vs `opponents`.

    me: my fixture WITHOUT usedCards (characterId/level/exp/unlockGrids/…).
    Returns {board, raw_used, score, winrate, n_cand, evaluated}: board = chosen
    MERGED id-list (for battle); raw_used = physical cards consumed from board+hand
    (for the env to update the hand). objective: 'life' (mean destiny margin) or
    'winrate'. No opponents (cold field) → first candidate unscored so play proceeds."""
    cands = candidates(board, hand, slots, cap=cap, automerge=automerge)
    if prescreen is not None and len(cands) > 6:
        cands = prescreen(cands)                  # net-ranked top-M: Oracle only
    if extra_sets:
        # FORCED candidates (template exploration): bypass the prescreen so the
        # Oracle honestly scores them every time — a half-assembled engine that
        # the net (rightly) ranks low still yields a counterfactual row, and
        # gets FIELDED the moment it actually outscores the alternatives.
        O_ = _oracle()
        seen = {tuple(sorted(m)) for _, m in cands}
        for xs in extra_sets:
            xs = [c for c in xs if c][:slots]
            if xs and tuple(sorted(xs)) not in seen \
                    and O_._concon_ok(xs, (2, 2, 2)):
                cands.append((list(xs), list(xs)))
    if not cands:
        return {"board": [], "raw_used": [], "score": 0.0, "winrate": 0.0,
                "n_cand": 0, "evaluated": False}
    if not opponents:
        raw, merged = cands[0]
        return {"board": merged, "raw_used": raw, "score": 0.0, "winrate": 0.0,
                "n_cand": len(cands), "evaluated": False}

    score = scorer or _default_scorer
    O = _oracle()
    pairs, spans = [], []                          # spans[i] = (start, end) in pairs for cand i
    for raw, merged in cands:
        me_c = {**me, "usedCards": O._pad_slots(merged, slots)}   # 0s = 普攻 slots
        start = len(pairs)
        for op in opponents:
            pairs.append((me_c, op))
        spans.append((start, len(pairs)))
    res = score(pairs, rnd)

    # win_fast objective (like live_best_lines): WIN-rate first, then among
    # GUARANTEED wins the tie-break is kill SPEED (fewer turns) — a fast clean
    # kill is robust; squeezing extra 命 out of an already-won matchup picks
    # fragile greed-lines that lose when the opponent prediction is off. Layered
    # scalar: WIN (1e6) ≫ speed bonus (≤3200) ≫ 命 margin (±60).
    WIN, TURN_W, MAX_TURNS = 1e6, 50.0, 64.0

    def _score(res_slice):
        lifes, turns, wins, n = [], [], 0, 0
        for r in res_slice:
            if not r:
                continue
            n += 1
            lifes.append(float(r.get("lifeDamage", 0) or 0))
            turns.append(float(r.get("turns", MAX_TURNS) or MAX_TURNS))
            if r.get("win"):
                wins += 1
        if n == 0:
            return None
        ml, mt, wr = sum(lifes) / n, sum(turns) / n, wins / n
        if objective == "win_fast":
            speed = (MAX_TURNS - mt) * TURN_W if wr >= 1.0 - 1e-9 else 0.0
            return wr * WIN + speed + ml, wr, ml
        if objective == "winrate":
            return wr, wr, ml
        return ml, wr, ml

    cand_val = []                    # (val, wr, i) per candidate — UNORDERED
    scored = []                      # (board, mean_life, wr) — same-state contrasts
    for i, (s, e) in enumerate(spans):
        sc = _score(res[s:e])
        if sc is None:
            continue
        val, wr, ml = sc
        scored.append((list(cands[i][1]), ml, wr))
        cand_val.append((val, wr, i))

    def _seed(merged):
        """qi-feasible seed order (fuel before consumers) + real-play slot bias —
        so a qi-engine set isn't judged in a stalled default order."""
        padded = O._pad_slots(list(merged), slots)
        try:
            import qi as QI
            import bias as BIAS
            cards = [c for c in padded if c]
            pads = [0] * (len(padded) - len(cards))
            cards.sort(key=lambda c: (BIAS.bias_pos(c) or (0.5, 0))[0])
            return QI.qi_repair(cards) + pads
        except Exception:
            return padded

    if not cand_val:
        raw, merged = cands[0]
        return {"board": list(merged), "raw_used": list(raw), "score": 0.0,
                "winrate": 0.0, "n_cand": len(cands), "evaluated": False,
                "scored": scored}

    cand_val.sort(reverse=True)
    if not order:
        best_val, best_wr, best_i = cand_val[0]
        raw, merged = cands[best_i]
        return {"board": list(merged), "raw_used": list(raw),
                "score": float(best_val), "winrate": best_wr,
                "n_cand": len(cands), "evaluated": True, "scored": scored}

    # ORDER the top-K candidate SETS, not just the unordered winner: a set's true
    # value depends on its SEQUENCE (a qi engine like 巨虎灵剑 is worthless in
    # default order but wins once ordered after its qi source), so the unordered
    # score can't rank ordering-dependent builds — ordering only the single
    # unordered-best silently dropped every combo board. Seed each with a
    # qi-feasible order first so the top-K genuinely covers them.
    # RANK the top-K sets by their qi-SEEDED board score (cheap: one batch each,
    # no ordering climb) — the seed is fuel-feasible so a qi/combo build reveals
    # its value here instead of scoring 0 in default order. Then DEEP-ORDER only
    # the few best seeded sets and pick the winner. (Ordering all of them was
    # correct but 25s; this is a few seconds with the same result.)
    K = min(len(cand_val), _ORDER_TOPK)
    seeded = []
    for _v, _wr, i in cand_val[:K]:
        raw_i, merged_i = cands[i]
        seed = _seed(merged_i)
        rr = score([({**me, "usedCards": O._pad_slots(seed, slots)}, op)
                    for op in opponents], rnd)
        sc = _score(rr)
        if sc:
            seeded.append((sc[0], seed, list(raw_i), sc[1]))
    seeded.sort(key=lambda t: t[0], reverse=True)

    best_val, board_out, raw, best_wr = None, None, None, cand_val[0][1]
    for sval, seed, raw_i, swr in seeded[:_ORDER_DEEP]:
        ordered, oval = best_ordering(me, list(seed), opponents, rnd=rnd,
                                      scorer=scorer, deep=deep_order,
                                      objective=objective)
        if best_val is None or oval > best_val:
            best_val, board_out, raw = oval, ordered, raw_i
            rr = score([({**me, "usedCards": O._pad_slots(ordered, slots)}, op)
                        for op in opponents], rnd)
            wsc = _score(rr)
            best_wr = wsc[1] if wsc else swr
    if board_out is None:                            # ordering all failed → seeded best
        best_val, seed, raw, best_wr = (seeded[0][0], seeded[0][1],
                                        seeded[0][2], seeded[0][3]) if seeded \
            else (cand_val[0][0], list(cands[cand_val[0][2]][1]),
                  list(cands[cand_val[0][2]][0]), cand_val[0][1])
        board_out = list(seed)
    return {"board": board_out, "raw_used": list(raw), "score": float(best_val or 0.0),
            "winrate": best_wr, "n_cand": len(cands), "evaluated": True,
            "scored": scored}


if __name__ == "__main__":
    import random
    O = _oracle(); O.warmup(); O._get_pool()
    rng = random.Random(0)
    me = {"characterId": 1000001, "level": 3, "exp": 20, "unlockGrids": 6}
    board = [1, 4]
    hand = [5, 6, 7, 3, 2]
    opponents = [{"characterId": 2000001, "level": 3, "exp": 20,
                  "usedCards": c, "unlockGrids": 6}
                 for c in ([4000003, 4000019], [4000019, 4000003, 1], [1, 4, 5, 6])]
    out = best_board(me, board, hand, slots=6, opponents=opponents, rnd=8, cap=20)
    print(f"candidates: {out['n_cand']}  chosen board: {out['board']}")
    print(f"score(mean life): {out['score']:.2f}  winrate: {out['winrate']:.2f}")
    base_out = {"usedCards": board}
    print("baseline board (current):", board)
