
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
