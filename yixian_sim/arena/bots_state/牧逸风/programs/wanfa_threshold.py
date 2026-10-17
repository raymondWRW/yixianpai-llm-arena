
# wanfa_threshold.py — quick reminder/checker for the #1 rule:
#   牧逸风's win condition = 万法归灵剑 at lv2+ with the qi suite, firing for >= ~75 dmg.
# Usage: run_program('wanfa_threshold.py')  -> prints the recipe + thresholds.
RECIPE = ["聚灵心法+1","百鸟灵剑诀+1","引气剑+1","巨鲲灵剑+2","云剑·点星","万法归灵剑+2","白鹭灵剑+1","辟邪阵纹+1"]
print("=== 万法归灵剑 QI-NUKE (牧逸风 #1 win-con) ===")
print("BOARD (cyclic):", RECIPE)
print()
print("THRESHOLDS (verified g22, 1000+ evals):")
print("  万法 lv1 @ ~11 qi = ~53 dmg  -> LOSES vs scaled 崩拳/体魄 board (138 HP)")
print("  万法 lv2 @ ~11 qi = ~75-82 dmg -> WINS vs 小布 R17 board, BOTH seats, ends turn 5")
print("  万法 lv3 @ ~11 qi = ~87-98 dmg")
print()
print("RULES:")
print("  - 辟邪阵纹 = slot 8 (LAST).  聚灵+百鸟 = the 2 持续 (max), DROP a 3rd 持续.")
print("  - 万法 slot 6-7, AFTER all qi generators.  白鹭 after 万法 (chase) or slot before.")
print("  - Need TWO 万法 copies OR one copy + 云泉道茶 (fate upgrade).")
print("  - From the 境5 gate round: NAME 万法 and spend EVERY exchange on it.")
print("  - No other reachable board beats a scaled 崩拳/体魄 board (proven g22).")
