"""
r11_test.py — test a fixed list of candidate boards vs pid1, both seats,
base and +1. args: [opp_cn_csv, cand1_cards | cand2_cards | ...]
Each candidate separated by ' | ', cards within by ','.
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
''' % (yf,yf,yf)

def run(reqs):
    open(os.path.join(HERE,"_r11reqs.json"),"w",encoding="utf-8").write(json.dumps(reqs,ensure_ascii=False))
    open(os.path.join(HERE,"_r11run.mjs"),"w",encoding="utf-8").write(RUNNER)
    r=subprocess.run(["bun",os.path.join(HERE,"_r11run.mjs")],capture_output=True,text=True,cwd=YISIM,timeout=120,shell=True,encoding='utf-8')
    if r.returncode!=0: print("ERR",(r.stderr or '')[-600:]); return None
    return json.load(open(os.path.join(HERE,"_r11res.json"),encoding="utf-8"))

def main():
    a=sys.argv[1:]
    opp_cn=a[0].split(',') if a else []
    cands=[c for c in a[1:] if c]
    opp=[to_en(c) for c in opp_cn]; opp1=[up(c) for c in opp]
    boards=[[to_en(x) for x in c.split(',')] for c in cands]
    reqs=[]
    for b in boards:
        reqs.append({"a_first":True,"a":dict(cultivation=42,hp=82,physique=24,max_physique=59,cards=b),
                     "b":dict(cultivation=44,hp=80,physique=0,max_physique=51,cards=opp)})
    r0=run(reqs)
    reqs=[]
    for b in boards:
        reqs.append({"a_first":True,"a":dict(cultivation=42,hp=82,physique=24,max_physique=59,cards=b),
                     "b":dict(cultivation=44,hp=80,physique=0,max_physique=51,cards=opp1)})
    r1=run(reqs)
    for i,b in enumerate(boards):
        s=r0[i]['r'] if r0 and r0[i].get('r') else None
        t=r1[i]['r'] if r1 and r1[i].get('r') else None
        print(f"#{i}: base F{s[0] if s else '?'} S{s[1] if s else '?'} | +1 F{t[0] if t else '?'} S{t[1] if t else '?'} :: {' | '.join(b)}")

if __name__=="__main__":
    main()
