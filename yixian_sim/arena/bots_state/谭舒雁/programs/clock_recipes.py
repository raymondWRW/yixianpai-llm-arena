#!/usr/bin/env python3
"""命理师 内伤 CLOCK — reference boards & roll targets. Edit as meta shifts.
run_program('clock_recipes.py') to print."""

# RECIPE A — full clock (g27, verified both seats vs all rivals). Slot 4&5 = 命运轮回 park.
CLOCK_FULL = ["命运轮回", "天星·牵引", "厄劫缠身", "血光之灾",
              "厄劫缠身", "血光之灾", "梅开二度", "杯弓蛇影"]

# RECIPE B — DOWNGRADE clock (g29, search_board 100%/100% both seats vs pid0 云剑).
# 天星·御心 right AFTER 厄劫缠身 fires its [开局] TWICE = double downgrade + double 内伤.
CLOCK_DOWNGRADE = ["流水无情+1", "天星·牵引", "厄劫缠身", "天星·御心",
                   "杯弓蛇影+2", "血光之灾", "杯弓蛇影", "血光之灾+1"]
# Minimal version (even 1 lv1 厄劫缠身 works vs pid0 base):
CLOCK_DOWNGRADE_MIN = ["天星·牵引", "落花有意", "厄劫缠身", "天星·御心",
                       "杯弓蛇影", "血光之灾", "杯弓蛇影", "血光之灾+1"]

# NAMED ROLL TARGETS in priority order — hunt these R9+.
ROLL_TARGETS = ["厄劫缠身", "天星·御心", "血光之灾", "杯弓蛇影",
                "命运轮回", "梅开二度", "天星·牵引"]
# NEVER absorb these for 修为 once you hold >=2 clock pieces.
DO_NOT_ABSORB = set(ROLL_TARGETS) | {"流水无情", "落花有意"}
UPGRADE_ORDER = ["厄劫缠身", "血光之灾", "天星·牵引", "命运轮回", "杯弓蛇影", "梅开二度"]

RULES = """
- 内伤 ticks at FOE turn START, IGNORES DEF. The clock is the win con, not played attacks.
- 天星·御心 = retrigger PREVIOUS opening x2 (put AFTER 厄劫缠身). [card_actions.js:8966]
- 天星·牵引 = retrigger NEXT 2 openings x1. [card_actions.js:8988]
- 命运轮回 skips slots 4&5 play but FIRES their opening (park 血光/厄劫 there). [gs:3306]
- 厄劫缠身 [开局] DOWNGRADES foe's same-slot card — hit their qi engine / finisher.
- ALWAYS sim BOTH seats. vs 云剑, pure clock wins only going first — need the downgrade pieces.
- DON'T dilute: max 1-2 utility slots; every other slot is clock.
"""

if __name__ == "__main__":
    print("=== 命理师 内伤 CLOCK recipes ===")
    print("A (full):     ", " -> ".join(CLOCK_FULL))
    print("B (downgrade):", " -> ".join(CLOCK_DOWNGRADE))
    print("B-min:        ", " -> ".join(CLOCK_DOWNGRADE_MIN))
    print()
    print("Roll targets:", " > ".join(ROLL_TARGETS))
    print("Upgrade order:", " > ".join(UPGRADE_ORDER))
    print(RULES)
