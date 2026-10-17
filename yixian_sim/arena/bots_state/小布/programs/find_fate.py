
import os, glob
YISIM = os.environ['YISIM_DIR']
# search js files for 'fate'
import re
for f in glob.glob(os.path.join(YISIM,'*.js')):
    txt = open(f, encoding='utf-8', errors='replace').read()
    if 'fate' in txt.lower():
        print("FILE:", os.path.basename(f))
        for i,l in enumerate(txt.split('\n')):
            if 'fate' in l.lower() and ('=' in l or 'if' in l or 'stack' in l.lower() or 'push' in l):
                print(f"  {i}: {l.strip()[:120]}")
