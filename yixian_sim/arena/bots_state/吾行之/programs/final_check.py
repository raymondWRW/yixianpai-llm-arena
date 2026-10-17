"""Quick reminder helper: given a water board, reminders for the standard check.
Run: python final_check.py   -> prints the canonical 'best water board' and the
key rule set so it's always in front of me while playing.
"""
BEST = ["水灵阵","水灵·波澜","水灵·纳百川","水灵·泉涌","水灵·腾浪","水灵·涛+1","水灵·涛+1","水灵·汹涌+1"]
print("CANONICAL BEST WATER BOARD (g16-verified 100/100 vs 牧逸风 & 小布 base):")
print("  ", " -> ".join(BEST))
print()
print("ORDER RULE: 水灵阵 first (持续, battery). 波澜 next (free 2 水势, 0 qi). "
      "纳百川 early (tank + 水势->HP). 泉涌/腾浪 (qi+水势). 涛/汹涌 PAYOFF near the END.")
print("MISSING PIECE THAT COST g16: 水灵·纳百川 (境5 五行-sect, 6 copies). HUNT IT HARD R13-R16.")
print("NEVER ABSORB engine pieces. BANK<=24 (25 wastes grant). HUNT at 境5, don't bank.")
