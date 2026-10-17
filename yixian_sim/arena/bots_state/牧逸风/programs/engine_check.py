# engine_check.py — ecord the canonical cloud-sword engine boards for next game.
# Usage: run_program('engine_check.py')
# Prints the two seat-specialist boards + the universal board to field.
UNIVERSAL = ["聚灵心法+1","回响阵纹","化灵诀","云舞诀+1","巨鲲灵剑+1","白鹭灵剑+1","万法归灵剑","百鸟灵剑诀"]
FIRST_SEAT = ["聚灵心法+1","回响阵纹","百鸟灵剑诀","化灵诀","云舞诀","巨鲲灵剑+1","白鹭灵剑+1","万法归灵剑"]
CORE = ["聚灵心法", "回响阵纹", "万法归灵剑"]  # NEVER roll/absorb these

def main():
    print("CORE keep-list (never roll/absorb):", CORE)
    print("UNIVERSAL board (100/100 vs all rivals+master, both seats):", UNIVERSAL)
    print("FIRST-SEAT board (deep qi bank, 万法 slot8):", FIRST_SEAT)
    print("MECH: 聚灵心法+1 slot1 + 回响阵纹 retrigger = +2qi/turn; 万法 dumps for 5+5*qi.")
    print("SEAT NUANCE: 万法 slot7 fires t6 (go 2nd); slot8 banks 18qi=95dmg (go 1st).")

if __name__ == "__main__":
    main()
