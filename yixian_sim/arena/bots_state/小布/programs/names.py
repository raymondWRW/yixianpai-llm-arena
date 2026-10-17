
import os, json, subprocess
YISIM = os.environ['YISIM_DIR']
# Write a small bun script in MY dir that imports from YISIM via absolute path? Modules are relative.
# Instead: use bun -e with stdin? bun supports eval and can import absolute path.
script = 'import { card_name_to_id_fuzzy, ready } from "%s/card_name_to_id_fuzzy.js"; await ready; for (const n of process.argv.slice(2)) { try { console.log(n, "=>", card_name_to_id_fuzzy(n)); } catch(e){ console.log(n, "ERR", ""+e); } }' % YISIM.replace("\\","/")
names = ["崩拳·封","探马掌","崩拳·寸劲","Crash Fist - Block","crash fist block","探灵","气疗术+1"]
r = subprocess.run(["bun","-e",script]+names, capture_output=True, text=True, cwd=YISIM, timeout=60, shell=True)
print(r.stdout)
print(r.stderr[-600:])
