# 谭舒雁 (命理师 sidejob7) — verified 内伤-clock recipe builder.
# KEY ORDER (g36 review, yisim-verified search_board, 100%/66% vs pid3 base,
#            80%/40% with 探灵 swap, 100%/100% vs pid0 and pid2):
#   [杯弓蛇影+1, 天星·牵引, 星弈·断(+2), 五雷轰顶+2, 天星·御心, 厄劫缠身, 血光之灾+1, 落花有意+1]
# Rules:
#   1. 杯弓蛇影 FIRST: seeds 3 内伤 + forces an immediate tick -> ~6 内伤 at t1.
#   2. 天星·牵引 SECOND: triggers the next 2 openings (厄劫/血光/牵引-related). +2 qi.
#   3. 星弈·断 mid: 22-28 dmg nuke, [星位] slot works (slot3 default 星位).
#   4. 五雷轰顶 as burst closer (30%*5 * 10-12).
#   5. 天星·御心 right AFTER the opening-heavy region (retrigger previous opening x2).
#   6. 厄劫缠身: 4 内伤 + [开局] downgrades enemy same-slot card. THE load-bearing piece.
#   7. 血光之灾+1: 2 内伤 + opening 1 内伤.
#   8. 落花有意+1: +2 qi + 1 内伤 (cheap filler, better than a 0-dmg defense card).
# NEVER field: 反震心法 / 诸事不宜 / 斗转星移 as pure defense (0 dmg = slow death).
# 内伤 ticks foe turn-start, ignores 防. Clock deals ~6-7/turn; burst closes t4-5.

BUILD = ["杯弓蛇影+1","天星·牵引","星弈·断+2","五雷轰顶+2","天星·御心","厄劫缠身","血光之灾+1","落花有意+1"]
CORE_HOLD = ["厄劫缠身","杯弓蛇影","天星·牵引","天星·御心","血光之灾","星弈·断","五雷轰顶"]

if __name__ == "__main__":
    print("BUILD (cyclic order):")
    for i, c in enumerate(BUILD, 1):
        print(f"  {i}. {c}")
    print("\nNEVER ABSORB/ROLL:", CORE_HOLD)
    print("Verified: 80%/40% vs 小布 base; 100%/100% vs 牧逸风 & 吾行之.")
