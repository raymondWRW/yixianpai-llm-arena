# g22 lesson: the 万法 board WITH 不动金刚阵 wins both seats vs 小布's burst board.
# Next game: after drawing 万法 + 不动金刚阵, field this recipe and sim_matchup both seats.
# Best board (yisim 100%/100% vs pid3's R13 final board):
BOARD_VS_XIAOBU = ["百鸟灵剑诀", "引气剑+1", "不动金刚阵", "云剑·点星",
                   "万法归灵剑+1", "白鹭灵剑+1", "辟邪阵纹", "云剑·点星"]
BOARD_VS_TAN = ["辟邪阵纹", "百鸟灵剑诀", "引气剑+1", "不动金刚阵",
                "云剑·点星+1", "万法归灵剑+1", "白鹭灵剑+1", "云剑·点星"]
# Usage: sim_matchup(my_cards=BOARD_VS_XIAOBU, opp_pid=3); if 100%/100% AND you hold these cards -> field it.
# KEY mechanical note: 不动金刚阵 = +7def AND +7hp/maxHP per turn when NOT chasing -> converts the burst race.
print("g22 recipe boards loaded. Field only if you HOLD 万法 + 不动金刚阵 + 引气(剑) + 百鸟 + 白鹭.")
