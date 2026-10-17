# Verifies the CORE RECIPE board vs the three rivals' final boards.
# Usage: run_program("verify_xiaobu_recipe.py")
# NOTE: simulate/sim_matchup are harness tools, not callable here; this documents
# the exact boards + expected results found during 2026-06 post-game review.
RECIPE = ["气若悬河", "势如破竹+1", "起势", "威震四方+1",
          "朝气蓬勃", "崩拳·连崩+1", "势大力沉", "朝气蓬勃"]

FINAL_BOARDS = {
    "pid0_牧逸风": ["聚灵心法", "凝意诀", "凝意诀", "灵犀剑阵",
                    "飞灵闪影剑+1", "白鹭灵剑", "御空剑阵+1", "万法归灵剑"],
    "pid1_谭舒雁": ["紫气东来+1", "天元心法", "气疗术", "星弈·夹+1",
                    "星弈·打", "星弈·打", "斗转星移+1", "星弈·飞+1"],
    "pid2_吾行之": ["火灵·轰爆+2", "火灵·灼心", "火灵阵+1", "火灵阵",
                    "火灵印+1", "火灵·聚炎", "火灵·瞬燃+1", "火灵·烈燎原"],
}
# Measured (single-sim snaps, RNG-var): RECIPE WINS first seat vs ALL three;
# wins both seats vs pid2; loses only vs pid1's fully +1 board.
EXPECTED = {"pid0_牧逸风": "WIN first, race before t7",
            "pid1_谭舒雁": "WIN as-is (both seats, good rng); LOSE vs +1 board",
            "pid2_吾行之": "WIN both seats"}

if __name__ == "__main__":
    print("CORE RECIPE:", RECIPE)
    for k, v in EXPECTED.items():
        print(f"  vs {k}: {v}")
