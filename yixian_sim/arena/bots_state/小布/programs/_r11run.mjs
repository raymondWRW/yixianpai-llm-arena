
import fs from 'fs';
import { GameState } from "C:/Users/raymo/OneDrive/Desktop/card counter with proxy/vendor/yisim-master/gamestate_full.js";
import { ready as cready } from "C:/Users/raymo/OneDrive/Desktop/card counter with proxy/vendor/yisim-master/card_name_to_id_fuzzy.js";
import parse_input from "C:/Users/raymo/OneDrive/Desktop/card counter with proxy/vendor/yisim-master/parse_input.js";
await cready;
const reqs = JSON.parse(fs.readFileSync(new URL('./_r11reqs.json', import.meta.url),'utf8'));
const out=[];
for (const req of reqs) {
  const reps = req.reps || 1;
  let fw=0, sw=0, ft=0, st=0, n=0;
  for (let k=0;k<reps;k++){
    for (const af of [true,false]) {
      try {
        const j = parse_input(JSON.stringify(req));
        const game = new GameState();
        const [p0,p1] = af ? [j.a,j.b] : [j.b,j.a];
        Object.assign(game.players[0], p0);
        Object.assign(game.players[1], p1);
        game.sim_n_turns(64);
        const log = game.output.join('\n');
        let m = log.match(/player ([01]) \([^)]*\) wins/);
        let w = m ? (m[1]==='0' ? (af?'a':'b') : (af?'b':'a')) : null;
        if (af) { if(w==='a') fw++; ft++; } else { if(w==='a') sw++; st++; }
      } catch(e){}
    }
  }
  out.push({first:fw, firstn:ft, second:sw, secondn:st});
}
fs.writeFileSync(new URL('./_r11res.json', import.meta.url), JSON.stringify(out));
