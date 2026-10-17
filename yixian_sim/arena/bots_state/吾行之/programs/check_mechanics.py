import os, sys

# Small helper: verify a few key yisim mechanics by locating the call sites
# in gamestate_full.js. Run: python check_mechanics.py
YISIM = os.environ["YISIM_DIR"]

def show(fname, needle, ctx=6):
    p = os.path.join(YISIM, fname)
    with open(p, encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    print(f"--- {fname}: lines containing '{needle}' ---")
    for i, l in enumerate(lines):
        if needle in l:
            print(f"  {i+1}: {l.rstrip()}")

# The single most important g28 finding: force_of_water pays out ONCE at end of turn.
show("gamestate_full.js", "do_force_of_water")
show("gamestate_full.js", "deal_damage(me.force_of_water)")
# 八门金锁阵 fires when opponent chases
show("gamestate_full.js", "do_octgates_lock_formation")
# 泉涌 mechanic
show("gamestate_full.js", "water_spirit_spring_stacks")
print("\nKEY RULE: 水势 is ONE end-of-turn hit = current stacks; ramp cards deal 0 direct. Field ATTACKERS.")
