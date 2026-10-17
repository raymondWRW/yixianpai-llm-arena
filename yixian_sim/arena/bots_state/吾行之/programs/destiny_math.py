"""
Destiny (命) loss math + endgame risk. Verified against
gamestate_full.js:1619 calculate_destiny_damage.

Usage: python destiny_math.py <round> <my_hp(命)> <my_maxHP> <opp_maxHP> [win] [my_hp_left] [opp_hp_left]
  If win == "0", compute the damage I would TAKE on a loss.
  hp_delta = winner.hp - loser.hp (in-battle remaining HP of both).
"""
import sys, math

def loss_damage(round_no, hp_delta):
    # hp_delta = winner.hp - loser.hp
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
    win = (len(a) > 4 and a[4] != "0")
    if len(a) > 5:
        my_left = int(a[5])
    else:
        my_left = my_max if win else 0
    opp_left = int(a[6]) if len(a) > 6 else (opp_max if not win else 0)
    delta = abs(opp_left - my_left)
    d = loss_damage(rnd, delta)
    print(f"R{rnd}: margin(hp_delta)={delta}  => loss damage = {d}")
    if not win:
        print(f"  My 命 {my_hp} - {d} = {my_hp - d}  "
              f"{'DEAD' if my_hp - d <= 0 else 'survive'}")
    print("  NOTE: 命 never regenerates. Every loss is permanent. "
          "Aim to WIN early rounds to bank 命 surplus; late losses cost round+5.")

if __name__ == "__main__":
    main()
