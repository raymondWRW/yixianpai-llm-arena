# -*- coding: utf-8 -*-
"""extract.py — pull per-game facts from the arena artifacts for the site."""
from __future__ import annotations

import json
import re
from pathlib import Path

ARENA = Path(__file__).resolve().parent.parent / "arena"
GAMES = ARENA / "games"
NAMES = {0: "牧逸风", 1: "谭舒雁", 2: "吾行之", 3: "小布"}
CAREERS = {1: "炼丹师", 2: "符咒师", 3: "琴师", 4: "画师", 5: "阵法师",
           6: "灵植师", 7: "命理师"}
LAST_GAME = 30

# Archetype rules: checked in order, first match wins. Keyed on cards that
# define each engine; "DoT" marks damage-over-time strategies.
ARCHETYPES = [
    ("内伤 clock", True, lambda b: sum(any(k in c for c in b) for k in
                                         ("厄劫缠身", "杯弓蛇影", "血光之灾", "流水无情")) >= 2),
    ("Water drain", True, lambda b: sum("水灵" in c for c in b) >= 3
                                     or any("万花迷魂阵" in c for c in b)),
    ("Qi-dump swords", False, lambda b: any(k in c for c in b for k in
                                             ("万法归灵剑", "白鹭灵剑", "聚灵心法"))),
    ("Star (星弈)", False, lambda b: any("天元心法" in c for c in b)
                                    or sum("星弈" in c for c in b) >= 2),
    ("Force fist (崩拳)", False, lambda b: sum("崩拳" in c for c in b) >= 2),
    ("Sustain / reflect", False, lambda b: sum(any(k in c for k in
                                                    ("反震心法", "静气心法", "金蝉脱壳", "气疗术"))
                                                for c in b) >= 2),
    ("Formation swords", False, lambda b: sum(any(k in c for k in
                                                   ("邪蛊阵", "周天剑阵", "碎杀阵", "辟邪阵纹"))
                                               for c in b) >= 2),
    ("Five-element seals", False, lambda b: sum(any(k in c for k in
                                                     ("火灵", "金灵", "土灵", "木灵", "五行"))
                                                 for c in b) >= 3),
    ("Cloud swords", False, lambda b: sum("云剑" in c for c in b) >= 3),
]


def archetype(board):
    for name, dot, rule in ARCHETYPES:
        if rule(board):
            return name, dot
    return "Other", False


def game_facts(g: int) -> dict | None:
    gdir = GAMES / f"game{g}"
    if not (gdir / "result.json").exists():
        return None
    r = json.loads((gdir / "result.json").read_text(encoding="utf-8"))
    log = (gdir / "game_log.txt").read_text(encoding="utf-8")
    boards = {}
    for m in re.finditer(r"^R\d+ pid(\d) \S+ acted[^\n]*", log, re.M):
        bs = re.findall(r"board = \[([^\]]*)\]", m.group(0))
        if bs:
            boards[int(m.group(1))] = [x.strip().strip("'")
                                       for x in bs[-1].split(",") if x.strip()]
    battles = []
    cur = 0
    for line in log.splitlines():
        m = re.match(r"R(\d+) ", line)
        if m:
            cur = int(m.group(1))
        m = re.search(r"battle pid\d\(first\) vs pid\d: .* turns=(\d+)", line)
        if m:
            battles.append((cur, int(m.group(1))))
    out = [int(m.group(1)) for m in re.finditer(r"pid(\d) \S+ ELIMINATED", log)]
    unfinished = bool(r.get("unfinished"))
    winner = None if unfinished else r.get("winner")
    arche = {pid: archetype(b) for pid, b in boards.items()}
    return {
        "game": g, "rounds": r.get("rounds"), "winner": winner,
        "winner_name": NAMES.get(winner) if winner is not None else None,
        "unfinished": unfinished,
        "standings": {int(k): v for k, v in r["standings"].items()},
        "sidejobs": {int(k): int(v) for k, v in (r.get("sidejobs") or {}).items()},
        "boards": boards, "archetypes": arche,
        "eliminated": out, "battles": battles,
        "fates_picked": len(re.findall(r"天命@境\d picked", log)),
        "fates_default": len(re.findall(r"天命@境\d default", log)),
    }


def all_games():
    return [f for f in (game_facts(g) for g in range(1, LAST_GAME + 1)) if f]


if __name__ == "__main__":
    import statistics as st
    for f in all_games():
        w = f["winner"]
        late = [t for rd, t in f["battles"] if rd >= 13]
        arc = f["archetypes"].get(w, ("-", False))[0] if w is not None else "UNFINISHED"
        sj = "".join(str(f["sidejobs"].get(p, "?")) for p in range(4))
        print(f"g{f['game']:>2} {str(f['winner_name']):<4} {arc:<18} "
              f"R{f['rounds']:>2} late-turns {st.mean(late) if late else 0:5.1f} "
              f"sidejobs {sj} fates {f['fates_picked']}/{f['fates_picked']+f['fates_default']}")
