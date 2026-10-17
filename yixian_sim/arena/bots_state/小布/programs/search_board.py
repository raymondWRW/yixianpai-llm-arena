
import os, json, subprocess, sys, itertools

YISIM = os.environ.get('YISIM_DIR')

# We can't call the sim tool from here easily; instead just print candidate lists
# Actually we rely on run_program being able to import yisim engine? Let's try.

def main():
    # list candidate cards
    cards = ["抱气法+1","踏破九霄+1","磅礴之势","朝气蓬勃+1","崩拳·降龙+1","崩拳·封+1","崩拳·惊触","九煞破灵曲","崩拳·弹+2","狂舞曲","浩然正气","锻髓"]
    print("cards:", cards)
    print("YISIM_DIR:", YISIM)
    try:
        print(os.listdir(YISIM))
    except Exception as e:
        print("err", e)

if __name__=="__main__":
    main()
