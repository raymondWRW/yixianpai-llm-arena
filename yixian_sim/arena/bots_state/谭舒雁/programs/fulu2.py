import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
# group by 2-digit prefix
groups = {}
for cid, c in data.items():
    if cid.startswith('D'): continue
    pre = cid[:2]
    groups.setdefault(pre, []).append((cid, c))
for pre in ['32','12','11','13','14']:
    print("=== prefix", pre, "===")
    for cid, c in sorted(groups.get(pre,[])):
        print(' ', cid, c.get('name'), '| qi=',c.get('qi_cost'),'hp=',c.get('hp_cost'),'|',json.dumps(c.get('actions'),ensure_ascii=False)[:120])
