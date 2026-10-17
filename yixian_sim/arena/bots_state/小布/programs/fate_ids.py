import os, json, glob
YISIM = os.environ['YISIM_DIR']
targets = ['磨砺不止','再生之躯','顿悟','副职兼修','筋骨健壮','崩拳传承','锻体','体修入道','稳步根基','变换之道','感悟丛生','强健筋骨']
for pat in ['**/*.json']:
    for f in glob.glob(os.path.join(YISIM, pat), recursive=True):
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        def walk(o, key=''):
            if isinstance(o, dict):
                # If dict maps id->obj with a name field
                nm = None
                for nk in ('name','Name','term','text_cn','text'):
                    if nk in o and isinstance(o[nk], str):
                        nm = o[nk]; break
                if nm and any(t in nm for t in targets):
                    print(os.path.relpath(f,YISIM), 'IDKEY=', key, 'NAME=', nm[:40])
                for k,v in o.items():
                    walk(v, k)
            elif isinstance(o, list):
                for i,v in enumerate(o):
                    walk(v, f'{key}[{i}]')
        walk(d)
