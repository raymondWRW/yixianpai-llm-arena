"""
Endgame 命-budget + odd-out risk tracker for 弈仙牌.

Usage:
  python endgame_risk.py round my_destiny opp1_destiny [opp2_destiny] ...

Tells you:
 - expected 命 loss for a narrow/moderate/blowout loss this round
 - how many losses your 命 can absorb
 - the deficit-to-leader and how many net wins you need to finish them
 - STRONG WARNING if you are in a 3-player round (odd-out fights an EXTRA
   battle -> you can lose 命 TWICE this round; budget accordingly).
"""
import sys, math


def loss(round_, hp_delta):
    hp_delta = max(0, hp_delta)
    if hp_delta <= 20:
        dmg = round_ + 1 + math.ceil(hp_delta / 5)
    else:
        extra = min(math.ceil((hp_delta - 20) / 10), 2 + round_ // 2)
        dmg = round_ + 5 + extra
    if round_ <= 9:
        dmg -= 1
    return dmg


def main(args):
    if len(args) < 2:
        print(__doc__)
        return
    r = int(args[0])
    mine = int(args[1])
    opps = [int(x) for x in args[2:]]
    narrow = loss(r, 0)
    moderate = loss(r, 10)
    print(f"Round {r} | my 命={mine} | opps 命={opps}  (alive: {1 + len(opps)})")
    print(f"  loss costs: narrow={narrow}  moderate={moderate}  blowout={loss(r,40)}")
    print(f"  => I can absorb {mine // narrow} narrow loss(es) before DEAD.")
    if len(opps) == 2:
        print("  *** 3-PLAYER ROUND: odd player fights an EXTRA battle. ***")
        print(f"      If I'm odd-out, worst case I lose TWICE ({2*narrow}) "
              f"-> my 命 {mine} -> {mine - 2*narrow} "
              f"({'DEAD' if mine - 2*narrow <= 0 else 'alive'}).")
    # net wins to finish the toughest opponent
    if opps:
        leader = max(opps)
        win_dmg = loss(r, 0)  # your win deals ~this much to the loser
        need = math.ceil(leader / win_dmg)
        print(f"  Leader 命={leader}; each convincing WIN deals ~{win_dmg}.")
        print(f"  => Need ~{need} net wins (undefeated-ish) to end them.")
        print(f"  Deficit to leader: {leader - mine} 命. You must NOT trade losses.")
    print("  RULE: win convincingly; avoid being odd-out when board isn't a clear win.")


if __name__ == "__main__":
    main(sys.argv[1:])
