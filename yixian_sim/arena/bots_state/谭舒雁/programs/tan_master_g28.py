# 谭舒雁 g28 MASTER BOARD — 100/100 vs all three g28 final boards (both seats).
# yisim sim_matchup verified 5 reps. Mechanism: slot-2 厄劫缠身 downgrades opp slot-1 qi engine
# (聚灵心法 lv2->lv1 halves qi/turn) => 万法 deals 75 not 89 => survive => clock wins t11.
# ORDER IS LOAD-BEARING: 厄劫 at slot 2. Moving it loses.
MASTER_BOARD = ["天星·牵引", "厄劫缠身", "杯弓蛇影", "杯弓蛇影",
                "诸事不宜", "诸事不宜", "厄劫缠身", "命运轮回"]

# Alternative finisher if 五雷轰顶 drawn: (still 100/100 as-is; 33% vs 小布 +1)
MASTER_BOARD_ALT = ["天星·牵引", "厄劫缠身", "杯弓蛇影+1", "杯弓蛇影",
                    "诸事不宜", "诸事不宜", "厄劫缠身", "五雷轰顶"]

# Fallback if NO 厄劫 available (g27 3-clock; loses to 牧逸风 only):
FALLBACK_3CLOCK = ["天星·牵引", "厄劫缠身", "杯弓蛇影", "杯弓蛇影",
                   "诸事不宜", "诸事不宜", "命运轮回", "杯弓蛇影"]

KEEP_LIST = ["厄劫缠身", "杯弓蛇影", "诸事不宜", "命运轮回", "天星·牵引",
             "血光之灾", "落花有意", "吉运初显"]
BAN_LIST = ["反震心法", "海底捞月"]

if __name__ == "__main__":
    print("MASTER:", MASTER_BOARD)
    print("KEEP:", KEEP_LIST)
    print("BAN:", BAN_LIST)
