# -*- coding: utf-8 -*-
"""Board-vs-field evaluation — the reward core for the offline model.

In this auto-battler you never choose a move against a KNOWN opponent: each round
you're paired at random, so a board's worth is its EXPECTED destiny outcome
against the FIELD (the distribution of boards other players field this round).

`FieldBank` holds a rolling sample of recent opponent fixtures (board + stats),
grouped by round so we compare against contemporaries, not a realm-1 board when
we're realm-4. Self-play fills it with the agents' own boards, so the field
sharpens as the policy improves (fictitious self-play). `score` runs my board vs
a `k`-sample of that field through the Oracle in parallel (oracle_sim.batch_matchup)
and aggregates to {mean destiny margin, win-rate}.

Everything stochastic takes an explicit rng for reproducibility.
"""
from __future__ import annotations

import sys
from collections import defaultdict, deque
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent
for _p in (str(_REPO / "proxy"), str(_REPO)):
    if _p not in sys.path:
        sys.path.insert(0, _p)


def _oracle():
    import oracle_sim
    return oracle_sim


class FieldBank:
    """Rolling bank of opponent fixtures, bucketed by round.

    A fixture is a plain dict the Oracle understands: at least
    {characterId, level, exp, usedCards, unlockGrids} (+ optional extraMaxHp,
    talents, fateStrategies). We keep the most recent `per_round` per bucket."""

    def __init__(self, per_round: int = 256):
        self.per_round = per_round
        self._buckets: dict[int, deque] = defaultdict(lambda: deque(maxlen=per_round))
        import threading
        self._lk = threading.Lock()        # concurrent games share one bank

    def add(self, rnd: int, fixture: dict):
        # store a shallow copy so later board mutation on the source doesn't alias
        with self._lk:
            self._buckets[int(rnd)].append(dict(fixture))

    def add_many(self, rnd: int, fixtures):
        for f in fixtures:
            self.add(rnd, f)

    def all_fixtures(self) -> list:
        """[(round, fixture), ...] across all buckets — a realistic fixture source
        (real self-play boards + stats) for battle-net data generation."""
        out = []
        for r, bucket in self._buckets.items():
            for f in bucket:
                out.append((r, f))
        return out

    def size(self, rnd: int | None = None) -> int:
        if rnd is None:
            return sum(len(b) for b in self._buckets.values())
        return len(self._buckets.get(int(rnd), ()))

    def sample(self, rnd: int, k: int, rng, window: int = 1) -> list:
        """k opponent fixtures near `rnd` (±window buckets), sampled WITH
        replacement. Falls back to the nearest non-empty bucket, then to the whole
        bank, so a cold early round still returns something."""
        with self._lk:
            pool = []
            for r in range(int(rnd) - window, int(rnd) + window + 1):
                pool.extend(self._buckets.get(r, ()))
            if not pool:                          # nearest non-empty bucket
                for d in range(1, 20):
                    for r in (int(rnd) - d, int(rnd) + d):
                        pool.extend(self._buckets.get(r, ()))
                    if pool:
                        break
            if not pool:                          # anything at all
                for b in self._buckets.values():
                    pool.extend(b)
        if not pool:
            return []
        return [pool[rng.randrange(len(pool))] for _ in range(k)]


def score(me: dict, opponents: list, rnd: int = 8) -> dict:
    """My board vs a list of opponent fixtures, via the Oracle (parallel).
    Returns {n, mean_life, winrate, lifes}. mean_life > 0 ⇒ I take destiny on
    average; winrate = fraction of sampled opponents I beat (hpDelta > 0)."""
    if not opponents:
        return {"n": 0, "mean_life": 0.0, "winrate": 0.0, "lifes": []}
    res = _oracle().batch_matchup([(me, o) for o in opponents], rnd=rnd)
    lifes, wins, n = [], 0, 0
    for r in res:
        if not r:
            continue
        n += 1
        lifes.append(float(r.get("lifeDamage", 0) or 0))
        if r.get("win"):
            wins += 1
    if n == 0:
        return {"n": 0, "mean_life": 0.0, "winrate": 0.0, "lifes": []}
    return {"n": n, "mean_life": sum(lifes) / n, "winrate": wins / n, "lifes": lifes}


def score_vs_field(me: dict, bank: FieldBank, k: int, rnd: int, rng,
                   window: int = 1) -> dict:
    """Convenience: sample k opponents from `bank` near `rnd`, then `score`."""
    opps = bank.sample(rnd, k, rng, window=window)
    return score(me, opps, rnd=rnd)


if __name__ == "__main__":
    import random
    rng = random.Random(0)
    me = {"characterId": 1000001, "level": 3, "exp": 20, "usedCards": [1, 4, 5, 6],
          "unlockGrids": 6}
    bank = FieldBank(per_round=64)
    for cards in ([4000003, 4000019], [4000019], [1, 4, 5], [4000003]):
        bank.add(8, {"characterId": 2000001, "level": 3, "exp": 20,
                     "usedCards": cards, "unlockGrids": 6})
    print("bank size @r8:", bank.size(8))
    print("score vs field:", score_vs_field(me, bank, k=8, rnd=8, rng=rng))
