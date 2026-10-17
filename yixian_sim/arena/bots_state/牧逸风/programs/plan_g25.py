"""Plan helper for 牧逸风 (云剑+阵法师5). Encodes the g24-verified win-con.
Usage: run_program('plan_g25.py', ['wincon']) prints the target board + thresholds."""
import sys

WINCON = ["辟邪阵纹+1", "聚灵心法+1", "百鸟灵剑诀+1", "引气剑+1",
          "巨鲲灵剑+2", "白鹭灵剑", "万法归灵剑+1", "云剑·点星"]

RECIPE_A = ["百鸟灵剑诀", "引气剑", "巨鲲灵剑+1", "白鹭灵剑+1", "巨鲲灵剑",
            "聚灵心法", "辟邪阵纹", "灵气灌注"]

NOTES = """
g24-verified facts:
- WIN-CON (万法 lb2 board): 100%/100% vs 小布 final board (t6, 万法=59), vs 谭舒雁 C7 (t7, 万法=77), vs 吾行之 base+1.
- 万法 lv1: wins vs 小布 base ONLY going first. lv2 = both seats.
- RECIPE A win threshold: 百鸟+1 OR 白鹭+2 OR 2x巨鲲+1.  白鹭+1 ALONE = LOSS.
- Named roll targets at 境5 (in order): 万法归灵剑(3.0%/roll) > 白鹭灵剑(1.5%) > 百鸟灵剑诀(3.5%).
- NEVER roll before 境5 unlocks your target. NEVER shotgun. Absorb everything R1-R9 for 修为/seat.
"""

def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else "wincon"
    if arg == "wincon":
        print("WIN-CON:", WINCON)
        print(NOTES)
    elif arg == "recipeA":
        print("RECIPE A:", RECIPE_A)

if __name__ == "__main__":
    main()
