
# Helper: given my candidate 万法 board and the announced foe, print the reorder rules.
# Usage (informational): run_program('final_board_check.py', ['foe'])
# This is a NOTES program (no engine access needed) — it just prints my g21-derived checklist.
import sys

foe = sys.argv[1] if len(sys.argv) > 1 else "?"

rules = {
 "pid1": ("谭舒雁 / 内伤 clock",
   ["KEEP 辟邪阵纹 in the board, field it EARLY (slot 1 safest)",
    "include 化灵诀 + >=2 strong qi feeders so 万法 one-shots (qi>=9)",
    "万法 LAST (dump)", "目标: 100%/100% both seats"]),
 "pid3": ("小布 / 崩拳 burst",
   ["DROP 辟邪阵纹 (no debuff stacks from him)",
    "field an extra qi feeder (3rd 云剑·点星)",
    "win-vs-his-+1 needs a power level: 点星+1 / 白鹭+2 / 万法+2",
    "目标: base 100%/100%, +1 board 100% first"]),
 "pid2": ("吾行之 / 水灵 tank", ["万法 board wins 100%/100% base and +1", "low threat"]),
}

name, notes = rules.get(foe, ("unknown foe", ["sim_matchup BOTH seats after any reorder"]))
print(f"Final-board plan vs {foe}: {name}")
for n in notes:
    print("  - " + n)
print("\nREMINDER: my_board order matters; re-run sim_matchup on the EXACT order after any swap.")
