import os, re
d = os.environ['YISIM_DIR']
src = open(os.path.join(d, 'gamestate_full.js')).read()
lines = src.split('\n')
def show(start, end):
    for i in range(start-1, min(end, len(lines))):
        print(i+1, lines[i])
# do_internal_injury
show(2798, 2830)
print('===== start of turn region 3370-3400')
show(3370, 3400)
