import os, sys
d = os.environ['YISIM_DIR']
p = os.path.join(d, 'gamestate_full.js')
with open(p, encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()
a = int(sys.argv[1]); b = int(sys.argv[2])
for i in range(a-1, min(b, len(lines))):
    print(f"{i+1}: {lines[i].rstrip()}")
