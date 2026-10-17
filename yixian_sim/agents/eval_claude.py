# -*- coding: utf-8 -*-
"""Head-to-head evaluation: claude_policy vs the built-in agents at shared 8-player tables.

    python agents/eval_claude.py --games 6 --opp search     # seats 0-3 claude, 4-7 Oracle-search baseline
    python agents/eval_claude.py --games 6 --opp greedy

Reports mean placement (1 = best) and win counts per side; also prints a per-game log.
"""
from __future__ import annotations
import argparse, random, sys, time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
for _p in (_HERE, _HERE.parent / "selfplay", _HERE.parent / "proxy"):
    sys.path.insert(0, str(_p))

import env as EV, field as F, characters as CH, economy as E
import claude_policy as CP


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=4)
    ap.add_argument("--opp", choices=["search", "greedy"], default="search")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--k", type=int, default=6)
    ap.add_argument("--cap", type=int, default=14)
    ap.add_argument("--noguide", action="store_true", help="disable the TapTap 剑意 archetype layer")
    ap.add_argument("--cloud", action="store_true", help="all 8 seats 云灵剑宗 characters (guide stress test)")
    a = ap.parse_args()

    guide = not a.noguide
    mine = CP.make_policy(k=a.k, cap=a.cap, order=True, guide=guide)
    if a.opp == "search":
        opp = EV.make_field_policy(k=a.k, cap=a.cap, order=True)
    else:
        opp = EV.greedy_policy
    MINE = {0, 1, 2, 3}

    def dispatch(env, p):
        (mine if p.pid in MINE else opp)(env, p)

    def sidejob(env, p):
        return CP.sidejob_chooser(env, p, guide) if p.pid in MINE else env.state.rng.randint(1, 7)

    def fate(env, p, offered):
        import fates as FA
        return CP.fate_chooser(env, p, offered, guide) if p.pid in MINE else FA.choose(offered, env.state.rng)

    bank = F.FieldBank()                                # shared, warms across games
    my_pl, op_pl, my_wins, op_wins = [], [], 0, 0
    for g in range(a.games):
        rng = random.Random(a.seed + g)
        chars = CH.sample(8, rng)
        if a.cloud:
            cloud = [c for c in CH.ids() if c // 1_000_000 == 1]
            chars = [cloud[i % len(cloud)] for i in range(8)]
        env = EV.YiXianEnv(n_players=8, characters=chars, seed=a.seed + g,
                           field_bank=bank, sidejob_chooser=sidejob, fate_chooser=fate)
        t0 = time.time()
        placement = env.play_game(dispatch, max_rounds=20)
        rank = {pid: i + 1 for i, pid in enumerate(placement)}
        m = [rank[i] for i in sorted(MINE)]; o = [rank[i] for i in range(8) if i not in MINE]
        my_pl += m; op_pl += o
        my_wins += placement[0] in MINE; op_wins += placement[0] not in MINE
        realms = [p.realm for p in env.state.players]
        sects = "".join("云七五锻"[p.char_id // 1_000_000 - 1] for p in env.state.players)
        print(f"game {g+1}: sects={sects} rounds={env.state.round} winner=pid{placement[0]} "
              f"claude ranks={m} opp ranks={o} realms={realms} ({time.time()-t0:.0f}s)", flush=True)
    n = a.games
    print(f"\n== {n} games vs {a.opp}: claude mean placement {sum(my_pl)/len(my_pl):.2f} "
          f"(wins {my_wins}/{n}) | {a.opp} mean placement {sum(op_pl)/len(op_pl):.2f} (wins {op_wins}/{n})")


if __name__ == "__main__":
    main()
