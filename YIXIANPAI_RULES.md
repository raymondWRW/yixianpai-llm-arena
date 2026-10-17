# YiXianPai (弈仙牌) — What It Is and the General Rules

> Compiled from the sibling project `card counter with proxy` (its `selfplay/GAME_MODEL.md`,
> `selfplay/economy.py`, `selfplay/draws.py`, `proxy_view.py`, game config dumps) plus
> general knowledge of the game. Numbers marked **exact** come from the game's own
> config tables; **mined** means fitted from recorded real games.

---

## 1. What YiXianPai is

**YiXianPai (弈仙牌, English title *Yi Xian: The Cultivation Card Game*)** is a free-to-play
**8-player auto-battler card game** with a Chinese *xianxia* (immortal cultivation) theme,
developed by 玄魂 (Guangzhou XuanHun) and released on Steam / mobile in 2023. It plays like a
cross between **Teamfight Tactics / Hearthstone Battlegrounds** (8 players, prep phase then an
auto-resolved 1v1 each round, last one standing wins) and a **deck-cycling card game** (your
"board" is an ordered loop of cards that fires in sequence).

Core loop of a match:

```
8 players ─► each round: PREP (draw / reroll / merge / absorb / arrange board / breakthrough)
                        └► BATTLE: random 1v1 pairing, combat auto-resolves (no input)
                        └► loser loses 命 (Destiny/life points); at 0 you are eliminated
          ─► repeat until one player remains; placement 1st–8th
```

The player only makes decisions in the **prep phase**. Combat is fully deterministic given
both boards, both players' stats, and the server's RNG queue — which is why the sibling
project could re-host the game's own combat DLL as an "Oracle" and get 99.97% parity.

Key vocabulary (Chinese / English used in the codebase):

| 中文 | English | Meaning |
|---|---|---|
| 修为 | Cultivation | XP-like resource; gates realm breakthroughs |
| 境界 / 境 | Realm | Level 1–5 (6 exists in config); sets base HP and unlocks card phases |
| 突破 | Breakthrough | Player-timed level-up once cultivation ≥ threshold; triggers a 天命 offer |
| 命 / 命元 | Destiny (life pool) | Starts at 100; loser drops by the battle margin; 0 = out |
| 生命 / 血量 | HP | In-battle health = realm base HP + extras |
| 灵气 | Qi | In-battle resource many cards consume/generate |
| 换牌 | Exchange / reroll | Swap a hand card for a fresh draw from your deck pool |
| 炼化 | Refine / absorb | Destroy a hand card for +1 修为 |
| 合成 | Merge | 3 copies of a card at level L → 1 copy at level L+1 |
| 天命 | Immortal Fate | Passive talents offered on breakthrough (pick 1 of 4) |
| 副职 | Side job / sub-profession | Chosen at round 2; adds a second card pool |
| 天衍 / 道韵 | Derivation / Dao rhyme | Special card/effect grants at fixed rounds |
| 体魄 | Physique | Secondary stat some cards/sects build |
| 消耗 / 持续 | Consumable / Continuous | Card tags whose count on a board is capped |
| 走火入魔 | Deviation Syndrome | Junk card dealt when the draw pool is empty |

---

## 2. Setup: characters, sects, sub-professions

- **4 sects**, each with its own card pool and 6 playable characters (24 total):

  | Sect | English | Characters |
  |---|---|---|
  | 云灵剑宗 | Cloud Spirit Sword Sect | 牧逸风, 炎雪, 龙瑶, 林小月, 陆剑心, 黎承云 |
  | 七星阁 | Heptastar Pavilion | 谭舒雁, 炎尘, 曜灵, 姜袭明, 吴策, 风绪 |
  | 五行道盟 | Five Elements Alliance | 吾行之, 杜伶鸳, 花沁蕊, 慕虎, 南宫生, 祁忘忧 |
  | 锻玄宗 | Duan Xuan Sect | 小布, 屠馗, 叶冥冥, 姬方生, 李㵘, 翎羽 |

- Each character has an **innate talent** and a personal 天命 line; sect determines the
  base card pool you draw from.
- **Sub-profession (副职)** is picked at **round 2** (one of 7): 炼丹师 Elixirist, 符咒师
  Fuluist (talismans), 琴师 Musician, 画师 Painter, 阵法师 Formation Master, 灵植师 Plant
  Master, 命理师 Fortune-teller. Its cards are added to your deck pool (phase-gated).
- Every player starts with **命 = 100**, realm 1, cultivation 0.

---

## 3. Round structure (prep phase)

Each round every player, simultaneously and privately:

1. **Round start grants** — new cards dealt, exchange charges added, +2 passive cultivation
   (from round 2), any fate/round-start effects.
2. **Free draw** — cards dealt at prep open (**mined**): **5** in round 1, **3** in rounds
   2–11, **4** from round 12. (~20% of rounds show +1, likely breakthrough/grant extras.)
3. **Exchange (换牌)** — spend a charge to swap one hand card for a new draw.
   Charges granted per round: **+3** (R1–9), **+4** (R10–12), **+6** (R13+); unlimited
   banking (real players bank ~17 by R10 and spend them fishing newly-unlocked cards).
4. **Refine (炼化)** — destroy a hand card for **+1 修为**. Does *not* affect the deck pool.
5. **Merge (合成)** — 3 identical cards at level L → 1 at level L+1 (levels 1→2→3, one
   level per round). Also **+1 修为** per merge (mined).
6. **Breakthrough (突破)** — when cultivation reaches the next realm's requirement you may
   break through; you get a **天命 offer (choose 1 of 4)**, HP base rises, and the next
   card phase becomes drawable. Player-timed: you can delay to bank a stronger fate.
7. **Arrange the board** — place cards from hand into the unlocked slots, in order.
8. **Ready (准备)** — ends your prep; the round proceeds when all are ready or the timer
   ends.

Hand size is effectively uncapped in practice (real hands reach 15+).

### 3.1 Realm table (**exact**, `LevelConfig.dat`)

| Realm 境 | Cultivation required | Base HP |
|---|---|---|
| 1 | 0 | 40 |
| 2 | 9 | 45 |
| 3 | 21 | 52 |
| 4 | 36 | 62 |
| 5 | 55 | 75 |
| 6 | 75 | 100 (config only; play is capped at 5) |

Battle max HP = base HP + extra max HP (from fates/cards).
Real median schedule (4k+ 道心 players): 境3 by ~R5, 境4 by ~R7, 境5 by ~R11.

### 3.2 Board slots (**mined**, n=103)

`unlocked = min(8, round + 2)` → R1: 3, R2: 4, R3: 5, R4: 6, R5: 7, R6+: 8.

### 3.3 Cultivation sources

- +2 passive every round from round 2 (floor = 2·(round−1))
- +1 per 炼化
- +1 per merge
- fates/cards can add more
- Real median: R2=2, R3=6, R4=10, R5=15, R6=22.

### 3.4 Special picks

- **副职 side job**: round 2.
- **道韵 (Dao rhyme)**: offered at the start of **round 4 and round 14** (4 options, e.g. a
  free draw now, or a chosen phase-4/5 card delivered when you reach that phase).
- **天衍 derivations**: special card lines (e.g. 云剑·X, 幻·X, 狂剑·X) that enter your deck
  *only* through their pick, never the normal draw.

---

## 4. The deck pool and draw rules

Every player has a private **deck pool** (your sect's cards + your side-job cards).

- **Copies per card**: **8** by default; **6** for phase-5 (Incarnation-phase) cards;
  **3** for the Elixirist's three special elixirs. Side-job and derivation cards start at 0
  copies until picked.
- **Card phases**: cards have a phase 1–5 (Meditation → Foundation → Virtuoso →
  Immortality → Incarnation). Only cards of the **current phase or lower** (phase unlocks with
  realm) are drawable.
- **Draw law**: uniform weighted-bag over remaining copies (each remaining copy = weight 1).
  **Exception**: on the *first* exchange of a Foundation / Virtuoso / Immortality round,
  current-phase copies count **double**.
- **Drawing removes 1 copy** of that card from the pool.
- **Exchange burn**: the discarded card loses copies from the pool — **3** for sect cards,
  **2** for sub-profession cards under the current season rule (cards with an Exchange
  effect are not burned). This is what makes a **card counter** useful: draw −1, reroll −2/−3.
- **炼化 does not touch the pool.**
- **Empty eligible pool → 走火入魔** (Deviation Syndrome) junk card is dealt.
- Excluded from the normal draw: derivation/event cards, dream (梦…) cards, personal-fate
  cards, special non-drawable cards.

---

## 5. Battle rules

- After prep, living players are **randomly paired** (the game avoids repeating your
  immediate-previous opponent when it can — repeats grow as the field shrinks). With an odd
  count someone fights a "ghost"/bye.
- Each side's board is an **ordered cycle** of up to 8 cards. Combat alternates turns; on your
  turn you play the **next card in your cycle** (after slot 8 it wraps to slot 1). Empty
  slots act as a basic attack (普攻). Because the cycle length is the number of slots used,
  **ordering matters enormously** — this is the main skill in the game.
- **Turn order**: the player with higher 修为 acts first (coin flip on ties).
- Each player has HP = realm base HP + extras. Cards deal damage, heal, add shields/defense,
  generate/consume 灵气 (qi), apply buffs/debuffs, trigger extra actions, etc. Many cards have
  conditions on qi, on the previous card, on your sect's mechanic (sword intent 剑意, five
  elements 五行, stars 星, physique 体魄, …).
- **Damage math** (official FAQ): apply flat additions/subtractions first (floored to 1), then
  multiply by the summed percentage modifiers; final result ≥ 1.
- Battle ends when a side hits 0 HP or the turn limit is reached (then higher HP wins).
- **Outcome → 命**: the **loser loses 命 equal to the margin** (roughly the winner's
  remaining HP / life-damage margin); the winner's 命 is unchanged. Some fates/cards add
  secondary 命 effects. At **0 命 you are eliminated**; last player standing wins, and
  final placement is by elimination order (survivors ranked by remaining 命).

### 5.1 Board legality (mined constraint)

Boards observed in real play respect **≤2 消耗 (consumable) and ≤2 持续 (continuous) cards,
combined ≤2** — the game caps how many of these tagged cards can be fielded.

---

## 6. Card levels and merging

- Cards come in **level 1 / 2 / 3** (id + 10000 per level in the data). Higher level = stronger
  numbers on the same effect.
- **3 copies at level L → 1 copy at level L+1**, only when the copies are in hand (board copies
  must be taken back first). Some cards (e.g. 灵羽) merge server-side at battle time with no
  visible marker.
- Duplicates are often *kept unmerged on purpose* (two lv1 copies fill two slots), so merging is
  a real decision, not automatic.

---

## 7. Fates (天命), talents, and other passives

- On each breakthrough you're offered **4 天命** (slot 0 is your character's phase-specific fate;
  the other 3 come from sect + general pools). Pick 1. Fates have **per-phase versions** whose
  magnitudes scale with when you take them.
- Effects range from flat stat deltas (+HP cap, +体魄, +修为, +命, +exchange charges) to card
  grants (draw N cards of type X) to in-combat triggers handled by the battle engine.
- Character **innates** and side-job passives layer on top.

---

## 8. Strategy summary (why the AI stack looks the way it does)

- **Economy vs. tempo**: 炼化 for cultivation to break through early (bigger HP, new phases)
  vs. keeping cards to build a board now vs. banking exchanges to fish key cards later.
- **Board building** is a search over *which* cards to field and *in what cyclic order* against
  an unknown opponent — the sibling project solves this with candidate enumeration + Held-Karp
  ordering + the re-hosted game engine, and predicts the opponent's board with a Transformer.
- **Card counting** matters because your deck pool is finite and burned by exchanges: knowing how
  many copies of a key card remain tells you whether fishing for it is worth the charges.
- The only inputs the player controls are prep-phase actions; everything else (pairing, draws,
  combat RNG queue) is server-authoritative.

---

## 9. Sources in the sibling repo

- `card counter with proxy/selfplay/GAME_MODEL.md` — confirmed transition rules and provenance
- `card counter with proxy/selfplay/economy.py`, `draws.py` — realm table, slots, rerolls,
  cultivation, deal counts, draw law
- `card counter with proxy/proxy_view.py` — copy counts, side-job pools, reroll burn
- `card counter with proxy/oracle/README.md` — the re-hosted combat engine (99.97% parity)
- `card counter with proxy/characters.csv`, `cards.csv`, `fates.csv`, `derivations.csv` — data
