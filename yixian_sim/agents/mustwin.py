# -*- coding: utf-8 -*-
"""mustwin.py — search for a board that WINS against the named opponents.

Usage: python agents/mustwin.py --must A B --pool C D --size 7,8 --iters 300 --opps 2 5

Prints, for each candidate, the life margin vs each listed opponent in BOTH
seats, ranked by the best achievable "win everything" seat regime. Read-only.
"""
from __future__ import annotations
import random, sys
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


def main():
    args = sys.argv[1:]
    must, pool_args, sizes, iters, opp_ids = [], [], [], 300, []
    mode = None
    for a in args:
        if a in ("--must", "--pool", "--size", "--iters", "--opps"):
            mode = a[2:]; continue
        if mode == "must": must.append(a)
        elif mode == "pool": pool_args.append(a)
        elif mode == "size": sizes = [int(x) for x in a.split(",")]
        elif mode == "iters": iters = int(a)
        elif mode == "opps": opp_ids.append(int(a))

    st = PL.load(); env = st["env"]; p = PL.me(st)
    rnd = env.state.round; slots = E.unlocked_slots(rnd)
    opps = [(pid, ofx) for pid, ofx in PL.opponents_fixtures(env)
            if not opp_ids or pid in opp_ids]
    must_ids = PL.resolve(p, must) if must else []
    pool_ids = PL.resolve(p, must + pool_args)[len(must_ids):] if pool_args else []
    if not sizes:
        sizes = [len(must_ids) + len(pool_ids)]
    rng = random.Random(999)
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
        fx = p.to_fixture(slots)
        fx["usedCards"] = list(chosen[:slots]) + [0] * max(0, slots - len(chosen))
        pool = [c for c in p.board if c] + list(p.hand)
        for c in chosen:
            if c in pool:
                pool.remove(c)
        fx["handCards"] = pool
        first, second = [], []
        for pid, ofx in opps:
            first.append(float(oracle_sim.matchup(fx, ofx, rnd=rnd).get("lifeDamage", 0) or 0))
            second.append(-float(oracle_sim.matchup(ofx, fx, rnd=rnd).get("lifeDamage", 0) or 0))
        best = max(min(first), min(second))
        results.append((best, min(first), min(second), chosen, first, second))
    results.sort(key=lambda t: -t[0])
    for best, mf, ms, b, f, s in results[:12]:
        print(f"  best-regime {best:+6.0f} | first {[int(x) for x in f]} | second {[int(x) for x in s]}"
              f" | {[PL.nm(c) for c in b]}")
    print(f"  ({len(results)} boards; opponents {[pid for pid, _ in opps]})")


if __name__ == "__main__":
    main()
