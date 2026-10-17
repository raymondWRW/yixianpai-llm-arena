# -*- coding: utf-8 -*-
"""claude_policy — a hand-written prep-phase agent for the yixian_sim environment.

Generic plan (guides + mined real-play data, see agents/README):
  1. TEMPO: break through the moment cultivation allows; if behind the real median realm
     schedule (境2@R3, 境3@R5, 境4@R7, 境5@R11) and the gap is coverable, absorb chaff /
     least-valuable board cards to cross the gate BEFORE rolling (new phase → new pool).
  2. ROLL CHAFF ONLY: a pre-pass Oracle search says which cards it would field ("needed");
     exchange the lowest-phase non-needed, non-pair cards. Bank a few charges mid-game
     (R4-9), dump the bank from R10.
  3. BOARD: exact Oracle search over card SETS vs a sample of the field, objective
     WIN ≫ kill-speed ≫ 命 margin, cyclic ordering optimised for the top sets.
  4. HOLD/ABSORB: keep current-phase-or-higher cards and merge pairs (≤ HOLD_MAX),
     absorb the rest for cultivation; absorb extra if that alone crosses a realm gate.

Archetype layer (guide=True, default): 云灵剑宗 seats follow the TapTap 剑意 guide
(jianyi_guide.py) — 练气 stall + core fishing, mid-game reroll bank, 化神 dump, 画师 side
job, 修为/斩道/灵猫乱剑 fate picks; the template board is force-offered to the search.
"""
from __future__ import annotations
import sys
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).resolve().parent
for _p in (_HERE, _HERE.parent / "selfplay", _HERE.parent / "proxy"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import economy as E
import merge as M
import placement as P
import jianyi_guide as JG          # TapTap 剑意 guide archetype (云灵剑宗)

HOLD_MAX = 6
SIDEJOB_BY_SECT = {1: 1, 2: 2, 3: 1, 4: 1}          # 云灵→炼丹师, 七星→符咒师, 五行→炼丹师, 锻玄→炼丹师


def realm_target(rnd: int) -> int:
    if rnd >= 11: return 5
    if rnd >= 7:  return 4
    if rnd >= 5:  return 3
    if rnd >= 3:  return 2
    return 1


def roll_floor(rnd: int) -> int:
    """Charges to keep banked after this round's rolling (generic plan)."""
    if rnd <= 3:  return 0
    if rnd <= 9:  return 3
    return 0                                          # R10+: dump the bank


def _phase(env, p, cid) -> int:
    return env._card_phase(p, cid)


def _pairs(p) -> Counter:
    return Counter([c for c in p.board if c] + list(p.hand))


def _search(env, p, slots, k, cap, order, guide=False):
    board_ids = [c for c in p.board if c]
    opps = env.field.sample(env.state.round, k, env.state.rng, window=1)
    extra = JG.template_sets(p, slots) if guide else None
    return P.best_board(p.to_fixture(slots), board_ids, p.hand, slots, opps,
                        rnd=env.state.round, cap=cap, objective="win_fast",
                        order=order, deep_order=order, extra_sets=extra)


def _apply_board(env, p, out):
    board_ids = [c for c in p.board if c]
    board, raw_used = out["board"], out["raw_used"]
    p.board = board + [0] * (8 - len(board))
    p.cultivation += M.merge_gain(raw_used) * E.MERGE_CULT
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
    p.hand.extend(displaced)


def _chaff(env, p, needed, protect=frozenset()):
    """Hand cards safe to roll/absorb: not needed by the search, not a merge-pair member,
    not a protected archetype base; lowest phase first."""
    need = Counter(needed)
    cnt = _pairs(p)
    out = []
    for c in p.hand:
        if need[c] > 0:
            need[c] -= 1
            continue
        if cnt[c] >= 2 and M.can_level(c):
            continue
        if JG.base(c) in protect:
            continue
        out.append(c)
    out.sort(key=lambda c: (_phase(env, p, c), c))
    return out


def _push_breakthrough(env, p, needed, rnd, protect=frozenset()):
    """Behind schedule → eat chaff (then least-needed board cards) to cross the gate now."""
    if p.realm >= realm_target(rnd) or p.realm >= E.MAX_REALM:
        return env.try_breakthrough(p)
    gap = E.CULT_REQ.get(p.realm + 1, 1 << 30) - p.cultivation
    if gap <= 0:
        return env.try_breakthrough(p)
    chaff = _chaff(env, p, needed, protect)
    board = [c for c in p.board if c]
    eatable = max(0, len(board) - 3)                  # keep at least 3 fielded
    if gap > len(chaff) + eatable:
        return False
    for c in chaff[:gap]:
        env.absorb(p, c); gap -= 1
    if gap > 0:
        order = sorted((c for c in board if JG.base(c) not in protect),
                       key=lambda c: (_phase(env, p, c), c))   # weakest, non-protected first
        for c in order[:gap]:
            env.absorb_board(p, c)
    return env.try_breakthrough(p)


def make_policy(k: int = 6, cap: int = 14, order: bool = True, guide: bool = True):
    def policy(env, p):
        rnd = env.state.round
        slots = E.unlocked_slots(rnd)
        g = guide and JG.applies(p)
        protect = JG.wanted(p, rnd) if g else frozenset()
        cards_all = [c for c in p.board if c] + list(p.hand)

        # 0) pre-pass: what would the search field right now?
        pre = _search(env, p, slots, k=max(2, k // 2), cap=cap, order=False, guide=g)
        needed = list(pre.get("raw_used") or [])

        # 1) tempo — breakthrough before rolling (guide: 练气 stall until core / clock)
        stall = g and not JG.should_break(p, rnd, cards_all)
        if not stall and _push_breakthrough(env, p, needed, rnd, protect):
            pre = _search(env, p, slots, k=max(2, k // 2), cap=cap, order=False, guide=g)
            needed = list(pre.get("raw_used") or [])

        # 2) rolls: generic = chaff down to the floor; guide = all @练气, none mid, all @化神
        budget = JG.roll_budget(p, rnd, p.rerolls) if g else max(0, p.rerolls - roll_floor(rnd))
        for c in _chaff(env, p, needed, protect):
            if budget <= 0:
                break
            if not g and _phase(env, p, c) >= p.realm and rnd >= 4:
                break                                  # current-phase cards: keep, don't burn
            if env.reroll(p, c) is not None:
                budget -= 1

        # 3) final board search with ordering (template force-offered when guided)
        out = _search(env, p, slots, k=k, cap=cap, order=order, guide=g)
        _apply_board(env, p, out)

        # 4) hold / absorb
        cnt = _pairs(p)
        keep = []
        hold_max = HOLD_MAX + (6 if g else 0)
        for c in sorted(p.hand, key=lambda c: (JG.base(c) not in protect, -_phase(env, p, c))):
            good = (JG.base(c) in protect) or (_phase(env, p, c) >= p.realm) \
                or (cnt[c] >= 2 and M.can_level(c))
            if good and len(keep) < hold_max:
                keep.append(c)
        gap = E.CULT_REQ.get(p.realm + 1, 1 << 30) - p.cultivation
        n_absorb = len(p.hand) - len(keep)
        if not stall and 0 < gap <= len(p.hand) and gap > n_absorb and p.realm < E.MAX_REALM:
            keep = keep[: len(p.hand) - gap]           # tempo > hoarding
        kc = Counter(keep)
        for c in list(p.hand):
            if kc[c] > 0:
                kc[c] -= 1
            else:
                env.absorb(p, c)
        if not stall:
            env.try_breakthrough(p)
    return policy


def sidejob_chooser(env, p, guide: bool = True):
    if guide and JG.applies(p):
        return JG.SIDEJOB                              # 画师
    return SIDEJOB_BY_SECT.get(p.sect_prefix, 1)


def fate_chooser(env, p, offered, guide: bool = True):
    if guide and JG.applies(p):
        return JG.fate_chooser(env, p, offered)
    import fates as FA
    return FA.choose(offered, env.state.rng)
