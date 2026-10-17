import os, sys
d = os.environ['YISIM_DIR']
fname = sys.argv[1]
start = int(sys.argv[2]); end = int(sys.argv[3])
with open(os.path.join(d, fname)) as f:
    lines = f.readlines()
for i in range(start-1, min(end, len(lines))):
    print(i+1, lines[i], end='')
