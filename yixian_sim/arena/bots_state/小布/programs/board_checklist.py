"""小布 g24 checklist helper. Prints the standard 境5 board variants and the
per-opponent slot-4 rule. Call: run_program('board_checklist.py')
This does NOT call the game API (no access); it is a reference card."""
BOARD_BASE = ["气若悬河+1", "威震四方", "冲霄破浪", "SLOT4", "崩拳·闪击", "崩拳·惊触", "崩拳·寸劲", "崩拳·连崩"]

def board(slot4):
    return [slot4 if c == "SLOT4" else c for c in BOARD_BASE]

def main():
    print("境5 board variants (slot 4 is the only difference):")
    print("  vs 吾行之(水灵 tank) / big-HP sustain -> slot4 = 踏破九霄 (burst agi):")
    print("   ", board("踏破九霄"))
    print("  vs 牧逸风(云剑/万法) / 谭舒雁(命理) -> slot4 = 灵玄迷踪步 (sustained agi):")
    print("   ", board("灵玄迷踪步"))
    print()
    print("Rule: matchup is ANNOUNCED each round -> pick slot4 per opponent.")
    print("Always sim_matchup BOTH seats vs the opp EXACT last board before set_board.")
    print("Engine: 崩拳·闪击 keeps 身法>=10 every turn -> auto-chase (2 crash fists/turn).")
    print("Finisher: 崩拳·惊触 bonus (+20ish) then 寸劲 (2x force) then 连崩 on the chase.")

if __name__ == "__main__":
    main()
