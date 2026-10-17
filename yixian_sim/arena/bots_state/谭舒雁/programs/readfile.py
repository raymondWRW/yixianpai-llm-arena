import os, sys
d = os.environ['YISIM_DIR']
fn = sys.argv[1]
p = os.path.join(d, fn)
with open(p, encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()
a = int(sys.argv[2]); b = int(sys.argv[3])
for i in range(a-1, min(b, len(lines))):
    print(f"{i+1}: {lines[i].rstrip()}")
