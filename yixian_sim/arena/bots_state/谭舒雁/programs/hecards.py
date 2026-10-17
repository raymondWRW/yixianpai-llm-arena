import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
for cid, c in data.items():
    ch = c.get('character')
    if ch and str(ch).startswith('he'):
        nm = c.get('name','')
        acts = json.dumps(c.get('actions',[]),ensure_ascii=False)
        print(cid, ch, nm, '| qi',c.get('qi_cost'),'hp',c.get('hp_cost'), '|', acts[:150])
