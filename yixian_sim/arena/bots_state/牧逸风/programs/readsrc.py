import os, sys
d = os.environ['YISIM_DIR']
path = os.environ.get('YISIM_DIR')
f = os.path.join(d, 'gamestate_full.js')
lines = open(f, encoding='utf-8').read().split('\n')
args = sys.argv[1:]
a = int(args[0]); b = int(args[1])
for i in range(a-1, min(b, len(lines))):
    print(i+1, lines[i])
