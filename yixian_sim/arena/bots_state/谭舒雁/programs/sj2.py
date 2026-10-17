import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
for cid, c in sorted(data.items()):
    nm = c.get('name') or ''
    if any(k in nm for k in ['Qi Therapy','Withered Wood','Mystery Seed','Leaf Shield','Leaf Blade','Entangling','Devouring','Zongzi','Spring']):
        print(cid, nm, 'qi=',c.get('qi_cost'),'hp=',c.get('hp_cost'),'|',json.dumps(c.get('actions'),ensure_ascii=False))
