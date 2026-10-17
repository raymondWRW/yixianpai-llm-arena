import os, json, sys
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
# print top-level structure
if isinstance(data, dict):
    print("KEYS:", list(data.keys())[:50])
    for k in list(data.keys())[:5]:
        print(k, type(data[k]), str(data[k])[:200])
elif isinstance(data, list):
    print("LIST len", len(data))
    print(json.dumps(data[0], ensure_ascii=False)[:500])
