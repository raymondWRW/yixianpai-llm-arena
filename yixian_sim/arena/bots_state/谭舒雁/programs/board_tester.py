# Helper for the NEXT game: plan the FINAL/important board to WIN BOTH SEATS.
# The simulate() tool uses live stats for me and last-known for opp, and takes
# my_cards in cyclic order. This program can't call simulate() directly, so it
# instead PRINTS the concrete candidate orderings + a checklist to paste into
# simulate() calls. It also computes seating + lethality from 修为/命 inputs.
#
# Usage:
#   run_program("board_tester.py", ["seat", my_ming, my_xiuwei, opp_ming, opp_xiuwei, loser_dmg])
#   run_program("board_tester.py", ["plan", cardA, cardB, cardC, ...])
import sys, itertools
a = sys.argv[1:]

def seat(my_ming, my_x, opp_ming, opp_x, dmg):
    my_ming, opp_ming, dmg = int(my_ming), int(opp_ming), int(dmg)
    if my_x > opp_x: s = "I act FIRST"
    elif my_x < opp_x: s = "I act SECOND"
    else: s = "TIE -> coinflip (tie-break by 修为)"
    print(s)
    print(f"if I LOSE I pay {dmg} (my \u547d={my_ming}) -> {'DEAD' if dmg>=my_ming else 'ok'}")
    print(f"if I WIN opp pays {dmg} (opp \u547d={opp_ming}) -> {'opp DEAD' if dmg>=opp_ming else 'opp lives'}")
    print("MUST_WIN =", dmg >= my_ming)

def plan(cards):
    print("Candidate cards:", cards)
    print("Let AI pick order, but TEST these structural rules:")
    print(" - Put 天元心法 (or the [star]-maker) in SLOT 1.")
    print(" - Keep a qi->DEF / guard / heal card in the board so going-SECOND survives.")
    print(" - Order: ramp/buff -> spender -> sustain -> scaling finisher.")
    print("Run simulate(my_cards=[...], opp_pid=X) for each of the 2 seat cases:")
    print("   i_go_first=True  (I win seat)  and  i_go_first=False (I lose seat).")
    print("Both must read 'I WIN'. If not, swap the defensive card in / upgrade it.")
    # emit a couple of low-effort permutations if <=6 cards to nudge the search
    if 0 < len(cards) <= 6:
        for i, p in enumerate(itertools.permutations(cards)):
            if i >= 12: break
            print("  try:", list(p))

if not a:
    print(__doc__)
elif a[0] == "seat":
    seat(*a[1:6])
elif a[0] == "plan":
    plan(a[1:])
else:
    print(__doc__)
