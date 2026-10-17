# g24 (ARENA 24) — the two verified 100%/100% 万法-engine boards.
# ENGINE: 聚灵心法+1 SLOT1 + 回响阵纹 retrigger = double qi ramp -> 万法 banks 17-20qi = one-shot kill.
BOARD_A = ["聚灵心法+1","百鸟灵剑诀+1","回响阵纹","万法归灵剑+1","云舞诀+2","云剑·点星","白鹭灵剑","巨虎灵剑+1"]
# vs 吾行之 (水灵 200HP heal-tank) 100/100 ; vs 谭舒雁 (内伤 clock) 100/100. LOSES 0/0 to 小布 (too slow).
BOARD_B = ["聚灵心法+1","百鸟灵剑诀+1","回响阵纹","引气剑","云舞诀+1","万法归灵剑+1","白鹭灵剑","巨虎灵剑+1"]
# vs 小布 (崩拳 burst) 100/100 (万法 t6 ~101 dmg, antes del combo). LOSES 0/0 to 吾行之 (万法 ~70, no lethal).
def which(opp_name):
    if "小布" in opp_name: return BOARD_B
    return BOARD_A  # 吾行之 / 谭舒雁 / default
