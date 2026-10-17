import os
d = os.environ['YISIM_DIR']
src = open(os.path.join(d, 'gamestate_full.js')).read().split('\n')
for i in range(1618, 1695):
    print(i+1, src[i])
