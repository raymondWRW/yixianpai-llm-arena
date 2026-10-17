"""
reorder_check.py — 五行 (吾行之) board ORDER helper.

The lesson (g29/g30): for the 水灵 board the COMPOSITION is rarely the problem — ORDER is.
g30 VERIFIED board (100%/100% BOTH seats vs 谭舒雁 AND 牧逸风, their actual final boards):
  [周天剑阵+1, 水灵·腾浪, 水灵阵, 水灵·纳百川, 水灵·汹涌+1, 水灵·汹涌+1, 水灵·潜遁, 五行刺+1]
Load-bearing moves vs my g30 R15/R16 fieldings:
  (1) 周天剑阵 (Endless Sword Formation) -> SLOT 1  (slot 7+ = 0 charges = 0 dmg).
  (2) 水灵·潜遁 (Dive) -> LATE (slot 6-7)           (slot 3 = -40% wasted on small early hits).
vs 小布 (崩拳 burst): 0%/0% UNWINNABLE — accept and minimize 命.
"""
import sys

CP6 = ["周天剑阵+1", "水灵·腾浪", "水灵阵", "水灵·纳百川",
       "水灵·汹涌+1", "水灵·汹涌+1", "水灵·潜遁", "五行刺+1"]

RULES = [
    "周天剑阵(Endless Sword Formation) -> SLOT 1 (charges fire from t1; slot 7+ = 0 dmg)",
    "水灵·腾浪(Great Waves) -> SLOT 2 (qi engine, no dry turns)",
    "水灵·潜遁(Dive) -> SLOT 6-7 (late -40%; slot 3 = wasted on small early hits)",
    "五行刺(Five Elements Fleche) -> SLOT 8 (scales with any active 五行)",
    "NEVER field 须弥阵纹 (Meru Formation) — proven dud (M87)",
    "NEVER field 木灵·柳纷飞 as filler if you hold 五行刺+1 (M90)",
    "ALWAYS run sim_matchup BOTH seats vs as-is AND +1 before committing.",
]

def main():
    print("=== 五行 g30-VERIFIED ORDER (100/100 vs 谭/牧 both seats) ===")
    for i, c in enumerate(CP6):
        print(f"  slot {i+1}: {c}")
    print("\n=== LOAD-BEARING REORDER RULES ===")
    for r in RULES:
        print(f"  - {r}")

if __name__ == "__main__":
    main()
