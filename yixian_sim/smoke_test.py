# -*- coding: utf-8 -*-
"""Smoke test for the packaged YiXianPai simulator.

    python smoke_test.py            # quick: oracle ping + 1 greedy game
    python smoke_test.py --search   # also 1 game with the Oracle board-search policy (slower)

Checks, in order:
  1. Oracle.exe (the game's own combat engine) is reachable and returns a battle result.
  2. Rules/data layers import and load (economy, draws, cards, fates, characters).
  3. A full 8-player game runs end-to-end with the greedy baseline policy.
  4. (optional) A game with the strong board-vs-field search policy.
"""
from __future__ import annotations
import argparse, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
for p in (ROOT / "selfplay", ROOT / "proxy", ROOT):
    sys.path.insert(0, str(p))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--search", action="store_true", help="also run a game with the Oracle search policy")
    ap.add_argument("--seed", type=int, default=7)
    a = ap.parse_args()

    # 1. Oracle
    import oracle_sim
    t0 = time.time()
    ok = oracle_sim.available()
    print(f"[1] Oracle available: {ok}  ({time.time()-t0:.1f}s)  exe={oracle_sim._oracle_exe()}")
    if not ok:
        print("    !! Oracle.exe not reachable. Needs the .NET 8 runtime; see README 'Requirements'.")
        return 1

    # 2. rules/data
    import economy as E, draws as D, cards as C, fates as FA, characters as CH, env as EV, field as F
    print(f"[2] realm table {E.CULT_REQ} | slots R1..R8 {[E.unlocked_slots(r) for r in range(1,9)]} "
          f"| fates {len(FA.all_fates())} | chars {len(CH.ids())} | "
          f"pool(云灵剑宗) {len(D.build_pool(1, max_phase=5))} cards")

    # 3. one battle through the engine
    e = EV.YiXianEnv(n_players=2, characters=[1000001, 2000001], seed=a.seed)
    e.reset()
    for _ in range(3):
        e.play_round(EV.greedy_policy)          # deal + build boards for 3 rounds
    p0, p1 = e.state.players
    slots = E.unlocked_slots(e.state.round)
    r = oracle_sim.matchup(p0.to_fixture(slots), p1.to_fixture(slots), rnd=e.state.round)
    names = lambda b: [C.id_to_name(c) for c in b if c]
    print(f"[3] matchup R{e.state.round} {names(p0.board)} vs {names(p1.board)} "
          f"→ lifeDamage={r.get('lifeDamage')} hpDelta={r.get('hpDelta')} turns={r.get('turns')}")

    # 4. full greedy game
    chars = CH.sample(8, __import__("random").Random(a.seed)) if hasattr(CH, "sample") else [1000001]*8
    env = EV.YiXianEnv(n_players=8, characters=chars, seed=a.seed)
    t0 = time.time()
    placement = env.play_game(EV.greedy_policy, max_rounds=20)
    print(f"[4] greedy 8-player game: rounds={env.state.round} placement={placement} "
          f"destiny={[p.destiny for p in env.state.players]} ({time.time()-t0:.1f}s)")

    if a.search:
        env = EV.YiXianEnv(n_players=8, characters=chars, seed=a.seed, field_bank=F.FieldBank())
        pol = EV.make_field_policy(k=4, cap=10, order=False)
        t0 = time.time()
        placement = env.play_game(pol, max_rounds=20)
        print(f"[5] search-policy game: rounds={env.state.round} placement={placement} ({time.time()-t0:.1f}s)")

    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
