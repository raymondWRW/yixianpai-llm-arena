# Improved planner for the NEXT game (star/reflect 谭舒雁 or similar).
# Encodes: seat decision, lethality/MUST_WIN check, breakthrough safety, and a
# board-order checklist that the agent pastes into simulate() in BOTH seats.
#
# Usage:
#   run_program("plan_next.py", ["seat", my_x, opp_x, my_ming, opp_ming, loser_dmg])
#   run_program("plan_next.py", ["break", my_ming, my_xiuwei, gate_xiuwei, my_phys, gate_phys])
#   run_program("plan_next.py", ["plan", cardA, cardB, ...])
import sys, itertools
a = sys.argv[1:]

def seat(my_x, opp_x, my_ming, opp_ming, dmg):
    my_x, opp_x, my_ming, opp_ming, dmg = map(int, (my_x, opp_x, my_ming, opp_ming, dmg))
    if my_x > opp_x:   s = "I act FIRST"
    elif my_x < opp_x: s = "I act SECOND"
    else:              s = "TIE -> coinflip"
    print(f"SEAT: {s}  (my 修为 {my_x} vs {opp_x})")
    print(f"lose -> I pay {dmg} (命={my_ming}) -> {'DEAD' if dmg>=my_ming else 'safe'}")
    print(f"win  -> opp pays {dmg} (命={opp_ming}) -> {'OPP DEAD - GAME OVER' if dmg>=opp_ming else 'opp lives'}")
    print("MUST_WIN =", dmg >= my_ming, "| KILL_SHOT =", dmg >= opp_ming)

def should_break(my_ming, my_x, gate_x, my_phys, gate_phys):
    my_ming, my_x, gate_x, my_phys, gate_phys = map(int, (my_ming,my_x,gate_x,my_phys,gate_phys))
    open_ = my_x >= gate_x or my_phys >= gate_phys
    print(f"命={my_ming} 修为={my_x}/{gate_x} 体魄={my_phys}/{gate_phys} -> gate {'OPEN' if open_ else 'closed'}")
    if open_ and my_ming < 18:
        print("*** DO NOT BREAK: 命<18, break costs ~10 命 and can kill you. ***")
    elif open_:
        print("SAFE to break (命>=18) if realm HP/fate helps.")
    else:
        print("No gate open: farm 修为 (absorb junk) / 体魄.")

def plan(cards):
    print("Candidate cards:", cards)
    print("ORDER RULES (star/reflect):")
    print(" 1) 天元心法 in SLOT 1 (makes all slots 星位). 众星拱月 early if fewer stars.")
    print(" 2) ramp/buff -> 星弈 spenders -> 聚气咒 (Qi->DEF sustain) -> finisher.")
    print(" 3) 火云符 to shred maxHP; 斩草除根 LAST (7x2 + shred).")
    print(" 4) If a former win-board loses: ADD/UPGRADE sustain (聚气咒) before adding dmg.")
    print("MANDATORY: simulate(my_cards=[...], opp_pid=X, i_go_first=True) AND (=False).")
    print("           Both must say 'I WIN'. If not, reorder / swap sustain.")
    if 0 < len(cards) <= 6:
        for i, p in enumerate(itertools.permutations(cards)):
            if i >= 10: break
            print("  try order:", list(p))

if not a:
    print(__doc__)
elif a[0] == "seat":  seat(*a[1:6])
elif a[0] == "break": should_break(*a[1:6])
elif a[0] == "plan":  plan(a[1:])
else: print(__doc__)
