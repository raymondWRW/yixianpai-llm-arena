#!/usr/bin/env python3
"""Phase-1.5 helper: given an engine board (list of card names), try moving each of a few
'flex' cards to a range of slots and report which orderings matter. Prints a checklist.
This is a PURE planner — it does not call the sim (the harness sim_matchup does that).
Usage: run_program('permute_engine.py', ['聚灵心法','百鸟灵剑诀','回响阵纹','灵气灌注','引气剑','化灵诀','白鹭灵剑','万法归灵剑+1'])
"""
import sys, itertools

def main():
    cards = sys.argv[1:]
    if not cards:
        print("pass the current board as args, in order")
        return
    print("CURRENT ORDER:", cards)
    print()
    print("RULES TO CHECK (from notebook, g25):")
    print(" 1) slot1 MUST be a [持续] qi-gen (聚灵心法) because 回响阵纹 retriggers SLOT 1.")
    print(" 2) 回响阵纹 anywhere AFTER slot1.")
    print(" 3) all qi-banks (灵气灌注/引气剑/化灵诀/百鸟) EARLY (slots 2-6).")
    print(" 4) 万法归灵剑 LAST (slot 7-8) — it dumps ALL qi.")
    print(" 5) legality: <=2 [持续]/[消耗] total.")
    print()
    print("PERMUTATIONS TO A/B WITH sim_matchup (both seats, 3+ reps each):")
    key = cards[0] if cards else ""
    # suggest moving each non-first, non-last card one step earlier and later
    for i, c in enumerate(cards):
        if i == 0 or i == len(cards) - 1:
            continue
        print(f"  - move '{c}' (slot {i+1}) to slot 4; and to slot 6")
    print()
    print("VERDICT RULE: if a permutation flips 0%->100%, THAT is your board. Do not trust the first sim.")

if __name__ == "__main__":
    main()
