# -*- coding: utf-8 -*-
"""Character roster — the 24 playable characters (CharacterConfig.dat).

6 per sect (id prefix 1/2/3/4 → card sect 1/2/3/4, matching draws.SECT_PREFIX_TO_FIELD).
A character choice affects BOTH the draw pool (its sect's cards) and combat (the
Oracle applies character-specific skills from characterId). Falls back to a literal
roster if the config isn't parseable.
"""
from __future__ import annotations

import random
from pathlib import Path

_CONFIGS = Path(__file__).resolve().parent.parent / "oracle" / "data" / "extracted" / "configs"

_FALLBACK = [1000001 + i for i in range(6)] + [2000001 + i for i in range(6)] + \
            [3000001 + i for i in range(6)] + [4000001 + i for i in range(6)]

_roster = None      # list of (id, name, sect)


def _load():
    global _roster
    if _roster is not None:
        return _roster
    out = []
    try:
        import blackboxprotobuf
        msg, _ = blackboxprotobuf.decode_message((_CONFIGS / "CharacterConfig.dat").read_bytes())
        rows = None
        for v in msg.values():
            if isinstance(v, list) and v and isinstance(v[0], dict) and "1" in v[0]:
                rows = v; break
            if isinstance(v, dict):
                for v2 in v.values():
                    if isinstance(v2, list) and v2 and isinstance(v2[0], dict) and "1" in v2[0]:
                        rows = v2; break
        for r in rows or []:
            cid = r.get("1")
            if not isinstance(cid, int):
                continue
            nm = r.get("2")
            name = nm.decode("utf-8", "ignore") if isinstance(nm, (bytes, bytearray)) else str(nm)
            sect = int(r.get("3", cid // 1_000_000) or cid // 1_000_000)
            out.append((cid, name, sect))
    except Exception:
        out = []
    if not out:
        out = [(c, str(c), c // 1_000_000) for c in _FALLBACK]
    _roster = sorted(out)
    return _roster


# Characters excluded from self-play (innates too hard to model faithfully).
EXCLUDED = {3000006, 1000006}   # 祁忘忧 (五行玉瓶), 黎承云 (悟剑天赋: 领悟 3 剑牌)


def roster() -> list:
    return list(_load())


def ids() -> list:
    return [c for c, _, _ in _load() if c not in EXCLUDED]


# ── character vocab (char id → index, for the value net's character embedding) ──
_char_vocab = None


def char_vocab() -> dict:
    global _char_vocab
    if _char_vocab is None:
        _char_vocab = {0: 0}
        for c, _, _ in _load():                    # full roster (stable indices)
            _char_vocab.setdefault(c, len(_char_vocab))
    return _char_vocab


def char_vocab_size() -> int:
    return len(char_vocab())


def char_index(cid: int) -> int:
    return char_vocab().get(int(cid), 0)


def name(cid: int) -> str:
    for c, n, _ in _load():
        if c == cid:
            return n
    return str(cid)


def sample(n: int, rng: random.Random, distinct: bool = True) -> list:
    """n character ids for a game. distinct=True → no repeats when the roster is
    large enough (spreads across sects); else sampled with replacement."""
    pool = ids()
    if distinct and n <= len(pool):
        return rng.sample(pool, n)
    return [pool[rng.randrange(len(pool))] for _ in range(n)]


if __name__ == "__main__":
    r = roster()
    print(f"{len(r)} characters")
    for cid, nm, sect in r:
        print(f"  {cid}  sect{sect}  {nm}")
