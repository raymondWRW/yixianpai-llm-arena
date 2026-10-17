# Board-order + matchup analyzer helper.
# I could not call the live `simulate` tool from inside this program (sandbox),
# so this prints a prioritized test PLAN: which orderings and which seat to test
# against each opponent. Use it to drive external simulate() calls efficiently.
#
# USAGE: run_program("board_search.py", ["vs_pid=1", "cards=A,B,C,..."])
#   - prints seat combos (first/second) and orderings worth simulating.
#
# KEY RULES baked in (learned across games):
#  * 云舞诀 MUST come before 巨虎/巨鲲 (they cost qi; no qi => they only GAIN qi).
#  * 云剑 chain [连云] scales with CONSECUTIVE cloud swords, BUT:
#      - vs a reflect turtle (反震心法), MORE hits = MORE reflected dmg => keep hit count LOW.
#      - vs normal decks, chaining 凌波/汇灵/极意 is good.
#  * SEAT MATTERS: test BOTH i_go_first=True and False. Acting second can WIN where first loses.
#  * 体魄 adds HP (physique -> hp). Big-sword kills give +4 max_physique IN battle.

import sys, itertools

def cloud(c): return "云剑" in c
def heavy(c): return ("巨虎" in c) or ("巨鲲" in c) or ("灵剑" in c)

def plan(cards, opp):
    seq_cards = [c for c in cards if not heavy(c)]
    heavy_cards = [c for c in cards if heavy(c)]
    print(f"=== TARGET {opp} ===")
    print(f"  qi/dance/cloud (pre-heavy): {seq_cards}")
    print(f"  heavy finishers (must follow qi): {heavy_cards}")
    print("  SUGGESTED ORDERS TO SIM (test each with i_go_first=True AND False):")
    # A: keep 云舞诀 early, then chain clouds, then heavies
    a = [c for c in cards if "云舞诀" in c] + [c for c in cards if cloud(c)] + heavy_cards
    # B: clouds first (max chain into 凌波/汇灵), 云舞诀 just before heavies
    b = [c for c in cards if cloud(c)] + [c for c in cards if "云舞诀" in c] + heavy_cards
    print("   A( qi-first, then chain, then heavy ): ", a)
    print("   B( chain-first, qi before heavy      ): ", b)
    print("  CONTRAST RULE:")
    print("   - if opp has 反震/reflect  -> prefer FEWER heavy hits (drop 凌波/汇灵), big single hits.")
    print("   - else                     -> prefer FULL chain (A or B whichever sims better).")
    print("  REMEMBER: only trust the SIM result, not the theory.")

if __name__ == "__main__":
    args = dict(a.split("=",1) for a in sys.argv[1:] if "=" in a)
    opp = args.get("vs_pid","?")
    cards = args.get("cards","").split(",") if args.get("cards") else []
    if cards:
        plan(cards, opp)
    else:
        print(__doc__)
