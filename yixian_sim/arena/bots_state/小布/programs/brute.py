import os, json, itertools, sys
# Enumerate permutations of candidate hand/board card multiset, call yisim sim via subprocess?
# Simpler: we cannot call the sim tool from here. Just print permutations for reference.
# Instead, read current board from args.
print("usage: pass candidate cards; prints orderings to try manually")
