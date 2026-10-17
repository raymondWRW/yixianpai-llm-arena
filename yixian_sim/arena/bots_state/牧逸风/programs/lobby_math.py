# Lobby survival/aggression math for YiXianPai.
# Purpose: decide HOW AGRESSIVELY to play each round based on my 命 vs the field,
# and whether I can afford to "lose cheaply" for economy or MUST win.
#
# USAGE: run_program("lobby_math.py", ["my=44", "p1=0,p2=81,p3=63", "round=13"])
#   my   = my current 命
#   pX   = each opponent's current 命 (dead ones = 0)
#   round= current round number
#
# OUTPUT: how many losses each opponent can absorb, how many I can absorb,
#         and what destiny a typical win/loss deals at this round.
import sys, math

def dmg(rnd, hp_delta):
    # exact formula from gamestate_full.js (destiny damage a WINNER deals)
    if hp_delta <= 20:
        d = rnd + 1 + math.ceil(hp_delta / 5)
    else:
        extra = min(math.ceil((hp_delta - 20) / 10), 2 + rnd // 2)
        d = rnd + 5 + extra
    if rnd <= 9:
        d -= 1
    return d

def losses_affordable(hp, rnd, kind="close"):
    # how many more losses of this round's typical damage before death
    d = dmg(rnd, {"narrow":5,"close":15,"big":25,"blowout":50}[kind])
    return math.ceil(hp / d) if hp > 0 else 0

if __name__ == "__main__":
    a = dict(x.split("=", 1) for x in sys.argv[1:] if "=" in x)
    me = int(a.get("my", "30"))
    rnd = int(a.get("round", "10"))
    opps = [(s.split("=")[0], int(s.split("=")[1]))
            for s in a.get("p", "p2=30,p3=30").split(",")] if "p" in a else [
                (x.split("=")[0], int(x.split("=")[1]))
                for x in sys.argv[1:] if x.startswith("p") and "=" in x]
    print(f"ROUND {rnd} — typical damage: narrow {dmg(rnd,5)}, close {dmg(rnd,15)}, "
          f"big {dmg(rnd,25)}, blowout {dmg(rnd,50)}")
    print(f"   I have {me} 命 -> can absorb "
          f"{losses_affordable(me,rnd,'close')} close losses, "
          f"{losses_affordable(me,rnd,'blowout')} blowout losses.")
    print()
    for name, hp in opps:
        if hp <= 0:
            print(f"   {name}: DEAD")
            continue
        print(f"   {name}: {hp} 命 -> needs "
              f"{losses_affordable(hp,rnd,'close')} close losses to die "
              f"({losses_affordable(hp,rnd,'blowout')} blowouts).")
    print()
    print("DECISION:")
    print("  * If MY absorbable-losses <= 1 -> I MUST WIN THIS ROUND; play for board, not economy.")
    print("  * If I have slack AND opp is close to death -> trade hp for econ only if safe.")
    print("  * LATE GAME (r>=13): every loss is -14..-23. NEVER coast; one loss can be fatal.")
    print("  * AVOID being paired with the lobby's unbeatable scaling tank while I'm <2 losses from death.")
