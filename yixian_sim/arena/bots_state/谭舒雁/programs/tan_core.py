"""谭舒雁 星/内伤 core recipe board + evaluation helper.
Proven game 21 (1st place): beat all rivals 100% both seats (base & +1)."""

CORE = ["天元心法+1", "探灵", "厄劫缠身", "血光之灾", "流水无情",
        "星弈·断+1", "星弈·断", "落雷术+1"]

# Slot-by-slot WHY:
# 1 天元心法  - [持续] all slots = 星位, so 星弈·断 skip always fires
# 2 探灵      - qi engine BEFORE qi-cost cards (avoid starvation)
# 3 厄劫缠身  - 4 内伤 + downgrade opp's same-slot card
# 4 血光之灾  - 内伤 stack
# 5 流水无情  - 内伤 stack + atk
# 6-7 星弈·断 x2 - 22/16 atk + forced skip (cheap, unconditional). DOUBLE = load-bearing.
# 8 落雷术    - 9-20 big unconditional atk

# 内伤 mechanic (verified gamestate_full.js do_internal_injury):
#   flat reduce_idx_hp(N) at START of each turn, ignores DEF, NO RNG.
#   9 stacks => 9 dmg/turn guaranteed clock. THE win condition.

# Priority draws: 星弈·断 > 厄劫缠身 > 天元心法 > 探灵 > 血光/流水 > 落雷.
# Double 星弈·断 is critical (R19 loss was having only one).

if __name__ == "__main__":
    print("core board:", CORE)
    print("key: DOUBLE 星弈·断, 探灵 before qi-cost cards, 天元心法 for all-星位")
