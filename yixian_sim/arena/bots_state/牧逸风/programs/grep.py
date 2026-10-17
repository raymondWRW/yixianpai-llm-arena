import os, sys, re
d = os.environ['YISIM_DIR']
pat = sys.argv[1] if len(sys.argv) > 1 else 'fate'
for fn in os.listdir(d):
    if not fn.endswith('.js'): continue
    try:
        src = open(os.path.join(d, fn), errors='ignore').read()
    except Exception:
        continue
    for i, line in enumerate(src.split('\n')):
        if re.search(pat, line):
            print(f"{fn}:{i+1}: {line.strip()[:160]}")
