import os
p = os.path.join(os.environ['YISIM_DIR'], 'gamestate_full.js')
lines = open(p).read().split('\n')
print('\n'.join(f"{i+1}: {l}" for i, l in enumerate(lines[1615:1700])))
