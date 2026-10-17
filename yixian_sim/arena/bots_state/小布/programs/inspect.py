
import os
YISIM = os.environ['YISIM_DIR']
for f in ['batch_run.js','example.json','example.yaml','check_names.py']:
    p = os.path.join(YISIM,f)
    try:
        print("="*30, f)
        print(open(p, encoding='utf-8', errors='replace').read()[:3000])
    except Exception as e:
        print("ERR", e)
