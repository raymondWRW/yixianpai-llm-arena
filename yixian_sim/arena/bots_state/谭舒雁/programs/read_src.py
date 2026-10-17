
import os, sys
d = os.environ.get('YISIM_DIR', '.')
for fn in ['gamestate_full.js']:
    p = os.path.join(d, fn)
    if not os.path.exists(p):
        print('missing', p); continue
    lines = open(p, encoding='utf-8', errors='replace').read().splitlines()
    name = sys.argv[1] if len(sys.argv) > 1 else 'hexproof'
    for i, l in enumerate(lines):
        if name in l:
            lo = max(0, i-4); hi = min(len(lines), i+5)
            print(f'--- {fn}:{i+1} ---')
            for j in range(lo, hi):
                print(f'{j+1}: {lines[j]}')
