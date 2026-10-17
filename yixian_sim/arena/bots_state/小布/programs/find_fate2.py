
import os, glob
YISIM = os.environ['YISIM_DIR']
keys = ['training','grind','body','physique','undying','vigor','vitality','fate','zh']
for f in glob.glob(os.path.join(YISIM,'*.js')):
    txt = open(f, encoding='utf-8', errors='replace').read()
    for i,l in enumerate(txt.split('\n')):
        low=l.lower()
        if ('磨砺' in l or '体修' in l or '锻体' in l or '生机不灭' in l or '修玄' in l):
            print(os.path.basename(f), i, l.strip()[:140])
