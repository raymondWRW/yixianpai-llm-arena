import os
d = os.environ['YISIM_DIR']
p = os.path.join(d, 'gamestate_full.js')
lines = open(p, encoding='utf-8').read().split('\n')
for i in range(2794, 2890):
    print(i+1, lines[i])
