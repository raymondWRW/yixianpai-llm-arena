import os
d=os.environ['YISIM_DIR']
f=os.path.join(d,'gamestate_full.js')
lines=open(f).read().split('\n')
print('\n'.join(f"{i+1}: {lines[i]}" for i in range(4425,4460)))
