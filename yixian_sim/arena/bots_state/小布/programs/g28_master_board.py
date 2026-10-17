"""
g28 master 崩拳 board + quick seat-race check.

Usage:
  python g28_master_board.py            -> print the target board + keep-list
  python g28_master_board.py verify     -> notes what to sim next game

The MASTER BOARD (yisim-verified g28 review, 7 reps, 100%/100% BOTH seats
vs ALL THREE rivals' final boards AND their +1):
  ['崩拳·闪击+1','气若悬河+1','崩拳·连崩','威震四方+1','踏破九霄','崩拳·戳','崩拳·弹+1','崩拳·惊触+1']
Key: 4 ATTACKERS (连崩/戳/弹/惊触) + 闪击; 惊触 LAST so its 追加 fires on the
next-cycle chase 崩拳. 崩拳·连崩 is the 4th attacker that flips the t6 seat race
(kill t6a first / t6b second, before 牧逸风's t7a 万法).
"""
import sys

MASTER = ["崩拳·闪击+1", "气若悬河+1", "崩拳·连崩", "威震四方+1",
          "踏破九霄", "崩拳·戳", "崩拳·弹+1", "崩拳·惊触+1"]

KEEP = ["崩拳·闪击", "崩拳·连崩", "威震四方", "崩拳·寸劲", "崩拳·惊触",
        "崩拳·戳", "崩拳·弹", "气若悬河", "踏破九霄", "冲霄破浪"]

HUNT = ["崩拳·闪击", "崩拳·连崩", "威震四方", "崩拳·寸劲",
        "崩拳·惊触", "崩拳·戳", "崩拳·弹"]


def main(argv):
    if argv and argv[0] == "verify":
        print("NEXT GAME — field MASTER, then sim_matchup(op_pid) for the announced opp.")
        print("If it loses a seat, try swapping slot1-8 order; if it loses both, hunt 崩拳·寸劲 for a 5th attacker.")
        return
    print("TARGET BOARD (slot order matters, 惊触 LAST):")
    for i, c in enumerate(MASTER):
        print(f"  {i+1}. {c}")
    print("\nKEEP-LIST (NEVER roll/absorb):", ", ".join(KEEP))
    print("POST-境5 NAME-HUNT (<=6 rolls/round, STOP on hit):", ", ".join(HUNT))
    print("\nRULE: 4 attackers minimum. A pure battery (冲霄破浪) LOSES its slot to 崩拳·连崩.")


if __name__ == "__main__":
    main(sys.argv[1:])
