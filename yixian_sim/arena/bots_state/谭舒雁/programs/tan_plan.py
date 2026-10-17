"""Tan Shuyan (star sect) quick reference — regenerated from 2024 review.
Helper for next game:
  - my key endgame board vs tanks (order-locked, verified via search_board with opp_cards):
      [坎卦, 乾卦, 星弈·断+1, 星轨推衍, 众星拱月+1, 众星拱月+1, 星弈·飞+1, 星弈·打+1]
  - KEY: 断 (skip) at 0-based slot 2 => default star point => skip fires.
    Default star points = 0-based idx 2 and 5 (from yisim source).
Usage convention: always call search_board(..., opp_cards=<enemy UPGRADED board>) because
base boards are already 100% vs my engine — the only informative test is the upgraded one.
"""
ENDER = ["坎卦", "乾卦", "星弈·断+1", "星轨推衍", "众星拱月+1", "众星拱月+1", "星弈·飞+1", "星弈·打+1"]
EARLY = ["离卦", "乾卦", "星轨推衍", "众星拱月", "星弈·夹", "星弈·飞", "坎卦", "星弈·打"]

def report():
    print("vs Tank(pid3): use ENDER, 断 at slot2. Win FIRST seat; 2nd seat coin-flip vs full-upgrade.")
    print("vs Burst(pid0): race, keep higher 修为 for first seat. vs 五行(pid2): ENDER wins both.")

if __name__ == "__main__":
    report()
    print("ENDER =", ENDER)
    print("EARLY =", EARLY)
