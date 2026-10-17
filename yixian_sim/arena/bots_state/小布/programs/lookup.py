
import os, json
YISIM = os.environ['YISIM_DIR']
HERE = os.path.dirname(os.path.abspath(__file__))
swogi = json.load(open(os.path.join(YISIM,'swogi.json'),encoding='utf-8'))
# find cards whose namecn matches my list
targets = ["崩拳·封","探马掌","崩拳·突","崩拳·撼","崩拳·连崩","气若悬河","崩拳·寸劲","崩拳·降龙",
  "破空爪","迎风掌","锻神开海","势大力沉","锻骨","天运·趋吉","探灵","落花有意","飞星刺",
  "斗转星移","星弈·断","星弈·夹","落雷术","气疗术"]
out={}
for cid,cd in swogi.items():
    nc = cd.get('namecn') or cd.get('nameCN') or cd.get('name_cn') or ''
    nm = cd.get('name','')
    for t in targets:
        if nc == t or nc==t+'1' or nc.startswith(t):
            out.setdefault(t,[]).append((cid,nm,nc))
for t in targets:
    print(t, "->", out.get(t))
