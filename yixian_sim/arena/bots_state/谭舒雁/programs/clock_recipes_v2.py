#!/usr/bin/env python3
"""命理师 内伤 CLOCK — reference boards & roll targets. v2 (g30). run_program to print."""

# g30 MINIMAL canonical (from held cards, 100%/100% both seats vs all 3 rivals, yisim-verified)
CLOCK_MIN = ["落花有意", "流水无情+1", "天星·牵引", "梅开二度",
             "厄劫缠身", "天星·御心", "天星·御心", "吉运初显"]

# Full clock (命运轮回 park)
CLOCK_FULL = ["命运轮回", "天星·牵引", "厄劫缠身", "血光之灾",
              "厄劫缠身", "血光之灾", "梅开二度", "杯弓蛇影"]

# Downgrade clock (pid0 云剑 killer)
CLOCK_DOWNGRADE = ["流水无情+1", "天星·牵引", "厄劫缠身", "天星·御心",
                   "杯弓蛇影+2", "血光之灾", "杯弓蛇影", "血光之灾+1"]

# NAMED ROLL TARGETS in priority order. 厄劫缠身 is the ONE-CARD flip (g30).
ROLL_TARGETS = ["厄劫缠身", "天星·御心", "血光之灾", "命运轮回",
                "杯弓蛇影", "梅开二度", "天星·牵引"]
DO_NOT_ABSORB = set(ROLL_TARGETS) | {"流水无情", "落花有意"}
UPGRADE_ORDER = ["厄劫缠身", "血光之灾", "天星·牵引", "命运轮回", "杯弓蛇影", "梅开二度"]

RULES = """
- 内伤 ticks at FOE turn START, IGNORES DEF. THE clock is the win con, not played attacks.
- 厄劫缠身 is the #1 card: retriggered by BOTH 天星·牵引 (before) and 天星·御心 (after).
  A retrigger engine with no 厄劫/血光 = dead weight (g30 lost this way).
- 天星·御心 = retrigger PREVIOUS opening x2 (put AFTER 厄劫缠身/血光). [card_actions.js:8966]
- 天星·牵引 = retrigger NEXT 2 openings x1 (put BEFORE 厄劫缠身/血光). [card_actions.js:8988]
- 命运轮回 skips slots 4&5 play but FIRES their opening (park 血光/厄劫 there). [gs:3307]
- ALWAYS sim BOTH seats. vs 云剑, pure clock wins only going first — need 厄劫缠身.
- DON'T dilute: max 1-2 utility slots; the rest clock.
- Bank 5-10 exchanges R10-R12 to fund the R13+ 厄劫缠身 hunt. Don't absorb junk at top 修为.
"""

if __name__ == "__main__":
    print("=== 命理师 内伤 CLOCK recipes (v2, g30) ===")
    print("MIN (g30):    ", " -> ".join(CLOCK_MIN))
    print("FULL:         ", " -> ".join(CLOCK_FULL))
    print("DOWNGRADE:    ", " -> ".join(CLOCK_DOWNGRADE))
    print()
    print("Roll targets:", " > ".join(ROLL_TARGETS))
    print("Upgrade order:", " > ".join(UPGRADE_ORDER))
    print(RULES)
