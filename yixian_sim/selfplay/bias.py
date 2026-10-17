# -*- coding: utf-8 -*-
"""Per-card SLOT BIAS mined from real season-9 play — ordering preference only.

Real players put specific cards in specific parts of the loop (buff engines
early, finishers late, …) — per character+career. We mine, for the sandbox
matchup (牧逸风 + 炼丹师), each card's preferred RELATIVE position (0=first
slot, 1=last) across real boards, and use it as a TIEBREAK when arranging
boards: when combat outcomes plateau, prefer the order that puts the most
cards near their real-play slots.

USER CONSTRAINT: this data steers PLACEMENT/ORDERING only — it is never fed to
the learning (card-value net training does not see it).

    python selfplay/bias.py --mine   # rebuild card_bias.json from the replays
"""
from __future__ import annotations

import json
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_OUT = _HERE / "card_bias.json"
_SRC = _HERE / "data" / "board_sequences.jsonl"   # only needed to re-mine; card_bias.json is bundled

CHAR = 1000001          # 牧逸风
CAREER = 1              # 炼丹师

_bias = None            # base_id(str) -> {"pos": mean relpos, "n": samples}


def _base(cid: int) -> int:
    lv = (int(cid) // 10000) % 100
    return int(cid) - lv * 10000


def mine(min_len: int = 5) -> dict:
    """Scan the replay sequences for CHAR+CAREER games; accumulate each card's
    relative slot position over boards with >= min_len cards."""
    import collections
    acc = collections.defaultdict(list)
    n_games = 0
    with open(_SRC, encoding="utf-8") as f:
        for line in f:
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("char") != CHAR or d.get("career") != CAREER:
                continue
            n_games += 1
            for r in d.get("rounds", []):
                b = r.get("board") or []
                if len(b) < min_len:
                    continue
                for i, cid in enumerate(b):
                    if cid:
                        acc[_base(cid)].append(i / (len(b) - 1))
    out = {str(k): {"pos": sum(v) / len(v), "n": len(v)}
           for k, v in acc.items() if len(v) >= 8}
    _OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"games": n_games, "cards": len(out)}


def _load() -> dict:
    global _bias
    if _bias is None:
        _bias = json.loads(_OUT.read_text(encoding="utf-8")) if _OUT.exists() else {}
    return _bias


def bias_pos(cid: int):
    """(preferred relative position, confidence 0-1) or None if unknown."""
    e = _load().get(str(_base(cid)))
    if not e:
        return None
    return e["pos"], min(1.0, e["n"] / 30.0)


def order_score(ids: list) -> float:
    """How well an arrangement matches real-play slots, in [0,1]: mean over
    known cards of (1 − |relpos − preferred|) × confidence. Pads (0) skipped."""
    cards = [c for c in ids if c]
    if len(cards) < 2:
        return 0.0
    tot = w = 0.0
    for i, c in enumerate(cards):
        bp = bias_pos(c)
        if bp is None:
            continue
        pos, conf = bp
        tot += (1.0 - abs(i / (len(cards) - 1) - pos)) * conf
        w += conf
    return tot / w if w else 0.0


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--mine", action="store_true")
    a = ap.parse_args()
    if a.mine:
        print(mine())
    import sys
    sys.path.insert(0, str(_HERE.parent / "proxy"))
    import cards as C
    b = _load()
    top = sorted(b.items(), key=lambda t: t[1]["pos"])
    print("earliest-slot cards:", [(C.id_to_name(int(k)), round(v["pos"], 2), v["n"]) for k, v in top[:8]])
    print("latest-slot cards:  ", [(C.id_to_name(int(k)), round(v["pos"], 2), v["n"]) for k, v in top[-8:]])
