#!/usr/bin/env python3
"""牧逸风 g26 helper: the canonical 聚灵心法+回响 engine board and its two 万法-slot variants.
Print the two RECIPE orders to field per announced opponent. (No engine internals — just the boards.)"""

# THE SWEEP BOARD (万法 slot6, fast race) — beats 小布 100/100, 谭舒雁 100/100, 吾行之 100%first.
SWEEP = ["聚灵心法", "回响阵纹", "灵气灌注+1", "引气剑+1", "白鹭灵剑+1",
         "万法归灵剑+1", "百鸟灵剑诀", "云剑·汇灵"]

# THE TANK BOARD (万法 slot3, big qi bank) — beats 吾行之 100/100.
TANK = ["聚灵心法", "回响阵纹", "万法归灵剑+1", "灵气灌注+1", "引气剑+1",
        "百鸟灵剑诀", "云剑·汇灵", "白鹭灵剑+1"]

# NAMED KEEP-LIST — never roll/absorb these (2nd copy = merge).
KEEP = ["回响阵纹", "聚灵心法", "万法归灵剑", "百鸟灵剑诀", "白鹭灵剑", "云剑·汇灵",
        "灵气灌注", "引气剑", "化灵诀", "云舞诀", "云剑·点星"]

def pick(opponent="小布"):
    if "吾行之" in opponent:
        return TANK
    return SWEEP

if __name__ == "__main__":
    print("SWEEP (vs 小布/谭舒雁 — 万法 slot6, fast):")
    print(" ", SWEEP)
    print("TANK  (vs 吾行之 — 万法 slot3, big bank + lock seat):")
    print(" ", TANK)
    print("2 [持续] used: 聚灵心法 + 百鸟灵剑诀 (legal).")
    print("KEEP-LIST:", KEEP)
