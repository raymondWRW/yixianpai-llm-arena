import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
for cid, c in sorted(data.items()):
    if cid.startswith('3'):
        print(cid, c.get('name'), '|qi',c.get('qi_cost'),'hp',c.get('hp_cost'),'|',json.dumps(c.get('actions',[]),ensure_ascii=False)[:150])
