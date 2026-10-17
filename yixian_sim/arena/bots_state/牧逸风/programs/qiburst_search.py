
# Helper: prints my known-good qi-burst board candidates for quick copy-paste.
# Core: ramp qi (云舞诀/聚灵阵/引气剑/聚灵丹) then 万法归灵剑 dumps ALL qi for one huge hit.
# 巨鹏灵剑 chains (再次行动) while qi>0 -> feeds 引气剑.
BOARDS = {
 "vs_pid1_win": ["云舞诀+2","巨鹏灵剑","引气剑","聚灵阵","万法归灵剑+1","云剑·无锋+1","巨鲸灵剑+1","云剑·探云+1"],
 "vs_all_win":  ["云舞诀+2","巨鹏灵剑","引气剑","聚灵阵","万法归灵剑+1","聚灵丹","巨鲸灵剑+1","云剑·探云+1"],
 "mirror_win":  ["云舞诀+2","巨鹏灵剑","引气剑","聚灵阵","万法归灵剑+1","聚灵丹","巨鲸灵剑+1","云剑·探云+1"],
}
if __name__ == "__main__":
    for k,v in BOARDS.items():
        print(k, "->", v)
