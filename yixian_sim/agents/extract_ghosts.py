# -*- coding: utf-8 -*-
"""extract_ghosts.py — pull real AI/bot opponents out of recorded replay shards.

Practice-lobby records in `yixian replay analysis/*.tar.zst` follow a player through a
whole game; every roundStat carries BOTH sides' full state, and bots are flagged with
`publicData.isAI` (uids like `ai3-lv1` — the lv suffix is the bot difficulty tier).
Records where the recorder met the same bot every round give complete round-by-round
bot trajectories: board (cyclic order preserved), realm/exp/extraMaxHp/talents/career.

This script collects those trajectories and writes the strongest ones to
`agents/ghosts.json`, from which `play.py new --ghosts` RANDOMLY seats 7 opponents —
each seat replays its recorded board each round (carry-forward between sightings, and
per the user's rule, past the end of the record the last known state repeats).

User rule (2026-09-04): only bots that REACHED 境5 (phase 5) qualify — keep ~30 of
them as a healthy pool. All *.tar.zst shards in the replay-analysis dir are scanned.

    python agents/extract_ghosts.py [--shard path.tar.zst ...] [--top 30]
"""
from __future__ import annotations

import argparse
import io
import json
import re
import tarfile
from pathlib import Path

_HERE = Path(__file__).resolve().parent
DEFAULT_SHARD = Path(r"C:\Users\raymo\OneDrive\Desktop\yixian replay analysis") / "31767000.tar.zst"
OUT = _HERE / "ghosts.json"
EXCLUDED_CHARS = {3000006, 1000006}      # roster gaps in the sim (innates unmodelled)


def iter_records(shard: Path):
    import zstandard
    dctx = zstandard.ZstdDecompressor()
    with open(shard, "rb") as f, dctx.stream_reader(f) as r:
        tf = tarfile.open(fileobj=io.BufferedReader(r), mode="r|")
        for m in tf:
            if not m.isfile():
                continue
            try:
                d = json.loads(tf.extractfile(m).read())
            except Exception:
                continue
            dd = d.get("data") or d
            if isinstance(dd, dict) and "roundStats" in dd:
                yield m.name.split("/")[-1], dd


def bot_lv(uid: str) -> int:
    m = re.search(r"-lv(\d+)$", uid or "")
    return int(m.group(1)) if m else 0


def collect(shards: list) -> list:
    trajs = {}
    for shard in shards:
        _collect_one(shard, trajs)
    out = []
    for t in trajs.values():
        rounds = sorted(t["rounds"])
        max_lv = max(r["level"] for r in t["rounds"].values())
        # full-game trajectories from bots that actually reached 境5 (user rule)
        if len(rounds) >= 8 and rounds[-1] >= 14 and max_lv >= 5:
            t["first"], t["last"], t["n"] = rounds[0], rounds[-1], len(rounds)
            t["max_lv"] = max_lv
            out.append(t)
    # strongest first: difficulty tier, then coverage
    out.sort(key=lambda t: (-t["lv"], -t["last"], -t["n"]))
    return out


def _collect_one(shard: Path, trajs: dict) -> None:
    prefix = shard.stem.replace(".tar", "")
    for name, dd in iter_records(shard):
        name = f"{prefix}/{name}"
        for rs in dd.get("roundStats") or []:
            rnd = int(rs.get("round") or 0)
            if rnd <= 0:
                continue
            for sk in ("p1", "p2"):
                side = rs.get(sk) or {}
                pub = side.get("publicData") or {}
                priv = side.get("privateData") or {}
                uid = str(pub.get("uid") or "")
                if not (pub.get("isAI") or uid.startswith("ai")):
                    continue
                if pub.get("characterId") in EXCLUDED_CHARS:
                    continue
                board = [int(c) for c in (priv.get("usedCards") or [])]
                while board and board[-1] == 0:
                    board.pop()                     # trailing pad; keep embedded order
                if not board:
                    continue
                pbt = pub.get("permanentBuffTempDatas") or {}
                key = (name, uid)
                t = trajs.setdefault(key, {"rec": name, "uid": uid, "lv": bot_lv(uid),
                                           "char": pub.get("characterId") or 0, "rounds": {}})
                hand = [int(c) for c in (priv.get("handCards") or []) if c]
                t["rounds"][rnd] = {
                    "board": board,
                    "hand": hand,
                    "level": int(pub.get("level") or 1),
                    "exp": int(pub.get("exp") or 0),
                    "extraMaxHp": int(pub.get("extraMaxHp") or 0),
                    "career": int(pub.get("career") or 0),
                    "talents": [int(x) for x in (pub.get("talents") or [])],
                    "tipo": int(pbt.get("10023") or 0),
                    "max_tipo": int(pbt.get("10024") or 0),
                }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shard", nargs="*", default=None,
                    help="shard files (default: every *.tar.zst in the analysis dir)")
    ap.add_argument("--top", type=int, default=30)
    a = ap.parse_args()
    shards = ([Path(s) for s in a.shard] if a.shard
              else sorted(DEFAULT_SHARD.parent.glob("*.tar.zst")))
    print("scanning:", ", ".join(s.name for s in shards))
    trajs = collect(shards)
    keep = trajs[: a.top]
    OUT.write_text(json.dumps({"shards": [s.name for s in shards], "trajs": keep},
                              ensure_ascii=False), encoding="utf-8")
    print(f"{len(trajs)} full-game 境5 bot trajectories; kept top {len(keep)} -> {OUT}")
    for t in keep:
        print(f"  {t['rec']} {t['uid']:>8} lv{t['lv']} char={t['char']} "
              f"rounds {t['first']}-{t['last']} ({t['n']} sightings, max境{t['max_lv']})")


if __name__ == "__main__":
    main()
