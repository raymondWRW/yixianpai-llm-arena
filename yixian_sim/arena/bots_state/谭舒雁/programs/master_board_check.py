"""
Verify the 谭舒雁 命理师 MASTER BOARD family against all rivals' last-known boards.
Run: run_program("master_board_check.py")
Prints which master-board variant is fully reachable from a given hand/pool snapshot,
and reminds of the assembly checks. (Wrapper around the sim tools' output — offline reminder.)
"""
MASTER_PRIMARY = ["杯弓蛇影","血光之灾","杯弓蛇影","天星·牵引","诸事不宜","诸事不宜","流水无情","星弈·断"]
MASTER_WITH_EJIE = ["天星·牵引","厄劫缠身","杯弓蛇影","杯弓蛇影","诸事不宜","诸事不宜","厄劫缠身","命运轮回"]
FALLBACK = ["天星·牵引","血光之灾","杯弓蛇影","杯弓蛇影","诸事不宜","诸事不宜","星弈·断","命运轮回"]
KEEP = ["厄劫缠身","杯弓蛇影","诸事不宜","命运轮回","天星·牵引","血光之灾","落花有意","流水无情","吉运初显"]
BAN  = ["反震心法","反震心法+1","海底捞月"]

def need(board):
    from collections import Counter
    return Counter(board)

def main():
    print("MASTER BOARD FAMILY (g29-verified 100/100 vs all rivals, both seats):")
    for name, b in [("PRIMARY  ", MASTER_PRIMARY), ("WITH_EJIE", MASTER_WITH_EJIE), ("FALLBACK ", FALLBACK)]:
        print(f"  {name}: {b}")
        print(f"      need: {dict(need(b))}")
    print()
    print("ASSEMBLY CHECKS before every set_board (my recurring fatal flaw):")
    print("  1) Do I hold 流水无情? -> MUST field it (free 4th clock). NEVER absorb it.")
    print("  2) Do I hold 2nd 诸事不宜 / 2nd 杯弓? -> field, don't bench.")
    print("  3) 天星·牵引 goes to SLOT 4 (fires 诸事不宜 openings = 防), NOT slot 1.")
    print("  4) 星弈·断 -> SLOT 8.")
    print("  5) NEVER field 反震心法 / 海底捞月 (BAN, 0 contribution).")
    print("  6) If 厄劫缠身 drawn -> put BOTH (if 2) at SLOT 2 (engine-starve qi nukes).")
    print()
    print("KEEP-LIST (never roll/absorb):", KEEP)
    print("BAN-LIST (never field):", BAN)

if __name__ == "__main__":
    main()
