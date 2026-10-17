"""
WATER ENGINE reference for 吾行之 (五行 sect, sidejob 5 阵法师).
Prints the canonical water board and the picklist. Use as `start` for search_board
and as the tuning template each round. Verified R17 review: WIN 100% both seats
vs pid0/pid1/pid3 FINAL boards (3+ reps, simulate + search_board).

Why it works (ONE LINE): 水势(force_of_water) is BOTH maxHP (纳百川 +6/stack) AND
damage (汹涌 +1 atk/stack), so it out-scales both pid1's Qi-Therapy heal and pid3's
崩拳 ramp. 水灵阵(continuous) + 须弥阵纹(skip+chase) loops 泉涌 to build qi+水势 fast.
"""
BOARD = [
    "水灵阵",        # continuous: +1 qi per 水灵 card -> qi engine
    "须弥阵纹+1",     # skip next + chase if continuous used -> loops 泉涌 (CORE)
    "水灵·泉涌",      # +2 qi, +1 水势 per 5 dmg -> qi + 水势 builder
    "水灵·泉涌",      # second copy
    "水灵·腾浪+1",    # +qi, +1 水势 per 2 qi -> 水势 builder
    "水灵·涛+1",      # 13atk flat + 水势, reliable mid-turn hit
    "水灵·纳百川",    # +6 HP&MaxHP per 水势 -> massive sustain (beats healers)
    "水灵·汹涌",      # 10+atk, +1 atk per 水势 -> FINISHER (place LAST)
]

# Picklist priority (grab on sight; do NOT roll past these):
PICKLIST = ["水灵·泉涌", "水灵·纳百川", "须弥阵纹", "水灵·腾浪",
            "水灵·汹涌", "水灵阵", "水灵·涛", "水灵·波澜", "水灵·印"]

# Order rules (verified via search_board trace):
#  水灵阵 slot0; 须弥阵纹 slot1; 泉涌 early; 纳百川 before 汹涌; 汹涌 LAST.

if __name__ == "__main__":
    print("CANONICAL WATER BOARD (cyclic order):")
    for i, c in enumerate(BOARD):
        print(f"  {i}: {c}")
    print("\nPICKLIST:", " > ".join(PICKLIST))
    print("\nRoll heavy R4-R9 for 泉涌/腾浪/水灵阵/纳百川; cap ~6 rolls/round; STOP on a hit.")
    print("Merge duplicate 泉涌/腾浪 for +lvl. Absorb all non-water spares for 修为.")
