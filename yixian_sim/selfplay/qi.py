# -*- coding: utf-8 -*-
"""灵气 (qi) economics per card — the fuel curve for board ORDERING.

User-diagnosed failure: 巨鲲灵剑 (qi_cost 3) placed at slot 1 with no income
stalls for turns; 引气剑 ([灵气]+2) first fuels it. The ordering hill-climb only
fixes this when its (possibly stale/weak) objective happens to punish the stall
— but the qi curve is about YOUR OWN loop functioning, opponent-independent. So
we mine each card's qi profile (gain from desc [灵气]+N, cost from the data's
qi_cost field) and SEED the hill-climb with a fuel-feasible order: generators
first, consumers once cumulative income covers them. First-improvement climbing
keeps the seed on ties, so the qi-correct basin survives weak objectives.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

_CC = (Path(__file__).resolve().parent.parent / "vendor" / "yisim-master" /
       "localization" / "1.5.8" / "combined_cards.json")

_profile = None      # card_id -> (qi_gain, qi_cost, is_buff)


def _load() -> dict:
    global _profile
    if _profile is None:
        _profile = {}
        for v in json.loads(_CC.read_text(encoding="utf-8")):
            cid = v.get("card_id")
            if not cid:
                continue
            d = v.get("desc_cn") or ""
            gain = sum(int(m) for m in re.findall(r"\[灵气\]\+(\d+)", d))
            cost = int(v.get("qi_cost") or 0)
            if "耗尽[灵气]" in d or "耗尽灵气" in d:
                cost = max(cost, 4)      # spend-ALL scalers (万法归灵剑): seed them
                                         # AFTER income so their payoff isn't wasted
            # BUFF/AURA engines want maximum uptime → seed them FIRST:
            # [持续] continuous effects (柔心, 百鸟诀) and stacking [加攻] layers
            # (月影's 连云 attack stacks buff every later hit).
            buff = ("[持续]" in d) or ("[加攻]" in d)
            _profile[int(cid)] = (gain, cost, buff)
    return _profile


def qi_gain(cid: int) -> int:
    return _load().get(int(cid), (0, 0, False))[0]


def qi_cost(cid: int) -> int:
    return _load().get(int(cid), (0, 0, False))[1]


def is_buff(cid: int) -> bool:
    return _load().get(int(cid), (0, 0, False))[2]


def seed_order(ids: list) -> list:
    """Uptime-then-fuel arrangement: BUFF/AURA engines first (their layers/effects
    apply to everything after — 月影 last wastes its 加攻 stacks), then walk the
    loop accumulating qi: play a consumer the moment income covers it (dearest
    affordable first), otherwise the best net generator. Zero-cost buffs that
    also generate go up front naturally. 0s (普攻 pads) keep count, at the end."""
    rest = [c for c in ids if c]
    pads = [c for c in ids if not c]
    out, qi = [], 0
    # buffs first — free ones immediately; qi-costed buffs enter the fuel walk
    for c in sorted([c for c in rest if is_buff(c) and qi_cost(c) == 0],
                    key=lambda c: -qi_gain(c)):
        out.append(c)
        qi += qi_gain(c)
        rest.remove(c)
    while rest:
        playable = [c for c in rest if qi_cost(c) <= qi]
        afford = [c for c in playable if qi_cost(c) > 0]
        if afford:
            pick = max(afford, key=qi_cost)          # spend on the biggest payoff
        elif playable:
            pick = max(playable, key=lambda c: qi_gain(c) - qi_cost(c))
        else:
            pick = max(rest, key=lambda c: qi_gain(c) - qi_cost(c))
        out.append(pick)
        rest.remove(pick)
        qi = max(0, qi + qi_gain(pick) - qi_cost(pick))
    return out + pads


def stall_count(ids: list):
    """Static qi-issue detector: walk the arrangement's first pass accumulating
    qi; every consumer arriving with insufficient qi is a STALL (wasted turns).
    Returns (n_stalls, total_shortfall). Pads (0/普攻) are neutral."""
    q, n, short = 0, 0, 0
    for c in ids:
        if not c:
            continue
        cost = qi_cost(c)
        if cost > q:
            n += 1
            short += cost - q
            q = 0
        else:
            q -= cost
        q += qi_gain(c)
    return n, short


def qi_repair(cards: list) -> list:
    """Minimal reordering to remove stalls while PRESERVING the given order as
    much as possible (bias precedence below qi): scan for the first playable
    card (cost ≤ banked qi); if none, play the best net generator."""
    pending = [c for c in cards if c]
    pads = [c for c in cards if not c]
    out, q = [], 0
    while pending:
        pick = next((c for c in pending if qi_cost(c) <= q), None)
        if pick is None:
            pick = max(pending, key=lambda c: qi_gain(c) - qi_cost(c))
        out.append(pick)
        pending.remove(pick)
        q = max(0, q + qi_gain(pick) - qi_cost(pick))
    return out + pads


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "proxy"))
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import cards as C
    for nm in ("引气剑", "巨鲲灵剑", "凝意诀", "剑劈", "震雷剑", "小还丹"):
        b = C.name_to_base_id(nm)
        print(f"  {nm}: gain={qi_gain(b)} cost={qi_cost(b)}  (L2: gain={qi_gain(b+10000)} cost={qi_cost(b+10000)})")
