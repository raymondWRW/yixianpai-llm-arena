"""
谭舒雁 命理师(7) CANONICAL g26 double-诸事 clock.
Usage: run_program('g26_clock.py')
Prints the canonical board + keep-list + named roll targets.
"""
CANON = ["天星·牵引","厄劫缠身","杯弓蛇影+1","杯弓蛇影",
         "诸事不宜","诸事不宜","命运轮回","命运轮回"]
FLEX  = ["天星·牵引","厄劫缠身","杯弓蛇影+1","杯弓蛇影",
         "诸事不宜","诸事不宜","命运轮回","吉运初显"]  # 2nd 命运 -> 吉运初显
KEEP = ["诸事不宜","厄劫缠身","杯弓蛇影","命运轮回","天星·牵引",
        "吉运初显","流水无情","血光之灾","落花有意","梅开二度"]
ROLL_TARGETS = ["诸事不宜","厄劫缠身","杯弓蛇影","命运轮回",
                "天星·牵引","吉运初显","流水无情","血光之灾"]

def main():
    print("CANONICAL g26 CLOCK (100% both seats vs all 3 rivals' ACTUAL final boards):")
    for i,c in enumerate(CANON,1): print(f"  slot{i}: {c}")
    print("\nFLEX variant (2nd 命运轮回 -> 吉运初显):")
    for i,c in enumerate(FLEX,1): print(f"  slot{i}: {c}")
    print("\nKEEP-LIST (NEVER roll/absorb):", ", ".join(KEEP))
    print("NAMED ROLL TARGETS (in order, STOP when one lands):", ", ".join(ROLL_TARGETS))
    print("\nLOAD-BEARING: 诸事不宜 x2 (single loses to 小布's chase burst).")
    print("R1-R9: absorb-all, ZERO rolls. R10: break 境5. R10-R15: named rolls <=6/round. R16-17: mass-merge.")

if __name__ == "__main__":
    main()
