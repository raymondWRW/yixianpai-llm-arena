"""
g22 DRAIN BOARD helper — the win condition for 吾行之 (五行 + 阵法师5).
Assembles the 万花/回响 drain board and reports per-opponent orderings.

BASE THEORY (yisim-verified g22, 5 reps each, rivals' BASE fielded boards):
  ['万花迷魂阵','回响阵纹','水灵·泉涌','不动金刚阵+1','水灵·波澜','水灵·汹涌','辟邪阵纹','水灵·纳百川']
    vs 小布 (崩拳 burst):  100% first / 100% second  (base AND +1 board)
    vs 牧逸风 (万法):      100% first / 0% second    (SEAT decides)
    vs 谭舒雁 (内伤):      100% first / 0% second
  WHY: 万花 end-turn drain 1HP/减攻-stack (bypasses 防, heals me); 回响 retriggers slot-1 万花 = double drain;
       不动金刚阵 +7防/turn-end + 7maxHP if no chase = anti-burst; 辟邪 blanks 内伤/debuff stacks.
  LEGALITY: 万花 + 不动金刚阵 = 2 [持续] (cap). 回响 goes slot2 (retrigger slot1).

Usage: python g22_drain_board.py <opp_pid 0|1|3>
Just prints the recommended ordering; do the sim_matchup yourself with live cards.
"""
import sys

BASE = ["万花迷魂阵", "回响阵纹", "水灵·泉涌", "不动金刚阵+1",
        "水灵·波澜", "水灵·汹涌", "辟邪阵纹", "水灵·纳百川"]

# per-opponent re-orderings (keep the SAME 8 cards; move 辟邪/不动 position only)
ORDERS = {
    3: ["万花迷魂阵", "回响阵纹", "水灵·泉涌", "不动金刚阵+1",
        "水灵·波澜", "水灵·汹涌", "辟邪阵纹", "水灵·纳百川"],   # 小布: robust both seats
    0: ["辟邪阵纹", "不动金刚阵+1", "万花迷魂阵", "回响阵纹",
        "水灵·泉涌", "水灵·波澜", "水灵·汹涌", "水灵·纳百川"],   # 牧逸风: early 辟邪+不动 vs qi burst, WIN SEAT
    1: ["万花迷魂阵", "回响阵纹", "辟邪阵纹", "不动金刚阵+1",
        "水灵·泉涌", "水灵·波澜", "水灵·汹涌", "水灵·纳百川"],   # 谭舒雁: 辟邪 slot3 vs 内伤 clock
}

NAMES = {0: "牧逸风 万法 battery", 1: "谭舒雁 内伤 clock", 3: "小布 崩拳 burst"}

def main():
    pid = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    board = ORDERS.get(pid, BASE)
    print(f"opp pid{pid} ({NAMES.get(pid,'?')}):")
    print("  ", board)
    print("  field ONLY after sim_matchup shows >0% for the seat you'll have.")
    print("  vs 牧逸风/谭舒雁: MUST win 修为 seat (go first) or the board loses.")

if __name__ == "__main__":
    main()
