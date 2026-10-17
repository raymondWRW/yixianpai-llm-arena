# Helper: decide seating risk and whether a round is "must-win".
# Usage: run_program("seat_and_risk.py", [my_ming, my_xiuwei, opp_ming, opp_xiuwei, loser_dmg])
# loset_dmg = expected 命 paid by the LOSER this round (from the destiny formula).
# Prints whether I act first and whether losing is lethal.
import sys
a = sys.argv[1:]
my_ming, my_x, opp_ming, opp_x, dmg = map(int, a[:5])

i_first = (my_x > opp_x)  # tie => coin flip
print(f"act_first={i_first} (tie=coinflip)" if my_x != opp_x else "act_first=coinflip(tie)")

lose_cost = dmg  # loser pays dmg; if I lose I pay dmg
print(f"if I LOSE I pay {lose_cost}, my 命={my_ming} -> {'DEAD' if lose_cost>=my_ming else 'SURVIVE'}")
print(f"if I WIN opp pays {dmg}, opp 命={opp_ming} -> {'opp DEAD' if dmg>=opp_ming else 'opp survives'}")

must_win = lose_cost >= my_ming
print(f"MUST_WIN={must_win}  -> {'maximize win prob, ignore economy' if must_win else 'can gamble / take economy if EV favors'}")
# Reminder logic: when must_win, prefer higher sustain boards (guard_up + reflect +
# heal-on-qi) because burst decks are out-raced not out-bursted. Pad 修为 with free
# absorbs BEFORE battle so seating favors me.
