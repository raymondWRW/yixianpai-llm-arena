# water_win_board.py — record the g19-verified lobby-winning 水灵 board order.
# Usage: run_program("water_win_board.py")  → prints the board to field + rationale.
# (Not a search driver; the harness's search_board tool does the searching. This is a memory aid.)

WIN_BOARD = [
    "五行天髓诀+1",   # slot1: chase engine, starts t1
    "水灵·泉涌",       # slot2: dmg->水势 converter (early!)
    "水灵·腾浪+1",     # slot3: qi + HP + 水势
    "水灵·纳百川+2",   # slot4: TANK heal (+8/水势 HP)
    "水灵·波澜+2",     # slot5: 水势 builder, free
    "水灵·涛+2",       # slot6: atk + 1 水势
    "不动金刚阵",      # slot7: SURVIVAL (+7防 +7HP/turn-end x2)  <-- anti-burst, vs 小布
    "水灵·汹涌+1",     # slot8: PAYOFF (atk + 水势) = the kill
]

NOTES = """
g19 yisim-verified 3 reps each: 100%/100% BOTH seats vs 小布 matrix board AND +1,
vs 牧逸风 base AND +1, vs 谭舒雁 base AND +1. THE WHOLE LOBBY.
Key rules:
 - 不动金刚阵 (own 阵法师 pool, 境4) is the anti-burst card. DROP 水灵阵 to fit it (2 持续 max).
 - 泉涌 EARLY (slot2) not last; 汹涌 LAST (slot8) after 水势 peaks.
 - NEVER absorb 汹涌/涛/纳百川 (converters are the win-condition).
 - Merge priority: 纳百川 > 天髓诀 > 波澜 > 涛 > 汹涌 > 腾浪.
"""

if __name__ == "__main__":
    print("Field (cyclic order):")
    for i, c in enumerate(WIN_BOARD, 1):
        print(f"  {i}. {c}")
    print(NOTES)
