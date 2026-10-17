import os, json, sys
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
targets = ['五雷','斩草','星弈','海底','杯弓','厄劫','天星','血光','梅开','两仪','静气','星轨','天元','命运轮回','金蝉','气吞','六爻','万事如意','天谕','诸事不宜','天机','吉运']
for cid, v in data.items():
    n = v.get('name') or ''
    if any(t in n for t in targets):
        print(cid, n, '| qi_cost=', v.get('qi_cost'), 'hp_cost=', v.get('hp_cost'), '| actions=', json.dumps(v.get('actions'), ensure_ascii=False))
