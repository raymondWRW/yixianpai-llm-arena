import os, sys
d = os.environ['YISIM_DIR']
fn = sys.argv[1] if len(sys.argv) > 1 else 'gamestate_full.js'
a = int(sys.argv[2]); b = int(sys.argv[3])
p = os.path.join(d, fn)
lines = open(p, errors='ignore').read().split('\n')
for i in range(a-1, min(b, len(lines))):
    print(i+1, lines[i])
