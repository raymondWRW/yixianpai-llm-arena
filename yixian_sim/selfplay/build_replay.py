# -*- coding: utf-8 -*-
"""Generate a self-contained HTML replay viewer from a selfplay_game.py game.json.

    python selfplay/selfplay_game.py --order --out selfplay/data/game.json
    python selfplay/build_replay.py            # -> selfplay/data/replay.html
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "selfplay" / "data" / "game.json").read_text(encoding="utf-8"))
DATA = json.dumps(data, ensure_ascii=False, separators=(",", ":"))

HTML = r"""<title>弈仙牌 · 自弈 — AI self-play replay</title>
<style>
:root{
  --ground:#0c0f16; --panel:#131926; --panel2:#1a2130; --line:#28303f;
  --text:#e9e3d5; --muted:#8b93a3; --faint:#5c6577;
  --jade:#57b28c; --gold:#cBa a; --gold:#c9a85c; --cinnabar:#d1503f;
  --s1:#6ea8d8; --s2:#5cbd9a; --s3:#d9825f; --s4:#a98bd8;
  --bar-track:#222a38; --champ:#c9a85c;
  --shadow:0 8px 30px rgba(0,0,0,.45);
}
@media (prefers-color-scheme:light){
  :root{
    --ground:#efe9db; --panel:#f6f1e6; --panel2:#efe8d8; --line:#d8cfbb;
    --text:#241f16; --muted:#6b6553; --faint:#9a927e;
    --jade:#2f8a68; --gold:#9c7a2e; --cinnabar:#b23d2c;
    --s1:#3d6fa3; --s2:#2f8a68; --s3:#b25f3a; --s4:#7a5bb0;
    --bar-track:#e0d8c4; --champ:#9c7a2e; --shadow:0 8px 24px rgba(60,50,30,.15);
  }
}
:root[data-theme="dark"]{
  --ground:#0c0f16; --panel:#131926; --panel2:#1a2130; --line:#28303f;
  --text:#e9e3d5; --muted:#8b93a3; --faint:#5c6577;
  --jade:#57b28c; --gold:#c9a85c; --cinnabar:#d1503f;
  --s1:#6ea8d8; --s2:#5cbd9a; --s3:#d9825f; --s4:#a98bd8;
  --bar-track:#222a38; --champ:#c9a85c; --shadow:0 8px 30px rgba(0,0,0,.45);
}
:root[data-theme="light"]{
  --ground:#efe9db; --panel:#f6f1e6; --panel2:#efe8d8; --line:#d8cfbb;
  --text:#241f16; --muted:#6b6553; --faint:#9a927e;
  --jade:#2f8a68; --gold:#9c7a2e; --cinnabar:#b23d2c;
  --s1:#3d6fa3; --s2:#2f8a68; --s3:#b25f3a; --s4:#7a5bb0;
  --bar-track:#e0d8c4; --champ:#9c7a2e; --shadow:0 8px 24px rgba(60,50,30,.15);
}
*{box-sizing:border-box}
html,body{margin:0}
body{
  background:
    radial-gradient(1200px 600px at 70% -10%, color-mix(in srgb,var(--jade) 8%,transparent), transparent 60%),
    radial-gradient(900px 500px at 10% 110%, color-mix(in srgb,var(--gold) 7%,transparent), transparent 55%),
    var(--ground);
  color:var(--text);
  font-family:"Songti SC","Noto Serif SC","STSong",Georgia,"Times New Roman",serif;
  line-height:1.5; -webkit-font-smoothing:antialiased; min-height:100vh;
}
.mono{font-family:ui-monospace,"SF Mono","Cascadia Code",Consolas,monospace;font-variant-numeric:tabular-nums}
.wrap{max-width:1080px;margin:0 auto;padding:32px 22px 80px}

/* header */
.masthead{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;flex-wrap:wrap;
  border-bottom:1px solid var(--line);padding-bottom:18px}
.title{font-size:clamp(28px,5vw,44px);font-weight:600;letter-spacing:.06em;margin:0;text-wrap:balance}
.title .dot{color:var(--jade)}
.sub{color:var(--muted);font-size:14px;margin-top:6px;letter-spacing:.02em}
.sub .mono{color:var(--gold)}

/* roster */
.roster{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 6px}
.chip-ch{display:flex;align-items:center;gap:7px;padding:5px 11px 5px 8px;border:1px solid var(--line);
  border-radius:999px;background:var(--panel);font-size:14px}
.pip{width:9px;height:9px;border-radius:50%;box-shadow:0 0 0 3px color-mix(in srgb,currentColor 22%,transparent)}
.chip-ch.champ{border-color:color-mix(in srgb,var(--champ) 60%,var(--line));
  box-shadow:0 0 0 1px color-mix(in srgb,var(--champ) 40%,transparent) inset}
.chip-ch .crown{color:var(--champ);font-size:12px}
.chip-ch .job{color:var(--faint);font-size:11px;font-family:ui-monospace,monospace;
  padding-left:5px;border-left:1px solid var(--line)}

/* controls */
.controls{display:flex;align-items:center;gap:14px;margin:26px 0 20px;flex-wrap:wrap}
.btn{font-family:inherit;font-size:15px;color:var(--text);background:var(--panel);border:1px solid var(--line);
  border-radius:10px;padding:9px 15px;cursor:pointer;transition:border-color .15s,background .15s}
.btn:hover{border-color:var(--jade)}
.btn:focus-visible{outline:2px solid var(--jade);outline-offset:2px}
.btn.play{min-width:88px}
.round-badge{font-family:ui-monospace,monospace;font-variant-numeric:tabular-nums;font-size:15px;
  color:var(--muted);letter-spacing:.04em}
.round-badge b{color:var(--text);font-size:22px;font-weight:600}
.scrub{flex:1;min-width:180px;accent-color:var(--jade);height:4px}
.slots{color:var(--faint);font-size:13px;letter-spacing:.04em}

/* layout grid */
.stage{display:grid;grid-template-columns:1.55fr 1fr;gap:22px;align-items:start}
@media(max-width:820px){.stage{grid-template-columns:1fr}}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;box-shadow:var(--shadow)}
.eyebrow{font-family:ui-monospace,monospace;font-size:11px;letter-spacing:.22em;text-transform:uppercase;
  color:var(--faint);padding:14px 18px 0}

/* duels */
.duels{display:flex;flex-direction:column;gap:14px;padding:10px 16px 18px}
.duel{border:1px solid var(--line);border-radius:12px;background:var(--panel2);overflow:hidden}
.duel-head{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:10px;padding:11px 14px;
  border-bottom:1px solid var(--line)}
.who{display:flex;align-items:center;gap:8px;font-size:16px}
.who.right{justify-content:flex-end}
.who .nm{font-weight:600}
.who.win .nm{color:var(--jade)}
.verdict{font-family:ui-monospace,monospace;font-size:12px;text-align:center;color:var(--muted);
  white-space:nowrap;line-height:1.3}
.verdict .loss{color:var(--cinnabar);font-weight:600}
.verdict .draw{color:var(--faint)}
.boards{display:grid;grid-template-columns:1fr 1fr;gap:0}
.side{padding:11px 14px;display:flex;flex-direction:column;gap:8px}
.side.left{border-right:1px solid var(--line)}
.statline{display:flex;gap:11px;font-family:ui-monospace,monospace;font-size:11px;
  color:var(--muted);font-variant-numeric:tabular-nums;letter-spacing:.02em}
.side.right .statline{justify-content:flex-end}
.statline .hp{color:var(--cinnabar)}
.statline .ti{color:var(--jade)}
.cards{display:flex;flex-wrap:wrap;gap:6px}
.side.right .cards{justify-content:flex-end}
.gd{display:inline-flex;align-items:center;gap:4px;padding:3px 8px;border-radius:7px;font-size:13px;
  background:color-mix(in srgb,var(--panel) 70%,var(--ground));border:1px solid var(--line);color:var(--text)}
.gd.m{border-color:color-mix(in srgb,var(--gold) 55%,var(--line));
  background:color-mix(in srgb,var(--gold) 12%,var(--panel));box-shadow:0 0 0 1px color-mix(in srgb,var(--gold) 20%,transparent) inset}
.gd .lv{font-family:ui-monospace,monospace;font-size:10px;color:var(--gold);font-weight:700}

/* ledger */
.ledger{padding:8px 16px 16px}
.row{display:grid;grid-template-columns:96px 1fr auto;align-items:center;gap:10px;padding:7px 2px}
.row .nm{display:flex;align-items:center;gap:7px;font-size:15px;white-space:nowrap}
.row.dead{opacity:.42}
.row.dead .nm .txt{text-decoration:line-through}
.row.champ .nm .txt{color:var(--champ)}
.track{position:relative;height:9px;background:var(--bar-track);border-radius:6px;overflow:hidden}
.fill{position:absolute;inset:0 auto 0 0;border-radius:6px;transition:width .5s cubic-bezier(.4,.7,.3,1),background .3s}
.stat{font-family:ui-monospace,monospace;font-variant-numeric:tabular-nums;font-size:13px;color:var(--muted);
  display:flex;gap:9px;align-items:baseline}
.stat .hp{color:var(--text);font-size:15px;min-width:30px;text-align:right}
.realm{color:var(--gold);font-size:12px}

/* podium */
.podium{margin-top:26px;display:none;grid-template-columns:1fr 1.15fr 1fr;gap:14px;align-items:end}
.podium.show{display:grid}
.pod{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px 14px;text-align:center;box-shadow:var(--shadow)}
.pod .rk{font-family:ui-monospace,monospace;font-size:12px;letter-spacing:.2em;color:var(--faint)}
.pod .pn{font-size:22px;font-weight:600;margin:6px 0 2px}
.pod .pd{font-family:ui-monospace,monospace;color:var(--muted);font-size:13px}
.pod.first{border-color:color-mix(in srgb,var(--champ) 55%,var(--line));padding-bottom:30px;
  background:linear-gradient(180deg,color-mix(in srgb,var(--champ) 12%,var(--panel)),var(--panel))}
.pod.first .pn{color:var(--champ)}
.pod.first .rk{color:var(--champ)}
.foot{margin-top:34px;color:var(--faint);font-size:12.5px;line-height:1.7;border-top:1px solid var(--line);padding-top:16px}
.foot b{color:var(--muted);font-weight:600}
@media(prefers-reduced-motion:reduce){.fill{transition:none}}
</style>

<div class="wrap">
  <header class="masthead">
    <div>
      <h1 class="title">弈仙牌<span class="dot"> · </span>自弈</h1>
      <div class="sub">An offline AI playing itself — <span class="mono" id="nplayers">8</span> cultivators,
        one destiny pool each, last one standing. Board search + merges + rerolls + card-ordering, exact combat.</div>
    </div>
    <div class="round-badge">回合 <b id="rnum">1</b> <span id="rtot"></span></div>
  </header>

  <div class="roster" id="roster"></div>

  <div class="controls">
    <button class="btn" id="prev" aria-label="previous round">◀ 前</button>
    <button class="btn play" id="play" aria-label="auto play">▶ 自动</button>
    <button class="btn" id="next" aria-label="next round">后 ▶</button>
    <input class="scrub" id="scrub" type="range" min="0" value="0" aria-label="round scrubber">
    <span class="slots" id="slots"></span>
  </div>

  <div class="stage">
    <section class="card">
      <div class="eyebrow">斗法 · duels this round</div>
      <div class="duels" id="duels"></div>
    </section>
    <aside class="card">
      <div class="eyebrow">命 · destiny standings</div>
      <div class="ledger" id="ledger"></div>
    </aside>
  </div>

  <div class="podium" id="podium"></div>

  <div class="card" id="fatespanel" style="margin-top:26px;padding:16px 18px 20px">
    <div class="eyebrow" style="padding:0 0 12px">天命 · the fates each AI chose</div>
    <div id="fates" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px"></div>
  </div>

  <div class="foot">
    <b>How to read it.</b> Each round every living cultivator is paired at random and their boards fight in the game's
    exact combat engine; the loser's 命 (destiny) falls by the margin. Reach 命 0 and you're out. Each side shows
    <b>♥ HP</b> / <b>修 cultivation</b> / <b>体 physique</b> going into the fight. 境N is the realm; gold-ringed cards are
    <b>merged</b> (two copies leveled up). Hover a name in the roster for their <b>天命 fates</b>. Winner is decided by
    survival, then destiny.
  </div>
</div>

<script>
const GAME = __DATA__;
const CH = GAME.characters, R = GAME.rounds, PLACE = GAME.placement;
const SECT = {1:'var(--s1)',2:'var(--s2)',3:'var(--s3)',4:'var(--s4)'};
const champPid = PLACE[0].pid;
const byPid = p => CH.find(c=>c.pid===p);

// parse "天谕·守·2" -> {base:"天谕·守", lv:2}
function parseCard(s){
  const i = s.lastIndexOf('·');
  if(i>0){ const tail=s.slice(i+1); if(/^\d+$/.test(tail)){ const lv=+tail; if(lv>1) return {base:s.slice(0,i),lv}; } }
  return {base:s,lv:1};
}
function gd(name){
  const {base,lv}=parseCard(name);
  const m = lv>1?' m':'';
  return `<span class="gd${m}">${base}${lv>1?`<span class="lv">·${lv}</span>`:''}</span>`;
}
function statline(hp,cult,tipo,hand,rolls){
  return `<div class="statline"><span class="hp">♥ ${hp}</span><span>修 ${cult}</span>`+
    `${tipo?`<span class="ti">体 ${tipo}</span>`:''}`+
    `${hand!=null?`<span>手牌 ${hand}</span>`:''}`+
    `${rolls!=null?`<span>换 ${rolls}</span>`:''}</div>`;
}

// roster
document.getElementById('nplayers').textContent = CH.length;
document.getElementById('roster').innerHTML = CH.map(c=>{
  const champ = c.pid===champPid?' champ':'';
  const fates = (c.fates||[]).join(' · ');
  return `<span class="chip-ch${champ}" title="${fates?'天命: '+fates:''}"><span class="pip" style="color:${SECT[c.sect]}"></span>`+
    `<span>${c.name}</span>${c.sidejob&&c.sidejob!=='—'?`<span class="job">${c.sidejob}</span>`:''}`+
    `${c.pid===champPid?'<span class="crown">☗ 魁</span>':''}</span>`;
}).join('');

// 天命 panel — each character's innate + the fates the AI chose at breakthroughs
document.getElementById('fates').innerHTML = CH.map(c=>{
  const champ = c.pid===champPid;
  const chosen = (c.chosen_fates||c.fates||[]);
  const chips = chosen.length
    ? chosen.map((f,i)=>`${i?'<span style="color:var(--faint);margin:0 5px">→</span>':''}`+
        `<span style="display:inline-block;padding:2px 8px;border:1px solid var(--line);border-radius:6px;`+
        `background:var(--panel2);font-size:13px;margin:2px 0">${f}</span>`).join('')
    : `<span style="color:var(--faint);font-size:13px">—</span>`;
  return `<div style="border:1px solid ${champ?'color-mix(in srgb,var(--champ) 55%,var(--line))':'var(--line)'};`+
    `border-radius:12px;padding:12px 14px;background:var(--panel2)">`+
    `<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px">`+
    `<span class="pip" style="color:${SECT[c.sect]}"></span>`+
    `<span style="font-weight:600;font-size:15px">${c.name}</span>`+
    (champ?'<span style="color:var(--champ);font-size:12px">☗ 魁</span>':'')+
    `<span style="margin-left:auto;font-family:ui-monospace,monospace;font-size:11px;color:var(--faint)">`+
    `${c.sidejob&&c.sidejob!=='—'?'副职 '+c.sidejob:''}</span></div>`+
    (c.innate?`<div style="font-size:11px;color:var(--muted);margin-bottom:7px">`+
      `<span style="font-family:ui-monospace,monospace">innate</span> ${c.innate}</div>`:'')+
    `<div style="line-height:1.9">${chips}</div></div>`;
}).join('');

const rtot=R.length;
document.getElementById('rtot').textContent = '/ '+rtot;
const scrub=document.getElementById('scrub'); scrub.max=rtot-1;

function nm(pid,win,right){
  const c=byPid(pid);
  return `<span class="who${right?' right':''}${win?' win':''}">`+
    (right?'':`<span class="pip" style="color:${SECT[c.sect]}"></span>`)+
    `<span class="nm txt">${c.name}</span>`+
    (right?`<span class="pip" style="color:${SECT[c.sect]}"></span>`:'')+`</span>`;
}

function render(i){
  const rd=R[i];
  document.getElementById('rnum').textContent = rd.round;
  document.getElementById('slots').textContent = '棋盘 '+ (Math.min(8, rd.round+2)) +' 格';
  scrub.value=i;
  // duels
  document.getElementById('duels').innerHTML = rd.battles.map(b=>{
    const aw=(b.a_won!==undefined)?b.a_won:b.margin>0.5, bw=!aw;
    const loser = aw?byPid(b.b).name:byPid(b.a).name;
    const amt = Math.round(Math.abs(b.margin));
    const verdict = `${aw?byPid(b.a).name:byPid(b.b).name} 胜<br><span class="loss">${loser} 命 −${amt}</span>`;
    return `<div class="duel"><div class="duel-head">
        ${nm(b.a,aw,false)}<div class="verdict">${verdict}</div>${nm(b.b,bw,true)}
      </div><div class="boards">
        <div class="side left">${statline(b.a_hp,b.a_cult,b.a_tipo,b.a_hand,b.a_rolls)}
          <div class="cards">${b.a_board.map(gd).join('')}</div></div>
        <div class="side right">${statline(b.b_hp,b.b_cult,b.b_tipo,b.b_hand,b.b_rolls)}
          <div class="cards">${b.b_board.map(gd).join('')}</div></div>
      </div></div>`;
  }).join('');
  // ledger (standings already sorted desc by destiny)
  document.getElementById('ledger').innerHTML = rd.standings.map(s=>{
    const c=byPid(s.pid), dead=!s.alive, champ=s.pid===champPid;
    const w=Math.max(0,Math.min(100,s.destiny));
    const col = dead?'var(--faint)':(s.destiny<25?'var(--cinnabar)':(champ?'var(--champ)':'var(--jade)'));
    return `<div class="row${dead?' dead':''}${champ?' champ':''}">
      <div class="nm"><span class="pip" style="color:${SECT[c.sect]}"></span><span class="txt">${c.name}</span></div>
      <div class="track"><div class="fill" style="width:${w}%;background:${col}"></div></div>
      <div class="stat"><span class="realm">境${s.realm}</span><span class="hp">${s.destiny}</span></div>
    </div>`;
  }).join('');
  // podium on final round
  const pod=document.getElementById('podium');
  if(i===rtot-1){
    const order=[1,0,2]; // silver, gold(center), bronze
    pod.className='podium show';
    pod.innerHTML=order.map(k=>{
      const p=PLACE[k]; const first=k===0;
      return `<div class="pod${first?' first':''}"><div class="rk">${['— 魁 —','第二','第三'][k]}</div>
        <div class="pn">${p.name}</div><div class="pd">境${p.realm} · 命 ${p.destiny}</div></div>`;
    }).join('');
  } else { pod.className='podium'; pod.innerHTML=''; }
}

let cur=0, timer=null;
function go(i){ cur=Math.max(0,Math.min(rtot-1,i)); render(cur); }
document.getElementById('prev').onclick=()=>{stop();go(cur-1)};
document.getElementById('next').onclick=()=>{stop();go(cur+1)};
scrub.oninput=e=>{stop();go(+e.target.value)};
const playBtn=document.getElementById('play');
function stop(){ if(timer){clearInterval(timer);timer=null;playBtn.textContent='▶ 自动'} }
playBtn.onclick=()=>{
  if(timer){stop();return}
  if(cur>=rtot-1) go(0);
  playBtn.textContent='❚❚ 暂停';
  timer=setInterval(()=>{ if(cur>=rtot-1){stop();return} go(cur+1); },1600);
};
window.addEventListener('keydown',e=>{
  if(e.key==='ArrowLeft'){stop();go(cur-1)} else if(e.key==='ArrowRight'){stop();go(cur+1)}
  else if(e.key===' '){e.preventDefault();playBtn.click()}
});
render(0);
</script>
"""

out = ROOT / "selfplay" / "data" / "replay.html"
out.write_text(HTML.replace("__DATA__", DATA), encoding="utf-8")
print("wrote", out, out.stat().st_size, "bytes")
