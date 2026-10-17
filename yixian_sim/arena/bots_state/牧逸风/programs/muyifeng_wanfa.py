
# 牧逸风 decision helper (g13). Encodes the 万法归灵剑 nuke board + matchup heuristics.
# Usage: run_program('muyifeng_wanfa.py', ['advice', 'vs_pid1'])

WANFA_BOARD = ["聚灵心法+1", "辟邪阵纹+1", "天罡聚力阵", "飞灵闪影剑+1",
               "白鹭灵剑", "化灵诀", "巨鲲灵剑", "万法归灵剑+1"]
# Fallback if no 万法 yet: generic ramp board that WINS FIRST ONLY (trap if rival out-修为's you).
GENERIC_BOARD = ["聚灵心法+1", "天罡聚力阵", "飞灵闪影剑+1", "巨鹏灵剑+1",
                 "白鹭灵剑", "巨鲸灵剑+1", "巨鲲灵剑", "形意剑+1"]

# 境5 pool = 9 card-types x6 = 54 copies; 万法 is 6 of them -> ~11% per card drawn at 境5.
# Expected draws to see >=1 万法 with 20 rolls ~ 1-(1-.11)^20 ~ 90%. Bank ~20 exchanges before R12.

ADVICE = {
  "vs_pid1": "谭舒雁 内伤 clock kills ~t7-8. MUST kill by t7. Use WANFA_BOARD (100%/100%). "
             "辟邪阵纹 blocks her 厄劫缠身 downgrade + injury seeding. Field 万法 LAST.",
  "vs_pid3": "小布 崩拳 force-burst. WANFA_BOARD 100%/100% incl +1. Out-damage fast. "
             "Don't field lv1 mishmash (the R15 loss).",
  "vs_pid2": "吾行之 water/wood. WANFA/GENERIC both 100%. Easy.",
  "draft":   "R2 sidejob=5(阵法师). Cultivate to 境5 by R12. Bank ~20 exchanges, then HUNT 万法归灵剑.",
}

def main(args):
    cmd = args[0] if args else "advice"
    if cmd == "advice":
        key = args[1] if len(args) > 1 else "draft"
        print(ADVICE.get(key, ADVICE["draft"]))
        print("WANFA:", WANFA_BOARD)
    elif cmd == "wanfa":
        print(WANFA_BOARD)
    elif cmd == "generic":
        print(GENERIC_BOARD)
    else:
        print(ADVICE)

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
