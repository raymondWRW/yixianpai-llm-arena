import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
# find cards with 'hp' or 'heal' or 'max_hp' actions, and note prefix families
for cid, c in sorted(data.items()):
    if cid.startswith('D'): continue
    acts = json.dumps(c.get('actions'), ensure_ascii=False)
    nm = c.get('name') or ''
    if ('max_hp' in acts or 'hp_gained' in acts) and 'reduce' not in acts:
        print(cid, nm, '|', acts[:150])
