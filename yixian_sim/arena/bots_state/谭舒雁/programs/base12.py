import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
for cid, c in sorted(data.items()):
    if cid.startswith('12') and len(cid)==6 and cid.endswith('1'):
        acts=json.dumps(c.get('actions',[]),ensure_ascii=False)
        print(cid, c.get('name'), '|', acts[:110])
