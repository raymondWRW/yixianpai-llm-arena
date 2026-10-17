
# Helper: print the canonical W-board and the key swap rationale.
# Usage: run_program("wboard_check.py")
W_BOARD = ["探灵", "威震四方", "崩灭心法", "势如破竹", "势如破竹", "崩拳·寸劲", "朝气蓬勃+1", "磅礴之势"]
OLD_BOARD = ["探灵", "起势", "崩灭心法", "势如破竹", "势如破竹", "崩拳·寸劲", "朝气蓬勃+1", "磅礴之势"]

def main():
    print("W-BOARD (sect4 小布, sidejob7):")
    for i, c in enumerate(W_BOARD):
        print(f"  slot{i}: {c}")
    print()
    print("KEY FIX: 起势 -> 威震四方 (slot1).")
    print("  WHY: 威震四方 = +8 def, +3 max_force, +3 force upfront.")
    print("  vs pid1 谭舒雁 (内伤 sustain), OLD board lost 0% both seats vs +1 upgrade;")
    print("  NEW board wins 100% both seats vs base AND +1 upgrade (~t8).")
    print("  Do NOT drop the 2nd 势如破竹 or 威震四方: both alternatives lose t11 (bleed out).")
    print()
    print("Load-bearing: 威震四方(def+ramp), double 势如破竹(burst), 磅礴之势(finisher/shield),")
    print("  崩拳·寸劲(double-Force damage), 探灵(qi engine), 崩灭心法(Force/costHP).")

if __name__ == "__main__":
    main()
