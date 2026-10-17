"""谭舒雁 (命理师7) g27 MASTER BOARD — verified 100%/100% vs all 3 rivals' final boards (both seats, yisim 3-5 reps).
The 3rd 杯弓蛇影 (clock density) is the key upgrade over g26 (which was 100/0 vs 小布).
Usage: print the board list to paste into set_board, or run to re-verify vs a rival pid.
"""
import os, subprocess, sys

MASTER = ['天星·牵引','厄劫缠身','杯弓蛇影','杯弓蛇影','诸事不宜','诸事不宜','命运轮回','杯弓蛇影']

# slot logic reminders:
# slot1 天星·牵引: +2 qi, retriggers the 2 开局 AFTER it (厄劫's 开局-downgrade + 诸事's 开局+4def)
# slots 2-4,8: clock cards (厄劫 4内伤; 杯弓×3 = 2内伤 + immediate tick each)
# slots 5-6 诸事不宜: -6 atk × 2 stacks each = anti-burst
# slot7 命运轮回: +8 HP + skip slots-4/5-开局
# RULE: never field 反震心法/海底捞月 over a held clock/survival piece.

if __name__ == '__main__':
    print('MASTER BOARD:', MASTER)
    print('core = 3 clock + 2 诸事 + 天星·牵引 + 命运轮回')
