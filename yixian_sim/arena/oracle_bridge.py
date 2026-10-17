# -*- coding: utf-8 -*-
"""oracle_bridge.py — fast outcome-only battle evaluation via the Yi Xian
Oracle (the GAME'S OWN combat code, JIT-compiled native in CoreCLR).

Role in the arena (measured 2026-09-25):
  * Oracle  ~2.6 ms/battle across 8 warm workers (383 battles/sec) — but its
    log is raw engine telemetry (numeric buff ids), useless for narration.
  * yisim   ~29 ms/battle, with human-readable turn-by-turn narration.
  * The two engines agree on the WINNER in 83% of real corpus matchups.

So: the Oracle is the fast PRE-FILTER inside board search (it explores ~11x
more candidates per second), and yisim — which resolves the arena's real
battles and writes the logs bots read — remains the ARBITER that ranks the
finalists. Never let an Oracle-only verdict reach a notebook.

Compatible by construction: arena card ids ARE game card ids (base + 10000
per level) and arena fate ids ARE game talent ids.
"""
from __future__ import annotations

import os
import queue
import sys
import threading

_ORACLE_SCRIPTS = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "..", "card counter with proxy", "oracle", "scripts")
_ORACLE_SCRIPTS = os.path.normpath(_ORACLE_SCRIPTS)

_pool = None            # [(worker, lock), ...]
_pool_failed = False
_base_hp = {}           # level -> base max HP (probed once)
_lock = threading.Lock()

PHYS_BUFF, PHYS_CAP_BUFF = "10023", "10024"


def _worker_cls():
    if _ORACLE_SCRIPTS not in sys.path:
        sys.path.insert(0, _ORACLE_SCRIPTS)
    from oracle_pool import OracleWorker      # noqa: WPS433
    return OracleWorker


def side_fixture(char_id, realm, max_hp, cards, talents=(), career=0,
                 physique=0, max_physique=0, slots=8) -> dict:
    """One side of an Oracle battle fixture, from arena state."""
    lvl = max(1, min(int(realm), 5))
    base = _base_hp.get(lvl, 75)
    d = {"characterId": int(char_id), "level": lvl, "exp": 0,
         "usedCards": [int(c) for c in cards],
         "talents": [int(t) for t in talents],
         "fateStrategies": [], "career": int(career or 0),
         "extraMaxHp": max(0, int(max_hp) - base),
         "unlockGrids": int(slots)}
    if physique or max_physique:
        d["permanentBuffTempDatas"] = {
            PHYS_BUFF: int(physique),
            PHYS_CAP_BUFF: max(int(max_physique), int(physique))}
    return d


def _fixture(p1, p2, round_no):
    return {"p1": p1, "p2": p2, "battleParams": [], "mainViewId": "",
            "round": int(round_no), "expected": {}, "wantLog": False}


def available(n_workers: int = None) -> bool:
    """True once a warm worker pool exists (spawns it on first call, ~15s)."""
    global _pool, _pool_failed
    if _pool:
        return True
    if _pool_failed:
        return False
    with _lock:
        if _pool:
            return True
        if _pool_failed:
            return False
        try:
            OracleWorker = _worker_cls()
        except Exception:
            _pool_failed = True
            return False
        n = int(n_workers or os.environ.get("ARENA_ORACLE_POOL", 0) or 0)
        if n <= 0:
            n = min(8, max(2, (os.cpu_count() or 8) // 2))
        warm = _fixture(side_fixture(2000001, 1, 75, [4000003]),
                        side_fixture(2000001, 1, 75, [4000003]), 1)
        slots = [None] * n

        def mk(i):
            try:
                w = OracleWorker()
                w.run(dict(warm))          # pre-JIT: first battle is ~10x slower
                slots[i] = (w, threading.Lock())
            except Exception:
                slots[i] = None

        ts = [threading.Thread(target=mk, args=(i,), daemon=True)
              for i in range(n)]
        for t in ts:
            t.start()
        for t in ts:
            t.join()
        _pool = [s for s in slots if s]
        if not _pool:
            _pool_failed = True
            return False
        # probe base max HP per realm so extraMaxHp matches arena HP exactly
        w, lk = _pool[0]
        for lvl in range(1, 6):
            try:
                probe = {"characterId": 2000001, "level": lvl, "exp": 0,
                         "usedCards": [4000003], "talents": [],
                         "fateStrategies": [], "career": 0, "extraMaxHp": 0,
                         "unlockGrids": 8}
                with lk:
                    r = w.run(_fixture(probe, dict(probe), 1))
                _base_hp[lvl] = int(r.get("leftHp") or 75)
            except Exception:
                _base_hp[lvl] = 75
        return True


def run_many(fixtures: list, timeout_each: float = 30.0) -> list:
    """Evaluate fixtures across the warm pool. Returns result dicts in order
    (each: winner 'p1'/'p2', lifeDamage, hpDelta, turns) or None on failure."""
    if not available():
        raise RuntimeError("oracle unavailable")
    out = [None] * len(fixtures)
    work = queue.Queue()
    for i, f in enumerate(fixtures):
        work.put((i, f))

    def loop(worker, lk):
        while True:
            try:
                i, f = work.get_nowait()
            except queue.Empty:
                return
            try:
                with lk:
                    out[i] = worker.run(f)
            except Exception:
                out[i] = None

    ts = [threading.Thread(target=loop, args=(w, lk), daemon=True)
          for w, lk in _pool]
    for t in ts:
        t.start()
    for t in ts:
        t.join(timeout=timeout_each * max(1, len(fixtures) // max(1, len(_pool))))
    return out


def evaluator(me_side_fn, opp_side, round_no, repeats=1):
    """Build an eval_many(cands) for search.hillclimb backed by the Oracle.

    me_side_fn(ids) -> my side fixture dict. Both seatings are evaluated
    ('me first' = p1, 'me second' = p2), matching the yisim evaluator's
    (seat, won, turns) result shape."""
    def eval_many(cands):
        fixtures = []
        for ids in cands:
            me = me_side_fn(ids)
            for _ in range(repeats):
                fixtures.append(_fixture(me, opp_side, round_no))       # me first
                fixtures.append(_fixture(opp_side, me, round_no))       # me second
        res = run_many(fixtures)
        per, i = [], 0
        for _ in cands:
            rr = []
            for _ in range(repeats):
                r1, r2 = res[i], res[i + 1]
                i += 2
                rr.append(("first", bool(r1) and r1.get("winner") == "p1",
                           (r1 or {}).get("turns")))
                rr.append(("second", bool(r2) and r2.get("winner") == "p2",
                           (r2 or {}).get("turns")))
            per.append(rr)
        return per
    return eval_many
