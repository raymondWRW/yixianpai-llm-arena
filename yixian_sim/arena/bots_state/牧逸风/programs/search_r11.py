
# Search board orderings vs announced opp to maximize hp_delta (win margin).
import itertools, subprocess, os, json, sys
# We can't call simulate directly from here; instead we print candidate orderings.
# Strategy: fix economy/qi/dur cards early, permute attack finishers.
# Core: 邪蛊阵(CONT), 化灵诀(Qi), 辟邪阵纹(DEF), 碎杀阵(CONT buff), 龟甲阵(CONT DEF)
core = ["邪蛊阵","化灵诀","辟邪阵纹","碎杀阵+1","龟甲阵+1"]
attacks = ["巨鲸灵剑","震雷剑+1","地煞剑"]
# try a few orderings of the attack cards among the tail, and a couple core placements
outs = []
tails = list(itertools.permutations(attacks))
for t in tails:
    outs.append(core + list(t))
    outs.append(["邪蛊阵","化灵诀","辟邪阵纹","碎杀阵+1"] + list(t) + ["龟甲阵+1"])
for o in outs:
    print(json.dumps(o, ensure_ascii=False))
