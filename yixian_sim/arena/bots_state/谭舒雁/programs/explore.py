import os, glob, sys
d = os.environ['YISIM_DIR']
for f in sorted(glob.glob(os.path.join(d, '**', '*'), recursive=True)):
    if os.path.isfile(f):
        print(os.path.relpath(f, d), os.path.getsize(f))
