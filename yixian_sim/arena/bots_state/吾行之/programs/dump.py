import os, sys
p = os.path.join(os.environ['YISIM_DIR'], 'gamestate_full.js')
args = sys.argv[1:]
with open(p) as f:
    lines = f.readlines()
for a in args:
    if '-' in a:
        lo, hi = a.split('-'); lo=int(lo); hi=int(hi)
    else:
        lo=int(a); hi=lo+15
    for i in range(lo-1, min(hi, len(lines))):
        print(i+1, lines[i].rstrip())
    print('-----')
