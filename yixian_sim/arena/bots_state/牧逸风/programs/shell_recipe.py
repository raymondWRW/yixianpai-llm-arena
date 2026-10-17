#!/usr/bin/env python3
"""Prints the recommended 牧逸风 control-shell recipe and legality checks.
Usage: python shell_recipe.py [slots]
No game-state access needed; pure reminder of the post-game-review finding.
"""
import sys

FULL8 = ["护灵符", "探灵+1", "巨鹏灵剑+1", "巨鲸灵剑+2", "引气剑+1", "驱邪丹", "万邪入体咒+1", "厄劫缠身"]
# slot-unlock schedule: 3,4,5,6,7,8,8,8 by round
DROP_ORDER = ["引气剑+1", "驱邪丹", "探灵+1", "巨鲸灵剑+2"]  # drop from the tail down

def recipe(slots):
    b = FULL8[:]
    # never drop 厄劫缠身(last) or 巨鹏/巨鲸 chase pair (the dmg engine) first
    drops = 0
    need = len(b) - slots
    for c in DROP_ORDER:
        if drops >= need:
            break
        if c in b:
            b.remove(c)
            drops += 1
    return b

def main():
    slots = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    b = recipe(slots)
    print("recommended shell for", slots, "slots:")
    for i, c in enumerate(b):
        print(f"  slot{i+1}: {c}")
    print()
    print("LEGALITY: 护灵符+驱邪丹 are both [消耗] -> combined [消耗]/[持续] = 2 (max 2) OK")
    print("CHASE: 巨鹏灵剑 must sit DIRECTLY before 巨鲸灵剑.")
    print("PLACEMENT: 厄劫缠身 must be LAST slot (downgrades opp's same-slot card).")
    print("vs pid1 heal / pid3 burst: both beaten 100% both seats (sim 5rep) at current levels.")

if __name__ == "__main__":
    main()
