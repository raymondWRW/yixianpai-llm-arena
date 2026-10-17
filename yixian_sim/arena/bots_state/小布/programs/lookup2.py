
import os, json
YISIM = os.environ['YISIM_DIR']
swogi = json.load(open(os.path.join(YISIM,'swogi.json'),encoding='utf-8'))
k = list(swogi.keys())[0]
print(k, json.dumps(swogi[k], ensure_ascii=False)[:600])
# print all names containing 'crash' or 'fist'
for cid,cd in swogi.items():
    nm = (cd.get('name') or '')
    if 'crash' in nm.lower() or 'fist' in nm.lower():
        print(cid, nm)
