import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
out=[]
for cid, c in sorted(data.items()):
    if cid.startswith('D'): continue
    nm = c.get('name') or ''
    if any(k in nm for k in ['Plant','Herb','Grain','Vine','Seed','Flower','Root','Leaf','Bud','Bloom','Cultivat','Garden','Forest','Wood','Ginseng','Spirit Plant']):
        out.append(f"{cid} {nm} qi={c.get('qi_cost')} {json.dumps(c.get('actions'),ensure_ascii=False)}")
print('\n'.join(out[:200]))
