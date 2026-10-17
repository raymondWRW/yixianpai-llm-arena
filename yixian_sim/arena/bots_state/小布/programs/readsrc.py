import os, sys
D = os.environ['YISIM_DIR']
path = os.path.join(D, 'gamestate_full.js')
with open(path, encoding='utf-8') as f:
    lines = f.readlines()
a = int(sys.argv[1]); b = int(sys.argv[2])
for i in range(a-1, min(b, len(lines))):
    print(i+1, lines[i], end='')
