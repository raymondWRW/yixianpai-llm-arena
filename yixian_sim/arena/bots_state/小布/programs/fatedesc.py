import os, json
d = os.environ['YISIM_DIR']
fp = os.path.join(d, 'localization', '1.5.9', 'Localization.json')
with open(fp, encoding='utf-8') as f:
    data = json.load(f)
def walk(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            walk(v, path + "/" + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, path + f"[{i}]")
    else:
        s = str(o)
        for t in ["磨砺不止", "顿悟", "稳固根基"]:
            if t in s:
                print(path, "=>", s[:300])
                print("---")
walk(data)
