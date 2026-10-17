#!/usr/bin/env python3
"""
core_card_guard.py — given a list of hand/board card names, flag any CORE cards
(must not roll/absorb) and suggest which slot they replace in the standard board.

Usage: python core_card_guard.py 天地浩荡 崩拳·寸劲 势如破竹 ...
Reads nothing external; pure classifier so it runs inside the sandbox.
"""
import sys

# Cards that are load-bearing in 小布's 气势/chase/崩拳 deck. Never roll/absorb these.
CORE = {
    "气若悬河": "qi+2/force+1, feeds next 2 attacks — engine starter",
    "冲霄破浪": "qi->force + agi+5 — force/agi engine",
    "威震四方": "force cap 6->9 + def8 + force+3 — enables the dump",
    "踏破九霄": "force+3 agi+6 — chase enabler",
    "天地浩荡": "10atk + HP+4 + agi(+2/force!) — TEMPO/DAMAGE/BUFFER triple (g17 discovery)",
    "崩拳·寸劲": "10atk, 2x force bonus — main attacker",
    "崩拳·降龙": "10atk, buffs next 崩拳 +5def/+5atk — chain finisher",
    "磅礴之势": "dump force -> +4def & +4dmg/point — the payoff",
    "鹤步": "HP+4, agi from physique — usable but inferior to 天地浩荡 in that slot",
}
# Cards that are fine to absorb/roll (setup/economy only)
JUNK_OK = {"疗愈阵纹","千斤坠","引雷阵","龟甲阵","锻筋","气沉丹田","锻拳","风冥爪","邪蛊阵",
           "探马掌","须弥阵纹","周天剑阵","聚灵阵"}

def main():
    args = sys.argv[1:]
    if not args:
        print("usage: core_card_guard.py <card names...>")
        return
    core_hits = [c for c in args if c in CORE]
    junk_hits = [c for c in args if c in JUNK_OK]
    unknown = [c for c in args if c not in CORE and c not in JUNK_OK]
    print("=== CORE CARDS FOUND (KEEP! field or hold) ===")
    for c in core_hits:
        print(f"  ! {c}: {CORE[c]}")
    if junk_hits:
        print("=== safe to absorb/roll ===")
        print("  " + ", ".join(junk_hits))
    if unknown:
        print("=== UNCLASSIFIED (judge manually) ===")
        print("  " + ", ".join(unknown))
    print()
    print("REMINDER: if any CORE card is in hand but not on board, REBUILD the board around it before end_turn.")

if __name__ == "__main__":
    main()
