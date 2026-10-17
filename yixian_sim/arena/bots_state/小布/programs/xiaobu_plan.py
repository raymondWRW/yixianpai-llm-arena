"""
小布 (崩拳 sect4 + sidejob7 命理师) decision helper.
Usage: run_program('xiaobu_plan.py', ['<my_pid>', '<my_soul>', '<their_soul>', '<banked_ex>'])
Prints: core-board status, seat advice, economy advice.
"""
import sys

CORE = ["威震四方", "崩拳·寸劲", "磅礴之势"]  # mandatory, per notebook
ENGINE = ["抱气法", "气若悬河", "势如破竹", "崩拳·降龙", "朝气蓬勃"]

def has(card, board):
    return any(c.split("+")[0] == card for c in board)

def main():
    args = sys.argv[1:]
    me_soul = int(args[1]) if len(args) > 1 else 0
    opp_soul = int(args[2]) if len(args) > 2 else 0
    ex = int(args[3]) if len(args) > 3 else 0
    print("=== 小布 plan ===")
    print("CORE cards (must be fielded):", CORE)
    print("  order: 抱气->气若悬河->威震四方(cap!)->势如破竹->降龙->寸劲(x2F)->朝气蓬勃->磅礴之势(finisher)")
    if me_soul > opp_soul:
        print("SEAT: you act FIRST. Good - vs pid0/pid1 that's the win condition.")
    elif me_soul < opp_soul:
        print("SEAT: you act SECOND. Absorb junk cards now to claw back 修为 lead!")
    else:
        print("SEAT: TIE = coin flip. Absorb junk to break the tie in your favor.")
    if ex >= 23:
        print(f"ECONOMY: {ex} exchanges banked (cap 25) - SPEND down now or waste next grant.")
    else:
        print(f"ECONOMY: {ex} exchanges. Rolling toward core cards is fine.")

if __name__ == "__main__":
    main()
