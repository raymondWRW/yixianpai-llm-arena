
import os
YISIM = os.environ['YISIM_DIR']
print(open(os.path.join(YISIM,'card_name_to_id_fuzzy.js'),encoding='utf-8',errors='replace').read()[:4000])
