#!/usr/bin/env python3
"""
burst_board.py -- 小布 g18 lobby-winning 崩拳/气势 burst board recipe.
Prints the canonical board + slot-by-slot rationale + reachability thresholds.
Usage: run_program('burst_board.py')
"""
BOARD = [
    ("气若悬河+1", "step1: +3qi, +1force, +1force on next 3 attacks (FUELLER)"),
    ("冲霄破浪",   "step2: +qi then +1 force PER current qi, +5agi (converts banked qi)"),
    ("踏破九霄+1", "step3: +4force, +6agi -> hits >=10 agi -> AUTO-CHASE driver"),
    ("势如破竹+1", "step4: 11atk; spend up to 3qi -> +3force & +9atk (CHASE target)"),
    ("崩拳·降龙+1","step5: 12atk; NEXT 崩拳 +7def,+7atk (PRE-BUFF)"),
    ("崩拳·寸劲+1","step6: 14atk, 2x FORCE bonus = ~44-58 dmg (THE KILL)"),
    ("朝气蓬勃+1","step7: 9atk +1atk/force; spend 1qi -> +2force (dmg + fuel)"),
    ("崩拳·突",   "step8: 10atk, 碎防 (chips def; carries to next 崩拳)"),
]

DO_NOT_ROLL = ["崩拳·寸劲", "崩拳·降龙", "踏破九霄", "势如破竹", "气若悬河",
               "冲霄破浪", "朝气蓬勃", "磅礴之势", "天地浩荡"]

def main():
    print("=== 小布 g18 BURST 崩拳 BOARD (lobby winner, 命20) ===\n")
    for i, (card, why) in enumerate(BOARD, 1):
        print(f"slot {i}: {card:14s} -- {why}")
    print("\nWIN RATE (yisim, 5-10 reps): 100%/100% vs 牧逸风 base AND +1;")
    print("  100%/100% vs 吾行之 base AND +1; 100%/100% vs 谭舒雁 base;")
    print("  ~coin-flip vs 谭舒雁 FULLY +1 SECOND seat (her 内伤 burst is swingy).")
    print("\nREACHABLE NEAR-FIX: 崩拳·降龙+2 (lv3 = FOUR lv1 copies) flips 谭舒雁")
    print("  full-+1 second seat 0%->100% (search_board 3 reps). Hunt 3rd/4th 降龙 copy.")
    print("\nDO NOT ROLL/ABSORB:", ", ".join(DO_NOT_ROLL))
    print("\nTURN-3 BURST: 踏破九霄(+agi)->auto-chase->势如破竹(same turn)->寸劲 ~44-58 dmg. Kill t5-6.")

if __name__ == "__main__":
    main()
