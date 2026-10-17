import os, glob, sys
d = os.environ.get('YISIM_DIR','.')
print("YISIM_DIR=", d)
# find files
for f in ['card_actions.js','gamestate_full.js']:
    p = os.path.join(d, f)
    if os.path.exists(p):
        with open(p, encoding='utf-8', errors='replace') as fh:
            lines = fh.readlines()
        print(f"=== {f} ({len(lines)} lines) ===")
        a, b = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv)>2 else (10040, 10075)
        for i in range(a, min(b, len(lines))):
            print(i+1, lines[i].rstrip())
