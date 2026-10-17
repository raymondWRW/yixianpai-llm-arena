
import itertools, json, subprocess, os, sys, random

# We'll use the env var for yisim source if provided; but simplest: shell out to nothing.
# Instead, print candidate permutations for the agent to sim.

avail = ["凶象","斗转星移","星弈·挡+1","星弈·挡","藕断丝连","斩草除根",
         "众星拱月","天运·趋吉","震卦"]

print("total avail:", len(avail))
print("candidates are permutations of size up to 7")
