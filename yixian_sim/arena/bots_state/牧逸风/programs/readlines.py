import os, sys
d = os.environ['YISIM_DIR']
fn = sys.argv[1]
a = int(sys.argv[2]); b = int(sys.argv[3])
p = os.path.join(d, fn)
with open(p, encoding='utf-8') as f:
    lines = f.readlines()
for i in range(a-1, min(b, len(lines))):
    print(i+1, lines[i].rstrip())
