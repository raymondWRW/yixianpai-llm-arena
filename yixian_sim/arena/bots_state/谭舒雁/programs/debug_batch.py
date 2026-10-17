
import os, json, subprocess
Y = os.environ['YISIM_DIR']
BATCH = os.path.join(Y, 'batch_run.js')
b = {"a": {"hp":62,"physique":0,"max_physique":400,"cultivation":26,
           "cards":["凶象","斗转星移","众星拱月","星弈·挡+1","斩草除根","星弈·挡","藕断丝连"]},
     "b": {"hp":59,"physique":0,"max_physique":400,"cultivation":17,
           "cards":["探灵","凶象","起势","岿然不动","破空爪+1","破空爪","血气方刚+1"]},
     "a_first": True, "deck_slots": 8}
inp = json.dumps({"battle": b, "want_log": False}) + "\n"
p = subprocess.run(["node", BATCH], input=inp, capture_output=True, text=True, cwd=Y)
print("RC:", p.returncode)
print("OUT:", repr(p.stdout[:2000]))
print("ERR:", p.stderr[:1500])
