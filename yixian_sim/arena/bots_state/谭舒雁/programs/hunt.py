import os, json
d = os.environ['YISIM_DIR']
with open(os.path.join(d, 'swogi.json'), encoding='utf-8') as f:
    data = json.load(f)
# my chars: heal(he), plant? and fulu. Let's list all cards with keyword in name/actions
kws = ['heal','max_hp','bonus_heal','hp','qi']
for cid, c in data.items():
    nm = c.get('name','')
    acts = json.dumps(c.get('actions',[]),ensure_ascii=False)
    ch = c.get('character')
    # find cards gaining hp / heal high, and plant
    if 'max_hp' in acts and 'hp' in acts:
        print(cid, ch, nm, '| qi',c.get('qi_cost'),'|', acts[:160])
