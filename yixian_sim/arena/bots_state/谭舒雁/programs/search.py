import itertools, subprocess, os, json

# We will brute force orderings of a card set using simulate via the tool is hard from subprocess.
# Instead just print candidate orderings for manual sim.
# Cards available (board + hand):
pool = ["天元心法","紫气东来","众星拱月","梅开二度","星弈·打+1","镇魂封元符+1","星弈·点+1","星弈·挡+1","反震心法","海底捞月"]
print(pool)
