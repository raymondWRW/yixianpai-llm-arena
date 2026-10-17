"""
Destiny-damage + risk calculator for 弈仙牌.

Learned from gamestate_full.js calculate_destiny_damage (line 1619):
  hp_delta = winner.hp - loser.hp
  if hp_delta <= 20:  damage = round + 1 + ceil(hp_delta/5)
  else:               extra = min(ceil((hp_delta-20)/10), 2 + floor(round/2))
                      damage = round + 5 + extra
  if round <= 9: damage -= 1
Tiebreak (line 1575): if both survive 64 turns, the player with MORE remaining HP
wins the battle. So DEF / HP-gain / sustain decide long grinds.

USAGE:
  python damage_and_risk.py round
      -> prints base loss for a small vs a large hp_delta at that round.
  python damage_and_risk.py round my_destiny opponent_destiny
      -> how much margin you can absorb; flags fatal losses.
"""
import sys, math

def loss(round_, hp_delta, flame=False, kindness=0, cat_soul=False, dragon_scale=False):
    hp_delta = max(0, hp_delta)
    if hp_delta <= 20:
        dmg = round_ + 1 + math.ceil(hp_delta / 5)
    else:
        extra = math.ceil((hp_delta - 20) / 10)
        extra = min(extra, 2 + round_ // 2)
        dmg = round_ + 5 + extra
    if round_ <= 9:
        dmg -= 1
    if flame:
        dmg += 4
    if kindness:
        dmg = max(1, dmg - kindness)
    if cat_soul and dmg % 2 == 0:
        dmg //= 2
    if dragon_scale and dmg > 20:
        dmg = 20
    return dmg

def main(args):
    if not args:
        print(__doc__); return
    r = int(args[0])
    print(f"Round {r} destiny loss:")
    print(f"  narrow loss (hp_delta=0..5):   {loss(r,0)} .. {loss(r,5)}")
    print(f"  moderate   (hp_delta=10):      {loss(r,10)}")
    print(f"  blowout    (hp_delta=40):      {loss(r,40)}")
    print(f"  blowout    (hp_delta=80):      {loss(r,80)}")
    print("  => margin barely changes damage. WINNING the round is everything.")
    if len(args) >= 3:
        mine = int(args[1]); opp = int(args[2])
        for d in (loss(r,0), loss(r,10), loss(r,40)):
            survive = mine - d
            print(f"  if I lose by ~{d}: I go {mine}->{survive} "
                  f"({'DEAD' if survive<=0 else 'alive'})")
        print(f"  opp at {opp}: a narrow loss drops them to "
              f"{opp-loss(r,0)} ({'DEAD' if opp-loss(r,0)<=0 else 'alive'})")

if __name__ == "__main__":
    main(sys.argv[1:])
