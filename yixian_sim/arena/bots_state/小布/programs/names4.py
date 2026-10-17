
import os, json, subprocess
YISIM = os.environ['YISIM_DIR']
HERE = os.path.dirname(os.path.abspath(__file__))
yisim_fwd = YISIM.replace("\\","/")
# runner reads names from _names.json
runner = '''
import fs from 'fs';
import { card_name_to_id_fuzzy, ready } from "%s/card_name_to_id_fuzzy.js";
await ready;
const names = JSON.parse(fs.readFileSync(new URL('./_names.json', import.meta.url), 'utf8'));
let out=[];
for (const n of names) { try { out.push([n, card_name_to_id_fuzzy(n)]); } catch(e){ out.push([n, "ERR:"+e]); } }
fs.writeFileSync(new URL('./_names_out.json', import.meta.url), JSON.stringify(out, null, 1));
''' % yisim_fwd
p = os.path.join(HERE, "_namecheck.mjs")
open(p,"w",encoding="utf-8").write(runner)
names = ["崩拳·封","探马掌","崩拳·突","崩拳·撼","崩拳·连崩","气若悬河","崩拳·寸劲","崩拳·降龙",
  "破空爪+1","迎风掌","锻神开海","势大力沉","锻骨","天运·趋吉","探灵","落花有意","飞星刺+1",
  "斗转星移+1","星弈·断","星弈·夹+1","落雷术+1","气疗术+1","normal attack"]
open(os.path.join(HERE,"_names.json"),"w",encoding="utf-8").write(json.dumps(names,ensure_ascii=False))
r = subprocess.run(["bun", p], capture_output=True, text=True, cwd=YISIM, timeout=60, shell=True, encoding='utf-8')
print("OUT", r.stdout[:300], "ERR", (r.stderr or "")[-500:])
print(open(os.path.join(HERE,"_names_out.json"),encoding="utf-8").read())
