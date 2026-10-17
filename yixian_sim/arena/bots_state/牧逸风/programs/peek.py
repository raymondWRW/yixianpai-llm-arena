import os, sys
d = os.environ['YISIM_DIR']
fn = sys.argv[1]; a = int(sys.argv[2]); b = int(sys.argv[3])
with open(os.path.join(d, fn), encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if a <= i <= b:
            print(i, line.rstrip())
