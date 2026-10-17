import os, glob
d = os.environ['YISIM_DIR']
print("YISIM_DIR contents:")
for f in sorted(os.listdir(d)):
    print(" ", f)
print("=== search all files for fate names ===")
terms = ["磨砺不止", "顿悟", "稳固根基", "磨砺", "顿悟"]
for root, dirs, files in os.walk(d):
    for fn in files:
        fp = os.path.join(root, fn)
        try:
            with open(fp, encoding='utf-8') as f:
                data = f.read()
        except Exception:
            continue
        for t in terms:
            if t in data:
                print("HIT", fp, t)
