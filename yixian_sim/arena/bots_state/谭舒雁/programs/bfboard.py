"""Brute-force board permutations vs opponents, calling yisim via node."""
import os, json, subprocess, shutil, glob

YISIM = os.environ['YISIM_DIR']
HERE = os.path.dirname(os.path.abspath(__file__))
ENG = os.path.join(HERE, 'engine')
NM = os.path.join(ENG, 'node_modules', 'seedrandom')

SEEDRANDOM = '''function seedrandom(seed, opts) {
  let s = 0;
  const str = String(seed == null ? Math.random() : seed);
  for (let i = 0; i < str.length; i++) s = (s * 31 + str.charCodeAt(i)) >>> 0;
  s = s || 1;
  function rng() {
    s ^= s << 13; s >>>= 0;
    s ^= s >> 17;
    s ^= s << 5; s >>>= 0;
    return s / 4294967296;
  }
  rng.quick = rng; rng.double = rng; rng.int32 = () => (s | 0);
  return rng;
}
seedrandom.alea = seedrandom; seedrandom.xor128 = seedrandom;
export default seedrandom;
'''

def setup():
    os.makedirs(NM, exist_ok=True)
    for f in glob.glob(os.path.join(YISIM, '*.js')):
        shutil.copy(f, ENG)
    with open(os.path.join(NM, 'package.json'), 'w') as f:
        f.write('{"name":"seedrandom","version":"0.0.0","type":"module","main":"index.js"}')
    with open(os.path.join(NM, 'index.js'), 'w', encoding='utf-8') as f:
        f.write(SEEDRANDOM)

DRIVER = '''
import { simulate, yisim } from './engine/yisim_entry.js';
await yisim.ready();
const chunks = [];
for await (const c of process.stdin) chunks.push(c);
const job = JSON.parse(Buffer.concat(chunks).toString());
const out = [];
for (const t of job.tests) {
  try {
    const r = simulate(
      t.my_cards,
      { rollMode: 'average', verbose: !!job.verbose, turnOrder: t.turnOrder || 'tied',
        playerState: t.playerState, opponentSlots: t.oppSlots, opponentState: t.oppState,
        maxTurns: 64 }
    );
    out.push({ cards: t.my_cards, turnOrder: t.turnOrder, outcome: r.outcome,
               verdict: r.verdict, endTurn: r.endTurn, error: r.error, tag: t.tag });
  } catch (e) {
    out.push({ cards: t.my_cards, error: String(e), tag: t.tag });
  }
}
console.log(JSON.stringify(out));
'''

def run_tests(tests, verbose=False):
    setup()
    dp = os.path.join(HERE, 'driver.mjs')
    with open(dp, 'w', encoding='utf-8') as f:
        f.write(DRIVER)
    job = {'tests': tests, 'verbose': verbose}
    p = subprocess.run(['node', dp], input=json.dumps(job).encode('utf-8'),
                       capture_output=True, cwd=HERE, timeout=45)
    if p.returncode != 0:
        return {'ERROR': p.stderr.decode('utf-8', 'replace')[-2500:]}
    try:
        return json.loads(p.stdout.decode('utf-8', 'replace'))
    except Exception:
        return {'RAW': p.stdout.decode('utf-8','replace')[-2000:],
                'ERR': p.stderr.decode('utf-8','replace')[-1500:]}

if __name__ == '__main__':
    r = run_tests([{'my_cards': ['巽卦','揽雀尾+1'], 'turnOrder': 'tied'}], verbose=False)
    print(json.dumps(r, ensure_ascii=False, indent=1)[:3000])
