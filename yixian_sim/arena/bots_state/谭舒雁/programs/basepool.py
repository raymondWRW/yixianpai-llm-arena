import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
# print all cards with id < 100000 (base pool) and their character
for cid, c in sorted(data.items()):
    try:
        n = int(cid)
    except:
        n = -1
    if n>=0 and n < 100000:
        print(cid, c.get('character'), c.get('name'), '|qi',c.get('qi_cost'),'hp',c.get('hp_cost'))
