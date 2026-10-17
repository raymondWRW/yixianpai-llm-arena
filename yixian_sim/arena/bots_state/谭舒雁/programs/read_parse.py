
import os
d = os.environ['YISIM_DIR']
with open(os.path.join(d,'parse_input.js'), encoding='utf-8', errors='replace') as f:
    print(f.read()[:6000])
