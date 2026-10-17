"""Post-game / in-game helper: report the anti-injury hexproof delta and remind of the
pid1 fix. Run with no args. It only reads the yisim source to re-confirm the injury
mechanic (internal_injury = stack count, DEF-ignoring, hexproof absorbs 1 instance/stack).
"""
import os, re
d = os.environ['YISIM_DIR']
gs = open(os.path.join(d, 'gamestate_full.js'), errors='ignore').read()
# 1) injury damage = stack count
m1 = 'amt = me.internal_injury' in gs and 'this.reduce_idx_hp(idx, amt)' in gs
# 2) hexproof absorbs min(amt, hexproof) fully per instance
m2 = 'const to_sub = Math.min(amt, me.hexproof)' in gs
# 3) max_chases default
m3 = 'this.max_chases = 1;' in gs
print("injury=stackcount:", m1, "| hexproof blocks per-instance:", m2, "| max_chases=1:", m3)
print("CHECKLIST vs pid1(谭舒雁/命理师): board MUST include 辟邪阵纹 at LEAST +1 (4 hexproof).")
print("  lv1 (3 hex) -> injury caps ~7-9 -> LOSS.  lv2 (4 hex) -> caps ~5 -> WIN.")
print("  Reachability: merge 2x 辟邪阵纹(lv1). HOARD/ROLL for the 2nd copy from mid-game.")
