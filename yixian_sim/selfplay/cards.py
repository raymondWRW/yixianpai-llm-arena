# -*- coding: utf-8 -*-
"""Card identity for the offline model: name ⇄ id.

The deal/pool layer (draws.py) works in NAMES — that's how card_phases.json and
the counter's fidelity checks are keyed. The Oracle battle engine works in IDS
(usedCards). This module is the single seam between the two.

Card ids encode name + level: `level(id) = ((id // 10000) % 100) + 1`. A drawn
card is always level-1 (the "base" id); merges level it up (economy.merge_map).
`name_to_base_id` therefore resolves a dealt NAME to its level-1 id.

41 of 901 names map to >1 level-1 id (the shared 普通攻击, plus a handful of
4M/10M derivation twins that share a display name with a real sect card). Default:
the SMALLEST id wins. EXCEPTION (game2 bug: 洗髓丹 resolved to the roguelike card
230 instead of the Elixirist pill 2000012, so its [炼化] read the wrong params):
when a name belongs to a sect/sidejob pool (card_pool.json) and one of its level-1
ids sits in that family's million-block, the POOL id wins — that is the card the
normal deal and the sidejob grants actually produce. The roguelike-mode twins
(小 ids 225-232: 地灵丹/飞云丹/锻体丹/还魂丹/洗髓丹/大还丹/冰灵护体丹…) are never
drawable here.
"""
from __future__ import annotations

import json
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent
_ID_MAP_FILE = _REPO / "proxy" / "card_id_map.json"


def _norm(s: str) -> str:
    return (s or "").replace("•", "·")   # match runtime/draws normalisation


def card_level(cid: int) -> int:
    return ((int(cid) // 10000) % 100) + 1


_id_to_name = None
_name_to_base = None


# million-block per pool family (matches proxy_view's sect/sidejob prefix maps):
# sects 1-4 → 1M/4M/7M/10M; sidejob careers 1-7 → 2M/3M/5M/6M/8M/9M/11M.
_SECT_BLOCK = {"1": 1, "2": 4, "3": 7, "4": 10}
_SIDEJOB_BLOCK = {"1": 2, "2": 3, "3": 5, "4": 6, "5": 8, "6": 9, "7": 11}
_POOL_FILE = Path(__file__).resolve().parent / "card_pool.json"


def _pool_blocks() -> dict:
    """{name: set(million-blocks)} for every name in a sect/sidejob pool."""
    out = {}
    try:
        cp = json.loads(_POOL_FILE.read_text(encoding="utf-8"))
        for key, blocks in (("sects", _SECT_BLOCK), ("sidejobs", _SIDEJOB_BLOCK)):
            for fam, cards in cp.get(key, {}).items():
                blk = blocks.get(str(fam))
                if blk is None:
                    continue
                for nm in cards:
                    out.setdefault(_norm(nm), set()).add(blk)
    except Exception:
        pass
    return out


def _load():
    global _id_to_name, _name_to_base
    if _id_to_name is not None:
        return
    raw = json.loads(_ID_MAP_FILE.read_text(encoding="utf-8"))   # {id(str): name}
    _id_to_name = {int(k): _norm(v) for k, v in raw.items()}
    cands = {}
    for cid, nm in _id_to_name.items():
        if card_level(cid) == 1:
            cands.setdefault(nm, []).append(cid)
    blocks = _pool_blocks()
    base = {}
    for nm, ids in cands.items():
        pool_ids = [i for i in ids if (i // 1_000_000) in blocks.get(nm, ())]
        # a pool-family id beats the roguelike/event twin; otherwise smallest wins
        base[nm] = min(pool_ids) if pool_ids else min(ids)
    _name_to_base = base


def name_to_base_id(name: str):
    """Level-1 id for a dealt card name, or None if unknown (e.g. 走火入魔)."""
    _load()
    return _name_to_base.get(_norm(name))


def id_to_name(cid: int) -> str:
    _load()
    return _id_to_name.get(int(cid), str(cid))


def is_card(cid: int) -> bool:
    _load()
    return int(cid) in _id_to_name


def names_to_ids(names) -> list:
    """Map a hand (names) to base ids, dropping any that don't resolve."""
    out = []
    for n in names:
        i = name_to_base_id(n)
        if i:
            out.append(i)
    return out


if __name__ == "__main__":
    _load()
    print(f"id map: {len(_id_to_name)} ids, {len(_name_to_base)} base names")
    for nm in ("云泉道茶", "七星灯", "走火入魔", "斩草除根"):
        print(f"  {nm!r:>10} -> {name_to_base_id(nm)}")
