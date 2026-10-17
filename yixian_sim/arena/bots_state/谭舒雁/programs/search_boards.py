
import os, json, itertools, subprocess

Y = os.environ['YISIM_DIR']
BATCH = os.path.join(Y, 'batch_run.js')

# My stats (live): hp base 62, physique 0, cultivation 26 -> seat decided, I act first.
# Opp pid3 小布 last known: maxHP 59, physique 0, hp base 59.
MY = {"hp": 62, "physique": 0, "max_physique": 400, "cultivation": 26,
      "character": "谭舒雁"}
# We'll set cards in the search.

# Candidate card set (hand+board), with level in name where known.
avail = ["凶象","斗转星移","星弈·挡+1","星弈·挡","藕断丝连","斩草除根",
         "众星拱月","天运·趋吉","震卦","察体"]

# Opp hypotheses: last known board + upgrades
opp_last = ["探灵","凶象","起势","岿然不动","破空爪+1","破空爪","血气方刚"]
opp_mod  = ["探灵","凶象","起势","岿然不动","破空爪+1","破空爪","血气方刚+1"]
opp_high = ["探灵","凶象","起势","岿然不动","破空爪+2","破空爪+1","血气方刚+1"]

def make_battle(mycards, oppcards, i_first=True):
    a = dict(MY); a["cards"] = mycards
    b = {"hp":59,"physique":0,"max_physique":400,"cultivation":17,"cards":oppcards}
    # a_first controls seating; our MY goes to a
    return {"a": a, "b": b, "a_first": i_first, "want_log": False, "deck_slots": 8}

def run_batch(battles):
    inp = "\n".join(json.dumps({"battle": b, "want_log": False}) for b in battles)
    p = subprocess.run(["node", BATCH], input=inp, capture_output=True, text=True, cwd=Y)
    out = []
    for line in p.stdout.splitlines():
        line=line.strip()
        if not line: continue
        try: out.append(json.loads(line))
        except: out.append({"error": line})
    if p.stderr.strip():
        print("STDERR:", p.stderr[:500])
    return out

# Generate all 7-card subsets and orderings? Too many. Do: subsets of size 7 from avail, all permutations.
# avail size 10 -> C(10,7)=120 subsets * 5040 perms = 604800 too many.
# Instead: search over orderings of the 8 most relevant, take top by quick score.

def score_board(mycards, opp, reps=2):
    battles = [make_battle(mycards, opp, True) for _ in range(reps)]
    res = run_batch(battles)
    wins = sum(1 for r in res if r.get("winner")=="a")
    return wins, reps

# Step 1: which 7-card subset? Test a fixed set of "core" then permutations.
core = ["凶象","斗转星移","众星拱月","星弈·挡+1","斩草除根","星弈·挡","藕断丝连","震卦","天运·趋吉"]
# Subsets of size 7 from core (9 choose 7 = 36), sample some permutations each
best = []
count=0
import random
random.seed(1)
subsets = list(itertools.combinations(core,7))
print("subsets:", len(subsets))
# For each subset test 30 random permutations vs opp_mod
tasks=[]
meta=[]
for sub in subsets:
    perms = list(itertools.permutations(sub))
    if len(perms)>40: perms = random.sample(perms,40)
    for pm in perms:
        tasks.append((list(pm),tuple(sub)))
        
print("total tasks:", len(tasks))
# run in chunks
results=[]
CH=300
for i in range(0,len(tasks),CH):
    chunk=tasks[i:i+CH]
    battles=[make_battle(pm, opp_mod, True) for pm,_ in chunk]
    rs=run_batch(battles)
    for (pm,sub),r in zip(chunk,rs):
        results.append((r.get("winner")=="a", tuple(pm), sub, r.get("turns")))
winners=[x for x in results if x[0]]
print("wins vs opp_mod (first seat):", len(winners), "/", len(results))
winners.sort(key=lambda x: (x[3] or 99))
for w in winners[:15]:
    print(w)
