# Canonical 万法归灵剑 qi-nuke board for 牧逸风 (云剑 sect, sidejob 5).
# Verified g14 (WINNER) + g15 review: wins 100%/100% vs pid1,pid2,pid3, base AND +1, both seats.

CANONICAL = ["辟邪阵纹+1", "聚灵心法+1", "百鸟灵剑诀", "引气剑+1",
             "巨鲲灵剑+2", "白鹭灵剑", "御空剑阵", "万法归灵剑+2"]

SEARCHED = ["辟邪阵纹+1", "聚灵心法+1", "百鸟灵剑诀", "引气剑+2",
            "云剑·点星", "巨鲲灵剑+2", "白鹭灵剑", "万法归灵剑+2"]

# CP7: when ANY of these appears, HOLD it — never roll it away.
ENGINE_CARDS = {"万法归灵剑", "聚灵心法", "百鸟灵剑诀", "引气剑",
                "白鹭灵剑", "御空剑阵", "辟邪阵纹", "云剑·点星"}

PLACEHOLDER = ["凝意诀", "云舞诀", "引气剑+1", "灵感剑",
               "飞牙剑+1", "巨鹏灵剑", "破气剑", "不动金刚阵"]

# [持续]/[消耗] cards that count against the <=2 board cap.
# NOTE: 辟邪阵纹 is NOT persistent (one-shot "if a 持续 was played"); it does NOT count.
PERSISTENT = {"聚灵心法", "百鸟灵剑诀", "不动金刚阵", "云剑·柔心", "周天剑阵",
              "聚灵阵", "龟甲阵", "碎杀阵", "引雷阵", "万花迷魂阵", "狂剑·零式",
              "命运轮回", "水月剑阵", "天罡聚力阵", "八门金锁阵", "天运·趋吉", "天运·避凶"}

def base(name):
    return name.split('+')[0]

def is_engine(name):
    return base(name) in ENGINE_CARDS

def persistence_count(board):
    return sum(1 for c in board if base(c) in PERSISTENT)

def legality_ok(board):
    return persistence_count(board) <= 2

if __name__ == "__main__":
    for label, b in [("CANONICAL", CANONICAL), ("SEARCHED", SEARCHED), ("PLACEHOLDER", PLACEHOLDER)]:
        print(f"{label}: persistence={persistence_count(b)} legal={legality_ok(b)}")
