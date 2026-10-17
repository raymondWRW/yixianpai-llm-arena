
import os, json, subprocess
YISIM = os.environ['YISIM_DIR']
HERE = os.path.dirname(os.path.abspath(__file__))
yisim_fwd = YISIM.replace("\\","/")
# name check with English names
names = ["Crash Fist - Block","Detect-Horse Palms","Crash Fist - Blitz","Crash Fist - Shake",
 "Crash Fist - Continue","Majestic Qi","Crash Fist - Inch Force","Crash Fist - Subdue Dragon",
 "Sky-Piercing Claw","Windward Palms","Strong Force","Detect Qi","Flower Sentient","Astral Fleche",
 "Shifting Stars","Astral Move - Cide","Astral Move - Flank","Falling Thunder","Qi Therapy"]
open(os.path.join(HERE,"_names.json"),"w",encoding="utf-8").write(json.dumps(names,ensure_ascii=False))
r = subprocess.run(["bun", os.path.join(HERE,"_namecheck.mjs")], capture_output=True, text=True, cwd=YISIM, timeout=60, shell=True, encoding='utf-8')
print(open(os.path.join(HERE,"_names_out.json"),encoding="utf-8").read())
