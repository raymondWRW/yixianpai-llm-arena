# -*- coding: utf-8 -*-
"""体魄 / physique — body cultivation.

Physique is gained IN COMBAT: certain cards grant [体魄]+N when they resolve, and
it ACCUMULATES across battles (recorded games: body cultivators reach ~90-104 by
realm 5, cap ≈ physique+5). The Oracle runs combat but doesn't report the ending
physique, so we model the accumulation ourselves from the board's physique-granting
cards, and feed the running total back as the fixture's `tipo` (which the Oracle
uses — physique is combat-decisive for body builds).

`_GRANTS` = {base_id: [体魄]+N} for the ~25 flat physique-granting cards (from
combined_cards.json; only real grants '[体魄]+N', not scaling refs like '每有2[体魄]').
A merged (leveled) card grants proportionally more (× level, a reasonable proxy —
exact per-level scaling isn't in our data). # STUB (per-level scaling)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import merge as M

_CARDS = (_HERE.parent / "vendor" / "yisim-master" / "localization" / "1.5.8" /
          "combined_cards.json")
CAP_HEADROOM = 5          # cap sits ~5 above current physique (recorded games)

_grants_cache = None


def _grants() -> dict:
    """{base_id: physique granted per resolution} for flat [体魄]+N cards."""
    global _grants_cache
    if _grants_cache is not None:
        return _grants_cache
    out = {}
    for c in json.loads(_CARDS.read_text(encoding="utf-8")):
        if c.get("level") != 1:
            continue
        m = re.search(r"\[体魄\]\+(\d+)", c.get("desc_cn", "") or "")
        if m:
            out[int(c["card_id"])] = int(m.group(1))
    _grants_cache = out
    return out


def physique_gain(board_ids) -> int:
    """Physique a board grants this battle = Σ over its 体魄 cards ([体魄]+N × level
    for merged copies)."""
    g = _grants()
    total = 0
    for cid in board_ids:
        if not cid:
            continue
        base = int(cid) - (M.card_level(cid) - 1) * 10000
        if base in g:
            total += g[base] * M.card_level(cid)
    return total


def accrue(player, board_ids):
    """After a battle, add the board's physique gain to the player's running 体魄
    and float the cap just above it. Also honours fate 体魄上限 already in max_tipo."""
    gain = physique_gain(board_ids)
    if gain:
        player.tipo += gain
        player.max_tipo = max(player.max_tipo, player.tipo + CAP_HEADROOM)
    return gain


if __name__ == "__main__":
    g = _grants()
    print(f"{len(g)} physique-granting cards")
    import cards as C
    for cid, v in sorted(g.items())[:12]:
        print(f"  {C.id_to_name(cid):8} [体魄]+{v}")
    # a body board
    board = [10000004, 10000006, 10000015, 10010004]   # 锻拳/抱气法/锻筋/锻拳·2
    print("physique_gain(sample body board):", physique_gain(board))
