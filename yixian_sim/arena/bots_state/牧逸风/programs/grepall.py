import os, sys, re
d = os.environ['YISIM_DIR']
pat = sys.argv[1]
for root, dirs, files in os.walk(d):
    for fn in files:
        if not fn.endswith('.js'): continue
        p = os.path.join(root, fn)
        try:
            with open(p) as f:
                for i, line in enumerate(f, 1):
                    if re.search(pat, line):
                        print(f"{fn}:{i}: {line.rstrip()}")
        except Exception as e:
            pass
