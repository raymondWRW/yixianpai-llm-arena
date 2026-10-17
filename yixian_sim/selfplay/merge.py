# -*- coding: utf-8 -*-
"""Card merging: two copies of the same card (same level) → one of the next level.

Card ids encode level as `level(id) = ((id//10000)%100)+1`, and the next level of
a card is simply `id + 10000` (same name) — verified for ~99% of multi-level
cards. Some cards have NO upgrade (e.g. 云泉道茶, 七星灯): `id+10000` isn't a real
card, so they can't merge. `level_up` returns None for those.

`apply_merges` takes a multiset of card ids (the cards a player commits) and
repeatedly combines pairs, cascading: 2×L1 → 1×L2, and two of those L2 → 1×L3.
This is what makes holding/drafting duplicates strategic — a merged leveled card
is stronger AND frees a board slot.
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import cards as C

LEVEL_STRIDE = 10000


def card_level(cid: int) -> int:
    return ((int(cid) // LEVEL_STRIDE) % 100) + 1


def level_up(cid: int):
    """Next-level id for a card, or None if it has no upgrade."""
    up = int(cid) + LEVEL_STRIDE
    if C.is_card(up) and C.id_to_name(up) == C.id_to_name(int(cid)):
        return up
    return None


def can_level(cid: int) -> bool:
    return level_up(cid) is not None


def apply_merges(ids) -> list:
    """Combine duplicate pairs (cascading) in a multiset of ids. 0/empty dropped.
    Returns the resulting id list (order not meaningful; caller re-sequences)."""
    cnt = Counter(int(i) for i in ids if i)
    changed = True
    while changed:
        changed = False
        for cid, c in list(cnt.items()):
            if c >= 2:
                up = level_up(cid)
                if up is None:
                    continue
                pairs = c // 2
                cnt[cid] -= pairs * 2
                if cnt[cid] == 0:
                    del cnt[cid]
                cnt[up] += pairs
                changed = True
                break
    out = []
    for cid, c in cnt.items():
        out += [cid] * c
    return out


def merge_gain(ids) -> int:
    """How many cards a merge pass removes (pairs collapsed) — a cheap proxy for
    'does this set have merge potential'."""
    return len([i for i in ids if i]) - len(apply_merges(ids))


if __name__ == "__main__":
    tests = [
        [5, 5],                 # 2xL1 -> 1xL2 (10005)
        [5, 5, 5],              # -> 1xL2 + 1xL1 leftover
        [5, 5, 5, 5],           # -> 2xL2 -> 1xL3 (20005)
        [1, 1],                 # 云泉道茶: no upgrade -> stays [1,1]
        [6, 6, 5, 5, 5],        # mixed
    ]
    for t in tests:
        print(f"  {t} -> {apply_merges(t)}   (names: "
              f"{[C.id_to_name(i) + '·L' + str(card_level(i)) for i in apply_merges(t)]})")
