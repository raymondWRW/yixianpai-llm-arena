# -*- coding: utf-8 -*-
"""boardsearch.py — seat-aware board search over my available cards.

Usage:
  python agents/boardsearch.py --must A B --pool C D E --size 6,7,8 [--iters 400]

Scores each candidate board against every alive opponent in the seat I will
ACTUALLY occupy (higher 修为 acts first; a tie is scored at its worse seat).
Ranks by (worst-case 命, then average). Read-only — never saves state.
"""
from __future__ import annotations
import itertools, random, sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
ROOT = _HERE.parent
for _p in (_HERE, ROOT / "selfplay", ROOT / "proxy"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import play as PL
_m = sys.modules["__main__"]
for _n in ("fate_chooser", "sidejob_chooser", "daoyun_chooser", "PREFS", "_prefs", "log"):
    setattr(_m, _n, getattr(PL, _n))

import economy as E, oracle_sim


def score(st, board, opps, p, rnd, slots):
    fx = p.to_fixture(slots)
    fx["usedCards"] = list(board[:slots]) + [0] * max(0, slots - len(board))
    pool = [c for c in p.board if c] + list(p.hand)
    for c in board:
        if c in pool:
            pool.remove(c)
    fx["handCards"] = pool
    vals = []
    for pid, ofx, cul in opps:
        if p.cultivation > cul:
            r = oracle_sim.matchup(fx, ofx, rnd=rnd)
            v = float(r.get("lifeDamage", 0) or 0)
        elif p.cultivation < cul:
            r = oracle_sim.matchup(ofx, fx, rnd=rnd)
            v = -float(r.get("lifeDamage", 0) or 0)
        else:
            a = float(oracle_sim.matchup(fx, ofx, rnd=rnd).get("lifeDamage", 0) or 0)
            b = -float(oracle_sim.matchup(ofx, fx, rnd=rnd).get("lifeDamage", 0) or 0)
            v = min(a, b)
        vals.append(v)
    return min(vals), sum(vals) / max(1, len(vals)), vals


def main():
    args = sys.argv[1:]
    must, pool_args, sizes, iters = [], [], [], 300
    mode = None
    for a in args:
        if a == "--must": mode = "must"; continue
        if a == "--pool": mode = "pool"; continue
        if a == "--size": mode = "size"; continue
        if a == "--iters": mode = "iters"; continue
        if mode == "must": must.append(a)
        elif mode == "pool": pool_args.append(a)
        elif mode == "size": sizes = [int(x) for x in a.split(",")]
        elif mode == "iters": iters = int(a)

    st = PL.load(); env = st["env"]; p = PL.me(st)
    rnd = env.state.round; slots = E.unlocked_slots(rnd)
    opps = [(pid, ofx, env.state.players[pid].cultivation)
            for pid, ofx in PL.opponents_fixtures(env)]
    must_ids = PL.resolve(p, must) if must else []
    pool_ids = PL.resolve(p, must + pool_args)[len(must_ids):] if pool_args else []
    if not sizes:
        sizes = [len(must_ids) + len(pool_ids)]
    rng = random.Random(12345)
    seen, results = set(), []
    for _ in range(iters):
        k = rng.choice(sizes)
        extra = k - len(must_ids)
        if extra < 0 or extra > len(pool_ids):
            continue
        chosen = must_ids + rng.sample(pool_ids, extra)
        rng.shuffle(chosen)
        key = tuple(chosen)
        if key in seen:
            continue
        seen.add(key)
        w, avg, vals = score(st, chosen, opps, p, rnd, slots)
        results.append((w, avg, chosen, vals))
    results.sort(key=lambda t: (-t[0], -t[1]))
    for w, avg, b, vals in results[:12]:
        print(f"  worst {w:+6.0f}  avg {avg:+6.1f}  {[PL.nm(c) for c in b]}  {[int(v) for v in vals]}")
    print(f"  ({len(results)} distinct boards evaluated; opponents in pid order "
          f"{[pid for pid, _, _ in opps]})")


if __name__ == "__main__":
    main()
