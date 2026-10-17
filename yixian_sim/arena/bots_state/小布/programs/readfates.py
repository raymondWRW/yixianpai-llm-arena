import os
d = os.environ['YISIM_DIR']
p = os.path.join(d, 'gamestate_full.js')
with open(p, encoding='utf-8') as f:
    lines = f.readlines()
# print lines 440-575 (general immortal fates region)
for i in range(440, 575):
    print(i+1, lines[i].rstrip())
