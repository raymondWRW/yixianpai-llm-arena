# -*- coding: utf-8 -*-
"""make_replays.py — per-bot replay HTMLs for an arena game.

    python make_replays.py --game 2

Parses games/gameN/game_log.txt + battles/*.log and writes
games/gameN/replays/replay_<botname>.html — one file per seat, showing that
bot's perspective round by round: cards dealt, every economy action, the
fielded board, stats (命/修为/境/HP/体魄), fate picks, what it saw of each
opponent (their LAST-round board — the same fog the bot played under), and
its battles with the full yisim turn-by-turn log.
"""
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

_HERE = Path(__file__).resolve().parent

NAMES = {0: None, 1: None, 2: None, 3: None}   # filled from the log


def parse_game(gdir: Path):
    text = (gdir / "game_log.txt").read_text(encoding="utf-8")
    lines = text.splitlines()
    rounds = {}          # rnd -> per-round dict
    cur = None
    battle_idx = {}      # rnd -> running battle index (for log filenames)

    def round_entry(rnd):
        if rnd not in rounds:
            rounds[rnd] = {"deals": {}, "actions": {}, "fates": {}, "notes": [],
                           "battles": [], "standings": {}, "elim": [],
                           "matchups": [], "hands": {}}
        return rounds[rnd]

    for ln in lines:
        m = re.match(r"R(\d+) pid(\d) dealt: (.*)", ln)
        if m:
            cur = int(m.group(1))
            round_entry(cur)["deals"][int(m.group(2))] = \
                [c.strip() for c in m.group(3).split(",")]
            continue
        m = re.match(r"R(\d+) pid(\d) (\S+) acted \((\d+)s\): (.*)", ln)
        if m:
            rnd, pid, name = int(m.group(1)), int(m.group(2)), m.group(3)
            NAMES[pid] = name
            acts = [a.strip() for a in m.group(5).split("; ") if a.strip()]
            round_entry(rnd)["actions"][pid] = {"secs": int(m.group(4)),
                                                "acts": acts}
            continue
        m = re.match(r"\s+pid(\d) 天命@境(\d) (?:picked|default) (\d+):(\S+) from \[(.*)\]", ln)
        if m and cur:
            offers = re.findall(r"\((\d+), '([^']+)'\)", m.group(5))
            round_entry(cur)["fates"].setdefault(int(m.group(1)), []).append(
                {"realm": int(m.group(2)), "picked": m.group(4),
                 "offers": [o[1] for o in offers]})
            continue
        m = re.match(r"\s+battle pid(\d)\(first\) vs pid(\d): winner pid(\d) "
                     r"loser pid(\d) -(\d+)命(?: \(not applied\))? turns=(\d+)"
                     r"( \[extra for pid(\d)\])?", ln)
        if m and cur:
            i = battle_idx.get(cur, 0)
            battle_idx[cur] = i + 1
            round_entry(cur)["battles"].append({
                "first": int(m.group(1)), "second": int(m.group(2)),
                "winner": int(m.group(3)), "loser": int(m.group(4)),
                "loss": int(m.group(5)), "turns": int(m.group(6)),
                "not_applied": "(not applied)" in ln,
                "extra_for": int(m.group(8)) if m.group(8) else None,
                "idx": i})
            continue
        m = re.match(r"R(\d+) standings: (.*)", ln)
        if m:
            st = dict(re.findall(r"pid(\d):(\d+)", m.group(2)))
            round_entry(int(m.group(1)))["standings"] = \
                {int(k): int(v) for k, v in st.items()}
            continue
        m = re.match(r"R(\d+) pid(\d) hand: (.*)", ln)
        if m:   # end-of-round hand snapshot (games 8+)
            hand = [] if m.group(3).strip() == "(empty)" else \
                [c.strip() for c in m.group(3).split(",") if c.strip()]
            round_entry(int(m.group(1)))["hands"][int(m.group(2))] = hand
            continue
        m = re.match(r"R(\d+) matchups: (.*)", ln)
        if m:   # announced at round start (games 4+)
            ent = round_entry(int(m.group(1)))
            for part in m.group(2).split("; "):
                mm = re.match(r"pid(\d) vs pid(\d)(\(ghost\))?", part)
                if mm:
                    ent["matchups"].append({"a": int(mm.group(1)),
                                            "b": int(mm.group(2)),
                                            "ghost": bool(mm.group(3))})
            continue
        m = re.match(r"R(\d+) rerolls: (.*)", ln)
        if m:   # logged by run_arena from game 3 on — ground truth
            rr = dict(re.findall(r"pid(\d):(-?\d+)", m.group(2)))
            round_entry(int(m.group(1)))["rerolls_logged"] = \
                {int(k): int(v) for k, v in rr.items()}
            continue
        m = re.match(r"\s+pid(\d) (\S+) ELIMINATED", ln)
        if m and cur:
            round_entry(cur)["elim"].append(int(m.group(1)))
            continue
        if cur and (ln.startswith("  pid") or "turn cap" in ln):
            round_entry(cur)["notes"].append(ln.strip())
    return rounds


BOARD_RE = re.compile(r"board = \[([^\]]*)\]")
CULT_RE = re.compile(r"修为 \d+->(\d+)|\(\+1 修为 = (\d+)\)")
BT_RE = re.compile(r"BREAKTHROUGH(?: via 体魄)? 境\d->境(\d); HP (\d+); "
                   r"体魄 (\d+)/(\d+); 天命 \[([^\]]*)\]")


def track_rerolls(rounds: dict) -> dict:
    """End-of-round 换牌 charges per seat. Games logged after 2026-09-17 carry
    a ground-truth 'RN rerolls:' line; earlier games are reconstructed exactly:
    +3/round (R1-9), +4 (R10-12), +6 (R13+), unlimited banking; -1 per logged
    roll (云雾变幻 holder's first roll each round free); +N per logged [置换]
    换牌机会 grant; 战斗历练 +2 per applied win; 磨砺不止 +1 per 7 命 lost."""
    # NOTE: reconstruction is deliberately UNCAPPED — games 1-2 were played
    # before the 25-cap rule (2026-09-17) existed; the replay shows what the
    # engine actually did. Capped games log 'RN rerolls:' lines and never
    # reach this reconstruction path.
    grant = lambda r: 3 if r <= 9 else (4 if r <= 12 else 6)
    start_fate, talents = {}, {p: set() for p in range(4)}
    for rnd in sorted(rounds):          # pre-scan: innate fate = first 天命
        for p, a in rounds[rnd]["actions"].items():
            m = BT_RE.search("; ".join(a["acts"]))
            if m and p not in start_fate:
                start_fate[p] = m.group(5).split(",")[0].strip().strip("'")
    for p, f in start_fate.items():
        talents[p].add(f)
    rr = {p: 0 for p in range(4)}
    cum_paid = {p: 0 for p in range(4)}
    prev_stand = {p: 100 for p in range(4)}
    alive = set(range(4))
    out = {}
    for rnd in sorted(rounds):
        r = rounds[rnd]
        if r.get("rerolls_logged"):
            out[rnd] = dict(r["rerolls_logged"])
            for p, v in out[rnd].items():
                rr[p] = v
            for p, a in r["actions"].items():       # keep talent sync current
                m = BT_RE.search("; ".join(a["acts"]))
                if m:
                    talents[p] = {t.strip().strip("'")
                                  for t in m.group(5).split(",") if t.strip()}
            for p, d in (r["standings"] or {}).items():
                prev_stand[p] = d
            alive -= set(r["elim"])
            continue
        for p in alive:
            rr[p] += grant(rnd)
        for p, a in r["actions"].items():
            joined = "; ".join(a["acts"])
            n = len(re.findall(r"\brolled ", joined))
            free = 1 if ("云雾变幻" in talents[p] and n >= 1) else 0
            rr[p] -= max(0, n - free)
            rr[p] += sum(int(x) for x in re.findall(r"换牌机会\+(\d+)", joined))
            m = BT_RE.search(joined)
            if m:
                talents[p] = {t.strip().strip("'")
                              for t in m.group(5).split(",") if t.strip()}
                talents[p] |= {start_fate.get(p, "")} - {""}
        for b in r["battles"]:
            if b["not_applied"]:
                continue
            if "战斗历练" in talents[b["winner"]]:
                rr[b["winner"]] += 2
            if "易数化劫" in talents[b["loser"]]:
                rr[b["loser"]] += 1
        for p, d in (r["standings"] or {}).items():
            paid = prev_stand[p] - d
            if paid > 0:
                before = cum_paid[p]
                cum_paid[p] += paid
                if "磨砺不止" in talents[p]:
                    rr[p] += cum_paid[p] // 7 - before // 7
            prev_stand[p] = d
        out[rnd] = {p: rr[p] for p in alive}
        alive -= set(r["elim"])
    return out


def track_states(rounds: dict, pid: int, rerolls: dict = None):
    """Per-round snapshot for one seat: board after acting, stats, battles."""
    rerolls = rerolls or {}
    state = {"board": [], "cult": 0, "realm": 1, "hp": None, "tipo": "0/6",
             "talents": [], "destiny": 100}
    out = {}
    last_boards = {p: [] for p in range(4)}     # fog: boards BEFORE this round
    for rnd in sorted(rounds):
        r = rounds[rnd]
        seen = {p: list(last_boards[p]) for p in range(4)}
        # update every seat's board from its action line (for future fog)
        for p, a in r["actions"].items():
            joined = "; ".join(a["acts"])
            boards = BOARD_RE.findall(joined)
            if boards:
                last_boards[p] = [c.strip().strip("'") for c in
                                  boards[-1].split(",") if c.strip()]
        a = r["actions"].get(pid)
        acts = a["acts"] if a else []
        joined = "; ".join(acts)
        for mm in CULT_RE.finditer(joined):
            state["cult"] = int(mm.group(1) or mm.group(2))
        mb = BT_RE.search(joined)
        if mb:
            state["realm"] = int(mb.group(1))
            state["hp"] = int(mb.group(2))
            state["tipo"] = f"{mb.group(3)}/{mb.group(4)}"
            state["talents"] = [t.strip().strip("'") for t in
                                mb.group(5).split(",") if t.strip()]
        boards = BOARD_RE.findall(joined)
        if boards:
            state["board"] = [c.strip().strip("'") for c in
                              boards[-1].split(",") if c.strip()]
        if r["standings"]:
            state["destiny"] = r["standings"].get(pid, state["destiny"])
        opp_next = None
        for mu in r.get("matchups", []):
            if pid == mu["a"]:
                opp_next = {"pid": mu["b"], "ghost": mu["ghost"]}
                break
            if pid == mu["b"] and not mu["ghost"]:
                opp_next = {"pid": mu["a"], "ghost": False}
                break
        out[rnd] = {"deal": r["deals"].get(pid, []), "acts": acts,
                    "hand": r["hands"].get(pid),
                    "secs": a["secs"] if a else None,
                    "fates": r["fates"].get(pid, []),
                    "board": list(state["board"]),
                    "cult": state["cult"], "realm": state["realm"],
                    "hp": state["hp"], "tipo": state["tipo"],
                    "talents": list(state["talents"]),
                    "destiny": state["destiny"],
                    "standings": dict(r["standings"]),
                    "rerolls": {str(k): v
                                for k, v in rerolls.get(rnd, {}).items()},
                    "opp_next": opp_next,
                    "opp_seen": {p: seen[p] for p in range(4) if p != pid},
                    "battles": [b for b in r["battles"]
                                if pid in (b["first"], b["second"])],
                    "notes": [n for n in r["notes"] if f"pid{pid}" in n],
                    "elim": list(r["elim"])}
        if pid in r["elim"]:
            break
    return out


def battle_log(gdir: Path, rnd: int, idx: int) -> str:
    hits = sorted((gdir / "battles").glob(f"r{rnd}_{idx}_*.log"))
    return hits[0].read_text(encoding="utf-8") if hits else "(log missing)"


CSS = """
:root{--bg:#14161d;--panel:#1d212c;--panel2:#242a38;--ink:#e8e6df;--dim:#9aa0ae;
--gold:#d4b46a;--red:#e07a6a;--green:#7fbf7f;--blue:#7aa5d8;--line:#333a4a}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);
font:14px/1.5 "Segoe UI","Microsoft YaHei",sans-serif;padding:16px}
h1{font-size:18px;margin:0 0 4px}.sub{color:var(--dim);font-size:12px;margin-bottom:12px}
.nav{display:flex;align-items:center;gap:10px;margin:10px 0;position:sticky;top:0;
background:var(--bg);padding:8px 0;z-index:5}
button{background:var(--panel2);color:var(--ink);border:1px solid var(--line);
border-radius:6px;padding:6px 14px;cursor:pointer;font-size:14px}
button:hover{border-color:var(--gold)}
input[type=range]{flex:1}
.stats{display:flex;gap:16px;flex-wrap:wrap;background:var(--panel);
border:1px solid var(--line);border-radius:8px;padding:10px 14px;margin-bottom:10px}
.stats b{color:var(--gold)}
.grid{display:grid;grid-template-columns:2fr 1fr;gap:12px}
@media(max-width:900px){.grid{grid-template-columns:1fr}}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:8px;
padding:12px;margin-bottom:12px}
.panel h2{font-size:13px;color:var(--dim);margin:0 0 8px;text-transform:none;
letter-spacing:.5px}
.cards{display:flex;flex-wrap:wrap;gap:6px}
.card{background:var(--panel2);border:1px solid var(--line);border-radius:6px;
padding:5px 9px;font-size:13px;white-space:nowrap}
.card.lv1{border-color:#5a89c0}.card.lv2{border-color:#b08ad0}.card.lv3{border-color:var(--gold)}
.slotn{color:var(--dim);font-size:10px;margin-right:4px}
.acts{margin:0;padding-left:18px}.acts li{margin:3px 0}
.acts .hl{color:var(--gold)}
.opp{border-top:1px dashed var(--line);padding-top:8px;margin-top:8px}
.opp:first-of-type{border-top:none;margin-top:0;padding-top:0}
.oppname{font-weight:600}.dead{color:var(--red)}
.battle{border:1px solid var(--line);border-radius:8px;margin-bottom:10px;overflow:hidden}
.battle>summary{cursor:pointer;padding:9px 12px;background:var(--panel2);font-weight:600}
.battle .win{color:var(--green)}.battle .lose{color:var(--red)}
.blog{max-height:480px;overflow:auto;background:#10131a;padding:10px;margin:0;
font:12px/1.45 Consolas,monospace;white-space:pre-wrap}
.fate{background:var(--panel2);border-left:3px solid var(--gold);padding:6px 10px;
border-radius:4px;margin:4px 0;font-size:13px}
.note{color:var(--dim);font-size:12px;font-style:italic}
.stand{display:flex;gap:10px;flex-wrap:wrap}
.stand span{background:var(--panel2);border-radius:6px;padding:4px 10px}
.stand .me{outline:1px solid var(--gold)}
.kbd{color:var(--dim);font-size:11px}
"""

JS = """
const D = __DATA__;
const rounds = Object.keys(D.rounds).map(Number).sort((a,b)=>a-b);
let i = 0;
function lv(name){const m=name.match(/\\+(\\d)$/);return m?Math.min(3,+m[1]+1):1}
function chip(n,idx){return `<span class="card lv${lv(n)}">${idx!=null?`<span class=slotn>${idx+1}</span>`:''}${n}</span>`}
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;')}
function render(){
  const rnd = rounds[i], r = D.rounds[rnd];
  document.getElementById('rlabel').textContent = `Round ${rnd}  (${i+1}/${rounds.length})`;
  document.getElementById('scrub').value = i;
  const myrr = r.rerolls[String(D.pid)];
  document.getElementById('stats').innerHTML =
    `<span>命 <b>${r.destiny}</b></span><span>修为 <b>${r.cult}</b></span>`+
    `<span>境 <b>${r.realm}</b></span>`+(r.hp?`<span>HP <b>${r.hp}</b></span>`:'')+
    `<span>体魄 <b>${r.tipo}</b></span>`+
    (myrr!=null?`<span>换牌存量 <b>${myrr}</b></span>`:'')+
    (r.opp_next?`<span>⚔ 本轮对手 <b>${D.names[r.opp_next.pid]||'pid'+r.opp_next.pid}`+
      `${r.opp_next.ghost?'（ghost — 只有我承担命损）':''}</b></span>`:'')+
    `<span>天命 ${r.talents.length? r.talents.join('、'):'—'}</span>`;
  let h = '';
  h += `<div class=panel><h2>我的场上牌（循环出牌顺序）</h2><div class=cards>`+
       (r.board.length? r.board.map((c,j)=>chip(c,j)).join(''):'<span class=note>（空场）</span>')+`</div></div>`;
  h += `<div class=panel><h2>本回合发牌</h2><div class=cards>`+
       (r.deal.length? r.deal.map(c=>chip(c)).join(''):'<span class=note>—</span>')+`</div></div>`;
  if(r.hand!=null){
    h += `<div class=panel><h2>我的手牌（回合结束时）</h2><div class=cards>`+
         (r.hand.length? r.hand.map(c=>chip(c)).join(''):'<span class=note>（空）</span>')+`</div></div>`;
  }
  if(r.fates.length){
    h += `<div class=panel><h2>天命抉择</h2>`+ r.fates.map(f=>
      `<div class=fate>境${f.realm} 选择 <b>${f.picked}</b> ｜ 备选: ${f.offers.join('、')}</div>`).join('')+`</div>`;
  }
  h += `<div class=panel><h2>行动（${r.secs!=null? r.secs+'s':'—'}）</h2><ol class=acts>`+
       (r.acts.length? r.acts.map(a=>`<li${/BREAKTHROUGH|sidejob/.test(a)?' class=hl':''}>${esc(a)}</li>`).join(''):'<li class=note>（无行动记录）</li>')+`</ol>`+
       (r.notes.length? r.notes.map(n=>`<div class=note>${esc(n)}</div>`).join(''):'')+`</div>`;
  document.getElementById('main').innerHTML = h;
  let o = '';
  for(const [pid,board] of Object.entries(r.opp_seen)){
    const nm = D.names[pid]||('pid'+pid);
    const st = r.standings[pid];
    const dead = r.elim.includes(+pid) || st===0;
    o += `<div class=opp><div class=oppname>${nm} (pid${pid}) `+
         `${dead?'<span class=dead>阵亡</span>':'命 '+ (st!=null?st:'?')}</div>`+
         `<div class=cards>`+(board.length? board.map(c=>chip(c)).join(''):
         '<span class=note>（未知/空）</span>')+`</div></div>`;
  }
  document.getElementById('opps').innerHTML = o;
  let b = '';
  for(const bt of r.battles){
    const meFirst = bt.first==D.pid;
    const won = bt.winner==D.pid;
    const oppPid = bt.first==D.pid? bt.second: bt.first;
    b += `<details class=battle><summary><span class=${won?'win':'lose'}>${won?'胜':'负'}</span>`+
         ` vs ${D.names[oppPid]||'pid'+oppPid} ｜ ${meFirst?'我先手':'对方先手'} ｜ `+
         `败者 -${bt.loss}命${bt.not_applied?'（不结算）':''} ｜ ${bt.turns} 回合`+
         `${bt.extra_for!=null?` ｜ 加赛(仅 pid${bt.extra_for} 承担)`:''}` +
         `</summary><pre class=blog>${esc(bt.log)}</pre></details>`;
  }
  document.getElementById('battles').innerHTML = b || '<span class=note>本回合无战斗</span>';
  let s = '';
  for(const [pid,d] of Object.entries(r.standings)){
    const rr = r.rerolls[pid];
    s += `<span class="${pid==D.pid?'me':''}">${D.names[pid]||'pid'+pid}: ${d}命`+
         `${rr!=null?` · ${rr}换`:''}</span>`;
  }
  document.getElementById('stand').innerHTML = s;
}
function go(d){i=Math.max(0,Math.min(rounds.length-1,i+d));render()}
document.getElementById('prev').onclick=()=>go(-1);
document.getElementById('next').onclick=()=>go(1);
document.getElementById('scrub').oninput=e=>{i=+e.target.value;render()};
document.addEventListener('keydown',e=>{
  if(e.key==='ArrowLeft')go(-1); if(e.key==='ArrowRight')go(1);});
render();
"""

PAGE = """<!doctype html><html lang="zh"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{css}</style></head><body>
<h1>{title}</h1>
<div class="sub">{sub}</div>
<div class="nav">
  <button id="prev">◀</button>
  <b id="rlabel"></b>
  <button id="next">▶</button>
  <input type="range" id="scrub" min="0" max="{maxr}" value="0">
  <span class="kbd">←/→ 换回合</span>
</div>
<div class="stats" id="stats"></div>
<div class="grid">
  <div>
    <div id="main"></div>
    <div class="panel"><h2>本回合战斗（点开看完整 yisim 逐回合日志）</h2>
      <div id="battles"></div></div>
  </div>
  <div>
    <div class="panel"><h2>对手（我能看到的：他们上一回合的场面）</h2>
      <div id="opps"></div></div>
    <div class="panel"><h2>回合结束命数</h2><div class="stand" id="stand"></div></div>
  </div>
</div>
<script>{js}</script></body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", type=int, required=True)
    a = ap.parse_args()
    gdir = _HERE / "games" / f"game{a.game}"
    result = json.loads((gdir / "result.json").read_text(encoding="utf-8"))
    rounds = parse_game(gdir)
    rerolls = track_rerolls(rounds)
    (gdir / "replays").mkdir(exist_ok=True)

    for pid in range(4):
        per = track_states(rounds, pid, rerolls)
        for rnd, r in per.items():
            for b in r["battles"]:
                b["log"] = battle_log(gdir, rnd, b["idx"])
        name = NAMES[pid] or f"pid{pid}"
        data = {"pid": pid, "names": {str(p): NAMES[p] for p in range(4)},
                "rounds": {str(k): v for k, v in per.items()}}
        winner = result["winner_name"]
        sub = (f"Arena game {a.game} · seed {result['seed']} · "
               f"{result['rounds']} rounds · winner {winner} · "
               f"perspective: {name} (pid{pid})")
        pg = PAGE.format(title=f"游戏{a.game}回放 — {name}", sub=sub, css=CSS,
                         maxr=len(per) - 1,
                         js=JS.replace("__DATA__",
                                       json.dumps(data, ensure_ascii=False)))
        out = gdir / "replays" / f"replay_{name}.html"
        out.write_text(pg, encoding="utf-8")
        print(f"wrote {out}  ({out.stat().st_size//1024} KB, "
              f"{len(per)} rounds)")


if __name__ == "__main__":
    main()
