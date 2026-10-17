"""
谭舒雁 (命理师/career 7) — g21 verified recipes.
run_program('tan_g21_antiwanfa.py', ['antiwanfa'])  -> the 厄劫缠身 board (vs 万法/burst)
run_program('tan_g21_antiwanfa.py', ['clock'])      -> the C6 8-slot clock (vs 崩拳/tank)
run_program('tan_g21_antiwanfa.py', ['rolls'])      -> roll targets from R12
"""
import sys
a = sys.argv[1:]

# g21 yisim-verified: 100% FIRST / 0% SECOND vs 牧逸风's EXACT 万法 board (base).
ANTIWANFA = ["杯弓蛇影+1", "厄劫缠身", "天星·牵引", "血光之灾",
             "梅开二度", "杯弓蛇影+2", "杯弓蛇影", "流水无情"]

# g20 verified: 100% first / 100% second vs 小布's fielded 崩拳 board.
CLOCK = ["天星·牵引", "血光之灾", "天星·御心", "诸事不宜",
         "落花有意", "梅开二度", "杯弓蛇影+2", "流水无情"]

def show(name, b, why):
    print(f"{name} (8 slots):")
    for i, c in enumerate(b):
        print(f"  slot{i+1}: {c}")
    print(why)

if not a or a[0] == "antiwanfa":
    show("ANTI-万法 / ANTI-BURST BOARD (needs 厄劫缠身, career 7, 6 copies @境5)", ANTIWANFA,
         "  - 厄劫缠身 slot2 downgrades enemy feeder, OR slot8 downgrades enemy 万法 (95->80).\n"
         "  - 4-6 内伤 pushes clock to 16-17 by t8 = kills 109-130 HP.\n"
         "  - Win ONLY going FIRST (t8 tick before their dump). Sim both seats.\n"
         "  - REACHABILITY: 厄劫缠身 is in MY OWN sidejob pool. ROLL IT BY NAME FROM R12.")
elif a[0] == "clock":
    show("C6 CLOCK (default, no 厄劫缠身)", CLOCK,
         "  - 诸事不宜 is load-bearing vs burst (-6 x2 hits). Removing it = 100%->20% (g20).\n"
         "  - 梅开二度 doubles 杯弓蛇影+2 -> 10 内伤 tick. Order matters. Sim before fielding.")
elif a[0] == "rolls":
    print("ROLL TARGETS FROM R12 (境5 gate):")
    print("  1. 厄劫缠身  (3.1%/roll, 6 copies) — THE anti-burst/万法 card. #1 PRIORITY.")
    print("  2. 杯弓蛇影  (merge -> +2/+3, bigger tick) — 4 left.")
    print("  3. 梅开二度  (double the biggest 内伤 ticker) — 5 left.")
    print("  4. 血光之灾 / 天星·御心 / 天星·牵引 (more opening stacks) — 7/4/3 left.")
    print("  NEVER: 反震心法/斗转星移/察体 as 0-dmg fillers.")
else:
    show("ANTI-万法 BOARD", ANTIWANFA, "")
