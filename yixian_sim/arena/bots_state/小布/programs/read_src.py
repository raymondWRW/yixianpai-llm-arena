import os, sys
d = os.environ['YISIM_DIR']
fn = os.path.join(d, 'gamestate_full.js')
lines = open(fn, encoding='utf-8').read().split('\n')
lo, hi = 4200, 4300
for i in range(lo, min(hi, len(lines))):
    print(i+1, lines[i])
