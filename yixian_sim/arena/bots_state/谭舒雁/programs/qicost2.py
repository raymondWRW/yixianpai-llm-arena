import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
for cid, v in sorted(data.items()):
    n = v.get('name') or ''
    qc = v.get('qi_cost')
    if qc is not None:
        print(cid, n, '| qi_cost=', qc)
