"""field_audit.py — reminder checklist for end-of-round (g14 lesson).
Prints the pre-end_turn ritual so I never again leave a win-con card in hand
while fielding an inferior board.
Usage: python field_audit.py <round> <banked_exchanges> <hand...>
"""
import sys

def main():
    args = sys.argv[1:]
    rnd = args[0] if len(args) > 0 else "?"
    bank = args[1] if len(args) > 1 else "?"
    hand = args[2:] if len(args) > 2 else []
    print(f"=== PRE-END_TURN RITUAL (round {rnd}) ===")
    print("1. Build best board FROM hand+board (sim it vs announced opp, >=5 reps both seats).")
    print("2. Is any ENGINE piece in hand unfielded? WIN-CONS: 天机·逆施, 厄劫缠身, 浩然正气,")
    print("   诸事不宜, 探灵, 踏破九霄, 磅礴之势, 势如破竹, 血光之灾.  -> FIELD IT.")
    print("3. set_board FIRST, THEN roll leftovers (never roll a sole-copy win-con).")
    print("4. Spend banked exchanges on TARGETED rolls for missing win-cons (5-8/round).")
    print(f"   Banked now = {bank} (cap 25; >21 wastes next grant).")
    print(f"HAND: {hand}")
    print("5. THEN end_turn.")

if __name__ == "__main__":
    main()
