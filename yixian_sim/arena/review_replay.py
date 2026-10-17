# -*- coding: utf-8 -*-
"""review_replay.py — re-run the post-game REVIEW for an already-played game.

    python review_replay.py --game 10

Reconstructs the final game state from games/gameN artifacts (logs carry
hands, fate picks with phases, per-battle STATE lines with exact max HP),
then runs the standard reflection conversations with the CURRENT review
prompt/tools. Notebooks are rewritten, same as a live post-game review.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))

import bots as B
import cards as C
import engine as ENG
import make_replays as MR
import run_arena as RA

AVATAR_IDS = {"云影化身": 7, "雁影化身": 65, "五行化身": 83, "生机不灭": 154}


def _ids(names):
    out = []
    for n in names:
        base, _, lv = n.partition("+")
        cid = C.name_to_base_id(base)
        if cid:
            out.append(cid + 10000 * int(lv or 0))
    return out


def rebuild(game_no: int):
    gdir = _HERE / "games" / f"game{game_no}"
    log = (gdir / "game_log.txt").read_text(encoding="utf-8")
    rounds = MR.parse_game(gdir)
    last_rnd = max(rounds)
    result = json.loads((gdir / "result.json").read_text(encoding="utf-8"))

    g = ENG.ArenaGame(seed=result["seed"])
    g.env.state.round = last_rnd

    # fate picks with ids + phases
    picks = {p: [] for p in range(4)}
    for m in re.finditer(r"pid(\d) 天命@境(\d) (?:picked|default) (\d+):", log):
        picks[int(m.group(1))].append((int(m.group(2)), int(m.group(3))))
    # 化身 consumption
    for m in re.finditer(r"pid(\d) 化身 (\S+) consumed", log):
        fid = AVATAR_IDS.get(m.group(2))
        if fid:
            g.consumed_avatars[int(m.group(1))].add(fid)

    final_stand = rounds[last_rnd]["standings"]
    per_all = {}
    for pid in range(4):
        per = MR.track_states(rounds, pid)
        per_all[pid] = per
        last = per[max(per)]
        q = g.env.state.players[pid]
        q.cultivation = last["cult"]
        q.realm = last["realm"]
        q.destiny = final_stand.get(pid, 0)
        q.alive = q.destiny > 0
        tp = last["tipo"].split("/")
        q.tipo, q.max_tipo = int(tp[0]), int(tp[1])
        board = _ids(last["board"])
        q.board = board + [0] * (8 - len(board))
        hand_names = rounds[max(per)]["hands"].get(pid, [])
        q.hand = _ids(hand_names)
        q.rerolls = rounds[max(per)].get("rerolls_logged", {}).get(pid, 0) \
            if "rerolls_logged" in rounds[max(per)] else 0
        for ph, fid in picks[pid]:
            if fid not in q.talents:
                q.talents.append(fid)
                if hasattr(q, "talent_phases"):
                    q.talent_phases[fid] = ph

    # battle_results with logs; calibrate battle_hp from STATE lines
    hp_target = {}
    for rnd in sorted(rounds):
        rr = []
        for b in rounds[rnd]["battles"]:
            hits = sorted((gdir / "battles").glob(f"r{rnd}_{b['idx']}_*.log"))
            blog = hits[0].read_text(encoding="utf-8") if hits else ""
            rr.append({"round": rnd, "a": b["first"], "b": b["second"],
                       "winner": b["winner"], "loser": b["loser"],
                       "destiny_loss": b["loss"], "applied": not b["not_applied"],
                       "turns": b["turns"], "log": blog})
            m = re.search(r"STATE after turn 1a: A\(hp -?\d+/(\d+).*?"
                          r"B\(hp -?\d+/(\d+)", blog)
            if m:
                hp_target[b["first"]] = int(m.group(1))
                hp_target[b["second"]] = int(m.group(2))
        g.battle_results.append(rr)
    for pid, target in hp_target.items():
        q = g.env.state.players[pid]
        q.extra_hp += target - q.battle_hp

    # histories
    for rnd, r in rounds.items():
        g.deal_history[rnd] = dict(r["deals"])
        g.hand_history[rnd] = dict(r["hands"])
        g.action_history[rnd] = {p: a["acts"] for p, a in r["actions"].items()}
        if r.get("rerolls_logged"):
            g.rr_history[rnd] = dict(r["rerolls_logged"])
    g.round_open = {q.pid: g.public_state(q) for q in g.env.state.players}
    return g, result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", type=int, required=True)
    ap.add_argument("--model", default="deepseek-chat")
    a = ap.parse_args()
    g, result = rebuild(a.game)
    keys = {int(k): v for k, v in json.loads(
        (_HERE / "deepseek_keys.json").read_text(encoding="utf-8")).items()}
    seats = {pid: B.BotSeat(g, pid) for pid in range(4)}
    for s in seats.values():
        s.game_no = a.game
    winner = g.env.state.players[result["winner"]]
    print(f"reconstructed game {a.game}: round {g.env.state.round}, "
          f"winner {result['winner_name']}")
    for q in g.env.state.players:
        print(f"  pid{q.pid} {ENG.NAMES[q.char_id]}: 命{q.destiny} "
              f"修为{q.cultivation} 境{q.realm} HP{q.battle_hp} "
              f"体魄{q.tipo}/{q.max_tipo} 天命x{len(q.talents)} "
              f"board {sum(1 for c in q.board if c)} hand {len(q.hand)}")
    RA.run_reflections(g, seats, keys, a.model, winner)
    (_HERE / "games" / f"game{a.game}" / "review_replay.log").write_text(
        "\n".join(g.log_lines), encoding="utf-8")
    print("\nreview done — notebook rewrites + search log in "
          f"games/game{a.game}/review_replay.log")


if __name__ == "__main__":
    main()
