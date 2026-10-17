import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
# find specific card ids by name
for nm in ['气疗术','枯木逢春','Qi Therapy','Withered Wood Meets Spring','Traces Revitalized','Only Traces']:
    for cid, c in data.items():
        if (c.get('name') or '') == nm:
            print(cid, nm)
