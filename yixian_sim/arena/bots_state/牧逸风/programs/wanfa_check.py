# Helper: score candidate qi-burst boards vs the 3 rival archetypes.
# Can't call live sim from sandbox -> prints a sim PLAN driven by external sim_matchup().
# USAGE: run_program("wanfa_check.py", ["cards=A,B,C,..."])
import sys

QI_GEN = ["云舞诀", "聚灵阵", "引气剑", "化灵诀", "云剑·点星", "百鸟灵剑诀", "聚灵心法", "凝意诀"]
FINISHER = ["万法归灵剑"]

def plan(cards):
    qg = [c for c in cards if any(k in c for k in QI_GEN)]
    wf = [c for c in cards if any(k in c for k in FINISHER)]
    other = [c for c in cards if c not in qg and c not in wf]
    print("QI-GEN (must be FIRST, in this order):", qg)
    print("万法 FINISHERS (must be LAST):", wf, f"({len(wf)} copies; want 2-3)")
    print("OTHER:", other)
    if len(wf) < 2:
        print("!! <2 万法 -> likely NOT a winning late board; roll harder for 万法.")
    print("\nRECOMMENDED ORDER:", ", ".join(qg + other + wf))
    print("Then call sim_matchup(my_cards=<that order>, opp_pid=1/2/3) for ALL THREE,")
    print("both seats (it auto-tests seat+upgrade). Need 100% base on each to win the lobby.")
    print("KEY: qi bank target ~16-18 by t5-6; 万法 dmg = 5 + 5*qi.")

if __name__ == "__main__":
    args = dict(a.split("=",1) for a in sys.argv[1:] if "=" in a)
    cards = args.get("cards","").split(",") if args.get("cards") else []
    plan(cards) if cards else print(__doc__)
