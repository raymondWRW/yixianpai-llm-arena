import os
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'gamestate_full.js')) as f:
    lines = f.readlines()
for i in range(4582, 4600):
    print(i+1, lines[i].rstrip())
