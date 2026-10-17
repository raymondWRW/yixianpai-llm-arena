
import os
YISIM = os.environ['YISIM_DIR']
p = os.path.join(YISIM,'parse_input.js')
print(open(p, encoding='utf-8', errors='replace').read()[:6000])
