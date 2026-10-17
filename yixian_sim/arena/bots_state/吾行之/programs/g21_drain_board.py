# g21_drain_board.py — the 万花/回响/辟邪 drain-sustain board (g21 verified, yisim).
# Beats 小布 100%/100% (base AND +1). Beats 谭舒雁 base 100%/100% with early 辟邪 + 汹涌+2.
# vs 牧逸风's 万法 battery: WINS 100% IF YOU GO FIRST, LOSES 0% if he goes first.
# >>> CONCLUSION: vs a 万法/qi battery, SEAT(修为) IS THE MATCHUP. Win 修为 or lose.

BASE = ["万花迷魂阵", "回响阵纹", "水灵·泉涌+1", "不动金刚阵+2",
        "水灵·波澜+1", "水灵·汹涌+1", "辟邪阵纹", "水灵·纳百川"]

# per-opponent re-order (matchups are ANNOUNCED — tune the ORDER to the foe):
# vs 小布 (崩拳 burst):  不动金刚阵+2 EARLY (survive burst) -> slot3.  (verified 100%/100%)
VS_XIAOBU = ["万花迷魂阵", "回响阵纹", "不动金刚阵+2", "水灵·泉涌+1",
             "水灵·波澜+1", "水灵·汹涌+1", "辟邪阵纹", "水灵·纳百川"]
# vs 谭舒雁 (内伤 clock): 辟邪 EARLY (slot3, blanks her 内伤) AND 汹涌+2 (speed). (verified 100%/100% base)
VS_TAN =    ["万花迷魂阵", "回响阵纹", "辟邪阵纹", "水灵·泉涌+1",
             "水灵·纳百川", "不动金刚阵+2", "水灵·汹涌+2", "水灵·波澜+1"]
# vs 牧逸风 (万法 battery): 不动金刚阵+2 early; you MUST win the seat. (100% first / 0% second)
VS_MU = BASE

NOTES = """
WHY IT WORKS (yisim, g21):
 - 万花迷魂阵[持续] = end-of-turn: +1 减攻 to foe, then drain (steal) 1 HP per 减攻 stack. 回响 at slot2
   RETRIGGERS slot-1 万花 -> a SECOND drain/turn. Drain bypasses 防/气势. 减攻 also blunts force-scaled burst.
 - 不动金刚阵+2 = +7 防 EVERY turn-end (3 turns) + 7 maxHP/heal if no chase. THE anti-burst survival slot.
 - 辟邪阵纹 = 3 [辟邪]: subtracts from incoming DEBUFF stacks (blanks 内伤). NOT vs attack dmg. Its +10 防
   clause fires only AFTER a 持续 card was played -> put it AFTER 万花/回响.
 - 水灵·纳百川 = the sustain/converter (+HP/+maxHP scaling with 水势). 水灵·汹涌 = the payoff (atk + 水势).
LEGALITY: 万花 + 不动金刚阵 = exactly 2 [持续] (at cap). Do NOT add a 3rd 持续.
NEVER ABSORB: 万花迷魂阵, 回响阵纹, 不动金刚阵, 辟邪阵纹, 八门金锁阵 (all core 阵法师 kit), 水灵·汹涌,
   水灵·纳百川, 水灵·泉涌, 水灵·波澜, 水灵·涛.
REACHABILITY: 万花 ×6, 回响 ×6, 不动金刚阵 ×8, 辟邪 ×8 in the 阵法师(5) pool — all common.
"""
if __name__ == "__main__":
    for name, b in [("BASE/VS_MU", BASE), ("VS_XIAOBU", VS_XIAOBU), ("VS_TAN", VS_TAN)]:
        print(name, b)
    print(NOTES)
