# Mu Yifeng 内伤/剑阵 attrition board-order planner for EXTERNAL simulate() calls.
# Prints the seat combos + orderings to test against the announced opponent.
# USAGE: run_program("attrition_plan.py", ["vs=1", "cards=化灵诀+1,破气剑+1,...", "rnd=18"])
#
# Rules baked in (verified across games):
#  * 化灵诀 (灵气 opener) MUST be slot 1 (everything downstream may cost/gate on 灵气).
#  * 破气剑 (strip opp 灵气) belongs EARLY (~slot 3) vs qi-gated decks (star/cloud).
#    Only ONE copy of 破气剑 — two copies LOST both seats previously.
#  * 周天剑阵 ([持续]: +5 ATK after each attacking card) should be EARLY-ish, but it needs
#    a 持续 card alive; place it before the bulk of attackers.
#  * 辟邪阵纹 (DEF 10/14/18 if a 持续 already played) MUST come AFTER 邪蛊阵/周天剑阵.
#  * 邪蛊阵 ([持续] 内伤 chip) early so its ticks stack up over the fight.
#  * 巨鲸/巨虎/巨鲲 finishers (need 灵气) go LATE, after qi is built.
#  * vs reflect/HP-attrition decks: fewer bigger hits, more DEF + 内伤 sustain.
import sys, itertools, math

def dmg(rnd, hd):
    if hd <= 20:
        d = rnd + 1 + math.ceil(hd/5)
    else:
        d = rnd + 5 + min(math.ceil((hd-20)/10), 2 + rnd//2)
    if rnd <= 9: d -= 1
    return d

def classify(c):
    if "化灵诀" in c or "灵气" in c: return "OPEN(qi) -> slot1"
    if "破气剑" in c: return "ANTI-QI (slot ~3, ONE only)"
    if "邪蛊阵" in c: return "CONT(内伤 chip)"
    if "周天剑阵" in c: return "CONT(+5atk global) -> early"
    if "辟邪阵纹" in c: return "DEF(after a 持续!)"
    if "反身剑" in c: return "atk+DEF (after 周天)"
    if "碎杀阵" in c: return "finisher(+atk/碎防)"
    if ("巨鲸" in c or "巨虎" in c or "巨鲲" in c or "巨鹏" in c): return "FINISHER(big, needs qi) -> late"
    if "阵" in c: return "阵/util"
    return "other"

if __name__ == "__main__":
    a = dict(x.split("=",1) for x in sys.argv[1:] if "=" in x)
    rnd = int(a.get("rnd","10")); opp = a.get("vs","?"); cards = a.get("cards","").split(",") if a.get("cards") else []
    print(f"=== TARGET pid{opp}  round {rnd} ===")
    print("destiny dealt on a WIN (they lose):",
          {hd: dmg(rnd,hd) for hd in [0,10,20,40,80,140]})
    print("  -> aim for hp_delta>=20 when possible; at low 命 just WIN.")
    for i,c in enumerate(cards): print(f"  slot{i}: {c:<18} [{classify(c)}]")
    print()
    print("ORDERINGS TO SIM (test EACH with i_go_first True AND False):")
    qi   = [c for c in cards if "化灵诀" in c or "灵气" in c]
    poq  = [c for c in cards if "破气剑" in c][:1]
    cont = [c for c in cards if "邪蛊阵" in c or "周天剑阵" in c]
    rest = [c for c in cards if c not in qi+poq+cont]
    print("  A( qi, 破气剑, 持续..., rest ): ", qi+poq+cont+rest)
    print("  B( qi, 持续..., 破气剑, rest ): ", qi+cont+poq+rest)
    print("  C( qi, rest with 破气剑 at slot3, 持续 ): ", qi+ (rest[:2]+poq+rest[2:]) + cont)
    print()
    print("CHECKLIST:")
    print(" [ ] 化灵诀 slot1. 破气剑 early (ONE). 周天 before attackers. 辟邪阵纹 after a 持续.")
    print(" [ ] Sim vs their LAST board AND a fully +1-upgraded version (worst case).")
    print(" [ ] If you only win going FIRST and you're lower 修为 -> you probably LOSE; retune.")
    print(" [ ] Low 命 (<=10)? absorb hand junk for 修为 to perhaps WIN SEAT; else full board.")
