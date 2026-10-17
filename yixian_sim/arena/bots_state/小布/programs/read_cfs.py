import os
d = os.environ['YISIM_DIR']
fn = os.path.join(d, 'gamestate_full.js')
lines = open(fn, encoding='utf-8').read().split('\n')
# print lines 2090-2160 and 2440-2460
for i in list(range(2090, 2160)) + list(range(2445, 2460)):
    if i < len(lines):
        print(i+1, lines[i])
