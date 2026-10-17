import os, json
d = os.environ['YISIM_DIR']
base = os.path.join(d, 'localization', '1.5.9')
for fn in ['talent_params.json', 'talent_analysis.json', 'talent_resonance_params.json']:
    fp = os.path.join(base, fn)
    with open(fp, encoding='utf-8') as f:
        data = json.load(f)
    s = json.dumps(data, ensure_ascii=False)
    for t in ['Talent_12', 'Talent_118', 'Talent_151']:
        idx = s.find(t)
        if idx >= 0:
            print(fn, t, "found at", idx)
            print(s[idx-50:idx+400])
            print("---")
