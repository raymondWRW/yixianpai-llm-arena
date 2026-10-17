
import os, sys
d = os.environ.get('YISIM_DIR', '.')
p = os.path.join(d, 'gamestate_full.js')
lines = open(p, encoding='utf-8', errors='replace').read().splitlines()
lo = int(sys.argv[1]); hi = int(sys.argv[2])
for j in range(lo-1, min(hi, len(lines))):
    print(f'{j+1}: {lines[j]}')
