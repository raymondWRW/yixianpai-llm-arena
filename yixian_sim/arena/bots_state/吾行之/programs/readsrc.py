import os, sys
d = os.environ['YISIM_DIR']
path = os.path.join(d, 'gamestate_full.js')
with open(path) as f:
    lines = f.readlines()
for i in range(4260, 4295):
    print(i+1, lines[i].rstrip())
