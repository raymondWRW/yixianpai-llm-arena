#!/usr/bin/env python3
"""Canonical 吾行之 water-engine recipe + ordering check notes.
Run: python water_recipe.py
Prints the locked board, the picklist, and the rules that produced it.
(No game API here — this is a memory aid; use sim_matchup in-game.)"""

BOARD = ["水灵阵", "水灵·纳百川", "水灵·波澜+1", "水灵·泉涌", "水灵·腾浪+1",
         "水灵·涛+1", "水灵·涛+1", "水灵·汹涌"]

NOTES = """
CANONICAL BOARD (g17-verified via yisim, 6 reps each):
  100%/100% BOTH SEATS vs 小布 final board  -> WIN
  100%/100% BOTH SEATS vs 谭舒雁 final board -> WIN
  0%/0% vs 牧逸风 final board (万法归灵剑 70-98 dmg t6-7) -> UNWINNABLE, accept.

ORDER RULES (each verified by moving one card):
  - 纳百川 must be slot 2-3 (EARLY). slot3+ -> second seat drops to 0%.
  - 水灵阵 slot 1 (持续 battery).
  - 泉涌 BEFORE payoff (it's the dmg->水势 growth engine).
  - 汹涌 LAST (payoff = 10 + 水势).
  - All qi generators (水灵阵/腾浪/泉涌) before 涛 (costs 2qi).

PICKLIST (never roll past, never absorb): 纳百川 > 须弥阵纹 > 水灵阵 > 泉涌 > 腾浪 > 汹涌 > 涛 > 波澜 > 水灵印 > 潜遁
ABSORB (for 修为/seat, the race that decides games): 金灵印/阵, 火灵·赤焰, 火灵印, 碎杀阵, 引雷阵,
  龟甲阵, 土灵·群山, 火灵阵, 五行刺, 周天剑阵, 天罡聚力阵, any off-engine card.

ECONOMY: ABSORB-HEAVY R1-R12 (rivals won the 修为 race 89-90 vs my 60 by doing this). 5-8 targeted
  rolls/round hunting engine pieces R7-R16. NEVER bank to 25 (wastes grant). NEVER shotgun 25 rolls.
"""

if __name__ == "__main__":
    print("BOARD:", BOARD)
    print(NOTES)
