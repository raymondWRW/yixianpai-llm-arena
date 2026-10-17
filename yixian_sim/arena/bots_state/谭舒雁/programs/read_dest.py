import os
d = os.environ['YISIM_DIR']
p = os.path.join(d, 'gamestate_full.js')
lines = open(p, encoding='utf-8').read().split('\n')
for i in range(1618, 1690):
    print(i+1, lines[i])
