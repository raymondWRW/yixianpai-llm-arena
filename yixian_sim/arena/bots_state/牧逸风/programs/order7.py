
# Test order permutations of my 7-card board vs pid3 full +1 board.
# Uses yisim via the harness 'simulate' is not callable here; so just print orders for manual sim.
import itertools, sys
cards = ["灵气灌注+1","剑劈+1","引气剑","飞牙剑","云剑·探云+1","巨虎灵剑+2","地煞剑"]
# We just enumerate a handful of sensible orders (keep 灵气灌注 near front).
orders = [
 ["灵气灌注+1","剑劈+1","引气剑","飞牙剑","云剑·探云+1","巨虎灵剑+2","地煞剑"],
 ["灵气灌注+1","剑劈+1","引气剑","飞牙剑","地煞剑","云剑·探云+1","巨虎灵剑+2"],
 ["灵气灌注+1","剑劈+1","飞牙剑","引气剑","地煞剑","云剑·探云+1","巨虎灵剑+2"],
 ["灵气灌注+1","引气剑","剑劈+1","飞牙剑","地煞剑","云剑·探云+1","巨虎灵剑+2"],
 ["灵气灌注+1","剑劈+1","引气剑","云剑·探云+1","飞牙剑","巨虎灵剑+2","地煞剑"],
 ["灵气灌注+1","剑劈+1","引气剑","地煞剑","飞牙剑","云剑·探云+1","巨虎灵剑+2"],
 ["灵气灌注+1","剑劈+1","引气剑","飞牙剑","地煞剑","巨虎灵剑+2","云剑·探云+1"],
]
for o in orders:
    print(",".join(o))
