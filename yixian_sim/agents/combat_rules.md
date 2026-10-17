# 弈仙牌 combat rules — hand-tracing reference

Extracted by reading `vendor/yisim-master` (sharpobject/yisim), the open-source JS
combat simulator. **No battles were run**; every rule below is cited to the file and
function it came from. Citations of the form `gs:NNNN` mean
`vendor/yisim-master/gamestate_full.js` line NNNN (the readable full engine —
`gamestate.js` is a stripped variant missing 剑意/无视防御/护体 entirely, do not use it).

yisim tracks the live game with a lag. Section 9 lists the places where it is
known or likely to be wrong. Where the code is ambiguous I say so rather than guess.

---

## 0. How to trace

Keep one row per **turn** (= one player's action window), alternating sides:

```
turn | side | slot/card        | qi in→out | 剑意 | 防 before→after | dmg to 防 / to HP | HP after
1a   | me   | [1] 剑劈+2       | 0 → 0     | 2→4  | 0 → 0           | 0 / 8             | them 92
1b   | them | [1] 地灵丹       | 0 → 0     | –    | 0 → 11          | –                 | –
```

Columns you must not omit: **qi** (a shortfall costs you the whole turn),
**剑意 bank** (it is spent at *end of card*, not at the attack), and **防 at the moment
of the hit** (it decays at the start of its owner's turn, not yours).

---

## 1. The battle loop

### 1.1 Turn order and what a "turn" is

`gs:1548 sim_n_turns(n)`

```
start_of_game_setup()
for i = 0,1,2,…,n-1:
    if i is odd: swap players
    sim_turn()            # exactly ONE player acts
    if i is odd: swap back
    if game_over: break
```

* A **turn** is one player's action window. Turn `i` is labelled `⌊i/2⌋+1` plus `a`/`b`
  (`gs:1545 turn_label`), so turns `1a, 1b, 2a, 2b, …`. A "round" = one `a` + one `b`.
* **Player `a` always acts first.** yisim does **not** compute who goes first — it is
  the input field `a first:` and `example_with_comments.yaml` says literally
  `# TODO implement speed comparison`. The live rule (higher 修为 first, ties random) is
  *not in this codebase*; take it from the strategy doc, not from here.
* **Turn cap**: `just_run.js` calls `sim_n_turns(64)` → 64 turns = 32 rounds = 32 plays
  per side. Real battles end far sooner. If the cap is reached, the winner is simply
  **whoever has more HP** (`gs:1573`); ties go to player 0 (`hp < hp` test).
* **Death**: checked at several points inside a turn (`gs:5143 check_for_death`) —
  start of turn after 内伤, before each action, and after each card resolves. Death is
  `hp <= 0` for either side. It is **not** checked mid-card, so a multi-hit card
  always resolves all of its hits.

### 1.2 The 8 slots and the cursor

* Board is up to **8 slots**, played in a **cycle**: after slot 8 the cursor wraps to
  slot 1 (`gs:917 get_next_playable_idx`, modulo `cards.length`). It wraps at the
  *deck length*, not at 8 — a 5-card board cycles 1→2→3→4→5→1.
* `card_play_direction` is normally `+1`; a few cards reverse it (`gs:2646 get_prev_idx`).
* **Empty slots**: yisim's parser pads the board to `deck_slots` (default 8) with
  `normal attack` (`parse_input.js`). 普通攻击 = card `601011` = **3攻** at lv1
  (lv2 = 6攻, lv3 = 9攻). So an empty slot **is a turn spent making a 3-damage attack**,
  not a skip. *(Ambiguity: the live game's 普通攻击 base row in
  `localization/1.5.9/combined_cards.json` is level 2 = 6攻. yisim uses lv1/3攻 for
  padding. The strategy doc's own observation is 3攻; I keep 3攻 but flag it.)*
* **When every slot is locked** (all 消耗/持续 spent), `get_next_playable_idx` gives up
  after one full lap and **overwrites the current slot with 普通攻击 and re-enables it**
  (`gs:926-929`). From then on you attack for 3 every turn.

### 1.3 Paying for a card — the "spend the turn gaining 1 qi" rule

`gs:3430-3500` (inside `sim_turn`)

Order per action:

1. Read `card.qi_cost`, then apply cost reducers (`decrease_qi_cost_by_x`,
   e.g. 御空剑阵 reduces its 1-qi cost by your current 防, so it is free whenever 防 ≥ 1).
2. If `qi < qi_cost` → **`gain_qi_to_afford_card()` (`gs:2666`) gives +1 qi and the turn
   ENDS.** The cursor does **not** advance; you retry the same card next turn.
   *This is the single most important tempo rule.* It is also a usable stall: a board
   that can't pay is a board with a free extra "virtual card".
3. Otherwise spend the qi, then spend `hp_cost` if any (HP cost is paid as `is_cost=true`,
   so it **bypasses 护体 and 防** — `gs:3660 reduce_idx_hp`), then play the card.
4. After the card resolves: `advance_next_card_index()` (unless a card suppressed it),
   then chases are processed.

Note there is **no** "not enough HP" branch — an HP cost can kill you; that's a legal
line the engine allows.

### 1.4 Chase / extra action — `[再次行动]`

* `chase()` (`gs:4924`) increments `this_card_chases`.
* At end of card, `process_this_card_chases()` (`gs:2534`) converts **any number of
  chases on one card into at most +1** to `me.chases`, and only while
  `chases < max_chases`. **`max_chases` defaults to 1** (`gs:161`).
* Loop guard: `while (action_idx <= chases && action_idx <= max_chases && can_act)`
  (`gs:3394`). **Result: at most 2 cards per turn**, no matter how many chase triggers
  fire. Only 龙-type effects raise `max_chases`.
* `[困缚]` entangle **eats a chase**: if you would chase and `entangle > 0`, you lose 1
  entangle instead of chasing (`gs:2555`).
* `[身法]` agility ≥ 10 buys a chase on a card that didn't otherwise chase, spending 10
  (`gs:2545`). There is no `[闪避]` keyword in this game.

### 1.5 `[消耗]`, `[持续]`, `[跳至]`, `[跳过]`, `[开局]`, `[后招]`

| keyword | code | effect |
|---|---|---|
| `[消耗]` consume | `consumption()` `gs:4946` | sets `can_play[slot] = false` — the slot is **skipped for the rest of the battle**. Only fires at `trigger_depth === 1` (i.e. not when the card is retriggered by another card). |
| `[持续]` continuous | `continuous()` `gs:4940` | identical slot-locking, plus sets `has_played_continuous_card`. The lasting effect lives in a stack counter, not in the slot. |
| `[跳过]` skip | `skip_one_play[idx]` `gs:3301` | the cursor passes over the slot once. |
| `[跳至]` jump-to | `astral_move_jump_stacks` `gs:3275`, `skip_to_previous_card_stacks` `gs:3263` | rare (玄冥重现, 星弈•跳, 天命·重现). Jump-to-next scans forward up to N playable slots for a matching card and **fires the `[开局]` of every slot it passes**. |
| `[开局]` opening | `do_opening` `gs:1421` | runs once per slot during `start_of_game_setup`, **before turn 1a**, for both players. |
| `[后招]` post-action | `if_post_action` `gs:5521` | true only if `can_post_action[slot]`, which is set after the slot's **first** play (`gs:2594`). So a `[后招]` rider does nothing on the first cycle and fires from the second cycle on. |

The `limit consumption: yes` option is a **deck-search constraint in `enqueue.js:42`**,
not a combat rule.

### 1.6 What happens inside one `sim_turn`, in order

`gs:3315`. The load-bearing steps for a hand trace:

1. `chases = 0`; per-turn flags reset; several 1-turn buff counters tick down
   (`metal_spirit_iron_bone`, `water_spirit_dive`, `counter_move`, …).
2. **`do_def_decay()`** — 防 loses `ceil(防 × 50 / 100)` (`gs:2703`, `gs:4854`).
   `moon_water_sword_formation_stacks > 0` sets decay to **0** and spends one stack;
   黑地龟 sets it to 20%.
3. `do_next_turn_def()` — banked `next_turn_def` is added **after** the halving.
4. Assorted start-of-turn generators: 聚灵心法 qi, 剑意 from 剑心心法, 恢复 heal
   (`do_regen`, `gs:2760`), …
5. **`do_internal_injury(0, true)`** — lose `内伤` HP. Then death check.
6. **Action loop** (1 card, +1 more if chased).
7. End-of-turn: formation/tune upkeep, then **`weaken(虚弱) −1, flaw(破绽) −1,
   entangle(困缚) −1`** and a handful of others (`gs:3620-3636`).
   **`内伤`, `外伤`, `减攻`, `加攻`, `恢复` do NOT decay** — they last the whole battle.

---

## 2. The damage pipeline

`gs:4776 atk(dmg, is_extra, smash)` → `gs:4409 deal_damage_inner`. Order is exact.

### 2.1 Before the numbers

`atk()` first fires on-attack side effects (`gs:4776-4795`): 飘冰刃, 撒花瓣 → 内伤,
attack counter, 火焰刃.

### 2.2 Additive stage (all `+` before any `×`)

Starting from the card's printed ATK:

1. **Mark 剑意 for exhaustion**: if `sword_intent > 0` and not `ignore_sword_intent`,
   set `sword_intent_to_lose = max(sword_intent_to_lose, sword_intent)` (`gs:4433-4438`).
   **Nothing is spent yet.**
2. `+ star_power` if this slot is a `[星位]`.
3. 碎防 / 无视防御 flags are claimed here: `ignore_def > 0` → spend 1 stack, set the
   ignore flag for **this one attack** (`gs:4456`).
4. `+` a pile of conditional flat bonuses: 孤夜狼, 炼骨, 星空铸骨, 万事随缘, 不屈意志,
   **`bonus_atk_amt`** (the card's own "每有1点X多1攻" term, e.g. 镜花剑阵, 万法归灵剑).
5. `+ next_attack_deals_extra`.
6. **`+ sword_intent`** (`gs:4490-4493`) — the whole current bank, **on every hit**.
7. `+ increase_atk` (`[加攻]`).
8. `+ craze_dance_tune_stacks`, 夺天机 transfers, …
9. `force` (`[气势]`): **1 stack of 气势 is spent per attack** (`reduce_c_of_x(1,"force")`)
   and each remaining point gives **+10% multiplier** (not flat), unless 梦-聚势 makes it flat.
10. `− decrease_atk` (`[减攻]`), then **clamp to ≥ 1**.
11. `− 5` per 金灵·铁骨 on the defender, clamp ≥ 1.

### 2.3 Multiplicative stage

`pct_multiplier` starts at 100 and accumulates additively-in-percent:

| source | Δ |
|---|---|
| `force` (see above) | +10 per point |
| defender has 水灵·潜 | −40 |
| attacker `虚弱 > 0` | −40 |
| defender `破绽 > 0` | +40 |
| 雷法心法 on a 雷 card | + stacks |
| 沉气 | +10 × your qi |
| defender 逆转式 in 拳架 | −50 |
| 梦-击退心法 | −25 (and reflects 25% back) |

Then **`dmg = floor(dmg × pct / 100)`, then `dmg = max(min_dmg, dmg)`** with
`min_dmg = 1` for attacks (`gs:4642-4644`). Damage from non-attack sources
(`deal_damage`, e.g. 断崖 reflection) has `min_dmg = 0` and **skips the entire
attack-only section above** — no 剑意, no 加攻, no 无视防御.

### 2.4 防 absorption

`gs:4667-4683`, three mutually exclusive branches:

* **`ignore_def` (`[无视防御]`)** → `damage_to_def = 0`, all of it goes to HP.
* **`smash_def` (`[碎防]`)** → 防 absorbs at double rate: it eats
  `min(floor(防/2), dmg)` points of your damage but loses twice that (plus 1 if 防 was
  odd and fully consumed). Remaining damage goes to HP.
* **normal** → `damage_to_def = min(防, dmg)`, remainder to HP.

### 2.5 HP stage

`gs:4686-4715`:

* `can_wound` (`[击伤]`) is true iff **damage_to_hp > 0** AND the defender has no
  `护体` (guard_up) AND no 匿形. Forced true by 火焰刃 / 梦-灵气灌注.
* If `can_wound`: `+ 锋锐 (penetrate)` is added to HP damage and **fully spent**;
  `+ 外伤 (wound)` of the defender is added.
* `护体` (`[护体]`) at `reduce_idx_hp` (`gs:3660`): spends 1 stack and **negates the
  entire HP hit** — regardless of size. It does *not* stop 防 from being chewed, and it
  does *not* stop HP paid as a card cost.
* HP can go negative; death is `hp <= 0` at the next `check_for_death`.

### 2.6 When 剑意 is actually spent — the exact rule

Two places:

* `deal_damage_inner` only **records** `sword_intent_to_lose = max(so far, current
  sword_intent)` (`gs:4436`).
* `do_sword_intent_end_of_card()` (`gs:4838`) runs **at the end of `trigger_card`**,
  i.e. after the card's *entire* action list including all appended extra attacks, and
  subtracts `sword_intent_to_lose`, then adds `sword_intent_to_regain`.
  `sword_intent_to_lose` is then reset to 0 (`gs:2515`).

Consequences a hand-tracer must get right:

* **Every hit of a multi-hit card gets the full bank; the bank is paid once.**
  灵猫乱剑 lv3 with 3 held cards = 7 hits, each at `2 + 剑意`.
* A card that **grants** 剑意 after attacking (剑劈: `atk 6` then `剑意 +4`) attacks with
  the *old* bank, then banks 4, then loses only the *old* amount. Net: bank keeps the +4.
* A card that **never attacks** (剑挡, 凝意诀, 云舞诀, 剑意激荡) loses nothing.
* An **appended extra attack** (无尽剑阵, 虚空剑阵, 剑气) re-runs the max: if the card
  raised your bank in between, `sword_intent_to_lose` is re-set to the *new, higher*
  bank and you end at 0 (`notes.txt` confirms exactly this for 剑劈).
* **飞牙剑 (Flying Fang Sword)** is *not* "does not consume". Its text is
  `8攻 / [击伤]：返还此牌攻击用的[剑意]`, implemented as
  `regain_sword_intent()` → `sword_intent_to_regain += sword_intent_to_lose` (`gs:4834`),
  so at end of card the loss and the refund cancel **exactly**.
  **The refund is gated on `[击伤]`.** If the hit is fully absorbed by the opponent's 防,
  `if_injured()` is false, there is no refund, and **your whole bank is gone.**
  This is the classic "fed my intent into a block turn" loss. Per `notes.txt`, an
  appended extra attack after 飞牙剑 also does not consume (the refund already covers the
  same max).

### 2.7 防 across turns

* 防 persists between turns and only decays at **the start of its owner's turn**, by
  `ceil(防/2)` (odd values round the loss *up*: 11 → 5, 13 → 6, 7 → 3).
* `next_turn_def` (土灵·群山 etc.) is granted **after** the decay, so it arrives at full value.
* 水月剑阵 sets that turn's decay to 0 and spends a stack. 剑阵守护 (fate) grants
  1 stack of the same effect every time slot 1 is played (`gs:1972`).
* 防 gain passes through `increase_idx_def` (`gs:3913`) — it can be blocked
  (`prevent_gain_def`) or amplified (锟铻金环 +1 flat per stack, 神机·顺 ×1.4 rounded up).

---

## 3. Resources

### 灵气 qi
* Starts at **0** (`gs:reset`). **No cap** in the code, no per-turn passive gain.
* Sources: card text `[灵气]+N`, and the **default action**: failing to afford a card
  gives **+1 qi** and burns the turn (`gs:2666`; 休心养神 makes it +3 qi +3 卦象 instead).
* Spent only as card costs. `sword_qi` (剑气 resource) can top up a shortfall before the
  default action triggers (`gs:3490`).

### 剑意 sword intent
* Starts at 0 unless a fate grants it. **No cap found anywhere in the engine.**
* Gained by card text; multiplied by 剑意激荡 (`for_each_x_add_c_pct_y`, **floor**):
  lv1 +80%, lv2 +110%, lv3 +140% of the current bank.
* Adds **+1 ATK per point, to every attack**, and is exhausted per §2.6.
* 剑意流 (`sword_intent_flow_stacks`) spends a stack instead of the bank (`gs:4841`).

### HP / max HP
* Both are plain mutable numbers. Healing is capped at `max_hp` (`gs:3870`) unless
  生机勃发 raises the cap by the overflow.
* max HP can move mid-battle (养魂玉莲, 水灵·腾浪, 无相体 costs). Lowering max HP below
  current HP clamps HP down (`gs:3705`).
* `[恢复]` regen heals at the start of every one of your turns and **never expires**.
* `[内伤]` internal injury deals its stack count in HP at the start of every one of your
  turns and **never expires**. `[外伤]` wound adds itself to every incoming `[击伤]`.

### 命元 destiny — **NOT a battle resource**
Destiny is computed **after** the battle ends, from the HP gap
(`gs:1618 calculate_destiny_damage`):

```
hp_delta = winner.hp − loser.hp
if hp_delta ≤ 20:  dmg = round + 1 + ceil(hp_delta/5)
else:              dmg = round + 5 + min( ceil((hp_delta−20)/10), 2 + floor(round/2) )
if round ≤ 9: dmg −= 1
+4 if winner has 生之焰;  − 慈念曲 stacks (floor 1);
猫魂庇佑: if dmg is EVEN, dmg = dmg/2;   龙鳞: cap dmg at 20
```

Nothing in this formula affects the fight. Do not track 命元 during a trace — track the
**final HP gap**, then apply the formula once.

---

## 4. Keyword glossary

Chinese is the game's own keyword text (`localization/1.5.9/combined_cards.json`);
English is yisim's internal field name.

| 中文 | yisim | rule |
|---|---|---|
| `[灵气]` | `qi` | see §3. |
| `[剑意]` | `sword_intent` | +1 ATK per point on every hit; exhausted at end of card (§2.6). |
| `[防]` | `def` | damage shield; halved (`ceil`) at start of owner's turn. |
| `[无视防御]` | `ignore_def` | **one attack** ignores 防 entirely; 1 stack spent per attack. Cards that say "此牌攻击时[无视防御]" (云剑·猫爪, 震雷剑-class) grant-then-spend per hit, so they never eat a pre-existing stack. |
| `[碎防]` | `smash_def` | attack destroys 防 at 2× rate; see §2.4. |
| `[护体]` | `guard_up` | negates one whole HP hit; does not protect 防 or HP costs. |
| `[锋锐]` | `penetrate` | flat bonus added to HP damage on `[击伤]`, then fully consumed. There is **no** `[穿透]` keyword. |
| `[再次行动]` | `chase` | one extra action; capped at **+1 per turn** (`max_chases=1`). There is **no** `[疾速]` keyword in the data. |
| `[身法]` | `agility` | 10 agility ⇒ buy one chase. |
| `[困缚]` | `entangle` | cancels a chase, spends 1; decays 1/turn. |
| `[击伤]` | `injured` | "this attack got HP damage through" — the condition on 震雷剑, 飞牙剑, 云剑·游龙, 飞灵闪影剑. |
| `[内伤]` | `internal_injury` | HP loss at start of each of your turns; permanent. |
| `[外伤]` | `wound` | adds to every `[击伤]` you take; permanent. |
| `[恢复]` | `regen` | heal at start of each of your turns; permanent. |
| `[加攻]/[减攻]` | `increase_atk` / `decrease_atk` | flat ± in the additive stage; permanent. |
| `[虚弱]` | `weaken` | your damage ×0.6; decays 1/turn. |
| `[破绽]` | `flaw` | damage taken ×1.4; decays 1/turn. |
| `[气势]` | `force` | +10% per point; **1 point spent per attack**. |
| `[消耗]/[持续]` | `consumption`/`continuous` | slot removed from the cycle (§1.5). |
| `[开局]/[后招]` | `opening`/`post_action` | pre-battle / from 2nd play of the slot. |
| `[连云]` | `cloud_hit` | true iff `cloud_sword_chain_count > 0` (`if_cloud_hit`, `gs:4808`). The counter increments **after** a 云剑 card resolves (`gs:1775`) and **resets to 0 the moment you play a non-云剑 card** (unless 云海/如海耐力 covers it). **So the first 云剑 of a run never has 连云; the second onward do.** |
| `[五行]` gating | `if_wood/fire/earth/metal/water_spirit` | true iff the **previously played card** (`last_card_id`, set at end of every card, `gs:1796`) is of that element, **or generates it** (木→火→土→金→水→木, `gs:5595`), **or** an `[激活X灵]` stack is live. Playing any non-element card breaks the chain. |
| `[卦象]/[星力]/[星位]` | `hexagram`/`star_power`/`is_star_point` | Heptastar resources. Slots **3 and 6** (0-indexed 2 and 5) are `[星位]` by default (`gs:862-867`). |

**Sword formations `剑阵`** (`is_sword_formation`, `gs:6058`) — a card-name class, not a
mechanic in itself; several cards key off "how many 剑阵 I've played" or "retrigger the
previous 剑阵".

---

## 5. Card reference (林小月 sword-intent lobby)

Levels are yisim's 1/2/3 = the UI's base / `+1` / `+2`. Qi cost 0 unless stated.

### Intent generators (never attack ⇒ never spend the bank)
| 卡 | lv1 / lv2 / lv3 |
|---|---|
| **剑挡** Sword Defence `111101` | 防+4/5/6, 剑意+2/3/4 |
| **凝意诀** Contemplate Spirits Rhythm `112071` | 灵气+1, 剑意+3/4/5 |
| **云舞诀** Cloud Dance Rhythm `113051` | 灵气+2/3/4, 防+2/3/4, 剑意+2/3/4 |
| **剑意激荡** Sword Intent Surge `115051` | current 剑意 **+80% / +110% / +140%** (floor) |
| **御空剑阵** Rule Sky Sword Formation `115061` | qi 1 **reduced by your 防** (free if 防≥1); 防+8/14/20; `[再次行动]` |
| **连环剑阵** Chain Sword Formation `115071` | 防+1/5/10; retriggers the **nearest 剑阵 card at a LOWER slot index** (`retrigger_previous_sword_formation`, `gs:4967`, scans backwards from the current slot). If none exists to its left, it does nothing but the 防. |

### Payoffs
| 卡 | lv1 / lv2 / lv3 |
|---|---|
| **剑劈** Sword Slash `111091` | **atk 4/5/6 first, then 剑意+2/3/4** |
| **震雷剑** Thunder Sword `111081` | qi 1; atk 5/6/7, `[击伤]` → extra atk 6/8/10 (both hits get the full bank) |
| **飞牙剑** Flying Fang Sword `111111` | qi 1; atk 8/11/14, `[击伤]` → refund the intent this card used (§2.6) |
| **灵猫乱剑** Spirit Cat Chaos Sword `614031` (林小月-only) | **2攻 × 2/3/4**, `+1 attack per card held in hand, max +3` → up to **5/6/7 hits**, each at `2 + 剑意` |
| **流云乱剑** Flow Cloud Chaos Sword `114081` | qi 1; 2攻 × 4/5/6 |
| **飞灵闪影剑** Flying Spirit Shade Sword `115031` | 1攻 × 4/5/6, **each `[击伤]` → +1 灵气** |
| **三峰剑** Tri-Peak Sword `113111` | 3/4/5 攻 × 3 |
| **骤风剑** Wind Sword `111121` | 3/4/6 攻 × 2 |
| **巨虎灵剑** Giant Tiger `111071` | qi 1; atk 10/13/16 |
| **巨鲲灵剑** Giant Kun `114061` | qi 3; atk 10/13/16, 防 same, `[再次行动]` |
| **万法归灵剑** Dharma Spirit Sword `115041` | drains **all** qi, +5/6/7 ATK per point drained, then atk 5 |

### Enablers / utility
| 卡 | effect |
|---|---|
| **灵气灌注** Qi Perfusion `111061` | 灵气+2/3/4; **下1次攻击[无视防御]** — the rider lands on whatever attacks next, so place it immediately before the one big hit. |
| **护身灵气** Guard Qi `111051` | 灵气+1/2/3, 防+5 (flat at all levels) |
| **轻剑** Light Sword `111041` | atk 4 (flat), 灵气+1/2/3 |
| **画龙点睛** Finishing Touch `345021` | `finishing_touch_stacks += 3/4/5`; `[消耗]`. Each subsequent card **permanently upgrades one level in the deck for the rest of the battle** (`do_finishing_touch`, `gs:3075`), applied *just before* that card is played. **A card already at lv3 fails to upgrade and does NOT consume a stack** (`try_upgrade_card` returns false) — the stack rolls forward to the next upgradable card. |
| **运笔如飞** Flying Brush `345011` | 防+6/12/18; the **next** card played chases (`do_flying_brush_chase`, `gs:2973` — fires at the start of that next card). |
| **云剑·猫爪** Cat Paw `612011` (林小月-only) | 4/6/8 攻 ×2, every hit `[无视防御]` (grants-then-spends, so pre-existing stacks survive). |
| **云剑·无妄** Necessity `113021` | 4/6/8 攻 ×2; `[连云]` → next 1 (lv3: 2) attacks `[无视防御]`. |
| **水月剑阵** Moon Water `114091` | 防+10/14/18; **防 does not halve for 3/4/5 of your turns** |
| **镜花剑阵** Mirror Flower `113101` | 防+3/5/8, then **atk 0 + your current 防** (bonus computed *after* the 防 gain) |
| **慈念曲** Kindness Tune `332011` | `[持续]`; the loser's 命元 damage −4/6/8 (floor 1). Symmetric — sets it for **both** players. |

### Common wall cards (what a defensive board looks like)
| 卡 | effect |
|---|---|
| **地灵丹** Earth Spirit Elixir `311011` | 防+11/16/21, `[消耗]` — a one-shot wall; a stall turn beats it. |
| **叶盾花** Leaf Shield Flower `362031` | 防+8/14; **lv3**: 防+20 and `[持续]`: up to half of every HP loss is redirected to 防 (`leaf_shield_flower_stacks`, `gs:3690`). |
| **土灵印** Earth Spirit Seal `131051` | 3/5/7 攻, 防+4/6/8, `[激活土灵]` |
| **土灵阵** Earth Spirit Formation `132051` | 防+4/6/8, `[持续]`: +2/3/4 防 on **every** 土灵 card played |
| **土灵·群山** Mountains `132061` | 5/6/7 攻, 防+2/3/4, `[土灵]`: +3/6/9 防 **next turn** |
| **土灵·断崖** Cliff `133061` | 防+10/15/20, `[土灵]`: the next time your 防 drops, deal that much (non-attack) damage back |
| **土灵·绝壁** Steep `134051` | 防+12, `[土灵]`: +1 防 per 6/5/4 防 you have lost this battle (`def_lost` is cumulative for the whole battle) |

### Cards that dominate the ghost pool
(from `agents/ghosts.json`, 30 trajectories; the pool is ~40% 云剑-chain, ~30% 五行, ~30% 卦象/星弈)

| 卡 | effect | why it matters to you |
|---|---|---|
| **云剑·游龙** `115011` (most common card in the pool) | 2攻 ×2/3/4; `[连云]` 防+3/5/7; **`[击伤]` → `[再次行动]`** | their chase engine; blocked entirely if they can't wound you |
| **云剑·闪风** `114011` | 4/8/12 攻; `[连云]` → chase | |
| **云剑·月影** `114021` | 防+1/2/3; `[连云]` → +2/3/4 `[加攻]` **permanently** | their ATK grows every cycle |
| **金灵·飞梭** `134071` | 4/8/12 攻; `[金灵]` → chase | |
| **水灵·腾浪** `134091` | 灵气+2/3/4, HP&max+2/3/4; `[水灵]` → 水势 per 2 qi | |

Because chases cap at **+1 per turn**, a 云剑 board with three chase cards still only
plays 2 cards per turn. Breaking the `[连云]` chain (they must play 云剑 back-to-back)
or denying `[击伤]` with 防 shuts most of their tempo off.

---

## 6. Character innates and fates

Only battle-relevant ones; this section is deliberately short.

**林小月 (sw4)**
* **剑韵修炼** Sword Rhyme Cultivate — `+1 剑意 at battle start` at 筑基/金丹/元婴 tiers,
  **`+2` at 化神** (`gs:1152 / 1184 / 1216 / 1253`). Stacks if taken more than once.
  Applied in `start_of_game_setup`, before turn 1a, so your opening card already has it.
* **灵猫踏云** Lithe As Cat — **+1 灵气 every time you play a 云剑 card**
  (`do_cloud_sword_softheart_and_friends`, `gs:1720`). Fires on the card, not on the chain.
* **猫魂庇佑** Cat Soul Bless — **post-battle only**: if the 命元 damage you take on a
  loss is **even**, halve it (`gs:1644`). Zero combat effect; do not put it in a trace.

**Sword-sect generic fates you will meet**
* **剑阵守护** Sword Formation Guard — playing **slot 1** gives 防 +1/3/6/9 (by tier) and
  1 stack of 水月剑阵 (no 防 halving next turn) (`gs:1972`). Only at `trigger_depth === 1`.
* **狂念** Mad Obsession — starts you with `unrestrained_sword_count`.
* **云之法则** Rule of the Cloud — +防 on every 云剑 card.

**Ghost-side innates worth knowing** (all post-battle or economy except as noted)
* **生之焰** Flame of Life (炎-sect) — **+4 命元 damage when they win.** Battle-neutral.
* **龙鳞** Dragon Scale — caps their 命元 loss at 20.
* **储灵** Store Qi — they open with +1 灵气 at 筑基/金丹, +2 at 元婴, +3 at 化神
  (`gs:1165 / 1211 / 1237 / 1270`), which changes their turn-1 tempo.
* **锟铻金环** Kun Wu Metal Ring — **+1 防 on every 防 gain** (`gs:3922`). Makes a wall
  materially thicker than the card text suggests.

---

## 7. Worked example

**Board (林小月, 化神):** `[1] 剑劈+2 · [2] 剑挡+2 · [3] 画龙点睛 · [4] 剑意激荡+1 · [5] 灵猫乱剑+1`
(5 slots, so the cycle is 1→2→3→4→5→1). HP 100, qi 0, 防 0.
Fate: **剑韵修炼 (化神) ⇒ 剑意 = 2 before turn 1a.** 3 cards held in hand.

**Opponent (a simple earth wall):**
`[1] 地灵丹 (防+11,[消耗]) · [2] 叶盾花 (防+8) · [3] 土灵印 (3攻,防+4,激活土灵) ·
[4] 土灵·群山 (5攻,防+2,[土灵]:下回合+3防) · [5] 护身灵气 (灵气+1,防+5)`. HP 100.

I go first.

| turn | card | qi | 剑意 | my 防 | their 防 | damage | HP after |
|---|---|---|---|---|---|---|---|
| **1a** | `[1] 剑劈+2` = 6攻 then 剑意+4 | 0 | 2 → mark 2 → +4 = 6 → **−2 = 4** | 0 | 0 | `6 + 2 = 8`, all to HP | them **92** |
| **1b** | `[1] 地灵丹` 防+11, `[消耗]` (slot 1 dead for the battle) | 0 | – | 0 | 0 → **11** | – | – |
| **2a** | `[2] 剑挡+2` = 防+6, 剑意+4. No attack ⇒ **nothing exhausted** | 0 | 4 → **8** | 0 → **6** | 11 | – | – |
| **2b** | 防 decay `11 − ceil(11/2)=6` → 5; `[2] 叶盾花` 防+8 | 0 | – | 6 | 5 → **13** | – | – |
| **3a** | 防 decay `6 − 3` → 3; `[3] 画龙点睛` → `finishing_touch = 3`, `[消耗]` (slot 3 dead) | 0 | 8 | 3 | 13 | – | – |
| **3b** | 防 decay `13 − 7` → 6; `[3] 土灵印` 3攻 then 防+4 | 0 | – | 3 → **0** (absorbs all 3) | 6 → **10** | 3 to 防, 0 to HP — **no `[击伤]`** | me **100** |
| **4a** | 防 decay 0; **`do_finishing_touch` upgrades slot 4 剑意激荡 lv2→lv3** (stacks 3→2), then plays it at **+140%**: `floor(8 × 1.40) = 11` | 0 | 8 → **19** | 0 | 10 | – | – |
| **4b** | 防 decay `10 − 5` → 5; `[4] 土灵·群山` 5攻, 防+2, `[土灵]` fires (previous card 土灵印 is 土) → `next_turn_def += 3` | 0 | – | 0 | 5 → **7** | 5 straight to my HP | me **95** |
| **5a** | 防 decay 0; **finishing touch upgrades slot 5 灵猫乱剑 lv2→lv3** (stacks 2→1) ⇒ `2攻 ×4` base **+3 held cards = 7 hits**, each `2 + 19 = 21` | 0 | 19 → **0** at end of card | 0 | 7 → 0 | hit 1: 7 to 防 + **14** to HP; hits 2–7: **6 × 21 = 126** to HP | them `92 − 140 = ` **−48 → dead** |

**Why 剑劈 was worth playing first and why the bank survived it:** on 1a the attack
marked `sword_intent_to_lose = 2` (the bank *at the moment of the hit*), the card then
banked +4, and end-of-card subtracted only 2. Net +2.

**What 画龙点睛 actually bought:** it never touched 剑劈/剑挡 — those are already lv3, so
`try_upgrade_card` fails and **no stack is spent**. Both stacks landed on the two cards
that could still grow. Counterfactual without it: 剑意激荡 lv2 = `floor(8×1.10) = 8` ⇒
bank 16; 灵猫乱剑 lv2 = `3 + 3 = 6` hits at 18 ⇒ `7` to 防 + `101` to HP ⇒ them at −9.
Still lethal, but the margin (and therefore the 命元 swing) is ~39 HP smaller.

**The failure mode this board has:** if the opponent's 防 on turn 5a had been ≥ 21, hit 1
would have been fully absorbed, no `[击伤]`, and the bank of 19 would still have been
spent at end of card. That is why 灵气灌注 (`[无视防御]` on the next attack) belongs
immediately before the payoff against a real wall — and why 飞牙剑, whose refund is
gated on `[击伤]`, must never be the card that eats a block turn.

---

## 8. Twelve rules people get wrong

1. 剑意 is spent **once per card, after all its hits**, not per hit — and the amount
   spent is the *maximum* bank observed during the card, so a card that banks intent
   *and then* gets an appended extra attack empties you.
2. 飞牙剑 refunds only on `[击伤]`. Blocked ⇒ bank lost.
3. Chases cap at **+1 per turn** regardless of how many chase triggers fire.
4. Failing to afford a card **ends your turn** and gives +1 qi; the cursor does not move.
5. 防 halves at the **start of its owner's turn** (`ceil` of the loss), so the number you
   hit into is the one set on their *previous* turn, undecayed.
6. `[消耗]`/`[持续]` remove the **slot** from the cycle permanently — shortening your
   cycle and changing which card meets which of theirs.
7. 画龙点睛 upgrades are **permanent for the battle** and **skip lv3 cards without
   spending a stack**.
8. `[连云]` is false on the first 云剑 of a run and resets on any non-云剑 card.
   五行 gating likewise looks only at the **immediately previous card played**.
9. `[护体]` negates one whole HP hit of any size — a 100-damage hit and a 1-damage hit
   cost the same stack.
10. `[气势]` is spent 1 per attack and is a **×** term (+10%/point), so it interacts
    badly with multi-hit cards (spent on hit 1, gone for hit 2).
11. An empty slot is a **3-damage attack turn**, not a free skip.
12. 命元 is computed once, after the battle, from the final HP gap. Nothing in combat
    reads it.

---

## 9. Where yisim probably differs from the live game

Flagged honestly; do not treat these as settled.

* **First-player determination is not implemented at all.** `a first:` is an input and
  the config comment says `TODO implement speed comparison`. Every speed/seating rule
  must come from observation, not this code.
* **`todo_patches.txt` lists cards patched in-game but not in yisim**: 清心剑阵
  (Clear Heart Sword Formation), 天髓葫芦, 星月卦扇, 冥影身法, 崩拳·还玄, 千星爆,
  不息乾坤. Also: 极致相克阵 (杜伶鸳) has moved from "after use" to "upon use" upstream.
  Treat any trace involving those as unreliable.
* **`hand_count` defaults to 17** (`gs:215`) rather than the real hand size, so yisim's
  灵猫乱剑 / 云剑-hand-count cards always get the maximum bonus unless you set it. In a
  hand trace, use the real number of cards you are holding.
* **The empty-slot filler is 普通攻击 lv1 (3攻)** in yisim's parser, while the live card
  table's base 普通攻击 row is level 2 (6攻). I have kept 3攻 (it matches field
  observation) but this is unverified.
* **`do_finishing_touch` reads `qi_cost` from the pre-upgrade card** (`gs:3441` computes
  cost, `gs:3572` re-reads `card_id` after the upgrade). If a card's qi cost differs
  between levels, yisim charges the old cost. No card in the 林小月 build is affected.
* Known engine bugs called out in the source itself: 破碎剑阵 consumes `smash_def`
  incorrectly (`gs:4457` "BUG"), 静止守护剑阵 miscounts chases cancelled by 困缚
  (`gs:3607` "BUG"), 崩拳-bounce is not re-checked under 梦-崩天步 (`gs:3466` "BUG").
* `notes.txt` records several behaviours as **speculation** rather than tested: whether
  虚空剑阵 triggers off 回声剑阵-copied cards, and the interaction of 无妄剑·清心 with
  non-无妄 attacks.
* The engine snapshot is from ~1.5.9 (`localization/1.5.9/`). Anything added or rebalanced
  after that is simply absent.
