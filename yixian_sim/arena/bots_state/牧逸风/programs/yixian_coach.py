#!/usr/bin/env python3
"""
yixian_coach.py — Mu Yifeng (剑阵 Sect 1) decision helper.
Prints an EXACT test plan + legality checks so external simulate() calls are fast.

USAGE:
  run_program("yixian_coach.py", ["cards=A,B,C", "opp=3", "rnd=17", "oppcards=X,Y"])

VERIFIED MECHANICS (gamestate_full.js / card_actions.js):
  - 剑意(sword_intent) is ADDED to EVERY attack's damage (line 4493); only drops at
    end of turn by the MAX reached. Build 剑意 early, then chain multi-hit attacks.
  - ignore_def/smash DEF: 云剑·无妄 = ignore_def; 碎杀阵/势大力沉 = smash_def. These are
    the ONLY ways through 小布's 磅礴之势 DEF wall (+4 DEF per 气势 point).
  - 周天剑阵 [持续]: EVERY attacking card adds +5 ATK => put it EARLY, before attackers.
  - 百鸟灵剑诀 [持续]: 灵剑 qi cost -1(-2 at lv3) => fixes qi starvation.
  - 聚灵心法 [持续]: +1 qi/your-turn (lv2) => sustained qi for sword decks.
  - qi-gated cards with insufficient qi are SKIPPED -> order qi-gainers FIRST.
  - SEAT: higher 修为 acts first. Sim BOTH i_go_first True/False.
  - [持续]/[消耗] cap = 2 per board.
  - 命 dmg: rnd+1+ceil(hd/5) if hd<=20 else rnd+5+min(ceil((hd-20)/10),2+rnd//2); -1 rnd<=9.
"""
import sys, math

CONT_BASES = {"周天剑阵","邪蛊阵","碎杀阵","引雷阵","狂剑·零式","聚灵心法",
              "百鸟灵剑诀","天罡聚力阵","万花迷魂阵","龟甲阵","水月剑阵","不动金刚阵"}
QI_BASES   = {"云舞诀","凝意诀","化灵诀","灵气灌注","引气剑","聚灵心法"}

def base(c): return c.split("+")[0]
def is_cont(c): return base(c) in CONT_BASES
def is_qi(c):   return base(c) in QI_BASES

def role(c):
    b = base(c)
    tbl = {
      "周天剑阵":"CONT(+5atk global) -> EARLY",
      "百鸟灵剑诀":"CONT(qi-cost -1) -> EARLY",
      "聚灵心法":"CONT(+qi/turn) -> EARLY",
      "碎杀阵":"CONT(+3atk,SMASH DEF) -> EARLY",
      "引雷阵":"CONT(4 dmg/turn)",
      "云舞诀":"QI+剑意 opener -> slot1",
      "凝意诀":"QI+剑意 opener -> slot1",
      "化灵诀":"QI opener -> slot1",
      "引气剑":"QI (+multi atk if qi>2)",
      "灵气灌注":"QI + next-atk ignore-DEF",
      "云剑·无妄":"ignore-DEF enabler (vs DEF wall)",
      "云剑·极意":"剑意 builder",
      "剑意激荡":"剑意 x1.8 BUILDER (use after stacking)",
      "万法归灵剑":"FINISHER(exhausts ALL qi -> burst) -> LAST",
      "御空剑阵":"DEF+8 + chase (free if DEF>0)",
    }
    if b in tbl: return tbl[b]
    if b in ("邪蛊阵","万花迷魂阵"): return "CONT(chip - BAD vs 崩拳/HP-cost)"
    if any(x in b for x in ("巨鲸","巨鲲","巨鹏","巨虎","灵剑")): return "FINISHER(big, needs qi) -> LATE"
    if "剑" in b: return "attacker"
    return "util"

def dmg(rnd, hd):
    if hd <= 20: d = rnd + 1 + math.ceil(hd/5)
    else: d = rnd + 5 + min(math.ceil((hd-20)/10), 2 + rnd//2)
    if rnd <= 9: d -= 1
    return d

def main(args):
    a = dict(x.split("=",1) for x in args if "=" in x)
    cards = a.get("cards","").split(",") if a.get("cards") else []
    rnd = int(a.get("rnd","10")); opp = a.get("opp","?")
    oppcards = a.get("oppcards","").split(",") if a.get("oppcards") else []
    j = "".join(oppcards)

    print(f"=== vs pid{opp}  round {rnd} ===")
    print("DESTINY table (hp_delta -> damage they LOSE on my win):")
    print("  ", {hd: dmg(rnd,hd) for hd in [0,10,20,40,80,140]})

    nc = sum(1 for c in cards if is_cont(c))
    print(f"\nBOARD LEGALITY: {nc} [持续]/[消耗] cards -> {'ILLEGAL (>2)!' if nc>2 else 'OK'}")

    print("\nCARD ROLES:")
    for c in cards: print(f"  {c:<20} {role(c)}")

    qi   = [c for c in cards if is_qi(c)]
    cont = [c for c in cards if is_cont(c) and c not in qi]   # avoid dup
    rest = [c for c in cards if c not in qi and c not in cont]
    print("\nORDERINGS TO SIM (each with i_go_first True AND False):")
    print("  A qi+cont->attackers:", qi+cont+rest)
    print("  B qi->attackers->late finishers:", qi+rest+cont)
    print("  C anti-DEF: 云剑·无妄 / 碎杀 right before the big finisher")

    print("\nKEY RULES:")
    print(" * qi-gainers slot1. 周天剑阵/百鸟灵剑诀 EARLY (before attackers).")
    print(" * 剑意 builders BEFORE multi-hit; 剑意激荡 after stacking.")
    print(" * vs 小布(体修/崩拳 + 磅礴之势 DEF wall): DON'T chip. BURST + ignore/smash DEF.")
    print(" * vs 谭舒雁(符咒 梅开二度+星弈): re-triggers 20+ hits. Race or hard-wall.")
    print(" * 2-card [持续] cap: usually 周天剑阵 + 聚灵心法; vs DEF wall use 周天+碎杀.")
    if j:
        if any(x in j for x in ["磅礴之势","水月剑阵","龟甲","不动金刚"]):
            print("  -> OPP DEF WALL: bring 碎杀阵 / 云剑·无妄 / 灵气灌注 (ignore/smash DEF).")
        if any(x in j for x in ["崩拳","崩灭","势大力沉","磅礴"]):
            print("  -> OPP HP-COST/崩拳: do NOT chip; burst or hard wall.")
        if any(x in j for x in ["梅开二度","星弈","众星拱月"]):
            print("  -> OPP 符咒 scaling burst: race them, defend, or 辟邪(hexproof).")
        if any(x in j for x in ["金灵","火灵","五行","天谕"]):
            print("  -> OPP 命理/五行 scaling: dmg grows each turn; kill by ~turn 8.")

if __name__ == "__main__":
    main(sys.argv[1:])
