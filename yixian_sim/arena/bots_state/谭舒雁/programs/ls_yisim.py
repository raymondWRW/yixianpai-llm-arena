
import os
d = os.environ.get('YISIM_DIR', '?')
print("YISIM_DIR:", d)
for root, dirs, files in os.walk(d):
    for f in files:
        print(os.path.join(root, f))
    # limit depth
    if root.count(os.sep) - d.count(os.sep) > 2:
        dirs[:] = []
