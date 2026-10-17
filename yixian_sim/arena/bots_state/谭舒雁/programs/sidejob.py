import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
# print unique keys used across cards
keys = set()
for cid, c in data.items():
    keys.update(c.keys())
print("ALL KEYS:", sorted(keys))
# sidejob related fields
for cid, c in data.items():
    for k in c.keys():
        if 'job' in k.lower() or 'career' in k.lower() or 'side' in k.lower() or 'sect' in k.lower():
            print(cid, k, c[k])
