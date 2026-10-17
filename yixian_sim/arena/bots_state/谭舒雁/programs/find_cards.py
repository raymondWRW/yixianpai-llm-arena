import os, json, sys
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
needles = ['Thousand Evil', 'Ice Incantation', 'Fire Cloud Fulu', 'Drag Moon', 'Astral Move', 'Weaken Fulu', 'Embracing Qi', 'Vigorous Force', 'Crash Fist', 'Guard Qi', 'Cloud Sword']
for cid, c in data.items():
    nm = c.get('name', '')
    if any(n.lower() in nm.lower() for n in needles):
        print(cid, nm, json.dumps(c, ensure_ascii=False))
