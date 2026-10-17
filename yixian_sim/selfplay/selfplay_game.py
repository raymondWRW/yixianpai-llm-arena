# -*- coding: utf-8 -*-
"""Watch the AI play itself: one 8-player game, distinct characters, the strong
policy (board-vs-field search + merges + rerolls + ordering).

Prints a round-by-round playthrough (each battle: characters, boards as card names,
destiny swing) and final standings; also writes game.json for the HTML viewer.

    python selfplay/selfplay_game.py --order --out selfplay/data/game.json
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

import economy as E
import cards as C
import merge as M
import field as F
import env as EV
import characters as CH
import fates as FA

SIDEJOB_NAMES = {0: "—", 1: "炼丹师", 2: "符咒师", 3: "琴师",
                 4: "画师", 5: "阵法师", 6: "灵植师", 7: "命理师"}


def board_names(ids: list) -> list:
    out = []
    for c in ids:
        lv = M.card_level(c)
        nm = C.id_to_name(c)
        out.append(nm + (f"·{lv}" if lv > 1 else ""))
    return out


def run(seed=7, order=True, k=6, cap=14, warmup=4, max_rounds=18, out=None,
        value_net=None, policy_net=None, log=print):
    import oracle_sim
    oracle_sim.warmup(); oracle_sim._get_pool()

    rng = __import__("random").Random(seed)
    roster = CH.sample(8, rng, distinct=True)
    bank = F.FieldBank(per_round=256)
    for g in range(warmup):                       # warm the field with quick games
        EV.YiXianEnv(8, seed=1000 + g, field_bank=bank).play_game(EV.greedy_policy, max_rounds)

    fate_chooser = sidejob_chooser = None
    if value_net:                                 # learned 天命/副职 decisions
        import net as NET, choosers as CHO
        _vnet = NET.load(value_net)
        fate_chooser = CHO.make_fate_chooser(_vnet)
        sidejob_chooser = CHO.make_sidejob_chooser(_vnet)
        log(f"[learned meta-picks from {value_net}]")
    env = EV.YiXianEnv(8, characters=roster, seed=seed, field_bank=bank,
                       fate_chooser=fate_chooser, sidejob_chooser=sidejob_chooser)
    if policy_net:                                # LEARNED board policy (fast, no search)
        import policy_net as PPN
        policy = EV.make_field_policy(place_net=PPN.load(policy_net))
        log(f"[learned board policy from {policy_net}]")
    else:
        policy = EV.make_field_policy(k=k, cap=cap, order=order)
    env.reset()
    chars = [{"pid": p.pid, "id": p.char_id, "name": CH.name(p.char_id),
              "sect": p.sect_prefix} for p in env.state.players]

    log("═" * 70)
    log("  8-PLAYER SELF-PLAY  —  the AI vs itself")
    log("═" * 70)
    for c in chars:
        log(f"   P{c['pid']}  {c['name']:<6} (sect {c['sect']})")
    log("─" * 70)

    rounds_data = []
    prev_alive = {p.pid for p in env.state.alive_players()}
    elim_order = []
    t0 = time.time()
    for _ in range(max_rounds):
        if len(env.state.alive_players()) <= 1:
            break
        env.play_round(policy)
        r = env.state.round
        battles = []
        log(f"\n▶ ROUND {r}   (slots {E.unlocked_slots(r)})")
        for bt in env.last_round_battles:
            pa, pb = env.state.players[bt["a"]], env.state.players[bt["b"]]
            m = bt["margin"]
            if m > 0.5:
                res = f"{chars[pa.pid]['name']} wins  (命 {chars[pb.pid]['name']} −{int(round(abs(m)))})"
            elif m < -0.5:
                res = f"{chars[pb.pid]['name']} wins  (命 {chars[pa.pid]['name']} −{int(round(abs(m)))})"
            else:
                res = "draw"
            log(f"   {chars[pa.pid]['name']} vs {chars[pb.pid]['name']}: {res}")
            log(f"      {chars[pa.pid]['name']} (HP{bt['a_hp']} 修{bt['a_cult']} 体{bt['a_tipo']}): "
                f"{board_names(bt['a_board'])}")
            log(f"      {chars[pb.pid]['name']} (HP{bt['b_hp']} 修{bt['b_cult']} 体{bt['b_tipo']}): "
                f"{board_names(bt['b_board'])}")
            battles.append({
                "a": bt["a"], "b": bt["b"], "margin": m,
                "a_board": board_names(bt["a_board"]), "b_board": board_names(bt["b_board"]),
                "a_hp": bt["a_hp"], "b_hp": bt["b_hp"], "a_cult": bt["a_cult"],
                "b_cult": bt["b_cult"], "a_tipo": bt["a_tipo"], "b_tipo": bt["b_tipo"]})
        # standings snapshot
        snap = [{"pid": p.pid, "name": chars[p.pid]["name"], "realm": p.realm,
                 "cult": p.cultivation, "destiny": p.destiny, "alive": p.alive}
                for p in sorted(env.state.players, key=lambda p: -p.destiny)]
        alive_line = "   命: " + "  ".join(
            f"{s['name']}={s['destiny']}(境{s['realm']})" for s in snap if s["alive"])
        log(alive_line)
        now = {p.pid for p in env.state.alive_players()}
        for pid in (prev_alive - now):
            elim_order.append(pid)
            log(f"   ✗ {chars[pid]['name']} eliminated")
        prev_alive = now
        rounds_data.append({"round": r, "battles": battles, "standings": snap})

    for c in chars:                               # sidejob (round 2) + 天命 fates
        pl = env.state.players[c["pid"]]
        c["career"] = pl.career
        c["sidejob"] = SIDEJOB_NAMES.get(c["career"], "—")
        innate = FA.char_innate(pl.char_id)
        c["innate"] = FA.name(innate) if innate else ""
        c["fates"] = [FA.name(t) for t in pl.talents if FA.name(t)]
        # chosen 天命 (exclude the innate the character starts with)
        c["chosen_fates"] = [FA.name(t) for t in pl.talents
                             if t != innate and FA.name(t)]

    survivors = sorted(env.state.alive_players(), key=lambda p: -p.destiny)
    placement = [p.pid for p in survivors] + list(reversed(elim_order))
    log("\n" + "═" * 70)
    log(f"  FINAL STANDINGS   ({env.state.round} rounds, {time.time()-t0:.0f}s)")
    log("═" * 70)
    for rank, pid in enumerate(placement, 1):
        p = env.state.players[pid]
        tag = "★" if rank == 1 else " "
        log(f"  {tag} #{rank}  {chars[pid]['name']:<6} [副职 {chars[pid]['sidejob']}]  境{p.realm}  "
            f"命 {p.destiny}  ({'alive' if p.alive else 'out'})")

    log("\n" + "─" * 70)
    log("  天命 / 仙命 — the fates each character's AI chose")
    log("─" * 70)
    for c in chars:
        innate = f"  ⟨innate {c['innate']}⟩" if c.get("innate") else ""
        picks = "  →  ".join(c["chosen_fates"]) if c["chosen_fates"] else "（none yet）"
        log(f"  {c['name']:<6} [副职 {c['sidejob']}]{innate}")
        log(f"         天命: {picks}")

    if out:
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_text(json.dumps({
            "characters": chars, "rounds": rounds_data,
            "placement": [{"rank": i + 1, "pid": pid, "name": chars[pid]["name"],
                           "realm": env.state.players[pid].realm,
                           "destiny": env.state.players[pid].destiny}
                          for i, pid in enumerate(placement)],
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        log(f"\nsaved playthrough → {out}")
    return placement


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--order", action="store_true", help="use ordering search (slower, stronger)")
    ap.add_argument("--k", type=int, default=6)
    ap.add_argument("--cap", type=int, default=14)
    ap.add_argument("--out", default=str(_HERE / "data" / "game.json"))
    ap.add_argument("--value-net", default=None,
                    help="value-net checkpoint → learned 天命/副职 picks (else heuristic)")
    ap.add_argument("--policy-net", default=None,
                    help="policy-net checkpoint → learned board placement (fast, no search)")
    args = ap.parse_args()

    def log(*a):
        print(*a, flush=True)
    run(seed=args.seed, order=args.order, k=args.k, cap=args.cap, out=args.out,
        value_net=args.value_net, policy_net=args.policy_net, log=log)
