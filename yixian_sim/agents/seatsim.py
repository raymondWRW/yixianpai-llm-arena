# -*- coding: utf-8 -*-
"""seatsim.py — sim MY board vs every alive opponent in BOTH seat orders.

Usage:  python agents/seatsim.py [card names...]
No args = my current board. Prints life margin for me-first and me-second.
Read-only: never saves state.
"""
from __future__ import annotations
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
ROOT = _HERE.parent
for _p in (_HERE, ROOT / "selfplay", ROOT / "proxy"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import play as PL
import economy as E, characters as CH, oracle_sim

# the save pickles the choosers as __main__.<name> (they were defined in play.py
# running as __main__) — rebind them here so pickle.load can resolve them.
_m = sys.modules["__main__"]
for _n in ("fate_chooser", "sidejob_chooser", "daoyun_chooser", "PREFS", "_prefs", "log"):
    setattr(_m, _n, getattr(PL, _n))


def _eff(v):
    """命 actually paid/gained after 猫魂庇佑 (a LOSS of even size is halved)."""
    v = int(round(v))
    if v < 0 and (-v) % 2 == 0:
        return v / 2
    return v


def main():
    st = PL.load()
    env = st["env"]
    p = PL.me(st)
    rnd = env.state.round
    slots = E.unlocked_slots(rnd)
    args = sys.argv[1:]
    if args:
        board = PL.resolve(p, args)
    else:
        board = [c for c in p.board if c]
    fx = p.to_fixture(slots)
    fx["usedCards"] = list(board[:slots]) + [0] * max(0, slots - len(board))
    if args:
        pool = [c for c in p.board if c] + list(p.hand)
        for c in board:
            if c in pool:
                pool.remove(c)
        fx["handCards"] = pool
    tot_f = tot_s = 0.0
    n = 0
    worst = None
    act = []
    eff = []
    for pid, ofx in PL.opponents_fixtures(env):
        rf = oracle_sim.matchup(fx, ofx, rnd=rnd)
        rs = oracle_sim.matchup(ofx, fx, rnd=rnd)
        lf = float(rf.get("lifeDamage", 0) or 0)
        ls = -float(rs.get("lifeDamage", 0) or 0)
        tot_f += lf; tot_s += ls; n += 1
        cul = env.state.players[pid].cultivation
        seat = "FIRST" if p.cultivation > cul else ("second" if p.cultivation < cul else "TIE")
        best_worst = min(lf, ls)
        worst = best_worst if worst is None else min(worst, best_worst)
        act.append(lf if seat == "FIRST" else ls if seat == "second" else min(lf, ls))
        eff.append(_eff(act[-1]))
        hf = float(rf.get("hpDelta", 0) or 0); hs = -float(rs.get("hpDelta", 0) or 0)
        print(f"  pid{pid} {CH.name(env.state.players[pid].char_id)} (修{cul}, me {seat}): "
              f"me-first {lf:+.0f} (hp {hf:+.0f}, t{rf.get('turns')})  "
              f"me-second {ls:+.0f} (hp {hs:+.0f}, t{rs.get('turns')})")
    n = max(1, n)
    print(f"  => avg first {tot_f/n:+.1f}  avg second {tot_s/n:+.1f}  minimax(worst over both seats) {worst:+.0f}")
    print(f"     ACTUAL-seat: avg {sum(act)/max(1,len(act)):+.1f}  worst {min(act):+.0f}  "
          f"(ties scored at their worse seat)")
    print(f"     EFFECTIVE (after 猫魂庇佑 even-halving): avg {sum(eff)/max(1,len(eff)):+.1f}  "
          f"worst {min(eff):+.0f}  vals {[round(x,1) for x in eff]}")
    print(f"  board={[PL.nm(c) for c in board]}  my 修为={p.cultivation}")


if __name__ == "__main__":
    main()
