#!/usr/bin/env python3
"""Reminder helper: prints the proven core board + upgrade priorities.
Run: run_program('core_check.py', ['qi_plan'])
Not a simulator (sims need the MCP simulate tool); this encodes the lessons so
next-game-me can re-derive the plan without re-reading the whole review.
"""
import sys

CORE = ["天元心法+1", "探灵", "厄劫缠身", "血光之灾", "流水无情",
        "星弈·断+1", "星弈·断", "落雷术+1"]

def main():
    args = sys.argv[1:]
    if not args or args[0] == "board":
        print("CORE (cyclic):")
        for i, c in enumerate(CORE, 1):
            print(f"  {i}. {c}")
        print("RULES: 2nd 星弈·断 > 星弈·夹 (strict upgrade). Last slot 落雷术 ONLY if 探灵 is lv2.")
        return
    if args[0] == "qi":
        print("QI BUG: 探灵 lv1 = 3 qi ONE-TIME only. 断/落雷/流水/厄劫 each cost 1qi.")
        print("FIX: merge 探灵->lv2 (+3 qi). Or field 斗转星移(0qi) in last slot.")
        return
    if args[0] == "order":
        print("Merge priority: 探灵=>lv2 (qi!) > 断=>+2 > 流水=>+1 > 血光=>+1 > 厄劫=>+1 > 天元=>+2.")
        return
    print("usage: board | qi | order")

if __name__ == "__main__":
    main()
