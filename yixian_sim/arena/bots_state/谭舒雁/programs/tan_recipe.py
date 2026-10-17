#!/usr/bin/env python3
# 谭舒雁 (命理师) recipe reference. Prints the canonical boards + keep-list + fates.
RECIPE = ["天星·牵引","血光之灾","天星·御心","诸事不宜","落花有意","梅开二度","杯弓蛇影+2","流水无情"]
# swap 血光之灾 -> 厄劫缠身 equivalent-power variant if 诸事不宜 missing
ALT = ["天星·牵引","厄劫缠身","血光之灾","天星·御心","诸事不宜","落花有意","杯弓蛇影+2","流水无情"]
KEEP = ["杯弓蛇影","血光之灾","流水无情","落花有意","天星·牵引","天星·御心","诸事不宜","梅开二度","厄劫缠身","白鹤亮翅"]
FATES = "境2: 勤学苦练>飞鸿踏雪 | 境3: 斩断俗尘>雪羽清风 | 境4: 妙手回春>观星 | 境5: 斩断俗尘>观星 (combat fates first if offered)"
def main():
    print("RECIPE (100%/100% both seats vs 小布 pid3 exact board):")
    print("  " + ", ".join(RECIPE))
    print("ALT (厄劫 variant):")
    print("  " + ", ".join(ALT))
    print("KEEP (never roll/absorb): " + ", ".join(KEEP))
    print("FATES: " + FATES)
if __name__ == "__main__":
    main()
