
import itertools, json, os, sys
# We can't call yisim directly here easily; instead just enumerate candidate boards for manual sim.
hand = ['巽卦', '揽雀尾', '星弈·夹', '白鹤亮翅', '藕断丝连']
combos = []
for r in [3]:
    for c in itertools.combinations(hand, r):
        for perm in itertools.permutations(c):
            combos.append(list(perm))
# dedupe
seen=set(); out=[]
for b in combos:
    k=tuple(b)
    if k in seen: continue
    seen.add(k); out.append(b)
print(len(out))
for b in out: print('|'.join(b))
