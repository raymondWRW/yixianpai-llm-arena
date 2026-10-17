"""谭舒雁 星/命理师 CORE recipe (R20 review 2025).
Verified vs 小布(pid3) FINAL board: 100% win both seats (~7-8t).
Key: 厄劫缠身 x2 (apply 4-5 [内伤] ON PLAY + [开局] 9 dmg if enemy slot lv1)
+ 杯弓蛇影 x2 (2 内伤 + immediate tick) = 内伤 clock lethal by t7-8,
BEFORE 小布's 磅礴之势 (force*3 inner burst) resolves at t8.
[内伤] ticks at START of victim's turn -> going FIRST = enemy dies before acting.
Load-bearing: 厄劫缠身 (x2, one upgraded to +1) + 杯弓蛇影 x2. Slots 6-8 = flex.
"""
# Verified-winning board (names as in hand/board):
CORE = ["厄劫缠身+1","厄劫缠身","血光之灾","杯弓蛇影","杯弓蛇影","流水无情","落花有意","星弈·断"]
# Flex alternative (if no 厄劫+1): upgrade either 厄劫 to +1 -> flips going-2nd to a win.
# 内伤 sources ranked by impact: 厄劫缠身(4/5) > 杯弓蛇影(2+tick) > 流水无情(2 if debuff) > 血光之灾(1+1开局) > 落花有意(1)
# Seat rule: 修为 must stay > enemy's or they act first and my 内伤 can't kill before their burst.
def report():
    return "CORE=", CORE
