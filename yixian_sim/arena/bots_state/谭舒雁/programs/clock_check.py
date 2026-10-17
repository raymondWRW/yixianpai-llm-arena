#!/usr/bin/env python3
"""Quick reference: the verified 内伤 CLOCK board + upgrade priority.
Usage: run_program('clock_check.py') to print the recipe.
This is a NOTES program; edit the lists as the meta shifts."""
CLOCK = ["命运轮回", "天星·牵引", "厄劫缠身", "血光之灾",
         "厄劫缠身", "血光之灾", "梅开二度", "杯弓蛇影"]
UPGRADE_ORDER = ["厄劫缠身", "血光之灾", "天星·牵引", "命运轮回", "杯弓蛇影", "梅开二度"]
AGO_FIRST_OPENERS = {"血光之灾", "厄劫缠身", "吉运初显", "落花有意"}

def main():
    print("=== 命理师 内伤 CLOCK (verified both seats vs all 3 rivals, g27) ===")
    print("Board:", " -> ".join(CLOCK))
    print()
    print("RULES:")
    print(" - Park [开局] 内伤 cards (血光之灾/厄劫缠身) in SLOTS 4 & 5 (0-idx 3,4):")
    print("   命运轮回 SKIPS their play but FIRES their [开局] free, 4 cycles.")
    print(" - 天星·牵引 early (slot1-2): triggers the NEXT 2 [开局] once each.")
    print(" - 梅开二度 IMMEDIATELY before 杯弓蛇影 = the finisher (doubles the whole tick).")
    print(" - 厄劫缠身 also DOWNGRADES foe's SAME-SLOT card (align to their finisher).")
    print()
    print("Upgrade priority:", " > ".join(UPGRADE_ORDER))
    print("Win window: ~turn 6-7. Clock reaches 16-18 内伤, ignores DEF, ticks at foe turn start.")
    print("DANGER: pure race vs 云剑 — ALWAYS sim BOTH seats; reorder if you only win going first.")
    print()
    print("[开局] cards that can be parked in slots 4/5:", ", ".join(sorted(AGO_FIRST_OPENERS)))

if __name__ == "__main__":
    main()
