import os, json, sys
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
targets = sys.argv[1:] or ['Astral Move - Hit','Astral Move - Flank','Astral Move - Point','Astral Fleche','Astral Move - Fly','Astral Move - Block','Astral Move - Extend']
for cid, c in data.items():
    nm = c.get('name') or ''
    if any(t.lower() in nm.lower() for t in targets):
        print(cid, nm, '|', json.dumps(c.get('actions'), ensure_ascii=False), '| char=', c.get('character'), '| marking=', c.get('marking'))
