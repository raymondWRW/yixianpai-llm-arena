import os, json, sys
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
pat = sys.argv[1] if len(sys.argv)>1 else 'star_power'
for cid, c in data.items():
    s = json.dumps(c, ensure_ascii=False)
    if pat in s:
        print(cid, c.get('name'), '|', json.dumps(c.get('actions'), ensure_ascii=False))
