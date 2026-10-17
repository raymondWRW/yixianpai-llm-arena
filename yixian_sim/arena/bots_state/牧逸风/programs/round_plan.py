# Round-planning helper for 牧逸风 云剑 burst.
# Prints, for each candidate board ordering: the turn-plan (qi -> stack 加攻/剑意 ->
# finisher) and the DESTINY damage a win would deal at this round. Reminds me to
# measure HP DELTA, not just win/loss, when simming.
#
# USAGE: run_program("round_plan.py", ["round=14", "cards=云舞诀,云剑·极意+1,..."])
import sys, math

def dmg(rnd, hp_delta):
    if hp_delta <= 20:
        d = rnd + 1 + math.ceil(hp_delta/5)
    else:
        extra = min(math.ceil((hp_delta-20)/10), 2 + rnd//2)
        d = rnd + 5 + extra
    if rnd <= 9: d -= 1
    return d

def classify(c):
    if "云舞诀" in c or "灵气" in c or "剑意" in c: return "OPEN(qi/intent)"
    if "月影" in c or "加攻" in c or "极意" in c: return "STACK(atk/intent)"
    if "巨虎" in c or "巨鲲" in c or "巨鹏" in c or "巨鲸" in c or "灵剑" in c:
        return "FINISHER(big)"
    if "云剑" in c: return "CHAIN"
    return "OTHER(def/util)"

if __name__ == "__main__":
    a = dict(x.split("=",1) for x in sys.argv[1:] if "=" in x)
    rnd = int(a.get("round","10"))
    cards = a.get("cards","").split(",") if a.get("cards") else []
    print(f"ROUND {rnd} — destiny damage table (win):")
    for hd in [0,5,10,15,20,25,40,60,100]:
        print(f"   hp_delta {hd:>4} -> deal {dmg(rnd,hd)}")
    print("  => AIM for a win with hp_delta >= 20 (blowout).")
    print()
    print("BOARD PLAN (cyclic order matters):")
    for i,c in enumerate(cards):
        print(f"   slot{i}: {c:<20} [{classify(c)}]")
    print()
    print("CHECKLIST:")
    print(" [ ] 云舞诀/qi BEFORE any 巨虎/巨鲲 (they need qi/剑意 to be big).")
    print(" [ ] Stack 加攻/剑意 EARLY, dump FINISHER last for max single-hit delta.")
    print(" [ ] vs reflect(反震): FEWER, BIGGER hits (chip reflects kill you).")
    print(" [ ] Sim each opp BOTH seats (i_go_first True AND False).")
    print(" [ ] Low 命? absorb hand/take weak card to WIN SEAT via higher 修为.")
