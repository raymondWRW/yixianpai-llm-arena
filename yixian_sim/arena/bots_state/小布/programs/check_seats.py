"""Helper: given my candidate board list and opp pid, this is just a reminder doc.
Real use is the sim_matchup tool, which already does both seats + opp base/+1.
Usage reminder (paste into reasoning, not a live API):
  1. sim_matchup(my_cards=[...], opp_pid=N, repeats=12)
  2. If result is 100%first / 0%second -> SEAT-LOCKED.
     FIRST try reorders: slide the double-force card (崩拳·寸劲) to slot1,
     chase-opener (崩拳·闪击) to slot2. Re-run sim_matchup.
  3. Only if reorders fail, do upgrades (merge a big attacker to +1).
  4. If still locked, ABSORB ALL junk -> win 修为 -> win seat.
"""
TARGET = ["崩拳·寸劲","崩拳·闪击","威震四方+1","崩灭心法","崩拳·连崩+1","崩拳·惊触","崩拳·降龙","崩拳·突+1"]
if __name__ == "__main__":
    print("MASTER (g30, both seats vs whole lobby):", TARGET)
    print("Reorder rule: 寸劲 slot1, 闪击 slot2. Test order before buying upgrades.")
