"""
r11_search.py — enumerate board compositions+orders from my card multiset vs
opponent's last board, using the real yisim engine.
Chinese names auto-translated via names.json; "+N" => level N+1 ("Name N").

Usage: args = [my_cn_csv, opp_cn_csv, slots, maxcombos, topN]
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
    """cn like '夜鬼啸' or '夜鬼啸+1'. returns engine name with level suffix."""
    lvl = 1
    base = cn
    if '+' in cn:
        base, num = cn.split('+',1)
        try: lvl = 1+int(num)
        except: lvl = 2
    en = _CN2EN.get(base)
    if en is None:
        # try fuzzy startswith
        for k,v in _CN2EN.items():
            if k.startswith(base) or base.startswith(k):
                en=v; break
    if en is None:
        en = base  # pass through (maybe already english)
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
    out.push({r:results, err:null});
  } catch(e){ out.push({r:null, err:''+e}); }
}
fs.writeFileSync(new URL('./_r11res.json', import.meta.url), JSON.stringify(out));
''' % (yf, yf, yf)

def run(reqs):
    open(os.path.join(HERE,"_r11reqs.json"),"w",encoding="utf-8").write(json.dumps(reqs,ensure_ascii=False))
    open(os.path.join(HERE,"_r11run.mjs"),"w",encoding="utf-8").write(RUNNER)
    r = subprocess.run(["bun",os.path.join(HERE,"_r11run.mjs")],capture_output=True,text=True,cwd=YISIM,timeout=240,shell=True,encoding='utf-8')
    if r.returncode!=0:
        print("RUNERR", (r.stderr or '')[-1200:]); return None
    return json.load(open(os.path.join(HERE,"_r11res.json"),encoding="utf-8"))

def score(pool, opp_en):
    reqs=[]
    for p in pool:
        reqs.append({"a_first":True,"a":dict(cultivation=42,hp=82,physique=24,max_physique=59,cards=p),
                     "b":dict(cultivation=44,hp=80,physique=0,max_physique=51,cards=opp_en)})
    res = run(reqs)
    if res is None: return None
    scored=[]
    for p,r in zip(pool,res):
        if r.get('r') is None:
            continue
        wa,wb = r['r'][0], r['r'][1]
        f = 1 if wa=='a' else 0
        s = 1 if wb=='a' else 0
        scored.append((f+s, f, s, p))
    scored.sort(key=lambda x:(-x[0], -x[1]-x[2]))
    return scored

def main():
    a = sys.argv[1:]
    my_cn = a[0].split(',') if len(a)>0 and a[0] else []
    opp_cn = a[1].split(',') if len(a)>1 and a[1] else []
    slots = int(a[2]) if len(a)>2 else 8
    maxcombos = int(a[3]) if len(a)>3 else 2000
    topN = int(a[4]) if len(a)>4 else 15
    my = [to_en(c) for c in my_cn]
    opp = [to_en(c) for c in opp_cn]
    print("my_en:", my)
    print("opp_en:", opp)

    cnt = Counter(my)
    items = list(cnt.keys())
    def gen_multisets(items, cnt, slots):
        res=[]
        def rec(i, cur):
            if sum(cur.values())==slots:
                res.append(dict(cur)); return
            if i>=len(items): return
            name=items[i]
            for k in range(0, cnt[name]+1):
                if sum(cur.values())+k>slots: break
                cur[name]=k
                rec(i+1,cur)
                del cur[name]
        rec(0,{})
        return res
    msets = gen_multisets(items, cnt, slots)
    print("composition multisets:", len(msets))

    pool = []
    for m in msets:
        cards=[]
        for k,v in m.items(): cards += [k]*v
        seen=set()
        tries = min(50, max(1, len(set(itertools.permutations(cards)))))
        for _ in range(tries):
            random.shuffle(cards)
            t=tuple(cards)
            if t in seen: continue
            seen.add(t)
            pool.append(list(cards))
    print("total ordered candidates:", len(pool))
    if len(pool)>maxcombos:
        pool = random.sample(pool, maxcombos)

    s = score(pool, opp)
    if s is None: return
    err = [r for r in (run([]) or [])]
    print("==== TOP vs opp base ====")
    for sc in s[:topN]:
        print(f"both={sc[0]} first={sc[1]} second={sc[2]} :: {' | '.join(sc[3])}")

    opp1 = [c+(' 2' if not c.split(' ')[-1].isdigit() else '') for c in opp]
    # increment level properly
    def up(c):
        parts=c.rsplit(' ',1)
        if len(parts)==2 and parts[1].isdigit():
            return f"{parts[0]} {int(parts[1])+1}"
        return c+" 2"
    opp1=[up(c) for c in opp]
    s = score(pool, opp1)
    if s is None: return
    print("==== TOP vs opp +1 ====")
    for sc in s[:topN]:
        print(f"both={sc[0]} first={sc[1]} second={sc[2]} :: {' | '.join(sc[3])}")

if __name__=="__main__":
    main()
