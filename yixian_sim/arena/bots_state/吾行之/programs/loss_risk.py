"""
Endgame loss-risk + 命-survival planner (verified vs gamestate_full.js calculate_destiny_damage).

Usage:
  python loss_risk.py <round> <my_命> <my_maxHP> <opp_maxHP> <my_hp_left_estimate> <opp_hp_left_estimate>

Prints what I'd lose on a loss AND how much 命 surplus I need to survive
the remaining rounds. Use it to DECIDE whether to gamble on a risky board
swap or play safe: if a loss would take me to <=0, do NOT gamble.

Rule of thumb: late rounds (>=13) each loss costs round+5..round+7, so by R15
a single catastrophic loss can be 20-24 命. You MUST bank early 命 surplus
(win rounds 3-10 while others still weak) to survive the late game.
"""
import sys, math

def loss_damage(round_no, hp_delta):
    if hp_delta <= 20:
        d = round_no + 1 + math.ceil(hp_delta / 5)
    else:
        extra = math.ceil((hp_delta - 20) / 10)
        extra = min(extra, 2 + math.floor(round_no / 2))
        d = round_no + 5 + extra
    if round_no <= 9:
        d -= 1
    return max(d, 1)

def main():
    a = sys.argv[1:]
    rnd = int(a[0]); my_hp = int(a[1]); my_max = int(a[2]); opp_max = int(a[3])
    my_left = int(a[4]) if len(a) > 4 else 0          # pessimistic: we lose at 0 HP
    opp_left = int(a[5]) if len(a) > 5 else opp_max
    delta = abs(opp_left - my_left)
    d = loss_damage(rnd, delta)
    print(f"R{rnd}: hp_delta={delta} -> catastrophic loss damage = {d}")
    print(f"  If I lose with {my_hp} 命: {my_hp} - {d} = {my_hp - d}"
          f"  {'*** DEAD ***' if my_hp - d <= 0 else 'survive'}")
    # margin needed
    print(f"  Need >= {d} 命 surplus to survive this single loss.")

if __name__ == "__main__":
    main()
