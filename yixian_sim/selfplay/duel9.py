# -*- coding: utf-8 -*-
"""Showcase — the season-9 DATA-DRIVEN agent, 牧逸风+炼丹师 MIRROR match.

Both seats run econ9 (real-data value net + hold net + median roll schedule +
realm-curve breakthroughs + real fate picks); battles use random 0-99
battleParams (the 复盘 patch). Placement searches against REAL season-9 boards.
Writes data/game.json for build_replay.py.

    python selfplay/duel9.py --seed 7
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import card_value as CV
import econ9 as E9
import economy as E
import env as EV
import fates as FA
import field as F
import policy_net as PN
import real9 as R9
from selfplay_game import SIDEJOB_NAMES, board_names

CHAR, CAREER = R9.CHAR, R9.CAREER
CHAR_NAME = {1000001: "牧逸风", 1000003: "龙瑶"}.get(CHAR, str(CHAR))
MAX_ROUNDS = 16


def real_bank(trajs, per_round=1024):
    """FieldBank of real season-9 boards (search opponents)."""
    bank = F.FieldBank(per_round=per_round)
    for g in trajs:
        for r in g["rounds"]:
            if not r["board"]:
                continue
            rnd = r["round"]
            unlocked = min(8, rnd + 2)
            used = list(r["board"])[:unlocked]
            used += [0] * (unlocked - len(used))
            bank.add(rnd, {"characterId": CHAR, "level": max(1, r["level"]),
                           "exp": r["exp"], "extraMaxHp": 0, "usedCards": used,
                           "unlockGrids": unlocked, "career": CAREER,
                           "tipo": 0, "max_tipo": 0,
                           "talents": list(r["talents"])})
    return bank


def run(seed=7, out=None, log=print):
    import oracle_sim
    oracle_sim.RANDOM_PARAMS = True                  # the 复盘 battle-param patch
    oracle_sim.warmup(); oracle_sim._get_pool()

    meta = R9.meta()
    trajs, _partial = R9.load()
    bank = real_bank(trajs)
    log(f"[real9: usage-analysis agent, {len(trajs)} real games in field bank, "
        f"random battleParams ON]")

    mk = lambda: E9.make_real9_policy(meta)
    pol_a, pol_b = mk(), mk()
    env = EV.YiXianEnv(2, characters=[CHAR, CHAR], seed=seed, field_bank=bank,
                       fate_chooser=E9.make_fate_chooser(meta, CHAR),
                       sidejob_chooser=lambda env, p: CAREER,
                       daoyun_chooser=E9.make_dao_chooser())
    env.reset()
    labels = {0: f"{CHAR_NAME}·甲", 1: f"{CHAR_NAME}·乙"}
    chars = [{"pid": p.pid, "id": p.char_id, "name": labels[p.pid],
              "sect": p.sect_prefix} for p in env.state.players]

    log("═" * 66)
    log("  SEASON-9 DATA-DRIVEN MIRROR — value/hold nets + median schedules")
    log("═" * 66)

    def pol(e, p):
        (pol_a if p.pid == 0 else pol_b)(e, p)

    rounds_data, elim = [], []
    prev_alive = {p.pid for p in env.state.alive_players()}
    t0 = time.time()
    for _ in range(MAX_ROUNDS):
        if len(env.state.alive_players()) <= 1:
            break
        env.play_round(pol)
        r = env.state.round
        battles = []
        log(f"\n▶ ROUND {r}   (slots {E.unlocked_slots(r)})")
        for pid, pick in getattr(env, "last_daoyun", []):
            import cards as _C
            nm = _C.id_to_name(pick) if pick else "自在随心"
            log(f"   道韵: {labels[pid]} → {nm}")
        for bt in env.last_round_battles:
            pa, pb = env.state.players[bt["a"]], env.state.players[bt["b"]]
            m = bt["margin"]
            a_won = bt.get("a_won", m > 0.5)        # ties don't exist: 0-命
            loss = int(round(abs(m)))               # rounds still have a winner
            res = (f"{labels[pa.pid]} wins  (命 {labels[pb.pid]} −{loss})" if a_won
                   else f"{labels[pb.pid]} wins  (命 {labels[pa.pid]} −{loss})")
            log(f"   {res}")
            log(f"      甲 (HP{bt['a_hp']} 修{bt['a_cult']}): {board_names(bt['a_board'])}  | hand {len(pa.hand)} rolls {pa.rerolls}")
            log(f"      乙 (HP{bt['b_hp']} 修{bt['b_cult']}): {board_names(bt['b_board'])}  | hand {len(pb.hand)} rolls {pb.rerolls}")
            battles.append({"a": bt["a"], "b": bt["b"], "margin": m,
                            "a_won": a_won,
                            "a_board": board_names(bt["a_board"]),
                            "b_board": board_names(bt["b_board"]),
                            "a_hp": bt["a_hp"], "b_hp": bt["b_hp"],
                            "a_cult": bt["a_cult"], "b_cult": bt["b_cult"],
                            "a_tipo": bt["a_tipo"], "b_tipo": bt["b_tipo"],
                            "a_hand": len(pa.hand), "b_hand": len(pb.hand),
                            "a_rolls": pa.rerolls, "b_rolls": pb.rerolls})
        snap = [{"pid": p.pid, "name": labels[p.pid], "realm": p.realm,
                 "cult": p.cultivation, "destiny": p.destiny, "alive": p.alive}
                for p in sorted(env.state.players, key=lambda p: -p.destiny)]
        log("   命: " + "  ".join(f"{s['name']}={s['destiny']}(境{s['realm']})"
                                  for s in snap if s["alive"]))
        now = {p.pid for p in env.state.alive_players()}
        for pid in (prev_alive - now):
            elim.append(pid)
            log(f"   ✗ {labels[pid]} eliminated")
        prev_alive = now
        rounds_data.append({"round": r, "battles": battles, "standings": snap})

    for c in chars:
        pl = env.state.players[c["pid"]]
        c["career"] = pl.career
        c["sidejob"] = SIDEJOB_NAMES.get(pl.career, "—")
        innate = FA.char_innate(pl.char_id)
        c["innate"] = FA.name(innate) if innate else ""
        c["fates"] = [FA.name(t) for t in pl.talents if FA.name(t)]
        c["chosen_fates"] = [FA.name(t) for t in pl.talents
                             if t != innate and FA.name(t)]

    survivors = sorted(env.state.alive_players(), key=lambda p: -p.destiny)
    placement = [p.pid for p in survivors] + list(reversed(elim))
    log("\n" + "═" * 66)
    log(f"  RESULT   ({env.state.round} rounds, {time.time()-t0:.0f}s)")
    for rank, pid in enumerate(placement, 1):
        p = env.state.players[pid]
        tag = "★" if rank == 1 else " "
        log(f"  {tag} #{rank}  {labels[pid]}  境{p.realm}  命 {p.destiny}  "
            f"({'alive' if p.alive else 'out'})")
    log("\n  天命: " + " | ".join(
        f"{labels[c['pid']]}: {' → '.join(c['chosen_fates'])}" for c in chars))

    if out:
        Path(out).write_text(json.dumps({
            "characters": chars, "rounds": rounds_data,
            "placement": [{"rank": i + 1, "pid": pid, "name": labels[pid],
                           "realm": env.state.players[pid].realm,
                           "destiny": env.state.players[pid].destiny}
                          for i, pid in enumerate(placement)],
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        log(f"\nsaved → {out}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--out", default=str(_HERE / "data" / "game.json"))
    args = ap.parse_args()

    def log(*a):
        print(*a, flush=True)
    run(seed=args.seed, out=args.out, log=log)
