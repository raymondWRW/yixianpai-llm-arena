import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
names = {c.get('name','').lower(): cid for cid,c in data.items()}
for n in ['ice incantation','fire cloud fulu','weaken fulu','thousand evil incantation','drag moon in sea','astral move - tiger','sharp metal fulu','guard qi','only traces','traces revitalized']:
    for nm,cid in names.items():
        if nm==n or n in nm:
            c=data[cid]
            print(cid, c.get('name'), 'qi=',c.get('qi_cost'),'hp=',c.get('hp_cost'),'ch=',c.get('character'), c.get('marking'), json.dumps(c.get('actions'),ensure_ascii=False))
            break
