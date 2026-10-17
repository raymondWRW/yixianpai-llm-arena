
import os
d = os.environ.get('YISIM_DIR', '?')
hits = []
for root, dirs, files in os.walk(d):
    for f in files:
        if f.endswith('.js'):
            hits.append(os.path.join(root, f))
for h in hits:
    print(h)
