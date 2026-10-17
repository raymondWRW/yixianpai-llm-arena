
# injury_board_check.py — rank a candidate 内伤-tank board's seat dependency note.
# Usage: run_program('injury_board_check.py', ['厄劫缠身','杯弓蛇影+1',...])
# Prints a checklist flag for each card's role. Pure text, no engine access needed.
import sys

ROLE = {
    "厄劫缠身": "CORE: +4 injury + opening downgrade foe same-slot",
    "血光之灾": "injury, opening +1 injury",
    "杯弓蛇影": "injury + force instant tick (burst)",
    "落花有意": "qi+1/def+1/1 injury (enables 流水无情 condition)",
    "流水无情": "6atk + 2 injury IF foe has debuff",
    "六爻绝阵": "continuous: +3 dmg per hexagram gained",
    "天机·逆施": "qi+2 + 50% of def/hp gain as dmg (CORE)",
    "天星·御心": "def4/hp4 + re-trigger opening before it x2",
    "天星·牵引": "qi+2 + trigger 2 openings AFTER it once each",
    "金蝉脱壳": "def/hp + guard; feeds 逆施",
    "诸事不宜": "def + reduce next 2 attacks by 6",
    "反震心法": "hp + counter 2 dmg per hit taken (anti-multi-hit)",
    "梅开二度": "double NEXT card -- put before 厄劫缠身/杯弓蛇影 NOT a qi-cost card",
    "命运轮回": "skip 4th/5th slot + trigger its opening",
}
QI_COST = {"五雷轰顶", "斩草除根", "星弈·夹", "星弈·立", "星弈·点", "星弈·虎",
           "落雷术", "海底捞月", "星弈·断", "海底捞月+1", "五雷轰顶+1", "斩草除根"}

def base(name):
    return name.split("+")[0]

def main(cards):
    print("Candidate board:", cards)
    has_qi_engine = any(base(c) in {"天机·逆施","探灵","天星·牵引","天星·御心","落花有意","气贯长虹"} for c in cards)
    for i, c in enumerate(cards):
        b = base(c)
        role = ROLE.get(b, "? (not in 内伤 role table)")
        flag = ""
        if b in QI_COST and not has_qi_engine:
            flag = " <<< WARNING: qi-cost card with NO qi engine -> will be SKIPPED"
        print(f"  slot{i+1}: {c:14s} {role}{flag}")
    print("qi engine present:", has_qi_engine)
    inj = sum(1 for c in cards if base(c) in {"厄劫缠身","血光之灾","杯弓蛇影","落花有意","流水无情"})
    print(f"injury-card count: {inj} (aim >=4, ideally 5 with 2x 杯弓蛇影)")

if __name__ == "__main__":
    main(sys.argv[1:] if len(sys.argv) > 1 else [])
