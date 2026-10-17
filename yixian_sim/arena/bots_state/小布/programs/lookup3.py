
import os, json
YISIM = os.environ['YISIM_DIR']
swogi = json.load(open(os.path.join(YISIM,'swogi.json'),encoding='utf-8'))
want = ['Detect-Horse','Majestic Qi','Sky-Piercing','Windward','Strong Force','Detect Qi','Flower Sentient','Astral','Shifting Stars','Falling Thunder','Qi Therapy','Exercise','Forge','Physique','Bone']
for cid,cd in swogi.items():
    nm = (cd.get('name') or '')
    for w in want:
        if w.lower() in nm.lower():
            print(cid, '|', nm, '|', json.dumps(cd.get('actions'),ensure_ascii=False)[:100])
            break
