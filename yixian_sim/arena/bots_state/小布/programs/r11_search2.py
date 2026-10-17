"""
r11_search2.py — faster. Fix a small pool, enumerate subsets of `slots`,
limited random orderings per subset, sim both seats vs opp base AND +1.
Usage args = [my_cn_csv, opp_cn_csv, slots, subset_samples, order_tries, topN]
"""
import os, sys, json, subprocess, itertools, random
from collections import Counter

YISIM = os.environ['YISIM_DIR']
HERE = os.path.dirname(os.path.abspath(__file__))
yf = YISIM.replace("\\", "/")

_NAMES = json.load(open(os.path.join(YISIM,'names.json'),encoding='utf-8'))
_CN2EN = {}
for d in _NAMES:
    cn, en = d.get('namecn',''), d.get('name','')
    if cn and en and cn not in _CN2EN:
        _CN2EN[cn] = en

def to_en(cn):
    lvl=1; base=cn
    if '+' in cn:
        base, num = cn.split('+',1)
        try: lvl=1+int(num)
        except: lvl=2
    en=_CN2EN.get(base)
    if en is None:
        for k,v in _CN2EN.items():
            if k.startswith(base) or base.startswith(k): en=v; break
    if en is None: en=base
    return en if lvl==1 else f"{en} {lvl}"

RUNNER = '''
import fs from 'fs';
import { GameState } from "%s/gamestate_full.js";
import { ready as cready } from "%s/card_name_to_id_fuzzy.js";
import parse_input from "%s/parse_input.js";
await cready;
const reqs = JSON.parse(fs.readFileSync(new URL('./_r11reqs.json', import.meta.url),'utf8'));
const out=[];
for (const req of reqs) {
  try {
    const j = parse_input(JSON.stringify(req));
    const results = [];
    for (const af of [true,false]) {
      const game = new GameState();
      const [p0,p1] = af ? [j.a,j.b] : [j.b,j.a];
      Object.assign(game.players[0], p0);
      Object.assign(game.players[1], p1);
      game.sim_n_turns(64);
      const log = game.output.join('\\n');
      let m = log.match(/player ([01]) \\([^)]*\\) wins/);
      let w=null;
      if(m) w = m[1]==='0' ? (af?'a':'b') : (af?'b':'a');
      results.push(w);
    }
    out.push({r:results});
  } catch(e){ out.push({r:null, err:''+e}); }
}
fs.writeFileSync(new URL('./_r11res.json', import.meta.url), JSON.stringify(out));
''' % (yf, yf, yf)

def run(reqs):
    open(os.path.join(HERE,"_r11reqs.json"),"w",encoding="utf-8").write(json.dumps(reqs,ensure_ascii=False))
    open(os.path.join(HERE,"_r11run.mjs"),"w",encoding="utf-8").write(RUNNER)
    r = subprocess.run(["bun",os.path.join(HERE,"_r11run.mjs")],capture_output=True,text=True,cwd=YISIM,timeout=120,shell=True,encoding='utf-8')
    if r.returncode!=0:
        print("RUNERR", (r.stderr or '')[-800:]); return None
    return json.load(open(os.path.join(HERE,"_r11res.json"),encoding="utf-8"))

def mateval(pool, opp_en, my_cult=42, my_hp=82, my_phys=24, my_maxphys=59):
    reqs=[]
    for p in pool:
        reqs.append({"a_first":True,"a":dict(cultivation=my_cult,hp=my_hp,physique=my_phys,max_physique=my_maxphys,cards=p),
                     "b":dict(cultivation=44,hp=80,physique=0,max_physique=51,cards=opp_en)})
    res=run(reqs)
    if res is None: return None
    out=[]
    for p,r in zip(pool,res):
        if r.get('r') is None: continue
        wa,wb=r['r']
        out.append((1 if wa=='a' else 0, 1 if wb=='a' else 0, p))
    return out

def main():
    a=sys.argv[1:]
    my_cn=a[0].split(',') if a and a[0] else []
    opp_cn=a[1].split(',') if len(a)>1 and a[1] else []
    slots=int(a[2]) if len(a)>2 else 8
    subset_samples=int(a[3]) if len(a)>3 else 200
    order_tries=int(a[4]) if len(a)>4 else 5
    topN=int(a[5]) if len(a)>5 else 15
    my=[to_en(c) for c in my_cn]; opp=[to_en(c) for c in opp_cn]
    print("pool_en:", my)

    def up(c):
        parts=c.rsplit(' ',1)
        if len(parts)==2 and parts[1].isdigit(): return f"{parts[0]} {int(parts[1])+1}"
        return c+" 2"
    opp1=[up(c) for c in opp]

    cnt=Counter(my); items=list(cnt.keys())
    msets=[]
    def rec(i,cur):
        if sum(cur.values())==slots: msets.append(dict(cur)); return
        if i>=len(items): return
        for k in range(0,cnt[items[i]]+1):
            if sum(cur.values())+k>slots: break
            cur[items[i]]=k; rec(i+1,cur); del cur[items[i]]
    rec(0,{})
    random.shuffle(msets)
    msets=msets[:subset_samples]

    pool=[]
    for m in msets:
        cards=[]
        for k,v in m.items(): cards+=[k]*v
        for _ in range(order_tries):
            random.shuffle(cards); pool.append(list(cards))
    print("candidates:", len(pool))

    r0=mateval(pool, opp)
    r1=mateval(pool, opp1)
    sc={}
    for (f,s,p) in r0:
        sc[tuple(p)]=[f,s,None,None]
    for (f,s,p) in r1:
        sc[tuple(p)][2]=f; sc[tuple(p)][3]=s
    rows=[]
    for p,(f,s,f1,s1) in sc.items():
        rows.append((f+s, f1+s1 if f1 is not None else -1, f, s, f1, s1, list(p)))
    rows.sort(key=lambda x:(-(x[1]), -(x[0])))
    print("==== TOP (sorted by win vs +1, then base) ====")
    for r_ in rows[:topN]:
        print(f"base[F{r_[2]} S{r_[3]}] +1[F{r_[4]} S{r_[5]}] :: {' | '.join(r_[6])}")

if __name__=="__main__":
    main()
