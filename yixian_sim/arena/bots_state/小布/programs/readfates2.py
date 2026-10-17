import os
d = os.environ['YISIM_DIR']
p = os.path.join(d, 'gamestate_full.js')
with open(p, encoding='utf-8') as f:
    lines = f.readlines()
for i in range(443, 490):
    print(i+1, lines[i].rstrip())
print("=== search for fate names across js files ===")
import glob
terms = ["磨砺", "顿悟", "稳固根基", "坚毅", "领悟"]
for fn in glob.glob(os.path.join(d, '*.js')):
    with open(fn, encoding='utf-8') as f:
        for ln, line in enumerate(f, 1):
            for t in terms:
                if t in line:
                    print(fn, ln, line.rstrip()[:200])
                    break
