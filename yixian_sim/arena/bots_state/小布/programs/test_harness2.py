
import os, json, subprocess
YISIM = os.environ['YISIM_DIR']
req = {
  "a_first": True,
  "a": {"cultivation":60,"hp":85,"physique":23,"max_physique":73,
        "cards":["崩拳·封","探马掌","崩拳·突","崩拳·撼","崩拳·连崩","气若悬河","崩拳·寸劲","崩拳·降龙"]},
  "b": {"cultivation":57,"hp":114,"physique":0,"max_physique":63,
        "cards":["探灵","落花有意","飞星刺+1","斗转星移+1","星弈·断","星弈·夹+1","落雷术+1","气疗术+1"]},
  "want_log": False,
}
inp = json.dumps({"battle": req})+"\n"
for cmd in [["bun","batch_run.js"],["node","--experimental-specifier-resolution=node","batch_run.js"]]:
    try:
        r = subprocess.run(cmd, input=inp, capture_output=True, text=True, cwd=YISIM, timeout=60, shell=True)
        print("CMD",cmd,"OUT:", r.stdout[:800], "ERRtail:", r.stderr[-400:])
    except Exception as e:
        print("CMD",cmd,"EXC",e)
