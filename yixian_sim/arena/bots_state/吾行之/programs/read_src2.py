import os, sys

def main():
    d = os.environ['YISIM_DIR']
    fname = sys.argv[1] if len(sys.argv) > 1 else 'gamestate_full.js'
    start = int(sys.argv[2]); end = int(sys.argv[3])
    with open(os.path.join(d, fname), encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    for i in range(start-1, min(end, len(lines))):
        print(i+1, lines[i], end='')

if __name__ == '__main__':
    main()
