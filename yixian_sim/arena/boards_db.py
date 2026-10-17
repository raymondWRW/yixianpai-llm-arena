# -*- coding: utf-8 -*-
"""boards_db.py — persistent database of every board fielded in past games.

Rows: {game, round, pid, name, board, cult, realm, result}
Built from games/gameN/game_log.txt via make_replays' parser; updated after
each real game; bots query it in review (board_db tool) to compare their
round-N board against every board that ever existed at that power level.

    python boards_db.py            # rebuild from all games/game* dirs
"""
from __future__ import annotations

import json
import re
from pathlib import Path

_HERE = Path(__file__).resolve().parent
DB_PATH = _HERE / "boards_db.json"


def _rows_for_game(gdir: Path, game_no: int) -> list:
    import make_replays as MR
    rounds = MR.parse_game(gdir)
    rows = []
    for pid in range(4):
        per = MR.track_states(rounds, pid)
        name = MR.NAMES.get(pid) or f"pid{pid}"
        for rnd, r in per.items():
            if not r["board"]:
                continue
            res = []
            for b in r["battles"]:
                opp = b["second"] if b["first"] == pid else b["first"]
                opp_name = MR.NAMES.get(opp) or f"pid{opp}"
                won = b["winner"] == pid
                res.append(f"{'won' if won else 'LOST'} vs {opp_name} "
                           f"(-{b['loss']}命"
                           + (", not applied" if b["not_applied"] else "")
                           + ")")
            rows.append({"game": game_no, "round": rnd, "pid": pid,
                         "name": name, "board": r["board"],
                         "cult": r["cult"], "realm": r["realm"],
                         "result": "; ".join(res) or "(no battle)"})
    return rows


def load() -> list:
    if DB_PATH.exists():
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    return []


def update_game(gdir: Path, game_no: int) -> int:
    """Replace this game's rows in the DB (idempotent per game)."""
    db = [r for r in load() if r["game"] != game_no]
    rows = _rows_for_game(Path(gdir), game_no)
    db.extend(rows)
    db.sort(key=lambda r: (r["game"], r["round"], r["pid"]))
    DB_PATH.write_text(json.dumps(db, ensure_ascii=False, indent=0),
                       encoding="utf-8")
    return len(rows)


def rebuild(games_dir: Path = None) -> int:
    games_dir = games_dir or (_HERE / "games")
    db = []
    for d in sorted(games_dir.glob("game*")):
        m = re.fullmatch(r"game(\d+)", d.name)
        if not m or int(m.group(1)) >= 90:        # 9x = stub smoke tests
            continue
        if not (d / "game_log.txt").exists():
            continue
        db.extend(_rows_for_game(d, int(m.group(1))))
    db.sort(key=lambda r: (r["game"], r["round"], r["pid"]))
    DB_PATH.write_text(json.dumps(db, ensure_ascii=False, indent=0),
                       encoding="utf-8")
    return len(db)


def query(round_no: int, window: int = 1, name: str = None,
          limit: int = 30) -> list:
    """Boards fielded around a round in past games, newest games first."""
    rows = [r for r in load()
            if abs(r["round"] - int(round_no)) <= int(window)
            and (name in (None, "", "any") or r["name"] == name)]
    rows.sort(key=lambda r: (-r["game"], abs(r["round"] - int(round_no))))
    return rows[:int(limit)]


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(_HERE))
    n = rebuild()
    print(f"boards_db.json rebuilt: {n} rows")
