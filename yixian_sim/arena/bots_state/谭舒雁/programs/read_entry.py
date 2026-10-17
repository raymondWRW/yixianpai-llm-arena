
import os
d = os.environ['YISIM_DIR']
for fn in ['just_run.js','yisim_entry.js','batch_run.js']:
    p = os.path.join(d, fn)
    print('='*30, fn, '='*30)
    try:
        with open(p, encoding='utf-8', errors='replace') as f:
            print(f.read()[:3000])
    except Exception as e:
        print('ERR', e)
