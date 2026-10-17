import os, sys
d = os.environ['YISIM_DIR']
fn = sys.argv[1]
a = int(sys.argv[2]); b = int(sys.argv[3])
for root, dirs, files in os.walk(d):
    for f in files:
        if f == fn:
            p = os.path.join(root, f)
            lines = open(p, encoding='utf-8').read().split('\n')
            for i in range(a-1, min(b, len(lines))):
                print(i+1, lines[i])
