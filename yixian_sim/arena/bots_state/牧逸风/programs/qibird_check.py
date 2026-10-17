
# QIBIRD recipe reference + quick self-note. Not a sim driver (use tools for that).
# Store the verified g23 winning board so future-me can re-test it as a SEARCH SEED.
QIBIRD = ["百鸟灵剑诀+1", "引气剑+1", "云剑·点星+1", "云剑·点星",
          "化灵诀", "回响阵纹", "白鹭灵剑+1", "万法归灵剑+1"]

def main():
    print("RECIPE QIBIRD (g23, yisim-verified 100%/100% both seats vs 吾行之/小布/谭舒雁 exact boards, ~t8):")
    for i, c in enumerate(QIBIRD):
        print(f"  slot{i+1}: {c}")
    print()
    print("KEY RULES:")
    print(" - 百鸟灵剑诀+1 must be SLOT 1 (it is [持续]); 回响阵纹 retriggers slot1 -> +6 qi/turn.")
    print(" - 回响 in slot1 and 百鸟 elsewhere = NOTHING (proven 0%/0%).")
    print(" - 万法+1 (5+6*qi) LAST: dump 15-17 qi = 78-107 dmg one-shot.")
    print(" - 万法 base wins only 1st seat; 百鸟 base -> full loss. Need BOTH at +1 for both seats.")
    print(" - DROP 巨鲲 (steals 3qi/cycle from 万法).")
    print("Use as search_board(start=QIBIRD, lock_cards=['万法归灵剑+1','百鸟灵剑诀+1','回响阵纹']).")

if __name__ == "__main__":
    main()
