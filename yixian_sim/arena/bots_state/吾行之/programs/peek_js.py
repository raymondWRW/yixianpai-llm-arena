import os, re, sys
Y = os.environ['YISIM_DIR']
fn = sys.argv[1] if len(sys.argv) > 1 else 'calculate_destiny_damage'
path = os.path.join(Y, 'gamestate_full.js')
s = open(path).read()
i = s.find(fn)
if i < 0:
    print('not found')
else:
    print(s[i-40:i+900])
