import os, json
d = os.environ['YISIM_DIR']
fp = os.path.join(d, 'localization', '1.5.9', 'Localization.json')
with open(fp, encoding='utf-8') as f:
    data = json.load(f)
terms = data['mSource']['mTerms']
for idx in [2610, 2675, 5705, 9664, 9665, 9703]:
    print(idx, json.dumps(terms[idx], ensure_ascii=False)[:600])
    print("===")
# also broad search for "磨砺" desc
for i, t in enumerate(terms):
    s = json.dumps(t, ensure_ascii=False)
    if "磨砺" in s and "共鸣" not in s:
        print("M", i, s[:500])
