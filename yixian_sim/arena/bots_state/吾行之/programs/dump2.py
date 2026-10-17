import os, sys
fn = sys.argv[1]
args = sys.argv[2:]
p = os.path.join(os.environ['YISIM_DIR'], fn)
with open(p, encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
for a in args:
    if '-' in a:
        lo, hi = a.split('-'); lo=int(lo); hi=int(hi)
    else:
        lo=int(a); hi=lo+10
    for i in range(lo-1, min(hi, len(lines))):
        print(i+1, lines[i].rstrip())
    print('-----')
