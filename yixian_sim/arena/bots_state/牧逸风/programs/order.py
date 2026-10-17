import itertools
# print orderings to test: keep 云舞诀 early for qi, then big swords + cloud swords
pool = ["云舞诀","云剑·极意+1","云剑·无锋","云剑·探云+2","云剑·飞刺+1","云剑·汇灵+1","巨虎灵剑+1","巨鹏灵剑","巨鲸灵剑","巨鲲灵剑"]
# candidates: permutations with 云舞诀 fixed first, pick 7 of remaining
import random
random.seed(1)
base = ["云舞诀"]
rest = [c for c in pool if c!="云舞诀"]
cands=[]
for perm in itertools.permutations(rest, 7):
    cands.append(tuple(base+list(perm)))
print("total", len(cands))
# sample 60
for c in random.sample(cands, 60):
    print(list(c))
