import os, json, sys
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
# My character is he1 (谭舒雁). Dump he1 cards + the qi/star/plant theme cards.
for cid, c in sorted(data.items()):
    ch = c.get('character')
    nm = c.get('name','')
    if ch in ('he1','he2','he3','he4','he5','he6'):
        print(cid, ch, nm, 'qi=',c.get('qi_cost'),'hp=',c.get('hp_cost'),'|',json.dumps(c.get('actions'),ensure_ascii=False)[:160])
