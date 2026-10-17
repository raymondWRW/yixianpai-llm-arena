import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
for cid, c in data.items():
    nm = c.get('name','')
    if any(k in nm for k in ['Fulu','Incantation','Talisman','Spirit','Herb','Plant','Grain','Vine','Sea','Moon','Drag']):
        print(cid, nm, '|', json.dumps(c.get('actions'), ensure_ascii=False), '| ch=', c.get('character'), 'qi=', c.get('qi_cost'), 'hp=', c.get('hp_cost'))
