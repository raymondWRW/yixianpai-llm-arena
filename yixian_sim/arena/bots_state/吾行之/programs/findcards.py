import os, json, sys
d = os.environ['YISIM_DIR']
data = json.load(open(os.path.join(d,'swogi.json')))
# print all cards whose id starts with given prefix, or whose name matches
pat = sys.argv[1] if len(sys.argv)>1 else "木灵"
cnt=0
for cid, info in data.items():
    nm = info.get('name','')
    if pat in nm or pat in cid:
        print(cid, nm)
        cnt+=1
print("total", cnt)
