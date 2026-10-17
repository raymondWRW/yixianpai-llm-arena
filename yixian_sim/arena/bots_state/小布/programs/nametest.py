"""nametest.py — test how the fuzzy matcher resolves names+levels."""
import os, json, subprocess
YISIM = os.environ['YISIM_DIR']
HERE = os.path.dirname(os.path.abspath(__file__))
yf = YISIM.replace("\\","/")
runner = '''
import fs from 'fs';
import { card_name_to_id_fuzzy, ready } from "%s/card_name_to_id_fuzzy.js";
await ready;
const names = JSON.parse(fs.readFileSync(new URL('./_nametest_in.json', import.meta.url), 'utf8'));
let out=[];
for (const n of names) { try { out.push([n, card_name_to_id_fuzzy(n)]); } catch(e){ out.push([n, "ERR:"+(""+e).slice(0,60)]); } }
fs.writeFileSync(new URL('./_nametest_out.json', import.meta.url), JSON.stringify(out, null, 1));
''' % yf
open(os.path.join(HERE,"_nametest.mjs"),"w",encoding="utf-8").write(runner)
names = ["Ghost Howling", "Ghost Howling 2", "Ghost Howling+1", "Ghost Howling 3",
         "Vigorous Force 2", "Crash Fist - Entangle", "Crash Fist - Entangle 2",
         "Sailing through Sky", "Spiritage Formation", "Ghost Howling (2)",
         "vigorous force 2"]
open(os.path.join(HERE,"_nametest_in.json"),"w",encoding="utf-8").write(json.dumps(names,ensure_ascii=False))
r = subprocess.run(["bun", os.path.join(HERE,"_nametest.mjs")], capture_output=True, text=True, cwd=YISIM, timeout=60, shell=True, encoding='utf-8')
print("ERR", (r.stderr or "")[-400:])
print(open(os.path.join(HERE,"_nametest_out.json"),encoding="utf-8").read())
