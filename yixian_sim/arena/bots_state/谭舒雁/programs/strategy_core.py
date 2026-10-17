# Core strategic decision helper for 弈仙牌 (pid1 谭舒雁, star/reflect archetype).
#
# HARD-WON LESSONS encoded here:
#  1. BREAKTHROUGH COSTS 命. NEVER break a realm gate when 命 < ~18.
#     R13 game-lost by breaking 境4->境5 at 命=9 (dropped to -1).
#  2. Winning the lobby = winning MOST rounds. Losing streaks snowball: loser's
#     命 damage grows each round. Going 3-7 R4-R12 = death.
#  3. SEATING decidable by 修为 BEFORE battle. Absorb junk cards to push 修为 to
#     guarantee first seat. First seat often decides burst-vs-burst matches.
#  4. MUST_WIN logic: if expected loser damage >= my 命, the round is MUST-WIN ->
#     field max-sustain board, ignore economy.
#  5. Reflect/tank (反震心法) MIRRORS multi-hit (cloud-sword/fire). Weak to pure
#     HP-scalers. Burst beats burst only with first seat.
#
# Usage:
#   run_program("strategy_core.py", ["seat", my_ming, my_xiuwei, my_phys, next_gate_xiuwei, next_gate_phys])
#   run_program("strategy_core.py", ["break", my_ming])   # should I break through?
#   run_program("strategy_core.py", ["risk", my_ming, exp_loser_dmg])
import sys
a = sys.argv[1:]

def seat(my_ming, my_x, my_phys, gate_x, gate_phys):
    my_ming, my_x, my_phys, gate_x, gate_phys = map(int, (my_ming,my_x,my_phys,gate_x,gate_phys))
    print(f"my 命={my_ming} 修为={my_x} 体魄={my_phys}")
    can_x = my_x >= gate_x
    can_phys = my_phys >= gate_phys
    print(f"gate next realm: need 修为>={gate_x} (have {my_x}: {can_x}) OR 体魄>={gate_phys} (have {my_phys}: {can_phys})")
    if (can_x or can_phys) and my_ming < 18:
        print("*** DO NOT BREAK: 命 too low (<18). Breaking costs ~10 命; wait for 命>=18. ***")
    elif can_x or can_phys:
        print("Breakthrough available AND 命>=18 -> safe to break if realm HP/fate helps.")

def should_break(my_ming):
    my_ming = int(my_ming)
    print(f"命={my_ming}")
    if my_ming < 18:
        print("NO — breaking costs ~10 命, would risk death. Farm economy/board instead.")
    else:
        print("YES if a gate is open (修为/体魄 threshold met).")
    print("Rule: maxHP from realm is great but the 命 cost can end your run.")

def risk(my_ming, exp_dmg):
    my_ming, exp_dmg = int(my_ming), int(exp_dmg)
    print(f"命={my_ming}, expected loser damage this round ~{exp_dmg}")
    print("MUST_WIN =", exp_dmg >= my_ming)
    if exp_dmg >= my_ming:
        print("-> field MAX-SUSTAIN board, dump all exchanges to upgrade, absorb to win seat.")
    else:
        print("-> can take economy risks if EV favors; still prefer winning (streaks snowball).")

if not a:
    print(__doc__)
elif a[0] == "seat": seat(*a[1:6])
elif a[0] == "break": should_break(*a[1:2])
elif a[0] == "risk": risk(*a[1:3])
else: print(__doc__)
