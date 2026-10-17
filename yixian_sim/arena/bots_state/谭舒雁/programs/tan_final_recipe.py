"""
谭舒雁 (命理师/内伤+逆施) CANONICAL RECIPE + roll/seat guidance.
Verified game25 (R20 winner, 命2). Evidence in notebook.
Usage: run_program('tan_final_recipe.py', ['board'])
       run_program('tan_final_recipe.py', ['flex', 'cards','...'])
"""
import sys
a = sys.argv[1:]

# best verified board: 2x 内伤 before the engine, 逆施 for DEF->dmg, 御心 re-triggers opening
RECIPE = ["天机·逆施", "厄劫缠身", "血光之灾+1", "血光之灾",
          "天星·御心", "金蝉脱壳", "气疗术", "天机·顺应"]

def board():
    print("TAN SHUYAN (命理师) 内伤+逆施 BOARD — won game25 R20 (命2):")
    for i, c in enumerate(RECIPE):
        print(f"  slot{i+1}: {c}")
    print("\nWhy it wins (verified sims vs all 3 rival final boards + realistic +1):")
    print(" - INJURY is the win engine: 内伤 ticks at foe's turn-start, IGNORES DEF.")
    print("   Stack it to ~14: kills 崩拳/金灵/云剑 ramps by t9-10.")
    print(" - FRONT-LOAD 内伤: 厄劫缠身 (4 + opening downgrade) ASAP, then 血光 (1+1).")
    print("   slot0 天机·逆施 ramps qi immediately; 内伤 first is the alternative (both win).")
    print(" - 天机·逆施: every DEF/HP gain -> deal 50% to foe. TURN DEF CARDS INTO DAMAGE.")
    print(" - 天星·御心 re-triggers one earlier [开局] x2 -> doubles a 血光/厄劫 opening.")
    print(" - 金蝉脱壳/气疗术 = DEF/HP fuel for 逆施 (they ARE damage). 天机·顺应 = +40% def/hp.")
    print("\nFLEX (priority order for slots 5-8): 2nd 血光之灾 > 反震心法(anti multihit) > 气疗术.")
    print("  NEVER run 反震 as slot6 filler when a 2nd 内伤 card is available (cost me R20 damage).")

def flex(cards):
    print("Flex check for:", cards)
    base = [c.split('+')[0] for c in cards]
    inj = sum(1 for b in base if b in {"厄劫缠身","血光之灾","杯弓蛇影","落花有意"})
    has_engine = any(b in {"天机·逆施","天机·顺应"} for b in base)
    print(f" injury cards: {inj} (aim >=4). engine present: {has_engine}")
    if inj < 4:
        print(" WARNING: low 内伤 density -> will lose the ramp race vs 崩拳/云剑.")
    if not has_engine:
        print(" WARNING: no 逆施/顺应 -> DEF/HP cards deal NO damage.")

if not a or a[0] == "board":
    board()
elif a[0] == "flex":
    flex(a[1:])
else:
    board()
