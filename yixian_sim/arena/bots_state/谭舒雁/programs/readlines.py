import os, sys
d = os.environ['YISIM_DIR']
f = os.path.join(d, 'card_actions.js')
lo = int(sys.argv[1]); hi = int(sys.argv[2])
with open(f, encoding='utf-8') as fh:
    for i, line in enumerate(fh, 1):
        if lo <= i <= hi:
            print(i, line.rstrip())
