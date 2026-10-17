"""cn2en.py — map Chinese card names -> engine names, show levels."""
import os, json, sys
YISIM = os.environ['YISIM_DIR']

def load():
    data = json.load(open(os.path.join(YISIM,'names.json'),encoding='utf-8'))
    return data

if __name__=="__main__":
    data = load()
    want = ["聚灵阵","邪蛊阵","踏破九霄","势如破竹","朝气蓬勃","崩拳·缠","夜鬼啸","势大力沉",
            "崩拳·封","荷重前行","天罡聚力阵","灵玄迷踪步","崩天步",
            "斗转星移","飞星刺","落花有意","血光之灾","星弈·点","星弈·打","金鸡独立","揽雀尾"]
    # group by namecn base (strip +N)
    for w in want:
        hits=[d for d in data if d.get('namecn','').startswith(w)]
        print("==",w)
        for h in hits[:6]:
            print("   ", h['namecn'], "=>", h['name'], "| id", h['id'], "other", h['other_id'])
