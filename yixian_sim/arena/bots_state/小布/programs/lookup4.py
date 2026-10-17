
import os, json
YISIM = os.environ['YISIM_DIR']
swogi = json.load(open(os.path.join(YISIM,'swogi.json'),encoding='utf-8'))
want = ['Forge','Train','Bone','Luck','Fortune','Auspicious','Detect','Flower','Fleche','Shifting','Thunder','Therapy','Belly','Sea','Open']
for cid,cd in swogi.items():
    nm = (cd.get('name') or '')
    for w in want:
        if w.lower() in nm.lower():
            print(cid, '|', nm, '|', json.dumps(cd.get('actions'),ensure_ascii=False)[:110])
            break
