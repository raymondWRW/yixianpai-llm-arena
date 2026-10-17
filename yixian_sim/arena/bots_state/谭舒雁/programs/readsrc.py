import os, sys
d = os.environ.get('YISIM_DIR', '.')
name = sys.argv[1]
a = int(sys.argv[2]); b = int(sys.argv[3])
p = os.path.join(d, name)
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
for i in range(a-1, min(b, len(lines))):
    print(i+1, lines[i].rstrip())
