import os, sys
d = os.environ['YISIM_DIR']
path = os.path.join(d, 'gamestate_full.js')
a = int(sys.argv[1]); b = int(sys.argv[2])
with open(path, encoding='utf-8') as f:
    lines = f.readlines()
for i in range(a-1, min(b, len(lines))):
    print(i+1, lines[i], end='')
