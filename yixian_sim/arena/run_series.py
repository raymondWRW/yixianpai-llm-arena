# -*- coding: utf-8 -*-
"""run_series.py — play arena games back to back until the API money runs out.

    python run_series.py --start 22

Each game runs through run_arena.py unchanged (off-peak waits and mid-game
peak pauses still apply). Before every game this checks the DeepSeek balance
and stops when it can no longer cover another game, using the measured cost
of the games already played. A 402 mid-game exits run_arena with code 3 and
ends the series. Replays are built after each game. Progress is appended to
series_log.md.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
PY = sys.executable
LOG = _HERE / "series_log.md"
FIRST_GAME_RESERVE = 1.00     # USD needed before the cost per game is known
SAFETY = 1.25                 # require 25% headroom over the average cost


def balance() -> tuple:
    """(USD balance, all keys usable). The four keys share one account."""
    import requests
    keys = json.loads((_HERE / "deepseek_keys.json").read_text(encoding="utf-8"))
    bals, ok = [], True
    for k in keys.values():
        r = requests.get("https://api.deepseek.com/user/balance",
                         headers={"Authorization": f"Bearer {k}"}, timeout=30)
        d = r.json()
        ok = ok and bool(d.get("is_available"))
        usd = [float(b["total_balance"]) for b in d.get("balance_infos", [])
               if b.get("currency") == "USD"]
        bals.append(usd[0] if usd else 0.0)
    return min(bals), ok


def note(line: str) -> None:
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"- {stamp} — {line}\n")
    print(line, flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--max-games", type=int, default=100)
    a = ap.parse_args()
    if sys.platform == "win32":                   # stay awake between games
        import ctypes
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | 0x1)
    if not LOG.exists():
        LOG.write_text("# Arena series log\n\n", encoding="utf-8")
    costs = []
    game = a.start
    for _ in range(a.max_games):
        bal, ok = balance()
        need = (sum(costs) / len(costs) * SAFETY) if costs else FIRST_GAME_RESERVE
        if not ok or bal < need:
            note(f"STOP before game {game}: balance ${bal:.2f} < "
                 f"${need:.2f} needed for one more game "
                 f"(avg cost ${sum(costs)/len(costs):.2f})" if costs else
                 f"STOP before game {game}: balance ${bal:.2f}, key usable={ok}")
            break
        note(f"game {game} starting — balance ${bal:.2f}")
        with open(_HERE / f"game{game}_run.log", "w", encoding="utf-8") as out:
            rc = subprocess.call([PY, "run_arena.py", "--game", str(game),
                                  "--seed", str(200 + game)],
                                 cwd=str(_HERE), stdout=out,
                                 stderr=subprocess.STDOUT,
                                 env={**__import__("os").environ,
                                      "PYTHONIOENCODING": "utf-8",
                                      "PYTHONUNBUFFERED": "1"})
        after, _ = balance()
        cost = bal - after
        if rc == 3:
            note(f"game {game}: OUT OF MONEY mid-run (cost so far "
                 f"${cost:.2f}) — series over")
            break
        if rc != 0:
            note(f"game {game}: run_arena exited {rc} — series stopped "
                 f"for inspection")
            break
        costs.append(cost)
        res = json.loads((_HERE / "games" / f"game{game}" / "result.json")
                         .read_text(encoding="utf-8"))
        subprocess.call([PY, "make_replays.py", "--game", str(game)],
                        cwd=str(_HERE), stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)
        note(f"game {game} done — winner {res.get('winner_name')} "
             f"(命{res['standings'].get(str(res.get('winner')), '?')}), "
             f"{res.get('rounds')} rounds; cost ${cost:.2f}; "
             f"balance ${after:.2f}")
        game += 1
    note(f"series finished: {len(costs)} games played, "
         f"total ${sum(costs):.2f}")


if __name__ == "__main__":
    main()
