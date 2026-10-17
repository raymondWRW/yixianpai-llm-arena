#!/usr/bin/env python3
"""Reference boards for 吾行之 (sect 五行 / sidejob 阵法师).
Run: python check_boards.py  — prints the v67 recipes. Edit RECIPES as meta shifts.
NOTE: these are the boards that this game's review found (evidence in notebook v67).
Mono-element rule: 五行天髓诀 only grants [再次行动] if the deck has ONE element."""
RECIPES = {
    # vs heal/tank (pid1-type, 静气心法 heal wall) — VERIFIED 100% both seats (R18 review)
    "vs_heal_wall": ["五行天髓诀+1","火灵·瞬燃","火灵·聚炎+1","火灵·轰爆+1","火灵阵+1","火灵·窜+2","火灵·灼心+1","火灵·烈燎原"],
    # vs burst (pid3 崩拳) — EXPECT LOSS; closest board found (survives to t8 vs t7)
    "vs_burst":     ["金灵·铁骨+2","金灵·铁骨+2","五行天髓诀+1","火灵阵+1","火灵·窜+2","火灵·轰爆+1","火灵·灼心+1","火灵·烈燎原"],
    # trap — do NOT build around: 天罡聚力阵 is 持续2次 = only 2 turns of +1加攻
    "trap_old":     ["天罡聚力阵","周天剑阵+1","火灵·聚炎+1","火灵·轰爆+1","火灵·窜+1","水灵·涛+1","金灵·穿心","金灵·针"],
}
def main():
    for name, board in RECIPES.items():
        assert len(board) <= 8, name
        mono = len(board)  # informational
        print(f"{name}: {board}")
    print("\nRULE: 五行天髓诀 needs deck = ONE element. 持续 caps at 2 per board.")
    print("RULE: 天罡聚力阵 fires only 2 turns — it is NOT a scaler.")
if __name__ == "__main__":
    main()
