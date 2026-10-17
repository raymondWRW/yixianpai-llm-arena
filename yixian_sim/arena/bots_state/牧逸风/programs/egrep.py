import os, sys
d = os.environ.get('YISIM_DIR','.')
pat = sys.argv[1]
for f in os.listdir(d):
    if not f.endswith('.js'): continue
    p = os.path.join(d, f)
    try:
        with open(p, encoding='utf-8', errors='replace') as fh:
            for i, line in enumerate(fh):
                if pat in line:
                    print(f"{f}:{i+1}: {line.rstrip()[:200]}")
    except Exception as e:
        print("ERR", f, e)
