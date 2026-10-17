import os, json, glob
YISIM = os.environ['YISIM_DIR']
# find resonance_talents / talent files inside YISIM only
cands = []
for pat in ['**/resonance_talents.json','**/talent*.json','**/*mirage*.json','**/Localization.json']:
    cands += glob.glob(os.path.join(YISIM, pat), recursive=True)
for f in cands:
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception as e:
        continue
    # look for fate/talent name entries
    def walk(o, path=''):
        if isinstance(o, dict):
            for k,v in o.items():
                if isinstance(v, str) and any(x in v for x in ['崩拳','传承','磨砺','顿悟','再生','筋骨','副职','锻体']):
                    print(os.path.basename(f), path+'/'+str(k), '=', v)
                walk(v, path+'/'+str(k))
        elif isinstance(o, list):
            for i,v in enumerate(o):
                walk(v, path+f'[{i}]')
    walk(d)
