# 命(destiny) damage calculator — exact formula from gamestate_full.js:1619
# damage = round + 1 + ceil(hp_delta/5)              if hp_delta <= 20
#         = round + 5 + min(ceil((hp_delta-20)/10), 2+floor(round/2))  if hp_delta > 20
#         minus 1 if round <= 9
# KEY: WINNING BIG multiplies damage. A narrow win (hp_delta ~0) deals ~round+1.
#      A blowout (hp_delta>20) deals ~round+5+bonus, up to +2+round/2 more.
# Use: how many rounds do I need to kill someone, and how many do they need?
import math
def dmg(rnd, hp_delta, flame=False, kindness=0, dragon_scale=False):
    if hp_delta <= 20:
        d = rnd + 1 + math.ceil(hp_delta/5)
    else:
        extra = math.ceil((hp_delta-20)/10)
        extra = min(extra, 2 + rnd//2)
        d = rnd + 5 + extra
    if rnd <= 9: d -= 1
    if flame: d += 4
    if kindness: d = max(1, d - kindness)
    if dragon_scale and d > 20: d = 20
    return d

if __name__ == "__main__":
    print("round  narrow(+5)  close(+15)  big(+25)  blowout(+50)")
    for r in [3,5,8,10,14,18]:
        print(r,
              dmg(r,5), dmg(r,15), dmg(r,25), dmg(r,50))
    # survival math: 30 starting destiny
    print()
    print("Rounds-to-kill from 30 destiny at narrow vs blowout wins:")
    for r in [10,14,18]:
        print(f"  r{r}: narrow deals {dmg(r,5)} -> {math.ceil(30/dmg(r,5))} wins; "
              f"blowout deals {dmg(r,50)} -> {math.ceil(30/dmg(r,50))} wins")
