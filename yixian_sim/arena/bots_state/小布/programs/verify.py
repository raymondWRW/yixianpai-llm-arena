"""verify.py — reminder helper: print the current universal board recipe and
the merge-priority list for 小布 (崩拳/气势). Run with no args.
This is a reference card, not a simulator (the harness provides sim_matchup)."""

UNIVERSAL = ["探灵", "威震四方+1", "崩拳·降龙+1", "崩灭心法",
             "势如破竹", "崩拳·寸劲+1", "夜鬼啸+1", "磅礴之势"]
MERGE_PRIORITY = ["崩拳·寸劲", "夜鬼啸", "崩拳·降龙", "威震四方"]
RIVALS = {
    "pid0 牧逸风 (云剑 def)": "100% base; 100% vs +1 both seats (~7-8t)",
    "pid1 谭舒雁 (内伤/def-reflect)": "100% base; 100% FIRST vs +1; LOSE second vs +1 — SEAT decides",
    "pid2 吾行之 (水灵 scale)": "100% both seats even vs +1 (~7-8t) — KILL before t9",
}

if __name__ == "__main__":
    print("RECIPE (slot order):")
    for i, c in enumerate(UNIVERSAL, 1):
        print(f"  {i}. {c}")
    print("\nMERGE PRIORITY:", " > ".join(MERGE_PRIORITY))
    print("\nRIVAL RULES:")
    for k, v in RIVALS.items():
        print(f"  {k}: {v}")
    print("\nALWAYS: sim_matchup before set_board; check which seat; update key cards to lv2.")
