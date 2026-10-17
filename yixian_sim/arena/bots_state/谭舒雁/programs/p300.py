import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
names = {}
for cid, c in data.items():
    nm = c.get('name','')
    if nm in ('Qi Therapy','Revitalized','Wild Horses Part the Mane','Snake in Reflection','Golden Rooster Independence','Stillness Citta-Dharma','Dance Of The Dragonfly','Distubing Fulu','Fire Cloud Fulu'):
        print(cid, nm, '|', json.dumps(c.get('actions',[]),ensure_ascii=False)[:140])
