import os, json, glob
YISIM = os.environ['YISIM_DIR']
f = glob.glob(os.path.join(YISIM,'**','resonance_talents.json'), recursive=True)
for fn in f:
    d = json.load(open(fn, encoding='utf-8'))
    print("=== file", os.path.relpath(fn,YISIM), "type", type(d))
    if isinstance(d, dict):
        for k,v in list(d.items())[:60]:
            print(k, "->", str(v)[:80])
    elif isinstance(d, list):
        for i,v in enumerate(d[:60]):
            print(i, "->", str(v)[:80])
    break
