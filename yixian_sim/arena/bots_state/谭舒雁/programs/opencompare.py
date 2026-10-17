"""Compare opening turns of two 谭舒雁 boards vs the same opponent board, via the raw engine.
Usage: run_program('opencompare.py')  (edit the globals below)
"""
import os, json, subprocess
Y = os.environ['YISIM_DIR']
BATCH = os.path.join(Y, 'batch_run.js')

OPP = ["崩拳·闪击","威震四方+1","崩灭心法","崩拳·寸劲","崩拳·连崩+1","崩拳·惊触","崩拳·降龙","崩拳·突+1"]
BOARD_A = ["诸事不宜","厄劫缠身","杯弓蛇影","杯弓蛇影","天星·牵引","星弈·断+1","流水无情","吉运初显"]  # slot2 ejie
BOARD_B = ["厄劫缠身","诸事不宜","杯弓蛇影","杯弓蛇影","天星·牵引","星弈·断+1","流水无情","吉运初显"]  # slot1 ejie

def run(board, a_first, turns=6):
    b = {"a": {"hp":122,"physique":0,"max_physique":400,"cultivation":60,"cards":board},
         "b": {"hp":122,"physique":9,"max_physique":400,"cultivation":40,"cards":OPP},
         "a_first": a_first, "deck_slots": 8}
    inp = json.dumps({"battle": b, "want_log": True}) + "\n"
    p = subprocess.run(["node", BATCH], input=inp, capture_output=True, text=True, cwd=Y)
    return p.stdout, p.stderr

for label, board in [("A(slot2)", BOARD_A), ("B(slot1)", BOARD_B)]:
    for first in [True, False]:
        out, err = run(board, first)
        print("="*70)
        print(f"BOARD {label}  a_first={first}")
        # print first ~35 log lines
        lines = out.splitlines()
        for ln in lines[:40]:
            print(ln)
        print("... [truncated] ...")
        # try to show winner
        for ln in lines:
            if 'winner' in ln.lower() or 'loses' in ln.lower() or 'wins' in ln.lower():
                print("RESULT:", ln)
