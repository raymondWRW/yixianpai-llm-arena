import os, json, sys, io
d = os.environ['YISIM_DIR']
names = json.load(io.open(os.path.join(d,'names.json'), encoding='utf-8'))
swogi = json.load(io.open(os.path.join(d,'swogi.json'), encoding='utf-8'))
pat = sys.argv[1] if len(sys.argv)>1 else "灵"
for e in names:
    if pat in e.get('namecn','') or pat in e.get('name',''):
        cid = str(e['id'])
        info = swogi.get(cid, {})
        print(e['namecn'], '|', cid, '|', json.dumps(info.get('actions',[]), ensure_ascii=False)[:160])
