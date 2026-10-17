import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
for cid, c in data.items():
    if c.get('character') == 'he1':
        print(cid, c.get('name'), json.dumps(c, ensure_ascii=False))
print("=== ALL character values ===")
chars = {}
for cid, c in data.items():
    ch = c.get('character')
    chars.setdefault(ch, 0)
    chars[ch]+=1
print(chars)
