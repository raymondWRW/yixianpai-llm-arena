import os, sys
d = os.environ['YISIM_DIR']
fname = sys.argv[1]
a = int(sys.argv[2]); b = int(sys.argv[3])
with open(os.path.join(d, fname)) as f:
    lines = f.readlines()
for i in range(a-1, min(b, len(lines))):
    print(i+1, lines[i], end='')
