import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
kw = ['Ice Incantation','Fire Cloud','Weaken Fulu','Golden Rooster','Wild Horses','Revitalized','Stillness','Qi Therapy','Dance','Snake','Fulu','Incantation','Guard Qi']
for cid, c in sorted(data.items()):
    nm = c.get('name','')
    for k in kw:
        if k.lower() in nm.lower():
            print(cid, c.get('character'), nm, '|qi',c.get('qi_cost'),'hp',c.get('hp_cost'),'|',json.dumps(c.get('actions',[]),ensure_ascii=False)[:130])
            break
