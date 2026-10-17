
import fs from 'fs';
import { GameState } from "C:/Users/raymo/OneDrive/Desktop/card counter with proxy/vendor/yisim-master/gamestate_full.js";
import { ready as cready } from "C:/Users/raymo/OneDrive/Desktop/card counter with proxy/vendor/yisim-master/card_name_to_id_fuzzy.js";
import parse_input from "C:/Users/raymo/OneDrive/Desktop/card counter with proxy/vendor/yisim-master/parse_input.js";
await cready;
const reqs = JSON.parse(fs.readFileSync(new URL('./_reqs.json', import.meta.url),'utf8'));
const out=[];
for (const req of reqs) {
  try {
    const j = parse_input(JSON.stringify(req));
    const a_first = j.a_first !== false;
    const game = new GameState();
    const [p0,p1] = a_first ? [j.a,j.b] : [j.b,j.a];
    Object.assign(game.players[0], p0);
    Object.assign(game.players[1], p1);
    game.sim_n_turns(64);
    const log = game.output.join('\n');
    let winner=null;
    let m = log.match(/player ([01]) \([^)]*\) wins/);
    if(m) winner = m[1];
    let w = null;
    if (winner!==null){ w = winner==='0' ? (a_first?'a':'b') : (a_first?'b':'a'); }
    out.push({winner:w});
  } catch(e){ out.push({error:''+e}); }
}
fs.writeFileSync(new URL('./_res.json', import.meta.url), JSON.stringify(out));
