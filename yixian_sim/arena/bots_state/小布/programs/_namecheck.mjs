
import fs from 'fs';
import { card_name_to_id_fuzzy, ready } from "C:/Users/raymo/OneDrive/Desktop/card counter with proxy/vendor/yisim-master/card_name_to_id_fuzzy.js";
await ready;
const names = JSON.parse(fs.readFileSync(new URL('./_names.json', import.meta.url), 'utf8'));
let out=[];
for (const n of names) { try { out.push([n, card_name_to_id_fuzzy(n)]); } catch(e){ out.push([n, "ERR:"+e]); } }
fs.writeFileSync(new URL('./_names_out.json', import.meta.url), JSON.stringify(out, null, 1));
