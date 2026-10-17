# -*- coding: utf-8 -*-
"""econ9 — the season-9 DATA-DRIVEN agent (user design, 2026-07-22).

Two real-data models + real-data schedules; no self-play training anywhere:
  · VALUE net (real9_card.pt)  — what a card/board is worth, trained on real
    牧逸风+炼丹师 battle outcomes. Drives WHICH card to roll away, the merge
    decision, and the placement prescreen.
  · HOLD net (real9_hold.pt)   — which cards real players keep for later.
    Protects fishing targets and decides the end-of-round hold/absorb.
  · ROLL AMOUNT = the real median rolls-left curve per round (season9 site
    data, ~520 weighted games): spend down to the round's median unless the
    hand is already high-value (then STOP and bank — user rule). R13+ the
    target is 0 (dump everything).
  · BREAKTHROUGH = the real median realm curve: push (eat the board) when
    behind it and the gate is within reach.
  · FATES = the real pick table per phase slot (云海连绵 at phase 3 in 76% of
    real games — the data recovers the sandbox gate on its own).
Placement stays the Oracle search (opponent-aware, bias+qi ordering); battles
run under random 0-99 battleParams (oracle_sim.RANDOM_PARAMS).
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import econ as EC
import economy as E
import env as EV
import fates as FA
import merge as M
# NOTE: no policy_net import here — it drags in torch, which can fail to load
# (WinError 1455) and then blocks the LIVE bot's whole brain for minutes.

HI_STOP_USE = 0.25    # min hand usage-share above which rolling stops (bank)
HOLD_USE = 0.12       # future usage-share above which a leftover is held

# THE TARGET BOARD (user, 2026-07-22) — the 龙瑶 archetype to hunt:
# 云剑·游龙 月影 闪风×2 唤雨 飞灵闪影剑 巨鲲灵剑 流云乱剑. Cards here are
# never rolled away, held unconditionally, exempt from merging when the build
# wants multiple copies, and force-fielded as an Oracle candidate.
TARGET = Counter({1000042: 1,   # 云剑·游龙
                  1000040: 1,   # 云剑·月影
                  1000039: 2,   # 云剑·闪风 ×2
                  15: 1,        # 云剑·唤雨 (phase-4 fate grant)
                  1000043: 1,   # 飞灵闪影剑
                  1000036: 1,   # 巨鲲灵剑
                  1000037: 1})  # 流云乱剑
HUILING = 1000063     # 云剑·汇灵 — the qi BRIDGE: kept until 飞灵闪影剑 shows
FEILING = 1000043


def _base(c):
    return c - ((c // 10000) % 100) * 10000


def _target_set(p):
    """The live protect set: TARGET bases + 汇灵 while 飞灵闪影剑 is missing."""
    t = set(TARGET)
    have_feiling = any(_base(c) == FEILING for c in list(p.board) + list(p.hand) if c)
    if not have_feiling:
        t.add(HUILING)
    return t


def _mk_usage(meta):
    """usage[round][base] = share of real boards fielding the card that round
    (user: WHAT to play comes from analysis, not the value model)."""
    return {int(rn): {int(b): float(s) for b, s in d.items()}
            for rn, d in (meta.get("usage") or {}).items()}


def _use(usage, rnd, base, horizon=0):
    """Best real usage-share of `base` over rounds rnd..rnd+horizon."""
    s = 0.0
    for rr in range(rnd, rnd + horizon + 1):
        s = max(s, usage.get(min(16, rr), {}).get(base, 0.0))
    return s


def _roll_schedule(env, p, usage, needed, target: int):
    """Spend charges down to the round's real-median target. `needed` = the
    multiset of cards the CALCULATOR would field this round (pre-placement
    pass) — those are never rolled; nor are target pieces or merge material.
    Among the rest, roll the card with the LOWEST real usage-share (now..+2).
    Stops early when every rollable card is genuinely popular (bank — the
    user rule); always uses the 云雾变幻 free roll."""
    rnd = env.state.round
    guard = 0
    while p.hand and guard < 30:
        innate_free = (EV.YiXianEnv.FREE_ROLL_FATE in p.talents
                       and not p.free_roll_used)
        if p.rerolls <= max(0, target) and not innate_free:
            break
        if p.rerolls <= 0 and not innate_free:
            break
        cnt = EC._pair_counts(p)
        tgt = _target_set(p)
        need = Counter(needed)
        cands = []
        for c in list(p.hand):
            if need.get(c, 0) > 0:
                need[c] -= 1
                continue                              # the calculator plays it
            if _base(c) in tgt:
                continue                              # the hunt — never rolled
            if cnt[c] >= 2 and M.can_level(c):
                continue                              # merge material — never
            cands.append((_use(usage, rnd, _base(c), 2), c))
        if not cands:
            break
        u_min, worst = min(cands)
        if u_min > HI_STOP_USE and not innate_free:
            break                                     # hand is all real-meta — bank
        if env.reroll(p, worst) is None and worst not in p.hand:
            break                                     # bag exhausted
        guard += 1


def realm_target(rnd: int) -> int:
    """The breakthrough SCHEDULE (user): 境3 by round 5, 境4 by round 7 (pulled
    up from 8 — phase-4 cards early), 境5 by round 11."""
    if rnd >= 11:
        return 5
    if rnd >= 7:
        return 4
    if rnd >= 5:
        return 3
    if rnd >= 3:
        return 2
    return 1


def _forced_break(env, p, usage, rnd: int):
    """Make the schedule happen: when BEHIND the target realm, cover the cult
    gap by absorbing hand chaff first (lowest real usage), then eating the
    board's least-used cards (keeping ≥2 fielded, target pieces last).
    Executes only when the gap is actually coverable."""
    if p.realm >= realm_target(rnd):
        return False
    gap = E.CULT_REQ.get(p.realm + 1, 1 << 30) - p.cultivation
    if gap <= 0:
        env.try_breakthrough(p)
        return True
    board = [c for c in p.board if c]
    cnt = EC._pair_counts(p)
    tgt = _target_set(p)
    chaff = [c for c in p.hand if not (cnt[c] >= 2 and M.can_level(c))
             and _base(c) not in tgt]
    chaff.sort(key=lambda c: _use(usage, rnd, _base(c), 3))
    eatable = max(0, len(board) - 2)
    if gap > len(chaff) + eatable:
        return False                                  # not coverable this round
    for c in list(chaff)[:gap]:
        env.absorb(p, c)
        gap -= 1
    if gap > 0:
        # eat NON-target, least-used cards first — the hunt survives the break
        order = sorted(range(len(board)),
                       key=lambda i: (_base(board[i]) in tgt,
                                      _use(usage, rnd, _base(board[i]), 3)))
        for i in order[:gap]:
            env.absorb_board(p, board[i])
    env.try_breakthrough(p)
    return True


def _calc_board(env, p, slots, usage, k, cap, order, deep_order, rng):
    """ONE calculator pass: the Oracle search over the cards AVAILABLE (board+
    hand) vs the known opponent + field samples. Usage analysis is only the
    PRESCREEN hint (which candidates get Oracle time) and the TARGET build is
    a forced candidate — the Oracle decides what is actually played."""
    import placement as P
    rnd = env.state.round
    board_ids = [c for c in p.board if c]
    me = p.to_fixture(slots)
    tgt = _target_set(p)
    avail = board_ids + list(p.hand)
    lvl = lambda c: (c // 10000) % 100
    want = Counter(TARGET)
    if HUILING in tgt:
        want[HUILING] = 1
    tb, rest = [], []
    for c in sorted(avail, key=lvl, reverse=True):
        b = _base(c)
        if want.get(b, 0) > 0:
            tb.append(c)
            want[b] -= 1
        else:
            rest.append(c)
    extra = None
    if len(tb) >= 3:
        ok = P._oracle()._concon_ok
        filled = list(tb[:slots])
        for c in rest:
            if len(filled) >= slots:
                break
            if ok(filled + [c], (2, 2, 2)):
                filled.append(c)
        extra = [tb[:slots], filled]
    others = [q for q in env.state.players if q.alive and q.pid != p.pid]
    known = getattr(env, "ghost_known", None)
    if known is None and len(others) == 1:
        known = getattr(env, "round_open_fixtures", {}).get(others[0].pid)
    if known is not None:
        opps = [known, known] + env.field.sample(rnd, max(1, k - 2), rng)
    else:
        opps = env.field.sample(rnd, k, rng)

    def presc(cands):
        def us(m):
            return sum(_use(usage, rnd, _base(c)) for c in m) / max(1, len(m))
        scs = [us(m) for _r, m in cands]
        maxlen = max(len(m) for _r, m in cands)
        big = [i for i, (_r, m) in enumerate(cands) if len(m) == maxlen]
        other = [i for i in range(len(cands)) if i not in big]
        keeps = sorted(big, key=lambda i: -scs[i])[:4] + \
            sorted(other, key=lambda i: -scs[i])[:2] + [0]
        return [cands[i] for i in sorted(set(keeps))]

    return P.best_board(me, board_ids, list(p.hand), slots, opps,
                        rnd=rnd, cap=cap, automerge=False,
                        prescreen=presc, order=order, deep_order=deep_order,
                        extra_sets=extra)


def make_real9_policy(meta, k: int = 6, cap: int = 14,
                      order: bool = True, deep_order: bool = False):
    rolls_med = {int(r): int(v) for r, v in meta["rolls_median"].items()}
    usage = _mk_usage(meta)

    def policy(env, p):
        rng = env.state.rng
        rnd = env.state.round
        slots = E.unlocked_slots(rnd)

        # 1) breakthrough FIRST (user rule) — the new phase's pool must be
        # unlocked before this round's rolls fish from it. Schedule: 境3/4/5
        # by rounds 5/8/11.
        _forced_break(env, p, usage, rnd)

        # 2) PRE-PASS: ask the calculator what it would play from the current
        # hand — those cards are "needed"; everything else is roll fodder
        pre = _calc_board(env, p, slots, usage, k, cap, order=False,
                          deep_order=False, rng=rng)
        needed = list(pre.get("raw_used") or [])

        # 3) rolls to the real median schedule (R13+ → 0: dump the bank),
        # rolling only cards the calculator does NOT need
        target = 0 if rnd >= 13 else rolls_med.get(rnd, 0)
        _roll_schedule(env, p, usage, needed, target)
        EC._forced_spend_down(env, p, None)           # 25-cap rule

        # 4) merges (binding heuristic; multi-copy TARGET bases like 闪风×2
        # stay unmerged — the build wants the copies, not the level)
        EC.decide_merges(env, p, card_net=None,
                         protect={b for b, n in TARGET.items() if n >= 2})

        # 5) FINAL calculator pass on the improved hand (with ordering)
        board_ids = [c for c in p.board if c]
        out = _calc_board(env, p, slots, usage, k, cap, order=order,
                          deep_order=deep_order, rng=rng)
        board, raw_used = out["board"], out["raw_used"]
        p.board = board + [0] * (8 - len(board))
        consumed = list(raw_used)
        for c in board_ids:
            if c in consumed:
                consumed.remove(c)
        for cid in consumed:
            if cid in p.hand:
                p.hand.remove(cid)
        displaced = list(board_ids)
        for c in raw_used:
            if c in displaced:
                displaced.remove(c)
        p.hand.extend(displaced)                      # DISPLACE back to hand

        # 6) hold/absorb: TARGET pieces unconditionally, then cards real
        # players still field in the coming rounds (usage analysis)
        leftovers = list(p.hand)
        if leftovers:
            tgt2 = _target_set(p)
            keep_t = [c for c in leftovers if _base(c) in tgt2]
            other = [c for c in leftovers if _base(c) not in tgt2]
            ranked = sorted(other, key=lambda c: -_use(usage, rnd + 1, _base(c), 3))
            hold = (keep_t + [c for c in ranked
                              if _use(usage, rnd + 1, _base(c), 3) >= HOLD_USE])[:10]
            hcnt = Counter(hold)
            for cid in leftovers:
                if hcnt[cid] > 0:
                    hcnt[cid] -= 1
                else:
                    env.absorb(p, cid)

        env.try_breakthrough(p)

    return policy


def make_dao_chooser():
    """道韵 pick priority (user): 月影 > 游龙 > 闪风 > 巨鲲 > 自在随心."""
    PRIO = [1000040, 1000042, 1000039, 1000036]

    def chooser(env, p, options):
        for want in PRIO:
            if want in options:
                return want
        return 0                                     # 自在随心: draw 1 now

    return chooser


def make_fate_chooser(meta, char_id=None):
    """GROUP-FIRST fate picks (user rule): fates split into three groups —
    INNATE (this character's own fates), CULTIVATION, OTHER (wiki categories).
    A single innate fate can top the raw pick table while the cultivation
    group COMBINED is what real players actually favor — so first choose the
    group by its combined real pick share, then the group's most-picked fate
    among the offered ones. Falls through group by group, then random."""
    import json as _json
    from collections import Counter as _Counter
    picks = {int(s): {int(f): int(n) for f, n in d.items()}
             for s, d in meta["fate_picks"].items()}
    cat_map = {}
    try:
        cat_p = _HERE / "data" / "fate_categories.json"   # bundled with the sim package
        cat_map = _json.loads(cat_p.read_text(encoding="utf-8"))
    except Exception:
        pass
    char_fates = set()
    try:
        fp = _json.loads((_HERE / "fate_pools.json").read_text(encoding="utf-8"))
        cp = fp.get("char_phase", {}).get(str(char_id)) or {}
        char_fates = {int(v) for v in cp.values()}
        char_fates |= {int(f) for f in fp.get("chars", {}).get(str(char_id)) or []}
    except Exception:
        pass

    def group(f):
        base = f % 10000 if f >= 10000 else f        # version ids → base
        if base in char_fates:
            return "innate"
        return cat_map.get(FA.name(base) or "", None) or "other"

    # user overrides: phases 3 AND 5 pick from the CULTIVATION group — the
    # 修为 ramp funds the R8/R11 breakthroughs; the innates (龙鳞/九霄玲珑镯)
    # are not the plan, but a fate IS selected (skipping was wrong)
    FORCE_GROUP = {3: "cultivation", 5: "cultivation"}
    # MUST-PICK fates (user): 唤雨 (fate 85, phase-4 pool) grants 云剑·唤雨 to
    # hand — a target build piece, so it overrides ALL group logic when offered.
    # Checked at EVERY phase, not just phase 4: live, the 天命 panel is answered
    # right after 突破 fires and the realm push can lag, so p.realm may still
    # read the OLD realm (the race that made it pick a cult fate over 唤雨).
    MUST_FATES = {85}

    def chooser(env, p, offered):
        for f in offered:
            if (f % 10000 if f >= 10000 else f) in MUST_FATES:
                return f                              # 唤雨 — always take it
        phase = max(2, min(5, p.realm))
        tab = picks.get(phase, {})

        def score(f):
            return max(tab.get(f, 0), tab.get(f + 10000 * (phase - 2), 0))

        order = []
        if phase in FORCE_GROUP:
            order.append(FORCE_GROUP[phase])
        gshare = _Counter()
        for f, n in tab.items():
            gshare[group(f)] += n
        order += [g for g, _n in gshare.most_common() if g not in order]
        for g in order:
            cands = [f for f in offered if group(f) == g]
            if cands:
                return max(cands, key=score)
        return FA.choose(offered, env.state.rng)

    return chooser
