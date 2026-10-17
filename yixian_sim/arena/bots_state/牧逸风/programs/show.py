import os, sys
d = os.environ['YISIM_DIR']
fn = sys.argv[1]
a = int(sys.argv[2]); b = int(sys.argv[3])
lines = open(os.path.join(d, fn), errors='ignore').read().split('\n')
for i in range(a-1, min(b, len(lines))):
    print(i+1, lines[i])
