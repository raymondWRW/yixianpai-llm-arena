# board W reference for 吾行之 (五行 + sidejob 5). ARENA g27 discovery.
# 水势(force_of_water) = DIRECT DAMAGE per [水灵] card played. Engine = qi batteries + 水势 ramp + attacker every slot.
BOARD_W = ["水灵·泉涌","水灵·波澜","五行刺+1","水灵·腾浪","水灵·潜遁","水灵·汹涌+1","水灵·纳百川","八门金锁阵"]
# beats 牧逸风 final+1 100% FIRST / 0% second; 小布 base 100%/0%; 谭舒雁 base 100%/0%. SEAT IS THE GAME.
SUBS = {"水灵·汹涌+1": ["水灵·涛","水灵·泉涌"],
        "八门金锁阵": ["辟邪阵纹+1","木灵·巡林","水灵·泉涌"],
        "五行刺+1": ["水灵·涛","火灵·烈燎原"]}
KEEP = ["水灵·泉涌","水灵·腾浪","水灵·波澜","水灵·涛","水灵·汹涌","水灵·纳百川","水灵·潜遁",
        "五行刺","八门金锁阵","不动金刚阵","金灵·穿心","木灵·巡林","辟邪阵纹","混元碎击","火灵·烈燎原","水灵阵"]
# PRIORITY ROLL TARGETS (R11+, named, budget<=6): 泉涌 ~ 腾浪 > 波澜 > 涛 > 汹涌 > 八门金锁阵
if __name__ == "__main__":
    print("BOARD_W:", BOARD_W)
