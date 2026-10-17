"""
r11_reps.py — like r11_test but N reps per seat, matching live stats.
args: [my_cult, my_hp, my_phys, opp_cult, opp_hp, opp_phys, opp_cn_csv, reps, cand1 | cand2 | ...]
"""
import os, sys, json, subprocess
YISIM = os.environ['YISIM_DIR']
HERE = os.path.dirname(os.path.abspath(__file__))
yf = YISIM.replace("\\", "/")
_NAMES = json.load(open(os.path.join(YISIM,'names.json'),encoding='utf-8'))
_CN2EN={}
for d in _NAMES:
    cn,en=d.get('namecn',''),d.get('name','')
    if cn and en and cn not in _CN2EN: _CN2EN[cn]=en
def to_en(cn):
    lvl=1; base=cn
    if '+' in cn:
        base,num=cn.split('+',1)
        try: lvl=1+int(num)
        except: lvl=2
    en=_CN2EN.get(base)
    if en is None:
        for k,v in _CN2EN.items():
            if k.startswith(base) or base.startswith(k): en=v; break
    if en is None: en=base
    return en if lvl==1 else f"{en} {lvl}"
def up(c):
    parts=c.rsplit(' ',1)
    if len(parts)==2 and parts[1].isdigit(): return f"{parts[0]} {int(parts[1])+1}"
    return c+" 2"

RUNNER='''
import fs from 'fs';
import { GameState } from "%s/gamestate_full.js";
import { ready as cready } from "%s/card_name_to_id_fuzzy.js";
import parse_input from "%s/parse_input.js";
await cready;
const reqs = JSON.parse(fs.readFileSync(new URL('./_r11reqs.json', import.meta.url),'utf8'));
const out=[];
for (const req of reqs) {
  const reps = req.reps || 1;
  let fw=0, sw=0, ft=0, st=0, n=0;
  for (let k=0;k<reps;k++){
    for (const af of [true,false]) {
      try {
        const j = parse_input(JSON.stringify(req));
        const game = new GameState();
        const [p0,p1] = af ? [j.a,j.b] : [j.b,j.a];
        Object.assign(game.players[0], p0);
        Object.assign(game.players[1], p1);
        game.sim_n_turns(64);
        const log = game.output.join('\\n');
        let m = log.match(/player ([01]) \\([^)]*\\) wins/);
        let w = m ? (m[1]==='0' ? (af?'a':'b') : (af?'b':'a')) : null;
        if (af) { if(w==='a') fw++; ft++; } else { if(w==='a') sw++; st++; }
      } catch(e){}
    }
  }
  out.push({first:fw, firstn:ft, second:sw, secondn:st});
}
fs.writeFileSync(new URL('./_r11res.json', import.meta.url), JSON.stringify(out));
''' % (yf,yf,yf)

def main():
    a=sys.argv[1:]
    mc,mh,mp,oc,oh,op = int(a[0]),int(a[1]),int(a[2]),int(a[3]),int(a[4]),int(a[5])
    opp_cn=a[6].split(','); reps=int(a[7]); cands=[c for c in a[8:] if c]
    opp=[to_en(c) for c in opp_cn]
    boards=[[to_en(x) for x in c.split(',')] for c in cands]
    reqs=[]
    for b in boards:
        reqs.append({"a_first":True,"reps":reps,
                     "a":dict(cultivation=mc,hp=mh,physique=mp,max_physique=mp+35,cards=b),
                     "b":dict(cultivation=oc,hp=oh,physique=op,max_physique=op+51,cards=opp)})
    open(os.path.join(HERE,"_r11reqs.json"),"w",encoding="utf-8").write(json.dumps(reqs,ensure_ascii=False))
    open(os.path.join(HERE,"_r11run.mjs"),"w",encoding="utf-8").write(RUNNER)
    r=subprocess.run(["bun",os.path.join(HERE,"_r11run.mjs")],capture_output=True,text=True,cwd=YISIM,timeout=150,shell=True,encoding='utf-8')
    if r.returncode!=0: print("ERR",(r.stderr or '')[-800:]); return
    res=json.load(open(os.path.join(HERE,"_r11res.json"),encoding="utf-8"))
    for i,b in enumerate(boards):
        x=res[i]
        print(f"#{i}: first {x['first']}/{x['firstn']}  second {x['second']}/{x['secondn']} :: {' | '.join(b)}")

if __name__=="__main__":
    main()
