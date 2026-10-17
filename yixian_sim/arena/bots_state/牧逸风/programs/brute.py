
# brute force is done via simulate calls externally; this helper just prints permutations
import itertools
cards = ["云剑·极意","云剑·无锋","云剑·探云+2","云剑·飞刺","剑挡","飞牙剑","震雷剑","巨虎灵剑+1"]
# fix cloud swords first (positions 0-3), permute the rest
tail = ["剑挡","飞牙剑","震雷剑","巨虎灵剑+1"]
for perm in itertools.permutations(tail):
    print(list(cards[:4]) + list(perm))
