import os, json, sys
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
target = sys.argv[1]
for cid, v in data.items():
    s = json.dumps(v, ensure_ascii=False)
    if target in s:
        print(cid, v.get('name'), v.get('actions'))
