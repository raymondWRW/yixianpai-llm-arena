"""g22 小布 canonical 崩拳/气势 burst boards + per-opponent orders.
Prints the boards to field and the named-roll priority list. No engine access needed."""

CANONICAL = ["崩拳·降龙+1", "崩拳·连崩", "威震四方", "冲霄破浪+1", "踏破九霄",
             "崩拳·寸劲", "崩拳·戳", "崩拳·突"]
# key order lesson (g22): 连崩 in SLOT 2 (before 威震四方) pre-buffs the line -> flipped 谭舒雁 matchup 0%->100%.

NO_WEIZHEN = ["崩拳·降龙+1", "崩拳·缠+1", "冲霄破浪", "踏破九霄", "崩拳·寸劲",
              "崩拳·连崩", "崩拳·戳", "崩拳·突"]  # g20 lobby winner, but 0% vs 万法 board

ANTI_CLOCK = ["崩拳·降龙+1", "玄心斩魄", "威震四方", "冲霄破浪+1", "踏破九霄",
              "崩拳·连崩", "崩拳·寸劲", "崩拳·突"]  # vs 谭舒雁 / any 内伤-debuff foe

NAMED_ROLLS = ["威震四方", "崩拳·连崩", "崩拳·寸劲", "崩拳·降龙", "冲霄破浪", "踏破九霄"]
UPGRADE_PRIORITY = ["崩拳·寸劲", "崩拳·降龙", "冲霄破浪", "踏破九霄", "势大力沉"]

def board_for(opp):
    if opp in (1, "谭舒雁", "内伤", "clock"):
        return ANTI_CLOCK
    if opp in (0, "牧逸风", "万法"):
        return CANONICAL
    if opp in (2, "吾行之", "水灵", "tank"):
        return CANONICAL
    return CANONICAL

if __name__ == "__main__":
    import sys
    print("g22 canonical burst board:", CANONICAL)
    print("anti-clock variant:      ", ANTI_CLOCK)
    print("named-roll order:        ", NAMED_ROLLS)
    print("upgrade priority:        ", UPGRADE_PRIORITY)
    if len(sys.argv) > 1:
        print("board for", sys.argv[1], "->", board_for(sys.argv[1]))
