
import os, json, subprocess
YISIM = os.environ['YISIM_DIR']
HERE = os.path.dirname(os.path.abspath(__file__))
yisim_fwd = YISIM.replace("\\","/")

RUNNER = '''
import fs from 'fs';
import { GameState } from "%s/gamestate_full.js";
import { ready as cready } from "%s/card_name_to_id_fuzzy.js";
import parse_input from "%s/parse_input.js";
await cready;
const reqs = JSON.parse(fs.readFileSync(new URL('./_reqs.json', import.meta.url),'utf8'));
const out=[];
for (const req of reqs) {
  try {
    const j = parse_input(JSON.stringify(req));
    const a_first = j.a_first !== false;
    const game = new GameState();
    const [p0,p1] = a_first ? [j.a,j.b] : [j.b,j.a];
    Object.assign(game.players[0], p0);
    Object.assign(game.players[1], p1);
    game.sim_n_turns(64);
    const log = game.output.join('\\n');
    let winner=null;
    let m = log.match(/player ([01]) \\([^)]*\\) wins/);
    if(m) winner = m[1];
    let w = null;
    if (winner!==null){ w = winner==='0' ? (a_first?'a':'b') : (a_first?'b':'a'); }
    out.push({winner:w});
  } catch(e){ out.push({error:''+e}); }
}
fs.writeFileSync(new URL('./_res.json', import.meta.url), JSON.stringify(out));
''' % (yisim_fwd,yisim_fwd,yisim_fwd)
open(os.path.join(HERE,"_simrun.mjs"),"w",encoding="utf-8").write(RUNNER)

def run(reqs):
    open(os.path.join(HERE,"_reqs.json"),"w",encoding="utf-8").write(json.dumps(reqs,ensure_ascii=False))
    r = subprocess.run(["bun",os.path.join(HERE,"_simrun.mjs")],capture_output=True,text=True,cwd=YISIM,timeout=120,shell=True,encoding='utf-8')
    if r.returncode!=0:
        print("ERR", (r.stderr or '')[-800:]); return None
    return json.load(open(os.path.join(HERE,"_res.json"),encoding="utf-8"))

if __name__=="__main__":
    my = ["Crash Fist - Block","Detect-Horse Palms","Crash Fist - Blitz","Crash Fist - Shake",
      "Crash Fist - Continue","Majestic Qi","Crash Fist - Inch Force","Crash Fist - Subdue Dragon"]
    opp = ["Detect Qi","Flower Sentient","Astral Fleche","Shifting Stars","Astral Move - Cide","Astral Move - Flank","Falling Thunder","Qi Therapy"]
    res = run([{"a_first":True,"a":dict(cultivation=60,hp=85,physique=23,max_physique=73,cards=my),
                "b":dict(cultivation=57,hp=114,physique=0,max_physique=63,cards=opp)}])
    print("TEST:", res)
