
import os
YISIM = os.environ['YISIM_DIR']
p = os.path.join(YISIM,'batch_run.js')
print(open(p, encoding='utf-8', errors='replace').read())
print("="*40, "example.json head")
print(open(os.path.join(YISIM,'example.json'), encoding='utf-8', errors='replace').read()[:1500])
