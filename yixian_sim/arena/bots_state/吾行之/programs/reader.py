import os, sys
d = os.environ['YISIM_DIR']
path = sys.argv[1]
a = int(sys.argv[2]); b = int(sys.argv[3])
lines = open(os.path.join(d, path), encoding='utf-8').read().splitlines()
for i in range(a-1, min(b, len(lines))):
    print(i+1, lines[i])
