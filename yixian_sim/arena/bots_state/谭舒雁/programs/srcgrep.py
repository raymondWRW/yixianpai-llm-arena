import os, sys, re
d = os.environ['YISIM_DIR']
pat = sys.argv[1] if len(sys.argv) > 1 else ''
files = ['gamestate_full.js', 'card_actions.js', 'card_info.js', 'swogi.js']
for fn in files:
    p = os.path.join(d, fn)
    if not os.path.exists(p):
        continue
    with open(p, encoding='utf-8', errors='ignore') as f:
        for i, line in enumerate(f, 1):
            if re.search(pat, line):
                print(f"{fn}:{i}: {line.rstrip()[:200]}")
