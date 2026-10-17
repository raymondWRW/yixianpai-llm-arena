import os, sys
d = os.environ.get('YISIM_DIR', '.')
path = os.path.join(d, sys.argv[1])
a, b = int(sys.argv[2]), int(sys.argv[3])
with open(path, encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
for i in range(a-1, min(b, len(lines))):
    print(i+1, lines[i], end='')
