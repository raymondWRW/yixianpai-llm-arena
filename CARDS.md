# YiXianPai Card Library (弈仙牌 卡牌图鉴)

Generated from `card counter with proxy` data: `cards.csv` (base list, 942 cards), `oracle/data/extracted/configs/CardConfig.dat` (current game config v2.9.1 — CN text + numeric params, primary source), `tools/cards_game.json` + `vendor/yisim-master/localization/1.5.8/combined_cards.json` (EN text / v1.5.8 fallback), `tools/card_phases.json` (phase / sect), `proxy/card_types.json` (消耗/持续 tags), `derivations.csv`.

**How to read:** each card lists Lv1/Lv2/Lv3 text (CN, then EN). Card ids: level = `id + 10000×(level−1)`. Phase = the realm stage at which the card becomes drawable (1 炼气 → 5 化神; 6 = special/non-drawable). Tags 消耗 (Consumable) / 持续 (Continuous) count against the board cap (≤2 each, combined ≤2). Text marked ⟨template⟩ is unresolved (newer card, no numeric params in the local dump).

**Common keyword glossary:** 攻 ATK · 防 DEF · 灵气 Qi · 剑意 Sword Intent · 剑气 Sword Qi · 击伤 Injured (on hit) · 再次行动 Chase (act again) · 被动 Passive · 持续 Continuous · 消耗 Consumable · 外伤 Wound · 内伤 Internal Injury · 星力 Star Power · 卦象 Hexagram · 五行 Five Elements · 体魄 Physique · 加攻 ATK up · 减攻 ATK down · 无法行动 Stunned · 命元 Destiny · 修为 Cultivation.

## Contents

- [Sect: 云灵剑宗 Cloud Spirit Sword Sect](#sect-云灵剑宗-cloud-spirit-sword-sect) — 97 cards
- [Sect: 七星阁 Heptastar Pavilion](#sect-七星阁-heptastar-pavilion) — 99 cards
- [Sect: 五行道盟 Five Elements Alliance](#sect-五行道盟-five-elements-alliance) — 105 cards
- [Sect: 锻玄宗 Duan Xuan Sect](#sect-锻玄宗-duan-xuan-sect) — 97 cards
- [Side job (副职): 炼丹师 Elixirist](#side-job-副职-炼丹师-elixirist) — 15 cards
- [Side job (副职): 符咒师 Fuluist](#side-job-副职-符咒师-fuluist) — 15 cards
- [Side job (副职): 琴师 Musician](#side-job-副职-琴师-musician) — 15 cards
- [Side job (副职): 画师 Painter](#side-job-副职-画师-painter) — 15 cards
- [Side job (副职): 阵法师 Formation Master](#side-job-副职-阵法师-formation-master) — 16 cards
- [Side job (副职): 灵植师 Plant Master](#side-job-副职-灵植师-plant-master) — 27 cards
- [Side job (副职): 命理师 Fortune-teller](#side-job-副职-命理师-fortune-teller) — 20 cards
- [Derivation / event cards of 云灵剑宗 Cloud Spirit Sword Sect (not in normal draw)](#derivation--event-cards-of-云灵剑宗-cloud-spirit-sword-sect-not-in-normal-draw) — 27 cards
- [Derivation / event cards of 七星阁 Heptastar Pavilion (not in normal draw)](#derivation--event-cards-of-七星阁-heptastar-pavilion-not-in-normal-draw) — 25 cards
- [Derivation / event cards of 五行道盟 Five Elements Alliance (not in normal draw)](#derivation--event-cards-of-五行道盟-five-elements-alliance-not-in-normal-draw) — 26 cards
- [Derivation / event cards of 锻玄宗 Duan Xuan Sect (not in normal draw)](#derivation--event-cards-of-锻玄宗-duan-xuan-sect-not-in-normal-draw) — 29 cards
- [General, event & special cards (id < 1,000,000)](#general-event--special-cards-id--1000000) — 251 cards
- [Dream (梦·) cards — general](#dream-梦-cards--general) — 24 cards
- [Dream (梦·) cards — 七星阁 Heptastar Pavilion](#dream-梦-cards--七星阁-heptastar-pavilion) — 1 cards
- [Special / event / spirit-pet cards (id 99xxxxxx)](#special--event--spirit-pet-cards-id-99xxxxxx) — 38 cards


## Sect: 云灵剑宗 Cloud Spirit Sword Sect


### Phase 1 — 炼气 Meditation

#### 云剑·探云 (Cloud Sword - Touch Sky) — id 1000001
- **Lv1**: 6攻  
  *6 ATK*
- **Lv2**: 9攻  
  *9 ATK*
- **Lv3**: 12攻  
  *12 ATK*

#### 云剑·飞刺 (Cloud Sword - Fleche) — id 1000002
- **Lv1**: 5攻 / [连云]：追加3攻  
  *5 ATK / [Cloud Hit]: Make an additional 3 ATK*
- **Lv2**: 6攻 / [连云]：追加5攻  
  *6 ATK / [Cloud Hit]: Make an additional 5 ATK*
- **Lv3**: 7攻 / [连云]：追加7攻  
  *7 ATK / [Cloud Hit]: Make an additional 7 ATK*

#### 云剑·厚土 (Cloud Sword - Touch Earth) — id 1000003
- **Lv1**: 4攻 / [连云]：[防]+4  
  *4 ATK / [Cloud Hit]: [DEF]+4*
- **Lv2**: 6攻 / [连云]：[防]+6  
  *6 ATK / [Cloud Hit]: [DEF]+6*
- **Lv3**: 8攻 / [连云]：[防]+8  
  *8 ATK / [Cloud Hit]: [DEF]+8*

#### 轻剑 (Light Sword) — id 1000004
- **Lv1**: 4攻 / [灵气]+1  
  *4 ATK / [Qi]+1*
- **Lv2**: 4攻 / [灵气]+2  
  *4 ATK / [Qi]+2*
- **Lv3**: 4攻 / [灵气]+3  
  *4 ATK / [Qi]+3*

#### 护身灵气 (Guard Qi) — id 1000005
- **Lv1**: [灵气]+1 / [防]+5  
  *[Qi]+1 / [DEF]+5*
- **Lv2**: [灵气]+2 / [防]+5  
  *[Qi]+2 / [DEF]+5*
- **Lv3**: [灵气]+3 / [防]+5  
  *[Qi]+3 / [DEF]+5*

#### 灵气灌注 (Qi Perfusion) — id 1000006
- **Lv1**: [灵气]+2 / 下1次攻击[无视防御]  
  *[Qi]+2 / Next 1 attack [Ignore DEF]*
- **Lv2**: [灵气]+3 / 下1次攻击[无视防御]  
  *[Qi]+3 / Next 1 attack [Ignore DEF]*
- **Lv3**: [灵气]+4 / 下1次攻击[无视防御]  
  *[Qi]+4 / Next 1 attack [Ignore DEF]*

#### 巨虎灵剑 (Giant Tiger Spirit Sword) — id 1000007
- **Lv1**: 10攻  
  *10 ATK*
- **Lv2**: 13攻  
  *13 ATK*
- **Lv3**: 16攻  
  *16 ATK*

#### 震雷剑 (Thunder Sword) — id 1000009
- **Lv1**: 5攻 / [击伤]：追加6攻  
  *5 ATK / [Injured]: Make an additional 6 ATK*
- **Lv2**: 6攻 / [击伤]：追加8攻  
  *6 ATK / [Injured]: Make an additional 8 ATK*
- **Lv3**: 7攻 / [击伤]：追加10攻  
  *7 ATK / [Injured]: Make an additional 10 ATK*

#### 剑劈 (Sword Slash) — id 1000010
- **Lv1**: 4攻 / [剑意]+2  
  *4 ATK / [Sword Intent]+2*
- **Lv2**: 5攻 / [剑意]+3  
  *5 ATK / [Sword Intent]+3*
- **Lv3**: 6攻 / [剑意]+4  
  *6 ATK / [Sword Intent]+4*

#### 剑挡 (Sword Defence) — id 1000012
- **Lv1**: [防]+4 / [剑意]+2  
  *[DEF]+4 / [Sword Intent]+2*
- **Lv2**: [防]+5 / [剑意]+3  
  *[DEF]+5 / [Sword Intent]+3*
- **Lv3**: [防]+6 / [剑意]+4  
  *[DEF]+6 / [Sword Intent]+4*

#### 骤风剑 (Wind Sword) — id 1000013
- **Lv1**: 3攻×2  
  *3 ATK × 2*
- **Lv2**: 4攻×2  
  *4 ATK × 2*
- **Lv3**: 6攻×2  
  *6 ATK × 2*

#### 飞牙剑 (Flying Fang Sword) — id 1000021
- **Lv1**: 8攻 / [击伤]：返还此牌攻击用的[剑意]  
  *8 ATK / [Injured]: Return the [Sword Intent] used by this attack*
- **Lv2**: 11攻 / [击伤]：返还此牌攻击用的[剑意]  
  *11 ATK / [Injured]: Return the [Sword Intent] used by this attack*
- **Lv3**: 14攻 / [击伤]：返还此牌攻击用的[剑意]  
  *14 ATK / [Injured]: Return the [Sword Intent] used by this attack*

#### 韵灵剑 (Rhyme Spirit Sword) — id 1000047
- **Lv1**: 4攻 / [击伤]：每击伤1点生命加1[灵气]  
  *4 ATK / [Injured]: Add [Qi] for each damage dealt to HP*
- **Lv2**: 5攻 / [击伤]：每击伤1点生命加1[灵气]  
  *5 ATK / [Injured]: Add [Qi] for each damage dealt to HP*
- **Lv3**: 6攻 / [击伤]：每击伤1点生命加1[灵气]  
  *6 ATK / [Injured]: Add [Qi] for each damage dealt to HP*

#### 勤拙剑 (Diligent Sword) — id 1000054
- **Lv1**: 6攻 / 每有5点修为多1攻  
  *6 ATK / Add 1 ATK for every 5 points of Cultivation*
- **Lv2**: 6攻 / 每有4点修为多1攻  
  *6 ATK / Add 1 ATK for every 4 points of Cultivation*
- **Lv3**: 6攻 / 每有3点修为多1攻  
  *6 ATK / Add 1 ATK for every 3 points of Cultivation*

#### 梦·灵气灌注 (Dream - Qi Perfusion) — id 1000067
- **Lv1**: [灵气]+1 / 下一次攻击多5攻  
  *[Qi]+1 / Next attack gains 5 ATK*
- **Lv2**: [灵气]+1 / 下一次攻击多7攻  
  *[Qi]+1 / Next attack gains 7 ATK*
- **Lv3**: [灵气]+1 / 下一次攻击多10攻 / [被动]：[相邻]牌的[击伤]效果必定触发  
  *[Qi]+1 / Next attack gains 10 ATK / [Passive]: [Adjacent] cards' [Injured] effects always trigger*

#### 梦·云剑点星 (Dream - Cloud Sword Pierce the Star) — id 1000069
- **Lv1**: [灵气]+2 / [被动]：[相邻]牌使用后造成1点伤害  
  *[Qi]+2 / [Passive]: After an [Adjacent] card is played deal 1 DMG*
- **Lv2**: [灵气]+2 / [被动]：[相邻]牌使用后造成2点伤害  
  *[Qi]+2 / [Passive]: After an [Adjacent] card is played deal 2 DMG*
- **Lv3**: [灵气]+2 / [被动]：[相邻]牌使用后造成3点伤害  
  *[Qi]+2 / [Passive]: After an [Adjacent] card is played deal 3 DMG*

#### 梦·云剑极意 (Dream - Cloud Sword - Riddle) — id 1000070
- **Lv1**: 6攻 / [云海]+1 / [连云]：[剑意]+2  
  *6 ATK / [Cloud Sea]+1 / [Cloud Hit]: [Sword Intent]+2*
- **Lv2**: 8攻 / [云海]+1 / [连云]：[剑意]+2  
  *8 ATK / [Cloud Sea]+1 / [Cloud Hit]: [Sword Intent]+2*
- **Lv3**: 8攻 / [云海]+1 / [连云]：每连续用过一次云剑加1[剑意]  
  *8 ATK / [Cloud Sea]+1 / [Cloud Hit]: For each consecutive Cloud Sword played, gain 1 [Sword Intent]*

#### 梦·飞牙剑 (Dream - Flying Fang Sword) — id 1000071
- **Lv1**: 6攻 / 返还此牌所耗[剑意]  
  *6 ATK / Return the [Sword Intent] consumed by this card*
- **Lv2**: 8攻 / 返还此牌所耗[剑意]  
  *8 ATK / Return the [Sword Intent] consumed by this card*
- **Lv3**: 10攻 / 返还此牌所耗[剑意]  
  *10 ATK / Return the [Sword Intent] consumed by this card*

#### 梦·云舞诀 (Dream - Cloud Dance Rhythm) — id 1000072
- **Lv1**: [灵气]+1 / [剑意]+2  
  *[Qi]+1 / [Sword Intent]+2*
- **Lv2**: [灵气]+2 / [剑意]+2  
  *[Qi]+2 / [Sword Intent]+2*
- **Lv3**: [灵气]+3 / [剑意]+2  
  *[Qi]+3 / [Sword Intent]+2*

#### 梦·狂剑一式 (Dream - Unrestrained Sword One) — id 1000073
- **Lv1**: 6攻 / 生命上限+10 / 每用过一次狂剑就吸取对方1生命  
  *6 ATK / Max HP+10 / For each Unrestrained Sword played, steal 1 HP from the opponent*
- **Lv2**: 8攻 / 生命上限+10 / 每用过一次狂剑就吸取对方1生命  
  *8 ATK / Max HP+10 / For each Unrestrained Sword played, steal 1 HP from the opponent*
- **Lv3**: 10攻 / 生命上限+10 / 每用过一次狂剑就吸取对方1生命  
  *10 ATK / Max HP+10 / For each Unrestrained Sword played, steal 1 HP from the opponent*

#### 梦·百鸟灵剑诀 (Dream - CentiBird Spirit Sword Rhythm) — id 1000074
- **Lv1**: [灵气]+1 / [剑气]+2  
  *[Qi]+1 / [Sword Qi]+2*
- **Lv2**: [灵气]+2 / [剑气]+2  
  *[Qi]+2 / [Sword Qi]+2*
- **Lv3**: [灵气]+3 / [剑气]+2  
  *[Qi]+3 / [Sword Qi]+2*

#### 梦·万法归灵剑 (Dream - Dharma Spirit Sword) — id 1000075
- **Lv1**: 3攻 / [剑气]+1 / [被动]：所有剑牌均可触发[剑气]  
  *3 ATK / [Sword Qi]+1 / [Passive]: All sword cards can trigger [Sword Qi]*
- **Lv2**: 5攻 / [剑气]+1 / [被动]：所有剑牌均可触发[剑气]  
  *5 ATK / [Sword Qi]+1 / [Passive]: All sword cards can trigger [Sword Qi]*
- **Lv3**: 5攻 / [剑气]+2 / [被动]：所有剑牌均可触发[剑气]  
  *5 ATK / [Sword Qi]+2 / [Passive]: All sword cards can trigger [Sword Qi]*

#### 梦·狂剑零式 (Dream - Unrestrained Sword Zero) — id 1000076
- **Lv1**: 生命+6 / 每用过一次狂剑加1生命  
  *HP+6 / For each Unrestrained Sword played, gain 1 HP*
- **Lv2**: 生命+7 / 每用过一次狂剑加2生命  
  *HP+7 / For each Unrestrained Sword played, gain 2 HP*
- **Lv3**: 生命+8 / 每用过一次狂剑加3生命  
  *HP+8 / For each Unrestrained Sword played, gain 3 HP*

#### 梦·灵犀剑阵 (Dream - Consonance Sword Formation) — id 1000077
*持续 Continuous*  
- **Lv1**: [防]+6 / [持续]：每加1[灵气]时加1[防]  
  *[DEF]+6 / [Continuous]: Whenever you gain 1 [Qi], gain 1 [DEF]*
- **Lv2**: [防]+6 / [持续]：每加1[灵气]时加2[防]  
  *[DEF]+6 / [Continuous]: Whenever you gain 1 [Qi], gain 2 [DEF]*
- **Lv3**: [防]+4 / [持续]：每加1[灵气]/[剑意]时加2/1[防]  
  *[DEF]+4 / [Continuous]: Whenever you gain 1 [Qi]/[Sword Intent], gain 2/1 [DEF]*

#### 梦·云剑厚土 (Dream - Cloud Sword - Touch Earth) — id 1000078
- **Lv1**: [防]+6 / [云海]+1 / [连云]：每连续用过一次云剑加1[防]  
  *[DEF]+6 / [Cloud Sea]+1 / [Cloud Hit]: For each consecutive Cloud Sword played, +1 [DEF]*
- **Lv2**: [防]+9 / [云海]+1 / [连云]：每连续用过一次云剑加1[防]  
  *[DEF]+9 / [Cloud Sea]+1 / [Cloud Hit]: For each consecutive Cloud Sword played, +1 [DEF]*
- **Lv3**: [防]+9 / [云海]+2 / [连云]：每连续用过一次云剑加2[防]  
  *[DEF]+9 / [Cloud Sea]+2 / [Cloud Hit]: For each consecutive Cloud Sword played, +2 [DEF]*

#### 梦·反身剑 (Dream - Reflexive Sword) — id 1000079
- **Lv1**: 4攻 / [防]+6  
  *4 ATK / [DEF]+6*
- **Lv2**: 6攻 / [防]+6  
  *6 ATK / [DEF]+6*
- **Lv3**: 6攻 / [防]+6 / 每用过一张剑牌多1攻和1[防]  
  *6 ATK / [DEF]+6 / For each Sword card played, +1 ATK and 1 [DEF]*

#### 梦·御空剑阵 (Dream - Rule Sky Sword Formation) — id 1000080
- **Lv1**: 造成6点[伤害] / 卡组每有一张剑阵多1[伤害]  
  *Deal 6 [DMG] / For each Sword Formation in your deck, deal 1 more [DMG]*
- **Lv2**: 造成6点[伤害] / 卡组每有一张剑阵多2[伤害]  
  *Deal 6 [DMG] / For each Sword Formation in your deck, deal 2 more [DMG]*
- **Lv3**: 造成6点[伤害] / 卡组每有一张剑阵多3[伤害]  
  *Deal 6 [DMG] / For each Sword Formation in your deck, deal 3 more [DMG]*

#### 梦·巨鹏灵剑 (Dream - Giant Roc Spirit Sword) — id 1000081
- **Lv1**: 5攻 / [灵气]+1  
  *5 ATK / [Qi]+1*
- **Lv2**: 7攻 / [灵气]+1  
  *7 ATK / [Qi]+1*
- **Lv3**: 9攻 / [灵气]+1  
  *9 ATK / [Qi]+1*

#### 梦·地煞剑 (Dream - Earth Evil Sword) — id 1000082
- **Lv1**: 1攻 / 每[击伤]1生命就施加1层[内伤]（最多2）  
  *1 ATK / For every 1 HP [Injured], apply 1 [Internal Injury] (max 2)*
- **Lv2**: 1攻 / 每[击伤]1生命就施加1层[内伤]（最多3）  
  *1 ATK / For every 1 HP [Injured], apply 1 [Internal Injury] (max 3)*
- **Lv3**: 2攻 / 每[击伤]1生命就施加1层[内伤]（最多4）  
  *2 ATK / For every 1 HP [Injured], apply 1 [Internal Injury] (max 4)*

#### 梦·云剑柔心 (Dream - Cloud Sword - Softheart) — id 1000083
*持续 Continuous*  
- **Lv1**: [防]+4 / [持续]：每回合开始时加1[防]  
  *[DEF]+4 / [Continuous]: At the beginning of each turn add 1 [DEF]*
- **Lv2**: [防]+8 / [持续]：每回合开始时加1[防]  
  *[DEF]+8 / [Continuous]: At the beginning of each turn add 1 [DEF]*
- **Lv3**: [防]+4 / [持续]：每回合开始时加2[防]  
  *[DEF]+4 / [Continuous]: At the beginning of each turn add 2 [DEF]*

#### 梦·引气剑 (Dream - Spiritage Sword) — id 1000084
*消耗 Consumable, 持续 Continuous*  
- **Lv1**: [灵气]+2 / [剑气]+1 / [消耗]  
  *[Qi]+2 / [Sword Qi]+1 / [Consumption]*
- **Lv2**: [灵气]+2 / [剑气]+2 / [消耗]  
  *[Qi]+2 / [Sword Qi]+2 / [Consumption]*
- **Lv3**: [灵气]+2 / [剑气]+3 / [消耗]  
  *[Qi]+2 / [Sword Qi]+3 / [Consumption]*

#### 梦·凝意诀 (Dream - Contemplate Spirits Rhythm) — id 1000085
- **Lv1**: [剑意]+3  
  *[Sword Intent]+3*
- **Lv2**: [剑意]+4  
  *[Sword Intent]+4*
- **Lv3**: [剑意]+5  
  *[Sword Intent]+5*

#### 梦·云剑汇灵 (Dream - Cloud Sword - Spirit Coercion) — id 1000086
- **Lv1**: 4攻 / [灵气]>0则追加一次攻击  
  *4 ATK / If [Qi] > 0, make an additional attack*
- **Lv2**: 5攻 / [灵气]>0则追加一次攻击  
  *5 ATK / If [Qi] > 0, make an additional attack*
- **Lv3**: 6攻 / [灵气]>0则追加一次攻击  
  *6 ATK / If [Qi] > 0, make an additional attack*

#### 梦·狂剑二式 (Dream - Unrestrained Sword Two) — id 1000087
*持续 Continuous*  
- **Lv1**: 4攻 / 生命+2 / 算作用过1次狂剑  
  *4 ATK / HP+2 / Count as having played 1 Unrestrained Sword*
- **Lv2**: 4攻 / 生命+4 / 算作用过1次狂剑  
  *4 ATK / HP+4 / Count as having played 1 Unrestrained Sword*
- **Lv3**: 4攻 / 生命+6 / 算作用过1次狂剑  
  *4 ATK / HP+6 / Count as having played 1 Unrestrained Sword*


### Phase 2 — 筑基 Foundation

#### 形意剑 (Form-Intention Sword) — id 1000011
- **Lv1**: 8攻 / [击伤]：[剑意]+3  
  *8 ATK / [Injured]: [Sword Intent]+3*
- **Lv2**: 11攻 / [击伤]：[剑意]+4  
  *11 ATK / [Injured]: [Sword Intent]+4*
- **Lv3**: 14攻 / [击伤]：[剑意]+5  
  *14 ATK / [Injured]: [Sword Intent]+5*

#### 云剑·无锋 (Cloud Sword - Conceal) — id 1000014
- **Lv1**: [连云]：9攻  
  *[Cloud Hit]: 9 ATK*
- **Lv2**: [连云]：13攻  
  *[Cloud Hit]: 13 ATK*
- **Lv3**: [连云]：17攻  
  *[Cloud Hit]: 17 ATK*

#### 云剑·极意 (Cloud Sword - Riddle) — id 1000015
- **Lv1**: 6攻 / [连云]：[剑意]+2  
  *6 ATK / [Cloud Hit]: [Sword Intent]+2*
- **Lv2**: 8攻 / [连云]：[剑意]+3  
  *8 ATK / [Cloud Hit]: [Sword Intent]+3*
- **Lv3**: 10攻 / [连云]：[剑意]+4  
  *10 ATK / [Cloud Hit]: [Sword Intent]+4*

#### 云剑·回守 (Cloud Sword - Reguard) — id 1000016
- **Lv1**: [防]+8 / [连云]：生命+3  
  *[DEF]+8 / [Cloud Hit]: HP+3*
- **Lv2**: [防]+11 / [连云]：生命+5  
  *[DEF]+11 / [Cloud Hit]: HP+5*
- **Lv3**: [防]+14 / [连云]：生命+7  
  *[DEF]+14 / [Cloud Hit]: HP+7*

#### 凝意诀 (Contemplate Spirits Rhythm) — id 1000017
- **Lv1**: [灵气]+1 / [剑意]+3  
  *[Qi]+1 / [Sword Intent]+3*
- **Lv2**: [灵气]+1 / [剑意]+4  
  *[Qi]+1 / [Sword Intent]+4*
- **Lv3**: [灵气]+1 / [剑意]+5  
  *[Qi]+1 / [Sword Intent]+5*

#### 化灵诀 (Transforming Spirits Rhythm) — id 1000018
- **Lv1**: [灵气]+3  
  *[Qi]+3*
- **Lv2**: [灵气]+4  
  *[Qi]+4*
- **Lv3**: [灵气]+5  
  *[Qi]+5*

#### 巨鲸灵剑 (Giant Whale Spirit Sword) — id 1000019
- **Lv1**: 16攻  
  *16 ATK*
- **Lv2**: 20攻  
  *20 ATK*
- **Lv3**: 24攻  
  *24 ATK*

#### 狂剑·一式 (Unrestrained Sword - One) — id 1000022
- **Lv1**: 5攻 / 每用过1次“狂剑”多2攻  
  *5 ATK / For each "Unrestrained Sword" you played in this battle, this card adds 2 more ATK*
- **Lv2**: 8攻 / 每用过1次“狂剑”多3攻  
  *8 ATK / For each "Unrestrained Sword" you played in this battle, this card adds 3 more ATK*
- **Lv3**: 10攻 / 每用过1次“狂剑”多5攻  
  *10 ATK / For each "Unrestrained Sword" you played in this battle, this card adds 5 more ATK*

#### 引气剑 (Spiritage Sword) — id 1000024
- **Lv1**: [灵气]+2 / [灵气]>2则追加3攻×2  
  *[Qi]+2 / If [Qi] is greater than 2, make an additional 3 ATK 2 times*
- **Lv2**: [灵气]+3 / [灵气]>3则追加3攻×2  
  *[Qi]+3 / If [Qi] is greater than 3, make an additional 3 ATK 2 times*
- **Lv3**: [灵气]+4 / [灵气]>4则追加3攻×2  
  *[Qi]+4 / If [Qi] is greater than 4, make an additional 3 ATK 2 times*

#### 地煞剑 (Earth Evil Sword) — id 1000030
- **Lv1**: 8攻 / [击伤]：每击伤1点生命加1[防]  
  *8 ATK / [Injured]: Add [DEF] for each damage dealt to HP*
- **Lv2**: 11攻 / [击伤]：每击伤1点生命加1[防]  
  *11 ATK / [Injured]: Add [DEF] for each damage dealt to HP*
- **Lv3**: 14攻 / [击伤]：每击伤1点生命加1[防]  
  *14 ATK / [Injured]: Add [DEF] for each damage dealt to HP*

#### 灵犀剑阵 (Consonance Sword Formation) — id 1000033
- **Lv1**: [防]+9 / 耗尽[剑意]，增加等量[灵气]  
  *[DEF]+9 / Exhaust [Sword Intent], add 1 [Qi] for each point exhausted*
- **Lv2**: [防]+14 / 耗尽[剑意]，增加等量[灵气]  
  *[DEF]+14 / Exhaust [Sword Intent], add 1 [Qi] for each point exhausted*
- **Lv3**: [防]+19 / 耗尽[剑意]，增加等量[灵气]  
  *[DEF]+19 / Exhaust [Sword Intent], add 1 [Qi] for each point exhausted*

#### 云剑·拂晓 (Cloud Sword - Dawn) — id 1000048
- **Lv1**: [防]+4 / [连云]：2攻×3  
  *[DEF]+4 / [Cloud Hit]: 2 ATK × 3*
- **Lv2**: [防]+6 / [连云]：3攻×3  
  *[DEF]+6 / [Cloud Hit]: 3 ATK × 3*
- **Lv3**: [防]+8 / [连云]：4攻×3  
  *[DEF]+8 / [Cloud Hit]: 4 ATK × 3*

#### 巨猿灵剑 (Giant Ape Spirit Sword) — id 1000055
- **Lv1**: 6攻 / 获得3层[加攻]  
  *6 ATK / Gain 3 stacks of [Increase ATK]*
- **Lv2**: 6攻 / 获得4层[加攻]  
  *6 ATK / Gain 4 stacks of [Increase ATK]*
- **Lv3**: 6攻 / 获得5层[加攻]  
  *6 ATK / Gain 5 stacks of [Increase ATK]*

#### 御灵心法 (Spirit Command Citta-Dharma) — id 1000088
*持续 Continuous*  
- **Lv1**: [持续]：每加1[灵气]时加2[防]，每失去1[灵气]时加1[防]  
  *[Continuous]: Whenever you gain 1 [Qi], add 2 [DEF]; whenever you lose 1 [Qi], add 1 [DEF]*
- **Lv2**: [持续]：每加1[灵气]时加2[防]，每失去1[灵气]时加2[防]  
  *[Continuous]: Whenever you gain 1 [Qi], add 2 [DEF]; whenever you lose 1 [Qi], add 2 [DEF]*
- **Lv3**: [防]+5 / [持续]：每加1[灵气]时加2[防]，每失去1[灵气]时加2[防]  
  *[DEF]+5 / [Continuous]: Whenever you gain 1 [Qi], add 2 [DEF]; whenever you lose 1 [Qi], add 2 [DEF]*


### Phase 3 — 金丹 Virtuoso

#### 反身剑 (Reflexive Sword) — id 1000008
- **Lv1**: 11攻 / [击伤]：下回合加7[防]  
  *11 ATK / [Injured]: Add 7 [DEF] in your next turn*
- **Lv2**: 14攻 / [击伤]：下回合加10[防]  
  *14 ATK / [Injured]: Add 10 [DEF] in your next turn*
- **Lv3**: 17攻 / [击伤]：下回合加13[防]  
  *17 ATK / [Injured]: Add 13 [DEF] in your next turn*

#### 暗鸦灵剑 (Raven Spirit Sword) — id 1000020
- **Lv1**: 6攻 / 每剩余1点灵气加2[防]  
  *6 ATK / Add 2 [DEF] for each [Qi]*
- **Lv2**: 6攻 / 每剩余1点灵气加3[防]  
  *6 ATK / Add 3 [DEF] for each [Qi]*
- **Lv3**: 6攻 / 每剩余1点灵气加4[防]  
  *6 ATK / Add 4 [DEF] for each [Qi]*

#### 破气剑 (Burst Sword) — id 1000023
- **Lv1**: 11攻 / [击伤]：对方灵气减1  
  *11 ATK / [Injured]: Opponent loses 1 Qi*
- **Lv2**: 13攻 / [击伤]：对方灵气减2  
  *13 ATK / [Injured]: Opponent loses 2 Qi*
- **Lv3**: 15攻 / [击伤]：对方灵气减3  
  *15 ATK / [Injured]: Opponent loses 3 Qi*

#### 云剑·柔心 (Cloud Sword - Softheart) — id 1000026
*持续 Continuous*  
- **Lv1**: [持续]：每次使用“云剑”时加2生命  
  *[Continuous]: Whenever you play a "Cloud Sword", heal 2 HP*
- **Lv2**: [持续]：每次使用“云剑”时加3生命  
  *[Continuous]: Whenever you play a "Cloud Sword", heal 3 HP*
- **Lv3**: [持续]：每次使用“云剑”时加4生命  
  *[Continuous]: Whenever you play a "Cloud Sword", heal 4 HP*

#### 云剑·点星 (Cloud Sword - Pierce the Star) — id 1000027
- **Lv1**: [灵气]+2 / 0攻（每剩余1点[灵气]多1攻）  
  *[Qi]+2 / 0 ATK (Add 1 ATK for each [Qi])*
- **Lv2**: [灵气]+3 / 0攻（每剩余1点[灵气]多1攻）  
  *[Qi]+3 / 0 ATK (Add 1 ATK for each [Qi])*
- **Lv3**: [灵气]+4 / 0攻（每剩余1点[灵气]多1攻）  
  *[Qi]+4 / 0 ATK (Add 1 ATK for each [Qi])*

#### 云剑·无妄 (Cloud Sword - Necessity) — id 1000028
- **Lv1**: 4攻×2 / [连云]：下1次攻击[无视防御]  
  *4 ATK × 2 / [Cloud Hit]: Next 1 time attack [Ignore DEF]*
- **Lv2**: 6攻×2 / [连云]：下1次攻击[无视防御]  
  *6 ATK × 2 / [Cloud Hit]: Next 1 time attack [Ignore DEF]*
- **Lv3**: 8攻×2 / [连云]：下2次攻击[无视防御]  
  *8 ATK × 2 / [Cloud Hit]: Next 2 times attack [Ignore DEF]*

#### 巨鹏灵剑 (Giant Roc Spirit Sword) — id 1000029
- **Lv1**: 9攻 / 剩余灵气>0则[再次行动]  
  *9 ATK / If [Qi] is greater than 0, [Chase]*
- **Lv2**: 12攻 / 剩余灵气>0则[再次行动]  
  *12 ATK / If [Qi] is greater than 0, [Chase]*
- **Lv3**: 15攻 / 剩余灵气>0则[再次行动]  
  *15 ATK / If [Qi] is greater than 0, [Chase]*

#### 云舞诀 (Cloud Dance Rhythm) — id 1000031
- **Lv1**: [灵气]+2 / [防]+2 / [剑意]+2  
  *[Qi]+2 / [DEF]+2 / [Sword Intent]+2*
- **Lv2**: [灵气]+3 / [防]+3 / [剑意]+3  
  *[Qi]+3 / [DEF]+3 / [Sword Intent]+3*
- **Lv3**: [灵气]+4 / [防]+4 / [剑意]+4  
  *[Qi]+4 / [DEF]+4 / [Sword Intent]+4*

#### 三峰剑 (Tri-Peak Sword) — id 1000032
- **Lv1**: 3攻×3  
  *3 ATK × 3*
- **Lv2**: 4攻×3  
  *4 ATK × 3*
- **Lv3**: 5攻×3  
  *5 ATK × 3*

#### 镜花剑阵 (Mirror Flower Sword Formation) — id 1000046
- **Lv1**: [防]+3 / 0攻（每有1点[防]多1攻）  
  *[DEF]+3 / 0 ATK (Add 1 ATK for each 1 [DEF])*
- **Lv2**: [防]+5 / 0攻（每有1点[防]多1攻）  
  *[DEF]+5 / 0 ATK (Add 1 ATK for each 1 [DEF])*
- **Lv3**: [防]+8 / 0攻（每有1点[防]多1攻）  
  *[DEF]+8 / 0 ATK (Add 1 ATK for each 1 [DEF])*

#### 狂剑·盘龙 (Unrestrained Sword - Dragon Coiled) — id 1000049
- **Lv1**: [防]+6 / 每用过1次“狂剑”多加6[防]  
  *[DEF]+6 / For each "Unrestrained Sword" you played in this battle, add 6 more [DEF]*
- **Lv2**: [防]+8 / 每用过1次“狂剑”多加8[防]  
  *[DEF]+8 / For each "Unrestrained Sword" you played in this battle, add 8 more [DEF]*
- **Lv3**: [防]+10 / 每用过1次“狂剑”多加10[防]  
  *[DEF]+10 / For each "Unrestrained Sword" you played in this battle, add 10 more [DEF]*

#### 一心一剑 (One Heart One Sword) — id 1000056
- **Lv1**: 6攻 / 此牌受4倍[剑意]加成，且不受[虚弱]影响  
  *6 ATK / This card receives a 4x bonus from [Sword Intent] and it is not affected by [Weakened]*
- **Lv2**: 6攻 / 此牌受5倍[剑意]加成，且不受[虚弱]影响  
  *6 ATK / This card receives a 5x bonus from [Sword Intent] and it is not affected by [Weakened]*
- **Lv3**: 6攻 / 此牌受6倍[剑意]加成，且不受[虚弱]影响  
  *6 ATK / This card receives a 6x bonus from [Sword Intent] and it is not affected by [Weakened]*

#### 合势剑阵 (Synergy Sword Formation) — id 1000062
- **Lv1**: 4攻 / [防]+4 / 卡组中每有1张其他“剑阵”，此牌多3攻和3[防]  
  *4 ATK / [DEF]+4 / For each other "Sword Formation" in the deck, this card has 3 more ATK and 3 more [DEF]*
- **Lv2**: 4攻 / [防]+4 / 卡组中每有1张其他“剑阵”，此牌多4攻和4[防]  
  *4 ATK / [DEF]+4 / For each other "Sword Formation" in the deck, this card has 4 more ATK and 4 more [DEF]*
- **Lv3**: 4攻 / [防]+4 / 卡组中每有1张其他“剑阵”，此牌多5攻和5[防]  
  *4 ATK / [DEF]+4 / For each other "Sword Formation" in the deck, this card has 5 more ATK and 5 more [DEF]*

#### 云剑·汇灵 (Cloud Sword - Spirit Coercion) — id 1000063
- **Lv1**: 7攻 / [连云]：每连续用过1张“云剑”加1[灵气]  
  *7 ATK / [Cloud Hit]: For each consecutive Cloud Sword played, add 1 [Qi]*
- **Lv2**: 11攻 / [连云]：每连续用过1张“云剑”加1[灵气]  
  *11 ATK / [Cloud Hit]: For each consecutive Cloud Sword played, add 1 [Qi]*
- **Lv3**: 15攻 / [连云]：每连续用过1张“云剑”加1[灵气]  
  *15 ATK / [Cloud Hit]: For each consecutive Cloud Sword played, add 1 [Qi]*

#### 丹雀灵剑 (Vermilion Sparrow Spirit Sword) — id 1000089
- **Lv1**: 6攻×2 / 再耗1[灵气]：追加6攻  
  *6 ATK × 2 / Spend 1 more [Qi]: make an additional 6 ATK*
- **Lv2**: 8攻×2 / 再耗1[灵气]：追加6攻  
  *8 ATK × 2 / Spend 1 more [Qi]: make an additional 6 ATK*
- **Lv3**: 10攻×2 / 再耗1[灵气]：追加6攻  
  *10 ATK × 2 / Spend 1 more [Qi]: make an additional 6 ATK*


### Phase 4 — 元婴 Immortality

#### 聚灵心法 (Spirit Gather Citta-Dharma) — id 1000034
*持续 Continuous*  
- **Lv1**: [灵气]+1 / [持续]：每2回合加1[灵气]  
  *[Qi]+1 / [Continuous]: Add 1 [Qi] every 2 turns*
- **Lv2**: [灵气]+1 / [持续]：每回合加1[灵气]  
  *[Qi]+1 / [Continuous]: Add 1 [Qi] each your turn*
- **Lv3**: [灵气]+3 / [持续]：每回合加1[灵气]  
  *[Qi]+3 / [Continuous]: Add 1 [Qi] each your turn*

#### 狂剑·二式 (Unrestrained Sword - Two) — id 1000035
*derived from: 轻剑*  
- **Lv1**: 4攻 / 每用过1次“狂剑”追加1次攻击  
  *4 ATK / For each "Unrestrained Sword" you played in this battle, make an additional attack*
- **Lv2**: 6攻 / 每用过1次“狂剑”追加1次攻击  
  *6 ATK / For each "Unrestrained Sword" you played in this battle, make an additional attack*
- **Lv3**: 9攻 / 每用过1次“狂剑”追加1次攻击  
  *9 ATK / For each "Unrestrained Sword" you played in this battle, make an additional attack*

#### 巨鲲灵剑 (Giant Kun Spirit Sword) — id 1000036
- **Lv1**: 10攻 / [防]+10 / [再次行动]  
  *10 ATK / [DEF]+10 / [Chase]*
- **Lv2**: 13攻 / [防]+13 / [再次行动]  
  *13 ATK / [DEF]+13 / [Chase]*
- **Lv3**: 16攻 / [防]+16 / [再次行动]  
  *16 ATK / [DEF]+16 / [Chase]*

#### 流云乱剑 (Flow Cloud Chaos Sword) — id 1000037
- **Lv1**: 2攻×4  
  *2 ATK × 4*
- **Lv2**: 2攻×5  
  *2 ATK × 5*
- **Lv3**: 2攻×6  
  *2 ATK × 6*

#### 灵感剑 (Inspiration Sword) — id 1000038
- **Lv1**: 8攻 / 每有1[灵气]加1[剑意](最多4) / [击伤]：改为最多7  
  *8 ATK / Add 1 [Sword Intent] for each [Qi] (maximum 4) / [Injured]: Change to maximum 7*
- **Lv2**: 12攻 / 每有1[灵气]加1[剑意](最多5) / [击伤]：改为最多10  
  *12 ATK / Add 1 [Sword Intent] for each [Qi] (maximum 5) / [Injured]: Change to maximum 10*
- **Lv3**: 16攻 / 每有1[灵气]加1[剑意](最多6) / [击伤]：改为最多13  
  *16 ATK / Add 1 [Sword Intent] for each [Qi] (maximum 6) / [Injured]: Change to maximum 13*

#### 云剑·闪风 (Cloud Sword - Flash Wind) — id 1000039
- **Lv1**: 4攻 / [连云]：[再次行动]  
  *4 ATK / [Cloud Hit]: [Chase]*
- **Lv2**: 8攻 / [连云]：[再次行动]  
  *8 ATK / [Cloud Hit]: [Chase]*
- **Lv3**: 12攻 / [连云]：[再次行动]  
  *12 ATK / [Cloud Hit]: [Chase]*

#### 云剑·月影 (Cloud Sword - Moon Shade) — id 1000040
- **Lv1**: [防]+1 / [连云]：获得2层[加攻]  
  *[DEF]+1 / [Cloud Hit]: Gain 2 stacks of [Increase ATK]*
- **Lv2**: [防]+2 / [连云]：获得3层[加攻]  
  *[DEF]+2 / [Cloud Hit]: Gain 3 stacks of [Increase ATK]*
- **Lv3**: [防]+3 / [连云]：获得4层[加攻]  
  *[DEF]+3 / [Cloud Hit]: Gain 4 stacks of [Increase ATK]*

#### 水月剑阵 (Moon Water Sword Formation) — id 1000041
- **Lv1**: [防]+10 / 回合开始时[防]不减半，持续3回合  
  *[DEF]+10 / At the beginning of your next 3 turns, your [DEF] will not halve*
- **Lv2**: [防]+14 / 回合开始时[防]不减半，持续4回合  
  *[DEF]+14 / At the beginning of your next 4 turns, your [DEF] will not halve*
- **Lv3**: [防]+18 / 回合开始时[防]不减半，持续5回合  
  *[DEF]+18 / At the beginning of your next 5 turns, your [DEF] will not halve*

#### 剑意流转 (Sword Intent Flow) — id 1000050
- **Lv1**: [剑意]+2 / 下一张牌攻击后保留剑意  
  *[Sword Intent]+2 / Keep the [Sword Intent] after the next card attack*
- **Lv2**: [剑意]+3 / 下一张牌攻击后保留剑意  
  *[Sword Intent]+3 / Keep the [Sword Intent] after the next card attack*
- **Lv3**: [剑意]+4 / 下一张牌攻击后保留剑意  
  *[Sword Intent]+4 / Keep the [Sword Intent] after the next card attack*

#### 溟空剑阵诀 (Emptiness Sword Formation) — id 1000051
*持续 Continuous*  
- **Lv1**: [持续]：每次使用“剑阵”牌后，追加7攻  
  *[Continuous]: After each time you play a "Sword Formation" card, make an additional 7 ATK*
- **Lv2**: [持续]：每次使用“剑阵”牌后，追加10攻  
  *[Continuous]: After each time you play a "Sword Formation" card, make an additional 10 ATK*
- **Lv3**: [持续]：每次使用“剑阵”牌后，追加13攻  
  *[Continuous]: After each time you play a "Sword Formation" card, make an additional 13 ATK*

#### 白鹭灵剑 (Egret Spirit Sword) — id 1000059
- **Lv1**: 5攻 / 每剩余1点灵气多2攻  
  *5 ATK / Add 2 ATK for each [Qi]*
- **Lv2**: 5攻 / 每剩余1点灵气多3攻  
  *5 ATK / Add 3 ATK for each [Qi]*
- **Lv3**: 5攻 / 每剩余1点灵气多4攻  
  *5 ATK / Add 4 ATK for each [Qi]*

#### 百鸟灵剑诀 (CentiBird Spirit Sword Rhythm) — id 1000065
*持续 Continuous · derived from: 云剑·厚土, 灵气灌注*  
- **Lv1**: [灵气]+1 / [持续]：“灵剑”牌的灵气消耗减1  
  *[Qi]+1 / [Continuous]: The "Spirit Sword" card's Qi cost decrease 1*
- **Lv2**: [灵气]+3 / [持续]：“灵剑”牌的灵气消耗减1  
  *[Qi]+3 / [Continuous]: The "Spirit Sword" card's Qi cost decrease 1*
- **Lv3**: [灵气]+3 / [持续]：“灵剑”牌的灵气消耗减2  
  *[Qi]+3 / [Continuous]: The "Spirit Sword" card's Qi cost decrease 2*

#### 飞豹灵剑 (Flying Leopard Spirit Sword) — id 1000090
- **Lv1**: 2攻 / [剑气]+2 / 每有1[灵气]或[剑气]加2[身法]（最多加10）  
  *2 ATK / [Sword Qi]+2 / Add 2 [Agility] for each [Qi] or [Sword Qi] (up to 10)*
- **Lv2**: 3攻 / [剑气]+3 / 每有1[灵气]或[剑气]加2[身法]（最多加10）  
  *3 ATK / [Sword Qi]+3 / Add 2 [Agility] for each [Qi] or [Sword Qi] (up to 10)*
- **Lv3**: 4攻 / [剑气]+4 / 每有1[灵气]或[剑气]加2[身法]（最多加10）  
  *4 ATK / [Sword Qi]+4 / Add 2 [Agility] for each [Qi] or [Sword Qi] (up to 10)*

#### 云剑·裂空 (Cloud Sword - Rend Sky) — id 1000091
- **Lv1**: 3攻×2 / 此牌受双倍[加攻]和[剑意]加成 / [连云]：此牌多1攻且获得[碎防]  
  *3 ATK × 2 / This card receives double [Increase ATK] and [Sword Intent] bonuses / [Cloud Hit]: This card adds 1 more ATK and gains [Smash DEF]*
- **Lv2**: 4攻×2 / 此牌受双倍[加攻]和[剑意]加成 / [连云]：此牌多2攻且获得[碎防]  
  *4 ATK × 2 / This card receives double [Increase ATK] and [Sword Intent] bonuses / [Cloud Hit]: This card adds 2 more ATK and gains [Smash DEF]*
- **Lv3**: 5攻×2 / 此牌受双倍[加攻]和[剑意]加成 / [连云]：此牌多3攻且获得[碎防]  
  *5 ATK × 2 / This card receives double [Increase ATK] and [Sword Intent] bonuses / [Cloud Hit]: This card adds 3 more ATK and gains [Smash DEF]*


### Phase 5 — 化神 Incarnation

#### 御空剑阵 (Rule Sky Sword Formation) — id 1000025
- **Lv1**: [防]>0则此牌无需灵气 / [防]+8 / [再次行动]  
  *No Qi cost for this card if [DEF]>0 / [DEF]+8 / [Chase]*
- **Lv2**: [防]>0则此牌无需灵气 / [防]+14 / [再次行动]  
  *No Qi cost for this card if [DEF]>0 / [DEF]+14 / [Chase]*
- **Lv3**: [防]>0则此牌无需灵气 / [防]+20 / [再次行动]  
  *No Qi cost for this card if [DEF]>0 / [DEF]+20 / [Chase]*

#### 云剑·游龙 (Cloud Sword - Dragon Roam) — id 1000042
*derived from: 云剑·探云*  
- **Lv1**: 2攻×2 / [连云]：[防]+3 / [击伤]：[再次行动]  
  *2 ATK × 2 / [Cloud Hit]: [DEF]+3 / [Injured]: [Chase]*
- **Lv2**: 2攻×3 / [连云]：[防]+5 / [击伤]：[再次行动]  
  *2 ATK × 3 / [Cloud Hit]: [DEF]+5 / [Injured]: [Chase]*
- **Lv3**: 2攻×4 / [连云]：[防]+7 / [击伤]：[再次行动]  
  *2 ATK × 4 / [Cloud Hit]: [DEF]+7 / [Injured]: [Chase]*

#### 飞灵闪影剑 (Flying Spirit Shade Sword) — id 1000043
*derived from: 云剑·飞刺*  
- **Lv1**: 1攻×4 / 每次[击伤]加1[灵气]  
  *1 ATK × 4 / Add 1 [Qi] for every attack that [Injured] the opponent*
- **Lv2**: 1攻×5 / 每次[击伤]加1[灵气]  
  *1 ATK × 5 / Add 1 [Qi] for every attack that [Injured] the opponent*
- **Lv3**: 1攻×6 / 每次[击伤]加1[灵气]  
  *1 ATK × 6 / Add 1 [Qi] for every attack that [Injured] the opponent*

#### 剑意激荡 (Sword Intent Surge) — id 1000044
- **Lv1**: 自身现有[剑意]增加80%  
  *Increase your existing [Sword Intent] stacks by 80%*
- **Lv2**: 自身现有[剑意]增加110%  
  *Increase your existing [Sword Intent] stacks by 110%*
- **Lv3**: 自身现有[剑意]增加140%  
  *Increase your existing [Sword Intent] stacks by 140%*

#### 万法归灵剑 (Dharma Spirit Sword) — id 1000045
- **Lv1**: 5攻 / 耗尽[灵气]，每耗1点多5攻  
  *5 ATK / Exhaust [Qi], add 5 ATK for each point exhausted*
- **Lv2**: 5攻 / 耗尽[灵气]，每耗1点多6攻  
  *5 ATK / Exhaust [Qi], add 6 ATK for each point exhausted*
- **Lv3**: 5攻 / 耗尽[灵气]，每耗1点多7攻  
  *5 ATK / Exhaust [Qi], add 7 ATK for each point exhausted*

#### 凌剑心法 (Apex Sword Citta-Dharma) — id 1000053
*持续 Continuous*  
- **Lv1**: [持续]：每回合加2[剑意]  
  *[Continuous]: Add 2 stacks of [Sword Intent] at the start of your turn*
- **Lv2**: [持续]：每回合加3[剑意]  
  *[Continuous]: Add 3 stacks of [Sword Intent] at the start of your turn*
- **Lv3**: [持续]：每回合加4[剑意]  
  *[Continuous]: Add 4 stacks of [Sword Intent] at the start of your turn*

#### 步月登云 (Step Moon Into Cloud) — id 1000057
*持续 Continuous*  
- **Lv1**: [持续]：每次使用“云剑”后获得1层[加攻]  
  *[Continuous]: After each time you play a "Cloud Sword", add 1 stack of [Increase ATK]*
- **Lv2**: [持续]：每次使用“云剑”后获得1层[加攻] / [再次行动]  
  *[Continuous]: After each time you play a "Cloud Sword", add 1 stack of [Increase ATK] / [Chase]*
- **Lv3**: [持续]：每次使用“云剑”后获得2层[加攻] / [再次行动]  
  *[Continuous]: After each time you play a "Cloud Sword", add 2 stacks of [Increase ATK] / [Chase]*

#### 云剑·凌波 (Cloud Sword - Step Lightly) — id 1000060
- **Lv1**: 3攻×2 / [防]+3 / [连云]：每连续用过1张“云剑”再加3[防]  
  *3 ATK × 2 / [DEF]+3 / [Cloud Hit]: For each consecutive Cloud Sword played, gain 3 [DEF]*
- **Lv2**: 3攻×3 / [防]+4 / [连云]：每连续用过1张“云剑”再加4[防]  
  *3 ATK × 3 / [DEF]+4 / [Cloud Hit]: For each consecutive Cloud Sword played, gain 4 [DEF]*
- **Lv3**: 3攻×4 / [防]+5 / [连云]：每连续用过1张“云剑”再加5[防]  
  *3 ATK × 4 / [DEF]+5 / [Cloud Hit]: For each consecutive Cloud Sword played, gain 5 [DEF]*

#### 狂剑·双龙 (Unrestrained Sword - Twin Dragons) — id 1000061
- **Lv1**: 2攻 / 下1次使用的“狂剑”连续生效2次  
  *2 ATK / Next "Unrestrained Sword" will trigger twice*
- **Lv2**: 8攻 / 下1次使用的“狂剑”连续生效2次  
  *8 ATK / Next "Unrestrained Sword" will trigger twice*
- **Lv3**: 14攻 / 下1次使用的“狂剑”连续生效2次  
  *14 ATK / Next "Unrestrained Sword" will trigger twice*

#### 连环剑阵 (Chain Sword Formation) — id 1000064
*derived from: 护身灵气*  
- **Lv1**: [防]+1 / 重复卡组中上一张“剑阵”牌的效果  
  *[DEF]+1 / Retrigger the previous "Sword Formation" card in the deck*
- **Lv2**: [防]+5 / 重复卡组中上一张“剑阵”牌的效果  
  *[DEF]+5 / Retrigger the previous "Sword Formation" card in the deck*
- **Lv3**: [防]+10 / 重复卡组中上一张“剑阵”牌的效果  
  *[DEF]+10 / Retrigger the previous "Sword Formation" card in the deck*

#### 狂剑·零式 (Unrestrained Sword - Zero) — id 1000066
*持续 Continuous*  
- **Lv1**: [持续]：用“狂剑”[击伤]对方时，恢复击伤值30%的生命  
  *[Continuous]: Whenever "Unrestrained Sword" [Injured] the opponent, you gain 30% of damage as HP*
- **Lv2**: [持续]：用“狂剑”[击伤]对方时，恢复击伤值50%的生命  
  *[Continuous]: Whenever "Unrestrained Sword" [Injured] the opponent, you gain 50% of damage as HP*
- **Lv3**: [持续]：用“狂剑”[击伤]对方时，恢复击伤值70%的生命  
  *[Continuous]: Whenever "Unrestrained Sword" [Injured] the opponent, you gain 70% of damage as HP*

#### 灵枢剑阵 (Spirit Pivot Sword Formation) — id 1000092
- **Lv1**: [灵气]+1 / [防]+1 / 1攻（每有1[灵气]多1攻） / 1攻（每有1[防]多1攻）  
  *[Qi]+1 / [DEF]+1 / 1 ATK (1 more ATK for each 1 [Qi]) / 1 ATK (1 more ATK for each 1 [DEF])*
- **Lv2**: [灵气]+2 / [防]+2 / 1攻（每有1[灵气]多1攻） / 1攻（每有1[防]多1攻）  
  *[Qi]+2 / [DEF]+2 / 1 ATK (1 more ATK for each 1 [Qi]) / 1 ATK (1 more ATK for each 1 [DEF])*
- **Lv3**: [灵气]+3 / [防]+3 / 1攻（每有1[灵气]多1攻） / 1攻（每有1[防]多1攻）  
  *[Qi]+3 / [DEF]+3 / 1 ATK (1 more ATK for each 1 [Qi]) / 1 ATK (1 more ATK for each 1 [DEF])*

#### 迅影飞剑 (Swift Shadow Flying Sword) — id 1000094
- **Lv1**: 4攻（不触发[剑意]） / [先机]：[剑意]+1 / [剑意]>0则[再次行动]  
  *4 ATK (does not trigger [Sword Intent]) / [First Use]: [Sword Intent]+1 / If [Sword Intent] > 0, [Chase]*
- **Lv2**: 5攻（不触发[剑意]） / [先机]：[剑意]+2 / [剑意]>0则[再次行动]  
  *5 ATK (does not trigger [Sword Intent]) / [First Use]: [Sword Intent]+2 / If [Sword Intent] > 0, [Chase]*
- **Lv3**: 6攻（不触发[剑意]） / [先机]：[剑意]+3 / [剑意]>0则[再次行动]  
  *6 ATK (does not trigger [Sword Intent]) / [First Use]: [Sword Intent]+3 / If [Sword Intent] > 0, [Chase]*

#### 剑影结界 (Sword Shadow Barrier) — id 1000095
- **Lv1**: 3攻×2 / [防]+4 / 本场战斗中自身每攻击过1次加2[防]  
  *3 ATK × 2 / [DEF]+4 / Add 2 [DEF] for each time you have attacked this battle*
- **Lv2**: 3攻×3 / [防]+5 / 本场战斗中自身每攻击过1次加2[防]  
  *3 ATK × 3 / [DEF]+5 / Add 2 [DEF] for each time you have attacked this battle*
- **Lv3**: 3攻×4 / [防]+6 / 本场战斗中自身每攻击过1次加2[防]  
  *3 ATK × 4 / [DEF]+6 / Add 2 [DEF] for each time you have attacked this battle*

#### 极·云剑柔心 (Ultimate - Cloud Sword - Softheart) — id 1000096
*持续 Continuous*  
- **Lv1**: 生命上限+20 / [再次行动] / [持续]：每次使用“云剑”时加1生命  
  *Max HP+20 / [Chase] / [Continuous]: Whenever you play a "Cloud Sword", heal 1 HP*
- **Lv2**: 生命上限+30 / [再次行动] / [持续]：每次使用“云剑”时加2生命  
  *Max HP+30 / [Chase] / [Continuous]: Whenever you play a "Cloud Sword", heal 2 HP*
- **Lv3**: 生命上限+40 / [再次行动] / [持续]：每次使用“云剑”时加3生命  
  *Max HP+40 / [Chase] / [Continuous]: Whenever you play a "Cloud Sword", heal 3 HP*

#### 极·暗鸦灵剑 (Ultimate - Raven Spirit Sword) — id 1000097
- **Lv1**: 6攻 / [灵气]+1 / 每剩余1点灵气加4[防]  
  *6 ATK / [Qi]+1 / Add 4 [DEF] for each [Qi]*
- **Lv2**: 6攻 / [灵气]+2 / 每剩余1点灵气加4[防]  
  *6 ATK / [Qi]+2 / Add 4 [DEF] for each [Qi]*
- **Lv3**: 6攻 / [灵气]+3 / 每剩余1点灵气加4[防]  
  *6 ATK / [Qi]+3 / Add 4 [DEF] for each [Qi]*

#### 云剑·追风 (Cloud Sword - Chase Wind) — id 1000098
- **Lv1**: [防]+2 / [云海]+2 / 此牌算作2次云剑 / [再次行动] / [连云]：此牌不耗[灵气]  
  *[DEF]+2 / [Cloud Sea]+2 / This card counts as 2 Cloud Swords / [Chase] / [Cloud Hit]: This card costs no [Qi]*
- **Lv2**: [防]+8 / [云海]+2 / 此牌算作2次云剑 / [再次行动] / [连云]：此牌不耗[灵气]  
  *[DEF]+8 / [Cloud Sea]+2 / This card counts as 2 Cloud Swords / [Chase] / [Cloud Hit]: This card costs no [Qi]*
- **Lv3**: [防]+12 / [云海]+2 / 此牌算作3次云剑 / [再次行动] / [连云]：此牌不耗[灵气]  
  *[DEF]+12 / [Cloud Sea]+2 / This card counts as 3 Cloud Swords / [Chase] / [Cloud Hit]: This card costs no [Qi]*


### Phase 6 — 特殊 Special

#### 残云封天剑 (Remnant Cloud Sky Sealing Sword) — id 1000052
- **Lv1**: 8攻 / 手牌中每留1张“云剑”，加8攻  
  *8 ATK / Add 8 ATK for each "Cloud Sword" remaining in your hand*
- **Lv2**: 10攻 / 手牌中每留1张“云剑”，加10攻  
  *10 ATK / Add 10 ATK for each "Cloud Sword" remaining in your hand*
- **Lv3**: 12攻 / 手牌中每留1张“云剑”，加12攻  
  *12 ATK / Add 12 ATK for each "Cloud Sword" remaining in your hand*

#### 秘剑·灵云 (Secret Sword - Spirit Cloud) — id 1000058
- **Lv1**: 4攻 / [连云]：攻+4 / 每有1点灵气追加1次攻击  
  *4 ATK / [Cloud Hit]: ATK+4 / Make an additional attack for each Qi*
- **Lv2**: 6攻 / [连云]：攻+6 / 每有1点灵气追加1次攻击  
  *6 ATK / [Cloud Hit]: ATK+6 / Make an additional attack for each Qi*
- **Lv3**: 8攻 / [连云]：攻+8 / 每有1点灵气追加1次攻击  
  *8 ATK / [Cloud Hit]: ATK+8 / Make an additional attack for each Qi*


### Phase 0 — ?

#### 梦·云剑探云 (Dream - Cloud Sword Touch Sky) — id 1000068
*消耗 Consumable*  
- **Lv1** ⟨template⟩: {attack}攻 / [消耗]  
  *{attack} ATK / [Consumption]*
- **Lv2** ⟨template⟩: {attack}攻 / [消耗]  
  *{attack} ATK / [Consumption]*
- **Lv3** ⟨template⟩: {attack}攻 / [升级]下{otherParams[0]}次使用的云剑 / [消耗]  
  *{attack} ATK / [Upgrade] the next {otherParams[0]} Cloud Swords you play / [Consumption]*


## Sect: 七星阁 Heptastar Pavilion


### Phase 1 — 炼气 Meditation

#### 巽卦 (Wind Hexagram) — id 4000001
- **Lv1**: [灵气]+1 / [卦象]+1  
  *[Qi]+1 / [Hexagram]+1*
- **Lv2**: [灵气]+2 / [卦象]+1  
  *[Qi]+2 / [Hexagram]+1*
- **Lv3**: [灵气]+2 / [卦象]+2  
  *[Qi]+2 / [Hexagram]+2*

#### 坤卦 (Earth Hexagram) — id 4000002
- **Lv1**: [防]+2 / [卦象]+2  
  *[DEF]+2 / [Hexagram]+2*
- **Lv2**: [防]+2 / [卦象]+3  
  *[DEF]+2 / [Hexagram]+3*
- **Lv3**: [防]+2 / [卦象]+4  
  *[DEF]+2 / [Hexagram]+4*

#### 震卦 (Zhen Hexagram) — id 4000003
- **Lv1**: 4攻 / [卦象]+1  
  *4 ATK / [Hexagram]+1*
- **Lv2**: 7攻 / [卦象]+1  
  *7 ATK / [Hexagram]+1*
- **Lv3**: 10攻 / [卦象]+1  
  *10 ATK / [Hexagram]+1*

#### 掌心雷 (Palm Thunder) — id 4000004
- **Lv1**: 2～10攻  
  *2～10 ATK*
- **Lv2**: 5～13攻  
  *5～13 ATK*
- **Lv3**: 8～16攻  
  *8～16 ATK*

#### 白鹤亮翅 (White Crane Bright Wings) — id 4000005
- **Lv1**: 1～8攻 / [灵气]+1  
  *1～8 ATK / [Qi]+1*
- **Lv2**: 1～8攻 / [灵气]+2  
  *1～8 ATK / [Qi]+2*
- **Lv3**: 1～8攻 / [灵气]+3  
  *1～8 ATK / [Qi]+3*

#### 野马分鬃 (Striding Into the Wind) — id 4000006
- **Lv1**: 3攻×2 / [防]+1～10  
  *3 ATK × 2 / [DEF]+1～10*
- **Lv2**: 4攻×2 / [防]+1～12  
  *4 ATK × 2 / [DEF]+1～12*
- **Lv3**: 5攻×2 / [防]+1～14  
  *5 ATK × 2 / [DEF]+1～14*

#### 星罗棋布 (Dotted Around) — id 4000008
- **Lv1**: [灵气]+1 / [防]+2 / [星力]+1  
  *[Qi]+1 / [DEF]+2 / [Star Power]+1*
- **Lv2**: [灵气]+2 / [防]+3 / [星力]+1  
  *[Qi]+2 / [DEF]+3 / [Star Power]+1*
- **Lv3**: [灵气]+2 / [防]+4 / [星力]+2  
  *[Qi]+2 / [DEF]+4 / [Star Power]+2*

#### 星弈·夹 (Astral Move - Flank) — id 4000010
- **Lv1**: 6攻 / [星位]：追加5攻  
  *6 ATK / [Star Point]: Make an additional 5 ATK*
- **Lv2**: 7攻 / [星位]：追加7攻  
  *7 ATK / [Star Point]: Make an additional 7 ATK*
- **Lv3**: 8攻 / [星位]：追加9攻  
  *8 ATK / [Star Point]: Make an additional 9 ATK*

#### 星弈·挡 (Astral Move - Block) — id 4000011
- **Lv1**: 6攻 / [星位]：[防]+2  
  *6 ATK / [Star Point]: [DEF]+2*
- **Lv2**: 8攻 / [星位]：[防]+4  
  *8 ATK / [Star Point]: [DEF]+4*
- **Lv3**: 10攻 / [星位]：[防]+6  
  *10 ATK / [Star Point]: [DEF]+6*

#### 藕断丝连 (Incessant) — id 4000013
- **Lv1**: 6攻 / [后招]：生命+2  
  *6 ATK / [Post Action]: HP+2*
- **Lv2**: 9攻 / [后招]：生命+4  
  *9 ATK / [Post Action]: HP+4*
- **Lv3**: 12攻 / [后招]：生命+6  
  *12 ATK / [Post Action]: HP+6*

#### 斗转星移 (Shifting Stars) — id 4000023
- **Lv1**: 5攻 / 后1格[成为星位]  
  *5 ATK / The next 1 slot(s) in your deck [Become Star Point]*
- **Lv2**: 8攻 / 后1格[成为星位]  
  *8 ATK / The next 1 slot(s) in your deck [Become Star Point]*
- **Lv3**: 8攻 / 后2格[成为星位]  
  *8 ATK / The next 2 slot(s) in your deck [Become Star Point]*

#### 卦灵返生 (Hexagrams Spirit Resurrection) — id 4000047
- **Lv1**: 耗尽卦象和灵气，每点加4生命  
  *Exhaust Hexagram and Qi, add 4 HP for each point exhausted*
- **Lv2**: 耗尽卦象和灵气，每点加5生命  
  *Exhaust Hexagram and Qi, add 5 HP for each point exhausted*
- **Lv3**: 耗尽卦象和灵气，每点加6生命  
  *Exhaust Hexagram and Qi, add 6 HP for each point exhausted*

#### 投石问路 (Throwing Stones For Directions) — id 4000053
- **Lv1**: 6攻 / 施加0～2层[虚弱] / 施加0～2层[破绽]  
  *6 ATK / Apply 0～2 stack(s) of [Weakened] / Apply 0～2 stack(s) of [Flaw]*
- **Lv2**: 6攻 / 施加0～2层[虚弱] / 施加0～3层[破绽]  
  *6 ATK / Apply 0～2 stack(s) of [Weakened] / Apply 0～3 stack(s) of [Flaw]*
- **Lv3**: 6攻 / 施加0～3层[虚弱] / 施加0～3层[破绽]  
  *6 ATK / Apply 0～3 stack(s) of [Weakened] / Apply 0～3 stack(s) of [Flaw]*

#### 揽雀尾 (Sparrow's Tail) — id 4000061
- **Lv1**: 9攻 / 10%概率追加5攻  
  *9 ATK / 10% chance make an additional 5 ATK*
- **Lv2**: 10攻 / 10%概率追加7攻  
  *10 ATK / 10% chance make an additional 7 ATK*
- **Lv3**: 11攻 / 10%概率追加9攻  
  *11 ATK / 10% chance make an additional 9 ATK*

#### 梦·星弈挡 (Dream - Astral Move - Block) — id 4000069
- **Lv1**: 6攻 / [防]+2 / [星位]：每有1[星力]加2[防]  
  *6 ATK / [DEF]+2 / [Star Point]: Add 2 [DEF] for each [Star Power]*
- **Lv2**: 8攻 / [防]+2 / [星位]：每有1[星力]加2[防]  
  *8 ATK / [DEF]+2 / [Star Point]: Add 2 [DEF] for each [Star Power]*
- **Lv3**: 10攻 / [防]+2 / [星位]：每有1[星力]加2[防]  
  *10 ATK / [DEF]+2 / [Star Point]: Add 2 [DEF] for each [Star Power]*

#### 梦·星轨推衍 (Dream - Star Trail Divination) — id 4000070
- **Lv1**: [灵气]+2 / 生命及上限+2 / 耗尽[卦象]，每点加1[星力]  
  *[Qi]+2 / HP and Max HP+2 / Exhaust [Hexagram], then gain 1 [Star Power] for each [Hexagram] exhausted*
- **Lv2**: [灵气]+2 / 生命及上限+4 / 耗尽[卦象]，每点加1[星力]  
  *[Qi]+2 / HP and Max HP+4 / Exhaust [Hexagram], then gain 1 [Star Power] for each [Hexagram] exhausted*
- **Lv3**: [灵气]+2 / 生命及上限+6 / 耗尽[卦象]，每点加1[星力]  
  *[Qi]+2 / HP and Max HP+6 / Exhaust [Hexagram], then gain 1 [Star Power] for each [Hexagram] exhausted*

#### 梦·轰雷掣电 (Dream - Thunder And Lightning) — id 4000071
- **Lv1**: 7攻 / 每有1点[卦象]多1攻  
  *7 ATK / For each [Hexagram] add 1 ATK*
- **Lv2**: 9攻 / 每有1点[卦象]多1攻  
  *9 ATK / For each [Hexagram] add 1 ATK*
- **Lv3**: 2攻×2 / 每有1点[卦象]多1攻  
  *2 ATK×2 / For each [Hexagram] add 1 ATK*

#### 梦·两仪阵 (Dream - Yin Yang Formation) — id 4000072
*持续 Continuous*  
- **Lv1**: [防]+4 / [持续]：每加1[灵气]或[卦象]时加1[防]  
  *[DEF]+4 / [Continuous]: Whenever you gain 1 [Qi] or [Hexagram], gain 1 [DEF]*
- **Lv2**: [持续]：每加1[灵气]或[卦象]时加2[防]  
  *[Continuous]: Whenever you gain 1 [Qi] or [Hexagram], gain 2 [DEF]*
- **Lv3**: [持续]：每加1[灵气]或[卦象]时加1[防]和1生命  
  *[Continuous]: Whenever you gain 1 [Qi] or [Hexagram], gain 1 [DEF] and 1 HP*

#### 梦·落雷术 (Dream - Falling Thunder) — id 4000073
- **Lv1**: 6攻（卡组中每有一张雷牌或卦牌就多1攻）  
  *6 ATK (Gain 1 more ATK for each Thunder or Hexagram card in your deck)*
- **Lv2**: 8攻（卡组中每有一张雷牌或卦牌就多1攻）  
  *8 ATK (Gain 1 more ATK for each Thunder or Hexagram card in your deck)*
- **Lv3**: 10攻（卡组中每有一张雷牌或卦牌就多1攻）  
  *10 ATK (Gain 1 more ATK for each Thunder or Hexagram card in your deck)*

#### 梦·落花有意 (Dream - Flower Sentient) — id 4000074
- **Lv1**: 施加1层[内伤] / [后招]：生命+4  
  *Apply 1 [Internal Injury] / [Post Action]: HP+4*
- **Lv2**: 施加1层[内伤] / [后招]：生命+8  
  *Apply 1 [Internal Injury] / [Post Action]: HP+8*
- **Lv3**: 施加1层[内伤] / [后招]：生命+12  
  *Apply 1 [Internal Injury] / [Post Action]: HP+12*

#### 梦·黄雀在后 (Dream - Hunter Hunting Hunter) — id 4000075
- **Lv1**: 6攻 / 已用过后招牌则追加2攻 / [先机]：反转[出牌方向]  
  *6 ATK / If you have played a Post Action card, make an additional 2 ATK / [First Use]: [Reverse Card Play Direction]*
- **Lv2**: 7攻 / 已用过后招牌则追加3攻 / [先机]：反转[出牌方向]  
  *7 ATK / If you have played a Post Action card, make an additional 3 ATK / [First Use]: [Reverse Card Play Direction]*
- **Lv3**: 8攻 / 已用过后招牌则追加4攻 / [先机]：反转[出牌方向]  
  *8 ATK / If you have played a Post Action card, make an additional 4 ATK / [First Use]: [Reverse Card Play Direction]*

#### 梦·海底捞月 (Dream - Drag Moon In Sea) — id 4000076
- **Lv1**: [后招]：7攻×2  
  *[Post Action]: 7 ATK×2*
- **Lv2**: [后招]：9攻×2  
  *[Post Action]: 9 ATK×2*
- **Lv3**: [后招]：11攻×2  
  *[Post Action]: 11 ATK×2*

#### 梦·反震心法 (Dream - Repel Citta-Dharma) — id 4000078
- **Lv1**: 生命及上限+2 / 受到攻击和[伤害]时减少25%，每减1点对方失去1生命，持续1回合  
  *HP and Max HP+2 / Reduce ATK and [DMG] received by 25%; for each 1 point reduced, the opponent loses 1 HP. Lasts for 1 turns*
- **Lv2**: 生命及上限+4 / 受到攻击和[伤害]时减少25%，每减1点对方失去1生命，持续1回合  
  *HP and Max HP+4 / Reduce ATK and [DMG] received by 25%; for each 1 point reduced, the opponent loses 1 HP. Lasts for 1 turns*
- **Lv3**: 生命及上限+6 / 受到攻击和[伤害]时减少25%，每减1点对方失去1生命，持续1回合  
  *HP and Max HP+6 / Reduce ATK and [DMG] received by 25%; for each 1 point reduced, the opponent loses 1 HP. Lasts for 1 turns*

#### 梦·斗转星移 (Dream - Shifting Stars) — id 4000079
- **Lv1**: [灵气]+1 / [星力]+1 / [被动]：[相邻]格是[星位]  
  *[Qi]+1 / [Star Power]+1 / [Passive]: [Adjacent] slots are [Star Point]*
- **Lv2**: [灵气]+2 / [星力]+1 / [被动]：[相邻]格是[星位]  
  *[Qi]+2 / [Star Power]+1 / [Passive]: [Adjacent] slots are [Star Point]*
- **Lv3**: [灵气]+3 / [星力]+1 / [被动]：[相邻]格是[星位]  
  *[Qi]+3 / [Star Power]+1 / [Passive]: [Adjacent] slots are [Star Point]*

#### 梦·离卦 (Dream - Flame Hexagram) — id 4000080
- **Lv1**: 对方减6生命 / 耗尽[卦象]，每点多减3  
  *Opponent loses 6 HP / Exhaust [Hexagram], for each stack deal 3 more*
- **Lv2**: 对方减8生命 / 耗尽[卦象]，每点多减3  
  *Opponent loses 8 HP / Exhaust [Hexagram], for each stack deal 3 more*
- **Lv3**: 对方减10生命 / 耗尽[卦象]，每点多减3  
  *Opponent loses 10 HP / Exhaust [Hexagram], for each stack deal 3 more*

#### 梦·蜻蜓点水 (Dream - Dance Of The Dragonfly) — id 4000081
- **Lv1**: 2攻 / [卦象]+2  
  *2 ATK / [Hexagram]+2*
- **Lv2**: 4攻 / [卦象]+2  
  *4 ATK / [Hexagram]+2*
- **Lv3**: 6攻 / [卦象]+2  
  *6 ATK / [Hexagram]+2*

#### 梦·杯弓蛇影 (Dream - Snake in Reflection) — id 4000082
- **Lv1**: 生命及上限+2 / 施加1层[内伤]  
  *HP and Max HP+2 / Apply 1 [Internal Injury]*
- **Lv2**: 生命及上限+4 / 施加1层[内伤]  
  *HP and Max HP+4 / Apply 1 [Internal Injury]*
- **Lv3**: 生命及上限+2 / 施加1层[内伤]和1层[虚弱]  
  *HP and Max HP+2 / Apply 1 [Internal Injury] and 1 [Weakened]*

#### 梦·气疗术 (Dream - Qi Therapy) — id 4000083
- **Lv1**: [灵气]+2 / 生命上限+10 / 生命+2  
  *[Qi]+2 / Max HP+10 / HP+2*
- **Lv2**: [灵气]+2 / 生命上限+10 / 生命+4  
  *[Qi]+2 / Max HP+10 / HP+4*
- **Lv3**: [灵气]+2 / 生命上限+10 / 生命+6  
  *[Qi]+2 / Max HP+10 / HP+6*

#### 梦·星罗棋布 (Dream - Dotted Around) — id 4000084
*持续 Continuous*  
- **Lv1**: [持续]1次：使用[非星位]上的牌后加1[灵气]和1[星力]  
  *[Continuous] 1 times: After playing a card on a non-[Star Point], gain 1 [Qi] and 1 [Star Power]*
- **Lv2**: [灵气]+1 / [持续]1次：使用[非星位]上的牌后加1[灵气]和1[星力]  
  *[Qi]+1 / [Continuous] 1 times: After playing a card on a non-[Star Point], gain 1 [Qi] and 1 [Star Power]*
- **Lv3**: [持续]2次：使用[非星位]上的牌后加1[灵气]和1[星力]  
  *[Continuous] 2 times: After playing a card on a non-[Star Point], gain 1 [Qi] and 1 [Star Power]*

#### 梦·白蛇吐信 (Dream - White Snake) — id 4000085
- **Lv1**: 3攻 / 重复1次：从[内伤]、[虚弱]、[外伤]中随机1层施加给对手 / [后招]：多重复1次  
  *3 ATK / Repeat 1 times: Randomly apply 1 stack from [Internal Injury], [Weakened], [Wound] to the opponent / [Post Action]: Repeat 1 more times*
- **Lv2**: 5攻 / 重复1次：从[内伤]、[虚弱]、[外伤]中随机1层施加给对手 / [后招]：多重复1次  
  *5 ATK / Repeat 1 times: Randomly apply 1 stack from [Internal Injury], [Weakened], [Wound] to the opponent / [Post Action]: Repeat 1 more times*
- **Lv3**: 5攻 / 重复1次：从[内伤]、[虚弱]、[外伤]中随机1层施加给对手 / [后招]：多重复2次  
  *5 ATK / Repeat 1 times: Randomly apply 1 stack from [Internal Injury], [Weakened], [Wound] to the opponent / [Post Action]: Repeat 2 more times*

#### 梦·乾卦 (Dream - Heaven Hexagram) — id 4000086
*消耗 Consumable*  
- **Lv1**: [卦象]+2 / [消耗]  
  *[Hexagram]+2 / [Consumption]*
- **Lv2**: [卦象]+3 / [消耗]  
  *[Hexagram]+3 / [Consumption]*
- **Lv3**: [卦象]+4 / [消耗]  
  *[Hexagram]+4 / [Consumption]*

#### 梦·枯木逢春 (Dream - Revitalized) — id 4000087
- **Lv1**: 若用过[梦·枯木逢春]，此牌攻翻倍 / 5攻  
  *If you have played [Dream - Revitalized], this card's ATK is doubled / 5 ATK*
- **Lv2**: 若用过[梦·枯木逢春]，此牌攻翻倍 / 6攻  
  *If you have played [Dream - Revitalized], this card's ATK is doubled / 6 ATK*
- **Lv3**: 若用过[梦·枯木逢春]，此牌攻翻倍 / 8攻  
  *If you have played [Dream - Revitalized], this card's ATK is doubled / 8 ATK*

#### 梦·御雷卦诀 (Dream - Thunder Hexagram Rhythm) — id 4000088
*消耗 Consumable, 持续 Continuous*  
- **Lv1**: 1～10攻 / 加回本场战斗失去的[卦象] / [消耗]  
  *1～10 ATK / Regain all [Hexagram] lost this battle / [Consumption]*
- **Lv2**: 3～12攻 / 加回本场战斗失去的[卦象] / [消耗]  
  *3～12 ATK / Regain all [Hexagram] lost this battle / [Consumption]*
- **Lv3**: 5～14攻 / 加回本场战斗失去的[卦象] / [消耗]  
  *5～14 ATK / Regain all [Hexagram] lost this battle / [Consumption]*

#### 梦·星弈点 (Dream - Astral Move Point) — id 4000089
- **Lv1**: 5攻 / [星位]：施加1层[内伤]  
  *5 ATK / [Star Point]: Apply 1 [Internal Injury]*
- **Lv2**: 3攻 / [星位]：施加2层[内伤]  
  *3 ATK / [Star Point]: Apply 2 [Internal Injury]*
- **Lv3**: 3攻 / [星位]：施加3层[内伤]  
  *3 ATK / [Star Point]: Apply 3 [Internal Injury]*


### Phase 2 — 筑基 Foundation

#### 星弈·立 (Astral Move - Stand) — id 4000009
- **Lv1**: 7攻 / [星位]：[灵气]+1  
  *7 ATK / [Star Point]: [Qi]+1*
- **Lv2**: 8攻 / [星位]：[灵气]+2  
  *8 ATK / [Star Point]: [Qi]+2*
- **Lv3**: 9攻 / [星位]：[灵气]+3  
  *9 ATK / [Star Point]: [Qi]+3*

#### 坎卦 (Water Hexagram) — id 4000015
- **Lv1**: [卦象]+2 / 后1格[成为星位]  
  *[Hexagram]+2 / The next 1 slot in your deck [Become Star Point]*
- **Lv2**: [卦象]+3 / 后1格[成为星位]  
  *[Hexagram]+3 / The next 1 slot in your deck [Become Star Point]*
- **Lv3**: [卦象]+4 / 后1格[成为星位]  
  *[Hexagram]+4 / The next 1 slot in your deck [Become Star Point]*

#### 艮卦 (Mountain Hexagram) — id 4000016
- **Lv1**: [卦象]+2 / 生命及上限+2  
  *[Hexagram]+2 / HP and Max HP+2*
- **Lv2**: [卦象]+3 / 生命及上限+3  
  *[Hexagram]+3 / HP and Max HP+3*
- **Lv3**: [卦象]+4 / 生命及上限+4  
  *[Hexagram]+4 / HP and Max HP+4*

#### 气贯长虹 (Imposing) — id 4000018
- **Lv1**: [灵气]+2 / [后招]：生命+6  
  *[Qi]+2 / [Post Action]: HP+6*
- **Lv2**: [灵气]+3 / [后招]：生命+9  
  *[Qi]+3 / [Post Action]: HP+9*
- **Lv3**: [灵气]+4 / [后招]：生命+12  
  *[Qi]+4 / [Post Action]: HP+12*

#### 斩草除根 (Cutting Weeds) — id 4000019
- **Lv1**: 5攻×2 / 对方减3～13生命上限  
  *5 ATK × 2 / Opponent loses 3～13 Max HP*
- **Lv2**: 7攻×2 / 对方减6～17生命上限  
  *7 ATK × 2 / Opponent loses 6～17 Max HP*
- **Lv3**: 9攻×2 / 对方减9～21生命上限  
  *9 ATK × 2 / Opponent loses 9～21 Max HP*

#### 金鸡独立 (Golden Rooster Independence) — id 4000020
- **Lv1**: 11攻 / 11%概率施加1层[虚弱]  
  *11 ATK / 11% chance to apply 1 stack(s) of [Weakened]*
- **Lv2**: 15攻 / 11%概率施加1层[虚弱]  
  *15 ATK / 11% chance to apply 1 stack(s) of [Weakened]*
- **Lv3**: 15攻 / 11%概率施加2层[虚弱]  
  *15 ATK / 11% chance to apply 2 stack(s) of [Weakened]*

#### 落花有意 (Flower Sentient) — id 4000021
- **Lv1**: 灵气+1 / [防]+1 / 施加1层[内伤]  
  *Qi+1 / [DEF]+1 / Apply 1 stack of [Internal injury]*
- **Lv2**: 灵气+2 / [防]+2 / 施加1层[内伤]  
  *Qi+2 / [DEF]+2 / Apply 1 stack of [Internal injury]*
- **Lv3**: 灵气+3 / [防]+3 / 施加1层[内伤]  
  *Qi+3 / [DEF]+3 / Apply 1 stack of [Internal injury]*

#### 飞星刺 (Astral Fleche) — id 4000024
- **Lv1**: 5攻 / [星力]+1  
  *5 ATK / [Star Power]+1*
- **Lv2**: 5攻 / [星力]+2  
  *5 ATK / [Star Power]+2*
- **Lv3**: 5攻 / [星力]+3  
  *5 ATK / [Star Power]+3*

#### 静气心法 (Stillness Citta-Dharma) — id 4000027
*持续 Continuous*  
- **Lv1**: [持续]：每加1点灵气时加2生命  
  *[Continuous]: Whenever you gain 1 Qi, add 2 HP*
- **Lv2**: [持续]：每加1点灵气时加3生命  
  *[Continuous]: Whenever you gain 1 Qi, add 3 HP*
- **Lv3**: [持续]：每加1点灵气时加4生命  
  *[Continuous]: Whenever you gain 1 Qi, add 4 HP*

#### 星弈·点 (Astral Move - Point) — id 4000028
- **Lv1**: 6攻 / [星位]：对方减1[灵气]  
  *6 ATK / [Star Point]: Opponent loses 1 [Qi]*
- **Lv2**: 10攻 / [星位]：对方减1[灵气]  
  *10 ATK / [Star Point]: Opponent loses 1 [Qi]*
- **Lv3**: 14攻 / [星位]：对方减1[灵气]  
  *14 ATK / [Star Point]: Opponent loses 1 [Qi]*

#### 落雷术 (Falling Thunder) — id 4000030
- **Lv1**: 6～16攻  
  *6～16 ATK*
- **Lv2**: 9～20攻  
  *9～20 ATK*
- **Lv3**: 12～24攻  
  *12～24 ATK*

#### 生机绽放 (Vitality Blossom) — id 4000048
*持续 Continuous*  
- **Lv1**: 生命及上限+7 / [持续]：加生命超过上限时，上限随生命增加  
  *HP and Max HP+7 / [Continuous]: When the added HP exceeds the Max HP, the Max HP increases with the HP*
- **Lv2**: 生命及上限+11 / [持续]：加生命超过上限时，上限随生命增加  
  *HP and Max HP+11 / [Continuous]: When the added HP exceeds the Max HP, the Max HP increases with the HP*
- **Lv3**: 生命及上限+15 / [持续]：加生命超过上限时，上限随生命增加  
  *HP and Max HP+15 / [Continuous]: When the added HP exceeds the Max HP, the Max HP increases with the HP*

#### 星衍诀 (Star Born Rhythm) — id 4000054
- **Lv1**: [星力]+2 / [后招]：[再次行动]  
  *[Star Power]+2 / [Post Action]:[Chase]*
- **Lv2**: [星力]+3 / [后招]：[再次行动]  
  *[Star Power]+3 / [Post Action]:[Chase]*
- **Lv3**: [星力]+4 / [后招]：[再次行动]  
  *[Star Power]+4 / [Post Action]:[Chase]*

#### 望星诀 (Star Gazing Rhythm) — id 4000090
- **Lv1**: [灵气]+2 / [防]+2 / 后2格[成为星位]  
  *[Qi]+2 / [DEF]+2 / The next 2 slots [Become Star Point]*
- **Lv2**: [灵气]+2 / [防]+4 / 后3格[成为星位]  
  *[Qi]+2 / [DEF]+4 / The next 3 slots [Become Star Point]*
- **Lv3**: [灵气]+2 / [防]+6 / 后4格[成为星位]  
  *[Qi]+2 / [DEF]+6 / The next 4 slots [Become Star Point]*


### Phase 3 — 金丹 Virtuoso

#### 气疗术 (Qi Therapy) — id 4000017
- **Lv1**: 生命上限+8 / 生命+8～18  
  *Max HP+8 / HP+8～18*
- **Lv2**: 生命上限+12 / 生命+12～22  
  *Max HP+12 / HP+12～22*
- **Lv3**: 生命上限+16 / 生命+16～26  
  *Max HP+16 / HP+16～26*

#### 流水无情 (Ruthless Water) — id 4000022
- **Lv1**: 6攻 / 若对方有[负面状态]，施加2层[内伤]  
  *6 ATK / If the opponent has [Debuff], then apply 2 stacks of [Internal Injury]*
- **Lv2**: 6攻 / 若对方有[负面状态]，施加3层[内伤]  
  *6 ATK / If the opponent has [Debuff], then apply 3 stacks of [Internal Injury]*
- **Lv3**: 6攻 / 若对方有[负面状态]，施加4层[内伤]  
  *6 ATK / If the opponent has [Debuff], then apply 4 stacks of [Internal Injury]*

#### 兑卦 (Lake Hexagram) — id 4000025
- **Lv1**: [卦象]+2 / 双方加2灵气  
  *[Hexagram]+2 / Both players add 2 Qi*
- **Lv2**: [卦象]+3 / 双方加3灵气  
  *[Hexagram]+3 / Both players add 3 Qi*
- **Lv3**: [卦象]+4 / 双方加4灵气  
  *[Hexagram]+4 / Both players add 4 Qi*

#### 星弈·打 (Astral Move - Hit) — id 4000029
- **Lv1**: 5攻×2 / [星位]：追加5攻  
  *5 ATK × 2 / [Star Point]: Make an additional 5 ATK*
- **Lv2**: 6攻×2 / [星位]：追加7攻  
  *6 ATK × 2 / [Star Point]: Make an additional 7 ATK*
- **Lv3**: 7攻×2 / [星位]：追加9攻  
  *7 ATK × 2 / [Star Point]: Make an additional 9 ATK*

#### 白蛇吐信 (White Snake) — id 4000031
- **Lv1**: 10%概率施加2层[破绽] / 6攻  
  *10% chance to apply 2 stacks of [Flaw] / 6 ATK*
- **Lv2**: 10%概率施加3层[破绽] / 6攻  
  *10% chance to apply 3 stacks of [Flaw] / 6 ATK*
- **Lv3**: 10%概率施加4层[破绽] / 6攻  
  *10% chance to apply 4 stacks of [Flaw] / 6 ATK*

#### 众星拱月 (Starry Moon) — id 4000032
- **Lv1**: [星力]+2 / 后2格[成为星位]  
  *[Star Power]+2 / The next 2 slots in your deck [Become Star Point]*
- **Lv2**: [星力]+3 / 后2格[成为星位]  
  *[Star Power]+3 / The next 2 slots in your deck [Become Star Point]*
- **Lv3**: [星力]+4 / 后2格[成为星位]  
  *[Star Power]+4 / The next 2 slots in your deck [Become Star Point]*

#### 海底捞月 (Drag Moon In Sea) — id 4000033
- **Lv1**: [后招]：12攻，并[再次行动]  
  *[Post Action]: 12 ATK, [Chase]*
- **Lv2**: [后招]：18攻，并[再次行动]  
  *[Post Action]: 18 ATK, [Chase]*
- **Lv3**: [后招]：24攻，并[再次行动]  
  *[Post Action]: 24 ATK, [Chase]*

#### 两仪阵 (Yin Yang Formation) — id 4000040
- **Lv1**: [灵气]+2 / 每点[卦象]加1[防]和1生命  
  *[Qi]+2 / Add 1 [DEF] and 1 HP for each [Hexagram]*
- **Lv2**: [灵气]+3 / 每点[卦象]加2[防]和1生命  
  *[Qi]+3 / Add 2 [DEF] and 1 HP for each [Hexagram]*
- **Lv3**: [灵气]+4 / 每点[卦象]加2[防]和2生命  
  *[Qi]+4 / Add 2 [DEF] and 2 HP for each [Hexagram]*

#### 枯木逢春 (Revitalized) — id 4000042
*derived from: 小还丹*  
- **Lv1**: 10攻 / 每加过5点生命多1攻  
  *10 ATK / Add 1 ATK for each 5 HP have added before*
- **Lv2**: 10攻 / 每加过4点生命多1攻  
  *10 ATK / Add 1 ATK for each 4 HP have added before*
- **Lv3**: 10攻 / 每加过3点生命多1攻  
  *10 ATK / Add 1 ATK for each 3 HP have added before*

#### 螳螂捕蝉 (Hunter Becomes Preyer) — id 4000043
- **Lv1**: 2攻×2 / 生命+4 / [后招]：追加7攻  
  *2 ATK × 2 / HP+4 / [Post Action]: Make an additional 7 ATK*
- **Lv2**: 3攻×2 / 生命+6 / [后招]：追加10攻  
  *3 ATK × 2 / HP+6 / [Post Action]: Make an additional 10 ATK*
- **Lv3**: 4攻×2 / 生命+8 / [后招]：追加13攻  
  *4 ATK × 2 / HP+8 / [Post Action]: Make an additional 13 ATK*

#### 日月争辉 (Sun And Moon For Glory) — id 4000050
- **Lv1**: 造成13[伤害]（生命上限每高对方2点就多1伤害）  
  *Deal 13 [DMG] (For every 2 Max HP higher than your opponent, deal 1 more [DMG])*
- **Lv2**: 造成17[伤害]（生命上限每高对方2点就多1伤害）  
  *Deal 17 [DMG] (For every 2 Max HP higher than your opponent, deal 1 more [DMG])*
- **Lv3**: 造成17[伤害]（生命上限每高对方1点就多1伤害）  
  *Deal 17 [DMG] (For every 1 Max HP higher than your opponent, deal 1 more [DMG])*

#### 一掷乾坤 (All-Or-Nothing) — id 4000055
- **Lv1**: 2～20攻 / [防]+2～20  
  *2～20 ATK / [DEF]+2～20*
- **Lv2**: 8～23攻 / [防]+8～23  
  *8～23 ATK / [DEF]+8～23*
- **Lv3**: 14～26攻 / [防]+14～26  
  *14～26 ATK / [DEF]+14～26*

#### 御雷卦诀 (Thunder Hexagram Rhythm) — id 4000068
- **Lv1**: 1～9攻 / 返还本场战斗中触发过的[卦象]（最多3点）  
  *1～9 ATK / [Hexagram]+X (X is the number of Hexagram triggered in this battle, and up to 3)*
- **Lv2**: 1～10攻 / 返还本场战斗中触发过的[卦象]（最多4点）  
  *1～10 ATK / [Hexagram]+X (X is the number of Hexagram triggered in this battle, and up to 4)*
- **Lv3**: 1～11攻 / 返还本场战斗中触发过的[卦象]（最多5点）  
  *1～11 ATK / [Hexagram]+X (X is the number of Hexagram triggered in this battle, and up to 5)*

#### 犀牛望月 (Rhinoceros Gazing at the Moon) — id 4000091
- **Lv1**: 1～7攻 / 生命及上限+1～7 / 返还此牌触发的[卦象]  
  *1~7 ATK / HP and Max HP+1~7 / Return [Hexagram] triggered by this card*
- **Lv2**: 1～9攻 / 生命及上限+1～9 / 返还此牌触发的[卦象]  
  *1~9 ATK / HP and Max HP+1~9 / Return [Hexagram] triggered by this card*
- **Lv3**: 1～11攻 / 生命及上限+1～11 / 返还此牌触发的[卦象]  
  *1~11 ATK / HP and Max HP+1~11 / Return [Hexagram] triggered by this card*


### Phase 4 — 元婴 Immortality

#### 星弈·长 (Astral Move - Extend) — id 4000007
- **Lv1**: 5攻 / [星位]：生命+1～6  
  *5 ATK / [Star Point]: HP+1～6*
- **Lv2**: 7攻 / [星位]：生命+1～8  
  *7 ATK / [Star Point]: HP+1～8*
- **Lv3**: 9攻 / [星位]：生命+1～10  
  *9 ATK / [Star Point]: HP+1～10*

#### 守株待兔 (Scholasticism) — id 4000012
- **Lv1**: [防]+7 / 1%概率9攻  
  *[DEF]+7 / 1% chance 9 ATK*
- **Lv2**: [防]+10 / 1%概率11攻  
  *[DEF]+10 / 1% chance 11 ATK*
- **Lv3**: [防]+13 / 1%概率13攻  
  *[DEF]+13 / 1% chance 13 ATK*

#### 六爻绝阵 (Hexagram Formacide) — id 4000014
*持续 Continuous · derived from: 飞云丹*  
- **Lv1**: [持续]：每加1点[卦象]时，向对方造成3[伤害]  
  *[Continuous]: Whenever you gain a stack of [Hexagram], deal 3 [DMG] to the opponent*
- **Lv2**: [持续]：每加1点[卦象]时，向对方造成4[伤害]  
  *[Continuous]: Whenever you gain a stack of [Hexagram], deal 4 [DMG] to the opponent*
- **Lv3**: [持续]：每加1点[卦象]时，向对方造成5[伤害]  
  *[Continuous]: Whenever you gain a stack of [Hexagram], deal 5 [DMG] to the opponent*

#### 离卦 (Flame Hexagram) — id 4000034
- **Lv1**: [卦象]+3 / 对方减3生命及上限  
  *[Hexagram]+3 / Opponent loses 3 HP and Max HP*
- **Lv2**: [卦象]+4 / 对方减4生命及上限  
  *[Hexagram]+4 / Opponent loses 4 HP and Max HP*
- **Lv3**: [卦象]+5 / 对方减5生命及上限  
  *[Hexagram]+5 / Opponent loses 5 HP and Max HP*

#### 蜻蜓点水 (Dance Of The Dragonfly) — id 4000035
- **Lv1**: 5攻 / 10%概率[再次行动]  
  *5 ATK / 10% chance to [Chase]*
- **Lv2**: 9攻 / 10%概率[再次行动]  
  *9 ATK / 10% chance to [Chase]*
- **Lv3**: 13攻 / 10%概率[再次行动]  
  *13 ATK / 10% chance to [Chase]*

#### 金蝉脱壳 (Escape Plan) — id 4000036
- **Lv1**: [防]+9 / 生命+9 / [后招]：获得1层[护体]  
  *[DEF]+9 / HP+9 / [Post Action]: Gain 1 stack of [Guard Up]*
- **Lv2**: [防]+12 / 生命+12 / [后招]：获得1层[护体]  
  *[DEF]+12 / HP+12 / [Post Action]: Gain 1 stack of [Guard Up]*
- **Lv3**: [防]+15 / 生命+15 / [后招]：获得1层[护体]  
  *[DEF]+15 / HP+15 / [Post Action]: Gain 1 stack of [Guard Up]*

#### 反震心法 (Repel Citta-Dharma) — id 4000037
*持续 Continuous*  
- **Lv1**: 生命及上限+4 / [持续]：每次受到攻击后，向对方造成2[伤害]  
  *HP and Max HP + 4 / [Continuous]: Whenever you are attacked by the opponent, deal 2 [DMG] to the opponent*
- **Lv2**: 生命及上限+6 / [持续]：每次受到攻击后，向对方造成3[伤害]  
  *HP and Max HP + 6 / [Continuous]: Whenever you are attacked by the opponent, deal 3 [DMG] to the opponent*
- **Lv3**: 生命及上限+8 / [持续]：每次受到攻击后，向对方造成4[伤害]  
  *HP and Max HP + 8 / [Continuous]: Whenever you are attacked by the opponent, deal 4 [DMG] to the opponent*

#### 星弈·飞 (Astral Move - Fly) — id 4000038
*derived from: 锻体丹*  
- **Lv1**: 2攻×2 / [星位]：[再次行动]  
  *2 ATK × 2 / [Star Point]: [Chase]*
- **Lv2**: 4攻×2 / [星位]：[再次行动]  
  *4 ATK × 2 / [Star Point]: [Chase]*
- **Lv3**: 6攻×2 / [星位]：[再次行动]  
  *6 ATK × 2 / [Star Point]: [Chase]*

#### 星弈·虎 (Astral Move - Tiger) — id 4000039
- **Lv1**: 1攻×3 / [星位]：令对方[虚弱]1回合  
  *1 ATK × 3 / [Star Point]: Apply 1 stack(s) of [Weakened]*
- **Lv2**: 1攻×3 / [星位]：令对方[虚弱]2回合  
  *1 ATK × 3 / [Star Point]: Apply 2 stack(s) of [Weakened]*
- **Lv3**: 1攻×3 / [星位]：令对方[虚弱]3回合  
  *1 ATK × 3 / [Star Point]: Apply 3 stack(s) of [Weakened]*

#### 星弈·屠龙 (Astral Move - Dragon Slay) — id 4000051
- **Lv1**: 10攻 / [星位]：此牌受5倍[星力]加成  
  *10 ATK / [Star Point]: This card receives a 5x bonus from [Star Power]*
- **Lv2**: 12攻 / [星位]：此牌受6倍[星力]加成  
  *12 ATK / [Star Point]: This card receives a 6x bonus from [Star Power]*
- **Lv3**: 14攻 / [星位]：此牌受7倍[星力]加成  
  *14 ATK / [Star Point]: This card receives a 7x bonus from [Star Power]*

#### 落花流水 (Flowers And Water) — id 4000056
- **Lv1**: 施加1层[内伤] / 对方每有1层[负面状态]追加1次1攻  
  *Apply 1 stack(s) of [Internal Injury] / Make an additional 1 ATK for each stack of your opponent's [Debuff]*
- **Lv2**: 施加2层[内伤] / 对方每有1层[负面状态]追加1次1攻  
  *Apply 2 stack(s) of [Internal Injury] / Make an additional 1 ATK for each stack of your opponent's [Debuff]*
- **Lv3**: 施加3层[内伤] / 对方每有1层[负面状态]追加1次1攻  
  *Apply 3 stack(s) of [Internal Injury] / Make an additional 1 ATK for each stack of your opponent's [Debuff]*

#### 杯弓蛇影 (Extremely Suspicious) — id 4000059
*derived from: 地灵丹*  
- **Lv1**: 施加2层[内伤] / 令对方的[内伤]立刻生效一次  
  *Apply 2 stacks of [Internal Injury] / Make the opponent's [Internal Injury] take effect once immediately*
- **Lv2**: 施加3层[内伤] / 令对方的[内伤]立刻生效一次  
  *Apply 3 stacks of [Internal Injury] / Make the opponent's [Internal Injury] take effect once immediately*
- **Lv3**: 施加4层[内伤] / 令对方的[内伤]立刻生效一次  
  *Apply 4 stacks of [Internal Injury] / Make the opponent's [Internal Injury] take effect once immediately*

#### 星轨推衍 (Star Trail Divination) — id 4000062
*derived from: 驱邪丹*  
- **Lv1**: [防]+6 / 耗尽[卦象]，每点加1[星力]、1[灵气]和1生命  
  *[DEF]+6 / Exhaust [Hexagram], then gain 1 [Star Power], 1 [Qi] and 1 HP for each [Hexagram] exhausted*
- **Lv2**: [防]+12 / 耗尽[卦象]，每点加1[星力]、1[灵气]和1生命  
  *[DEF]+12 / Exhaust [Hexagram], then gain 1 [Star Power], 1 [Qi] and 1 HP for each [Hexagram] exhausted*
- **Lv3**: [防]+18 / 耗尽[卦象]，每点加1[星力]、1[灵气]和2生命  
  *[DEF]+18 / Exhaust [Hexagram], then gain 1 [Star Power], 1 [Qi] and 2 HP for each [Hexagram] exhausted*

#### 轰雷掣电 (Thunder And Lighting) — id 4000063
- **Lv1**: 重复2次： / 1～10攻 / 有[卦象]生效时加1[灵气]  
  *Repeat twice:  / 1～10 ATK / If a [Hexagram] is triggered add 1 [Qi]*
- **Lv2**: 重复2次： / 1～13攻 / 有[卦象]生效时加1[灵气]  
  *Repeat twice:  / 1～13 ATK / If a [Hexagram] is triggered add 1 [Qi]*
- **Lv3**: 重复2次： / 1～16攻 / 有[卦象]生效时加1[灵气]  
  *Repeat twice:  / 1～16 ATK / If a [Hexagram] is triggered add 1 [Qi]*

#### 雷霆心法 (Thunder Citta-Dharma) — id 4000064
*持续 Continuous*  
- **Lv1**: [卦象]+1 / [持续]：之后名字含“雷”的牌多40%攻  
  *[Hexagram]+1 / [Continuous]: The card containing the name "Thunder" add 40% more ATK*
- **Lv2**: [卦象]+2 / [持续]：之后名字含“雷”的牌多50%攻  
  *[Hexagram]+2 / [Continuous]: The card containing the name "Thunder" add 50% more ATK*
- **Lv3**: [卦象]+3 / [持续]：之后名字含“雷”的牌多60%攻  
  *[Hexagram]+3 / [Continuous]: The card containing the name "Thunder" add 60% more ATK*

#### 伤魂咒阵 (Soul Wound Curse Formation) — id 4000092
*持续 Continuous*  
- **Lv1**: [灵气]+2 / [持续]3次：攻击或受到攻击时，向对方施加1层[内伤]  
  *[Qi]+2 / [Continuous] 3 times: When attacking or being attacked, apply 1 [Internal Injury] to the opponent*
- **Lv2**: [灵气]+2 / [持续]4次：攻击或受到攻击时，向对方施加1层[内伤]  
  *[Qi]+2 / [Continuous] 4 times: When attacking or being attacked, apply 1 [Internal Injury] to the opponent*
- **Lv3**: [灵气]+2 / [持续]5次：攻击或受到攻击时，向对方施加1层[内伤]  
  *[Qi]+2 / [Continuous] 5 times: When attacking or being attacked, apply 1 [Internal Injury] to the opponent*

#### 星弈·长 (Astral Move - Stretch) — id 4000093
- **Lv1**: 2攻 / [星力]+1 / [星位]：生命及上限+4（每有1[星力]多加2）  
  *2 ATK / [Star Power]+1 / [Star Point]: HP and Max HP+4 (2 more for each [Star Power])*
- **Lv2**: 2攻 / [星力]+1 / [星位]：生命及上限+6（每有1[星力]多加3）  
  *2 ATK / [Star Power]+1 / [Star Point]: HP and Max HP+6 (3 more for each [Star Power])*
- **Lv3**: 2攻 / [星力]+1 / [星位]：生命及上限+8（每有1[星力]多加4）  
  *2 ATK / [Star Power]+1 / [Star Point]: HP and Max HP+8 (4 more for each [Star Power])*


### Phase 5 — 化神 Incarnation

#### 乾卦 (Heaven Hexagram) — id 4000026
- **Lv1**: [灵气]+1 / [卦象]+1 / [卦象]≥3则[再次行动]  
  *[Qi]+1 / [Hexagram]+1 / If [Hexagram] is greater or equal to 3, [Chase]*
- **Lv2**: [灵气]+2 / [卦象]+2 / [卦象]≥3则[再次行动]  
  *[Qi]+2 / [Hexagram]+2 / If [Hexagram] is greater or equal to 3, [Chase]*
- **Lv3**: [灵气]+3 / [卦象]+3 / [卦象]≥3则[再次行动]  
  *[Qi]+3 / [Hexagram]+3 / If [Hexagram] is greater or equal to 3, [Chase]*

#### 梅开二度 (Strike Twice) — id 4000041
- **Lv1**: 生命+2 / 下1次使用的牌连续生效两次  
  *HP+2 / The next card will trigger twice*
- **Lv2**: 生命+8 / 下1次使用的牌连续生效两次  
  *HP+8 / The next card will trigger twice*
- **Lv3**: 生命+14 / 下1次使用的牌连续生效两次  
  *HP+14 / The next card will trigger twice*

#### 星弈·断 (Astral Move - Cide) — id 4000044
- **Lv1**: 16攻 / [星位]：对方[跳过]下1张牌  
  *16 ATK / [Star Point]: [Skip] opponent's next card*
- **Lv2**: 22攻 / [星位]：对方[跳过]下1张牌  
  *22 ATK / [Star Point]: [Skip] opponent's next card*
- **Lv3**: 28攻 / [星位]：对方[跳过]下1张牌  
  *28 ATK / [Star Point]: [Skip] opponent's next card*

#### 天元心法 (Polaris Citta-Dharma) — id 4000045
*持续 Continuous · derived from: 培元丹*  
- **Lv1**: [星力]+1 / (此牌在第一格时多加1点) / [持续]：全部格子都是[星位]  
  *[Star Power]+1 (Add 1 more if this card is in the first slot) / [Continuous]: All the slots in you deck are [Star Point]*
- **Lv2**: [星力]+2 / (此牌在第一格时多加1点) / [持续]：全部格子都是[星位]  
  *[Star Power]+2 (Add 1 more if this card is in the first slot) / [Continuous]: All the slots in you deck are [Star Point]*
- **Lv3**: [星力]+3 / (此牌在第一格时多加1点) / [持续]：全部格子都是[星位]  
  *[Star Power]+3 (Add 1 more if this card is in the first slot) / [Continuous]: All the slots in you deck are [Star Point]*

#### 五雷轰顶 (Five Thunders) — id 4000046
- **Lv1**: 重复5次： / 30%概率8攻  
  *Repeat 5 Times:  / 30% chance to 8 ATK*
- **Lv2**: 重复5次： / 30%概率10攻  
  *Repeat 5 Times:  / 30% chance to 10 ATK*
- **Lv3**: 重复5次： / 30%概率12攻  
  *Repeat 5 Times:  / 30% chance to 12 ATK*

#### 先发制人 (Preemptive Strike) — id 4000049
*持续 Continuous*  
- **Lv1**: 4攻 / [持续]：[后招]可在首次使用时触发  
  *4 ATK / [Continuous]: [Post Action] can be triggered when first time play it*
- **Lv2**: 10攻 / [持续]：[后招]可在首次使用时触发  
  *10 ATK / [Continuous]: [Post Action] can be triggered when first time play it*
- **Lv3**: 16攻 / [持续]：[后招]可在首次使用时触发  
  *16 ATK / [Continuous]: [Post Action] can be triggered when first time play it*

#### 铁树开花 (Thin On The Ground) — id 4000057
*消耗 Consumable*  
- **Lv1**: 生命上限永久+2 / 生命+15 / 1%概率此牌效果加倍 / [消耗]  
  *Max HP+2 in this game / HP+15 / 1% chance to get doubled effect / [Consumption]*
- **Lv2**: 生命上限永久+3 / 生命+20 / 1%概率此牌效果加倍 / [消耗]  
  *Max HP+3 in this game / HP+20 / 1% chance to get doubled effect / [Consumption]*
- **Lv3**: 生命上限永久+4 / 生命+25 / 1%概率此牌效果加倍 / [消耗]  
  *Max HP+4 in this game / HP+25 / 1% chance to get doubled effect / [Consumption]*

#### 气吞山河 (Great Spirit) — id 4000060
- **Lv1**: 生命上限+12 / [再次行动] / [后招]：生命+24  
  *Max HP+12 / [Chase] / [Post Action]: HP+24*
- **Lv2**: 生命上限+16 / [再次行动] / [后招]：生命+31  
  *Max HP+16 / [Chase] / [Post Action]: HP+31*
- **Lv3**: 生命上限+20 / [再次行动] / [后招]：生命+38  
  *Max HP+20 / [Chase] / [Post Action]: HP+38*

#### 流星天陨 (Meteorite Meteor) — id 4000065
- **Lv1**: 失去全部[星力]，每点重复1次：向对方造成8[伤害]  
  *Lost all [Star Power], for each: Deal 8 [DMG] to the opponent*
- **Lv2**: 失去全部[星力]，每点重复1次：向对方造成9[伤害]  
  *Lost all [Star Power], for each: Deal 9 [DMG] to the opponent*
- **Lv3**: 失去全部[星力]，每点重复1次：向对方造成10[伤害]  
  *Lost all [Star Power], for each: Deal 10 [DMG] to the opponent*

#### 黄雀在后 (Hunter Hunting Hunter) — id 4000066
*持续 Continuous*  
- **Lv1**: 反转自身[出牌方向] / [持续]：使用含“后招”的牌后追加7攻  
  *Reverse self [Card Play Direction] / [Continuous]: All cards with "Post Action" will make an additional 7 ATK after being played*
- **Lv2**: 反转自身[出牌方向] / [持续]：使用含“后招”的牌后追加10攻  
  *Reverse self [Card Play Direction] / [Continuous]: All cards with "Post Action" will make an additional 10 ATK after being played*
- **Lv3**: 反转自身[出牌方向] / [持续]：使用含“后招”的牌后追加13攻  
  *Reverse self [Card Play Direction] / [Continuous]: All cards with "Post Action" will make an additional 13 ATK after being played*

#### 紫气东来 (Propitious Omen) — id 4000067
- **Lv1**: [灵气]+2 / [灵气]、[卦象]、[星力]中最高者加3（相同时取靠前者）  
  *[Qi]+2 / Add 3 to the largest stack of: [Qi], [Hexagram] or [Star Power] (if there is a tie, add to the former)*
- **Lv2**: [灵气]+2 / [灵气]、[卦象]、[星力]中最高者加5（相同时取靠前者）  
  *[Qi]+2 / Add 5 to the largest stack of: [Qi], [Hexagram] or [Star Power] (if there is a tie, add to the former)*
- **Lv3**: [灵气]+2 / [灵气]、[卦象]、[星力]中最高者加7（相同时取靠前者）  
  *[Qi]+2 / Add 7 to the largest stack of: [Qi], [Hexagram] or [Star Power] (if there is a tie, add to the former)*

#### 星弈·劫争 (Astral Move - Ko Fight) — id 4000094
- **Lv1**: 1攻 / [灵气]+1 / 自身[灵气]＞对方则施加1层[破绽] / [星位]：若[星力]≥2则[再次行动]  
  *1 ATK / [Qi]+1 / If your [Qi] > opponent's, apply 1 stack(s) of [Flaw] / [Star Point]: [Chase] if [Star Power] ≥ 2*
- **Lv2**: 6攻 / [灵气]+1 / 自身[灵气]＞对方则施加1层[破绽] / [星位]：若[星力]≥2则[再次行动]  
  *6 ATK / [Qi]+1 / If your [Qi] > opponent's, apply 1 stack(s) of [Flaw] / [Star Point]: [Chase] if [Star Power] ≥ 2*
- **Lv3**: 6攻 / [灵气]+2 / 自身[灵气]＞对方则施加1层[破绽] / [星位]：若[星力]≥2则[再次行动]  
  *6 ATK / [Qi]+2 / If your [Qi] > opponent's, apply 1 stack(s) of [Flaw] / [Star Point]: [Chase] if [Star Power] ≥ 2*

#### 灵蛇绕柱 (Spirit Snake Coiling Pillar) — id 4000095
- **Lv1**: 施加1层[内伤] / [防]+1（对方每有1层[负面状态]多1，合计最多为5） / [防]≥5则[再次行动]  
  *Apply 1 stack(s) of [Internal Injury] / [DEF]+1 (1 more for each [Debuff] on the opponent) / If [DEF] ≥ 5, [Chase]*
- **Lv2**: 施加2层[内伤] / [防]+2（对方每有1层[负面状态]多1，合计最多为10） / [防]≥5则[再次行动]  
  *Apply 2 stack(s) of [Internal Injury] / [DEF]+2 (1 more for each [Debuff] on the opponent) / If [DEF] ≥ 5, [Chase]*
- **Lv3**: 施加3层[内伤] / [防]+3（对方每有1层[负面状态]多1，合计最多为15） / [防]≥5则[再次行动]  
  *Apply 3 stack(s) of [Internal Injury] / [DEF]+3 (1 more for each [Debuff] on the opponent) / If [DEF] ≥ 5, [Chase]*

#### 折枝点穴 (Branch Break Acupressure) — id 4000096
- **Lv1**: 每次攻击时施加1[内伤]，持续2回合 / 2攻 / 10%概率追加2攻×2 / 10%概率施加1[减攻]  
  *Each of your attacks applies 1 [Internal Injury] for 2 turns / 2 ATK × 1 / 10% chance to make an additional 2 ATK / 10% chance to apply 1 [Decrease ATK]*
- **Lv2**: 每次攻击时施加1[内伤]，持续2回合 / 2攻×2 / 10%概率追加2攻×2 / 10%概率施加1[减攻]  
  *Each of your attacks applies 1 [Internal Injury] for 2 turns / 2 ATK × 2 / 10% chance to make an additional 2 ATK / 10% chance to apply 1 [Decrease ATK]*
- **Lv3**: 每次攻击时施加1[内伤]，持续2回合 / 2攻×3 / 10%概率追加2攻×2 / 10%概率施加1[减攻]  
  *Each of your attacks applies 1 [Internal Injury] for 2 turns / 2 ATK × 3 / 10% chance to make an additional 2 ATK / 10% chance to apply 1 [Decrease ATK]*

#### 弯弓射虎 (Drawing the Bow at the Tiger) — id 4000097
- **Lv1**: [先机]：生命及上限+16 / [后招]：8攻（每加过4生命多1攻） / 10%概率[再次行动]  
  *[First Use]: HP and Max HP+16 / [Post Action]: 8 ATK (1 more ATK for each 4 HP added) / 10% chance to [Chase]*
- **Lv2**: [先机]：生命及上限+24 / [后招]：8攻（每加过4生命多1攻） / 10%概率[再次行动]  
  *[First Use]: HP and Max HP+24 / [Post Action]: 8 ATK (1 more ATK for each 4 HP added) / 10% chance to [Chase]*
- **Lv3**: [先机]：生命及上限+32 / [后招]：8攻（每加过4生命多1攻） / 10%概率[再次行动]  
  *[First Use]: HP and Max HP+32 / [Post Action]: 8 ATK (1 more ATK for each 4 HP added) / 10% chance to [Chase]*

#### 极·静气心法 (Ultimate - Stillness Citta-Dharma) — id 4000098
*持续 Continuous*  
- **Lv1**: 生命上限+20 / [再次行动] / [持续]：每加1点灵气时加1生命  
  *Max HP+20 / [Chase] / [Continuous]: Whenever you gain 1 Qi, heal 1 HP*
- **Lv2**: 生命上限+20 / [再次行动] / [持续]：每加1点灵气时加2生命  
  *Max HP+20 / [Chase] / [Continuous]: Whenever you gain 1 Qi, heal 2 HP*
- **Lv3**: 生命上限+20 / [再次行动] / [持续]：每加1点灵气时加3生命  
  *Max HP+20 / [Chase] / [Continuous]: Whenever you gain 1 Qi, heal 3 HP*

#### 极·两仪阵 (Ultimate - Yin Yang Formation) — id 4000099
- **Lv1**: [灵气]+2 / 卦象+2 / 每点[卦象]加2[防]和2生命  
  *[Qi]+2 / [Hexagram]+2 / Add 2 [DEF] and 2 HP for each [Hexagram]*
- **Lv2**: [灵气]+2 / 卦象+3 / 每点[卦象]加2[防]和2生命  
  *[Qi]+2 / [Hexagram]+3 / Add 2 [DEF] and 2 HP for each [Hexagram]*
- **Lv3**: [灵气]+2 / 卦象+4 / 每点[卦象]加2[防]和2生命  
  *[Qi]+2 / [Hexagram]+4 / Add 2 [DEF] and 2 HP for each [Hexagram]*


### Phase 6 — 特殊 Special

#### 移花接木 (Covert Shift) — id 4000052
- **Lv1**: 下2次生命损失反转为加生命  
  *Reduce HP is reversed to add HP for next 2 times*
- **Lv2**: 下3次生命损失反转为加生命  
  *Reduce HP is reversed to add HP for next 3 times*
- **Lv3**: 下4次生命损失反转为加生命  
  *Reduce HP is reversed to add HP for next 4 times*

#### 天命劫 (Destiny Catastrophe) — id 4000058
- **Lv1**: 若自身[卦象]正好为8点，将对方生命变为8  
  *If your [Hexagram] is exactly 8 stacks, change your opponent's HP to 8*
- **Lv2**: 若自身[卦象]正好为8点，将对方生命变为4  
  *If your [Hexagram] is exactly 8 stacks, change your opponent's HP to 4*
- **Lv3**: 若自身[卦象]正好为8点，将对方生命变为1  
  *If your [Hexagram] is exactly 8 stacks, change your opponent's HP to 1*


### Phase 0 — ?

#### 梦·流水无情 (Dream - Ruthless Water) — id 4000077
- **Lv1** ⟨template⟩: 对方减{otherParams[0]}生命 / 对方每失去过一次生命就多减{otherParams[1]}点  
  *Opponent loses {otherParams[0]} HP / For each time the opponent has lost HP, reduce {otherParams[1]} more*
- **Lv2** ⟨template⟩: 对方减{otherParams[0]}生命 / 对方每失去过一次生命就多减{otherParams[1]}点  
  *Opponent loses {otherParams[0]} HP / For each time the opponent has lost HP, reduce {otherParams[1]} more*
- **Lv3** ⟨template⟩: 对方减{otherParams[0]}生命 / 对方每失去过一次生命就多减{otherParams[1]}点  
  *Opponent loses {otherParams[0]} HP / For each time the opponent has lost HP, reduce {otherParams[1]} more*


## Sect: 五行道盟 Five Elements Alliance


### Phase 1 — 炼气 Meditation

#### 金灵印 (Metal Spirit Seal) — id 7000001
- **Lv1**: 6攻 / [激活金灵]  
  *6 ATK / [Activate Metal Spirit]*
- **Lv2**: 9攻 / [激活金灵]  
  *9 ATK / [Activate Metal Spirit]*
- **Lv3**: 12攻 / [激活金灵]  
  *12 ATK / [Activate Metal Spirit]*

#### 金灵·针 (Metal Spirit - Needle) — id 7000002
- **Lv1**: 6攻 / [金灵]：[锋锐]+2  
  *6 ATK / [Metal Spirit]: [Penetrate]+2*
- **Lv2**: 7攻 / [金灵]：[锋锐]+4  
  *7 ATK / [Metal Spirit]: [Penetrate]+4*
- **Lv3**: 8攻 / [金灵]：[锋锐]+6  
  *8 ATK / [Metal Spirit]: [Penetrate]+6*

#### 木灵印 (Wood Spirit Seal) — id 7000003
- **Lv1**: [灵气]+1 / 生命+4 / [激活木灵]  
  *[Qi]+1 / HP+4 / [Activate Wood Spirit]*
- **Lv2**: [灵气]+2 / 生命+4 / [激活木灵]  
  *[Qi]+2 / HP+4 / [Activate Wood Spirit]*
- **Lv3**: [灵气]+3 / 生命+4 / [激活木灵]  
  *[Qi]+3 / HP+4 / [Activate Wood Spirit]*

#### 木灵·芽 (Wood Spirit - Bud) — id 7000004
- **Lv1**: 3攻×2 / [木灵]：生命+5  
  *3 ATK × 2 / [Wood Spirit]: HP+5*
- **Lv2**: 3攻×3 / [木灵]：生命+5  
  *3 ATK × 3 / [Wood Spirit]: HP+5*
- **Lv3**: 3攻×4 / [木灵]：生命+5  
  *3 ATK × 4 / [Wood Spirit]: HP+5*

#### 水灵印 (Water Spirit Seal) — id 7000006
- **Lv1**: [灵气]+2 / [激活水灵]  
  *[Qi]+2 / [Activate Water Spirit]*
- **Lv2**: [灵气]+3 / [激活水灵]  
  *[Qi]+3 / [Activate Water Spirit]*
- **Lv3**: [灵气]+4 / [激活水灵]  
  *[Qi]+4 / [Activate Water Spirit]*

#### 水灵·涛 (Water Spirit - Waves) — id 7000007
- **Lv1**: 10攻 / [水灵]：获得1层[水势]  
  *10 ATK / [Water Spirit]: Gain 1 stack of [Force of Water]*
- **Lv2**: 13攻 / [水灵]：获得1层[水势]  
  *13 ATK / [Water Spirit]: Gain 1 stack of [Force of Water]*
- **Lv3**: 16攻 / [水灵]：获得1层[水势]  
  *16 ATK / [Water Spirit]: Gain 1 stack of [Force of Water]*

#### 水灵·润物 (Water Spirit - Cleanse) — id 7000008
- **Lv1**: 6攻 / [水灵]：生命+2  
  *6 ATK / [Water Spirit]: HP+2*
- **Lv2**: 8攻 / [水灵]：生命+3  
  *8 ATK / [Water Spirit]: HP+3*
- **Lv3**: 10攻 / [水灵]：生命+4  
  *10 ATK / [Water Spirit]: HP+4*

#### 火灵印 (Fire Spirit Seal) — id 7000009
*derived from: 水气符*  
- **Lv1**: [灵气]+1 / 对方减3生命及上限 / [激活火灵]  
  *[Qi]+1 / Opponent loses 3 HP and Max HP / [Activate Fire Spirit]*
- **Lv2**: [灵气]+2 / 对方减3生命及上限 / [激活火灵]  
  *[Qi]+2 / Opponent loses 3 HP and Max HP / [Activate Fire Spirit]*
- **Lv3**: [灵气]+3 / 对方减3生命及上限 / [激活火灵]  
  *[Qi]+3 / Opponent loses 3 HP and Max HP / [Activate Fire Spirit]*

#### 火灵·窜 (Fire Spirit - Rush) — id 7000010
- **Lv1**: 9攻 / [火灵]：追加2攻  
  *9 ATK / [Fire Spirit]: Make an additional 2 ATK*
- **Lv2**: 11攻 / [火灵]：追加3攻  
  *11 ATK / [Fire Spirit]: Make an additional 3 ATK*
- **Lv3**: 13攻 / [火灵]：追加4攻  
  *13 ATK / [Fire Spirit]: Make an additional 4 ATK*

#### 土灵印 (Earth Spirit Seal) — id 7000011
- **Lv1**: 3攻 / [防]+4 / [激活土灵]  
  *3 ATK / [DEF]+4 / [Activate Earth Spirit]*
- **Lv2**: 5攻 / [防]+6 / [激活土灵]  
  *5 ATK / [DEF]+6 / [Activate Earth Spirit]*
- **Lv3**: 7攻 / [防]+8 / [激活土灵]  
  *7 ATK / [DEF]+8 / [Activate Earth Spirit]*

#### 土灵·碎 (Earth Spirit - Smash) — id 7000013
- **Lv1**: 6攻 / [土灵]：若自身或对方防>0则多3攻  
  *6 ATK / [Earth Spirit]: If either you or your opponent have DEF greater than 0, increase ATK by 3*
- **Lv2**: 7攻 / [土灵]：若自身或对方防>0则多5攻  
  *7 ATK / [Earth Spirit]: If either you or your opponent have DEF greater than 0, increase ATK by 5*
- **Lv3**: 8攻 / [土灵]：若自身或对方防>0则多7攻  
  *8 ATK / [Earth Spirit]: If either you or your opponent have DEF greater than 0, increase ATK by 7*

#### 混元守护 (Cosmos Guard) — id 7000054
- **Lv1**: [防]+6 / 若已激活至少2种[五行]，再加6生命及上限  
  *[DEF]+6 / If at least 2 types of [Five Elements] have been activated, add 6 HP and Max HP*
- **Lv2**: [防]+9 / 若已激活至少2种[五行]，再加9生命及上限  
  *[DEF]+9 / If at least 2 types of [Five Elements] have been activated, add 9 HP and Max HP*
- **Lv3**: [防]+12 / 若已激活至少2种[五行]，再加12生命及上限  
  *[DEF]+12 / If at least 2 types of [Five Elements] have been activated, add 12 HP and Max HP*

#### 五行刺 (Five Elements Fleche) — id 7000060
- **Lv1**: 5攻 / 若已激活任意[五行]则多3攻  
  *5 ATK / If any [Five Elements] has been activated, increase 3 ATK*
- **Lv2**: 5攻 / 若已激活任意[五行]则多6攻  
  *5 ATK / If any [Five Elements] has been activated, increase 6 ATK*
- **Lv3**: 5攻 / 若已激活任意[五行]则多9攻  
  *5 ATK / If any [Five Elements] has been activated, increase 9 ATK*

#### 木灵秘印 (Wood Spirit Secret Seal) — id 7000068
- **Lv1**: 获得2层[加攻] / [激活木灵]  
  *Gain 2 stacks of [Increase ATK] / [Activate Wood Spirit]*
- **Lv2**: 获得2层[加攻] / 生命及上限+4 / [激活木灵]  
  *Gain 2 stacks of [Increase ATK] / HP and Max HP+4 / [Activate Wood Spirit]*
- **Lv3**: 获得2层[加攻] / 生命及上限+8 / [激活木灵]  
  *Gain 2 stacks of [Increase ATK] / HP and Max HP+8 / [Activate Wood Spirit]*

#### 火灵秘印 (Fire Spirit Secret Seal) — id 7000069
- **Lv1**: 对方减8生命及上限 / [激活火灵]  
  *Opponent loses 8 HP and Max HP / [Activate Fire Spirit]*
- **Lv2**: 对方减12生命及上限 / [激活火灵]  
  *Opponent loses 12 HP and Max HP / [Activate Fire Spirit]*
- **Lv3**: 对方减16生命及上限 / [激活火灵]  
  *Opponent loses 16 HP and Max HP / [Activate Fire Spirit]*

#### 土灵秘印 (Earth Spirit Secret Seal) — id 7000070
- **Lv1**: [防]+6 / 下回合再加6[防] / [激活土灵]  
  *[DEF]+6 / Add 6 [DEF] in the next turn / [Activate Earth Spirit]*
- **Lv2**: [防]+9 / 下回合再加9[防] / [激活土灵]  
  *[DEF]+9 / Add 9 [DEF] in the next turn / [Activate Earth Spirit]*
- **Lv3**: [防]+12 / 下回合再加12[防] / [激活土灵]  
  *[DEF]+12 / Add 12 [DEF] in the next turn / [Activate Earth Spirit]*

#### 金灵秘印 (Metal Spirit Secret Seal) — id 7000071
- **Lv1**: [锋锐]+8 / [激活金灵]  
  *[Penetrate]+8 / [Activate Metal Spirit]*
- **Lv2**: [锋锐]+11 / [激活金灵]  
  *[Penetrate]+11 / [Activate Metal Spirit]*
- **Lv3**: [锋锐]+14 / [激活金灵]  
  *[Penetrate]+14 / [Activate Metal Spirit]*

#### 水灵秘印 (Water Spirit Secret Seal) — id 7000072
- **Lv1**: 获得2层[水势] / [激活水灵]  
  *Gain 2 stacks of [Force of Water] / [Activate Water Spirit]*
- **Lv2**: 获得3层[水势] / [激活水灵]  
  *Gain 3 stacks of [Force of Water] / [Activate Water Spirit]*
- **Lv3**: 获得4层[水势] / [激活水灵]  
  *Gain 4 stacks of [Force of Water] / [Activate Water Spirit]*

#### 梦·金灵阵 (Dream - Metal Spirit Formation) — id 7000074
*持续 Continuous*  
- **Lv1**: [激活金灵] / [锋锐]+7  
  *[Activate Metal Spirit] / [Penetrate]+7*
- **Lv2**: [激活金灵] / [锋锐]+8  
  *[Activate Metal Spirit] / [Penetrate]+8*
- **Lv3**: [激活金灵] / [锋锐]+10  
  *[Activate Metal Spirit] / [Penetrate]+10*

#### 梦·浑天印 (Dream - Cosmos Seal) — id 7000075
- **Lv1**: [灵气]+1 / 造成5点[伤害] / [被动]：[相邻]牌使用时先[激活]其所属[五行]  
  *[Qi]+1 / Deal 5 [DMG] / [Passive]: When [Adjacent] cards are played, first [Activate] their corresponding [Five Elements]*
- **Lv2**: [灵气]+1 / 造成7点[伤害] / [被动]：[相邻]牌使用时先[激活]其所属[五行]  
  *[Qi]+1 / Deal 7 [DMG] / [Passive]: When [Adjacent] cards are played, first [Activate] their corresponding [Five Elements]*
- **Lv3**: [灵气]+1 / 造成9点[伤害] / [被动]：[相邻]牌使用时先[激活]其所属[五行]  
  *[Qi]+1 / Deal 9 [DMG] / [Passive]: When [Adjacent] cards are played, first [Activate] their corresponding [Five Elements]*

#### 梦·水灵波澜 (Dream - Water Spirit Billows) — id 7000076
- **Lv1**: [灵气]+1 / 获得1层[水势]  
  *[Qi]+1 / Gain 1 [Force of Water]*
- **Lv2**: [灵气]+1 / 生命及上限+2 / 获得1层[水势]  
  *[Qi]+1 / HP and Max HP+2 / Gain 1 [Force of Water]*
- **Lv3**: [灵气]+1 / 生命及上限+2 / 获得2层[水势]  
  *[Qi]+1 / HP and Max HP+2 / Gain 2 [Force of Water]*

#### 梦·五行刺 (Dream - Five Elements Fleche) — id 7000077
- **Lv1**: 6攻 / 卡组中每有1种[五行]加1[防]  
  *6 ATK / For each type of [Five Elements] in your deck, gain 1 [DEF]*
- **Lv2**: 6攻 / 卡组中每有1种[五行]加2[防]  
  *6 ATK / For each type of [Five Elements] in your deck, gain 2 [DEF]*
- **Lv3**: 6攻 / 卡组中每有1种[五行]加3[防]  
  *6 ATK / For each type of [Five Elements] in your deck, gain 3 [DEF]*

#### 梦·混元无极阵 (Dream - Primordial Infinity Formation) — id 7000078
- **Lv1**: 使用后一格牌对应的1级[五行灵印]  
  *Play the Lv.1 [Five Elements Spirit Seal] corresponding to the next slot's card*
- **Lv2**: 使用后一格牌对应的2级[五行灵印]  
  *Play the Lv.2 [Five Elements Spirit Seal] corresponding to the next slot's card*
- **Lv3**: 使用后一格牌对应的3级[五行灵印]  
  *Play the Lv.3 [Five Elements Spirit Seal] corresponding to the next slot's card*

#### 梦·水灵泉涌 (Dream - Water Spirit Spring) — id 7000079
- **Lv1**: 本场战斗每[击伤]过对方8生命就获得1层[水势] / [开局]：[灵气]+1  
  *This battle, for every 8 HP [Injured] to the opponent, gain 1 [Force of Water] / [Opening]: [Qi]+1*
- **Lv2**: 本场战斗每[击伤]过对方7生命就获得1层[水势] / [开局]：[灵气]+1  
  *This battle, for every 7 HP [Injured] to the opponent, gain 1 [Force of Water] / [Opening]: [Qi]+1*
- **Lv3**: 本场战斗每[击伤]过对方6生命就获得1层[水势] / [开局]：[灵气]+1  
  *This battle, for every 6 HP [Injured] to the opponent, gain 1 [Force of Water] / [Opening]: [Qi]+1*

#### 梦·木灵柳纷飞 (Dream - Wood Spirit Willow Leaf) — id 7000080
- **Lv1**: 生命+6 / 每有1层[水势]，下次攻击就多1攻  
  *HP+6 / For each stack of [Force of Water], the next attack gains 1 ATK*
- **Lv2**: 生命+8 / 每有1层[水势]，下次攻击就多1攻  
  *HP+8 / For each stack of [Force of Water], the next attack gains 1 ATK*
- **Lv3**: 生命+10 / 每有1层[水势]，下次攻击就多1攻  
  *HP+10 / For each stack of [Force of Water], the next attack gains 1 ATK*

#### 梦·木灵阵 (Dream - Wood Spirit Formation) — id 7000081
*持续 Continuous*  
- **Lv1**: [激活木灵] / [灵气]+1 / [持续]3次：攻击时吸取对方1生命  
  *[Activate Wood Spirit] / [Qi]+1 / [Continuous] 3 times: When attacking, steal 1 HP from the opponent*
- **Lv2**: [激活木灵] / [灵气]+1 / [持续]4次：攻击时吸取对方1生命  
  *[Activate Wood Spirit] / [Qi]+1 / [Continuous] 4 times: When attacking, steal 1 HP from the opponent*
- **Lv3**: [激活木灵] / [灵气]+1 / [持续]5次：攻击时吸取对方1生命  
  *[Activate Wood Spirit] / [Qi]+1 / [Continuous] 5 times: When attacking, steal 1 HP from the opponent*

#### 梦·火灵灼心 (Dream - Fire Spirit Heart Fire) — id 7000082
- **Lv1**: 6攻 / 对方每减少过一次生命上限就多1攻  
  *6 ATK / Gain 1 extra ATK for each time the opponent has lost Max HP*
- **Lv2**: 8攻 / 对方每减少过一次生命上限就多1攻  
  *8 ATK / Gain 1 extra ATK for each time the opponent has lost Max HP*
- **Lv3**: 10攻 / 对方每减少过一次生命上限就多1攻  
  *10 ATK / Gain 1 extra ATK for each time the opponent has lost Max HP*

#### 梦·火灵瞬燃 (Dream - Fire Spirit Flash Fire) — id 7000083
- **Lv1**: 对方减6生命及上限（每有3[防]多减1点）  
  *Opponent loses 6 HP and Max HP (lose 1 more for every 3 [DEF] you have)*
- **Lv2**: 对方减8生命及上限（每有3[防]多减1点）  
  *Opponent loses 8 HP and Max HP (lose 1 more for every 3 [DEF] you have)*
- **Lv3**: 对方减8生命及上限（每有2[防]多减1点）  
  *Opponent loses 8 HP and Max HP (lose 1 more for every 2 [DEF] you have)*

#### 梦·金灵铁骨 (Dream - Metal Spirit Iron Bone) — id 7000084
- **Lv1**: [防]+8（每加过2[锋锐]或1[水势]多加1[防]）  
  *[DEF]+8 (For every 2 [Penetrate] or 1 [Force of Water] gained, add 1 more [DEF])*
- **Lv2**: [防]+11（每加过2[锋锐]或1[水势]多加1[防]）  
  *[DEF]+11 (For every 2 [Penetrate] or 1 [Force of Water] gained, add 1 more [DEF])*
- **Lv3**: [防]+14（每加过2[锋锐]或1[水势]多加1[防]）  
  *[DEF]+14 (For every 2 [Penetrate] or 1 [Force of Water] gained, add 1 more [DEF])*

#### 梦·金灵锋芒 (Dream - Metal Spirit Sharp) — id 7000085
- **Lv1**: 2攻 / [灵气]+1 / [击伤]：获得1层[水势]  
  *2 ATK / [Qi]+1 / [Injured]: Gain 1 [Force of Water]*
- **Lv2**: 4攻 / [灵气]+1 / [击伤]：获得1层[水势]  
  *4 ATK / [Qi]+1 / [Injured]: Gain 1 [Force of Water]*
- **Lv3**: 4攻 / [灵气]+2 / [击伤]：获得1层[水势]  
  *4 ATK / [Qi]+2 / [Injured]: Gain 1 [Force of Water]*

#### 梦·土灵绝壁 (Dream - Earth Spirit Steep) — id 7000086
- **Lv1**: [防]+6 / 下回合开始时加4[防]  
  *[DEF]+6 / At the start of next turn add 4 [DEF]*
- **Lv2**: [防]+8 / 下回合开始时加6[防]  
  *[DEF]+8 / At the start of next turn add 6 [DEF]*
- **Lv3**: [防]+10 / 下回合开始时加8[防]  
  *[DEF]+10 / At the start of next turn add 8 [DEF]*

#### 梦·五行天髓诀 (Dream - Five Elements Heavenly Marrow Rhythm) — id 7000087
*持续 Continuous*  
- **Lv1**: 生命及上限+2 / [持续]1[次]：使用[灵印]或[灵阵]后加10[身法]  
  *HP and Max HP+2 / [Continuous] 1 time: After playing a [Spirit Seal] or [Spirit Formation], gain 10 [Agility]*
- **Lv2**: 生命及上限+4 / [持续]1[次]：使用[灵印]或[灵阵]后加10[身法]  
  *HP and Max HP+4 / [Continuous] 1 time: After playing a [Spirit Seal] or [Spirit Formation], gain 10 [Agility]*
- **Lv3**: [持续]2[次]：使用[灵印]或[灵阵]后加10[身法]  
  *[Continuous] 2 times: After playing a [Spirit Seal] or [Spirit Formation], gain 10 [Agility]*

#### 梦·木灵芽 (Dream - Wood Spirit Bud) — id 7000088
- **Lv1**: 3攻×2 / 加过生命则多1攻  
  *3 ATK×2 / If HP has been added, +1 ATK*
- **Lv2**: 4攻×2 / 加过生命则多1攻  
  *4 ATK×2 / If HP has been added, +1 ATK*
- **Lv3**: 5攻×2 / 每加过8生命多1攻  
  *5 ATK×2 / For every 8 HP added, +1 ATK*

#### 梦·火灵聚炎 (Dream - Fire Spirit Flame Eater) — id 7000089
*消耗 Consumable*  
- **Lv1**: [灵气]+1 / 减对方5生命及上限 / [先机]：双方使用下张牌时将其[消耗]  
  *[Qi]+1 / Opponent loses 5 HP and Max HP / [First Use]: When either player plays their next card, [Consume] it*
- **Lv2**: [灵气]+1 / 减对方7生命及上限 / [先机]：双方使用下张牌时将其[消耗]  
  *[Qi]+1 / Opponent loses 7 HP and Max HP / [First Use]: When either player plays their next card, [Consume] it*
- **Lv3**: [灵气]+3 / 减对方2生命及上限（每点[灵气]多1） / [先机]：双方使用下张牌时将其[消耗]  
  *[Qi]+3 / Opponent loses 2 HP and Max HP (+1 for each [Qi]) / [First Use]: When either player plays their next card, [Consume] it*

#### 梦·火灵阵 (Dream - Fire Spirit Formation) — id 7000090
*持续 Continuous*  
- **Lv1**: [激活火灵] / [防]+2 / 减对方6生命及上限  
  *[Activate Fire Spirit] / [DEF]+2 / Opponent loses 6 HP and Max HP*
- **Lv2**: [激活火灵] / [防]+2 / 减对方8生命及上限  
  *[Activate Fire Spirit] / [DEF]+2 / Opponent loses 8 HP and Max HP*
- **Lv3**: [激活火灵] / [防]+2 / 减对方10生命及上限  
  *[Activate Fire Spirit] / [DEF]+2 / Opponent loses 10 HP and Max HP*

#### 梦·土灵断崖 (Dream - Earth Spirit Cliff) — id 7000091
- **Lv1**: [防]+8 / 自身[防]减半，每减1点造成1[伤害]  
  *[DEF]+8 / [DEF] halved, deal 1 [DMG] for each point reduced*
- **Lv2**: [防]+10 / 自身[防]减半，每减1点造成1[伤害]  
  *[DEF]+10 / [DEF] halved, deal 1 [DMG] for each point reduced*
- **Lv3**: [防]+12 / 自身[防]减半，每减1点造成1[伤害]  
  *[DEF]+12 / [DEF] halved, deal 1 [DMG] for each point reduced*

#### 梦·混元碎击 (Dream - Primordial Smash) — id 7000093
- **Lv1**: [灵气]+1 / 2攻 / 卡组中每有1种[五行]就追加1次2攻（最多3次）  
  *[Qi]+1 / 2 ATK / For each type of [Five Elements] in your deck, make an additional 2 ATK (up to 3 times)*
- **Lv2**: [灵气]+1 / 4攻 / 卡组中每有1种[五行]就追加1次2攻（最多3次）  
  *[Qi]+1 / 4 ATK / For each type of [Five Elements] in your deck, make an additional 2 ATK (up to 3 times)*
- **Lv3**: [灵气]+1 / 6攻 / 卡组中每有1种[五行]就追加1次2攻（最多3次）  
  *[Qi]+1 / 6 ATK / For each type of [Five Elements] in your deck, make an additional 2 ATK (up to 3 times)*

#### 梦·水灵汹涌 (Dream - Water Spirit Turbulent) — id 7000103
- **Lv1**: 5攻（每有1[灵气]或[水势]此牌多1攻）  
  *5 ATK (+1 ATK for each [Qi] or [Force of Water])*
- **Lv2**: 7攻（每有1[灵气]或[水势]此牌多1攻）  
  *7 ATK (+1 ATK for each [Qi] or [Force of Water])*
- **Lv3**: 9攻（每有1[灵气]或[水势]此牌多1攻）  
  *9 ATK (+1 ATK for each [Qi] or [Force of Water])*


### Phase 2 — 筑基 Foundation

#### 浑天印 (Cosmos Seal) — id 7000014
- **Lv1**: 5攻 / [灵气]+1 / 下1次使用[五行]牌时，先[激活]其所属[五行]  
  *5 ATK / [Qi]+1 / The next time you play a [Five Elements] card, [Activate] the corresponding [Five Elements]*
- **Lv2**: 9攻 / [灵气]+1 / 下1次使用[五行]牌时，先[激活]其所属[五行]  
  *9 ATK / [Qi]+1 / The next time you play a [Five Elements] card, [Activate] the corresponding [Five Elements]*
- **Lv3**: 13攻 / [灵气]+1 / 下1次使用[五行]牌时，先[激活]其所属[五行]  
  *13 ATK / [Qi]+1 / The next time you play a [Five Elements] card, [Activate] the corresponding [Five Elements]*

#### 金灵·穿心 (Metal Spirit - Heart Pierce) — id 7000015
- **Lv1**: 7攻 / [金灵]：下1次攻击[无视防御]  
  *7 ATK / [Metal Spirit]: Your next 1 attack will [Ignore DEF]*
- **Lv2**: 10攻 / [金灵]：下2次攻击[无视防御]  
  *10 ATK / [Metal Spirit]: Your next 2 attacks will [Ignore DEF]*
- **Lv3**: 13攻 / [金灵]：下3次攻击[无视防御]  
  *13 ATK / [Metal Spirit]: Your next 3 attacks will [Ignore DEF]*

#### 金灵阵 (Metal Spirit Formation) — id 7000016
*持续 Continuous*  
- **Lv1**: [锋锐]+4 / [持续]：每次使用“金灵”牌时加1[锋锐]  
  *[Penetrate]+4 / [Continuous]: Whenever you play a "Metal Spirit" card, add 1 [Penetrate]*
- **Lv2**: [锋锐]+4 / [持续]：每次使用“金灵”牌时加2[锋锐]  
  *[Penetrate]+4 / [Continuous]: Whenever you play a "Metal Spirit" card, add 2 [Penetrate]*
- **Lv3**: [锋锐]+4 / [持续]：每次使用“金灵”牌时加3[锋锐]  
  *[Penetrate]+4 / [Continuous]: Whenever you play a "Metal Spirit" card, add 3 [Penetrate]*

#### 木灵·疏影 (Wood Spirit - Sparse Shadow) — id 7000017
- **Lv1**: 3攻×2 / [木灵]：获得1层[加攻]  
  *3 ATK × 2 / [Wood Spirit]: Gain 1 stack of [Increase ATK]*
- **Lv2**: 3攻×3 / [木灵]：获得1层[加攻]  
  *3 ATK × 3 / [Wood Spirit]: Gain 1 stack of [Increase ATK]*
- **Lv3**: 3攻×4 / [木灵]：获得1层[加攻]  
  *3 ATK × 4 / [Wood Spirit]: Gain 1 stack of [Increase ATK]*

#### 木灵·复苏 (Wood Spirit - Recovery) — id 7000018
- **Lv1**: [灵气]+2 / [木灵]：生命+3（每有1层[加攻]多1生命）  
  *[Qi]+2 / [Wood Spirit]: HP+3 / （Add 1 HP for each stack of [Increase ATK]）*
- **Lv2**: [灵气]+3 / [木灵]：生命+4（每有1层[加攻]多1生命）  
  *[Qi]+3 / [Wood Spirit]: HP+4 / （Add 1 HP for each stack of [Increase ATK]）*
- **Lv3**: [灵气]+4 / [木灵]：生命+6（每有1层[加攻]多1生命）  
  *[Qi]+4 / [Wood Spirit]: HP+6 / （Add 1 HP for each stack of [Increase ATK]）*

#### 水灵·波澜 (Water Spirit - Billows) — id 7000019
- **Lv1**: 获得2层[水势] / [水灵]：此牌不耗[灵气]  
  *Gain 2 stacks of [Force of Water] / [Water Spirit]: This card consumes 0 Qi*
- **Lv2**: 获得3层[水势] / [水灵]：此牌不耗[灵气]  
  *Gain 3 stacks of [Force of Water] / [Water Spirit]: This card consumes 0 Qi*
- **Lv3**: 获得4层[水势] / [水灵]：此牌不耗[灵气]  
  *Gain 4 stacks of [Force of Water] / [Water Spirit]: This card consumes 0 Qi*

#### 火灵·聚炎 (Fire Spirit - Flame Eater) — id 7000021
- **Lv1**: [灵气]+2 / [火灵]：对方减3生命及上限  
  *[Qi]+2 / [Fire Spirit]: Opponent loses 3 HP and Max HP*
- **Lv2**: [灵气]+3 / [火灵]：对方减4生命及上限  
  *[Qi]+3 / [Fire Spirit]: Opponent loses 4 HP and Max HP*
- **Lv3**: [灵气]+4 / [火灵]：对方减6生命及上限  
  *[Qi]+4 / [Fire Spirit]: Opponent loses 6 HP and Max HP*

#### 火灵·赤焰 (Fire Spirit - Scarlet Flame) — id 7000022
- **Lv1**: 4攻×2 / [火灵]：追加4攻  
  *4 ATK × 2 / [Fire Spirit]: Make an additional 4 ATK*
- **Lv2**: 5攻×2 / [火灵]：追加6攻  
  *5 ATK × 2 / [Fire Spirit]: Make an additional 6 ATK*
- **Lv3**: 6攻×2 / [火灵]：追加8攻  
  *6 ATK × 2 / [Fire Spirit]: Make an additional 8 ATK*

#### 土灵阵 (Earth Spirit Formation) — id 7000023
*持续 Continuous*  
- **Lv1**: [防]+4 / [持续]：每次使用“土灵”牌时加2[防]  
  *[DEF]+4 / [Continuous]: Whenever you play an "Earth Spirit" card, add 2 [DEF]*
- **Lv2**: [防]+6 / [持续]：每次使用“土灵”牌时加3[防]  
  *[DEF]+6 / [Continuous]: Whenever you play an "Earth Spirit" card, add 3 [DEF]*
- **Lv3**: [防]+8 / [持续]：每次使用“土灵”牌时加4[防]  
  *[DEF]+8 / [Continuous]: Whenever you play an "Earth Spirit" card, add 4 [DEF]*

#### 土灵·群山 (Earth Spirit - Mountains) — id 7000024
- **Lv1**: 5攻 / [防]+2 / [土灵]：下回合再加3[防]  
  *5 ATK / [DEF]+2 / [Earth Spirit]: Add 3 [DEF] in your next turn*
- **Lv2**: 6攻 / [防]+3 / [土灵]：下回合再加6[防]  
  *6 ATK / [DEF]+3 / [Earth Spirit]: Add 6 [DEF] in your next turn*
- **Lv3**: 7攻 / [防]+4 / [土灵]：下回合再加9[防]  
  *7 ATK / [DEF]+4 / [Earth Spirit]: Add 9 [DEF] in your next turn*

#### 水灵·汹涌 (Water Spirit - Turbulent) — id 7000037
- **Lv1**: 10攻 / [水灵]：每有1层[水势]多1攻  
  *10 ATK / [Water Spirit]: Add 1 ATK for each stack of [Force of Water]*
- **Lv2**: 14攻 / [水灵]：每有1层[水势]多1攻  
  *14 ATK / [Water Spirit]: Add 1 ATK for each stack of [Force of Water]*
- **Lv3**: 18攻 / [水灵]：每有1层[水势]多1攻  
  *18 ATK / [Water Spirit]: Add 1 ATK for each stack of [Force of Water]*

#### 水灵·润木 (Water Spirit - Rhythm Wood) — id 7000048
- **Lv1**: [水灵]：[灵气]+2 / [木灵]：每有1点灵气加2生命  
  *[Water Spirit]: [Qi]+2 / [Wood Spirit]: Add 2 HP for each Qi you have*
- **Lv2**: [水灵]：[灵气]+3 / [木灵]：每有1点灵气加2生命  
  *[Water Spirit]: [Qi]+3 / [Wood Spirit]: Add 2 HP for each Qi you have*
- **Lv3**: [水灵]：[灵气]+4 / [木灵]：每有1点灵气加2生命  
  *[Water Spirit]: [Qi]+4 / [Wood Spirit]: Add 2 HP for each Qi you have*

#### 火灵·窑土 (Fire Spirit - Rhythm Earth) — id 7000049
- **Lv1**: [火灵]：对方减8生命及上限 / [土灵]：[防]+4（每减过对方2生命上限就多加1[防]）  
  *[Fire Spirit]: Opponent loses 8 HP and Max HP / [Earth Spirit]: [DEF]+4 (Add 1 [DEF] for every 2 Max HP of the opponent has been reduced)*
- **Lv2**: [火灵]：对方减12生命及上限 / [土灵]：[防]+6（每减过对方2生命上限就多加1[防]）  
  *[Fire Spirit]: Opponent loses 12 HP and Max HP / [Earth Spirit]: [DEF]+6 (Add 1 [DEF] for every 2 Max HP of the opponent has been reduced)*
- **Lv3**: [火灵]：对方减16生命及上限 / [土灵]：[防]+8（每减过对方2生命上限就多加1[防]）  
  *[Fire Spirit]: Opponent loses 16 HP and Max HP / [Earth Spirit]: [DEF]+8 (Add 1 [DEF] for every 2 Max HP of the opponent has been reduced)*

#### 金灵·封喉 (Metal Spirit - Chokehold) — id 7000063
- **Lv1**: 8攻 / [金灵]：令对方无法加生命，持续2回合  
  *8 ATK / [Metal Spirit]: Make the opponent cannot add HP for 2 turns*
- **Lv2**: 12攻 / [金灵]：令对方无法加生命，持续3回合  
  *12 ATK / [Metal Spirit]: Make the opponent cannot add HP for 3 turns*
- **Lv3**: 16攻 / [金灵]：令对方无法加生命，持续4回合  
  *16 ATK / [Metal Spirit]: Make the opponent cannot add HP for 4 turns*

#### 镇印心法 (Seal Suppression Citta-Dharma) — id 7000094
*持续 Continuous*  
- **Lv1**: 造成6[伤害] / [持续]：每次[激活][五行]时，向对方造成2[伤害]  
  *Deal 6 [DMG] / [Continuous]: Whenever you [Activate] [Five Elements], deal 2 [DMG] to the opponent*
- **Lv2**: 造成7[伤害] / [持续]：每次[激活][五行]时，向对方造成3[伤害]  
  *Deal 7 [DMG] / [Continuous]: Whenever you [Activate] [Five Elements], deal 3 [DMG] to the opponent*
- **Lv3**: 造成8[伤害] / [持续]：每次[激活][五行]时，向对方造成4[伤害]  
  *Deal 8 [DMG] / [Continuous]: Whenever you [Activate] [Five Elements], deal 4 [DMG] to the opponent*


### Phase 3 — 金丹 Virtuoso

#### 土灵·扬尘 (Earth Spirit - Dust) — id 7000012
- **Lv1**: 8攻 / [土灵]：和对方每相差4点生命上限就加1[防]，下回合再加等量[防]  
  *8 ATK / [Earth Spirit]: Add 1 [DEF] for every 4 Max HP difference between you and your opponent, then add the same amount of [DEF] next turn*
- **Lv2**: 12攻 / [土灵]：和对方每相差4点生命上限就加1[防]，下回合再加等量[防]  
  *12 ATK / [Earth Spirit]: Add 1 [DEF] for every 4 Max HP difference between you and your opponent, then add the same amount of [DEF] next turn*
- **Lv3**: 16攻 / [土灵]：和对方每相差4点生命上限就加1[防]，下回合再加等量[防]  
  *16 ATK / [Earth Spirit]: Add 1 [DEF] for every 4 Max HP difference between you and your opponent, then add the same amount of [DEF] next turn*

#### 金灵·蓄锐 (Metal Spirit - Charge) — id 7000025
- **Lv1**: [防]+4 / [锋锐]+4 / [金灵]：每有4[防]就多加1层[锋锐]  
  *[DEF]+4 / [Penetrate]+4 / [Metal Spirit]: Add 1 stack of [Penetrate] for each 4 [DEF]*
- **Lv2**: [防]+6 / [锋锐]+6 / [金灵]：每有4[防]就多加1层[锋锐]  
  *[DEF]+6 / [Penetrate]+6 / [Metal Spirit]: Add 1 stack of [Penetrate] for each 4 [DEF]*
- **Lv3**: [防]+8 / [锋锐]+8 / [金灵]：每有4[防]就多加1层[锋锐]  
  *[DEF]+8 / [Penetrate]+8 / [Metal Spirit]: Add 1 stack of [Penetrate] for each 4 [DEF]*

#### 金灵·锋芒 (Metal Spirit - Sharp) — id 7000026
- **Lv1**: 6攻 / [金灵]：每[击伤]2点生命加1层[锋锐]  
  *6 ATK / [Metal Spirit]: For every 2 HP [Injured] by this card, gain 1 stack of [Penetrate]*
- **Lv2**: 9攻 / [金灵]：每[击伤]2点生命加1层[锋锐]  
  *9 ATK / [Metal Spirit]: For every 2 HP [Injured] by this card, gain 1 stack of [Penetrate]*
- **Lv3**: 12攻 / [金灵]：每[击伤]2点生命加1层[锋锐]  
  *12 ATK / [Metal Spirit]: For every 2 HP [Injured] by this card, gain 1 stack of [Penetrate]*

#### 木灵·巡林 (Wood Spirit - Forest Guard) — id 7000028
- **Lv1**: 1攻×2 / [碎防] / [木灵]：若已加过生命则[再次行动]  
  *1 ATK × 2 / [Smash DEF] / [Wood Spirit]: If you have already added HP, [Chase]*
- **Lv2**: 2攻×2 / [碎防] / [木灵]：若已加过生命则[再次行动]  
  *2 ATK × 2 / [Smash DEF] / [Wood Spirit]: If you have already added HP, [Chase]*
- **Lv3**: 3攻×2 / [碎防] / [木灵]：若已加过生命则[再次行动]  
  *3 ATK × 2 / [Smash DEF] / [Wood Spirit]: If you have already added HP, [Chase]*

#### 水灵阵 (Water Spirit Formation) — id 7000029
*持续 Continuous*  
- **Lv1**: [灵气]+2 / [持续]：每次使用“水灵”牌时加1[灵气]  
  *[Qi]+2 / [Continuous]: Whenever you play a "Water Spirit" card, add 1 [Qi]*
- **Lv2**: [灵气]+3 / [持续]：每次使用“水灵”牌时加1[灵气]  
  *[Qi]+3 / [Continuous]: Whenever you play a "Water Spirit" card, add 1 [Qi]*
- **Lv3**: [灵气]+5 / [持续]：每次使用“水灵”牌时加1[灵气]  
  *[Qi]+5 / [Continuous]: Whenever you play a "Water Spirit" card, add 1 [Qi]*

#### 火灵阵 (Fire Spirit Formation) — id 7000031
*持续 Continuous*  
- **Lv1**: 对方减2生命及上限 / [持续]：每次使用“火灵”牌时减对方2生命及上限  
  *Opponent loses 2 HP and Max HP / [Continuous]: Whenever you play a "Fire Spirit" card, the opponent loses 2 HP and Max HP*
- **Lv2**: 对方减3生命及上限 / [持续]：每次使用“火灵”牌时减对方3生命及上限  
  *Opponent loses 3 HP and Max HP / [Continuous]: Whenever you play a "Fire Spirit" card, the opponent loses 3 HP and Max HP*
- **Lv3**: 对方减4生命及上限 / [持续]：每次使用“火灵”牌时减对方4生命及上限  
  *Opponent loses 4 HP and Max HP / [Continuous]: Whenever you play a "Fire Spirit" card, the opponent loses 4 HP and Max HP*

#### 火灵·轰爆 (Fire Spirit - Blast) — id 7000032
- **Lv1**: 获得1层[加攻] / [火灵]：对方减7生命及上限（每有1层[加攻]多减1点）  
  *Gain 1 stack(s) of [Increase ATK] / [Fire Spirit]: Opponent loses 7 HP and Max HP (increase this by 1 for every stack of [Increase ATK])*
- **Lv2**: 获得2层[加攻] / [火灵]：对方减7生命及上限（每有1层[加攻]多减1点）  
  *Gain 2 stack(s) of [Increase ATK] / [Fire Spirit]: Opponent loses 7 HP and Max HP (increase this by 1 for every stack of [Increase ATK])*
- **Lv3**: 获得3层[加攻] / [火灵]：对方减7生命及上限（每有1层[加攻]多减1点）  
  *Gain 3 stack(s) of [Increase ATK] / [Fire Spirit]: Opponent loses 7 HP and Max HP (increase this by 1 for every stack of [Increase ATK])*

#### 木灵阵 (Wood Spirit Formation) — id 7000036
*持续 Continuous*  
- **Lv1**: 生命上限+10 / [持续]：每次使用“木灵”牌时加2生命  
  *Max HP+10 / [Continuous]: Whenever you play a "Wood Spirit" card, add 2 HP*
- **Lv2**: 生命上限+15 / [持续]：每次使用“木灵”牌时加3生命  
  *Max HP+15 / [Continuous]: Whenever you play a "Wood Spirit" card, add 3 HP*
- **Lv3**: 生命上限+20 / [持续]：每次使用“木灵”牌时加4生命  
  *Max HP+20 / [Continuous]: Whenever you play a "Wood Spirit" card, add 4 HP*

#### 土灵·岩崩 (Earth Spirit - Rockslide) — id 7000041
- **Lv1**: [防]+10 / [土灵]：对双方各造成10[伤害]（自身每有1[防]就多1[伤害]）  
  *[DEF]+10 / [Earth Spirit]: Deal 10 [DMG] to both players (For each [DEF] you have, the [DMG] increased by 1)*
- **Lv2**: [防]+15 / [土灵]：对双方各造成10[伤害]（自身每有1[防]就多1[伤害]）  
  *[DEF]+15 / [Earth Spirit]: Deal 10 [DMG] to both players (For each [DEF] you have, the [DMG] increased by 1)*
- **Lv3**: [防]+20 / [土灵]：对双方各造成10[伤害]（自身每有1[防]就多1[伤害]）  
  *[DEF]+20 / [Earth Spirit]: Deal 10 [DMG] to both players (For each [DEF] you have, the [DMG] increased by 1)*

#### 金灵·凝水 (Metal Spirit - Rhythm Water) — id 7000050
- **Lv1**: [金灵]：[锋锐]+4 / [水灵]：[锋锐]减半，每减1点获得1层[水势]  
  *[Metal Spirit]: [Penetrate]+4 / [Water Spirit]: [Penetrate] halved, for each reduced point you gain 1 stack of [Force of Water]*
- **Lv2**: [金灵]：[锋锐]+6 / [水灵]：[锋锐]减半，每减1点获得1层[水势]  
  *[Metal Spirit]: [Penetrate]+6 / [Water Spirit]: [Penetrate] halved, for each reduced point you gain 1 stack of [Force of Water]*
- **Lv3**: [金灵]：[锋锐]+8 / [水灵]：[锋锐]减半，每减1点获得1层[水势]  
  *[Metal Spirit]: [Penetrate]+8 / [Water Spirit]: [Penetrate] halved, for each reduced point you gain 1 stack of [Force of Water]*

#### 五行遁术 (Five Elements Escape) — id 7000055
- **Lv1**: [防]+8 / 若已激活至少2种[五行]则[再次行动]  
  *[DEF]+8 / If at least 2 types of [Five Elements] have been activated, [Chase]*
- **Lv2**: [防]+13 / 若已激活至少2种[五行]则[再次行动]  
  *[DEF]+13 / If at least 2 types of [Five Elements] have been activated, [Chase]*
- **Lv3**: [防]+18 / 若已激活至少2种[五行]则[再次行动]  
  *[DEF]+18 / If at least 2 types of [Five Elements] have been activated, [Chase]*

#### 水灵·泉涌 (Water Spirit - Spring) — id 7000059
- **Lv1**: [灵气]+2 / [水灵]：下1次攻击每[击伤]5点生命就获得1层[水势]  
  *[Qi]+2 / [Water Spirit]: Gain 1 stack of [Force of Water] for every 5 [Injured] opponent's HP in next 1 attack*
- **Lv2**: [灵气]+3 / [水灵]：下1次攻击每[击伤]5点生命就获得1层[水势]  
  *[Qi]+3 / [Water Spirit]: Gain 1 stack of [Force of Water] for every 5 [Injured] opponent's HP in next 1 attack*
- **Lv3**: [灵气]+4 / [水灵]：下1次攻击每[击伤]5点生命就获得1层[水势]  
  *[Qi]+4 / [Water Spirit]: Gain 1 stack of [Force of Water] for every 5 [Injured] opponent's HP in next 1 attack*

#### 土灵·断崖 (Earth Spirit - Cliff) — id 7000062
- **Lv1**: [防]+10 / [土灵]：下1次[防]减少时，向对方造成减少值的[伤害]  
  *[DEF]+10 / [Earth Spirit]: When the next 1 time your DEF is reduced, deal the same value of the reduced DEF's [DMG] to the opponent*
- **Lv2**: [防]+15 / [土灵]：下1次[防]减少时，向对方造成减少值的[伤害]  
  *[DEF]+15 / [Earth Spirit]: When the next 1 time your DEF is reduced, deal the same value of the reduced DEF's [DMG] to the opponent*
- **Lv3**: [防]+20 / [土灵]：下1次[防]减少时，向对方造成减少值的[伤害]  
  *[DEF]+20 / [Earth Spirit]: When the next 1 time your DEF is reduced, deal the same value of the reduced DEF's [DMG] to the opponent*

#### 木灵·藤蔓 (Wood Spirit - Vine) — id 7000064
- **Lv1**: 4攻×2 / [木灵]：每加过5点生命，追加1次攻击（最多追加3次）  
  *4 ATK × 2. / [Wood Spirit]: For every 5 HP was added, make an additional ATK (Up to 3 times)*
- **Lv2**: 4攻×2 / [木灵]：每加过5点生命，追加1次攻击（最多追加4次）  
  *4 ATK × 2. / [Wood Spirit]: For every 5 HP was added, make an additional ATK (Up to 4 times)*
- **Lv3**: 4攻×2 / [木灵]：每加过5点生命，追加1次攻击（最多追加5次）  
  *4 ATK × 2. / [Wood Spirit]: For every 5 HP was added, make an additional ATK (Up to 5 times)*

#### 五行流转 (Five Elements Circulation) — id 7000067
*derived from: 清心咒*  
- **Lv1**: 若前一格牌[五行相生]后一格牌，则[激活]后一格牌的[五行]，并使用其效果（最高1级）  
  *If the previous slot card has [Five Element Generating Interaction] with the next card, then [Activate] the [Five Elements] of the next card and trigger its effect (Up to Lv.1)*
- **Lv2**: 若前一格牌[五行相生]后一格牌，则[激活]后一格牌的[五行]，并使用其效果（最高2级）  
  *If the previous slot card has [Five Element Generating Interaction] with the next card, then [Activate] the [Five Elements] of the next card and trigger its effect (Up to Lv.2)*
- **Lv3**: 若前一格牌[五行相生]后一格牌，则[激活]后一格牌的[五行]，并使用其效果（最高3级）  
  *If the previous slot card has [Five Element Generating Interaction] with the next card, then [Activate] the [Five Elements] of the next card and trigger its effect (Up to Lv.3)*

#### 五行灵击 (Five Elements Spirit Strike) — id 7000095
- **Lv1**: 15攻（每剩余1[灵气]多1攻） / 卡组中每有1种不同[五行]此牌少耗1[灵气]  
  *15 ATK (1 more ATK for each [Qi]) / This card costs 1 less [Qi] for each different [Five Elements] type in your deck*
- **Lv2**: 19攻（每剩余1[灵气]多1攻） / 卡组中每有1种不同[五行]此牌少耗1[灵气]  
  *19 ATK (1 more ATK for each [Qi]) / This card costs 1 less [Qi] for each different [Five Elements] type in your deck*
- **Lv3**: 23攻（每剩余1[灵气]多1攻） / 卡组中每有1种不同[五行]此牌少耗1[灵气]  
  *23 ATK (1 more ATK for each [Qi]) / This card costs 1 less [Qi] for each different [Five Elements] type in your deck*


### Phase 4 — 元婴 Immortality

#### 木灵·暗香 (Wood Spirit - Fragrant) — id 7000005
- **Lv1**: 3攻 / [木灵]：获得1层[加攻]  
  *3 ATK / [Wood Spirit]: Gain 1 stack of [Increase ATK]*
- **Lv2**: 3攻×2 / [木灵]：获得1层[加攻]  
  *3 ATK × 2 / [Wood Spirit]: Gain 1 stack of [Increase ATK]*
- **Lv3**: 3攻×3 / [木灵]：获得1层[加攻]  
  *3 ATK × 3 / [Wood Spirit]: Gain 1 stack of [Increase ATK]*

#### 水灵·潜遁 (Water Spirit - Dive) — id 7000020
- **Lv1**: 生命及上限+2 / [水灵]：受到的攻击减少40%，持续2回合  
  *HP and Max HP+2 / [Water Spirit]: You take 40% less ATK for 2 turn*
- **Lv2**: 生命及上限+7 / [水灵]：受到的攻击减少40%，持续2回合  
  *HP and Max HP+7 / [Water Spirit]: You take 40% less ATK for 2 turn*
- **Lv3**: 生命及上限+12 / [水灵]：受到的攻击减少40%，持续2回合  
  *HP and Max HP+12 / [Water Spirit]: You take 40% less ATK for 2 turn*

#### 木灵·玫刺 (Wood Spirit - Thorn) — id 7000027
- **Lv1**: 4攻×3 / [木灵]：每[击伤]3点生命，自身加1生命  
  *4 ATK × 3 / [Wood Spirit]: For every 3 HP [Injured] by this card, add 1 HP*
- **Lv2**: 4攻×4 / [木灵]：每[击伤]3点生命，自身加1生命  
  *4 ATK × 4 / [Wood Spirit]: For every 3 HP [Injured] by this card, add 1 HP*
- **Lv3**: 4攻×5 / [木灵]：每[击伤]3点生命，自身加1生命  
  *4 ATK × 5 / [Wood Spirit]: For every 3 HP [Injured] by this card, add 1 HP*

#### 水灵·腾浪 (Water Spirit - Great Waves) — id 7000030
- **Lv1**: [灵气]+2 / 生命及上限+2 / [水灵]：每有2点灵气就获得1层[水势]  
  *[Qi]+2 / HP and Max HP+2 / [Water Spirit]: Add 1 stack of [Force of Water] for every 2 [Qi]*
- **Lv2**: [灵气]+3 / 生命及上限+3 / [水灵]：每有2点灵气就获得1层[水势]  
  *[Qi]+3 / HP and Max HP+3 / [Water Spirit]: Add 1 stack of [Force of Water] for every 2 [Qi]*
- **Lv3**: [灵气]+4 / 生命及上限+4 / [水灵]：每有2点灵气就获得1层[水势]  
  *[Qi]+4 / HP and Max HP+4 / [Water Spirit]: Add 1 stack of [Force of Water] for every 2 [Qi]*

#### 土灵·流沙 (Earth Spirit - Quicksand) — id 7000033
- **Lv1**: 9攻 / [土灵]：自身每减少过6防，此牌多1攻  
  *9 ATK / [Earth Spirit]: Add 1 ATK for every 6 [DEF] you have been lost*
- **Lv2**: 9攻 / [土灵]：自身每减少过5防，此牌多1攻  
  *9 ATK / [Earth Spirit]: Add 1 ATK for every 5 [DEF] you have been lost*
- **Lv3**: 9攻 / [土灵]：自身每减少过4防，此牌多1攻  
  *9 ATK / [Earth Spirit]: Add 1 ATK for every 4 [DEF] you have been lost*

#### 金灵·飞梭 (Metal Spirit - Shuttle) — id 7000034
- **Lv1**: 4攻 / 此牌攻击不触发[锋锐] / [金灵]：[再次行动]  
  *4 ATK / This card's attack will not trigger [Penetrate] / [Metal Spirit]: [Chase]*
- **Lv2**: 8攻 / 此牌攻击不触发[锋锐] / [金灵]：[再次行动]  
  *8 ATK / This card's attack will not trigger [Penetrate] / [Metal Spirit]: [Chase]*
- **Lv3**: 12攻 / 此牌攻击不触发[锋锐] / [金灵]：[再次行动]  
  *12 ATK / This card's attack will not trigger [Penetrate] / [Metal Spirit]: [Chase]*

#### 金灵·铁骨 (Metal Spirit - Iron Bone) — id 7000035
- **Lv1**: [金灵]：受到的攻或伤害减5（最低减至1），持续2回合  
  *[Metal Spirit]: You take 5 less ATK or DMG (min 1) from your opponent for 2 turns*
- **Lv2**: [金灵]：受到的攻或伤害减5（最低减至1），持续3回合  
  *[Metal Spirit]: You take 5 less ATK or DMG (min 1) from your opponent for 3 turns*
- **Lv3**: [金灵]：受到的攻或伤害减5（最低减至1），持续4回合  
  *[Metal Spirit]: You take 5 less ATK or DMG (min 1) from your opponent for 4 turns*

#### 火灵·瞬燃 (Fire Spirit - Flash Fire) — id 7000038
*derived from: 火云符*  
- **Lv1**: 对方减4生命上限 / [火灵]：[再次行动]  
  *Opponent loses 4 Max HP / [Fire Spirit]: [Chase]*
- **Lv2**: 对方减8生命上限 / [火灵]：[再次行动]  
  *Opponent loses 8 Max HP / [Fire Spirit]: [Chase]*
- **Lv3**: 对方减12生命上限 / [火灵]：[再次行动]  
  *Opponent loses 12 Max HP / [Fire Spirit]: [Chase]*

#### 火灵·灼心 (Fire Spirit - Heart Fire) — id 7000039
- **Lv1**: 4攻×2 / [火灵]：每[击伤]1点生命，减对方2生命上限  
  *4 ATK × 2 / [Fire Spirit]: For every [Injured] HP by this card, decrease opponent's Max HP by 2*
- **Lv2**: 5攻×2 / [火灵]：每[击伤]1点生命，减对方2生命上限  
  *5 ATK × 2 / [Fire Spirit]: For every [Injured] HP by this card, decrease opponent's Max HP by 2*
- **Lv3**: 7攻×2 / [火灵]：每[击伤]1点生命，减对方2生命上限  
  *7 ATK × 2 / [Fire Spirit]: For every [Injured] HP by this card, decrease opponent's Max HP by 2*

#### 土灵·绝壁 (Earth Spirit - Steep) — id 7000040
- **Lv1**: [防]+12 / [土灵]：自身每减少过6[防]就多加1[防]  
  *[DEF]+12 / [Earth Spirit]: Add 1 [DEF] for every 6 [DEF] you have been lost*
- **Lv2**: [防]+12 / [土灵]：自身每减少过5[防]就多加1[防]  
  *[DEF]+12 / [Earth Spirit]: Add 1 [DEF] for every 5 [DEF] you have been lost*
- **Lv3**: [防]+12 / [土灵]：自身每减少过4[防]就多加1[防]  
  *[DEF]+12 / [Earth Spirit]: Add 1 [DEF] for every 4 [DEF] you have been lost*

#### 土灵·撼地 (Earth Spirit - Earthquake) — id 7000046
- **Lv1**: 6攻 / [防]+6 / [土灵]：令对方[灵气]和[防]减半  
  *6 ATK / [DEF]+6 / [Earth Spirit]: Halve the opponent's [Qi] and [DEF]*
- **Lv2**: 9攻 / [防]+9 / [土灵]：令对方[灵气]和[防]减半  
  *9 ATK / [DEF]+9 / [Earth Spirit]: Halve the opponent's [Qi] and [DEF]*
- **Lv3**: 12攻 / [防]+12 / [土灵]：令对方[灵气]和[防]减半  
  *12 ATK / [DEF]+12 / [Earth Spirit]: Halve the opponent's [Qi] and [DEF]*

#### 土灵·韵金 (Earth Spirit - Rhythm Metal) — id 7000047
- **Lv1**: [土灵]：[防]+10，失去所有[防]再加回 / [金灵]：本场战斗每失去过4[防]就加1[锋锐]  
  *[Earth Spirit]: [DEF]+10, then lose all [DEF] and add it back / [Metal Spirit]: Add 1 stack of [Penetrate] for every 4 [DEF] you have been lost*
- **Lv2**: [土灵]：[防]+15，失去所有[防]再加回 / [金灵]：本场战斗每失去过4[防]就加1[锋锐]  
  *[Earth Spirit]: [DEF]+15, then lose all [DEF] and add it back / [Metal Spirit]: Add 1 stack of [Penetrate] for every 4 [DEF] you have been lost*
- **Lv3**: [土灵]：[防]+20，失去所有[防]再加回 / [金灵]：本场战斗每失去过4[防]就加1[锋锐]  
  *[Earth Spirit]: [DEF]+20, then lose all [DEF] and add it back / [Metal Spirit]: Add 1 stack of [Penetrate] for every 4 [DEF] you have been lost*

#### 木灵·燃火 (Wood Spirit - Rhythm Fire) — id 7000051
- **Lv1**: [木灵]：生命+16 / [火灵]：1攻（剩余生命减半，每减1点多1攻）  
  *[Wood Spirit]: HP+16 / [Fire Spirit]: 1 ATK (The rest of HP halved, for each reduced HP you gain 1 ATK)*
- **Lv2**: [木灵]：生命+22 / [火灵]：1攻（剩余生命减半，每减1点多1攻）  
  *[Wood Spirit]: HP+22 / [Fire Spirit]: 1 ATK (The rest of HP halved, for each reduced HP you gain 1 ATK)*
- **Lv3**: [木灵]：生命+28 / [火灵]：1攻（剩余生命减半，每减1点多1攻）  
  *[Wood Spirit]: HP+28 / [Fire Spirit]: 1 ATK (The rest of HP halved, for each reduced HP you gain 1 ATK)*

#### 木灵·暗香 (Wood Spirit - Fragrant) — id 7000061
- **Lv1**: [灵气]+2 / 生命+2 / [木灵]：每有3点[灵气]就获得1层[加攻]  
  *[Qi]+2 / HP+2 / [Wood Spirit]: For every 3 [Qi], gain 1 stack of [Increase ATK]*
- **Lv2**: [灵气]+3 / 生命+3 / [木灵]：每有3点[灵气]就获得1层[加攻]  
  *[Qi]+3 / HP+3 / [Wood Spirit]: For every 3 [Qi], gain 1 stack of [Increase ATK]*
- **Lv3**: [灵气]+4 / 生命+4 / [木灵]：每有3点[灵气]就获得1层[加攻]  
  *[Qi]+4 / HP+4 / [Wood Spirit]: For every 3 [Qi], gain 1 stack of [Increase ATK]*

#### 混元碎击 (World Smash) — id 7000066
- **Lv1**: 4攻 / [碎防] / 卡组中每有1种不同[五行]，此牌多4攻  
  *4 ATK / [Smash DEF] / For each different [Five Elements] you have in your deck, this card adds 4 ATK*
- **Lv2**: 7攻 / [碎防] / 卡组中每有1种不同[五行]，此牌多5攻  
  *7 ATK / [Smash DEF] / For each different [Five Elements] you have in your deck, this card adds 5 ATK*
- **Lv3**: 10攻 / [碎防] / 卡组中每有1种不同[五行]，此牌多6攻  
  *10 ATK / [Smash DEF] / For each different [Five Elements] you have in your deck, this card adds 6 ATK*

#### 土灵·遁地 (Earth Spirit - Burrow) — id 7000096
- **Lv1**: [防]+4 / [土灵]：[再次行动]  
  *[DEF]+4 / [Earth Spirit]: [Chase]*
- **Lv2**: [防]+8 / [土灵]：[再次行动]  
  *[DEF]+8 / [Earth Spirit]: [Chase]*
- **Lv3**: [防]+12 / [土灵]：[再次行动]  
  *[DEF]+12 / [Earth Spirit]: [Chase]*


### Phase 5 — 化神 Incarnation

#### 金灵·巨鼎落 (Metal Spirit - Giant Tripod) — id 7000042
- **Lv1**: 7攻 / [金灵]：此牌[击伤]对手时扣减的生命加倍  
  *7 ATK / [Metal Spirit]: If the opponent is [Injured] by this card, double the HP deduction*
- **Lv2**: 11攻 / [金灵]：此牌[击伤]对手时扣减的生命加倍  
  *11 ATK / [Metal Spirit]: If the opponent is [Injured] by this card, double the HP deduction*
- **Lv3**: 15攻 / [金灵]：此牌[击伤]对手时扣减的生命加倍  
  *15 ATK / [Metal Spirit]: If the opponent is [Injured] by this card, double the HP deduction*

#### 木灵·柳纷飞 (Wood Spirit - Willow Leaf) — id 7000043
*derived from: 锐金符*  
- **Lv1**: 获得1层[加攻] / 生命+3 / [木灵]：[再次行动]  
  *Gain 1 stack(s) of [Increase ATK] / HP+3 / [Wood Spirit]: [Chase]*
- **Lv2**: 获得2层[加攻] / 生命+3 / [木灵]：[再次行动]  
  *Gain 2 stack(s) of [Increase ATK] / HP+3 / [Wood Spirit]: [Chase]*
- **Lv3**: 获得3层[加攻] / 生命+3 / [木灵]：[再次行动]  
  *Gain 3 stack(s) of [Increase ATK] / HP+3 / [Wood Spirit]: [Chase]*

#### 水灵·海龙啸 (Water Spirit - Tsunami) — id 7000044
- **Lv1**: 获得4层[水势] / [水灵]：令对方无法行动1回合  
  *Gain 4 stacks of [Force of Water] / [Water Spirit]: Make the opponent unable to act for 1 turn*
- **Lv2**: 获得5层[水势] / [水灵]：令对方无法行动1回合  
  *Gain 5 stacks of [Force of Water] / [Water Spirit]: Make the opponent unable to act for 1 turn*
- **Lv3**: 获得6层[水势] / [水灵]：令对方无法行动1回合  
  *Gain 6 stacks of [Force of Water] / [Water Spirit]: Make the opponent unable to act for 1 turn*

#### 火灵·焚天焱 (Fire Spirit - Burning Sky) — id 7000045
- **Lv1**: 3攻×3 / [火灵]：每减过对方3点生命上限此牌多1攻  
  *3 ATK × 3 / [Fire Spirit]: For every 3 Max HP of the opponent has been reduced, this card add 1 ATK*
- **Lv2**: 5攻×3 / [火灵]：每减过对方3点生命上限此牌多1攻  
  *5 ATK × 3 / [Fire Spirit]: For every 3 Max HP of the opponent has been reduced, this card add 1 ATK*
- **Lv3**: 7攻×3 / [火灵]：每减过对方3点生命上限此牌多1攻  
  *7 ATK × 3 / [Fire Spirit]: For every 3 Max HP of the opponent has been reduced, this card add 1 ATK*

#### 土灵·合八荒 (Earth Spirit - Combine World) — id 7000053
- **Lv1**: [防]+12 / [土灵]：下2次[防]减少时，立刻加回减少的[防]  
  *[DEF]+12 / [Earth Spirit]: The next 2 times your [DEF] is reduced, restore it immediately*
- **Lv2**: [防]+12 / [土灵]：下3次[防]减少时，立刻加回减少的[防]  
  *[DEF]+12 / [Earth Spirit]: The next 3 times your [DEF] is reduced, restore it immediately*
- **Lv3**: [防]+12 / [土灵]：下4次[防]减少时，立刻加回减少的[防]  
  *[DEF]+12 / [Earth Spirit]: The next 4 times your [DEF] is reduced, restore it immediately*

#### 火灵·烈燎原 (Fire Spirit - Blazing Prairie) — id 7000056
- **Lv1**: 6攻×3 / [火灵]：令对方生命上限减至其当前生命减2  
  *6 ATK × 3 / [Fire Spirit]: Reduces the opponent's Max HP to their current HP minus 2*
- **Lv2**: 8攻×3 / [火灵]：令对方生命上限减至其当前生命减3  
  *8 ATK × 3 / [Fire Spirit]: Reduces the opponent's Max HP to their current HP minus 3*
- **Lv3**: 10攻×3 / [火灵]：令对方生命上限减至其当前生命减4  
  *10 ATK × 3 / [Fire Spirit]: Reduces the opponent's Max HP to their current HP minus 4*

#### 水灵·纳百川 (Water Spirit - Combine Rivers) — id 7000057
- **Lv1**: 获得3层[水势] / [水灵]：生命及上限+6（每有1层[水势]多1点）  
  *Gain 3 stacks of [Force of Water] / [Water Spirit]: Add 6 HP and Max HP (for every stack of [Force of Water], increase by 1)*
- **Lv2**: 获得4层[水势] / [水灵]：生命及上限+8（每有1层[水势]多1点）  
  *Gain 4 stacks of [Force of Water] / [Water Spirit]: Add 8 HP and Max HP (for every stack of [Force of Water], increase by 1)*
- **Lv3**: 获得5层[水势] / [水灵]：生命及上限+10（每有1层[水势]多1点）  
  *Gain 5 stacks of [Force of Water] / [Water Spirit]: Add 10 HP and Max HP (for every stack of [Force of Water], increase by 1)*

#### 混元无极阵 (Ultimate World Formation) — id 7000058
*持续 Continuous · derived from: 护灵符*  
- **Lv1**: [持续]0[次]（卡组中每有1种不同[五行]就多1次）：激活任意[五行]后[再次行动]  
  *[Continuous] X [Times] (X is the number of different [Five Elements] in your deck): Whenever you activate any [Five Elements], [Chase]*
- **Lv2**: [持续]2[次]（卡组中每有1种不同[五行]就多1次）：激活任意[五行]后[再次行动]  
  *[Continuous] X+2 [Times] (X is the number of different [Five Elements] in your deck): Whenever you activate any [Five Elements], [Chase]*
- **Lv3**: [持续]4[次]（卡组中每有1种不同[五行]就多1次）：激活任意[五行]后[再次行动]  
  *[Continuous] X+4 [Times] (X is the number of different [Five Elements] in your deck): Whenever you activate any [Five Elements], [Chase]*

#### 五行天髓诀 (Five Elements Heavenly Marrow Rhythm) — id 7000073
*持续 Continuous · derived from: 奔雷符*  
- **Lv1**: [持续]2[次]：若卡组仅含一种[五行]，使用该[五行]的牌时未攻击则[再次行动]  
  *[Continuous] 2 [Times]: If there is only one type of [Five Elements] in your deck, whenever you play a [Five Elements] card that is not an ATK, [Chase]*
- **Lv2**: [灵气]+2 / [持续]2[次]：若卡组仅含一种[五行]，使用该[五行]的牌时未攻击则[再次行动]  
  *[Qi]+2 / [Continuous] 2 [Times]: If there is only one type of [Five Elements] in your deck, whenever you play a [Five Elements] card that is not an ATK, [Chase]*
- **Lv3**: [灵气]+2 / [持续]3[次]：若卡组仅含一种[五行]，使用该[五行]的牌时未攻击则[再次行动]  
  *[Qi]+2 / [Continuous] 3 [Times]: If there is only one type of [Five Elements] in your deck, whenever you play a [Five Elements] card that is not an ATK, [Chase]*

#### 木灵·春风拂 (Wood Spirit - Spring Breeze) — id 7000097
- **Lv1**: [灵气]+2 / [木灵]：自身每次攻击时加2生命及上限，持续4回合 / 2攻×2  
  *[Qi]+2 / [Wood Spirit]: Each of your attacks adds 2 HP and Max HP for 4 turns / 2 ATK × 2*
- **Lv2**: [灵气]+3 / [木灵]：自身每次攻击时加2生命及上限，持续4回合 / 2攻×3  
  *[Qi]+3 / [Wood Spirit]: Each of your attacks adds 2 HP and Max HP for 4 turns / 2 ATK × 3*
- **Lv3**: [灵气]+4 / [木灵]：自身每次攻击时加2生命及上限，持续4回合 / 2攻×4  
  *[Qi]+4 / [Wood Spirit]: Each of your attacks adds 2 HP and Max HP for 4 turns / 2 ATK × 4*

#### 火灵·焚脉诀 (Fire Spirit - Vein Burn Rhythm) — id 7000098
- **Lv1**: [灵气]+3 / 加至2层[加攻]，每加1层减自身4生命上限 / [火灵]：每有1层[加攻]，减对方2生命及上限  
  *[Qi]+3 / Raise [Increase ATK] to 2 stacks, lose 4 Max HP for each stack gained / [Fire Spirit]: Reduce opponent's HP and Max HP by 2 for each stack of [Increase ATK]*
- **Lv2**: [灵气]+3 / 加至3层[加攻]，每加1层减自身4生命上限 / [火灵]：每有1层[加攻]，减对方2生命及上限  
  *[Qi]+3 / Raise [Increase ATK] to 3 stacks, lose 4 Max HP for each stack gained / [Fire Spirit]: Reduce opponent's HP and Max HP by 2 for each stack of [Increase ATK]*
- **Lv3**: [灵气]+3 / 加至4层[加攻]，每加1层减自身4生命上限 / [火灵]：每有1层[加攻]，减对方2生命及上限  
  *[Qi]+3 / Raise [Increase ATK] to 4 stacks, lose 4 Max HP for each stack gained / [Fire Spirit]: Reduce opponent's HP and Max HP by 2 for each stack of [Increase ATK]*

#### 金灵·回锋刃 (Metal Spirit - Returning Edge) — id 7000099
- **Lv1**: 6攻×2 / [金灵]：此牌每次攻击消耗[锋锐]后，返还60%的[锋锐]（向上取整）  
  *6 ATK × 2 / [Metal Spirit]: After each of this card's attacks consumes [Penetrate], return 60% of the [Penetrate] (rounded up)*
- **Lv2**: 6攻×3 / [金灵]：此牌每次攻击消耗[锋锐]后，返还60%的[锋锐]（向上取整）  
  *6 ATK × 3 / [Metal Spirit]: After each of this card's attacks consumes [Penetrate], return 60% of the [Penetrate] (rounded up)*
- **Lv3**: 6攻×4 / [金灵]：此牌每次攻击消耗[锋锐]后，返还60%的[锋锐]（向上取整）  
  *6 ATK × 4 / [Metal Spirit]: After each of this card's attacks consumes [Penetrate], return 60% of the [Penetrate] (rounded up)*

#### 水灵·乘风浪 (Water Spirit - Ride the Waves) — id 7000100
- **Lv1**: [水势]+1 / 生命及上限+4 / [水灵]：每有1[水势]或[灵气]加2[身法]（最多加12）  
  *[Force of Water]+1 / HP and Max HP+4 / [Water Spirit]: Add 2 [Agility] for each [Force of Water] or [Qi] (up to 12)*
- **Lv2**: [水势]+2 / 生命及上限+6 / [水灵]：每有1[水势]或[灵气]加2[身法]（最多加14）  
  *[Force of Water]+2 / HP and Max HP+6 / [Water Spirit]: Add 2 [Agility] for each [Force of Water] or [Qi] (up to 14)*
- **Lv3**: [水势]+3 / 生命及上限+8 / [水灵]：每有1[水势]或[灵气]加2[身法]（最多加16）  
  *[Force of Water]+3 / HP and Max HP+8 / [Water Spirit]: Add 2 [Agility] for each [Force of Water] or [Qi] (up to 16)*

#### 混元化灵 (Primordial Spirit Transmutation) — id 7000101
- **Lv1**: [灵气]+2（卡组中每有1种[五行]多1） / [激活][相邻]牌所属[五行] / [被动]：卡组中算作多1种[五行]  
  *[Qi]+2 (+1 per [Five Elements] type in deck) / [Activate] the [Five Elements] of [Adjacent] cards / [Passive]: Deck counts as having 1 more [Five Elements] types*
- **Lv2**: [灵气]+4（卡组中每有1种[五行]多1） / [激活][相邻]牌所属[五行] / [被动]：卡组中算作多1种[五行]  
  *[Qi]+4 (+1 per [Five Elements] type in deck) / [Activate] the [Five Elements] of [Adjacent] cards / [Passive]: Deck counts as having 1 more [Five Elements] types*
- **Lv3**: [灵气]+5（卡组中每有1种[五行]多1） / [激活][相邻]牌所属[五行] / [被动]：卡组中算作多2种[五行]  
  *[Qi]+5 (+1 per [Five Elements] type in deck) / [Activate] the [Five Elements] of [Adjacent] cards / [Passive]: Deck counts as having 2 more [Five Elements] types*

#### 极·水灵阵 (Ultimate - Water Spirit Formation) — id 7000104
*持续 Continuous*  
- **Lv1**: [再次行动] / [持续]：每次使用“水灵”牌时加1[灵气]  
  *[Chase] / [Continuous]: Whenever you play a "Water Spirit" card, add 1 [Qi]*
- **Lv2**: [灵气]+2 / [再次行动] / [持续]：每次使用“水灵”牌时加1[灵气]  
  *[Qi]+2 / [Chase] / [Continuous]: Whenever you play a "Water Spirit" card, add 1 [Qi]*
- **Lv3**: [灵气]+4 / [再次行动] / [持续]：每次使用“水灵”牌时加1[灵气]  
  *[Qi]+4 / [Chase] / [Continuous]: Whenever you play a "Water Spirit" card, add 1 [Qi]*

#### 极·木灵巡林 (Ultimate - Wood Spirit - Forest Guard) — id 7000105
- **Lv1**: [木刺]+1 / 1攻×2 / [木灵]：若已加过生命则[再次行动]  
  *[Wood Thorn]+1 / 1 ATK × 2 / [Wood Spirit]: If you have already added HP, [Chase]*
- **Lv2**: [木刺]+1 / 1攻×3 / [木灵]：若已加过生命则[再次行动]  
  *[Wood Thorn]+1 / 1 ATK × 3 / [Wood Spirit]: If you have already added HP, [Chase]*
- **Lv3**: [木刺]+1 / 1攻×4 / [木灵]：若已加过生命则[再次行动]  
  *[Wood Thorn]+1 / 1 ATK × 4 / [Wood Spirit]: If you have already added HP, [Chase]*


### Phase 6 — 特殊 Special

#### 五行灵爆术 (Five Elements Spirit Blast) — id 7000052
- **Lv1**: [木灵]：25攻 / [火灵]：25攻 / [土灵]：25攻 / [金灵]：25攻 / [水灵]：25攻  
  *[Wood Spirit]: 25 ATK / [Fire Spirit]: 25 ATK / [Earth Spirit]: 25 ATK / [Metal Spirit]: 25 ATK / [Water Spirit]: 25 ATK*
- **Lv2**: [木灵]：28攻 / [火灵]：28攻 / [土灵]：28攻 / [金灵]：28攻 / [水灵]：28攻  
  *[Wood Spirit]: 28 ATK / [Fire Spirit]: 28 ATK / [Earth Spirit]: 28 ATK / [Metal Spirit]: 28 ATK / [Water Spirit]: 28 ATK*
- **Lv3**: [木灵]：31攻 / [火灵]：31攻 / [土灵]：31攻 / [金灵]：31攻 / [水灵]：31攻  
  *[Wood Spirit]: 31 ATK / [Fire Spirit]: 31 ATK / [Earth Spirit]: 31 ATK / [Metal Spirit]: 31 ATK / [Water Spirit]: 31 ATK*

#### 五行绽放 (Five Elements Blossom) — id 7000065
*消耗 Consumable*  
- **Lv1**: 使用全部[五行]灵印 / [再次行动] / [消耗]  
  *Play all [Five Elements] Spirit Seal cards / [Chase] / [Consumption]*
- **Lv2**: 使用全部[五行]灵印 / [再次行动] / [消耗]  
  *Play all [Five Elements] Spirit Seal cards / [Chase] / [Consumption]*
- **Lv3**: 使用全部[五行]灵印 / [再次行动] / [消耗]  
  *Play all [Five Elements] Spirit Seal cards / [Chase] / [Consumption]*


### Phase 0 — ?

#### 梦·五行流转 (Dream - Five Elements Circulation) — id 7000092
- **Lv1** ⟨template⟩: [灵气]+{anima} / [被动]：使用五行牌后，若触发[五行相生]则造成{otherParams[0]}[伤害]  
  *[Qi]+{anima} / [Passive]: After playing a [Five Elements] card, if [Five Element Generating Interaction] is triggered, deal {otherParams[0]} [DMG]*
- **Lv2** ⟨template⟩: [灵气]+{anima} / [被动]：使用五行牌后，若触发[五行相生]则造成{otherParams[0]}[伤害]  
  *[Qi]+{anima} / [Passive]: After playing a [Five Elements] card, if [Five Element Generating Interaction] is triggered, deal {otherParams[0]} [DMG]*
- **Lv3** ⟨template⟩: [灵气]+{anima} / [被动]：使用五行牌后，若触发[五行相生]则造成{otherParams[0]}[伤害]  
  *[Qi]+{anima} / [Passive]: After playing a [Five Elements] card, if [Five Element Generating Interaction] is triggered, deal {otherParams[0]} [DMG]*

#### 天机刻印ICON背面 — id 7003822
- (no text available)


## Sect: 锻玄宗 Duan Xuan Sect


### Phase 1 — 炼气 Meditation

#### 崩拳·戳 (Crash Fist - Poke) — id 10000001
- **Lv1**: 9攻 / 下一张崩拳多2攻  
  *9 ATK / The next Crash Fist adds 2 ATK*
- **Lv2**: 11攻 / 下一张崩拳多3攻  
  *11 ATK / The next Crash Fist adds 3 ATK*
- **Lv3**: 13攻 / 下一张崩拳多4攻  
  *13 ATK / The next Crash Fist adds 4 ATK*

#### 崩拳·封 (Crash Fist - Block) — id 10000002
- **Lv1**: 7攻 / [防]+2（下一张崩拳也附加此效果）  
  *7 ATK / [DEF]+2 (also triggered in the next Crash Fist)*
- **Lv2**: 9攻 / [防]+3（下一张崩拳也附加此效果）  
  *9 ATK / [DEF]+3 (also triggered in the next Crash Fist)*
- **Lv3**: 11攻 / [防]+4（下一张崩拳也附加此效果）  
  *11 ATK / [DEF]+4 (also triggered in the next Crash Fist)*

#### 崩拳·弹 (Crash Fist - Bounce) — id 10000003
*derived from: 掌心雷*  
- **Lv1**: 8攻 / 下一张崩拳耗生命时加回所耗生命  
  *8 ATK / When the next Crash Fist costs HP, add it back*
- **Lv2**: 11攻 / 下一张崩拳耗生命时加回所耗生命  
  *11 ATK / When the next Crash Fist costs HP, add it back*
- **Lv3**: 14攻 / 下一张崩拳耗生命时加回所耗生命  
  *14 ATK / When the next Crash Fist costs HP, add it back*

#### 锻拳 (Exercise Fist) — id 10000004
- **Lv1**: 6攻 / [体魄]+1  
  *6 ATK / [Physique]+1*
- **Lv2**: 9攻 / [体魄]+1  
  *9 ATK / [Physique]+1*
- **Lv3**: 12攻 / [体魄]+1  
  *12 ATK / [Physique]+1*

#### 劈山掌 (Mountain-Cleaving Palms) — id 10000005
- **Lv1**: 10攻 / 每有2[体魄]此牌少耗1生命  
  *10 ATK / 1 less HP Cost for each 2 [Physique]*
- **Lv2**: 13攻 / 每有2[体魄]此牌少耗1生命  
  *13 ATK / 1 less HP Cost for each 2 [Physique]*
- **Lv3**: 16攻 / 每有2[体魄]此牌少耗1生命  
  *16 ATK / 1 less HP Cost for each 2 [Physique]*

#### 抱气法 (Embracing Qi Technique) — id 10000006
- **Lv1**: [灵气]+1 / [体魄]+2 / 生命+1  
  *[Qi]+1 / [Physique]+2 / HP+1*
- **Lv2**: [灵气]+1 / [体魄]+2 / 生命+4  
  *[Qi]+1 / [Physique]+2 / HP+4*
- **Lv3**: [灵气]+1 / [体魄]+2 / 生命+7  
  *[Qi]+1 / [Physique]+2 / HP+7*

#### 破空爪 (Sky-Piercing Claw) — id 10000007
- **Lv1**: 12攻 / 自身加1层[内伤]  
  *12 ATK / Gain 1 stack of [Internal Injury]*
- **Lv2**: 15攻 / 自身加1层[内伤]  
  *15 ATK / Gain 1 stack of [Internal Injury]*
- **Lv3**: 18攻 / 自身加1层[内伤]  
  *18 ATK / Gain 1 stack of [Internal Injury]*

#### 罗刹扑 (Rakshasa Pouncing) — id 10000008
- **Lv1**: 8攻 / [灵气]+1 / 自身加1层[外伤]  
  *8 ATK / [Qi]+1 / Gain 1 stack of [Wound]*
- **Lv2**: 11攻 / [灵气]+1 / 自身加1层[外伤]  
  *11 ATK / [Qi]+1 / Gain 1 stack of [Wound]*
- **Lv3**: 14攻 / [灵气]+1 / 自身加1层[外伤]  
  *14 ATK / [Qi]+1 / Gain 1 stack of [Wound]*

#### 千斤坠 (Mountain Falling) — id 10000009
- **Lv1**: 6攻 / 随机减1层[负面状态]  
  *6 ATK / Reduce 1 stack of random [Debuff]*
- **Lv2**: 9攻 / 随机减1层[负面状态]  
  *9 ATK / Reduce 1 stack of random [Debuff]*
- **Lv3**: 12攻 / 随机减1层[负面状态]  
  *12 ATK / Reduce 1 stack of random [Debuff]*

#### 起势 (Gather Force) — id 10000010
- **Lv1**: 2攻 / [灵气]+1 / [气势]+2  
  *2 ATK / [Qi]+1 / [Force]+2*
- **Lv2**: 5攻 / [灵气]+1 / [气势]+2  
  *5 ATK / [Qi]+1 / [Force]+2*
- **Lv3**: 8攻 / [灵气]+1 / [气势]+2  
  *8 ATK / [Qi]+1 / [Force]+2*

#### 朝气蓬勃 (Vigorous Force) — id 10000011
- **Lv1**: 6攻（每有1层[气势]多1攻） / 耗1灵气：[气势]+2  
  *6 ATK (1 more ATK for each stack of [Force]) / Cost 1 Qi: [Force]+2*
- **Lv2**: 9攻（每有1层[气势]多1攻） / 耗1灵气：[气势]+2  
  *9 ATK (1 more ATK for each stack of [Force]) / Cost 1 Qi: [Force]+2*
- **Lv3**: 12攻（每有1层[气势]多1攻） / 耗1灵气：[气势]+2  
  *12 ATK (1 more ATK for each stack of [Force]) / Cost 1 Qi: [Force]+2*

#### 血气方刚 (Youthful Vigor) — id 10000012
- **Lv1**: 8攻 / 耗1灵气：追加4攻  
  *8 ATK / Cost 1 Qi: Make an additional 4 ATK*
- **Lv2**: 10攻 / 耗1灵气：追加6攻  
  *10 ATK / Cost 1 Qi: Make an additional 6 ATK*
- **Lv3**: 12攻 / 耗1灵气：追加8攻  
  *12 ATK / Cost 1 Qi: Make an additional 8 ATK*

#### 气势不绝 (Endless Force) — id 10000053
*持续 Continuous*  
- **Lv1**: [持续]：每当[气势]为0时，加4[气势]  
  *[Continuous]: Whenever you have no [Force], gain 4 [Force]*
- **Lv2**: [持续]：每当[气势]为0时，加5[气势]  
  *[Continuous]: Whenever you have no [Force], gain 5 [Force]*
- **Lv3**: [持续]：每当[气势]为0时，加6[气势]  
  *[Continuous]: Whenever you have no [Force], gain 6 [Force]*

#### 死缠烂打 (Endless Entanglement) — id 10000054
- **Lv1**: [体魄]+2 / 双方减14生命上限  
  *[Physique]+2 / Both players reduce 14 Max HP*
- **Lv2**: [体魄]+2 / 双方减20生命上限  
  *[Physique]+2 / Both players reduce 20 Max HP*
- **Lv3**: [体魄]+2 / 双方减26生命上限  
  *[Physique]+2 / Both players reduce 26 Max HP*

#### 梦·灵玄迷踪步 (Dream - Elusive Footwork) — id 10000069
*持续 Continuous*  
- **Lv1**: [灵气]+1 / [生命]+2 / [持续]：自身回合内首次获得[负面状态]后令对方也获得1层  
  *[Qi]+1 / HP+2 / [Continuous]: The first time you gain a [Debuff] during your turn, the opponent also gains 1 stack*
- **Lv2**: [灵气]+1 / [生命]+4 / [持续]：自身回合内首次获得[负面状态]后令对方也获得1层  
  *[Qi]+1 / HP+4 / [Continuous]: The first time you gain a [Debuff] during your turn, the opponent also gains 1 stack*
- **Lv3**: [灵气]+1 / [生命]+6 / [持续]：自身回合内首次获得[负面状态]后令对方也获得1层  
  *[Qi]+1 / HP+6 / [Continuous]: The first time you gain a [Debuff] during your turn, the opponent also gains 1 stack*

#### 梦·修罗吼 (Dream - Shura Roar) — id 10000070
- **Lv1**: [体魄]+2 / [生命]+4 / 双方加2层[内伤]  
  *[Physique]+2 / HP+4 / Both sides gain 2 [Internal Injury]*
- **Lv2**: [体魄]+2 / [生命]+6 / 双方加2层[内伤]  
  *[Physique]+2 / HP+6 / Both sides gain 2 [Internal Injury]*
- **Lv3**: [体魄]+3 / [生命]+7 / 双方加2层[内伤]  
  *[Physique]+3 / HP+7 / Both sides gain 2 [Internal Injury]*

#### 梦·崩拳封 (Dream - Crash Fist Block) — id 10000071
- **Lv1**: [防]+12 / 下张崩拳多2[攻]  
  *[DEF]+12 / The next Crash Fist gains 2 ATK*
- **Lv2**: [防]+14 / 下张崩拳多3[攻]  
  *[DEF]+14 / The next Crash Fist gains 3 ATK*
- **Lv3**: [防]+18 / 每加过7[防]，下张崩拳就多1[攻]  
  *[DEF]+18 / For every 7 [DEF] gained, the next Crash Fist gains 1 ATK*

#### 梦·锻神开海 (Dream - Exercise Soul) — id 10000072
- **Lv1**: 5攻 / [防]+2 / [体魄]+2  
  *5 ATK / [DEF]+2 / [Physique]+2*
- **Lv2**: 6攻 / [防]+2 / [体魄]+3  
  *6 ATK / [DEF]+2 / [Physique]+3*
- **Lv3**: 7攻 / [防]+2 / [体魄]+4  
  *7 ATK / [DEF]+2 / [Physique]+4*

#### 梦·冲霄破浪 (Dream - Surging Waves) — id 10000073
*消耗 Consumable*  
- **Lv1**: [灵气]+2 / 生命+3 / [身法]+4 / [消耗]  
  *[Qi]+2 / HP+3 / [Agility]+4 / [Consumption]*
- **Lv2**: [灵气]+2 / 生命+5 / [身法]+4 / [消耗]  
  *[Qi]+2 / HP+5 / [Agility]+4 / [Consumption]*
- **Lv3**: [灵气]+2 / 生命+7 / [身法]+4 / [消耗]  
  *[Qi]+2 / HP+7 / [Agility]+4 / [Consumption]*

#### 梦·崩拳突 (Dream - Crash Fist Blitz) — id 10000074
- **Lv1**: 若有[身法]或[气势]，此牌和下张崩拳多2[攻] / 10攻  
  *If you have [Agility] or [Force], this card and next Crash Fist gain 2 ATK / 10 ATK*
- **Lv2**: 若有[身法]或[气势]，此牌和下张崩拳多3[攻] / 10攻  
  *If you have [Agility] or [Force], this card and next Crash Fist gain 3 ATK / 10 ATK*
- **Lv3**: 若有[身法]或[气势]，此牌和下张崩拳多4[攻] / 10攻  
  *If you have [Agility] or [Force], this card and next Crash Fist gain 4 ATK / 10 ATK*

#### 梦·锻筋 (Dream - Exercise Tendons) — id 10000075
- **Lv1**: [体魄]+2 / [防]+7  
  *[Physique]+2 / [DEF]+7*
- **Lv2**: [体魄]+2 / [防]+10  
  *[Physique]+2 / [DEF]+10*
- **Lv3**: [体魄]+3 / [防]+13  
  *[Physique]+3 / [DEF]+13*

#### 梦·崩拳弹 (Dream - Crash Fist Bounce) — id 10000076
*持续 Continuous*  
- **Lv1**: [防]+8 / [持续]2次：使用耗生命的牌后，加所耗生命值的[防]  
  *[DEF]+8 / [Continuous] 2 times: After playing a card that costs HP, add the HP cost as [DEF]*
- **Lv2**: [防]+12 / [持续]2次：使用耗生命的牌后，加所耗生命值的[防]  
  *[DEF]+12 / [Continuous] 2 times: After playing a card that costs HP, add the HP cost as [DEF]*
- **Lv3**: [防]+12 / [持续]3次：使用耗生命的牌后，加所耗生命值的[防]  
  *[DEF]+12 / [Continuous] 3 times: After playing a card that costs HP, add the HP cost as [DEF]*

#### 梦·冥影身法 (Dream - Styx Agility) — id 10000077
- **Lv1**: 5攻×2 / 自身有[负面状态]则多1攻  
  *5 ATK×2 / If you have any [Debuff], +1 ATK*
- **Lv2**: 6攻×2 / 自身有[负面状态]则多1攻  
  *6 ATK×2 / If you have any [Debuff], +1 ATK*
- **Lv3**: 7攻×2 / 自身有[负面状态]则多1攻  
  *7 ATK×2 / If you have any [Debuff], +1 ATK*

#### 梦·朝气蓬勃 (Dream - Vigorous Force) — id 10000078
- **Lv1**: 6攻（每加过1层[气势]多1攻）  
  *6 ATK (For each stack of [Force] gained, add 1 more ATK)*
- **Lv2**: 8攻（每加过1层[气势]多1攻）  
  *8 ATK (For each stack of [Force] gained, add 1 more ATK)*
- **Lv3**: 10攻（每加过1层[气势]多1攻）  
  *10 ATK (For each stack of [Force] gained, add 1 more ATK)*

#### 梦·劈山掌 (Dream - Mountain-Cleaving Palms) — id 10000079
- **Lv1**: 8攻（每加过2[体魄]就多1攻）  
  *8 ATK (For every 2 [Physique] gained, add 1 more ATK)*
- **Lv2**: 10攻（每加过2[体魄]就多1攻）  
  *10 ATK (For every 2 [Physique] gained, add 1 more ATK)*
- **Lv3**: 12攻（每加过2[体魄]就多1攻）  
  *12 ATK (For every 2 [Physique] gained, add 1 more ATK)*

#### 梦·崩天步 (Dream - Crash Footwork) — id 10000080
- **Lv1**: [防]+8 / [身法]+2 / [被动]：此牌和后一格的牌算作崩拳  
  *[DEF]+8 / [Agility]+2 / [Passive]: This card and the card in the next slot count as Crash Fist*
- **Lv2**: [防]+11 / [身法]+2 / [被动]：此牌和后一格的牌算作崩拳  
  *[DEF]+11 / [Agility]+2 / [Passive]: This card and the card in the next slot count as Crash Fist*
- **Lv3**: [防]+14 / [身法]+2 / [被动]：此牌和后一格的牌算作崩拳  
  *[DEF]+14 / [Agility]+2 / [Passive]: This card and the card in the next slot count as Crash Fist*

#### 梦·迎风掌 (Dream - Windward Palms) — id 10000081
- **Lv1**: 3攻×2 / 已加过[防]则追加3攻  
  *3 ATK×2 / If you have gained [DEF], make an additional 3 ATK*
- **Lv2**: 4攻×2 / 已加过[防]则追加3攻  
  *4 ATK×2 / If you have gained [DEF], make an additional 3 ATK*
- **Lv3**: 5攻×2 / 已加过[防]则追加3攻  
  *5 ATK×2 / If you have gained [DEF], make an additional 3 ATK*

#### 梦·崩拳连崩 (Dream - Crash Fist Continue) — id 10000082
- **Lv1**: 3攻×2 / 使用下张崩拳后追加2攻×2  
  *3 ATK×2 / After playing the next Crash Fist, make an additional 2 ATK×2*
- **Lv2**: 4攻×2 / 使用下张崩拳后追加2攻×2  
  *4 ATK×2 / After playing the next Crash Fist, make an additional 2 ATK×2*
- **Lv3**: 5攻×2 / 使用下张崩拳后追加2攻×2  
  *5 ATK×2 / After playing the next Crash Fist, make an additional 2 ATK×2*

#### 梦·荷重前行 (Dream - Bearing the Load) — id 10000083
- **Lv1**: [防]+7（每有1层[负面状态]多加1防）  
  *[DEF]+7 (add 1 extra DEF for each stack of [Debuff] you have)*
- **Lv2**: [防]+10（每有1层[负面状态]多加1防）  
  *[DEF]+10 (add 1 extra DEF for each stack of [Debuff] you have)*
- **Lv3**: [防]+13（每有1层[负面状态]多加1防）  
  *[DEF]+13 (add 1 extra DEF for each stack of [Debuff] you have)*

#### 梦·威震四方 (Dream - Gather Intense Force) — id 10000084
- **Lv1**: 生命+2 / [气势]+3 / [被动]：[气势]效果由每点多10%攻改为每点多1攻  
  *HP+2 / [Force]+3 / [Passive]: [Force] effect changes from +10% ATK per stack to +1 ATK per stack*
- **Lv2**: 生命+4 / [气势]+3 / [被动]：[气势]效果由每点多10%攻改为每点多1攻  
  *HP+4 / [Force]+3 / [Passive]: [Force] effect changes from +10% ATK per stack to +1 ATK per stack*
- **Lv3**: 生命+6 / [气势]+3 / [被动]：[气势]效果由每点多10%攻改为每点多1攻  
  *HP+6 / [Force]+3 / [Passive]: [Force] effect changes from +10% ATK per stack to +1 ATK per stack*

#### 梦·气若悬河 (Dream - Majestic Qi) — id 10000085
*持续 Continuous*  
- **Lv1**: [灵气]+2 / [气势]+1 / [持续]2次：攻击时先加1[气势]  
  *[Qi]+2 / [Force]+1 / [Continuous] 2 times: When attacking, add 1 [Force] first*
- **Lv2**: [灵气]+2 / [气势]+1 / [持续]3次：攻击时先加1[气势]  
  *[Qi]+2 / [Force]+1 / [Continuous] 3 times: When attacking, add 1 [Force] first*
- **Lv3**: [灵气]+2 / [气势]+1 / [持续]4次：攻击时先加1[气势]  
  *[Qi]+2 / [Force]+1 / [Continuous] 4 times: When attacking, add 1 [Force] first*

#### 梦·磅礴之势 (Dream - Overwhelming Force) — id 10000086
- **Lv1**: 若有[灵气]或[气势]： / [体魄]+2 / 生命+6  
  *If you have [Qi] or [Force]: / [Physique]+2 / HP+6*
- **Lv2**: 若有[灵气]或[气势]： / [体魄]+3 / 生命+8  
  *If you have [Qi] or [Force]: / [Physique]+3 / HP+8*
- **Lv3**: 若有[灵气]或[气势]： / [体魄]+4 / 生命+10  
  *If you have [Qi] or [Force]: / [Physique]+4 / HP+10*

#### 梦·锻拳 (Dream - Exercise Fist) — id 10000087
- **Lv1**: 6攻 / [体魄]+2 / 使用下张牌时加2[体魄] / 此牌算作崩拳  
  *6 ATK / [Physique]+2 / When playing the next card, gain 2 [Physique] / This card counts as a Crash Fist*
- **Lv2**: 8攻 / [体魄]+2 / 使用下张牌时加2[体魄] / 此牌算作崩拳  
  *8 ATK / [Physique]+2 / When playing the next card, gain 2 [Physique] / This card counts as a Crash Fist*
- **Lv3**: 10攻 / [体魄]+2 / 使用下张牌时加2[体魄] / 此牌算作崩拳  
  *10 ATK / [Physique]+2 / When playing the next card, gain 2 [Physique] / This card counts as a Crash Fist*

#### 梦·岿然不动 (Dream - Standing Firm) — id 10000088
*持续 Continuous*  
- **Lv1**: [防]+3 / [持续]：每次加[防]时造成2点[伤害]  
  *[DEF]+3 / [Continuous]: Whenever you gain [DEF], deal 2 [DMG]*
- **Lv2**: [防]+6 / [持续]：每次加[防]时造成2点[伤害]  
  *[DEF]+6 / [Continuous]: Whenever you gain [DEF], deal 2 [DMG]*
- **Lv3**: [防]+9 / [持续]：每次加[防]时造成2点[伤害]  
  *[DEF]+9 / [Continuous]: Whenever you gain [DEF], deal 2 [DMG]*

#### 梦·崩拳连崩 (Dream - Crash Fist Continue) — id 10000089
- **Lv1**: 3攻×2 / 使用下张崩拳后追加2攻×2  
  *3 ATK×2 / After playing the next Crash Fist, make an additional 2 ATK×2*
- **Lv2**: 4攻×2 / 使用下张崩拳后追加2攻×2  
  *4 ATK×2 / After playing the next Crash Fist, make an additional 2 ATK×2*
- **Lv3**: 5攻×2 / 使用下张崩拳后追加2攻×2  
  *5 ATK×2 / After playing the next Crash Fist, make an additional 2 ATK×2*


### Phase 2 — 筑基 Foundation

#### 崩拳·撼 (Crash Fist - Shake) — id 10000013
- **Lv1**: 10攻 / 使用下一张崩拳时加2[气势]  
  *10 ATK / When you play the next Crash Fist, gain 2 [Force]*
- **Lv2**: 11攻 / 使用下一张崩拳时加3[气势]  
  *11 ATK / When you play the next Crash Fist, gain 3 [Force]*
- **Lv3**: 12攻 / 使用下一张崩拳时加4[气势]  
  *12 ATK / When you play the next Crash Fist, gain 4 [Force]*

#### 崩拳·缠 (Crash Fist - Entangle) — id 10000014
- **Lv1**: 10攻 / 使用下一张崩拳时施加1层[外伤]  
  *10 ATK / When you play the next Crash Fist, apply 1 stack of [Wound]*
- **Lv2**: 11攻 / 使用下一张崩拳时施加2层[外伤]  
  *11 ATK / When you play the next Crash Fist, apply 2 stacks of [Wound]*
- **Lv3**: 12攻 / 使用下一张崩拳时施加3层[外伤]  
  *12 ATK / When you play the next Crash Fist, apply 3 stacks of [Wound]*

#### 崩拳·突 (Crash Fist - Blitz) — id 10000015
- **Lv1**: 10攻 / [碎防]（下一张崩拳也附加此效果）  
  *10 ATK / [Smash DEF] (also triggered in the next Crash Fist)*
- **Lv2**: 14攻 / [碎防]（下一张崩拳也附加此效果）  
  *14 ATK / [Smash DEF] (also triggered in the next Crash Fist)*
- **Lv3**: 18攻 / [碎防]（下一张崩拳也附加此效果）  
  *18 ATK / [Smash DEF] (also triggered in the next Crash Fist)*

#### 锻筋 (Exercise Tendons) — id 10000016
- **Lv1**: 5攻 / [体魄]+2 / [体魄]≥15：[防]+4  
  *5 ATK / [Physique]+2 / [Physique]≥15: [DEF]+4*
- **Lv2**: 7攻 / [体魄]+2 / [体魄]≥15：[防]+6  
  *7 ATK / [Physique]+2 / [Physique]≥15: [DEF]+6*
- **Lv3**: 9攻 / [体魄]+2 / [体魄]≥15：[防]+8  
  *9 ATK / [Physique]+2 / [Physique]≥15: [DEF]+8*

#### 探马掌 (Detect-Horse Palms) — id 10000017
- **Lv1**: 7攻 / 每有2[体魄]加1[防]（上限8）  
  *7 ATK / Add 1 [DEF] for each 2 [Physique] (up to 8)*
- **Lv2**: 9攻 / 每有2[体魄]加1[防]（上限11）  
  *9 ATK / Add 1 [DEF] for each 2 [Physique] (up to 11)*
- **Lv3**: 11攻 / 每有2[体魄]加1[防]（上限14）  
  *11 ATK / Add 1 [DEF] for each 2 [Physique] (up to 14)*

#### 风冥爪 (Gale Shadow Claw) — id 10000018
- **Lv1**: 4攻×2 / [灵气]+2 / 自身加3层[破绽]  
  *4 ATK × 2 / [Qi]+2 / Gain 3 stacks of [Flaw]*
- **Lv2**: 6攻×2 / [灵气]+2 / 自身加3层[破绽]  
  *6 ATK × 2 / [Qi]+2 / Gain 3 stacks of [Flaw]*
- **Lv3**: 8攻×2 / [灵气]+2 / 自身加3层[破绽]  
  *8 ATK × 2 / [Qi]+2 / Gain 3 stacks of [Flaw]*

#### 夜鬼啸 (Ghost Howling) — id 10000019
- **Lv1**: 14攻 / [无视防御] / 自身加3层[虚弱]  
  *14 ATK / [Ignore DEF] / Gain 3 stacks of [Weakened]*
- **Lv2**: 18攻 / [无视防御] / 自身加3层[虚弱]  
  *18 ATK / [Ignore DEF] / Gain 3 stacks of [Weakened]*
- **Lv3**: 22攻 / [无视防御] / 自身加3层[虚弱]  
  *22 ATK / [Ignore DEF] / Gain 3 stacks of [Weakened]*

#### 岿然不动 (Standing Firm) — id 10000021
- **Lv1**: [防]+4 / [气势]+2 / 耗1灵气：生命+5  
  *[DEF]+4 / [Force]+2 / Cost 1 Qi: HP+5*
- **Lv2**: [防]+5 / [气势]+3 / 耗1灵气：生命+5  
  *[DEF]+5 / [Force]+3 / Cost 1 Qi: HP+5*
- **Lv3**: [防]+6 / [气势]+4 / 耗1灵气：生命+5  
  *[DEF]+6 / [Force]+4 / Cost 1 Qi: HP+5*

#### 势大力沉 (Strong Force) — id 10000022
- **Lv1**: 9攻 / 耗1灵气：此牌获得[碎防]并多4攻  
  *9 ATK / Cost 1 Qi: This card gains [Smash DEF] and adds 4 ATK*
- **Lv2**: 12攻 / 耗1灵气：此牌获得[碎防]并多5攻  
  *12 ATK / Cost 1 Qi: This card gains [Smash DEF] and adds 5 ATK*
- **Lv3**: 15攻 / 耗1灵气：此牌获得[碎防]并多6攻  
  *15 ATK / Cost 1 Qi: This card gains [Smash DEF] and adds 6 ATK*

#### 浩然正气 (Magnanimous Righteousness) — id 10000023
- **Lv1**: [灵气]+1 / [防]+4 / 获得2层[辟邪]  
  *[Qi]+1 / [DEF]+4 / Gain 2 stacks of [Hexproof]*
- **Lv2**: [灵气]+1 / [防]+8 / 获得3层[辟邪]  
  *[Qi]+1 / [DEF]+8 / Gain 3 stacks of [Hexproof]*
- **Lv3**: [灵气]+1 / [防]+12 / 获得4层[辟邪]  
  *[Qi]+1 / [DEF]+12 / Gain 4 stacks of [Hexproof]*

#### 气沉丹田 (Sinking Qi) — id 10000032
- **Lv1**: [灵气]+2 / [生命]+2  
  *[Qi]+2 / [HP]+2*
- **Lv2**: [灵气]+2 / [生命]+6  
  *[Qi]+2 / [HP]+6*
- **Lv3**: [灵气]+2 / [生命]+10  
  *[Qi]+2 / [HP]+10*

#### 百毒不侵 (Toxin Immunity) — id 10000055
*持续 Continuous*  
- **Lv1**: 生命及上限+5 / [持续]：自身回合结束时，每有1层[负面状态]加1生命（最多6）  
  *HP and Max HP+5 / [Continuous]: At the end of your turn, heal 1 HP for each stack of [Debuff] (up to 6)*
- **Lv2**: 生命及上限+9 / [持续]：自身回合结束时，每有1层[负面状态]加1生命（最多9）  
  *HP and Max HP+9 / [Continuous]: At the end of your turn, heal 1 HP for each stack of [Debuff] (up to 9)*
- **Lv3**: 生命及上限+13 / [持续]：自身回合结束时，每有1层[负面状态]加1生命（最多12）  
  *HP and Max HP+13 / [Continuous]: At the end of your turn, heal 1 HP for each stack of [Debuff] (up to 12)*

#### 醉卧逍遥 (Lying Drunk) — id 10000056
- **Lv1**: 3攻 / [身法]+8 / 下一张普通攻击额外攻击3次  
  *3 ATK / [Agility]+8 / Next Normal Attack makes 3 additional attacks*
- **Lv2**: 3攻 / [身法]+10 / 下一张普通攻击额外攻击4次  
  *3 ATK / [Agility]+10 / Next Normal Attack makes 4 additional attacks*
- **Lv3**: 3攻 / [身法]+12 / 下一张普通攻击额外攻击5次  
  *3 ATK / [Agility]+12 / Next Normal Attack makes 5 additional attacks*

#### 金刚捣碓 (Vajra Smash) — id 10000097
- **Lv1**: 7攻 / [防]+4 / 最多耗2[灵气]：每耗1[灵气]此牌多3攻和3[防]  
  *7 ATK / [DEF]+4 / Spend up to 2 [Qi]: for each spent, this card adds 3 more ATK and 3 [DEF]*
- **Lv2**: 11攻 / [防]+4 / 最多耗2[灵气]：每耗1[灵气]此牌多3攻和3[防]  
  *11 ATK / [DEF]+4 / Spend up to 2 [Qi]: for each spent, this card adds 3 more ATK and 3 [DEF]*
- **Lv3**: 15攻 / [防]+4 / 最多耗2[灵气]：每耗1[灵气]此牌多3攻和3[防]  
  *15 ATK / [DEF]+4 / Spend up to 2 [Qi]: for each spent, this card adds 3 more ATK and 3 [DEF]*


### Phase 3 — 金丹 Virtuoso

#### 气若悬河 (Majestic Qi) — id 10000020
- **Lv1**: [灵气]+2 / [气势]+1 / 自身下2次攻击时先加1[气势]  
  *[Qi]+2 / [Force]+1 / Add 1 [Force] first during your next 2 attacks*
- **Lv2**: [灵气]+3 / [气势]+1 / 自身下3次攻击时先加1[气势]  
  *[Qi]+3 / [Force]+1 / Add 1 [Force] first during your next 3 attacks*
- **Lv3**: [灵气]+4 / [气势]+1 / 自身下4次攻击时先加1[气势]  
  *[Qi]+4 / [Force]+1 / Add 1 [Force] first during your next 4 attacks*

#### 崩拳·截脉 (Crash Fist - Truncate) — id 10000024
- **Lv1**: 随机转移自身1层[负面状态]给对手（下一张崩拳也附加此效果） / 9攻  
  *Transfer 1 stack of your random [Debuff] to the opponent (also triggered in the next Crash Fist) / 9 ATK*
- **Lv2**: 随机转移自身1层[负面状态]给对手（下一张崩拳也附加此效果） / 13攻  
  *Transfer 1 stack of your random [Debuff] to the opponent (also triggered in the next Crash Fist) / 13 ATK*
- **Lv3**: 随机转移自身1层[负面状态]给对手（下一张崩拳也附加此效果） / 17攻  
  *Transfer 1 stack of your random [Debuff] to the opponent (also triggered in the next Crash Fist) / 17 ATK*

#### 崩天步 (Crash Footwork) — id 10000026
*持续 Continuous*  
- **Lv1**: [灵气]+1 / [身法]+4 / [持续]：所有牌都可算作“崩拳”  
  *[Qi]+1 / [Agility]+4 / [Continuous]: Every card can be regarded as "Crash Fist"*
- **Lv2**: [灵气]+2 / [身法]+4 / [持续]：所有牌都可算作“崩拳”  
  *[Qi]+2 / [Agility]+4 / [Continuous]: Every card can be regarded as "Crash Fist"*
- **Lv3**: [灵气]+3 / [身法]+4 / [持续]：所有牌都可算作“崩拳”  
  *[Qi]+3 / [Agility]+4 / [Continuous]: Every card can be regarded as "Crash Fist"*

#### 锻骨 (Exercise Bones) — id 10000027
- **Lv1**: [体魄]+1 / [生命]+3 / 下2次攻击时多3攻并加1[体魄]  
  *[Physique]+1 / [HP]+3 / Add 3 ATK and 1 [Physique] during your next 2 attacks*
- **Lv2**: [体魄]+1 / [生命]+4 / 下3次攻击时多3攻并加1[体魄]  
  *[Physique]+1 / [HP]+4 / Add 3 ATK and 1 [Physique] during your next 3 attacks*
- **Lv3**: [体魄]+1 / [生命]+5 / 下4次攻击时多3攻并加1[体魄]  
  *[Physique]+1 / [HP]+5 / Add 3 ATK and 1 [Physique] during your next 4 attacks*

#### 迎风掌 (Windward Palms) — id 10000028
- **Lv1**: 4攻×2 / 每有6[体魄]多1攻（上限3）  
  *4 ATK × 2 / 1 more ATK (up to 3) for each 6 [Physique]*
- **Lv2**: 5攻×2 / 每有6[体魄]多1攻（上限5）  
  *5 ATK × 2 / 1 more ATK (up to 5) for each 6 [Physique]*
- **Lv3**: 6攻×2 / 每有6[体魄]多1攻（上限7）  
  *6 ATK × 2 / 1 more ATK (up to 7) for each 6 [Physique]*

#### 饿虎扑食 (Tiger Pouncing) — id 10000029
- **Lv1**: 自身每有1层[负面状态]，此牌少耗1[灵气] / 18攻  
  *Reduce Qi cost by 1 for each stack of [Debuff] you have / 18 ATK*
- **Lv2**: 自身每有1层[负面状态]，此牌少耗1[灵气] / 22攻  
  *Reduce Qi cost by 1 for each stack of [Debuff] you have / 22 ATK*
- **Lv3**: 自身每有1层[负面状态]，此牌少耗1[灵气] / 26攻  
  *Reduce Qi cost by 1 for each stack of [Debuff] you have / 26 ATK*

#### 双鬼拍门 (Double Trouble) — id 10000030
- **Lv1**: 双方各加1层[内伤]和1层[外伤] / 6攻×2  
  *Apply and gain 1 stack of [Internal Injury] and 1 stack of [Wound] / 6 ATK × 2*
- **Lv2**: 双方各加2层[内伤]和1层[外伤] / 7攻×2  
  *Apply and gain 2 stacks of [Internal Injury] and 1 stack of [Wound] / 7 ATK × 2*
- **Lv3**: 双方各加2层[内伤]和2层[外伤] / 8攻×2  
  *Apply and gain 2 stacks of [Internal Injury] and 2 stacks of [Wound] / 8 ATK × 2*

#### 荷重前行 (Bearing the Load) — id 10000031
- **Lv1**: [体魄]+3 / 自身加2层[困缚] / [防]+8(每有1层[负面状态]多1）  
  *[Physique]+3 / Gain 2 [Entangled] / [DEF]+8 (1 more [DEF] for each stack of [Debuff])*
- **Lv2**: [体魄]+3 / 自身加3层[困缚] / [防]+11(每有1层[负面状态]多1）  
  *[Physique]+3 / Gain 3 [Entangled] / [DEF]+11 (1 more [DEF] for each stack of [Debuff])*
- **Lv3**: [体魄]+3 / 自身加4层[困缚] / [防]+14(每有1层[负面状态]多1）  
  *[Physique]+3 / Gain 4 [Entangled] / [DEF]+14 (1 more [DEF] for each stack of [Debuff])*

#### 势如破竹 (Mighty Force) — id 10000033
- **Lv1**: 最多耗2灵气：每点加1[气势]，且此牌多3攻 / 10攻  
  *Costs up to 2 Qi: For each, gain 1 [Force] and add 3 ATK / 10 ATK*
- **Lv2**: 最多耗3灵气：每点加1[气势]，且此牌多3攻 / 11攻  
  *Costs up to 3 Qi: For each, gain 1 [Force] and add 3 ATK / 11 ATK*
- **Lv3**: 最多耗4灵气：每点加1[气势]，且此牌多3攻 / 12攻  
  *Costs up to 4 Qi: For each, gain 1 [Force] and add 3 ATK / 12 ATK*

#### 踏破九霄 (Sailing through Sky) — id 10000034
- **Lv1**: [气势]+3 / [身法]+6  
  *[Force]+3 / [Agility]+6*
- **Lv2**: [气势]+4 / [身法]+6  
  *[Force]+4 / [Agility]+6*
- **Lv3**: [气势]+5 / [身法]+6  
  *[Force]+5 / [Agility]+6*

#### 崩拳·降龙 (Crash Fist - Subdue Dragon) — id 10000036
- **Lv1**: 10攻 / 使用下一张崩拳时加5[防]并多5攻  
  *10 ATK / The next Crash Fist adds 5 [DEF] and 5 ATK*
- **Lv2**: 12攻 / 使用下一张崩拳时加7[防]并多7攻  
  *12 ATK / The next Crash Fist adds 7 [DEF] and 7 ATK*
- **Lv3**: 14攻 / 使用下一张崩拳时加9[防]并多9攻  
  *14 ATK / The next Crash Fist adds 9 [DEF] and 9 ATK*

#### 灵草药浴 (Herbal Bath) — id 10000058
- **Lv1**: [炼化]：[体魄上限]+4，[体魄]+4  
  *[Absorb]: [Physique] Cap+4, [Physique]+4*
- **Lv2**: [炼化]：[体魄上限]+8，[体魄]+8  
  *[Absorb]: [Physique] Cap+8, [Physique]+8*
- **Lv3**: [炼化]：[体魄上限]+16，[体魄]+16  
  *[Absorb]: [Physique] Cap+16, [Physique]+16*

#### 破釜沉舟 (Break Pots and Sink Boats) — id 10000061
- **Lv1**: 自身生命上限减少80% / 获得3层[气势]、[护体]和[加攻]  
  *Lose 80% Max HP / Gain 3 stacks of [Force], [Guard Up] and [Increase ATK]*
- **Lv2**: 自身生命上限减少80% / 获得4层[气势]、[护体]和[加攻]  
  *Lose 80% Max HP / Gain 4 stacks of [Force], [Guard Up] and [Increase ATK]*
- **Lv3**: 自身生命上限减少80% / 获得5层[气势]、[护体]和[加攻]  
  *Lose 80% Max HP / Gain 5 stacks of [Force], [Guard Up] and [Increase ATK]*

#### 醉拳架势 (Drunken Fist Stance) — id 10000090
*持续 Continuous*  
- **Lv1**: [体魄]+2 / 生命+2 / 获得2层[破绽] / [持续]（不可叠加）：每失去1层[破绽]就获得1层[加攻]  
  *[Physique]+2 / HP+2 / Gain 2 [Flaw] / [Continuous] (non-stackable): Whenever you lose 1 stack of [Flaw], gain 1 [Increase ATK]*
- **Lv2**: [体魄]+3 / 生命+5 / 获得2层[破绽] / [持续]（不可叠加）：每失去1层[破绽]就获得1层[加攻]  
  *[Physique]+3 / HP+5 / Gain 2 [Flaw] / [Continuous] (non-stackable): Whenever you lose 1 stack of [Flaw], gain 1 [Increase ATK]*
- **Lv3**: [体魄]+4 / 生命+8 / 获得2层[破绽] / [持续]：每失去1层[破绽]就获得1层[加攻]  
  *[Physique]+4 / HP+8 / Gain 2 [Flaw] / [Continuous]: Whenever you lose 1 stack of [Flaw], gain 1 [Increase ATK]*


### Phase 4 — 元婴 Immortality

#### 崩拳·寸劲 (Crash Fist - Inch Force) — id 10000025
- **Lv1**: 10攻 / 受双倍[气势]加成（下一张崩拳也附加此效果，不可叠加）  
  *10 ATK /  This card receive 2x bonus from [Force] (also triggered in the next Crash Fist, non-stackable)*
- **Lv2**: 14攻 / 受双倍[气势]加成（下一张崩拳也附加此效果，不可叠加）  
  *14 ATK /  This card receive 2x bonus from [Force] (also triggered in the next Crash Fist, non-stackable)*
- **Lv3**: 18攻 / 受双倍[气势]加成（下一张崩拳也附加此效果，不可叠加）  
  *18 ATK /  This card receive 2x bonus from [Force] (also triggered in the next Crash Fist, non-stackable)*

#### 崩拳·连崩 (Crash Fist - Continue) — id 10000035
- **Lv1**: 11攻 / 此牌触发的崩拳效果保留至下一张崩拳  
  *11 ATK / The Crash Fist effect triggered remain for the next one*
- **Lv2**: 16攻 / 此牌触发的崩拳效果保留至下一张崩拳  
  *16 ATK / The Crash Fist effect triggered remain for the next one*
- **Lv3**: 21攻 / 此牌触发的崩拳效果保留至下一张崩拳  
  *21 ATK / The Crash Fist effect triggered remain for the next one*

#### 锻髓 (Exercise Marrow) — id 10000037
- **Lv1**: [体魄]+3 / 回复生命上限8%的生命  
  *[Physique]+3 / Restore HP of 8% Max HP*
- **Lv2**: [体魄]+3 / 回复生命上限12%的生命  
  *[Physique]+3 / Restore HP of 12% Max HP*
- **Lv3**: [体魄]+3 / 回复生命上限16%的生命  
  *[Physique]+3 / Restore HP of 16% Max HP*

#### 鹤步 (Crane Footwork) — id 10000038
- **Lv1**: 生命+4 / 每有4[体魄]加1[身法]（上限10）  
  *HP+4 / Add 1 [Agility] (up to 10) for each 4 [Physique]*
- **Lv2**: 生命+5 / 每有4[体魄]加1[身法]（上限13）  
  *HP+5 / Add 1 [Agility] (up to 13) for each 4 [Physique]*
- **Lv3**: 生命+6 / 每有4[体魄]加1[身法]（上限16）  
  *HP+6 / Add 1 [Agility] (up to 16) for each 4 [Physique]*

#### 冥影身法 (Styx Agility) — id 10000039
- **Lv1**: 自身加1层[减攻] / [身法]+10  
  *Gain 1 stack of [Decrease ATK] / [Agility]+10*
- **Lv2**: 自身加1层[减攻] / [身法]+14  
  *Gain 1 stack of [Decrease ATK] / [Agility]+14*
- **Lv3**: 自身加2层[减攻] / [身法]+18  
  *Gain 2 stacks of [Decrease ATK] / [Agility]+18*

#### 玄手夺魂 (Soul Seizing) — id 10000040
- **Lv1**: 吸取对方7生命 / 自身每有1层[负面状态]就多吸取1点（最多加7）  
  *Steal 7 HP from the opponent / Steal 1 more HP for each stack of [Debuff] you have (up to 7 more)*
- **Lv2**: 吸取对方10生命 / 自身每有1层[负面状态]就多吸取1点（最多加10）  
  *Steal 10 HP from the opponent / Steal 1 more HP for each stack of [Debuff] you have (up to 10 more)*
- **Lv3**: 吸取对方13生命 / 自身每有1层[负面状态]就多吸取1点（最多加13）  
  *Steal 13 HP from the opponent / Steal 1 more HP for each stack of [Debuff] you have (up to 13 more)*

#### 冲霄破浪 (Surging Waves) — id 10000042
- **Lv1**: [灵气]+1 / 每有1[灵气]加1[气势] / [身法]+5  
  *[Qi]+1 / Add 1 [Force] for each [Qi] / [Agility]+5*
- **Lv2**: [灵气]+2 / 每有1[灵气]加1[气势] / [身法]+5  
  *[Qi]+2 / Add 1 [Force] for each [Qi] / [Agility]+5*
- **Lv3**: [灵气]+3 / 每有1[灵气]加1[气势] / [身法]+5  
  *[Qi]+3 / Add 1 [Force] for each [Qi] / [Agility]+5*

#### 磅礴之势 (Overwhelming Force) — id 10000043
- **Lv1**: 耗尽[气势]，每点加4[防]并造成3[伤害] / [身法]+5  
  *Exhaust [Force]. Add 4 [DEF] and Deal 3 [DMG] for each point exhausted / [Agility]+5*
- **Lv2**: 耗尽[气势]，每点加4[防]并造成4[伤害] / [身法]+6  
  *Exhaust [Force]. Add 4 [DEF] and Deal 4 [DMG] for each point exhausted / [Agility]+6*
- **Lv3**: 耗尽[气势]，每点加4[防]并造成5[伤害] / [身法]+7  
  *Exhaust [Force]. Add 4 [DEF] and Deal 5 [DMG] for each point exhausted / [Agility]+7*

#### 崩灭心法 (Crash Citta-Dharma) — id 10000044
*持续 Continuous*  
- **Lv1**: [气势]+2 / [持续]：每次使用[耗生命]的牌时加1[气势]  
  *[Force]+2 / [Continuous]: Whenever you play a [Cost HP] card, gain 1 [Force] first*
- **Lv2**: [气势]+3 / [持续]：每次使用[耗生命]的牌时加1[气势]  
  *[Force]+3 / [Continuous]: Whenever you play a [Cost HP] card, gain 1 [Force] first*
- **Lv3**: [气势]+4 / [持续]：每次使用[耗生命]的牌时加1[气势]  
  *[Force]+4 / [Continuous]: Whenever you play a [Cost HP] card, gain 1 [Force] first*

#### 灵玄迷踪步 (Elusive Footwork) — id 10000050
*持续 Continuous · derived from: 震卦, 野马分鬃*  
- **Lv1**: [灵气]+1 / [身法]+2 / [持续]：在自身的每个回合首次失去生命时，加1[灵气]和1[身法]  
  *[Qi]+1 / [Agility]+2 / [Continuous]: Add 1 [Qi] and 1 [Agility] for the first HP lost in each your turn*
- **Lv2**: [灵气]+2 / [身法]+3 / [持续]：在自身的每个回合首次失去生命时，加1[灵气]和1[身法]  
  *[Qi]+2 / [Agility]+3 / [Continuous]: Add 1 [Qi] and 1 [Agility] for the first HP lost in each your turn*
- **Lv3**: [灵气]+3 / [身法]+4 / [持续]：在自身的每个回合首次失去生命时，加1[灵气]和1[身法]  
  *[Qi]+3 / [Agility]+4 / [Continuous]: Add 1 [Qi] and 1 [Agility] for the first HP lost in each your turn*

#### 力若疯魔 (Strength Driven Mad) — id 10000057
- **Lv1**: 每有10[体魄]就获得1层[加攻]和[内伤]  
  *Gain 1 stack of [Increase ATK] and [Internal Injury] for each 10 [Physique]*
- **Lv2**: 每有9[体魄]就获得1层[加攻]和[内伤]  
  *Gain 1 stack of [Increase ATK] and [Internal Injury] for each 9 [Physique]*
- **Lv3**: 每有8[体魄]就获得1层[加攻]和[内伤]  
  *Gain 1 stack of [Increase ATK] and [Internal Injury] for each 8 [Physique]*

#### 崩拳·双影 (Crash Fist - Double) — id 10000060
- **Lv1**: 10攻 / 下一张崩拳生效2次  
  *10 ATK / Next "Crash Fist" will trigger twice*
- **Lv2**: 15攻 / 下一张崩拳生效2次  
  *15 ATK / Next "Crash Fist" will trigger twice*
- **Lv3**: 20攻 / 下一张崩拳生效2次  
  *20 ATK / Next "Crash Fist" will trigger twice*

#### 幽冥三点手 (Styx Three Hit) — id 10000067
- **Lv1**: 2攻×3 / 每有30生命上限多1攻  
  *2 ATK × 3 / 1 more ATK for each 30 Max HP*
- **Lv2**: 2攻×3 / 每有22生命上限多1攻  
  *2 ATK × 3 / 1 more ATK for each 22 Max HP*
- **Lv3**: 2攻×3 / 每有16生命上限多1攻  
  *2 ATK × 3 / 1 more ATK for each 16 Max HP*

#### 玄灵愈体 (Mystic Spirit Healing) — id 10000091
- **Lv1**: [灵气]+3 / 获得2层[内伤] / 自身每有1[灵气]或1层[负面状态]就加1生命及上限  
  *[Qi]+3 / Gain 2 stack(s) of [Internal Injury] / Add 1 HP and Max HP for each [Qi] or stack of [Debuff]*
- **Lv2**: [灵气]+5 / 获得3层[内伤] / 自身每有1[灵气]或1层[负面状态]就加1生命及上限  
  *[Qi]+5 / Gain 3 stack(s) of [Internal Injury] / Add 1 HP and Max HP for each [Qi] or stack of [Debuff]*
- **Lv3**: [灵气]+7 / 获得4层[内伤] / 自身每有1[灵气]或1层[负面状态]就加1生命及上限  
  *[Qi]+7 / Gain 4 stack(s) of [Internal Injury] / Add 1 HP and Max HP for each [Qi] or stack of [Debuff]*

#### 凌空飞扫 (Aerial Sweep) — id 10000092
- **Lv1**: 8攻（每有1[灵气]多1攻） / 最多耗2[灵气]：每耗1点加3[身法]并减1层[负面状态]  
  *8 ATK (1 more ATK for each [Qi]) / Spend up to 2 [Qi]: for each spent, add 3 [Agility] and remove 1 stack of [Debuff]*
- **Lv2**: 13攻（每有1[灵气]多1攻） / 最多耗2[灵气]：每耗1点加3[身法]并减1层[负面状态]  
  *13 ATK (1 more ATK for each [Qi]) / Spend up to 2 [Qi]: for each spent, add 3 [Agility] and remove 1 stack of [Debuff]*
- **Lv3**: 18攻（每有1[灵气]多1攻） / 最多耗2[灵气]：每耗1点加3[身法]并减1层[负面状态]  
  *18 ATK (1 more ATK for each [Qi]) / Spend up to 2 [Qi]: for each spent, add 3 [Agility] and remove 1 stack of [Debuff]*


### Phase 5 — 化神 Incarnation

#### 修罗吼 (Shura Roar) — id 10000041
- **Lv1**: 双方各加4层[内伤] / 自身每有2层[负面状态]加1[灵气]和1生命  
  *Both players gain 4 stacks of [Internal Injury] / Add 1 [Qi] and 1 HP for each 2 stacks of [Debuff] you have*
- **Lv2**: 双方各加6层[内伤] / 自身每有2层[负面状态]加1[灵气]和1生命  
  *Both players gain 6 stacks of [Internal Injury] / Add 1 [Qi] and 1 HP for each 2 stacks of [Debuff] you have*
- **Lv3**: 双方各加8层[内伤] / 自身每有2层[负面状态]加1[灵气]和1生命  
  *Both players gain 8 stacks of [Internal Injury] / Add 1 [Qi] and 1 HP for each 2 stacks of [Debuff] you have*

#### 崩拳·闪击 (Crash Fist - Blink) — id 10000045
*derived from: 白鹤亮翅*  
- **Lv1**: 5攻 / [身法]+7（下一张崩拳也附加此效果）  
  *5 ATK / [Agility]+7 (also triggered in the next Crash Fist)*
- **Lv2**: 7攻 / [身法]+8（下一张崩拳也附加此效果）  
  *7 ATK / [Agility]+8 (also triggered in the next Crash Fist)*
- **Lv3**: 9攻 / [身法]+9（下一张崩拳也附加此效果）  
  *9 ATK / [Agility]+9 (also triggered in the next Crash Fist)*

#### 崩拳·惊触 (Crash Fist - Shocked) — id 10000046
- **Lv1**: 10攻 / 使用下一张崩拳后追加1攻（本场战斗中每失去过5生命多1攻）  
  *10 ATK / After you played the next Crash Fist, make an additional 1 ATK (1 more ATK for each 5 HP you have lost)*
- **Lv2**: 16攻 / 使用下一张崩拳后追加1攻（本场战斗中每失去过5生命多1攻）  
  *16 ATK / After you played the next Crash Fist, make an additional 1 ATK (1 more ATK for each 5 HP you have lost)*
- **Lv3**: 22攻 / 使用下一张崩拳后追加1攻（本场战斗中每失去过5生命多1攻）  
  *22 ATK / After you played the next Crash Fist, make an additional 1 ATK (1 more ATK for each 5 HP you have lost)*

#### 百杀破境掌 (Realm-Killing Palms) — id 10000047
- **Lv1**: 3攻（本轮战斗每加过4[体魄]多1攻） / 每有25[体魄]追加1次攻击  
  *3 ATK (1 more ATK for each 4 [Physique] you have gained in this battle) / Make an additional ATK for each 25 [Physique]*
- **Lv2**: 4攻（本轮战斗每加过3[体魄]多1攻） / 每有25[体魄]追加1次攻击  
  *4 ATK (1 more ATK for each 3 [Physique] you have gained in this battle) / Make an additional ATK for each 25 [Physique]*
- **Lv3**: 5攻（本轮战斗每加过2[体魄]多1攻） / 每有25[体魄]追加1次攻击  
  *5 ATK (1 more ATK for each 2 [Physique] you have gained in this battle) / Make an additional ATK for each 25 [Physique]*

#### 锻神开海 (Exercise Soul) — id 10000048
- **Lv1**: 4攻 / [体魄]+3 / [体魄]≥50：获得1层[加攻] / [体魄]≥65：[身法]+5  
  *4 ATK / [Physique]+3 / [Physique]≥50: Gain 1 [Increase ATK] / [Physique]≥65: [Agility]+5*
- **Lv2**: 8攻 / [体魄]+4 / [体魄]≥50：获得1层[加攻] / [体魄]≥65：[身法]+6  
  *8 ATK / [Physique]+4 / [Physique]≥50: Gain 1 [Increase ATK] / [Physique]≥65: [Agility]+6*
- **Lv3**: 12攻 / [体魄]+5 / [体魄]≥50：获得1层[加攻] / [体魄]≥65：[身法]+7  
  *12 ATK / [Physique]+5 / [Physique]≥50: Gain 1 [Increase ATK] / [Physique]≥65: [Agility]+7*

#### 万魂破军 (Thousand Souls Strike) — id 10000049
- **Lv1**: 将自身最多2层[负面状态]转为[气势] / 11攻（受3倍[气势]加成）  
  *Turn no more than 2 stacks of [Debuff] into [Force] / 11 ATK (Receive 3x bonus from [Force])*
- **Lv2**: 将自身最多3层[负面状态]转为[气势] / 14攻（受3倍[气势]加成）  
  *Turn no more than 3 stacks of [Debuff] into [Force] / 14 ATK (Receive 3x bonus from [Force])*
- **Lv3**: 将自身最多4层[负面状态]转为[气势] / 17攻（受3倍[气势]加成）  
  *Turn no more than 4 stacks of [Debuff] into [Force] / 17 ATK (Receive 3x bonus from [Force])*

#### 威震四方 (Gather Intense Force) — id 10000051
- **Lv1**: [防]+8 / [气势]上限+3 / [气势]+3  
  *[DEF]+8 / [Force] Cap+3 / [Force]+3*
- **Lv2**: [防]+10 / [气势]上限+4 / [气势]+4  
  *[DEF]+10 / [Force] Cap+4 / [Force]+4*
- **Lv3**: [防]+12 / [气势]上限+5 / [气势]+5  
  *[DEF]+12 / [Force] Cap+5 / [Force]+5*

#### 天地浩荡 (Vast Universe) — id 10000052
*derived from: 巽卦*  
- **Lv1**: 10攻 / 生命+4 / [身法]+4（每剩1[气势]多2）  
  *10 ATK / HP+4 / [Agility]+4 (2 more [Agility] for each [Force])*
- **Lv2**: 12攻 / 生命+6 / [身法]+5（每剩1[气势]多2）  
  *12 ATK / HP+6 / [Agility]+5 (2 more [Agility] for each [Force])*
- **Lv3**: 14攻 / 生命+8 / [身法]+6（每剩1[气势]多2）  
  *14 ATK / HP+8 / [Agility]+6 (2 more [Agility] for each [Force])*

#### 破茧化蝶 (Break Cocoon) — id 10000062
- **Lv1**: [身法]+5 / 清空自身[负面状态]，每层加2[体魄]和2生命  
  *[Agility]+5 / Clear [Debuff]. Add 2 [Physique] and 2 HP for each stack of [Debuff] cleared*
- **Lv2**: [身法]+10 / 清空自身[负面状态]，每层加2[体魄]和2生命  
  *[Agility]+10 / Clear [Debuff]. Add 2 [Physique] and 2 HP for each stack of [Debuff] cleared*
- **Lv3**: [身法]+15 / 清空自身[负面状态]，每层加2[体魄]和2生命  
  *[Agility]+15 / Clear [Debuff]. Add 2 [Physique] and 2 HP for each stack of [Debuff] cleared*

#### 鬼音葬魂 (Eerie Melody Buries Soul) — id 10000064
- **Lv1**: 双方各加3层[内伤]、[破绽]、[虚弱]、[困缚]和[外伤]  
  *Both players gain 3 stacks of [Internal Injury], [Flaw], [Weakened], [Entangled] and [Wound]*
- **Lv2**: 双方各加4层[内伤]、[破绽]、[虚弱]、[困缚]和[外伤]  
  *Both players gain 4 stacks of [Internal Injury], [Flaw], [Weakened], [Entangled] and [Wound]*
- **Lv3**: 双方各加5层[内伤]、[破绽]、[虚弱]、[困缚]和[外伤]  
  *Both players gain 5 stacks of [Internal Injury], [Flaw], [Weakened], [Entangled] and [Wound]*

#### 玄心斩魄 (Soul Cleaving) — id 10000068
*derived from: 坤卦*  
- **Lv1**: 向对方施加自身已有的[负面状态]各2层 / 8攻（攻击时自身[负面状态]的效果当做[气势]）  
  *Apply 2 stacks of each kind of [Debuff] you have / 8 ATK (your [Debuff] is regarded as [Force] in this attack)*
- **Lv2**: 向对方施加自身已有的[负面状态]各2层 / 14攻（攻击时自身[负面状态]的效果当做[气势]）  
  *Apply 2 stacks of each kind of [Debuff] you have / 14 ATK (your [Debuff] is regarded as [Force] in this attack)*
- **Lv3**: 向对方施加自身已有的[负面状态]各2层 / 20攻（攻击时自身[负面状态]的效果当做[气势]）  
  *Apply 2 stacks of each kind of [Debuff] you have / 20 ATK (your [Debuff] is regarded as [Force] in this attack)*

#### 崩拳·碎骨 (Crash Fist - Shatter) — id 10000093
- **Lv1**: 此牌[耗生命]时向对方造成等量[伤害]（下一张[崩拳]也附加此效果） / 3攻×2 / [碎防]  
  *When this card costs HP, deal equal [DMG] to the opponent (the next "Crash Fist" also gains this effect) / 3 ATK × 2 / [Smash DEF]*
- **Lv2**: 此牌[耗生命]时向对方造成等量[伤害]（下一张[崩拳]也附加此效果） / 3攻×3 / [碎防]  
  *When this card costs HP, deal equal [DMG] to the opponent (the next "Crash Fist" also gains this effect) / 3 ATK × 3 / [Smash DEF]*
- **Lv3**: 此牌[耗生命]时向对方造成等量[伤害]（下一张[崩拳]也附加此效果） / 3攻×4 / [碎防]  
  *When this card costs HP, deal equal [DMG] to the opponent (the next "Crash Fist" also gains this effect) / 3 ATK × 4 / [Smash DEF]*

#### 万魂破军 (Thousand Souls Strike) — id 10000094
- **Lv1**: 每用过1次[耗生命]的牌就加1[气势] / 10攻（每有1[气势]多1攻）  
  *Gain 1 [Force] for each [HP cost] card played / 10 ATK (1 more ATK for each [Force])*
- **Lv2**: 每用过1次[耗生命]的牌就加1[气势] / 16攻（每有1[气势]多1攻）  
  *Gain 1 [Force] for each [HP cost] card played / 16 ATK (1 more ATK for each [Force])*
- **Lv3**: 每用过1次[耗生命]的牌就加1[气势] / 22攻（每有1[气势]多1攻）  
  *Gain 1 [Force] for each [HP cost] card played / 22 ATK (1 more ATK for each [Force])*

#### 血影遁术 (Blood Shadow Escape) — id 10000095
- **Lv1**: 生命+8 / [身法]+8 / 下1次使用[耗生命]的牌时每耗1生命就加1[身法]  
  *HP+8 / [Agility]+8 / The next time you play a [HP cost] card, add 1 [Agility] for each HP spent*
- **Lv2**: 生命+14 / [身法]+8 / 下1次使用[耗生命]的牌时每耗1生命就加1[身法]  
  *HP+14 / [Agility]+8 / The next time you play a [HP cost] card, add 1 [Agility] for each HP spent*
- **Lv3**: 生命+20 / [身法]+8 / 下1次使用[耗生命]的牌时每耗1生命就加1[身法]  
  *HP+20 / [Agility]+8 / The next time you play a [HP cost] card, add 1 [Agility] for each HP spent*

#### 锻灵指 (Spirit Forging Finger) — id 10000096
- **Lv1**: 1攻×3 / [灵气]+2 / [体魄]+2（每有2[灵气]多加1[体魄]）  
  *1 ATK × 3 / [Qi]+2 / [Physique]+2 (1 more [Physique] for each 2 [Qi])*
- **Lv2**: 1攻×4 / [灵气]+3 / [体魄]+3（每有2[灵气]多加1[体魄]）  
  *1 ATK × 4 / [Qi]+3 / [Physique]+3 (1 more [Physique] for each 2 [Qi])*
- **Lv3**: 1攻×5 / [灵气]+4 / [体魄]+4（每有2[灵气]多加1[体魄]）  
  *1 ATK × 5 / [Qi]+4 / [Physique]+4 (1 more [Physique] for each 2 [Qi])*

#### 极·崩天步 (Ultimate - Crash Footwork) — id 10000098
*持续 Continuous*  
- **Lv1**: [身法]+10 / [持续]：所有牌都可算作“崩拳”  
  *[Agility]+10 / [Continuous]: Every card can be regarded as "Crash Fist"*
- **Lv2**: [灵气]+2 / [身法]+10 / [持续]：所有牌都可算作“崩拳”  
  *[Qi]+2 / [Agility]+10 / [Continuous]: Every card can be regarded as "Crash Fist"*
- **Lv3**: [灵气]+4 / [身法]+10 / [持续]：所有牌都可算作“崩拳”  
  *[Qi]+4 / [Agility]+10 / [Continuous]: Every card can be regarded as "Crash Fist"*

#### 极·迎风掌 (Ultimate - Windward Palms) — id 10000099
- **Lv1**: 4攻×2 / 每有7[体魄]多1攻  
  *4 ATK × 2 / 1 more ATK for each 7 [Physique]*
- **Lv2**: [体魄]+3 / 4攻×2 / 每有7[体魄]多1攻  
  *[Physique]+3 / 4 ATK × 2 / 1 more ATK for each 7 [Physique]*
- **Lv3**: [体魄]+6 / 4攻×2 / 每有7[体魄]多1攻  
  *[Physique]+6 / 4 ATK × 2 / 1 more ATK for each 7 [Physique]*


### Phase 6 — 特殊 Special

#### 无尽崩绝 (Endless Crash) — id 10000065
*消耗 Consumable*  
- **Lv1**: 随机使用5张崩拳的1级效果（不耗生命） / [消耗]  
  *Trigger the effect of 5 Lv.1 Crash Fist cards (without Cost HP) / [Consumption]*
- **Lv2**: 随机使用5张崩拳的2级效果（不耗生命） / [消耗]  
  *Trigger the effect of 5 Lv.2 Crash Fist cards (without Cost HP) / [Consumption]*
- **Lv3**: 随机使用5张崩拳的3级效果（不耗生命） / [消耗]  
  *Trigger the effect of 5 Lv.3 Crash Fist cards (without Cost HP) / [Consumption]*

#### 返璞归真 (Return to Simplicity) — id 10000066
*持续 Continuous*  
- **Lv1**: [体魄]+5 / [持续]：自身每有5[体魄]，之后使用普通攻击时就多1攻并加1[身法]  
  *[Physique]+5 / [Continuous]: For each 5 [Physique] you have, add 1 ATK and 1 [Agility] in your Normal Attack*
- **Lv2**: [体魄]+10 / [持续]：自身每有5[体魄]，之后使用普通攻击时就多1攻并加1[身法]  
  *[Physique]+10 / [Continuous]: For each 5 [Physique] you have, add 1 ATK and 1 [Agility] in your Normal Attack*
- **Lv3**: [体魄]+15 / [持续]：自身每有5[体魄]，之后使用普通攻击时就多1攻并加1[身法]  
  *[Physique]+15 / [Continuous]: For each 5 [Physique] you have, add 1 ATK and 1 [Agility] in your Normal Attack*


## Side job (副职): 炼丹师 Elixirist


### Phase 1 — 炼气 Meditation

#### 小还丹 (Small Recover Elixir) — id 2000001
*消耗 Consumable*  
- **Lv1**: 生命+8 / [消耗]  
  *HP+8 / [Consumption]*
- **Lv2**: 生命+12 / [消耗]  
  *HP+12 / [Consumption]*
- **Lv3**: 生命+16 / [消耗]  
  *HP+16 / [Consumption]*

#### 培元丹 (Fundamental Elixir) — id 2000002
*消耗 Consumable*  
- **Lv1**: [灵气]+2 / [防]+3 / [消耗]  
  *[Qi]+2 / [DEF]+3 / [Consumption]*
- **Lv2**: [灵气]+3 / [防]+5 / [消耗]  
  *[Qi]+3 / [DEF]+5 / [Consumption]*
- **Lv3**: [灵气]+4 / [防]+7 / [消耗]  
  *[Qi]+4 / [DEF]+7 / [Consumption]*

#### 地灵丹 (Earth Spirit Elixir) — id 2000003
*消耗 Consumable*  
- **Lv1**: [防]+11 / [消耗]  
  *[DEF]+11 / [Consumption]*
- **Lv2**: [防]+16 / [消耗]  
  *[DEF]+16 / [Consumption]*
- **Lv3**: [防]+21 / [消耗]  
  *[DEF]+21 / [Consumption]*


### Phase 2 — 筑基 Foundation

#### 驱邪丹 (Exorcism Elixir) — id 2000004
*消耗 Consumable*  
- **Lv1**: [防]+8 / 重复2次：随机[负面状态]减3层 / [消耗]  
  *[DEF]+8 / Repeat 2 times: Random [Debuff] decrease 3 stacks / [Consumption]*
- **Lv2**: [防]+12 / 重复3次：随机[负面状态]减3层 / [消耗]  
  *[DEF]+12 / Repeat 3 times: Random [Debuff] decrease 3 stacks / [Consumption]*
- **Lv3**: [防]+16 / 重复4次：随机[负面状态]减3层 / [消耗]  
  *[DEF]+16 / Repeat 4 times: Random [Debuff] decrease 3 stacks / [Consumption]*

#### 飞云丹 (Cloud Elixir) — id 2000005
*消耗 Consumable*  
- **Lv1**: [灵气]+2 / 下2次攻击[无视防御] / [消耗]  
  *[Qi]+2 / Next 2 attacks [Ignore DEF] / [Consumption]*
- **Lv2**: [灵气]+3 / 下3次攻击[无视防御] / [消耗]  
  *[Qi]+3 / Next 3 attacks [Ignore DEF] / [Consumption]*
- **Lv3**: [灵气]+4 / 下4次攻击[无视防御] / [消耗]  
  *[Qi]+4 / Next 4 attacks [Ignore DEF] / [Consumption]*

#### 锻体丹 (Bodybuilding Elixir) — id 2000006
- **Lv1**: [炼化]：生命上限永久加1  
  *[Absorb]: Max HP increased by 1 in this game*
- **Lv2**: [炼化]：生命上限永久加2  
  *[Absorb]: Max HP increased by 2 in this game*
- **Lv3**: [炼化]：生命上限永久加4  
  *[Absorb]: Max HP increased by 4 in this game*


### Phase 3 — 金丹 Virtuoso

#### 疗伤丹 (Healing Elixir) — id 2000007
*消耗 Consumable*  
- **Lv1**: 生命+7 / 每剩余1点灵气额外加2生命 / [消耗]  
  *HP+7 / Add 2 HP for each Qi / [Consumption]*
- **Lv2**: 生命+12 / 每剩余1点灵气额外加2生命 / [消耗]  
  *HP+12 / Add 2 HP for each Qi / [Consumption]*
- **Lv3**: 生命+17 / 每剩余1点灵气额外加2生命 / [消耗]  
  *HP+17 / Add 2 HP for each Qi / [Consumption]*

#### 神力丹 (Divine Power Elixir) — id 2000008
*消耗 Consumable*  
- **Lv1**: 获得1层[加攻] / [消耗]  
  *Gain 1 stack of [Increase ATK] / [Consumption]*
- **Lv2**: 获得2层[加攻] / [消耗]  
  *Gain 2 stacks of [Increase ATK] / [Consumption]*
- **Lv3**: 获得3层[加攻] / [消耗]  
  *Gain 3 stacks of [Increase ATK] / [Consumption]*

#### 还魂丹 (Resurrection Elixir) — id 2000009
- **Lv1**: [炼化]：[命元]+2  
  *[Absorb]: [Destiny]+2*
- **Lv2**: [炼化]：[命元]+4  
  *[Absorb]: [Destiny]+4*
- **Lv3**: [炼化]：[命元]+8  
  *[Absorb]: [Destiny]+8*


### Phase 4 — 元婴 Immortality

#### 聚灵丹 (Spiritage Elixir) — id 2000010
*消耗 Consumable*  
- **Lv1**: [灵气]+4 / [消耗]  
  *[Qi]+4 / [Consumption]*
- **Lv2**: [灵气]+6 / [消耗]  
  *[Qi]+6 / [Consumption]*
- **Lv3**: [灵气]+8 / [消耗]  
  *[Qi]+8 / [Consumption]*

#### 大还丹 (Great Recover Elixir) — id 2000011
*消耗 Consumable*  
- **Lv1**: 生命上限+13 / 生命+13 / [消耗]  
  *Max HP+13 / HP+13 / [Consumption]*
- **Lv2**: 生命上限+19 / 生命+19 / [消耗]  
  *Max HP+19 / HP+19 / [Consumption]*
- **Lv3**: 生命上限+25 / 生命+25 / [消耗]  
  *Max HP+25 / HP+25 / [Consumption]*

#### 洗髓丹 (Talent Elixir) — id 2000012
- **Lv1**: [炼化]：额外加1[修为]  
  *[Absorb]: Add 1 more [Cultivation]*
- **Lv2**: [炼化]：额外加2[修为]  
  *[Absorb]: Add 2 more [Cultivation]*
- **Lv3**: [炼化]：额外加4[修为]  
  *[Absorb]: Add 4 more [Cultivation]*


### Phase 5 — 化神 Incarnation

#### 冰灵护体丹 (Ice Spirit Guard Elixir) — id 2000013
*消耗 Consumable*  
- **Lv1**: 获得2层[护体] / [消耗]  
  *Gain 2 stacks of [Guard Up] / [Consumption]*
- **Lv2**: 获得3层[护体] / [消耗]  
  *Gain 3 stacks of [Guard Up] / [Consumption]*
- **Lv3**: 获得4层[护体] / [消耗]  
  *Gain 4 stacks of [Guard Up] / [Consumption]*

#### 锻体玄丹 (Great Bodybuilding Elixir) — id 2000014
- **Lv1**: [炼化]：生命上限永久加2  
  *[Absorb]: Max HP increased by 2 in this game*
- **Lv2**: [炼化]：生命上限永久加4  
  *[Absorb]: Max HP increased by 4 in this game*
- **Lv3**: [炼化]：生命上限永久加8  
  *[Absorb]: Max HP increased by 8 in this game*

#### 悟道丹 (Enlightenment Elixir) — id 2000015
- **Lv1**: [炼化]：随机升级1张手牌或卡组中的1级牌  
  *[Absorb]: Upgrade 1 Level 1 card(s) in your hand or deck randomly*
- **Lv2**: [炼化]：随机升级2张手牌或卡组中的1级牌  
  *[Absorb]: Upgrade 2 Level 1 card(s) in your hand or deck randomly*
- **Lv3**: [炼化]：随机升级4张手牌或卡组中的1级牌  
  *[Absorb]: Upgrade 4 Level 1 card(s) in your hand or deck randomly*


## Side job (副职): 符咒师 Fuluist


### Phase 1 — 炼气 Meditation

#### 奔雷符 (Thunder Fulu) — id 3000001
*消耗 Consumable*  
- **Lv1**: 造成4～12[伤害] / [消耗]  
  *Deal 4～12 [DMG] / [Consumption]*
- **Lv2**: 造成7～15[伤害] / [消耗]  
  *Deal 7～15 [DMG] / [Consumption]*
- **Lv3**: 造成10～18[伤害] / [消耗]  
  *Deal 10～18 [DMG] / [Consumption]*

#### 护灵符 (Guard Spirit Fulu) — id 3000002
*消耗 Consumable*  
- **Lv1**: [灵气]+1 / [防]+7 / [消耗]  
  *[Qi]+1 / [DEF]+7 / [Consumption]*
- **Lv2**: [灵气]+1 / [防]+11 / [消耗]  
  *[Qi]+1 / [DEF]+11 / [Consumption]*
- **Lv3**: [灵气]+1 / [防]+15 / [消耗]  
  *[Qi]+1 / [DEF]+15 / [Consumption]*

#### 锐金符 (Sharp Metal Fulu) — id 3000003
*消耗 Consumable*  
- **Lv1**: 造成8[伤害] / [消耗]  
  *Deal 8 [DMG] / [Consumption]*
- **Lv2**: 造成11[伤害] / [消耗]  
  *Deal 11 [DMG] / [Consumption]*
- **Lv3**: 造成14[伤害] / [消耗]  
  *Deal 14 [DMG] / [Consumption]*


### Phase 2 — 筑基 Foundation

#### 水气符 (Mist Fulu) — id 3000004
*消耗 Consumable*  
- **Lv1**: [灵气]+1 / 造成7[伤害] / [消耗]  
  *[Qi]+1 / Deal 7 [DMG] / [Consumption]*
- **Lv2**: [灵气]+1 / 造成11[伤害] / [消耗]  
  *[Qi]+1 / Deal 11 [DMG] / [Consumption]*
- **Lv3**: [灵气]+1 / 造成15[伤害] / [消耗]  
  *[Qi]+1 / Deal 15 [DMG] / [Consumption]*

#### 火云符 (Fire Cloud Fulu) — id 3000005
*消耗 Consumable*  
- **Lv1**: 对方减12生命及上限 / [消耗]  
  *Opponent loses 12 HP and Max HP / [Consumption]*
- **Lv2**: 对方减16生命及上限 / [消耗]  
  *Opponent loses 16 HP and Max HP / [Consumption]*
- **Lv3**: 对方减20生命及上限 / [消耗]  
  *Opponent loses 20 HP and Max HP / [Consumption]*

#### 清心咒 (Calm Incantation) — id 3000006
- **Lv1**: [灵气]+2 / 全部[负面状态]减2层  
  *[Qi]+2 / All [Debuff] reduces 2 stacks*
- **Lv2**: [灵气]+3 / 全部[负面状态]减3层  
  *[Qi]+3 / All [Debuff] reduces 3 stacks*
- **Lv3**: [灵气]+4 / 全部[负面状态]减4层  
  *[Qi]+4 / All [Debuff] reduces 4 stacks*


### Phase 3 — 金丹 Virtuoso

#### 吸灵符 (Spirit Absorb Fulu) — id 3000007
*消耗 Consumable*  
- **Lv1**: [灵气]+2 / 对方减1[灵气] / [消耗]  
  *[Qi]+2 / Opponent loses 1 [Qi] / [Consumption]*
- **Lv2**: [灵气]+3 / 对方减2[灵气] / [消耗]  
  *[Qi]+3 / Opponent loses 2 [Qi] / [Consumption]*
- **Lv3**: [灵气]+4 / 对方减3[灵气] / [消耗]  
  *[Qi]+4 / Opponent loses 3 [Qi] / [Consumption]*

#### 瘴气符 (Miasma Fulu) — id 3000008
*消耗 Consumable*  
- **Lv1**: 施加2层[内伤] / [消耗]  
  *Apply 2 stacks of [Internal Injury] / [Consumption]*
- **Lv2**: 施加3层[内伤] / [消耗]  
  *Apply 3 stacks of [Internal Injury] / [Consumption]*
- **Lv3**: 施加4层[内伤] / [消耗]  
  *Apply 4 stacks of [Internal Injury] / [Consumption]*

#### 寒冰咒 (Ice Incantation) — id 3000009
- **Lv1**: 重复2次：对方减4生命  
  *Repeat 2 times: Opponent loses 4 HP*
- **Lv2**: 重复3次：对方减4生命  
  *Repeat 3 times: Opponent loses 4 HP*
- **Lv3**: 重复4次：对方减4生命  
  *Repeat 4 times: Opponent loses 4 HP*


### Phase 4 — 元婴 Immortality

#### 聚气咒 (Spiritage Incantation) — id 3000010
- **Lv1**: [灵气]+3 / 每有1[灵气]加1[防]（最多7）  
  *[Qi]+3 / Add 1 [DEF] for each [Qi] (up to 7)*
- **Lv2**: [灵气]+4 / 每有1[灵气]加1[防]（最多13）  
  *[Qi]+4 / Add 1 [DEF] for each [Qi] (up to 13)*
- **Lv3**: [灵气]+5 / 每有1[灵气]加1[防]（最多19）  
  *[Qi]+5 / Add 1 [DEF] for each [Qi] (up to 19)*

#### 扰心符 (Distubing Fulu) — id 3000011
*消耗 Consumable*  
- **Lv1**: 施加3层[破绽] / [消耗]  
  *Apply 3 stacks of [Flaw] / [Consumption]*
- **Lv2**: 施加4层[破绽] / [消耗]  
  *Apply 4 stacks of [Flaw] / [Consumption]*
- **Lv3**: 施加5层[破绽] / [消耗]  
  *Apply 5 stacks of [Flaw] / [Consumption]*

#### 弱体符 (Weaken Fulu) — id 3000012
*消耗 Consumable*  
- **Lv1**: 施加2层[虚弱] / [消耗]  
  *Apply 2 stacks of [Weakened] / [Consumption]*
- **Lv2**: 施加3层[虚弱] / [消耗]  
  *Apply 3 stacks of [Weakened] / [Consumption]*
- **Lv3**: 施加4层[虚弱] / [消耗]  
  *Apply 4 stacks of [Weakened] / [Consumption]*


### Phase 5 — 化神 Incarnation

#### 千里神行符 (Divine Walk Fulu) — id 3000013
*消耗 Consumable*  
- **Lv1**: [灵气]+2 / [消耗] / [再次行动]  
  *[Qi]+2 / [Consumption] / [Chase]*
- **Lv2**: [灵气]+4 / [消耗] / [再次行动]  
  *[Qi]+4 / [Consumption] / [Chase]*
- **Lv3**: [灵气]+6 / [消耗] / [再次行动]  
  *[Qi]+6 / [Consumption] / [Chase]*

#### 镇魂封元符 (Soul Requiem Fulu) — id 3000014
*消耗 Consumable*  
- **Lv1**: 对方减15%当前生命及当前生命上限 / 对方减2[灵气] / [消耗]  
  *Opponent loses 15% of current HP and current Max HP / Opponent loses 2 [Qi] / [Consumption]*
- **Lv2**: 对方减20%当前生命及当前生命上限 / 对方减3[灵气] / [消耗]  
  *Opponent loses 20% of current HP and current Max HP / Opponent loses 3 [Qi] / [Consumption]*
- **Lv3**: 对方减25%当前生命及当前生命上限 / 对方减4[灵气] / [消耗]  
  *Opponent loses 25% of current HP and current Max HP / Opponent loses 4 [Qi] / [Consumption]*

#### 万邪入体咒 (Thousand Evil Incantation) — id 3000015
- **Lv1**: 施加2层[内伤]、2层[破绽]、1层[虚弱]  
  *Apply 2 stacks of [Internal Injury], 2 stacks of [Flaw], and 1 stack of [Weakened]*
- **Lv2**: 施加3层[内伤]、2层[破绽]、2层[虚弱]  
  *Apply 3 stacks of [Internal Injury], 2 stacks of [Flaw], and 2 stacks of [Weakened]*
- **Lv3**: 施加3层[内伤]、3层[破绽]、3层[虚弱]  
  *Apply 3 stacks of [Internal Injury], 3 stacks of [Flaw], and 3 stacks of [Weakened]*


## Side job (副职): 琴师 Musician


### Phase 1 — 炼气 Meditation

#### 破音 (Cracking Voice) — id 5000001
- **Lv1**: 6攻（若用过琴师牌则多1攻） / [无视防御]  
  *6 ATK (1 more ATK if you've played a Musician Card) / [Ignore DEF]*
- **Lv2**: 9攻（若用过琴师牌则多1攻） / [无视防御]  
  *9 ATK (1 more ATK if you've played a Musician Card) / [Ignore DEF]*
- **Lv3**: 12攻（若用过琴师牌则多1攻） / [无视防御]  
  *12 ATK (1 more ATK if you've played a Musician Card) / [Ignore DEF]*

#### 土行曲 (Earth Tune) — id 5000002
- **Lv1**: 双方加14[防]  
  *Both players add 14 [DEF]*
- **Lv2**: 双方加20[防]  
  *Both players add 20 [DEF]*
- **Lv3**: 双方加26[防]  
  *Both players add 26 [DEF]*

#### 逍遥曲 (Carefree Tune) — id 5000003
*持续 Continuous*  
- **Lv1**: [持续]：双方的[普通攻击]加4攻  
  *[Continuous]: Both players' [Normal Attack] add 4 ATK*
- **Lv2**: [持续]：双方的[普通攻击]加6攻  
  *[Continuous]: Both players' [Normal Attack] add 6 ATK*
- **Lv3**: [持续]：双方的[普通攻击]加9攻  
  *[Continuous]: Both players' [Normal Attack] add 9 ATK*


### Phase 2 — 筑基 Foundation

#### 天灵曲 (Sky Spirit Tune) — id 5000004
- **Lv1**: 双方加3[灵气]  
  *Both players add 3 [Qi]*
- **Lv2**: 双方加5[灵气]  
  *Both players add 5 [Qi]*
- **Lv3**: 双方加7[灵气]  
  *Both players add 7 [Qi]*

#### 幻音曲 (Illusion Tune) — id 5000005
*持续 Continuous*  
- **Lv1**: [持续]：双方在各自回合开始时减3生命，加3[防]  
  *[Continuous]: Both players will lose 3 HP and add 3 [DEF] at the beginning of their turn*
- **Lv2**: [持续]：双方在各自回合开始时减5生命，加5[防]  
  *[Continuous]: Both players will lose 5 HP and add 5 [DEF] at the beginning of their turn*
- **Lv3**: [持续]：双方在各自回合开始时减7生命，加7[防]  
  *[Continuous]: Both players will lose 7 HP and add 7 [DEF] at the beginning of their turn*

#### 慈念曲 (Kindness Tune) — id 5000006
*持续 Continuous*  
- **Lv1**: [持续]：败者所受命元伤害减4(最低减到1） / 此牌效果不可叠加  
  *[Continuous]: Both players reduce damage to [Destiny] by 4 (min 1) / This effect is not stackable*
- **Lv2**: [持续]：败者所受命元伤害减6(最低减到1） / 此牌效果不可叠加  
  *[Continuous]: Both players reduce damage to [Destiny] by 6 (min 1) / This effect is not stackable*
- **Lv3**: [持续]：败者所受命元伤害减8(最低减到1） / 此牌效果不可叠加  
  *[Continuous]: Both players reduce damage to [Destiny] by 8 (min 1) / This effect is not stackable*


### Phase 3 — 金丹 Virtuoso

#### 断肠曲 (Heartbroken Tune) — id 5000007
*持续 Continuous*  
- **Lv1**: [持续]：双方在各自回合开始时加1层[内伤]  
  *[Continuous]: Both players will gain 1 stack(s) of [Internal Injury] at the beginning of their turn*
- **Lv2**: [持续]：双方在各自回合开始时加2层[内伤]  
  *[Continuous]: Both players will gain 2 stack(s) of [Internal Injury] at the beginning of their turn*
- **Lv3**: [持续]：双方在各自回合开始时加3层[内伤]  
  *[Continuous]: Both players will gain 3 stack(s) of [Internal Injury] at the beginning of their turn*

#### 狂舞曲 (Craze Dance Tune) — id 5000008
*持续 Continuous*  
- **Lv1**: [持续]：双方所有牌加2攻  
  *[Continuous]: Both players' cards add 2 ATK*
- **Lv2**: [持续]：双方所有牌加4攻  
  *[Continuous]: Both players' cards add 4 ATK*
- **Lv3**: [持续]：双方所有牌加6攻  
  *[Continuous]: Both players' cards add 6 ATK*

#### 轮指连音 (Tremolo) — id 5000009
- **Lv1**: 2攻×3（若用过琴师牌则多1攻） / [无视防御]  
  *2 ATK × 3 /  (1 more ATK if you've played a Musician Card) / [Ignore DEF]*
- **Lv2**: 3攻×3（若用过琴师牌则多1攻） / [无视防御]  
  *3 ATK × 3 /  (1 more ATK if you've played a Musician Card) / [Ignore DEF]*
- **Lv3**: 4攻×3（若用过琴师牌则多1攻） / [无视防御]  
  *4 ATK × 3 /  (1 more ATK if you've played a Musician Card) / [Ignore DEF]*


### Phase 4 — 元婴 Immortality

#### 回春曲 (Regen Tune) — id 5000010
*持续 Continuous*  
- **Lv1**: [持续]：双方在各自回合结束时加4生命及上限  
  *[Continuous]: Both players will add 4 HP and Max HP at the end of their turn*
- **Lv2**: [持续]：双方在各自回合结束时加6生命及上限  
  *[Continuous]: Both players will add 6 HP and Max HP at the end of their turn*
- **Lv3**: [持续]：双方在各自回合结束时加8生命及上限  
  *[Continuous]: Both players will add 8 HP and Max HP at the end of their turn*

#### 九煞破灵曲 (Nine Evil Ruptsprite) — id 5000011
- **Lv1**: 双方减3[灵气]  
  *Both players lose 3 [Qi]*
- **Lv2**: 双方减5[灵气]  
  *Both players lose 5 [Qi]*
- **Lv3**: 双方减7[灵气]  
  *Both players lose 7 [Qi]*

#### 同心曲 (Concentric Tune) — id 5000012
- **Lv1**: 若自身有[负面状态]，则向对方施加同样的[负面状态]  
  *Apply all [Debuff] on you to the opponent*
- **Lv2**: 若自身有[负面状态]，则向对方施加同样的[负面状态]  
  *Apply all [Debuff] on you to the opponent*
- **Lv3**: 若自身有[负面状态]，则向对方施加同样的[负面状态]  
  *Apply all [Debuff] on you to the opponent*


### Phase 5 — 化神 Incarnation

#### 幽绪乱心曲 (Apparition Confusion) — id 5000013
*持续 Continuous*  
- **Lv1**: [持续]：双方在每次攻击时减4生命  
  *[Continuous]: Both players lose 4 HP when they attack*
- **Lv2**: [持续]：双方在每次攻击时减5生命  
  *[Continuous]: Both players lose 5 HP when they attack*
- **Lv3**: [持续]：双方在每次攻击时减6生命  
  *[Continuous]: Both players lose 6 HP when they attack*

#### 转弦合调 (Chord In Tune) — id 5000014
- **Lv1**: [灵气]+2 / 若使用过琴师牌或后一格为琴师牌则[再次行动]  
  *[Qi]+2 / If you have played a Musician Card this battle or the next card in your deck is a Musician Card, [Chase]*
- **Lv2**: [灵气]+4 / 若使用过琴师牌或后一格为琴师牌则[再次行动]  
  *[Qi]+4 / If you have played a Musician Card this battle or the next card in your deck is a Musician Card, [Chase]*
- **Lv3**: [灵气]+6 / 若使用过琴师牌或后一格为琴师牌则[再次行动]  
  *[Qi]+6 / If you have played a Musician Card this battle or the next card in your deck is a Musician Card, [Chase]*

#### 天音困仙曲 (Predicament for Immortals) — id 5000015
*持续 Continuous*  
- **Lv1**: [持续]：双方无法触发[再次行动]  
  *[Continuous]: Both players cannot trigger [Chase]*
- **Lv2**: [持续]：双方无法触发[再次行动]  
  *[Continuous]: Both players cannot trigger [Chase]*
- **Lv3**: [持续]：双方无法触发[再次行动]  
  *[Continuous]: Both players cannot trigger [Chase]*


## Side job (副职): 画师 Painter


### Phase 1 — 炼气 Meditation

#### 调色 (Toning) — id 6000001
- **Lv1**: 3攻 / [灵气]+1 / [防]+3  
  *3 ATK / [Qi]+1 / [DEF]+3*
- **Lv2**: 3攻 / [灵气]+2 / [防]+3  
  *3 ATK / [Qi]+2 / [DEF]+3*
- **Lv3**: 4攻 / [灵气]+3 / [防]+3  
  *4 ATK / [Qi]+3 / [DEF]+3*

#### 练笔 (Practice Writing) — id 6000002
- **Lv1**: [置换]：换牌机会+2  
  *[Exchange]: Exchange Card Chance + 2*

#### 研墨 (Grinding Ink) — id 6000003
- **Lv1**: 8攻 / [灵气]+<color=#2C81BF>1</color>  
  *8 ATK / [Qi]+1*
- **Lv2**: 11攻 / [灵气]+<color=#2C81BF>1</color>  
  *11 ATK / [Qi]+1*
- **Lv3**: 14攻 / [灵气]+<color=#2C81BF>1</color>  
  *14 ATK / [Qi]+1*


### Phase 2 — 筑基 Foundation

#### 笔走龙蛇 (Pen Walks Dragon Snake) — id 6000004
- **Lv1**: [防]+5～16  
  *[DEF]+5～16*
- **Lv2**: [防]+10～21  
  *[DEF]+10～21*
- **Lv3**: [防]+15～26  
  *[DEF]+15～26*

#### 画饼充饥 (Feed On Illusions) — id 6000005
- **Lv1**: 生命上限+10 / [灵气]+2  
  *Max HP+10 / [Qi]+2*
- **Lv2**: 生命上限+15 / [灵气]+3  
  *Max HP+15 / [Qi]+3*
- **Lv3**: 生命上限+20 / [灵气]+4  
  *Max HP+20 / [Qi]+4*

#### 画蛇添足 (Gild The Lily) — id 6000006
- **Lv1**: 5攻×2 / 对方加8[防]  
  *5 ATK × 2 / Opponent add 8 [DEF]*
- **Lv2**: 7攻×2 / 对方加8[防]  
  *7 ATK × 2 / Opponent add 8 [DEF]*
- **Lv3**: 9攻×2 / 对方加8[防]  
  *9 ATK × 2 / Opponent add 8 [DEF]*


### Phase 3 — 金丹 Virtuoso

#### 挥毫泼墨 (Splash Ink) — id 6000007
- **Lv1**: 施加一种随机[负面状态]2层  
  *Apply 2 stacks of random [Debuff]*
- **Lv2**: 施加一种随机[负面状态]3层  
  *Apply 3 stacks of random [Debuff]*
- **Lv3**: 施加一种随机[负面状态]4层  
  *Apply 4 stacks of random [Debuff]*

#### 灵感迸发 (Inspiration) — id 6000008
- **Lv1**: [灵气]+2 / 下一张牌[灵气]消耗减2  
  *[Qi]+2 / Next card's [Qi] cost reduce 2*
- **Lv2**: [灵气]+3 / 下一张牌[灵气]消耗减3  
  *[Qi]+3 / Next card's [Qi] cost reduce 3*
- **Lv3**: [灵气]+4 / 下一张牌[灵气]消耗减4  
  *[Qi]+4 / Next card's [Qi] cost reduce 4*

#### 以画入道 (Ask Dao By Paint) — id 6000009
- **Lv1**: [置换]：获得1张自身境界的门派牌  
  *[Exchange]: Gain a current Phase Sect Card*


### Phase 4 — 元婴 Immortality

#### 触类旁通 (Reason By Analogy) — id 6000010
- **Lv1**: [置换]：换牌机会+1，获得1张画师以外副职业的牌（筑基期以上）  
  *[Exchange]: Exchange Card Chance+1. Gain a card from Side Job other than the Painter (Above Foundation Phase)*

#### 神来之笔 (Divine Brush) — id 6000011
- **Lv1**: [防]+4 / 随机使用一张门派牌的效果  
  *[DEF]+4 / Trigger the effect of a random Card of your Sect*
- **Lv2**: [防]+6 / 随机使用一张门派牌的效果  
  *[DEF]+6 / Trigger the effect of a random Card of your Sect*
- **Lv3**: [防]+8 / 随机使用一张门派牌的效果  
  *[DEF]+8 / Trigger the effect of a random Card of your Sect*

#### 落纸云烟 (Falling Paper Clouds) — id 6000014
- **Lv1**: 随机1种效果： / 加18[防]，或加14生命，或加1层[护体]  
  *Random Effect:  / Add 18 [DEF], add 14 HP, or add 1 stack(s) of [Guard Up]*
- **Lv2**: 随机1种效果： / 加26[防]，或加20生命，或加2层[护体]  
  *Random Effect:  / Add 26 [DEF], add 20 HP, or add 2 stack(s) of [Guard Up]*
- **Lv3**: 随机1种效果： / 加34[防]，或加26生命，或加3层[护体]  
  *Random Effect:  / Add 34 [DEF], add 26 HP, or add 3 stack(s) of [Guard Up]*


### Phase 5 — 化神 Incarnation

#### 运笔如飞 (Flying Brush) — id 6000012
- **Lv1**: [防]+6 / 使用下张牌后[再次行动]  
  *[DEF]+6 / After playing the next card [Chase]*
- **Lv2**: [防]+12 / 使用下张牌后[再次行动]  
  *[DEF]+12 / After playing the next card [Chase]*
- **Lv3**: [防]+18 / 使用下张牌后[再次行动]  
  *[DEF]+18 / After playing the next card [Chase]*

#### 画龙点睛 (Finishing Touch) — id 6000013
*消耗 Consumable*  
- **Lv1**: [升级]下3次使用的牌（战斗结束还原） / [消耗]  
  *[Upgrade] next 3 cards when playing them (restored after the battle) / [Consumption]*
- **Lv2**: [升级]下4次使用的牌（战斗结束还原） / [消耗]  
  *[Upgrade] next 4 cards when playing them (restored after the battle) / [Consumption]*
- **Lv3**: [升级]下5次使用的牌（战斗结束还原） / [消耗]  
  *[Upgrade] next 5 cards when playing them (restored after the battle) / [Consumption]*

#### 妙笔生花 (Wonderful Strokes) — id 6000015
- **Lv1**: [置换]：获得1张升级后的牌（金丹期以上）  
  *[Exchange]: Gain an upgraded Card (Above Virtuoso Phase)*


## Side job (副职): 阵法师 Formation Master


### Phase 1 — 炼气 Meditation

#### 引雷阵 (Thunderphilia Formation) — id 8000001
*持续 Continuous*  
- **Lv1**: [持续]2[次]：回合结束时向对方造成4伤害  
  *[Continuous]: 2 [Times]: At the end of your turn, deal 4 DMG to the opponent.*
- **Lv2**: [持续]3[次]：回合结束时向对方造成4伤害  
  *[Continuous]: 3 [Times]: At the end of your turn, deal 4 DMG to the opponent.*
- **Lv3**: [持续]4[次]：回合结束时向对方造成4伤害  
  *[Continuous]: 4 [Times]: At the end of your turn, deal 4 DMG to the opponent.*

#### 碎杀阵 (Fraccide Formation) — id 8000002
*持续 Continuous*  
- **Lv1**: [持续]2[次]：攻击时多3攻并附加[碎防]  
  *[Continuous] 2 [Times]: Add 3 more ATK when attack and apply [Smash DEF] effect*
- **Lv2**: [持续]3[次]：攻击时多3攻并附加[碎防]  
  *[Continuous] 3 [Times]: Add 3 more ATK when attack and apply [Smash DEF] effect*
- **Lv3**: [持续]4[次]：攻击时多3攻并附加[碎防]  
  *[Continuous] 4 [Times]: Add 3 more ATK when attack and apply [Smash DEF] effect*

#### 冲击阵纹 (Impact Formation) — id 8000003
- **Lv1**: 6攻 / 若使用过持续牌，追加2攻  
  *6 ATK / If you have played a Continuous card in this battle, make an additional 2 ATK*
- **Lv2**: 8攻 / 若使用过持续牌，追加3攻  
  *8 ATK / If you have played a Continuous card in this battle, make an additional 3 ATK*
- **Lv3**: 10攻 / 若使用过持续牌，追加4攻  
  *10 ATK / If you have played a Continuous card in this battle, make an additional 4 ATK*


### Phase 2 — 筑基 Foundation

#### 龟甲阵 (Scutturtle Formation) — id 8000004
*持续 Continuous*  
- **Lv1**: [持续]4[次]：回合结束时加3[防]  
  *[Continuous] 4 [Times]: At the end of your turn, add 3 [DEF]*
- **Lv2**: [持续]6[次]：回合结束时加3[防]  
  *[Continuous] 6 [Times]: At the end of your turn, add 3 [DEF]*
- **Lv3**: [持续]8[次]：回合结束时加3[防]  
  *[Continuous] 8 [Times]: At the end of your turn, add 3 [DEF]*

#### 邪蛊阵 (Cacopoisonous Formation) — id 8000005
*持续 Continuous*  
- **Lv1**: [持续]2[次]：回合开始时向对方施加1层[内伤]  
  *[Continuous] 2 [Times]: At the beginning of your turn, apply 1 stack of [Internal Injury] to the opponent*
- **Lv2**: [持续]3[次]：回合开始时向对方施加1层[内伤]  
  *[Continuous] 3 [Times]: At the beginning of your turn, apply 1 stack of [Internal Injury] to the opponent*
- **Lv3**: [持续]4[次]：回合开始时向对方施加1层[内伤]  
  *[Continuous] 4 [Times]: At the beginning of your turn, apply 1 stack of [Internal Injury] to the opponent*

#### 疗愈阵纹 (Cure Formation) — id 8000006
- **Lv1**: 生命+7 / 若使用过持续牌，先加6生命上限  
  *HP+7 / If you have played a Continuous card in this battle, add 6 Max HP first*
- **Lv2**: 生命+11 / 若使用过持续牌，先加9生命上限  
  *HP+11 / If you have played a Continuous card in this battle, add 9 Max HP first*
- **Lv3**: 生命+15 / 若使用过持续牌，先加12生命上限  
  *HP+15 / If you have played a Continuous card in this battle, add 12 Max HP first*


### Phase 3 — 金丹 Virtuoso

#### 聚灵阵 (Spiritage Formation) — id 8000007
*持续 Continuous*  
- **Lv1**: [持续]2[次]：回合开始时加2[灵气]  
  *[Continuous] 2 [Times]: At the beginning of your turn, add 2 [Qi]*
- **Lv2**: [持续]3[次]：回合开始时加2[灵气]  
  *[Continuous] 3 [Times]: At the beginning of your turn, add 2 [Qi]*
- **Lv3**: [持续]4[次]：回合开始时加2[灵气]  
  *[Continuous] 4 [Times]: At the beginning of your turn, add 2 [Qi]*

#### 周天剑阵 (Endless Sword Formation) — id 8000008
*持续 Continuous*  
- **Lv1**: [持续]2[次]：使用有攻的牌后额外追加5攻  
  *[Continuous] 2 [Times]: All cards with ATK will make an additional 5 ATK after being played*
- **Lv2**: [持续]3[次]：使用有攻的牌后额外追加5攻  
  *[Continuous] 3 [Times]: All cards with ATK will make an additional 5 ATK after being played*
- **Lv3**: [持续]4[次]：使用有攻的牌后额外追加5攻  
  *[Continuous] 4 [Times]: All cards with ATK will make an additional 5 ATK after being played*

#### 辟邪阵纹 (Hexproof Formation) — id 8000009
- **Lv1**: 获得3层[辟邪] / 若使用过持续牌，加10[防]  
  *Gain 3 stacks of [Hexproof] / If you have played a Continuous card in this battle, gain 10 [DEF]*
- **Lv2**: 获得4层[辟邪] / 若使用过持续牌，加14[防]  
  *Gain 4 stacks of [Hexproof] / If you have played a Continuous card in this battle, gain 14 [DEF]*
- **Lv3**: 获得5层[辟邪] / 若使用过持续牌，加18[防]  
  *Gain 5 stacks of [Hexproof] / If you have played a Continuous card in this battle, gain 18 [DEF]*


### Phase 4 — 元婴 Immortality

#### 八门金锁阵 (Octgates Lock Formation) — id 8000010
*持续 Continuous*  
- **Lv1**: 造成8[伤害] / [持续]2[次]：对方触发再次行动前，对其造成8伤害  
  *Deal 8 [DMG] / [Continuous] 2 [Times]: Deal 8 DMG to the opponent before the opponent's Chase*
- **Lv2**: 造成12[伤害] / [持续]3[次]：对方触发再次行动前，对其造成8伤害  
  *Deal 12 [DMG] / [Continuous] 3 [Times]: Deal 8 DMG to the opponent before the opponent's Chase*
- **Lv3**: 造成16[伤害] / [持续]4[次]：对方触发再次行动前，对其造成8伤害  
  *Deal 16 [DMG] / [Continuous] 4 [Times]: Deal 8 DMG to the opponent before the opponent's Chase*

#### 天罡聚力阵 (Heavenly Spirit Forceage Formation) — id 8000011
*持续 Continuous*  
- **Lv1**: [持续]2[次]：回合开始时获得1层[加攻]  
  *[Continuous] 2 [Times]: At the beginning of your turn, gain 1 stack of [Increase ATK]*
- **Lv2**: [持续]3[次]：回合开始时获得1层[加攻]  
  *[Continuous] 3 [Times]: At the beginning of your turn, gain 1 stack of [Increase ATK]*
- **Lv3**: [持续]4[次]：回合开始时获得1层[加攻]  
  *[Continuous] 4 [Times]: At the beginning of your turn, gain 1 stack of [Increase ATK]*

#### 阵纹重绘 (Reform Formation) — id 8000015
- **Lv1**: [置换]：获得1张持续牌（筑基期以上），换牌机会+1  
  *[Exchange]: Gain a Continuous Card (Above Foundation Phase), Exchange Card Chance+1*

#### 不动金刚阵 (Motionless Tutelary Formation) — id 8000016
*持续 Continuous*  
- **Lv1**: [持续]2[次]：回合结束时加7[防]，若本回合未触发再次行动则再加7生命及上限  
  *[Continuous] 2 [Times]: At the end of your turn, add 7 [DEF]. If you do not Chase this turn, add 7 HP and Max HP additionally*
- **Lv2**: [持续]3[次]：回合结束时加7[防]，若本回合未触发再次行动则再加7生命及上限  
  *[Continuous] 3 [Times]: At the end of your turn, add 7 [DEF]. If you do not Chase this turn, add 7 HP and Max HP additionally*
- **Lv3**: [持续]4[次]：回合结束时加7[防]，若本回合未触发再次行动则再加7生命及上限  
  *[Continuous] 4 [Times]: At the end of your turn, add 7 [DEF]. If you do not Chase this turn, add 7 HP and Max HP additionally*


### Phase 5 — 化神 Incarnation

#### 回响阵纹 (Echo Formation) — id 8000012
- **Lv1**: 若第一格为持续牌，重复其效果  
  *If the first slot is a Continuous Card, then retrigger its effect*
- **Lv2**: 若第一格为持续牌，重复其[升级]1次后的效果  
  *If the first slot is a Continuous Card, then retrigger its effect after [Upgrade] 1 time*
- **Lv3**: 若第一格为持续牌，重复其[升级]2次后的效果  
  *If the first slot is a Continuous Card, then retrigger its effect after [Upgrade] 2 times*

#### 万花迷魂阵 (Anthomania Formation) — id 8000013
*持续 Continuous*  
- **Lv1**: [持续]2[次]：回合结束时向对方施加1层[减攻]，然后对方每有1层[减攻]吸取其1生命  
  *[Continuous] 2 [Times]: At the end of your turn, apply 1 stack of [Decrease ATK] to the opponent, then steal 1 HP for every stack of [Decrease ATK] they have*
- **Lv2**: [持续]3[次]：回合结束时向对方施加1层[减攻]，然后对方每有1层[减攻]吸取其1生命  
  *[Continuous] 3 [Times]: At the end of your turn, apply 1 stack of [Decrease ATK] to the opponent, then steal 1 HP for every stack of [Decrease ATK] they have*
- **Lv3**: [持续]4[次]：回合结束时向对方施加1层[减攻]，然后对方每有1层[减攻]吸取其1生命  
  *[Continuous] 4 [Times]: At the end of your turn, apply 1 stack of [Decrease ATK] to the opponent, then steal 1 HP for every stack of [Decrease ATK] they have*

#### 须弥阵纹 (Meru Formation) — id 8000014
- **Lv1**: [跳过]自身下1张牌 / 若使用过持续牌则[再次行动]  
  *[Skip] your next 1 card / If you have played a Continuous card in this battle, then [Chase]*
- **Lv2**: [跳过]自身下2张牌 / 若使用过持续牌则[再次行动]  
  *[Skip] your next 2 cards / If you have played a Continuous card in this battle, then [Chase]*
- **Lv3**: [跳过]自身下3张牌 / 若使用过持续牌则[再次行动]  
  *[Skip] your next 3 cards / If you have played a Continuous card in this battle, then [Chase]*


## Side job (副职): 灵植师 Plant Master


### Phase 1 — 炼气 Meditation

#### 归元草 (Origin Herb) — id 9000001
- **Lv1**: [成长] / [炼化]：下场战斗开始时，临时加1生命及上限  
  *[Growth] / [Absorb]: At the beginning of the next battle, temporarily add 1 HP and Max HP*
- **Lv2**: [成长] / [炼化]：下场战斗开始时，临时加3生命及上限  
  *[Growth] / [Absorb]: At the beginning of the next battle, temporarily add 3 HP and Max HP*
- **Lv3**: [炼化]：下场战斗开始时，临时加5生命及上限  
  *[Absorb]: At the beginning of the next battle, temporarily add 5 HP and Max HP*

#### 金梭兰 (Shuttle Orchid) — id 9000002
- **Lv1**: [成长] / [炼化]：下场战斗开始时，向对方造成1[伤害]  
  *[Growth] / [Absorb]: At the beginning of the next battle, deal 1 [DMG]*
- **Lv2**: [成长] / [炼化]：下场战斗开始时，向对方造成3[伤害]  
  *[Growth] / [Absorb]: At the beginning of the next battle, deal 3 [DMG]*
- **Lv3**: [炼化]：下场战斗开始时，向对方造成5[伤害]  
  *[Absorb]: At the beginning of the next battle, deal 5 [DMG]*

#### 剑枝竹 (Sword Bamboo) — id 9000003
- **Lv1**: [成长] / 6攻  
  *[Growth] / 6 ATK*
- **Lv2**: [成长] / 4攻×2  
  *[Growth] / 4 ATK × 2*
- **Lv3**: 3攻×3  
  *3 ATK × 3*


### Phase 2 — 筑基 Foundation

#### 神秘种子 (Mystery Seed) — id 9000006
- **Lv1**: [成长] / 留在手牌时，下轮开始前变为随机变异灵植牌  
  *[Growth] / When left in hand, grows to a random variation plant before the start of the next round*
- **Lv2**: [成长] / 留在手牌时，下轮开始前变为随机变异灵植牌  
  *[Growth] / When left in hand, grows to a random variation plant before the start of the next round*
- **Lv3**: 留在手牌时，下轮开始前变为随机变异灵植牌  
  *When left in hand, grows to a random variation plant before the start of the next round*

#### 神力草 (Divine Power Grass) — id 9000008
- **Lv1**: [成长] / [炼化]：下场战斗开始时，获得0层[加攻]  
  *[Growth] / [Absorb]: At the beginning of the next battle, gain 0 stacks of [Increase ATK]*
- **Lv2**: [成长] / [炼化]：下场战斗开始时，获得0～1层[加攻]  
  *[Growth] / [Absorb]: At the beginning of the next battle, gain 0～1 stack of [Increase ATK]*
- **Lv3**: [炼化]：下场战斗开始时，获得1层[加攻]  
  *[Absorb]: At the beginning of the next battle, gain 1 stack of [Increase ATK]*

#### 叶盾花 (Leaf Shield Flower) — id 9000009
*持续 Continuous*  
- **Lv1**: [成长] / [防]+8  
  *[Growth] / [DEF]+8*
- **Lv2**: [成长] / [防]+14  
  *[Growth] / [DEF]+14*
- **Lv3**: [防]+20 / [持续]：自身生命减少时，其中最多一半可被[防]抵消  
  *[DEF]+20 / [Continuous]: When your HP is reduced, up to half of it can be offset by [DEF]*

#### 归岩草 (Rock Herb) — id 9000016
- **Lv1**: [成长] / [炼化]：下场战斗开始时，加4[防]  
  *[Growth] / [Absorb]: At the beginning of the next battle, gain 4 [DEF]*
- **Lv2**: [成长] / [炼化]：下场战斗开始时，加8[防]  
  *[Growth] / [Absorb]: At the beginning of the next battle, gain 8 [DEF]*
- **Lv3**: [炼化]：下场战斗开始时，加16[防]  
  *[Absorb]: At the beginning of the next battle, gain 16 [DEF]*

#### 叶刃花 (Leaf Blade Flower) — id 9000018
*持续 Continuous*  
- **Lv1**: [成长] / 4攻  
  *[Growth] / 4 ATK*
- **Lv2**: [成长] / 4攻×2  
  *[Growth] / 4 ATK × 2*
- **Lv3**: 4攻×3 / [持续]：之后自身全部攻击获得[碎防]效果  
  *4 ATK × 3 / [Continuous]: All your attacks gain [Smash DEF] effect*

#### 火梭兰 (Fire Orchid) — id 9000021
- **Lv1**: [成长] / [炼化]：下场战斗开始时，减对方2生命上限  
  *[Growth] / [Absorb]: At the beginning of the next battle, reduces 2 Max HP of your opponent*
- **Lv2**: [成长] / [炼化]：下场战斗开始时，减对方4生命上限  
  *[Growth] / [Absorb]: At the beginning of the next battle, reduces 4 Max HP of your opponent*
- **Lv3**: [炼化]：下场战斗开始时，减对方8生命上限  
  *[Absorb]: At the beginning of the next battle, reduces 8 Max HP of your opponent*

#### 失力草 (Lose Power Grass) — id 9000022
- **Lv1**: [成长] / [炼化]：下场战斗开始时，向对方施加0层[减攻]  
  *[Growth] / [Absorb]: At the beginning of the next battle, apply 0 stacks of [Decrease ATK]*
- **Lv2**: [成长] / [炼化]：下场战斗开始时，向对方施加0～1层[减攻]  
  *[Growth] / [Absorb]: At the beginning of the next battle, apply 0～1 stack of [Decrease ATK]*
- **Lv3**: [炼化]：下场战斗开始时，向对方施加1层[减攻]  
  *[Growth] / [Absorb]: At the beginning of the next battle, apply 1 stacks of [Decrease ATK]*

#### 硬枝竹 (Hard Bamboo) — id 9000027
*持续 Continuous*  
- **Lv1**: [成长] / [防]+4  
  *[Growth] / [DEF]+4*
- **Lv2**: [成长] / [防]+6  
  *[Growth] / [DEF]+6*
- **Lv3**: [防]+8 / [持续]：自身每回合结束时，每有4[防]就向对方造成1[伤害]  
  *[DEF]+8 / [Continuous]: At the end of each your turn, deal 1 [DMG] to your opponent for every 4 [DEF] you have*


### Phase 3 — 金丹 Virtuoso

#### 愈甘菊 (Healing Chamomile) — id 9000004
- **Lv1**: [成长] / [炼化]：下场战斗开始时，获得0层[恢复]  
  *[Growth] / [Absorb]: At the beginning of the next battle, gain 0 stacks of [Regeneration]*
- **Lv2**: [成长] / [炼化]：下场战斗开始时，获得1层[恢复]  
  *[Growth] / [Absorb]: At the beginning of the next battle, gain 1 stack of [Regeneration]*
- **Lv3**: [炼化]：下场战斗开始时，获得2层[恢复]  
  *[Absorb]: At the beginning of the next battle, gain 2 stacks of [Regeneration]*

#### 向灵葵 (Qi-seeking Sunflower) — id 9000005
- **Lv1**: [成长] / [灵气]+2  
  *[Growth] / [Qi]+2*
- **Lv2**: [成长] / [灵气]+3  
  *[Growth] / [Qi]+3*
- **Lv3**: [灵气]+4（若自身或对方[灵气]>0则多加2灵气）  
  *[Qi]+4 (add 2 more [Qi] if either you or opponent have [Qi])*

#### 灵植浇灌 (Spiritual Plant Watering) — id 9000007
- **Lv1**: [炼化]：手牌中全部成长牌升级1次  
  *[Absorb]: Upgrade all Growth cards in your hand 1 time.*
- **Lv2**: [炼化]：手牌中全部成长牌升级2次，灵植牌有50%概率变异  
  *[Absorb]: Upgrade all Growth cards in your hand 2 times, then plant cards have a 50% chance of variation.*
- **Lv3**: [炼化]：手牌中全部成长牌升级2次，灵植牌有100%概率变异  
  *[Absorb]: Upgrade all Growth cards in your hand 2 times, then plant cards have a 100% chance of variation.*

#### 邪灵葵 (Qi-corrupting Sunflower) — id 9000017
- **Lv1**: [成长] / 对方减1[灵气]  
  *[Growth] / Opponent loses 1 [Qi]*
- **Lv2**: [成长] / 对方减2[灵气]  
  *[Growth] / Opponent loses 2 [Qi]*
- **Lv3**: 对方减3[灵气] / 若对方的灵气不足以扣减，每缺1点造成5伤害  
  *Opponent loses 3 [Qi] / If the opponent does not have enough [Qi], deal 5 damage for every point of [Qi] lacking*

#### 清甘菊 (Clear Chamomile) — id 9000023
- **Lv1**: [成长] / [炼化]：下场战斗开始时，获得1层[辟邪]  
  *[Growth] / [Absorb]: At the beginning of the next battle, gain 1 stack of [Hexproof]*
- **Lv2**: [成长] / [炼化]：下场战斗开始时，获得2层[辟邪]  
  *[Growth] / [Absorb]: At the beginning of the next battle, gain 2 stacks of [Hexproof]*
- **Lv3**: [炼化]：下场战斗开始时，获得3层[辟邪]  
  *[Absorb]: At the beginning of the next battle, gain 3 stacks of [Hexproof]*


### Phase 4 — 元婴 Immortality

#### 飞枭灵芝 (Flying Owl Reishi) — id 9000010
- **Lv1**: [成长] / [炼化]：下场战斗开始时，加0[速度]  
  *[Growth] / [Absorb]: At the beginning of the next battle, gain 0 [Speed]*
- **Lv2**: [成长] / [炼化]：下场战斗开始时，加1[速度]  
  *[Growth] / [Absorb]: At the beginning of the next battle, gain 1 [Speed]*
- **Lv3**: [炼化]：下场战斗开始时，加2[速度]  
  *[Absorb]: At the beginning of the next battle, gain 2 [Speed]*

#### 穿肠紫蕨 (Toxic Purple Fern) — id 9000012
- **Lv1**: [成长] / [炼化]：下场战斗开始时，向对方施加0层[内伤]  
  *[Growth] / [Absorb]: At the beginning of the next battle, apply 0 stacks of [Internal Injury]*
- **Lv2**: [成长] / [炼化]：下场战斗开始时，向对方施加1层[内伤]  
  *[Growth] / [Absorb]: At the beginning of the next battle, apply 1 stack of [Internal Injury]*
- **Lv3**: [炼化]：下场战斗开始时，向对方施加2层[内伤]  
  *[Absorb]: At the beginning of the next battle, apply 2 stacks of [Internal Injury]*

#### 冰封雪莲 (Frozen Snow Lotus) — id 9000013
- **Lv1**: [成长] / 生命+5  
  *[Growth] / HP+5*
- **Lv2**: [成长] / 生命+10  
  *[Growth] / HP+10*
- **Lv3**: 生命+10 / 下3次减少生命后，加回等量的[防]  
  *HP+10 / Next 3 times after losing HP, gain [DEF] equal to the lost HP*

#### 冰封血莲 (Frozen Blood Lotus) — id 9000020
- **Lv1**: [成长] / 自身减10生命 / (至少剩1生命) / 获得1层[护体]  
  *[Growth] / Lose 10 HP / (At least 1 HP left) / Gain 1 stack of [Guard Up]*
- **Lv2**: [成长] / 自身减10生命2次 / (至少剩1生命) / 获得2层[护体]  
  *[Growth] / Lose 10 HP 2 times / (At least 1 HP left) / Gain 2 stack of [Guard Up]*
- **Lv3**: 自身减10生命3次 / (至少剩1生命) / 获得3层[护体]  
  *Lose 10 HP 3 times / (At least 1 HP left) / Gain 3 stacks of [Guard Up]*

#### 影枭灵芝 (Shadow Owl Reishi) — id 9000024
- **Lv1**: [成长] / [炼化]：下场战斗开始时自身减35生命，之后首次使用牌后[再次行动]  
  *[Growth] / [Absorb]: At the beginning of the next battle, you lose 35 HP, then [Chase] after the first time you play a card*
- **Lv2**: [成长] / [炼化]：下场战斗开始时自身减25生命，之后首次使用牌后[再次行动]  
  *[Growth] / [Absorb]: At the beginning of the next battle, you lose 25 HP, then [Chase] after the first time you play a card*
- **Lv3**: [炼化]：下场战斗开始时自身减15生命，之后首次使用牌后[再次行动]  
  *[Absorb]: At the beginning of the next battle, you lose 15 HP, then [Chase] after the first time you play a card*

#### 清肠紫蕨 (Detoxific Purple Fern) — id 9000026
- **Lv1**: [成长] / 随机一项[负面状态]减1层  
  *[Growth] / One random [Debuff] decreases 1 stack*
- **Lv2**: [成长] / 随机一项[负面状态]减2层  
  *[Growth] / One random [Debuff] decreases 2 stacks*
- **Lv3**: 随机一项[负面状态]减3层，然后若自身没有[负面状态]则[再次行动]  
  *One random [Debuff] decreases 3 stacks, then [Chase] if you have no [Debuff]*


### Phase 5 — 化神 Incarnation

#### 缚仙古藤 (Entangling Ancient Vine) — id 9000011
*持续 Continuous*  
- **Lv1**: [成长] / 施加1层[困缚]  
  *[Growth] / Apply 1 stack of [Entangled]*
- **Lv2**: [成长] / 施加2层[困缚]  
  *[Growth] / Apply 2 stacks of [Entangled]*
- **Lv3**: 施加3层[困缚] / [持续]：[困缚]阻止对方再次行动时，再施加2层[外伤]  
  *Apply 3 stacks of [Entangled] / [Continuous]: When [Entangled] stops the opponent Chase, apply 2 stack of [Wound] additionally*

#### 玄韵道果 (Mysterious Dao Fruit) — id 9000014
- **Lv1**: [成长] / [炼化]：生命上限永久+1  
  *[Growth] / [Absorb]: Max HP increased by 1 in this game*
- **Lv2**: [成长] / [炼化]：随机升级1张1级牌  
  *[Growth] / [Absorb]: Upgrade a Lv. 1 card in your hand or deck randomly*
- **Lv3**: [炼化]：触发1次道韵预感  
  *[Absorb]: Trigger the Daoist Rhyme Omen (you can select a card to get)*

#### 空间灵田 (Space Spiritual Field) — id 9000015
- **Lv1**: [灵气]+4（若在卡组后2格，首次使用改为[跳过]此牌） / [被动]：战斗结束时减1修为并获得1张成长牌  
  *[Qi]+4 (If in the last 2 slots of deck, [Skip] the first play)  / [Passive]: At the end of battle you lose 1 Cul. and gain 1 Growth card*
- **Lv2**: [灵气]+6（若在卡组后2格，首次使用改为[跳过]此牌） / [被动]：战斗结束时减1修为并获得1张成长牌  
  *[Qi]+6 (If in the last 2 slots of deck, [Skip] the first play)  / [Passive]: At the end of battle you lose 1 Cul. and gain 1 Growth card*
- **Lv3**: [灵气]+6（若在卡组后2格，首次使用改为[跳过]此牌） / [被动]：战斗结束时减2修为并获得2张成长牌  
  *[Qi]+6 (If in the last 2 slots of deck, [Skip] the first play)  / [Passive]: At the end of battle you lose 2 Cul. and gain 2 Growth card*

#### 噬仙古藤 (Devouring Ancient Vine) — id 9000019
*持续 Continuous*  
- **Lv1**: [成长] / 吸取对方5生命  
  *[Growth] / Steal 5 HP from the opponent*
- **Lv2**: [成长] / 吸取对方10生命  
  *[Growth] / Steal 10 HP from the opponent*
- **Lv3**: 吸取对方10生命 / [持续]：每当对方触发[再次行动]时，吸取其6生命  
  *Steal 10 HP from the opponent / [Continuous]: Whenever the opponent triggers [Chase], steal 6 HP*

#### 魔韵道果 (Demonic Dao Fruit) — id 9000025
- **Lv1**: [成长] / [炼化]：[命元]减15(最低减至1)，抽1张化神期牌  
  *[Growth] / [Absorb]: Lose 15 Destiny (min 1), then draw 1 Incarnation Phase Card*
- **Lv2**: [成长] / [炼化]：[命元]减15(最低减至1)，修为减1，抽2张化神期牌  
  *[Growth] / [Absorb]: Lose 15 Destiny (min 1) and lose 1 Cul., then draw 2 Incarnation Phase Cards*
- **Lv3**: [炼化]：[命元]减15(最低减至1)，修为减2，抽3张化神期牌  
  *[Absorb]: Lose 15 Destiny (min 1) and lose 2 Cul., then draw 3 Incarnation Phase Cards*


## Side job (副职): 命理师 Fortune-teller


### Phase 1 — 炼气 Meditation

#### 卜命 (Foretell Fate) — id 11000001
- **Lv1**: 对方减6生命 / [开局]：对方减2生命  
  *Opponent loses 6 HP / [Opening]: Opponent loses 2 HP*
- **Lv2**: 对方减8生命 / [开局]：对方减3生命  
  *Opponent loses 8 HP / [Opening]: Opponent loses 3 HP*
- **Lv3**: 对方减10生命 / [开局]：对方减4生命  
  *Opponent loses 10 HP / [Opening]: Opponent loses 4 HP*

#### 天谕·守 (Heavenly Decree - Defend) — id 11000003
*消耗 Consumable*  
- **Lv1**: 2攻 / [防]+9 / [消耗] / [转换]  
  *2 ATK / [DEF]+9 / [Consumption] / [Switch]*
- **Lv2**: 3攻 / [防]+12 / [消耗] / [转换]  
  *3 ATK / [DEF]+12 / [Consumption] / [Switch]*
- **Lv3**: 4攻 / [防]+15 / [消耗] / [转换]  
  *4 ATK / [DEF]+15 / [Consumption] / [Switch]*

#### 天谕·攻 (Heavenly Decree - Attack) — id 11000004
*消耗 Consumable*  
- **Lv1**: 6攻 / [防]+3 / [消耗] / [转换]  
  *6 ATK / [DEF]+3 / [Consumption] / [Switch]*
- **Lv2**: 9攻 / [防]+4 / [消耗] / [转换]  
  *9 ATK / [DEF]+4 / [Consumption] / [Switch]*
- **Lv3**: 12攻 / [防]+5 / [消耗] / [转换]  
  *12 ATK / [DEF]+5 / [Consumption] / [Switch]*

#### 察体 (Examine Body) — id 11000022
- **Lv1**: 下次使用有攻牌后追加5攻 / [开局]：下1次攻击附加[碎防]  
  *The next card with ATK will make an additional 5 ATK after being played / [Opening]: Next 1 attack [Smash DEF]*
- **Lv2**: 下次使用有攻牌后追加8攻 / [开局]：下1次攻击附加[碎防]  
  *The next card with ATK will make an additional 8 ATK after being played / [Opening]: Next 1 attack [Smash DEF]*
- **Lv3**: 下次使用有攻牌后追加11攻 / [开局]：下1次攻击附加[碎防]  
  *The next card with ATK will make an additional 11 ATK after being played / [Opening]: Next 1 attack [Smash DEF]*


### Phase 2 — 筑基 Foundation

#### 天运·避凶 (Heavenly Fortune - Shun Misfortune) — id 11000007
*持续 Continuous*  
- **Lv1**: [持续]2[次]：使用非[开局]牌后，加3[防]及2生命 / [转换]  
  *[Continuous] 2 [Times]: After playing a card without an [Opening] effect, add 3 [DEF] and 2 HP / [Switch]*
- **Lv2**: [持续]3[次]：使用非[开局]牌后，加3[防]及2生命 / [转换]  
  *[Continuous] 3 [Times]: After playing a card without an [Opening] effect, add 3 [DEF] and 2 HP / [Switch]*
- **Lv3**: [持续]4[次]：使用非[开局]牌后，加3[防]及2生命 / [转换]  
  *[Continuous] 4 [Times]: After playing a card without an [Opening] effect, add 3 [DEF] and 2 HP / [Switch]*

#### 天运·趋吉 (Heavenly Fortune - Seek Fortune) — id 11000008
*持续 Continuous*  
- **Lv1**: [持续]2[次]：使用[开局]牌后，触发其[开局]效果并造成3伤害 / [转换]  
  *[Continuous] 2 [Times]: After playing a card with an [Opening] effect, trigger its [Opening] effect and deal 3 DMG / [Switch]*
- **Lv2**: [持续]3[次]：使用[开局]牌后，触发其[开局]效果并造成3伤害 / [转换]  
  *[Continuous] 3 [Times]: After playing a card with an [Opening] effect, trigger its [Opening] effect and deal 3 DMG / [Switch]*
- **Lv3**: [持续]4[次]：使用[开局]牌后，触发其[开局]效果并造成3伤害 / [转换]  
  *[Continuous] 4 [Times]: After playing a card with an [Opening] effect, trigger its [Opening] effect and deal 3 DMG / [Switch]*

#### 探灵 (Detect Qi) — id 11000009
- **Lv1**: [灵气]+2 / [开局]：[灵气]+1  
  *[Qi]+2 / [Opening]: [Qi]+1*
- **Lv2**: [灵气]+3 / [开局]：[灵气]+1  
  *[Qi]+3 / [Opening]: [Qi]+1*
- **Lv3**: [灵气]+4 / [开局]：[灵气]+1  
  *[Qi]+4 / [Opening]: [Qi]+1*

#### 凶象 (Bad Omen) — id 11000023
- **Lv1**: 对方下1次损失生命时，施加1层[外伤] / [开局]：双方减3生命  
  *For next 1 time，apply 1 [Wound] when opponent loses HP / [Opening]: Both players lose 3 HP*
- **Lv2**: 对方下2次损失生命时，施加1层[外伤] / [开局]：双方减4生命  
  *For next 2 times，apply 1 [Wound] when opponent loses HP / [Opening]: Both players lose 4 HP*
- **Lv3**: 对方下3次损失生命时，施加1层[外伤] / [开局]：双方减5生命  
  *For next 3 times，apply 1 [Wound] when opponent loses HP / [Opening]: Both players lose 5 HP*


### Phase 3 — 金丹 Virtuoso

#### 吉运初显 (Lucky Start) — id 11000005
- **Lv1**: 生命+7 / [开局]：生命及上限+4  
  *HP+7 / [Opening]: HP and Max HP+4*
- **Lv2**: 生命+10 / [开局]：生命及上限+5  
  *HP+10 / [Opening]: HP and Max HP+5*
- **Lv3**: 生命+13 / [开局]：生命及上限+6  
  *HP+13 / [Opening]: HP and Max HP+6*

#### 天命·飞逝 (Heavenly Time - Fleeting) — id 11000011
*消耗 Consumable*  
- **Lv1**: [防]+6 / [跳过]自身下2张牌 / [消耗] / [转换]  
  *[DEF]+6 / [Skip] your next 2 cards / [Consumption] / [Switch]*
- **Lv2**: [防]+12 / [跳过]自身下2张牌 / [消耗] / [转换]  
  *[DEF]+12 / [Skip] your next 2 cards / [Consumption] / [Switch]*
- **Lv3**: [防]+18 / [跳过]自身下2张牌 / [消耗] / [转换]  
  *[DEF]+18 / [Skip] your next 2 cards / [Consumption] / [Switch]*

#### 天命·重现 (Heavenly Time - Recurring) — id 11000012
*消耗 Consumable*  
- **Lv1**: 生命+4 / [跳至]自身上1张牌 / [消耗] / [转换]  
  *HP+4 / [Skip To] the card in your previous slot / [Consumption] / [Switch]*
- **Lv2**: 生命+8 / [跳至]自身上1张牌 / [消耗] / [转换]  
  *HP+8 / [Skip To] the card in your previous slot / [Consumption] / [Switch]*
- **Lv3**: 生命+12 / [跳至]自身上1张牌 / [消耗] / [转换]  
  *HP+12 / [Skip To] the card in your previous slot / [Consumption] / [Switch]*

#### 血光之灾 (Disaster of Bloodshed) — id 11000024
- **Lv1**: 施加1层[内伤] / [开局]：施加1层[内伤]  
  *Apply 1 [Internal Injury] / [Opening]: Apply 1 [Internal Injury]*
- **Lv2**: 施加2层[内伤] / [开局]：施加1层[内伤]  
  *Apply 2 [Internal Injury] / [Opening]: Apply 1 [Internal Injury]*
- **Lv3**: 施加3层[内伤] / [开局]：施加1层[内伤]  
  *Apply 3 [Internal Injury] / [Opening]: Apply 1 [Internal Injury]*


### Phase 4 — 元婴 Immortality

#### 万事如意 (Everything Goes Your Way) — id 11000013
- **Lv1**: 自身的每次攻击不低于6攻，持续3回合 / [开局]：获得1层[辟邪]  
  *Your ATK is no lower than 6 in every attack for 3 turns / [Opening]: Gain 1 [Hexproof]*
- **Lv2**: 自身的每次攻击不低于6攻，持续4回合 / [开局]：获得2层[辟邪]  
  *Your ATK is no lower than 6 in every attack for 4 turns / [Opening]: Gain 2 [Hexproof]*
- **Lv3**: 自身的每次攻击不低于6攻，持续5回合 / [开局]：获得3层[辟邪]  
  *Your ATK is no lower than 6 in every attack for 5 turns / [Opening]: Gain 3 [Hexproof]*

#### 诸事不宜 (Everything is Unadvisable) — id 11000014
- **Lv1**: [防]+4 / 下2次受到的攻击减6攻（最低减至1） / [开局]：[防]+4  
  *[DEF]+4 / You take 6 less ATK (min 1) in opponent's next 2 attack / [Opening]: [DEF]+4*
- **Lv2**: [防]+5 / 下3次受到的攻击减6攻（最低减至1） / [开局]：[防]+5  
  *[DEF]+5 / You take 6 less ATK (min 1) in opponent's next 3 attack / [Opening]: [DEF]+5*
- **Lv3**: [防]+6 / 下4次受到的攻击减6攻（最低减至1） / [开局]：[防]+6  
  *[DEF]+6 / You take 6 less ATK (min 1) in opponent's next 4 attack / [Opening]: [DEF]+6*

#### 天星·牵引 (Heavenly Star - Pull) — id 11000025
- **Lv1**: [灵气]+2 / 触发卡组中此牌之后的2个[开局]效果各1次 / [转换]  
  *[Qi]+2 / Trigger the 2 [Opening] effects in your deck after this card, once each. / [Switch]*
- **Lv2**: [灵气]+3 / 触发卡组中此牌之后的2个[开局]效果各1次 / [转换]  
  *[Qi]+3 / Trigger the 2 [Opening] effects in your deck after this card, once each. / [Switch]*
- **Lv3**: [灵气]+4 / 触发卡组中此牌之后的2个[开局]效果各1次 / [转换]  
  *[Qi]+4 / Trigger the 2 [Opening] effects in your deck after this card, once each. / [Switch]*

#### 天星·御心 (Heavenly Star - Guard) — id 11000026
- **Lv1**: [防]+4 / 生命+4 / 触发卡组中此牌之前的1个[开局]效果2次 / [转换]  
  *[DEF]+4 / HP+4 / Trigger the 1 [Opening] effect in your deck before this card, twice. / [Switch]*
- **Lv2**: [防]+6 / 生命+6 / 触发卡组中此牌之前的1个[开局]效果2次 / [转换]  
  *[DEF]+6 / HP+6 / Trigger the 1 [Opening] effect in your deck before this card, twice. / [Switch]*
- **Lv3**: [防]+8 / 生命+8 / 触发卡组中此牌之前的1个[开局]效果2次 / [转换]  
  *[DEF]+8 / HP+8 / Trigger the 1 [Opening] effect in your deck before this card, twice. / [Switch]*


### Phase 5 — 化神 Incarnation

#### 厄劫缠身 (Envelop In Disaster) — id 11000018
- **Lv1**: 施加4层[内伤] / [开局]：对方同格牌[降级](战斗结束还原)，无法降级则改为造成6伤害  
  *Apply 4 [Internal Injury] / [Opening]: [Downgrade] oppenent's card in the same slot (Restored at end of battle), or deal 6 DMG if unable*
- **Lv2**: 施加5层[内伤] / [开局]：对方同格牌[降级](战斗结束还原)，无法降级则改为造成9伤害  
  *Apply 5 [Internal Injury] / [Opening]: [Downgrade] oppenent's card in the same slot (Restored at end of battle), or deal 9 DMG if unable*
- **Lv3**: 施加6层[内伤] / [开局]：对方同格牌[降级](战斗结束还原)，无法降级则改为造成12伤害  
  *Apply 6 [Internal Injury] / [Opening]: [Downgrade] oppenent's card in the same slot (Restored at end of battle), or deal 12 DMG if unable*

#### 天机·顺应 (Heavenly Will - Comply) — id 11000019
- **Lv1**: [灵气]+2 / 加[防]、生命或上限时多加40%(向上取整)，持续3回合 / [转换]  
  *[Qi]+2 / Lasts for 3 turns, when you add [DEF], HP or Max HP, add 40% more (Rounded up). / [Switch]*
- **Lv2**: [灵气]+4 / 加[防]、生命或上限时多加40%(向上取整)，持续3回合 / [转换]  
  *[Qi]+4 / Lasts for 3 turns, when you add [DEF], HP or Max HP, add 40% more (Rounded up). / [Switch]*
- **Lv3**: [灵气]+6 / 加[防]、生命或上限时多加40%(向上取整)，持续3回合 / [转换]  
  *[Qi]+6 / Lasts for 3 turns, when you add [DEF], HP or Max HP, add 40% more (Rounded up). / [Switch]*

#### 天机·逆施 (Heavenly Will - Defy) — id 11000020
- **Lv1**: [灵气]+2 / 加[防]或生命时，向对方造成50%伤害(向下取整)，持续3回合 / [转换]  
  *[Qi]+2 / Lasts for 3 turns, when you add [DEF] or HP, deal 50% DMG to opponent (Rounded down) / [Switch]*
- **Lv2**: [灵气]+4 / 加[防]或生命时，向对方造成50%伤害(向下取整)，持续3回合 / [转换]  
  *[Qi]+4 / Lasts for 3 turns, when you add [DEF] or HP, deal 50% DMG to opponent (Rounded down) / [Switch]*
- **Lv3**: [灵气]+6 / 加[防]或生命时，向对方造成50%伤害(向下取整)，持续3回合 / [转换]  
  *[Qi]+6 / Lasts for 3 turns, when you add [DEF] or HP, deal 50% DMG to opponent (Rounded down) / [Switch]*

#### 命运轮回 (Cycle of Fate) — id 11000021
*持续 Continuous*  
- **Lv1**: 生命及上限+8 / [持续]4[次]：即将打出第4或第5格牌时，[跳过]并触发其中的[开局]效果  
  *HP and Max HP+8 / [Continuous] 4 [Times]: Before playing the card in the 4th or 5th slot, [Skip] it and trigger its [Opening] effect*
- **Lv2**: 生命及上限+12 / [持续]6[次]：即将打出第4或第5格牌时，[跳过]并触发其中的[开局]效果  
  *HP and Max HP+12 / [Continuous] 6 [Times]: Before playing the card in the 4th or 5th slot, [Skip] it and trigger its [Opening] effect*
- **Lv3**: 生命及上限+16 / [持续]8[次]：即将打出第4或第5格牌时，[跳过]并触发其中的[开局]效果  
  *HP and Max HP+16 / [Continuous] 8 [Times]: Before playing the card in the 4th or 5th slot, [Skip] it and trigger its [Opening] effect*


## Derivation / event cards of 云灵剑宗 Cloud Spirit Sword Sect (not in normal draw)


### Phase 3 — 金丹 Virtuoso

#### 狂剑·星云 (Unrestrained Sword - Nebula Cloud) — id 151
- **Lv1**: 6攻 / 每用过1次“狂剑”加1[灵气]、1[防]和1[剑意]  
  *6 ATK / For each "Unrestrained Sword" you played in this battle, gain 1 [Qi], 1 [DEF] and 1 [Sword Intent]*
- **Lv2**: 7攻 / 每用过1次“狂剑”加1[灵气]、2[防]和1[剑意]  
  *7 ATK / For each "Unrestrained Sword" you played in this battle, gain 1 [Qi], 2 [DEF] and 1 [Sword Intent]*
- **Lv3**: 8攻 / 每用过1次“狂剑”加1[灵气]、3[防]和1[剑意]  
  *8 ATK / For each "Unrestrained Sword" you played in this battle, gain 1 [Qi], 3 [DEF] and 1 [Sword Intent]*

#### 御灵曲 (Spiritstat Tune) — id 185
*持续 Continuous*  
- **Lv1**: [持续]：每加1[灵气]时加3[防]  
  *[Continuous]: Whenever you gain 1 [Qi], add 3 [DEF]*
- **Lv2**: [持续]：每加1[灵气]时加4[防]  
  *[Continuous]: Whenever you gain 1 [Qi], add 4 [DEF]*
- **Lv3**: [持续]：每加1[灵气]时加5[防]  
  *[Continuous]: Whenever you gain 1 [Qi], add 5 [DEF]*


### Phase 4 — 元婴 Immortality

#### 云剑·晚霞 (Cloud Sword - Sunset Glow) — id 47
- **Lv1**: [剑意]+2 / [连云]：每连续用过1张“云剑”多加2[剑意]  
  *[Sword Intent]+2 / [Cloud Hit]: For each consecutive Cloud Sword played, gain 2 [Sword Intent]*
- **Lv2**: [剑意]+4 / [连云]：每连续用过1张“云剑”多加2[剑意]  
  *[Sword Intent]+4 / [Cloud Hit]: For each consecutive Cloud Sword played, gain 2 [Sword Intent]*
- **Lv3**: [剑意]+6 / [连云]：每连续用过1张“云剑”多加2[剑意]  
  *[Sword Intent]+6 / [Cloud Hit]: For each consecutive Cloud Sword played, gain 2 [Sword Intent]*

#### 青龙剑阵 (Azure Dragon Sword Formation) — id 48
- **Lv1**: [防]+8 / 每有3[防]就加1[剑意]  
  *[DEF]+8 / Add 1 [Sword Intent] for every 3 [DEF] you have*
- **Lv2**: [防]+12 / 每有3[防]就加1[剑意]  
  *[DEF]+12 / Add 1 [Sword Intent] for every 3 [DEF] you have*
- **Lv3**: [防]+16 / 每有3[防]就加1[剑意]  
  *[DEF]+16 / Add 1 [Sword Intent] for every 3 [DEF] you have*

#### 凝意生机诀 (Contemplate Spirits Vitality Rhythm) — id 183
- **Lv1**: [剑意]+3 / 生命上限+18 / 每有1点[剑意]加2生命  
  *[Sword Intent]+3 / Max Hp+18 / Add 2 HP for each [Sword Intent]*
- **Lv2**: [剑意]+4 / 生命上限+24 / 每有1点[剑意]加2生命  
  *[Sword Intent]+4 / Max Hp+24 / Add 2 HP for each [Sword Intent]*
- **Lv3**: [剑意]+5 / 生命上限+30 / 每有1点[剑意]加2生命  
  *[Sword Intent]+5 / Max Hp+30 / Add 2 HP for each [Sword Intent]*

#### 云剑·空明 (Cloud Sword - Clarity) — id 184
- **Lv1**: 4攻×2 / [连云]：施加2层[虚弱]  
  *4 ATK × 2 / [Cloud Hit]: Apply 2 [Weakened]*
- **Lv2**: 4攻×3 / [连云]：施加2层[虚弱]  
  *4 ATK × 3 / [Cloud Hit]: Apply 2 [Weakened]*
- **Lv3**: 4攻×4 / [连云]：施加2层[虚弱]  
  *4 ATK × 4 / [Cloud Hit]: Apply 2 [Weakened]*

#### 云剑·周天 (Cloud Sword - Endless) — id 187
*持续 Continuous*  
- **Lv1**: [持续]：阵法师牌算作“云剑”，每次使用“云剑”后追加2攻  
  *[Continuous]: Formation Master Card can be considered as Cloud Sword,  all Cloud Sword will make an additional 2 ATK after being played*
- **Lv2**: [持续]：阵法师牌算作“云剑”，每次使用“云剑”后追加3攻  
  *[Continuous]: Formation Master Card can be considered as Cloud Sword,  all Cloud Sword will make an additional 3 ATK after being played*
- **Lv3**: [持续]：阵法师牌算作“云剑”，每次使用“云剑”后追加4攻  
  *[Continuous]: Formation Master Card can be considered as Cloud Sword,  all Cloud Sword will make an additional 4 ATK after being played*

#### 剑灵葵 (Sword Spirit Sunflower) — id 188
- **Lv1**: [灵气]+2 / 卡组每有1张“灵剑”再加1[灵气](最多3）  
  *[Qi]+2 / For each Spirit Sword in the deck, add 1 [Qi] (up to 3)*
- **Lv2**: [灵气]+4 / 卡组每有1张“灵剑”再加1[灵气](最多3）  
  *[Qi]+4 / For each Spirit Sword in the deck, add 1 [Qi] (up to 3)*
- **Lv3**: [灵气]+6 / 卡组每有1张“灵剑”再加1[灵气](最多3）  
  *[Qi]+6 / For each Spirit Sword in the deck, add 1 [Qi] (up to 3)*

#### 幻·暗鸦灵剑 (M - Raven Spirit Sword) — id 260
- **Lv1**: 4攻 / 每点[灵气]加2[防]（最多4） / 卡组中灵剑数量≥3时[再次行动]  
  *4 ATK / Add 2 [DEF] for each [Qi] (up to 4) / If the number of Spirit Sword in the deck ≥ 3, [Chase]*
- **Lv2**: 8攻 / 每点[灵气]加2[防]（最多12） / 卡组中灵剑数量≥2时[再次行动]  
  *8 ATK / Add 2 [DEF] for each [Qi] (up to 12) / If the number of Spirit Sword in the deck ≥ 2, [Chase]*
- **Lv3**: 12攻 / 每点[灵气]加2[防]（最多20） / 卡组中灵剑数量≥1时[再次行动]  
  *12 ATK / Add 2 [DEF] for each [Qi] (up to 20) / If the number of Spirit Sword in the deck ≥ 1, [Chase]*

#### 幻·轻剑 (M - Light Sword) — id 261
- **Lv1**: 8攻 / [灵气]+1 / 此牌算作云剑和狂剑（使用下张牌时也附带此效果）  
  *8 ATK / [Qi]+1 / This card counts as both Cloud Sword and Unrestrained Sword (also be applied to the next card played)*
- **Lv2**: 10攻 / [灵气]+2 / 此牌算作云剑和狂剑（使用下张牌时也附带此效果）  
  *10 ATK / [Qi]+2 / This card counts as both Cloud Sword and Unrestrained Sword (also be applied to the next card played)*
- **Lv3**: 12攻 / [灵气]+3 / 此牌算作云剑和狂剑（使用下张牌时也附带此效果）  
  *12 ATK / [Qi]+3 / This card counts as both Cloud Sword and Unrestrained Sword (also be applied to the next card played)*

#### 幻·引气剑 (M - Spiritage Sword) — id 262
- **Lv1**: 使用手牌最右侧加[灵气]的[常规牌]（最高1级），若为元婴期及以下则追加3攻（每点[灵气]多1攻）  
  *Play the rightmost [Regular Card] from hand that adds [Qi] (up to Lv.1), if it is an Immortality Phase card or lower: 3 ATK (1 more ATK for every point of [Qi])*
- **Lv2**: 使用手牌最右侧加[灵气]的[常规牌]（最高2级），若为元婴期及以下则追加5攻（每点[灵气]多1攻）  
  *Play the rightmost [Regular Card] from hand that adds [Qi] (up to Lv.2), if it is an Immortality Phase card or lower: 5 ATK (1 more ATK for every point of [Qi])*
- **Lv3**: 使用手牌最右侧加[灵气]的[常规牌]（最高3级），若为元婴期及以下则追加7攻（每点[灵气]多1攻）  
  *Play the rightmost [Regular Card] from hand that adds [Qi] (up to Lv.3), if it is an Immortality Phase card or lower: 7 ATK (1 more ATK for every point of [Qi])*

#### 幻·飞牙剑 (M - Flying Fang Sword) — id 263
- **Lv1**: 4攻 / [再次行动] / 返还此牌所耗[剑意]并额外加1  
  *4 ATK / [Chase] / Return the [Sword Intent] used by this attack and add additional 1 [Sword Intent]*
- **Lv2**: 4攻 / [再次行动] / 返还此牌所耗[剑意]并额外加2  
  *4 ATK / [Chase] / Return the [Sword Intent] used by this attack and add additional 2 [Sword Intent]*
- **Lv3**: 4攻 / [再次行动] / 返还此牌所耗[剑意]并额外加3  
  *4 ATK / [Chase] / Return the [Sword Intent] used by this attack and add additional 3 [Sword Intent]*

#### 幻·勤拙剑 (M - Diligent Sword) — id 323
- **Lv1**: 6攻 / 下1次使用云剑、狂剑、灵剑、剑阵以外的剑牌后[再次行动] / 修为≥85：改为下2次  
  *6 ATK / The next 1 Sword card (excl. [Cloud] / [Unrestrained] / [Spirit] / [Formation]) gain [Chase] / Cultivation ≥ 85: the next 1 more such card gain [Chase]*
- **Lv2**: 10攻 / 下1次使用云剑、狂剑、灵剑、剑阵以外的剑牌后[再次行动] / 修为≥80：改为下2次  
  *10 ATK / The next 1 Sword card (excl. [Cloud] / [Unrestrained] / [Spirit] / [Formation]) gain [Chase] / Cultivation ≥ 80: the next 1 more such card gain [Chase]*
- **Lv3**: 14攻 / 下1次使用云剑、狂剑、灵剑、剑阵以外的剑牌后[再次行动] / 修为≥75：改为下2次  
  *14 ATK / The next 1 Sword card (excl. [Cloud] / [Unrestrained] / [Spirit] / [Formation]) gain [Chase] / Cultivation ≥ 75: the next 1 more such card gain [Chase]*


### Phase 5 — 化神 Incarnation

#### 百兽灵剑阵 (Beast Spirit Sword Formation) — id 49
*持续 Continuous*  
- **Lv1**: [灵气]+2 / [持续]：每回合首次使用“灵剑”或“剑阵”牌后，每剩1点灵气向对方造成1伤害  
  *[Qi]+2 / [Continuous]: Once per turn, after playing a "Sword Formation" or "Spirit Sword" card, deal 1 [DMG] to the opponent for each [Qi] you have*
- **Lv2**: [灵气]+3 / [持续]：每回合首次使用“灵剑”或“剑阵”牌后，每剩1点灵气向对方造成1伤害  
  *[Qi]+3 / [Continuous]: Once per turn, after playing a "Sword Formation" or "Spirit Sword" card, deal 1 [DMG] to the opponent for each [Qi] you have*
- **Lv3**: [灵气]+4 / [持续]：每回合首次使用“灵剑”或“剑阵”牌后，每剩1点灵气向对方造成1伤害  
  *[Qi]+4 / [Continuous]: Once per turn, after playing a "Sword Formation" or "Spirit Sword" card, deal 1 [DMG] to the opponent for each [Qi] you have*

#### 狂龙吞云 (Dragon Devours Clouds) — id 50
*持续 Continuous*  
- **Lv1**: [持续]：狂剑可算作云剑，云剑可算作狂剑  
  *[Continuous]: Cloud Sword can be considered as Unrestrained Sword, and vice versa*
- **Lv2**: 算作用过1次狂剑 / [持续]：狂剑可算作云剑，云剑可算作狂剑  
  *Count as 1 Unrestrained Sword has been played / [Continuous]: Cloud Sword can be considered as Unrestrained Sword, and vice versa*
- **Lv3**: 算作用过2次狂剑 / [持续]：狂剑可算作云剑，云剑可算作狂剑  
  *Count as 2 Unrestrained Sword has been played / [Continuous]: Cloud Sword can be considered as Unrestrained Sword, and vice versa*

#### 云剑·星空 (Cloud Sword - Starry Sky) — id 141
- **Lv1**: [防]+4 / [再次行动] / [连云]：每有1[灵气]加1[防]  
  *[DEF]+4 / [Chase] / [Cloud Hit]: Add 1 [DEF] for each [Qi]*
- **Lv2**: [防]+10 / [再次行动] / [连云]：每有1[灵气]加1[防]  
  *[DEF]+10 / [Chase] / [Cloud Hit]: Add 1 [DEF] for each [Qi]*
- **Lv3**: [防]+16 / [再次行动] / [连云]：每有1[灵气]加1[防]  
  *[DEF]+16 / [Chase] / [Cloud Hit]: Add 1 [DEF] for each [Qi]*

#### 玄冥剑意诀 (Xuanming Sword Intent Mantra) — id 163
- **Lv1**: [剑意]+6 / 自身每失去过6生命就再加1[剑意]  
  *[Sword Intent]+6 / For every 6 HP lost in this battle, add 1 more [Sword Intent]*
- **Lv2**: [剑意]+8 / 自身每失去过6生命就再加1[剑意]  
  *[Sword Intent]+8 / For every 6 HP lost in this battle, add 1 more [Sword Intent]*
- **Lv3**: [剑意]+10 / 自身每失去过6生命就再加1[剑意]  
  *[Sword Intent]+10 / For every 6 HP lost in this battle, add 1 more [Sword Intent]*

#### 万劫天锋 (Shen Jian Ao Zhou) — id 167
- **Lv1**: 12攻 / 此牌受6倍[剑意]和4倍[加攻]的加成 / [碎防]  
  *12 ATK / This card receives a 6x bonus from [Sword Intent] and 4x bonus from [Increase ATK] / [Smash DEF]*

#### 狂剑·降神 (Unrestrained Sword  - Divine) — id 186
- **Lv1**: [防]+4 / 生命+4 / 随机使用1张“狂剑”  
  *[DEF]+4 / HP+4 / Trigger the effect of a random "Unrestrained Sword"*
- **Lv2**: [防]+6 / 生命+6 / 随机使用1张“狂剑”  
  *[DEF]+6 / HP+6 / Trigger the effect of a random "Unrestrained Sword"*
- **Lv3**: [防]+8 / 生命+8 / 随机使用1张“狂剑”  
  *[DEF]+8 / HP+8 / Trigger the effect of a random "Unrestrained Sword"*

#### 天机·地煞 (Heavenly Will - Earth Evil) — id 189
- **Lv1**: [灵气]+4 / 下1次攻击[碎防]且每[击伤]1点生命加1[防]  
  *[Qi]+4 / Next 1 attack [Smash Def] and will add 1 [DEF] for every [Injured] opponent's HP*
- **Lv2**: [灵气]+4 / 下2次攻击[碎防]且每[击伤]1点生命加1[防]  
  *[Qi]+4 / Next 2 attacks [Smash Def] and will add 1 [DEF] for every [Injured] opponent's HP*
- **Lv3**: [灵气]+4 / 下3次攻击[碎防]且每[击伤]1点生命加1[防]  
  *[Qi]+4 / Next 3 attacks [Smash Def] and will add 1 [DEF] for every [Injured] opponent's HP*

#### 幻·云剑探云 (M - Cloud Sword Touch Sky) — id 264
- **Lv1**: 6攻 / 此牌算作2次云剑 / 下张云剑获得[再次行动]  
  *6 ATK / This card counts as 2 Cloud Sword / The next Cloud Sword gain [Chase]*
- **Lv2**: 8攻 / 此牌算作3次云剑 / 下张云剑获得[再次行动]  
  *8 ATK / This card counts as 3 Cloud Sword / The next Cloud Sword gain [Chase]*
- **Lv3**: 10攻 / 此牌算作4次云剑 / 下张云剑获得[再次行动]  
  *10 ATK / This card counts as 4 Cloud Sword / The next Cloud Sword gain [Chase]*

#### 幻·云剑无锋 (M - Cloud Sword Conceal) — id 288
- **Lv1**: [连云]：6攻（本场战斗每攻击过一次多2攻）  
  *[Cloud Hit]: 6 ATK (Add 2 more ATK for each attack performed in combat)*
- **Lv2**: [连云]：12攻（本场战斗每攻击过一次多2攻）  
  *[Cloud Hit]: 12 ATK (Add 2 more ATK for each attack performed in combat)*
- **Lv3**: [连云]：12攻（本场战斗每攻击过一次多3攻）  
  *[Cloud Hit]: 12 ATK (Add 3 more ATK for each attack performed in combat)*

#### 幻·灵犀剑阵 (M - Consonance Sword Formation) — id 293
- **Lv1**: [防]+2 / 下次附带[剑意]的攻击耗尽[剑意]后增加等量[灵气]  
  *[DEF]+2 / For the next 1 attack with [Sword Intent], after [Sword Intent] is used, add an equal amount of [Qi]*
- **Lv2**: [防]+10 / 下次附带[剑意]的攻击耗尽[剑意]后增加等量[灵气]  
  *[DEF]+10 / For the next 1 attack with [Sword Intent], after [Sword Intent] is used, add an equal amount of [Qi]*
- **Lv3**: [防]+18 / 下次附带[剑意]的攻击耗尽[剑意]后增加等量[灵气]  
  *[DEF]+18 / For the next 1 attack with [Sword Intent], after [Sword Intent] is used, add an equal amount of [Qi]*

#### 幻·云舞诀 (M - Cloud Dance Rhythm) — id 309
- **Lv1**: [灵气]+2 / [防]+4 / [剑意]+2 / 每用过1张牌再加1[剑意]  
  *[Qi]+2 / [DEF]+4 / [Sword Intent]+2 / Gain 1 [Sword Intent] for each card used*
- **Lv2**: [灵气]+3 / [防]+6 / [剑意]+3 / 每用过1张牌再加1[剑意]  
  *[Qi]+3 / [DEF]+6 / [Sword Intent]+3 / Gain 1 [Sword Intent] for each card used*
- **Lv3**: [灵气]+4 / [防]+8 / [剑意]+4 / 每用过1张牌再加1[剑意]  
  *[Qi]+4 / [DEF]+8 / [Sword Intent]+4 / Gain 1 [Sword Intent] for each card used*

#### 幻·狂剑盘龙 (M - Unrestrained Sword Dragon Coiled) — id 312
- **Lv1**: [防]+12 / 每用过一次剑阵下回合就加3[防] / [被动]：卡组中的所有狂剑[常规牌]也算作剑阵  
  *[DEF]+12 / For each Sword Formation used, gain 3 [DEF] in your next turn. / [Passive]: All Unrestrained Sword [Regular Card] are also counted as Sword Formation*
- **Lv2**: [防]+16 / 每用过一次剑阵下回合就加4[防] / [被动]：卡组中的所有狂剑[常规牌]也算作剑阵  
  *[DEF]+16 / For each Sword Formation used, gain 4 [DEF] in your next turn. / [Passive]: All Unrestrained Sword [Regular Card] are also counted as Sword Formation*
- **Lv3**: [防]+20 / 每用过一次剑阵下回合就加5[防] / [被动]：卡组中的所有狂剑[常规牌]也算作剑阵  
  *[DEF]+20 / For each Sword Formation used, gain 5 [DEF] in your next turn. / [Passive]: All Unrestrained Sword [Regular Card] are also counted as Sword Formation*

#### 幻·灵犀剑阵 (M - Consonance Sword Formation) — id 325
- **Lv1**: [防]+6 / 每有4[防]就加1[灵气]  
  *[DEF]+6 / Add 1 [Qi] for every 4 [DEF] you have*
- **Lv2**: [防]+10 / 每有4[防]就加1[灵气]  
  *[DEF]+10 / Add 1 [Qi] for every 4 [DEF] you have*
- **Lv3**: [防]+14 / 每有4[防]就加1[灵气]  
  *[DEF]+14 / Add 1 [Qi] for every 4 [DEF] you have*


### Phase 6 — 特殊 Special

#### 首山定岳剑 (Xuan-Yuan Sword) — id 171
- **Lv1**: [蓄灵]5 / 120攻 / [无视防御] / 无视[护体]  
  *[Gather Qi] 5 / 120 ATK / [Ignore DEF] / Ignore [Guard Up]*


## Derivation / event cards of 七星阁 Heptastar Pavilion (not in normal draw)


### Phase 2 — 筑基 Foundation

#### 星弈·拆 (Astral Move - Extend) — id 142
- **Lv1**: 4攻 / [灵气]+1 / 后3格[成为星位]  
  *4 ATK / [Qi]+1 / The next 3 slots [Become Star Point]*
- **Lv2**: 6攻 / [灵气]+1 / 后4格[成为星位]  
  *6 ATK / [Qi]+1 / The next 4 slots [Become Star Point]*
- **Lv3**: 8攻 / [灵气]+1 / 后5格[成为星位]  
  *8 ATK / [Qi]+1 / The next 5 slots [Become Star Point]*


### Phase 4 — 元婴 Immortality

#### 灵卦术 (Spiritual Divination) — id 51
*持续 Continuous*  
- **Lv1**: [持续]：每加1点灵气时加1[卦象]  
  *[Continuous]: Whenever you gain 1 Qi, add 1 [Hexagram]*
- **Lv2**: [卦象]+1 / [持续]：每加1点灵气时加1[卦象]  
  *[Hexagram]+1 / [Continuous]: Whenever you gain 1 Qi, add 1 [Hexagram]*
- **Lv3**: [卦象]+3 / [持续]：每加1点灵气时加1[卦象]  
  *[Hexagram]+3 / [Continuous]: Whenever you gain 1 Qi, add 1 [Hexagram]*

#### 摘花飞叶 (Throw Petals) — id 52
*持续 Continuous*  
- **Lv1**: [持续]：每次攻击对方或被对方攻击后，向对方施加1层[内伤]  
  *[Continuous]: Apply 1 stack of [Internal Injury] each time you attack or are attacked by the opponent*
- **Lv2**: [灵气]+1 / [持续]：每次攻击对方或被对方攻击后，向对方施加1层[内伤]  
  *[Qi]+1 / [Continuous]: Apply 1 stack of [Internal Injury] each time you attack or are attacked by the opponent*
- **Lv3**: [灵气]+3 / [持续]：每次攻击对方或被对方攻击后，向对方施加1层[内伤]  
  *[Qi]+3 / [Continuous]: Apply 1 stack of [Internal Injury] each time you attack or are attacked by the opponent*

#### 春雷霹雳曲 (Thunderbolt Tune) — id 192
*持续 Continuous*  
- **Lv1**: 生命及上限+10 / [持续]：双方在各自回合结束时有10%概率向对方造成10伤害  
  *HP and Max HP+10 / [Continuous]: Both players has 10% chance to deal 10 [DMG] to their opponent at the end of their turn*
- **Lv2**: 生命及上限+15 / [持续]：双方在各自回合结束时有10%概率向对方造成12伤害  
  *HP and Max HP+15 / [Continuous]: Both players has 10% chance to deal 12 [DMG] to their opponent at the end of their turn*
- **Lv3**: 生命及上限+20 / [持续]：双方在各自回合结束时有10%概率向对方造成14伤害  
  *HP and Max HP+20 / [Continuous]: Both players has 10% chance to deal 14 [DMG] to their opponent at the end of their turn*

#### 浮光掠影 (Fleeting Glimpse) — id 193
- **Lv1**: 施加0~2层随机[负面状态]] / 对方[负面状态]层数≥3则[再次行动]  
  *Apply 0~2 random [Debuff] / [Chase] if the opponent's [Debuff] stack count ≥ 3*
- **Lv2**: 施加1~3层随机[负面状态]] / 对方[负面状态]层数≥3则[再次行动]  
  *Apply 1~3 random [Debuff] / [Chase] if the opponent's [Debuff] stack count ≥ 3*
- **Lv3**: 施加2~4层随机[负面状态]] / 对方[负面状态]层数≥3则[再次行动]  
  *Apply 2~4 random [Debuff] / [Chase] if the opponent's [Debuff] stack count ≥ 3*

#### 两仪金刚阵 (Yin Yang Tutelary Formation) — id 194
*持续 Continuous*  
- **Lv1**: [持续]2[次]：自身回合结束时，若有[灵气]或[卦象]，每点[灵气]/[卦象]加1/2生命和等量[防]  
  *[Continuous] 2 [Times]: At the end of your turn, if you have [Qi] or [Hexagram], add 1/2 HP and [DEF] for each [Qi] / [Hexagram]*
- **Lv2**: [持续]3[次]：自身回合结束时，若有[灵气]或[卦象]，每点[灵气]/[卦象]加1/2生命和等量[防]  
  *[Continuous] 3 [Times]: At the end of your turn, if you have [Qi] or [Hexagram], add 1/2 HP and [DEF] for each [Qi] / [Hexagram]*
- **Lv3**: [持续]4[次]：自身回合结束时，若有[灵气]或[卦象]，每点[灵气]/[卦象]加1/2生命和等量[防]  
  *[Continuous] 4 [Times]: At the end of your turn, if you have [Qi] or [Hexagram], add 1/2 HP and [DEF] for each [Qi] / [Hexagram]*

#### 幻·斩草除根 (M - Cutting Weeds) — id 265
- **Lv1**: 令对方生命上限减至其当前生命减8（耗尽[灵气]/[卦象]，每点多减3/3）  
  *Reduces the opponent's Max HP to their current HP minus 8 (Exhasust [Qi] / [Hexagram], each reduces 3 / 3 more)*
- **Lv2**: 令对方生命上限减至其当前生命减8（耗尽[灵气]/[卦象]，每点多减4/3）  
  *Reduces the opponent's Max HP to their current HP minus 8 (Exhasust [Qi] / [Hexagram], each reduces 4 / 3 more)*
- **Lv3**: 令对方生命上限减至其当前生命减8（耗尽[灵气]/[卦象]，每点多减4/4）  
  *Reduces the opponent's Max HP to their current HP minus 8 (Exhasust [Qi] / [Hexagram], each reduces 4 / 4 more)*

#### 幻·流水无情 (M - Ruthless Water) — id 266
*持续 Continuous*  
- **Lv1**: 施加2层[内伤] / [持续]：对方每获得1层[内伤]以外的[负面状态]就获得1层[内伤]  
  *Apply 2 [Internal Injury] /  [Continuous]: Whenever the opponent gain 1 stack of [Debuff] other than [Internal Injury], they also gain 1 [Internal Injury]*
- **Lv2**: 施加3层[内伤] / [持续]：对方每获得1层[内伤]以外的[负面状态]就获得1层[内伤]  
  *Apply 3 [Internal Injury] /  [Continuous]: Whenever the opponent gain 1 stack of [Debuff] other than [Internal Injury], they also gain 1 [Internal Injury]*
- **Lv3**: 施加5层[内伤] / [持续]：对方每获得1层[内伤]以外的[负面状态]就获得1层[内伤]  
  *Apply 5 [Internal Injury] /  [Continuous]: Whenever the opponent gain 1 stack of [Debuff] other than [Internal Injury], they also gain 1 [Internal Injury]*

#### 幻·星罗棋布 (M - Dotted Around) — id 268
- **Lv1**: [灵气]+2 / [星力]+1 / 之后加[灵气]时加等量[星力]（累计最多加3）  
  *[Qi]+2 / [Star Power]+1 / When you add [Qi], add equal amount of [Star Power] (up to add 3 this way)*
- **Lv2**: [灵气]+2 / [星力]+1 / 之后加[灵气]时加等量[星力]（累计最多加5）  
  *[Qi]+2 / [Star Power]+1 / When you add [Qi], add equal amount of [Star Power] (up to add 5 this way)*
- **Lv3**: [灵气]+2 / [星力]+2 / 之后加[灵气]时加等量[星力]（累计最多加7）  
  *[Qi]+2 / [Star Power]+2 / When you add [Qi], add equal amount of [Star Power] (up to add 7 this way)*

#### 幻·坤卦 (M - Earth Hexagram) — id 307
- **Lv1**: [防]+2 / [卦象]+2 / [升级]下1张使用的牌，每有3点[卦象]就多[升级]1张（战斗结束还原）  
  *[DEF]+2 / [Hexagram]+2 / [Upgrade] the next card used, and for every 3 [Hexagram], [Upgrade] 1 more (restored after the battle)*
- **Lv2**: [防]+4 / [卦象]+3 / [升级]下1张使用的牌，每有3点[卦象]就多[升级]1张（战斗结束还原）  
  *[DEF]+4 / [Hexagram]+3 / [Upgrade] the next card used, and for every 3 [Hexagram], [Upgrade] 1 more (restored after the battle)*
- **Lv3**: [防]+6 / [卦象]+4 / [升级]下1张使用的牌，每有3点[卦象]就多[升级]1张（战斗结束还原）  
  *[DEF]+6 / [Hexagram]+4 / [Upgrade] the next card used, and for every 3 [Hexagram], [Upgrade] 1 more (restored after the battle)*

#### 幻·生机绽放 (M - Vitality Blossom) — id 324
*持续 Continuous*  
- **Lv1**: 生命及上限+10 / [持续]：自身每回合结束时先加8生命（超过上限部分加等量上限），然后减8生命  
  *HP and Max HP+10 / [Continuous]: At the end of your turn, add 8 HP (the excess increases Max HP by the same amount), then lose 8 HP*
- **Lv2**: 生命及上限+15 / [持续]：自身每回合结束时先加12生命（超过上限部分加等量上限），然后减12生命  
  *HP and Max HP+15 / [Continuous]: At the end of your turn, add 12 HP (the excess increases Max HP by the same amount), then lose 12 HP*
- **Lv3**: 生命及上限+20 / [持续]：自身每回合结束时先加16生命（超过上限部分加等量上限），然后减16生命  
  *HP and Max HP+20 / [Continuous]: At the end of your turn, add 16 HP (the excess increases Max HP by the same amount), then lose 16 HP*


### Phase 5 — 化神 Incarnation

#### 星弈·双飞燕 (Astral Move - Twin Swallows) — id 53
- **Lv1**: 4攻 / [再次行动] / [星位]：此牌多4攻 / [后招]：追加1次攻击  
  *4 ATK / [Chase] / [Star Point]: ATK+4 / [Post Action]: Make an additional attack*
- **Lv2**: 5攻 / [再次行动] / [星位]：此牌多6攻 / [后招]：追加1次攻击  
  *5 ATK / [Chase] / [Star Point]: ATK+6 / [Post Action]: Make an additional attack*
- **Lv3**: 6攻 / [再次行动] / [星位]：此牌多8攻 / [后招]：追加1次攻击  
  *6 ATK / [Chase] / [Star Point]: ATK+8 / [Post Action]: Make an additional attack*

#### 滴水穿石 (Water Drop Erosion) — id 54
- **Lv1**: 1攻 / 对方有[负面状态]则[再次行动] / [后招]：施加6层[内伤]  
  *1 ATK / If opponent has [Debuff], [Chase] / [Post Action]: Apply 6 stacks of [Internal Injury]*
- **Lv2**: 1攻 / 对方有[负面状态]则[再次行动] / [后招]：施加8层[内伤]  
  *1 ATK / If opponent has [Debuff], [Chase] / [Post Action]: Apply 8 stacks of [Internal Injury]*
- **Lv3**: 1攻 / 对方有[负面状态]则[再次行动] / [后招]：施加10层[内伤]  
  *1 ATK / If opponent has [Debuff], [Chase] / [Post Action]: Apply 10 stacks of [Internal Injury]*

#### 气吞星河 (Great Galaxy) — id 152
- **Lv1**: 耗尽[灵气]和[星力]，每点[灵气]/[星力]加2/4生命及上限 / 若已加过生命则[再次行动] / [后招]：[灵气]+2  
  *Exhaust [Qi] and [Star Power], for each [Qi] / [Star Power] exhausted, add 2 / 4 HP and Max HP / If you have already added HP, [Chase] / [Post Action]: [Qi]+2*
- **Lv2**: 耗尽[灵气]和[星力]，每点[灵气]/[星力]加2/4生命及上限 / 若已加过生命则[再次行动] / [后招]：[灵气]+4  
  *Exhaust [Qi] and [Star Power], for each [Qi] / [Star Power] exhausted, add 2 / 4 HP and Max HP / If you have already added HP, [Chase] / [Post Action]: [Qi]+4*
- **Lv3**: 耗尽[灵气]和[星力]，每点[灵气]/[星力]加2/4生命及上限 / 若已加过生命则[再次行动] / [后招]：[灵气]+6  
  *Exhaust [Qi] and [Star Power], for each [Qi] / [Star Power] exhausted, add 2 / 4 HP and Max HP / If you have already added HP, [Chase] / [Post Action]: [Qi]+6*

#### 玄冥雷云劫 (Xuanming Thundercloud Tribulation) — id 164
- **Lv1**: 重复5次： / 自身受到7[伤害]（每次有10%概率避免），对方受到9[伤害]  
  *Repeat 5 times: / You take 7 [DMG] (with a 10% chance to avoid each time), and the opponent takes 9 [DMG]*
- **Lv2**: 重复5次： / 自身受到7[伤害]（每次有10%概率避免），对方受到10[伤害]  
  *Repeat 5 times: / You take 7 [DMG] (with a 10% chance to avoid each time), and the opponent takes 10 [DMG]*
- **Lv3**: 重复5次： / 自身受到7[伤害]（每次有10%概率避免），对方受到11[伤害]  
  *Repeat 5 times: / You take 7 [DMG] (with a 10% chance to avoid each time), and the opponent takes 11 [DMG]*

#### 灵雀在后 (Spiritual Hunter) — id 190
*持续 Continuous*  
- **Lv1**: [灵气]+1 / [持续]：含“后招”的牌的[灵气]消耗减2，且使用后追加1攻  
  *[Qi]+1 / [Continuous]: "Post Action" card's [Qi] cost decrease 2, and will make an additional 1 ATK after being played*
- **Lv2**: [灵气]+1 / [持续]：含“后招”的牌的[灵气]消耗减2，且使用后追加4攻  
  *[Qi]+1 / [Continuous]: "Post Action" card's [Qi] cost decrease 2, and will make an additional 4 ATK after being played*
- **Lv3**: [灵气]+1 / [持续]：含“后招”的牌的[灵气]消耗减2，且使用后追加7攻  
  *[Qi]+1 / [Continuous]: "Post Action" card's [Qi] cost decrease 2, and will make an additional 7 ATK after being played*

#### 卦衍万邪 (Hexagrams Generating Evils) — id 191
- **Lv1**: 施加1层[内伤] / 生命+2 / 耗尽[卦象]，每点再施加1层[内伤]和[虚弱]  
  *Apply 1 [Internal Injury] / HP+2 / Exhaust [Hexagram], then Apply 1 [Internal Injury] and [Weakened] for each [Hexagram] exhausted*
- **Lv2**: 施加2层[内伤] / 生命+4 / 耗尽[卦象]，每点再施加1层[内伤]和[虚弱]  
  *Apply 2 [Internal Injury] / HP+4 / Exhaust [Hexagram], then Apply 1 [Internal Injury] and [Weakened] for each [Hexagram] exhausted*
- **Lv3**: 施加3层[内伤] / 生命+6 / 耗尽[卦象]，每点再施加1层[内伤]和[虚弱]  
  *Apply 3 [Internal Injury] / HP+6 / Exhaust [Hexagram], then Apply 1 [Internal Injury] and [Weakened] for each [Hexagram] exhausted*

#### 缚仙棘 (Entangling Thornbush) — id 195
- **Lv1**: 施加1层[困缚]（仅首次使用生效） / 施加1层[外伤] / [后招]：2攻×2  
  *Apply 1 [Entangled] (only effective on first play) / Apply 1 [Wound] / [Post Action]: 2 ATK × 2*
- **Lv2**: 施加1层[困缚]（仅首次使用生效） / 施加1层[外伤] / [后招]：5攻×2  
  *Apply 1 [Entangled] (only effective on first play) / Apply 1 [Wound] / [Post Action]: 5 ATK × 2*
- **Lv3**: 施加1层[困缚]（仅首次使用生效） / 施加1层[外伤] / [后招]：8攻×2  
  *Apply 1 [Entangled] (only effective on first play) / Apply 1 [Wound] / [Post Action]: 8 ATK × 2*

#### 星弈·跳 (Astral Move - Jump) — id 196
- **Lv1**: 2攻×2 / [再次行动] / [星位]：若后2格中有星弈牌，[跳至]下一张星弈牌并触发跳过的[开局]效果  
  *2 ATK × 2 / [Chase] / [Star Point]: [Skip to] the next Astral Move card if an Astral Move card is in the next 2 slots, and trigger the skipped [Opening] effect*
- **Lv2**: 2攻×2 / [再次行动] / [星位]：若后3格中有星弈牌，[跳至]下一张星弈牌并触发跳过的[开局]效果  
  *2 ATK × 2 / [Chase] / [Star Point]: [Skip to] the next Astral Move card if an Astral Move card is in the next 3 slots, and trigger the skipped [Opening] effect*
- **Lv3**: 2攻×2 / [再次行动] / [星位]：若后4格中有星弈牌，[跳至]下一张星弈牌并触发跳过的[开局]效果  
  *2 ATK × 2 / [Chase] / [Star Point]: [Skip to] the next Astral Move card if an Astral Move card is in the next 4 slots, and trigger the skipped [Opening] effect*

#### 幻·斗转星移 (M - Shifting Stars) — id 269
*持续 Continuous*  
- **Lv1**: 后一格[成为星位] / [持续]：每次使用“星弈”牌后，使后一格[成为星位]，并追加2攻  
  *The next slot [Become Star Point] / [Continuous]: After each "Astral Move" card is played, the next slot [Become Star Point] and make an addtional 2 ATK*
- **Lv2**: 后一格[成为星位] / [持续]：每次使用“星弈”牌后，使后一格[成为星位]，并追加4攻  
  *The next slot [Become Star Point] / [Continuous]: After each "Astral Move" card is played, the next slot [Become Star Point] and make an addtional 4 ATK*
- **Lv3**: 后一格[成为星位] / [持续]：每次使用“星弈”牌后，使后一格[成为星位]，并追加6攻  
  *The next slot [Become Star Point] / [Continuous]: After each "Astral Move" card is played, the next slot [Become Star Point] and make an addtional 6 ATK*

#### 幻·落花有意 (M - Flower Sentient) — id 289
- **Lv1**: [灵气]+3 / 施加1层[内伤] / 对方每次获得[内伤]时多加2层，持续3回合  
  *[Qi]+3 / Apply 1 [Internal Injury] / Each time your opponent gains [Internal Injury], 2 more are added, lasts for 3 turns*
- **Lv2**: [灵气]+3 / 施加2层[内伤] / 对方每次获得[内伤]时多加2层，持续4回合  
  *[Qi]+3 / Apply 2 [Internal Injury] / Each time your opponent gains [Internal Injury], 2 more are added, lasts for 4 turns*
- **Lv3**: [灵气]+3 / 施加3层[内伤] / 对方每次获得[内伤]时多加2层，持续5回合  
  *[Qi]+3 / Apply 3 [Internal Injury] / Each time your opponent gains [Internal Injury], 2 more are added, lasts for 5 turns*

#### 幻·飞星刺 (M - Astral Fleche) — id 294
- **Lv1**: 5攻 / [星力]+1 / 若不在[星位]则[再次行动]  
  *5 ATK / [Star Power]+1 / If this card not on [Star Point], [Chase]*
- **Lv2**: 9攻 / [星力]+1 / 若不在[星位]则[再次行动]  
  *9 ATK / [Star Power]+1 / If this card not on [Star Point], [Chase]*
- **Lv3**: 9攻 / [星力]+2 / 若不在[星位]则[再次行动]  
  *9 ATK / [Star Power]+2 / If this card not on [Star Point], [Chase]*

#### 幻·藕断丝连 (M - Incessant) — id 298
- **Lv1**: 6攻 / 获得2层[恢复] / 生命上限+9（每层[恢复]多加1） / [后招]：改为加生命及上限  
  *6 ATK / Gain 2 [Regeneration] /  Max HP+9 (add 1 more for each [Regeneration]) /  [Post Action]: add Max HP and HP instead*
- **Lv2**: 6攻 / 获得3层[恢复] / 生命上限+12（每层[恢复]多加1） / [后招]：改为加生命及上限  
  *6 ATK / Gain 3 [Regeneration] /  Max HP+12 (add 1 more for each [Regeneration]) /  [Post Action]: add Max HP and HP instead*
- **Lv3**: 6攻 / 获得4层[恢复] / 生命上限+15（每层[恢复]多加1） / [后招]：改为加生命及上限  
  *6 ATK / Gain 4 [Regeneration] /  Max HP+15 (add 1 more for each [Regeneration]) /  [Post Action]: add Max HP and HP instead*

#### 幻·两仪阵 (M - Yin Yang Formation) — id 320
- **Lv1**: 每点[灵气]或[卦象]加1[防]和生命 / 交换自身的[灵气]和[卦象]  
  *Gain 1 [DEF] and HP for each point of [Qi] or [Hexagram] / Swap your [Qi] and [Hexagram]*
- **Lv2**: [灵气]+1 / 每点[灵气]或[卦象]加1[防]和生命 / 交换自身的[灵气]和[卦象]  
  *[Qi]+1 / Gain 1 [DEF]  and HP for each point of [Qi] or [Hexagram] / Swap your [Qi] and [Hexagram]*
- **Lv3**: [灵气]+2 / 每点[灵气]或[卦象]加1[防]和生命 / 交换自身的[灵气]和[卦象]  
  *[Qi]+2 / Gain 1 [DEF]  and HP for each point of [Qi] or [Hexagram] / Swap your [Qi] and [Hexagram]*


### Phase 6 — 特殊 Special

#### 九天流光轮 (Heavenly Maiden White Jade Ring) — id 172
- **Lv1**: [蓄灵]6 / 自身下1次生命≤0时，复活并回复到64生命 / （次数可叠加）  
  *[Gather Qi] 6 / For the next 1 time when your HP ≤ 0, you will be resurrected and restored to 64 HP / (The number of times can be stacked)*


## Derivation / event cards of 五行道盟 Five Elements Alliance (not in normal draw)


### Phase 2 — 筑基 Foundation

#### 浑星刺 (Cosmos Fleche) — id 153
- **Lv1**: 7攻 / 立刻[激活]后2格牌的所属[五行]，若其中只含1种[五行]则加1[灵气]  
  *7 ATK / Immediately [Activate] the [Five Elements] of the next 2 slots, if which contain only one type of [Five Elements], add 1 [Qi]*
- **Lv2**: 11攻 / 立刻[激活]后2格牌的所属[五行]，若其中只含1种[五行]则加1[灵气]  
  *11 ATK / Immediately [Activate] the [Five Elements] of the next 2 slots, if which contain only one type of [Five Elements], add 1 [Qi]*
- **Lv3**: 15攻 / 立刻[激活]后2格牌的所属[五行]，若其中只含1种[五行]则加1[灵气]  
  *15 ATK / Immediately [Activate] the [Five Elements] of the next 2 slots, if which contain only one type of [Five Elements], add 1 [Qi]*


### Phase 3 — 金丹 Virtuoso

#### 火灵·耀炎 (Fire Spirit - Blazing Flame) — id 198
- **Lv1**: 获得2层[加攻] / [火灵]：双方所有[负面状态]减2层  
  *Gain 2 [Increase ATK] / [Fire Spirit]: All [Debuff] reduces 2 stacks for both players*
- **Lv2**: 获得3层[加攻] / [火灵]：双方所有[负面状态]减3层  
  *Gain 3 [Increase ATK] / [Fire Spirit]: All [Debuff] reduces 3 stacks for both players*
- **Lv3**: 获得4层[加攻] / [火灵]：双方所有[负面状态]减4层  
  *Gain 4 [Increase ATK] / [Fire Spirit]: All [Debuff] reduces 4 stacks for both players*


### Phase 4 — 元婴 Immortality

#### 野渡之印 (Wild Crossing Seal) — id 55
- **Lv1**: [灵气]+2 / 下1次加生命或灵气后[再次行动] / [开局]：[激活水灵]、[激活木灵]  
  *[Qi]+2 / Next time you gain HP or Qi, [Chase]. / [Opening]: [Activate Water Spirit], [Activate Wood Spirit]*
- **Lv2**: [灵气]+4 / 下1次加生命或灵气后[再次行动] / [开局]：[激活水灵]、[激活木灵]  
  *[Qi]+4 / Next time you gain HP or Qi, [Chase]. / [Opening]: [Activate Water Spirit], [Activate Wood Spirit]*
- **Lv3**: [灵气]+6 / 下1次加生命或灵气后[再次行动] / [开局]：[激活水灵]、[激活木灵]  
  *[Qi]+6 / Next time you gain HP or Qi, [Chase]. / [Opening]: [Activate Water Spirit], [Activate Wood Spirit]*

#### 熔岩之印 (Lava Seal) — id 56
- **Lv1**: 减对方10生命及上限（自身每有1防就多减1点） / [开局]：[激活火灵]、[激活土灵]  
  *Opponent loses 10 HP and Max HP (1 more for each 1 DEF you have) / [Opening]: [Activate Fire Spirit], [Activate Earth Spirit]*
- **Lv2**: 减对方15生命及上限（自身每有1防就多减1点） / [开局]：[激活火灵]、[激活土灵]  
  *Opponent loses 15 HP and Max HP (1 more for each 1 DEF you have) / [Opening]: [Activate Fire Spirit], [Activate Earth Spirit]*
- **Lv3**: 减对方20生命及上限（自身每有1防就多减1点） / [开局]：[激活火灵]、[激活土灵]  
  *Opponent loses 20 HP and Max HP (1 more for each 1 DEF you have) / [Opening]: [Activate Fire Spirit], [Activate Earth Spirit]*

#### 金灵·流星 (Metal Spirit - Meteor) — id 143
- **Lv1**: 4攻（自身每减少过8[防]就多1攻） / [金灵]：[再次行动]  
  *4 ATK (1 more ATK for every 8 [DEF] you have been lost) / [Metal Spirit]: [Chase]*
- **Lv2**: 6攻（自身每减少过7[防]就多1攻） / [金灵]：[再次行动]  
  *6 ATK (1 more ATK for every 7 [DEF] you have been lost) / [Metal Spirit]: [Chase]*
- **Lv3**: 8攻（自身每减少过6[防]就多1攻） / [金灵]：[再次行动]  
  *8 ATK (1 more ATK for every 6 [DEF] you have been lost) / [Metal Spirit]: [Chase]*

#### 木灵天罡阵 (Wood Spirit Forceage Formation) — id 201
*持续 Continuous*  
- **Lv1**: 获得1层[加攻] / [持续]：每次使用“木灵”牌时，每有1层[加攻]加1生命  
  *Gain 1 [Increase ATK] / [Continuous]: Whenever you play a "Wood Spirit" card, add 1 HP for every stack of [Increase ATK]*
- **Lv2**: 获得2层[加攻] / [持续]：每次使用“木灵”牌时，每有1层[加攻]加1生命  
  *Gain 2 [Increase ATK] / [Continuous]: Whenever you play a "Wood Spirit" card, add 1 HP for every stack of [Increase ATK]*
- **Lv3**: 获得3层[加攻] / [持续]：每次使用“木灵”牌时，每有1层[加攻]加1生命  
  *Gain 3 [Increase ATK] / [Continuous]: Whenever you play a "Wood Spirit" card, add 1 HP for every stack of [Increase ATK]*

#### 水灵·川流 (Water Spirit - Continuous Flow) — id 203
- **Lv1**: 获得2层[水势] / [开局]：获得1点[灵气]和1层[水势]  
  *Gain 2 [Force of Water] / [Opening]: Gain 1 [Qi] and 1 [Force of Water]*
- **Lv2**: 获得3层[水势] / [开局]：获得1点[灵气]和1层[水势]  
  *Gain 3 [Force of Water] / [Opening]: Gain 1 [Qi] and 1 [Force of Water]*
- **Lv3**: 获得4层[水势] / [开局]：获得1点[灵气]和1层[水势]  
  *Gain 4 [Force of Water] / [Opening]: Gain 1 [Qi] and 1 [Force of Water]*

#### 幻·火灵聚炎 (M - Fire Spirit Flame Eater) — id 270
- **Lv1**: [灵气]+3 / 对方减4生命及上限 / [火灵]：耗4[灵气]令下1张火灵或土灵牌连续生效两次  
  *[Qi]+3 / Opponent loses 4 HP and Max HP / [Fire Spirit]: Cost 4 [Qi] to make the next Fire Spirit or Earth Spirit card trigger twice*
- **Lv2**: [灵气]+4 / 对方减6生命及上限 / [火灵]：耗4[灵气]令下1张火灵或土灵牌连续生效两次  
  *[Qi]+4 / Opponent loses 6 HP and Max HP / [Fire Spirit]: Cost 4 [Qi] to make the next Fire Spirit or Earth Spirit card trigger twice*
- **Lv3**: [灵气]+5 / 对方减8生命及上限 / [火灵]：耗4[灵气]令下1张火灵或土灵牌连续生效两次  
  *[Qi]+5 / Opponent loses 8 HP and Max HP / [Fire Spirit]: Cost 4 [Qi] to make the next Fire Spirit or Earth Spirit card trigger twice*

#### 幻·木灵复苏 (M - Wood Spirit Recovery) — id 272
- **Lv1**: [灵气]+2 / 回复至自身上回合开始时的生命（最多加20） / [木灵]：若已加过生命则获得1层[加攻]  
  *[Qi]+2 / Restore your HP to what it was at the start of your last turn(up to +20) / [Wood Spirit]: If you have already added HP, gain 1 [Increase ATK]*
- **Lv2**: [灵气]+2 / 回复至自身上回合开始时的生命（最多加30） / [木灵]：若已加过生命则获得2层[加攻]  
  *[Qi]+2 / Restore your HP to what it was at the start of your last turn(up to +30) / [Wood Spirit]: If you have already added HP, gain 2 [Increase ATK]*
- **Lv3**: [灵气]+2 / 回复至自身上回合开始时的生命（最多加40） / [木灵]：若已加过生命则获得3层[加攻]  
  *[Qi]+2 / Restore your HP to what it was at the start of your last turn(up to +40) / [Wood Spirit]: If you have already added HP, gain 3 [Increase ATK]*

#### 幻·金灵针 (M - Metal Spirit Needle) — id 273
- **Lv1**: 6攻（[无视防御]） / [锋锐]+4 / [金灵]：下次触发[锋锐]后，返还触发的[锋锐]  
  *6 ATK ([Ignore DEF])  / [Penetrate]+4 / [Metal Spirit]: the next time you trigger [Penetrate], return the triggered [Penetrate]*
- **Lv2**: 6攻（[无视防御]） / [锋锐]+7 / [金灵]：下次触发[锋锐]后，返还触发的[锋锐]  
  *6 ATK ([Ignore DEF])  / [Penetrate]+7 / [Metal Spirit]: the next time you trigger [Penetrate], return the triggered [Penetrate]*
- **Lv3**: 6攻（[无视防御]） / [锋锐]+10 / [金灵]：下次触发[锋锐]后，返还触发的[锋锐]  
  *6 ATK ([Ignore DEF])  / [Penetrate]+10 / [Metal Spirit]: the next time you trigger [Penetrate], return the triggered [Penetrate]*

#### 幻·火灵印 (M - Fire Spirit Seal) — id 315
- **Lv1**: [灵气]+2 / 对方减3生命及上限，之后的加[锋锐]效果改为每点减对方2生命及上限，持续3回合 / [开局]：[激活火灵]、[激活金灵]  
  *[Qi]+2 / Opp loses 3 HP&Max HP / When you gain [Penetrate], lose all gained and opp loses 2 HP&Max HP per stack (3 turns) / [Opening]: [Activate Fire and Metal Spirit]*
- **Lv2**: [灵气]+2 / 对方减6生命及上限，之后的加[锋锐]效果改为每点减对方2生命及上限，持续4回合 / [开局]：[激活火灵]、[激活金灵]  
  *[Qi]+2 / Opp loses 6 HP&Max HP / When you gain [Penetrate], lose all gained and opp loses 2 HP&Max HP per stack (4 turns) / [Opening]: [Activate Fire and Metal Spirit]*
- **Lv3**: [灵气]+2 / 对方减9生命及上限，之后的加[锋锐]效果改为每点减对方2生命及上限，持续5回合 / [开局]：[激活火灵]、[激活金灵]  
  *[Qi]+2 / Opp loses 9 HP&Max HP / When you gain [Penetrate], lose all gained and opp loses 2 HP&Max HP per stack (5 turns) / [Opening]: [Activate Fire and Metal Spirit]*

#### 幻·土灵阵 (M - Earth Spirit Formation) — id 317
*持续 Continuous*  
- **Lv1**: 获得1层[水势] / [激活土灵]、[激活水灵] / [持续]：自身回合结束时，每有1层[水势]加1[防]（最多4）  
  *Gain 1 [Force of Water] / [Activate Earth Spirit], [Activate Water Spirit] / [Continuous]: At the end of your turn, gain 1 [DEF] for each [Force of Water] (up to 4)*
- **Lv2**: 获得1层[水势] / [激活土灵]、[激活水灵] / [持续]：自身回合结束时，每有1层[水势]加1[防]（最多10）  
  *Gain 1 [Force of Water] / [Activate Earth Spirit], [Activate Water Spirit] / [Continuous]: At the end of your turn, gain 1 [DEF] for each [Force of Water] (up to 10)*
- **Lv3**: 获得1层[水势] / [激活土灵]、[激活水灵] / [持续]：自身回合结束时，每有1层[水势]加1[防]（最多16）  
  *Gain 1 [Force of Water] / [Activate Earth Spirit], [Activate Water Spirit] / [Continuous]: At the end of your turn, gain 1 [DEF] for each [Force of Water] (up to 16)*


### Phase 5 — 化神 Incarnation

#### 滚石之印 (Boulder Seal) — id 57
- **Lv1**: [防]+2（每用过1张牌多2） / [再次行动] / [开局]：[激活土灵]、[激活金灵]  
  *[DEF]+2 (2 more for each card you've played) / [Chase] / [Opening]: [Activate Earth Spirit], [Activate Metal Spirit]*
- **Lv2**: [防]+3（每用过1张牌多3） / [再次行动] / [开局]：[激活土灵]、[激活金灵]  
  *[DEF]+3 (3 more for each card you've played) / [Chase] / [Opening]: [Activate Earth Spirit], [Activate Metal Spirit]*
- **Lv3**: [防]+4（每用过1张牌多4） / [再次行动] / [开局]：[激活土灵]、[激活金灵]  
  *[DEF]+4 (4 more for each card you've played) / [Chase] / [Opening]: [Activate Earth Spirit], [Activate Metal Spirit]*

#### 斩浪之印 (Wave Cutter Seal) — id 58
- **Lv1**: [灵气]+2 / 每有1点[灵气]加3[锋锐] / [开局]：[激活金灵]、[激活水灵]  
  *[Qi]+2 / Add 3 [Penetrate] for each [Qi] you have / [Opening]: [Activate Metal Spirit], [Activate Water Spirit]*
- **Lv2**: [灵气]+3 / 每有1点[灵气]加3[锋锐] / [开局]：[激活金灵]、[激活水灵]  
  *[Qi]+3 / Add 3 [Penetrate] for each [Qi] you have / [Opening]: [Activate Metal Spirit], [Activate Water Spirit]*
- **Lv3**: [灵气]+4 / 每有1点[灵气]加3[锋锐] / [开局]：[激活金灵]、[激活水灵]  
  *[Qi]+4 / Add 3 [Penetrate] for each [Qi] you have / [Opening]: [Activate Metal Spirit], [Activate Water Spirit]*

#### 玄冥天髓灭 (Xuanming Heavenly Essence Destruction) — id 165
- **Lv1**: 10攻（自身每失去过5生命多1攻） / 若卡组中不超过2种[五行]则[再次行动]  
  *10 ATK (1 more ATK for every 5 HP lost in this battle) / If there are no more than 2 types of [Five Elements] in your deck, [Chase]*
- **Lv2**: 15攻（自身每失去过5生命多1攻） / 若卡组中不超过2种[五行]则[再次行动]  
  *15 ATK (1 more ATK for every 5 HP lost in this battle) / If there are no more than 2 types of [Five Elements] in your deck, [Chase]*
- **Lv3**: 20攻（自身每失去过5生命多1攻） / 若卡组中不超过2种[五行]则[再次行动]  
  *20 ATK (1 more ATK for every 5 HP lost in this battle) / If there are no more than 2 types of [Five Elements] in your deck, [Chase]*

#### 穿云御风 (Pi Yun Zhui Yue) — id 169
- **Lv1**: 2攻×3 / 卡组中每有1种不同[五行]，此牌多2攻  
  *2 ATK × 3 / For each different [Five Elements] you have in your deck, this card adds 2 ATK*

#### 五行护身 (Five Elements Guard) — id 197
- **Lv1**: [防]+10 / 获得1层[护体]（首次使用时多加1层） / [激活]后一格牌的所属[五行]  
  *[DEF]+10 / Gain 1 [Guard Up](Gain 1 more on first play) / [Activate] the [Five Elements] in the next slot*
- **Lv2**: [防]+18 / 获得1层[护体]（首次使用时多加1层） / [激活]后一格牌的所属[五行]  
  *[DEF]+18 / Gain 1 [Guard Up](Gain 1 more on first play) / [Activate] the [Five Elements] in the next slot*
- **Lv3**: [防]+26 / 获得1层[护体]（首次使用时多加1层） / [激活]后一格牌的所属[五行]  
  *[DEF]+26 / Gain 1 [Guard Up](Gain 1 more on first play) / [Activate] the [Five Elements] in the next slot*

#### 天髓狂舞曲 (Heavenly Marrow Dance Tune) — id 199
*持续 Continuous*  
- **Lv1**: 双方获得2层[加攻] / [持续]：双方所有牌获得[再次行动]  
  *Both players gain 2 [Increase ATK] / [Continuous]: All cards of both players gain [Chase]*
- **Lv2**: 双方获得3层[加攻] / [持续]：双方所有牌获得[再次行动]  
  *Both players gain 3 [Increase ATK] / [Continuous]: All cards of both players gain [Chase]*
- **Lv3**: [灵气]+1 / 双方获得4层[加攻] / [持续]：双方所有牌获得[再次行动]  
  *Both players gain 4 [Increase ATK] / [Continuous]: All cards of both players gain [Chase]*

#### 浑天运笔 (Cosmos Brush) — id 200
- **Lv1**: [灵气]+2 / [防]+2 / 若后一格是[五行]牌，[激活]其[五行]并[再次行动]  
  *[Qi]+2 / [DEF]+2 / If the next slot is a [Five Elements] card, [Activate] the [Five Elements] and [Chase]*
- **Lv2**: [灵气]+3 / [防]+4 / 若后一格是[五行]牌，[激活]其[五行]并[再次行动]  
  *[Qi]+3 / [DEF]+4 / If the next slot is a [Five Elements] card, [Activate] the [Five Elements] and [Chase]*
- **Lv3**: [灵气]+4 / [防]+6 / 若后一格是[五行]牌，[激活]其[五行]并[再次行动]  
  *[Qi]+4 / [DEF]+6 / If the next slot is a [Five Elements] card, [Activate] the [Five Elements] and [Chase]*

#### 五行灵田 (Five Elements Spiritual Field) — id 202
- **Lv1**: 若在卡组最后一格，使用改为[跳过]此牌 / [被动]：战斗结束时减1修为，获得1张1级[五行]牌（优先取卡组首种[五行]）  
  *[Skip] this card if in the last slot. / [Passive]: At the end of battle you lose 1 Cul. and gain 1 [Five Elements] card (First card's [Five Elements] priority).*
- **Lv2**: 若在卡组最后一格，使用改为[跳过]此牌 / [被动]：战斗结束时减2修为，获得2张1级[五行]牌（优先取卡组首种[五行]）  
  *[Skip] this card if in the last slot. / [Passive]: At the end of battle you lose 2 Cul. and gain 2 [Five Elements] card (First card's [Five Elements] priority).*
- **Lv3**: 若在卡组最后一格，使用改为[跳过]此牌 / [被动]：战斗结束时减3修为，获得3张1级[五行]牌（优先取卡组首种[五行]）  
  *[Skip] this card if in the last slot. / [Passive]: At the end of battle you lose 3 Cul. and gain 3 [Five Elements] card (First card's [Five Elements] priority).*

#### 幻·水灵波澜 (M - Water Spirit Billows) — id 271
- **Lv1**: 获得3层[水势] / 自身回合结束时[水势]额外触发一次，持续2回合 / [水灵]：此牌不耗[灵气]  
  *Gain 3 [Force of Water]. / At the end of your turn, [Force of Water] triggers an additional time (lasts 2 turns) / [Water Spirit]: This card consumes 0 Qi*
- **Lv2**: 获得4层[水势] / 自身回合结束时[水势]额外触发一次，持续2回合 / [水灵]：此牌不耗[灵气]  
  *Gain 4 [Force of Water]. / At the end of your turn, [Force of Water] triggers an additional time (lasts 2 turns) / [Water Spirit]: This card consumes 0 Qi*
- **Lv3**: 获得5层[水势] / 自身回合结束时[水势]额外触发一次，持续2回合 / [水灵]：此牌不耗[灵气]  
  *Gain 5 [Force of Water]. / At the end of your turn, [Force of Water] triggers an additional time (lasts 2 turns) / [Water Spirit]: This card consumes 0 Qi*

#### 幻·土灵群山 (M - Earth Spirit Mountains) — id 274
- **Lv1**: [防]+10 / 自身[防]减半，每减1点造成1[伤害] / [土灵]：下回合开始时加回本次减的[防]  
  *[DEF]+10 / Your [DEF] is halved, and for each point reduced, deal 1 [DMG] / [Earth Spirit]: In your next turn, restore the [DEF] reduced this way*
- **Lv2**: [防]+15 / 自身[防]减半，每减1点造成1[伤害] / [土灵]：下回合开始时加回本次减的[防]  
  *[DEF]+15 / Your [DEF] is halved, and for each point reduced, deal 1 [DMG] / [Earth Spirit]: In your next turn, restore the [DEF] reduced this way*
- **Lv3**: [防]+20 / 自身[防]减半，每减1点造成1[伤害] / [土灵]：下回合开始时加回本次减的[防]  
  *[DEF]+20 / Your [DEF] is halved, and for each point reduced, deal 1 [DMG] / [Earth Spirit]: In your next turn, restore the [DEF] reduced this way*

#### 幻·浑天印 (M - Cosmos Seal) — id 292
- **Lv1**: 5攻 / [灵气]+1 / [激活]后1格的[五行] / [被动]：卡组中算作2种[五行]（不可叠加）  
  *5 ATK / [Qi]+1 / [Active] the [Five Elements] in next grid / [Passive]: The deck is considered to have 2 additional types of [Five Elements] (non-stackable)*
- **Lv2**: 8攻 / [灵气]+2 / [激活]后1格的[五行] / [被动]：卡组中算作2种[五行]（不可叠加）  
  *8 ATK / [Qi]+2 / [Active] the [Five Elements] in next grid / [Passive]: The deck is considered to have 2 additional types of [Five Elements] (non-stackable)*
- **Lv3**: 11攻 / [灵气]+3 / [激活]后1格的[五行] / [被动]：卡组中算作2种[五行]（不可叠加）  
  *11 ATK / [Qi]+3 / [Active] the [Five Elements] in next grid / [Passive]: The deck is considered to have 2 additional types of [Five Elements] (non-stackable)*

#### 幻·五行流转 (M - Five Elements Circulation) — id 295
- **Lv1**: [灵气]+2 / 若前后两格存在[五行相生]，则[激活]后一格的[五行]并[再次行动] / 本场战斗每[激活]过一次[五行]加2[防]  
  *[Qi]+2 / If there is [Five Element Generating Interaction] between pre and next slot, [Activate] next slot and [Chase] / Gain 2 [DEF] for each [Five Elements] [Activated]*
- **Lv2**: [灵气]+3 / 若前后两格存在[五行相生]，则[激活]后一格的[五行]并[再次行动] / 本场战斗每[激活]过一次[五行]加4[防]  
  *[Qi]+3 / If there is [Five Element Generating Interaction] between pre and next slot, [Activate] next slot and [Chase] / Gain 4 [DEF] for each [Five Elements] [Activated]*
- **Lv3**: [灵气]+4 / 若前后两格存在[五行相生]，则[激活]后一格的[五行]并[再次行动] / 本场战斗每[激活]过一次[五行]加6[防]  
  *[Qi]+4 / If there is [Five Element Generating Interaction] between pre and next slot, [Activate] next slot and [Chase] / Gain 6 [DEF] for each [Five Elements] [Activated]*

#### 幻·金灵印 (M - Metal Spirit Seal) — id 316
- **Lv1**: [锋锐]+8 / [激活金灵]、[激活木灵] / 之后的加生命效果改为加[锋锐]，持续3回合  
  *[Penetrate]+8 / [Activate Metal Spirit] / [Activate Wood Spirit] / When you add HP, convert it to [Penetrate] instead, lasts for 3 turns*
- **Lv2**: [锋锐]+12 / [激活金灵]、[激活木灵] / 之后的加生命效果改为加[锋锐]，持续4回合  
  *[Penetrate]+12 / [Activate Metal Spirit] / [Activate Wood Spirit] / When you add HP, convert it to [Penetrate] instead, lasts for 4 turns*
- **Lv3**: [锋锐]+16 / [激活金灵]、[激活木灵] / 之后的加生命效果改为加[锋锐]，持续5回合  
  *[Penetrate]+16 / [Activate Metal Spirit] / [Activate Wood Spirit] / When you add HP, convert it to [Penetrate] instead, lasts for 5 turns*


### Phase 6 — 特殊 Special

#### 瑶光溯时镜 (Kunlun Mirror) — id 173
- **Lv1**: [蓄灵]9 / [激活]全部[五行] / 复制后一格牌的效果 / [再次行动]（不会被其他效果阻止）  
  *[Gather Qi] 9 / [Activate] all [Five Elements] / Duplicate the effect of the card in the next slot / [Chase] (Cannot be stoped by other effects)*


## Derivation / event cards of 锻玄宗 Duan Xuan Sect (not in normal draw)


### Phase 1 — 炼气 Meditation

#### 罗刹扑 (Rakshasa Pouncing) — id 71
- **Lv1**: 8攻 / [灵气]+1 / 自身加1层[外伤]  
  *8 ATK / [Qi]+1 / Gain 1 stack of [Wound]*
- **Lv2**: 11攻 / [灵气]+1 / 自身加1层[外伤]  
  *11 ATK / [Qi]+1 / Gain 1 stack of [Wound]*
- **Lv3**: 14攻 / [灵气]+1 / 自身加1层[外伤]  
  *14 ATK / [Qi]+1 / Gain 1 stack of [Wound]*

#### 破空爪 (Sky-Piercing Claw) — id 72
- **Lv1**: 13攻 / 自身加1层[内伤]  
  *13 ATK / Gain 1 stack of [Internal Injury]*
- **Lv2**: 16攻 / 自身加1层[内伤]  
  *16 ATK / Gain 1 stack of [Internal Injury]*
- **Lv3**: 19攻 / 自身加1层[内伤]  
  *19 ATK / Gain 1 stack of [Internal Injury]*


### Phase 3 — 金丹 Virtuoso

#### 星辰锻骨诀 (Star Sky Forge Bone) — id 154
- **Lv1**: [体魄]+3 / [气势]+2 / 每有5体魄，下1次攻击多1攻（最多5）  
  *[Physique]+3 / [Force]+2 / For every 5 [Physique], increase your next ATK by 1 (up to 5)*
- **Lv2**: [体魄]+4 / [气势]+2 / 每有5体魄，下1次攻击多1攻（最多8）  
  *[Physique]+4 / [Force]+2 / For every 5 [Physique], increase your next ATK by 1 (up to 8)*
- **Lv3**: [体魄]+5 / [气势]+2 / 每有5体魄，下1次攻击多1攻（最多11）  
  *[Physique]+5 / [Force]+2 / For every 5 [Physique], increase your next ATK by 1 (up to 11)*


### Phase 4 — 元婴 Immortality

#### 崩拳·夺星 (Crash Fist - Star Seizing) — id 144
- **Lv1**: 12攻 / 自身回复[击伤]值60%的生命（下一张崩拳也附加此效果）  
  *12 ATK / If you [Injured] opponent with this card, you restore 60% of the damage inflicted as your own HP (also triggered in the next Crash Fist)*
- **Lv2**: 16攻 / 自身回复[击伤]值60%的生命（下一张崩拳也附加此效果）  
  *16 ATK / If you [Injured] opponent with this card, you restore 60% of the damage inflicted as your own HP (also triggered in the next Crash Fist)*
- **Lv3**: 20攻 / 自身回复[击伤]值60%的生命（下一张崩拳也附加此效果）  
  *20 ATK / If you [Injured] opponent with this card, you restore 60% of the damage inflicted as your own HP (also triggered in the next Crash Fist)*

#### 踏鹤飞云 (Cloud Footwork) — id 204
- **Lv1**: [灵气]+1 / [身法]+10 / 下2次攻击[无视防御]  
  *[Qi]+1 / [Agility]+10 / Next 2 attacks [Ignore DEF]*
- **Lv2**: [灵气]+2 / [身法]+10 / 下3次攻击[无视防御]  
  *[Qi]+2 / [Agility]+10 / Next 3 attacks [Ignore DEF]*
- **Lv3**: [灵气]+3 / [身法]+10 / 下4次攻击[无视防御]  
  *[Qi]+3 / [Agility]+10 / Next 4 attacks [Ignore DEF]*

#### 灵气锻身 (Spiritage And Exercise) — id 205
- **Lv1**: [灵气]+3 / [体魄]+3 / 每有1[灵气]加1[体魄]（上限10）  
  *[Qi]+3 / [Physique]+3 / Add 1 [Physique] for each [Qi] (up to 10）*
- **Lv2**: [灵气]+4 / [体魄]+4 / 每有1[灵气]加1[体魄]（上限15）  
  *[Qi]+4 / [Physique]+4 / Add 1 [Physique] for each [Qi] (up to 15）*
- **Lv3**: [灵气]+5 / [体魄]+5 / 每有1[灵气]加1[体魄]（上限20）  
  *[Qi]+5 / [Physique]+5 / Add 1 [Physique] for each [Qi] (up to 20）*

#### 逍遥连音曲 (Continuous Tune) — id 206
*持续 Continuous*  
- **Lv1**: [身法]+4 / [持续]：双方的下一张[普通攻击]变为其上一格的牌的升级（战斗结束还原）  
  *[Agility]+4 / [Continuous]: The next [Normal Attack] of both players will be changed to the upgraded card in their previous slot (Restored at end of battle)*
- **Lv2**: [身法]+7 / [持续]：双方的下一张[普通攻击]变为其上一格的牌的升级（战斗结束还原）  
  *[Agility]+7 / [Continuous]: The next [Normal Attack] of both players will be changed to the upgraded card in their previous slot (Restored at end of battle)*
- **Lv3**: [身法]+10 / [持续]：双方的下一张[普通攻击]变为其上一格的牌的升级（战斗结束还原）  
  *[Agility]+10 / [Continuous]: The next [Normal Attack] of both players will be changed to the upgraded card in their previous slot (Restored at end of battle)*

#### 玄域雪莲 (Mystic Snowdrop) — id 209
- **Lv1**: 生命+5 / 自身下2次获得[负面状态]时，令对方也获得同样的[负面状态]  
  *HP+5 / The next 2 times you gain [Debuff], apply the same [Debuff] to your opponent*
- **Lv2**: 生命+10 / 自身下2次获得[负面状态]时，令对方也获得同样的[负面状态]  
  *HP+10 / The next 2 times you gain [Debuff], apply the same [Debuff] to your opponent*
- **Lv3**: 生命+15 / 自身下2次获得[负面状态]时，令对方也获得同样的[负面状态]  
  *HP+15 / The next 2 times you gain [Debuff], apply the same [Debuff] to your opponent*

#### 幻·血气方刚 (M - Youthful Vigor) — id 275
- **Lv1**: 6攻×2 / 本场战斗每加过24生命就追加1次攻击  
  *6 ATK × 2 / For every 24 HP added in this battle, make an additional attack*
- **Lv2**: 6攻×2 / 本场战斗每加过18生命就追加1次攻击  
  *6 ATK × 2 / For every 18 HP added in this battle, make an additional attack*
- **Lv3**: 6攻×2 / 本场战斗每加过14生命就追加1次攻击  
  *6 ATK × 2 / For every 14 HP added in this battle, make an additional attack*

#### 幻·锻骨 (M - Exercise Bones) — id 277
*持续 Continuous*  
- **Lv1**: [持续]：加[体魄]时若超过上限，每点加2生命并造成1[伤害]  
  *[Continuous]: Whenever you add 1 [Physique], if your [Physique] exceeds the cap, gain 2 HP and deal 1 [DMG] to the opponent*
- **Lv2**: [持续]：加[体魄]时若超过上限，每点加3生命并造成1[伤害]  
  *[Continuous]: Whenever you add 1 [Physique], if your [Physique] exceeds the cap, gain 3 HP and deal 1 [DMG] to the opponent*
- **Lv3**: [持续]：加[体魄]时若超过上限，每点加4生命并造成1[伤害]  
  *[Continuous]: Whenever you add 1 [Physique], if your [Physique] exceeds the cap, gain 4 HP and deal 1 [DMG] to the opponent*

#### 幻·气沉丹田 (M - Sinking Qi) — id 278
- **Lv1**: [灵气]+2 / 生命+6 / 使用下2张牌攻击时，每点[灵气]增加10%的攻  
  *[Qi]+2 / HP+6 / Increase 10% ATK for each [Qi] for the next 2 attack cards you played*
- **Lv2**: [灵气]+3 / 生命+7 / 使用下2张牌攻击时，每点[灵气]增加10%的攻  
  *[Qi]+3 / HP+7 / Increase 10% ATK for each [Qi] for the next 2 attack cards you played*
- **Lv3**: [灵气]+3 / 生命+7 / 使用下3张牌攻击时，每点[灵气]增加10%的攻  
  *[Qi]+3 / HP+7 / Increase 10% ATK for each [Qi] for the next 3 attack cards you played*

#### 幻·岿然不动 (M - Standing Firm) — id 291
- **Lv1**: [气势]+2 / [防]+4 / 每有1[气势]加2[防] / 每有1[身法]加2生命 / [身法]减至5  
  *[Force]+2 / [DEF]+4 / Add 2 [DEF] for each [Force] / Add 2 HP for each [Agility] / [Agility] Decreased to 5*
- **Lv2**: [气势]+2 / [防]+4 / 每有1[气势]加3[防] / 每有1[身法]加2生命 / [身法]减至5  
  *[Force]+2 / [DEF]+4 / Add 3 [DEF] for each [Force] / Add 2 HP for each [Agility] / [Agility] Decreased to 5*
- **Lv3**: [气势]+2 / [防]+4 / 每有1[气势]加4[防] / 每有1[身法]加2生命 / [身法]减至5  
  *[Force]+2 / [DEF]+4 / Add 4 [DEF] for each [Force] / Add 2 HP for each [Agility] / [Agility] Decreased to 5*

#### 幻·死缠烂打 (M - Endless Entanglement) — id 318
- **Lv1**: [体魄]+2 / 双方各加2层[内伤] / 每有30点[体魄]，就令双方下回合开始时的[内伤]额外生效一次  
  *[Physique]+2 / Both players gain 2 [Internal Injury] / For each 30 [Physique], both players' [Internal Injury] will trigger 1 additional time at their next turn*
- **Lv2**: [体魄]+4 / 双方各加3层[内伤] / 每有30点[体魄]，就令双方下回合开始时的[内伤]额外生效一次  
  *[Physique]+4 / Both players gain 3 [Internal Injury] / For each 30 [Physique], both players' [Internal Injury] will trigger 1 additional time at their next turn*
- **Lv3**: [体魄]+6 / 双方各加4层[内伤] / 每有30点[体魄]，就令双方下回合开始时的[内伤]额外生效一次  
  *[Physique]+6 / Both players gain 4 [Internal Injury] / For each 30 [Physique], both players' [Internal Injury] will trigger 1 additional time at their next turn*

#### 幻·气沉丹田 (M - Sinking Qi) — id 328
- **Lv1** ⟨template⟩: [灵气]+{anima} / 自身受到的攻击减少{otherParams[2]}%，持续{otherParams[0]}回合，持续结束时，自身的下{otherParams[1]}次攻击每有1灵气就多1攻  
  *[Qi]+{anima} / You take {otherParams[2]}% less ATK for {otherParams[0]} turns, when the effect ends, add 1 ATK for each [Qi] for your next {otherParams[1]} attacks*
- **Lv2** ⟨template⟩: [灵气]+{anima} / 自身受到的攻击减少{otherParams[2]}%，持续{otherParams[0]}回合，持续结束时，自身的下{otherParams[1]}次攻击每有1灵气就多1攻  
  *[Qi]+{anima} / You take {otherParams[2]}% less ATK for {otherParams[0]} turns, when the effect ends, add 1 ATK for each [Qi] for your next {otherParams[1]} attacks*
- **Lv3** ⟨template⟩: [灵气]+{anima} / 自身受到的攻击减少{otherParams[2]}%，持续{otherParams[0]}回合，持续结束时，自身的下{otherParams[1]}次攻击每有1灵气就多1攻  
  *[Qi]+{anima} / You take {otherParams[2]}% less ATK for {otherParams[0]} turns, when the effect ends, add 1 ATK for each [Qi] for your next {otherParams[1]} attacks*

#### 玄灵附身 (Dark Spirit Possession) — id 336
- **Lv1**: [灵气]+2 / 获得3层[加攻]和3层[减攻] / 自身每有1层[负面状态]加1[身法]  
  *[Qi] + 2 / Gain 3 [Increase ATK] and 3 [Decrease ATK] / Gain 1 [Agility] for each 1 stack of [Debuff] you have*
- **Lv2**: [灵气]+3 / 获得4层[加攻]和4层[减攻] / 自身每有1层[负面状态]加1[身法]  
  *[Qi] + 3 / Gain 4 [Increase ATK] and 4 [Decrease ATK] / Gain 1 [Agility] for each 1 stack of [Debuff] you have*
- **Lv3**: [灵气]+4 / 获得5层[加攻]和5层[减攻] / 自身每有1层[负面状态]加1[身法]  
  *[Qi] + 4 / Gain 5 [Increase ATK] and 5 [Decrease ATK] / Gain 1 [Agility] for each 1 stack of [Debuff] you have*

#### 崩拳·伏虎 (Crash Fist - Tiger Subdue) — id 337
- **Lv1**: 7攻 / [防]+7 / 每有1[防]向对方造成1[伤害]（使用下1张崩拳后也附加此效果）  
  *7 [ATK] / [DEF] + 7 / Deal 1 [DMG] to the opponent for each 1 [DEF] you have (This effect also applies after playing your next 1 Crash Fist card)*
- **Lv2**: 9攻 / [防]+9 / 每有1[防]向对方造成1[伤害]（使用下1张崩拳后也附加此效果）  
  *9 [ATK] / [DEF] + 9 / Deal 1 [DMG] to the opponent for each 1 [DEF] you have (This effect also applies after playing your next 1 Crash Fist card)*
- **Lv3**: 11攻 / [防]+11 / 每有1[防]向对方造成1[伤害]（使用下1张崩拳后也附加此效果）  
  *11 [ATK] / [DEF] + 11 / Deal 1 [DMG] to the opponent for each 1 [DEF] you have (This effect also applies after playing your next 1 Crash Fist card)*


### Phase 5 — 化神 Incarnation

#### 玄冥破境掌 (Xuanming Boundary-Breaking Palms) — id 166
- **Lv1**: 4攻×2 / 自身每失去过30生命就多攻击1次  
  *4 ATK × 2 / Make an additional attack for every 30 HP lost in this battle*
- **Lv2**: 5攻×2 / 自身每失去过27生命就多攻击1次  
  *5 ATK × 2 / Make an additional attack for every 27 HP lost in this battle*
- **Lv3**: 6攻×2 / 自身每失去过25生命就多攻击1次  
  *6 ATK × 2 / Make an additional attack for every 25 HP lost in this battle*

#### 玄真破妄 (Jiu Qi Po Xiao) — id 170
- **Lv1**: 10攻 / 耗尽自身全部[气势]/[灵气]/[身法]，每点分别多4/3/2攻  
  *10 ATK / Exhaust [Force] / [Qi] / [Agility], add 4/3/2 ATK for each point exhausted*

#### 锻龙诀 (Exercise To The Utmost) — id 207
*消耗 Consumable*  
- **Lv1**: [体魄]+4 / [体魄上限]永久+3 / 获得2层[加攻] / [消耗]  
  *[Physique]+4 / Physique Cap+3 permanently. / Gain 2 [Increase ATK] / [Consumption]*
- **Lv2**: [体魄]+6 / [体魄上限]永久+3 / 获得3层[加攻] / [消耗]  
  *[Physique]+6 / Physique Cap+3 permanently. / Gain 3 [Increase ATK] / [Consumption]*
- **Lv3**: [体魄]+8 / [体魄上限]永久+3 / 获得4层[加攻] / [消耗]  
  *[Physique]+8 / Physique Cap+3 permanently. / Gain 4 [Increase ATK] / [Consumption]*

#### 势灵阵 (Force Spiritage Formation) — id 208
*持续 Continuous*  
- **Lv1**: [气势]上限+4 / [持续]2次：回合开始时加2[灵气]与[气势]  
  *[Force] Cap+4 / [Continuous] 2 [Times]: At the beginning of your turn, add 2 [Qi] and [Force]*
- **Lv2**: [气势]上限+4 / [持续]3次：回合开始时加2[灵气]与[气势]  
  *[Force] Cap+4 / [Continuous] 3 [Times]: At the beginning of your turn, add 2 [Qi] and [Force]*
- **Lv3**: [气势]上限+4 / [持续]4次：回合开始时加2[灵气]与[气势]  
  *[Force] Cap+4 / [Continuous] 4 [Times]: At the beginning of your turn, add 2 [Qi] and [Force]*

#### 天机·返蛊 (Heavenly Will - Seizing) — id 210
- **Lv1**: 10攻 / 下1次攻击时先转移对手所有[负面状态]到自身，每转移1层多1攻  
  *10 ATK / Next 1 attack will transfer all [Debuff] from the opponent to yourself (gain 1 additional ATK for every [Debuff] transferred)*
- **Lv2**: 16攻 / 下1次攻击时先转移对手所有[负面状态]到自身，每转移1层多1攻  
  *16 ATK / Next 1 attack will transfer all [Debuff] from the opponent to yourself (gain 1 additional ATK for every [Debuff] transferred)*
- **Lv3**: 22攻 / 下1次攻击时先转移对手所有[负面状态]到自身，每转移1层多1攻  
  *22 ATK / Next 1 attack will transfer all [Debuff] from the opponent to yourself (gain 1 additional ATK for every [Debuff] transferred)*

#### 幻·双鬼拍门 (M - Double Trouble) — id 296
- **Lv1**: 6攻×2 / 双方各加2层[内伤]、1层[外伤]和1层[虚弱]  
  *6 ATK × 2  /  Both players gain 2 [Internal Injury], 1 [Wound] and 1 [Weakened]*
- **Lv2**: 8攻×2 / 双方各加4层[内伤]、1层[外伤]和1层[虚弱]  
  *8 ATK × 2  /  Both players gain 4 [Internal Injury], 1 [Wound] and 1 [Weakened]*
- **Lv3**: 10攻×2 / 双方各加6层[内伤]、1层[外伤]和1层[虚弱]  
  *10 ATK × 2  /  Both players gain 6 [Internal Injury], 1 [Wound] and 1 [Weakened]*

#### 幻·罗刹扑 (M - Rakshasa Pouncing) — id 297
- **Lv1**: [灵气]+1 / 将对方所有[负面状态]转为[外伤] / 12攻 / 下3次攻击[无视防御]  
  *[Qi]+1 / Convert all opponent's [Debuff] to [Wound] / 12 ATK / Next 3 attack [Ignore DEF]*
- **Lv2**: [灵气]+1 / 将对方所有[负面状态]转为[外伤] / 18攻 / 下4次攻击[无视防御]  
  *[Qi]+1 / Convert all opponent's [Debuff] to [Wound] / 18 ATK / Next 4 attack [Ignore DEF]*
- **Lv3**: [灵气]+1 / 将对方所有[负面状态]转为[外伤] / 24攻 / 下5次攻击[无视防御]  
  *[Qi]+1 / Convert all opponent's [Debuff] to [Wound] / 24 ATK / Next 5 attack [Ignore DEF]*

#### 幻·崩拳戳 (M - Crash Fist Poke) — id 308
- **Lv1**: 12攻 / 每有8点[体魄]，下张崩拳多1攻  
  *12 ATK / For every 8 [Physique], the next Crash Fist increase 1 ATK*
- **Lv2**: 12攻 / 每有7点[体魄]，下张崩拳多1攻  
  *12 ATK / For every 7 [Physique], the next Crash Fist increase 1 ATK*
- **Lv3**: 12攻 / 每有6点[体魄]，下张崩拳多1攻  
  *12 ATK / For every 6 [Physique], the next Crash Fist increase 1 ATK*

#### 幻·浩然正气 (M - Magnanimous Righteousness) — id 310
- **Lv1**: [灵气]+2 / [身法]+6 / 自身减最多4层[负面状态]，每减1层再加1[身法]和1[气势]  
  *[Qi]+2 / [Agility]+6 / Remove up to 4 stacks of [Debuff], and for each stack removed, gain 1 [Agility] and 1 [Force]*
- **Lv2**: [灵气]+2 / [身法]+6 / 自身减最多6层[负面状态]，每减1层再加1[身法]和1[气势]  
  *[Qi]+2 / [Agility]+6 / Remove up to 6 stacks of [Debuff], and for each stack removed, gain 1 [Agility] and 1 [Force]*
- **Lv3**: [灵气]+2 / [身法]+6 / 自身减最多8层[负面状态]，每减1层再加1[身法]和1[气势]  
  *[Qi]+2 / [Agility]+6 / Remove up to 8 stacks of [Debuff], and for each stack removed, gain 1 [Agility] and 1 [Force]*

#### 幻·崩拳缠 (M - Crash Fist Entangle) — id 319
- **Lv1**: 施加2层[外伤] / 3攻×2 / 使用下张崩拳后追加3攻×2  
  *Apply 2 [Wound] / 3 ATK × 2 / After you played the next Crash Fist, make 3 ATK × 2*
- **Lv2**: 施加2层[外伤] / 3攻×3 / 使用下张崩拳后追加3攻×2  
  *Apply 2 [Wound] / 3 ATK × 3 / After you played the next Crash Fist, make 3 ATK × 2*
- **Lv3**: 施加2层[外伤] / 3攻×4 / 使用下张崩拳后追加3攻×2  
  *Apply 2 [Wound] / 3 ATK × 4 / After you played the next Crash Fist, make 3 ATK × 2*

#### 瞬影击 (Instant Shadow Strike) — id 338
- **Lv1**: [身法]+8 / [跳过]自身下2张[耗生命]的牌，此法[跳过]的牌仍会[耗生命]，每耗1生命向对方造成2[伤害]  
  *[Agility] + 8 / [Skip] your next 2 [HP cost] cards. Cards [Skipped] this way still trigger [HP cost], and deal 2 [DMG] to the opponent for each 1 HP consumed*
- **Lv2**: [身法]+8 / [跳过]自身下3张[耗生命]的牌，此法[跳过]的牌仍会[耗生命]，每耗1生命向对方造成2[伤害]  
  *[Agility] + 8 / [Skip] your next 3 [HP cost] cards. Cards [Skipped] this way still trigger [HP cost], and deal 2 [DMG] to the opponent for each 1 HP consumed*
- **Lv3**: [身法]+8 / [跳过]自身下4张[耗生命]的牌，此法[跳过]的牌仍会[耗生命]，每耗1生命向对方造成2[伤害]  
  *[Agility] + 8 / [Skip] your next 4 [HP cost] cards. Cards [Skipped] this way still trigger [HP cost], and deal 2 [DMG] to the opponent for each 1 HP consumed*

#### 逍遥无影拳 (Carefree Shadowless Fist) — id 339
- **Lv1**: 2攻×4（卡组中每有1张普通攻击就多攻击1次） / 此牌每次攻击时加1[体魄]和1[身法]  
  *2 [ATK] × 4 (Attack an additional time for each 1 Normal Attack card in your deck) / Gain 1 [Physique] and 1 [Agility] each time this card attacks*
- **Lv2**: 2攻×5（卡组中每有1张普通攻击就多攻击1次） / 此牌每次攻击时加1[体魄]和1[身法]  
  *2 [ATK] × 5 (Attack an additional time for each 1 Normal Attack card in your deck) / Gain 1 [Physique] and 1 [Agility] each time this card attacks*
- **Lv3**: 2攻×6（卡组中每有1张普通攻击就多攻击1次） / 此牌每次攻击时加1[体魄]和1[身法]  
  *2 [ATK] × 6 (Attack an additional time for each 1 Normal Attack card in your deck) / Gain 1 [Physique] and 1 [Agility] each time this card attacks*


### Phase 6 — 特殊 Special

#### 裂穹开天斧 (Pangu Axe) — id 174
- **Lv1**: 30攻 / 令对方无法加生命，持续1回合 / [击伤]：对方下次生命≤0时，对其造成20命元伤害  
  *30 ATK / Your opponent cannot add HP for 1 turn / [Injured]: For the next time when your opponent's HP ≤ 0, deal 20 Destiny Damage to your opponent.*


## General, event & special cards (id < 1,000,000)


### Phase 1 — 炼气 Meditation

#### 普通攻击 (Normal Attack) — id 0
- **Lv1** ⟨template⟩: {attack}攻  
  *{attack} ATK*
- **Lv2**: 6攻  
  *6 ATK*
- **Lv3**: 9攻  
  *9 ATK*

#### 澄心剑胚 (Clear Heart Sword Embryo) — id 19
- **Lv1**: 7攻 / 根据仙命选择附加对应效果  
  *7 ATK / Effects according to your choice of Immortal Fate*
- **Lv2**: 7攻 / 根据仙命选择附加对应效果
- **Lv3**: 7攻 / 根据仙命选择附加对应效果

#### 算无遗策 (Perfectly Planned) — id 22
- **Lv1**: [灵气]+1 / [卦象]+1 / 后1格[成为星位]  
  *[Qi]+1 / [Hexagram]+1 / The next slot [Become Star Point]*
- **Lv2**: [灵气]+1 / [卦象]+1 / 后1格[成为星位] / [星力]+1  
  *[Qi]+1 / [Hexagram]+1 / The next slot [Become Star Point] / [Star Power]+1*
- **Lv3**: [灵气]+1 / [卦象]+1 / 后1格[成为星位] / [星力]+1 / 生命及上限+4  
  *[Qi]+1 / [Hexagram]+1 / The next slot [Become Star Point] / [Star Power]+1 / HP and Max HP+4*

#### 小鱼干 (Dried small fish) — id 33
- **Lv1**: [炼化]：生命上限+1，[命元]+2  
  *[Absorb]: Max HP+1, [Destiny]+2*
- **Lv2**: [炼化]：生命上限+2，[命元]+4  
  *[Absorb]: Max HP+2, [Destiny]+4*
- **Lv3**: [炼化]：生命上限+4，[命元]+8  
  *[Absorb]: Max HP+4, [Destiny]+8*

#### 猫薄荷 (Catnip) — id 34
- **Lv1**: [炼化]：随机升级手牌或卡组中1张1级牌（优先升级名字含“猫”的牌）  
  *[Absorb]: Upgrade 1 Level 1 card(s) in your hand or deck randomly (Prioritize upgrading cards with "Cat" in their name)*
- **Lv2**: [炼化]：随机升级手牌或卡组中2张1级牌（优先升级名字含“猫”的牌）  
  *[Absorb]: Upgrade 2 Level 1 card(s) in your hand or deck randomly (Prioritize upgrading cards with "Cat" in their name)*
- **Lv3**: [炼化]：随机升级手牌或卡组中2张2级牌（优先升级名字含“猫”的牌）  
  *[Absorb]: Upgrade 2 Level 2 card(s) in your hand or deck randomly (Prioritize upgrading cards with "Cat" in their name)*

#### 逗猫棒 (Cat Teaser) — id 35
- **Lv1**: [炼化]：换牌机会+1  
  *[Absorb]: Exchange Card Chance+1*
- **Lv2**: [炼化]：换牌机会+2  
  *[Absorb]: Exchange Card Chance+2*
- **Lv3**: [炼化]：换牌机会+4  
  *[Absorb]: Exchange Card Chance+4*

#### 云剑·飞砂 (Cloud Sword - Flying Sand) — id 36
- **Lv1**: 5攻 / [连云]：施加2层[破绽]  
  *5 ATK / [Cloud Hit]: Apply 2 stacks of [Flaw]*
- **Lv2**: 8攻 / [连云]：施加2层[破绽]  
  *8 ATK / [Cloud Hit]: Apply 2 stacks of [Flaw]*
- **Lv3**: 9攻 / [连云]：施加3层[破绽]  
  *9 ATK / [Cloud Hit]: Apply 3 stacks of [Flaw]*

#### 青铜猫 (Bronze Cat) — id 37
- **Lv1**: [防]+5 / 每有1点剑意多加2[防]  
  *[DEF]+5 / For each Sword Intent add 2 [DEF]*
- **Lv2**: [防]+5 / 每有1点剑意多加3[防]  
  *[DEF]+5 / For each Sword Intent add 3 [DEF]*
- **Lv3**: [防]+5 / 每有1点剑意多加4[防]  
  *[DEF]+5 / For each Sword Intent add 4 [DEF]*

#### 鱼跃龙门 (Leaping the Dragon Gate) — id 78
- **Lv1**: 3攻 / [被动]：战斗结束后升级此牌  
  *3 ATK / As long as this card is in your deck, upgrade it at the end of battle.*
- **Lv2**: 6攻 / [被动]：战斗结束后升级此牌  
  *6 ATK / As long as this card is in your deck, upgrade it at the end of battle.*
- **Lv3**: 9攻 / [被动]：战斗结束后此牌变为1级的[龙]  
  *9 ATK / As long as this card is in your deck, turn it into lv.1 [Loong] the end of battle.*

#### 红豆粽 (Red Bean Zongzi) — id 83
- **Lv1**: [甜粽] / 生命+10  
  *[Sweet Zongzi] / HP+10*
- **Lv2**: [甜粽] / 生命+13  
  *[Sweet Zongzi] / HP+13*
- **Lv3**: [甜粽] / 生命+16  
  *[Sweet Zongzi] / HP+16*

#### 红枣粽 (Jujube Zongzi) — id 84
- **Lv1**: [甜粽] / [灵气]+1 / 生命+4  
  *[Sweet Zongzi] / [Qi]+1 / HP+4*
- **Lv2**: [甜粽] / [灵气]+1 / 生命+7  
  *[Sweet Zongzi] / [Qi]+1 / HP+7*
- **Lv3**: [甜粽] / [灵气]+1 / 生命+10  
  *[Sweet Zongzi] / [Qi]+1 / HP+10*

#### 蜂蜜粽 (Honey Zongzi) — id 85
- **Lv1**: [甜粽] / 生命+3 / 获得1层[恢复]  
  *[Sweet Zongzi] / HP+3 / Gain 1 stack of [Regeneration]*
- **Lv2**: [甜粽] / 生命+6 / 获得1层[恢复]  
  *[Sweet Zongzi] / HP+6 / Gain 1 stack of [Regeneration]*
- **Lv3**: [甜粽] / 生命+9 / 获得1层[恢复]  
  *[Sweet Zongzi] / HP+9 / Gain 1 stack of [Regeneration]*

#### 咸肉粽 (Salted Meat Zongzi) — id 98
- **Lv1**: [咸粽] / [灵气]+1 / 生命+6 / 获得1层[内伤]  
  *[Salty Zongzi] / [Qi]+1 / HP+6 / Gain 1 stack of [Internal Injury]*
- **Lv2**: [咸粽] / [灵气]+1 / 生命+9 / 获得1层[内伤]  
  *[Salty Zongzi] / [Qi]+1 / HP+9 / Gain 1 stack of [Internal Injury]*
- **Lv3**: [咸粽] / [灵气]+1 / 生命+12 / 获得1层[内伤]  
  *[Salty Zongzi] / [Qi]+1 / HP+12 / Gain 1 stack of [Internal Injury]*

#### 香菇粽 (Mushroom Zongzi) — id 99
- **Lv1**: [咸粽] / 生命+6 / 耗1[灵气]：生命+3  
  *[Salty Zongzi] / HP+6 / Cost 1 [Qi]: HP+3*
- **Lv2**: [咸粽] / 生命+9 / 耗1[灵气]：生命+3  
  *[Salty Zongzi] / HP+9 / Cost 1 [Qi]: HP+3*
- **Lv3**: [咸粽] / 生命+12 / 耗1[灵气]：生命+3  
  *[Salty Zongzi] / HP+12 / Cost 1 [Qi]: HP+3*

#### 鲜肉粽 (Fresh Meat Zongzi) — id 100
- **Lv1**: [咸粽] / 生命+6 / 随机减1层[负面状态]  
  *[Salty Zongzi] / HP+6 / Reduce 1 stack of random [Debuff]*
- **Lv2**: [咸粽] / 生命+9 / 随机减1层[负面状态]  
  *[Salty Zongzi] / HP+9 / Reduce 1 stack of random [Debuff]*
- **Lv3**: [咸粽] / 生命+12 / 随机减1层[负面状态]  
  *[Salty Zongzi] / HP+12 / Reduce 1 stack of random [Debuff]*

#### 白粽 (Pure Rice Zongzi) — id 113
- **Lv1**: 生命+3  
  *HP+3*
- **Lv2**: 生命+6  
  *HP+6*
- **Lv3**: 生命+9  
  *HP+9*

#### 1 (1) — id 115
- **Lv1**: 1 / [炼化]→7 / [置换]→2  
  *1 / [Absorb]→7 / [Exchange]→2*

#### 2 (2) — id 116
- **Lv1**: 2 / [炼化]→1 / [置换]→3  
  *2 / [Absorb]→1 / [Exchange]→3*

#### 3 (3) — id 117
- **Lv1**: 3 / [炼化]→2 / [置换]→4  
  *3 / [Absorb]→2 / [Exchange]→4*

#### 4 (4) — id 118
- **Lv1**: 4 / [炼化]→3 / [置换]→5  
  *4 / [Absorb]→3 / [Exchange]→5*

#### 5 (5) — id 119
- **Lv1**: 5 / [炼化]→4 / [置换]→6  
  *5 / [Absorb]→4 / [Exchange]→6*

#### 6 (6) — id 120
- **Lv1**: 6 / [炼化]→5 / [置换]→7  
  *6 / [Absorb]→5 / [Exchange]→7*

#### 7 (7) — id 121
- **Lv1**: 7 / [炼化]→6 / [置换]→1  
  *7 / [Absorb]→6 / [Exchange]→1*

#### 一段攻击 (1 Attack) — id 145
- **Lv1**: 3攻  
  *3 ATK*

#### 二段攻击 (2 Attacks) — id 146
- **Lv1**: 3攻×2  
  *3 ATK × 2*

#### 三段攻击 (3 Attacks) — id 147
- **Lv1**: 3攻×3  
  *3 ATK × 3*

#### 四段攻击 (4 Attacks) — id 148
- **Lv1**: 3攻×4  
  *3 ATK × 4*

#### 五段攻击 (5 Attacks) — id 149
- **Lv1**: 3攻×5  
  *3 ATK × 5*

#### 七段攻击 (7 Attacks) — id 150
- **Lv1**: 3攻×7  
  *3 ATK × 7*

#### 玄冥之水 (Xuanming Waters) — id 155
- **Lv1**: [炼化]或[融汇]：生命上限+3 / [置换]：换牌机会+3  
  *[Absorb] or [Fuse]: Max HP + 3 / [Exchange]: Exchange Card Chance + 3*

#### 双节棍 (Double Stick) — id 219
- **Lv1**: 6攻 / [拳]：每有5[体魄]加1[防] / [棍]：追加1攻（每有6[体魄]多1攻） / 使用后[切换架势]  
  *6 ATK / [Fist]: Gain 1 DEF for every 5 [Physique] / [Stick]: Make an additional 1 ATK (Gain 1 ATK for every 6 [Physique]) / [Switch Stance]*
- **Lv2**: 9攻 / [拳]：每有5[体魄]加1[防] / [棍]：追加1攻（每有6[体魄]多1攻） / 使用后[切换架势]  
  *9 ATK / [Fist]: Gain 1 DEF for every 5 [Physique] / [Stick]: Make an additional 1 ATK (Gain 1 ATK for every 6 [Physique]) / [Switch Stance]*
- **Lv3**: 12攻 / [拳]：每有5[体魄]加1[防] / [棍]：追加1攻（每有6[体魄]多1攻） / 使用后[切换架势]  
  *12 ATK / [Fist]: Gain 1 DEF for every 5 [Physique] / [Stick]: Make an additional 1 ATK (Gain 1 ATK for every 6 [Physique]) / [Switch Stance]*

#### 休息 (Rest) — id 223
- **Lv1**: [使用]：[体力]+2  
  *[Use]: [Energy]+2*

#### 炼丹炉 (Furnace ) — id 224
- **Lv1**: [使用]：耗2体力，获得1张丹药牌  
  *[Use]: Costs 2 [Energy], gain 1 random elixir card*

#### 地灵丹 (Earth Spirit Elixir) — id 225
- **Lv1**: [出售]：[通宝]+14 / [炼化]：额外加6[通宝]  
  *[Sell]: [Coin]+14 / [Absorb]: Add 6 Extra [Coin]*

#### 奔雷符 (Thunder Fulu) — id 234
- **Lv1**: [使用]：[通宝]+2~10  
  *[Use]: [Coin]+2~10*

#### 护灵符 (Guard Spirit Fulu) — id 235
- **Lv1**: [使用]：耗1[体力]，[通宝]+8  
  *[Use]: Costs 1 [Energy], [Coin]+8*

#### 玄银甲 (Black Silver Armor) — id 244
- **Lv1**: [耐久]2 / [使用]：[通宝]+12  
  *[Durability] 2 / [Use]: [Coin]+12*
- **Lv2**: [耐久]1 / [使用]：[通宝]+12  
  *[Durability] 1 / [Use]: [Coin]+12*

#### 刺尖枪 (Thorns Spear) — id 245
- **Lv1**: [耐久]2 / [使用]：每有3[通宝]就加1[通宝](最多14)  
  *[Durability] 2 / [Use]: gain 1 [Coin] for every 3 [Coin] (Up to 14)*
- **Lv2**: [耐久]1 / [使用]：每有3[通宝]就加1[通宝](最多14)  
  *[Durability] 1 / [Use]: gain 1 [Coin] for every 3 [Coin] (Up to 14)*

#### 逍遥·无相 (Xiaoyao - Formless) — id 280
- **Lv1**: 令对方跳过下1张牌 / [再次行动] / <#B21D81>[耗尽]</color>  
  *[Skip] opponent's next 1 card / [Chase] / <#B21D81>[Exhaust]</color>*

#### 逍遥·无隙 (Xiaoyao - Seamless) — id 281
- **Lv1**: 获得1层[护体] / [再次行动] / <#B21D81>[耗尽]</color>  
  *Gain 1 [Guard Up] / [Chase] / <#B21D81>[Exhaust]</color>*

#### 逍遥·无息 (Xiaoyao - Breathless) — id 282
- **Lv1**: 施加4层[内伤] / <#B21D81>[耗尽]</color>  
  *Apply 4 [Internal Injury] / <#B21D81>[Exhaust]</color>*

#### 逍遥·无衡 (Xiaoyao - Imbalance) — id 283
- **Lv1**: 施加2层[虚弱] / 施加3层[破绽] / <#B21D81>[耗尽]</color>  
  *Apply 2 [Weakened] and 3 [Flaw] / <#B21D81>[Exhaust]</color>*

#### 逍遥·无回 (Xiaoyao - Irreversible) — id 284
- **Lv1**: 20攻 / <#B21D81>[耗尽]</color>  
  *20 ATK / <#B21D81>[Exhaust]</color>*

#### 逍遥·无律 (Xiaoyao - Lawless) — id 285
- **Lv1**: 4攻×4 / <#B21D81>[耗尽]</color>  
  *4 ATK × 4 / <#B21D81>[Exhaust]</color>*

#### 普通攻击 (Normal Attack) — id 286
- **Lv1**: 3攻  
  *3 ATK*
- **Lv2**: 6攻  
  *6 ATK*
- **Lv3**: 9攻  
  *9 ATK*

#### 逍遥·附灵 — id 287
- **Lv1**: [炼化]：若卡组首格为炼气期或筑基期[常规牌]，本局游戏所有该名称的牌附加“[灵气]+1”的效果  
  *[Absorb]: If the first card in your deck is a [Regular Card] of Meditation Phase or Foundation Phase, all such cards gain the effect of "[Qi] +1" for the rest of the game.*

#### 逍遥·复刻 (Xiaoyao - Reproduction) — id 322
- **Lv1**: 此牌使用时，先永久变为对方的同格牌  
  *When using this card, first permanently transform it into the opponent's card in the same grid.*

#### 角度 (Angle) — id 326
- **Lv1**: 角度{0}  
  *Angle {0}*

#### 力度 (Force) — id 327
- **Lv1**: 力度{0}  
  *Force {0}*

#### 暗器 (Hidden Weapon) — id 330
*消耗 Consumable*  
- **Lv1**: 造成5伤害 / 施加1层[内伤]和[外伤] / [消耗]  
  *Deal 5 [DMG] / Apply 1 [Internal Injury] and [Wound] / [Consumption]*
- **Lv2**: 造成8伤害 / 施加1层[内伤]和[外伤] / [消耗]  
  *Deal 8 [DMG] / Apply 1 [Internal Injury] and [Wound] / [Consumption]*
- **Lv3**: 造成11伤害 / 施加1层[内伤]和[外伤] / [消耗]  
  *Deal 11 [DMG] / Apply 1 [Internal Injury] and [Wound] / [Consumption]*

#### 天马行空 (Heavenly Horse Soaring the Skies) — id 352
- **Lv1**: 随机使用1张门派牌或副职牌  
  *Randomly play 1 Sect Card or Side Job Card*
- **Lv2**: 随机使用1张门派牌或副职牌  
  *Randomly play 1 Sect Card or Side Job Card*
- **Lv3**: 随机使用1张门派牌或副职牌  
  *Randomly play 1 Sect Card or Side Job Card*

#### 金戈铁马 (Golden Spears and Iron Horses) — id 353
- **Lv1**: 3攻 / 随机使用1张含攻击效果的门派牌  
  *3 ATK / Randomly play 1 Sect Card with Attack Effect*
- **Lv2**: 4攻 / 随机使用1张含攻击效果的门派牌  
  *4 ATK / Randomly play 1 Sect Card with Attack Effect*
- **Lv3**: 5攻 / 随机使用1张含攻击效果的门派牌  
  *5 ATK / Randomly play 1 Sect Card with Attack Effect*

#### 马蹄 (Horse’s Hoof) — id 367
- **Lv1**: 1～8攻  
  *1~8 ATK*
- **Lv2**: 1～12攻  
  *1~12 ATK*
- **Lv3**: 1～16攻  
  *1~16 ATK*


### Phase 2 — 筑基 Foundation

#### 云剑·猫爪 (Cloud Sword - Cat Paw) — id 8
- **Lv1**: 4攻×2 / 此牌攻击时[无视防御]  
  *4 ATK × 2 / This card's attacks Ignore DEF*
- **Lv2**: 6攻×2 / 此牌攻击时[无视防御]  
  *6 ATK × 2 / This card's attacks Ignore DEF*
- **Lv3**: 8攻×2 / 此牌攻击时[无视防御]  
  *8 ATK × 2 / This card's attacks Ignore DEF*

#### 飞鸿踏雪 (Only Traces) — id 12
- **Lv1**: [灵气]+3 / [后招]：[再次行动]  
  *[Qi]+3 / [Post Action]: [Chase]*
- **Lv2**: [灵气]+3 / 减4生命并[再次行动] / [后招]：生命+1  
  *[Qi]+3 / Lose 4 HP and [Chase] / [Post Action]: HP+1*
- **Lv3**: [灵气]+4 / 减4生命并[再次行动] / [后招]：生命+1  
  *[Qi]+4 / Lose 4 HP and [Chase] / [Post Action]: HP+1*

#### 木灵·桃花印 (Wood Spirit - Peach Blossom Seal) — id 20
- **Lv1**: 2攻×2 / [灵气]+2 / [激活木灵]  
  *2 ATK × 2 / [Qi]+2 / [Activate Wood Spirit]*
- **Lv2**: 2攻×3 / [灵气]+3 / [激活木灵]  
  *2 ATK × 3 / [Qi]+3 / [Activate Wood Spirit]*
- **Lv3**: 2攻×4 / [灵气]+4 / [激活木灵]  
  *2 ATK × 4 / [Qi]+4 / [Activate Wood Spirit]*

#### 爆竹 (Firecracker) — id 41
*消耗 Consumable*  
- **Lv1**: 获得2层[辟邪] / 对方跳过下1张牌 / [消耗]  
  *Gain 2 [Hexproof] / Opponent skips their next card / [Consumption]*
- **Lv2**: 获得3层[辟邪] / 对方跳过下1张牌 / [消耗]  
  *Gain 3 [Hexproof] / Opponent skips their next card / [Consumption]*
- **Lv3**: 获得4层[辟邪] / 对方跳过下1张牌 / [消耗]  
  *Gain 4 [Hexproof] / Opponent skips their next card / [Consumption]*

#### 锻体不息 (Unceasing Exercising) — id 45
- **Lv1**: 6攻 / [体魄]+3 / 生命+3  
  *6 ATK / [Physique]+3 / HP+3*
- **Lv2**: 8攻 / [体魄]+4 / 生命+4  
  *8 ATK / [Physique]+4 / HP+4*
- **Lv3**: 10攻 / [体魄]+5 / 生命+5  
  *10 ATK / [Physique]+5 / HP+5*

#### 盛气凌人 (Overwhelming Power) — id 70
*持续 Continuous*  
- **Lv1**: [防]+4 / [气势]+2 / [持续]：每失去1[气势]或超过上限1[气势]时，向对方造成2[伤害]  
  *[DEF]+4 / [Force]+2 / [Continuous]: Whenever you lose 1 [Force] or have 1 [Force] exceeding the cap, deal 2 [DMG] to the opponent*
- **Lv2**: [防]+5 / [气势]+3 / [持续]：每失去1[气势]或超过上限1[气势]时，向对方造成2[伤害]  
  *[DEF]+5 / [Force]+3 / [Continuous]: Whenever you lose 1 [Force] or have 1 [Force] exceeding the cap, deal 2 [DMG] to the opponent*
- **Lv3**: [防]+6 / [气势]+4 / [持续]：每失去1[气势]或超过上限1[气势]时，向对方造成2[伤害]  
  *[DEF]+6 / [Force]+4 / [Continuous]: Whenever you lose 1 [Force] or have 1 [Force] exceeding the cap, deal 2 [DMG] to the opponent*

#### 绿豆粽 (Mung Bean Zongzi) — id 86
- **Lv1**: [甜粽] / 生命+8（每用过1张[甜粽]多加1生命）  
  *[Sweet Zongzi] / HP+8(for each [Sweet Zongzi] used before, add 1 more HP)*
- **Lv2**: [甜粽] / 生命+12（每用过1张[甜粽]多加1生命）  
  *[Sweet Zongzi] / HP+12(for each [Sweet Zongzi] used before, add 1 more HP)*
- **Lv3**: [甜粽] / 生命+16（每用过1张[甜粽]多加1生命）  
  *[Sweet Zongzi] / HP+16(for each [Sweet Zongzi] used before, add 1 more HP)*

#### 蜜枣粽 (Candied Jujube Zongzi) — id 87
- **Lv1**: [甜粽] / [灵气]+2 / 每有1点[灵气]加1生命  
  *[Sweet Zongzi] / [Qi]+2 / Add 1 HP for each [Qi]*
- **Lv2**: [甜粽] / [灵气]+3 / 每有1点[灵气]加1生命  
  *[Sweet Zongzi] / [Qi]+3 / Add 1 HP for each [Qi]*
- **Lv3**: [甜粽] / [灵气]+4 / 每有1点[灵气]加1生命  
  *[Sweet Zongzi] / [Qi]+4 / Add 1 HP for each [Qi]*

#### 枣泥粽 (Jujube Paste Zongzi) — id 88
- **Lv1**: [甜粽] / [灵气]+1 / 生命+6（每剩余1点[灵气]多加2生命） / 获得2层[食滞]  
  *[Sweet Zongzi] / [Qi]+1 / HP+6(add 2 more HP for each [Qi] left) / Gain 2 stacks of [Indigestion]*
- **Lv2**: [甜粽] / [灵气]+1 / 生命+10（每剩余1点[灵气]多加2生命） / 获得2层[食滞]  
  *[Sweet Zongzi] / [Qi]+1 / HP+10(add 2 more HP for each [Qi] left) / Gain 2 stacks of [Indigestion]*
- **Lv3**: [甜粽] / [灵气]+1 / 生命+14（每剩余1点[灵气]多加2生命） / 获得2层[食滞]  
  *[Sweet Zongzi] / [Qi]+1 / HP+14(add 2 more HP for each [Qi] left) / Gain 2 stacks of [Indigestion]*

#### 烧肉粽 (Roasted Meat Zongzi) — id 101
- **Lv1**: [咸粽] / 获得1层[食欲] / 生命+2  
  *[Salty Zongzi] / Gain 1 stack of [Appetite] / HP+2*
- **Lv2**: [咸粽] / 获得1层[食欲] / 生命+6  
  *[Salty Zongzi] / Gain 1 stack of [Appetite] / HP+6*
- **Lv3**: [咸粽] / 获得1层[食欲] / 生命+10  
  *[Salty Zongzi] / Gain 1 stack of [Appetite] / HP+10*

#### 麻辣粽 (Spicy Zongzi) — id 102
- **Lv1**: [咸粽] / 获得1层[内伤] / 重复2次：生命+5 / 耗1[灵气]：生命+4  
  *[Salty Zongzi] / Gain 1 stack of [Internal Injury] / Repeat 2 times: HP+5 / Cost 1 [Qi]: HP+4*
- **Lv2**: [咸粽] / 获得1层[内伤] / 重复2次：生命+7 / 耗1[灵气]：生命+4  
  *[Salty Zongzi] / Gain 1 stack of [Internal Injury] / Repeat 2 times: HP+7 / Cost 1 [Qi]: HP+4*
- **Lv3**: [咸粽] / 获得1层[内伤] / 重复2次：生命+9 / 耗1[灵气]：生命+4  
  *[Salty Zongzi] / Gain 1 stack of [Internal Injury] / Repeat 2 times: HP+9 / Cost 1 [Qi]: HP+4*

#### 腊肉粽 (Preserved Meat Zongzi) — id 103
- **Lv1**: [咸粽] / [灵气]+1 / 生命+3 / 获得1层[辟邪]  
  *[Salty Zongzi] / [Qi]+1 / HP+3 / Gain 1 stack of [Hexproof]*
- **Lv2**: [咸粽] / [灵气]+1 / 生命+6 / 获得2层[辟邪]  
  *[Salty Zongzi] / [Qi]+1 / HP+6 / Gain 2 stacks of [Hexproof]*
- **Lv3**: [咸粽] / [灵气]+1 / 生命+9 / 获得3层[辟邪]  
  *[Salty Zongzi] / [Qi]+1 / HP+9 / Gain 3 stacks of [Hexproof]*

#### 阴符玉简 (Jade Scroll of Yin Symbol) — id 214
*持续 Continuous*  
- **Lv1**: 施加1层[虚弱]和2层[破绽] / [持续]：对方所受[虚弱]和[破绽]效果从40%提升至50%  
  *[Qi]+{anima} / Apply 1 [Weakened] and 2 [Flaw] / [Continuous]: The [Weakened] and [Flaw] effects on the opponent are increased from 40% to 50%.*
- **Lv2**: 施加2层[虚弱]和2层[破绽] / [持续]：对方所受[虚弱]和[破绽]效果从40%提升至50%  
  *[Qi]+{anima} / Apply 2 [Weakened] and 2 [Flaw] / [Continuous]: The [Weakened] and [Flaw] effects on the opponent are increased from 40% to 50%.*
- **Lv3**: 施加3层[虚弱]和2层[破绽] / [持续]：对方所受[虚弱]和[破绽]效果从40%提升至50%  
  *[Qi]+{anima} / Apply 3 [Weakened] and 2 [Flaw] / [Continuous]: The [Weakened] and [Flaw] effects on the opponent are increased from 40% to 50%.*

#### 拆招 (Counter Move) — id 221
- **Lv1**: [防]+7 / 直到自身下回合开始前： / [拳]：受到的[攻]和[伤害]减50% / [棍]：每次受到攻击后向对方造成6[伤害]  
  *[DEF]+7 / Until the start of your next turn: / [Fist]: Reduce incoming [ATK] and [DMG] by 50% / [Stick]: Deal 6 [DMG] to the opponent each time you are attacked*
- **Lv2**: [防]+12 / 直到自身下回合开始前： / [拳]：受到的[攻]和[伤害]减50% / [棍]：每次受到攻击后向对方造成6[伤害]  
  *[DEF]+12 / Until the start of your next turn: / [Fist]: Reduce incoming [ATK] and [DMG] by 50% / [Stick]: Deal 6 [DMG] to the opponent each time you are attacked*
- **Lv3**: [防]+17 / 直到自身下回合开始前： / [拳]：受到的[攻]和[伤害]减50% / [棍]：每次受到攻击后向对方造成6[伤害]  
  *[DEF]+17 / Until the start of your next turn: / [Fist]: Reduce incoming [ATK] and [DMG] by 50% / [Stick]: Deal 6 [DMG] to the opponent each time you are attacked*

#### 飞云丹 (Cloud Elixir) — id 226
- **Lv1**: [出售]：[通宝]+18 / [炼化]：抽1张牌  
  *[Sell]: [Coin]+18 / [Absorb]: Draw 1 card*

#### 锻体丹 (Bodybuilding Elixir) — id 227
- **Lv1**: [出售]：[通宝]+18 / [炼化]：[体力]+4  
  *[Sell]: [Coin]+18 / [Absorb]: [Energy]+4*

#### 火云符 (Fire Cloud Fulu) — id 236
- **Lv1**: [使用]：耗2[体力]，每次加[通宝]时多加2点  
  *[Use]: Costs 2 [Energy], each time gaining [Coin] when using card in the deck, gain 2 more*

#### 清心咒 (Calm Incantation) — id 237
- **Lv1**: [使用]：[体力]+2，[通宝]+4  
  *[Use]: [Energy]+2, [Coin]+4*

#### 玉露瓶 (Dew Jade Vase) — id 246
- **Lv1**: [耐久]2 / [使用]：[体力]+8  
  *[Durability] 2 / [Use]: [Energy]+8*
- **Lv2**: [耐久]1 / [使用]：[体力]+8  
  *[Durability] 1 / [Use]: [Energy]+8*

#### 无名古剑 (Nameless Ancient Sword) — id 247
- **Lv1**: [耐久]2 / [使用]：[通宝]+9（若使用此牌前[体力]低于3，则再加9[通宝]）  
  *[Durability] 2 / [Use]: [Coin]+9 (If the [Energy] is lower than 3 before using this card, then gain 9 more [Coin])*
- **Lv2**: [耐久]1 / [使用]：[通宝]+9（若使用此牌前[体力]低于3，则再加9[通宝]）  
  *[Durability] 1 / [Use]: [Coin]+9 (If the [Energy] is lower than 3 before using this card, then gain 9 more [Coin])*

#### 暗星蝙蝠 (Dark Star Bat) — id 254
- **Lv1**: 只要在卡组中：所有牌获得[通宝]+1的效果  
  *As long as in the deck: gain 1[Coin] after each [use] or [sell] of any card*

#### 云剑·潜龙 (Cloud Sword - Hidden Loong) — id 331
- **Lv1**: 7攻 / 此牌及下1张使用的牌同时视作云剑和狂剑 / [连云]：改为下2张  
  *7 [ATK] / This card and the next 1 played cards are treated as Cloud Sword and Unrestrained Sword / [Cloud Hit]: Change to the next 2 cards*
- **Lv2**: 11攻 / 此牌及下1张使用的牌同时视作云剑和狂剑 / [连云]：改为下3张  
  *11 [ATK] / This card and the next 1 played cards are treated as Cloud Sword and Unrestrained Sword / [Cloud Hit]: Change to the next 3 cards*
- **Lv3**: 15攻 / 此牌及下1张使用的牌同时视作云剑和狂剑 / [连云]：改为下4张  
  *15 [ATK] / This card and the next 1 played cards are treated as Cloud Sword and Unrestrained Sword / [Cloud Hit]: Change to the next 4 cards*

#### 秣马厉兵 (Feed the Horses, Sharpen the Weapons) — id 354
- **Lv1**: [防]+5 / 随机使用1张不含攻击效果的门派牌  
  *[DEF]+5 / Randomly play 1 Sect Card without Attack Effect*
- **Lv2**: [防]+7 / 随机使用1张不含攻击效果的门派牌  
  *[DEF]+7 / Randomly play 1 Sect Card without Attack Effect*
- **Lv3**: [防]+9 / 随机使用1张不含攻击效果的门派牌  
  *[DEF]+9 / Randomly play 1 Sect Card without Attack Effect*

#### 指鹿为马 (Call a Deer a Horse) — id 355
- **Lv1**: 随机使用2张其他门派的牌  
  *Randomly play 2 cards from other Sects*
- **Lv2**: 随机使用2张其他门派的牌  
  *Randomly play 2 cards from other Sects*
- **Lv3**: 随机使用2张其他门派的牌  
  *Randomly play 2 cards from other Sects*

#### 走马观花 (View Flowers from a Galloping Horse) — id 356
*持续 Continuous*  
- **Lv1**: [持续]：每回合开始时随机一种效果：自身受到7点伤害或者对方受到10点伤害  
  *[Continuous]: At the start of each turn, trigger one random effect: self takes 7 DMG or opponent takes 10 DMG*
- **Lv2**: [持续]：每回合开始时随机一种效果：自身受到8点伤害或者对方受到13点伤害  
  *[Continuous]: At the start of each turn, trigger one random effect: self takes 8 DMG or opponent takes 13 DMG*
- **Lv3**: [持续]：每回合开始时随机一种效果：自身受到9点伤害或者对方受到16点伤害  
  *[Continuous]: At the start of each turn, trigger one random effect: self takes 9 DMG or opponent takes 16 DMG*

#### 灵羽 (Spirit Feather) — id 381
- **Lv1**: 2攻×2 / [灵气]+1 / [体魄]+1 / [身法]+5  
  *2 ATK × 2 / [Qi]+1 / [Physique]+1 / [Agility]+5*
- **Lv2**: 2攻×3 / [灵气]+2 / [体魄]+1 / [身法]+6  
  *2 ATK × 3 / [Qi]+2 / [Physique]+1 / [Agility]+6*
- **Lv3**: 2攻×4 / [灵气]+3 / [体魄]+1 / [身法]+7  
  *2 ATK × 4 / [Qi]+3 / [Physique]+1 / [Agility]+7*


### Phase 3 — 金丹 Virtuoso

#### 七星灯 (Heptastar Lantern) — id 4
- **Lv1**: [炼化]：[命元]变为50  
  *[Absorb]: [Destiny] becomes 50*

#### 灯焰飞舞 (Flame Flutter) — id 6
- **Lv1**: 3攻 / 施加1～3层[内伤]  
  *3 ATK / Apply 1～3 stack(s) of [Internal Injury]*
- **Lv2**: 4攻 / 施加2～4层[内伤]  
  *4 ATK / Apply 2～4 stack(s) of [Internal Injury]*
- **Lv3**: 5攻 / 施加3～5层[内伤]  
  *5 ATK / Apply 3～5 stack(s) of [Internal Injury]*

#### 星爆术 (Starburst) — id 10
- **Lv1**: 8攻 / 若有[星力]，则减1[星力]且此牌多8攻  
  *8 ATK / If you have [Star Power], remove 1 [Star Power] and this card has 8 more ATK*
- **Lv2**: 10攻 / 若有[星力]，则减1[星力]且此牌多10攻  
  *10 ATK / If you have [Star Power], remove 1 [Star Power] and this card has 10 more ATK*
- **Lv3**: 12攻 / 若有[星力]，则减1[星力]且此牌多13攻  
  *12 ATK / If you have [Star Power], remove 1 [Star Power] and this card has 13 more ATK*

#### 悠然葫芦 (Gourd Of Leisurely) — id 13
- **Lv1**: [灵气]+1 / 生命+3 / 若已激活任意[五行]则[再次行动]  
  *[Qi]+1 / HP+3 / If any [Five Elements] has been activated, [Chase]*
- **Lv2**: [灵气]+2 / 生命+5 / 若已激活任意[五行]则[再次行动]  
  *[Qi]+2 / HP+5 / If any [Five Elements] has been activated, [Chase]*
- **Lv3**: [灵气]+3 / 生命+7 / 若已激活任意[五行]则[再次行动]  
  *[Qi]+3 / HP+7 / If any [Five Elements] has been activated, [Chase]*

#### 自在随心 (At Own Pace) — id 27
- **Lv1**: 立刻抽1张牌  
  *Draw 1 Card*

#### 无极卦盘 (Ultimate Hexagram Base) — id 28
*持续 Continuous*  
- **Lv1**: [持续]：自身每回合开始时加1[卦象]  
  *[Continuous]: At the beginning of your turn, add 1 [Hexagram]*
- **Lv2**: [卦象]+2 / [持续]：自身每回合开始时加1[卦象]  
  *[Hexagram]+2 / [Continuous]: At the beginning of your turn, add 1 [Hexagram]*
- **Lv3**: [卦象]+4 / [持续]：自身每回合开始时加1[卦象]  
  *[Hexagram]+4 / [Continuous]: At the beginning of your turn, add 1 [Hexagram]*

#### 锟铻金环 (Kun Wu Metal Ring) — id 38
*持续 Continuous*  
- **Lv1**: [激活土灵] / [激活金灵] / [持续]：每次加[防]或加[锋锐]时多加2点  
  *[Activate Earth Spirit] / [Activate Metal Spirit] / [Continuous]: Whenever you gain [DEF] or [Penetrate], gain 2 additional stacks*
- **Lv2**: [激活土灵] / [激活金灵] / [持续]：每次加[防]或加[锋锐]时多加3点  
  *[Activate Earth Spirit] / [Activate Metal Spirit] / [Continuous]: Whenever you gain [DEF] or [Penetrate], gain 3 additional stacks*
- **Lv3**: [激活土灵] / [激活金灵] / [持续]：每次加[防]或加[锋锐]时多加4点  
  *[Activate Earth Spirit] / [Activate Metal Spirit] / [Continuous]: Whenever you gain [DEF] or [Penetrate], gain 4 additional stacks*

#### 魔气缠身 (Demonic Qi Haunt) — id 39
- **Lv1**: 4攻 / 施加2层[内伤]  
  *4 ATK / Apply 2 stacks of [Internal Injury]*
- **Lv2**: 4攻 / 施加3层[内伤]  
  *4 ATK / Apply 3 stacks of [Internal Injury]*
- **Lv3**: 4攻 / 施加4层[内伤]  
  *4 ATK / Apply 4 stacks of [Internal Injury]*

#### 疯魔 (Gone Crazy) — id 73
- **Lv1**: 获得2层[冥]和2层随机[负面状态] / [体魄]+1（每有1层[负面状态]多1，最多加10）  
  *Gain 2 [Styx] and 2 random [Debuff] / [Physique]+1 (increases by 1 for each stack of [Debuff], up to 10)*
- **Lv2**: 获得3层[冥]和1层随机[负面状态] / [体魄]+1（每有1层[负面状态]多1，最多加15）  
  *Gain 3 [Styx] and 1 random [Debuff] / [Physique]+1 (increases by 1 for each stack of [Debuff], up to 15)*
- **Lv3**: 获得4层[冥] / [体魄]+1（每有1层[负面状态]多1，最多加20）  
  *Gain 4 [Styx] / [Physique]+1 (increases by 1 for each stack of [Debuff], up to 20)*

#### 魔龙之爪 (Magic Dragon's Paw) — id 76
- **Lv1**: 2攻×2 / 每次攻击后施加1层[外伤]  
  *2 ATK×2 / Apply 1 [Wound] for each attack*
- **Lv2**: 2攻×3 / 每次攻击后施加1层[外伤]  
  *2 ATK×3 / Apply 1 [Wound] for each attack*
- **Lv3**: 2攻×4 / 每次攻击后施加1层[外伤]  
  *2 ATK×4 / Apply 1 [Wound] for each attack*

#### 烟花 (Firework) — id 80
- **Lv1**: 获得1层[辟邪] / [再次行动]  
  *Gain 1 [Hexproof] / [Chase]*
- **Lv2**: 获得2层[辟邪] / [再次行动]  
  *Gain 2 [Hexproof] / [Chase]*
- **Lv3**: 获得3层[辟邪] / [再次行动]  
  *Gain 3 [Hexproof] / [Chase]*

#### 碱水粽 (Alkaline Water Zongzi) — id 89
*持续 Continuous*  
- **Lv1**: [甜粽] / 生命+2 / [持续]：每次使用[甜粽]时先加1[灵气]，使用[咸粽]时先加2生命  
  *[Sweet Zongzi] / HP+2 / [Continuous]: Whenever you play a [Sweet Zongzi], add 1 [Qi], and whenever you play a [Salty Zongzi], you add 2 HP*
- **Lv2**: [甜粽] / 生命+6 / [持续]：每次使用[甜粽]时先加1[灵气]，使用[咸粽]时先加2生命  
  *[Sweet Zongzi] / HP+6 / [Continuous]: Whenever you play a [Sweet Zongzi], add 1 [Qi], and whenever you play a [Salty Zongzi], you add 2 HP*
- **Lv3**: [甜粽] / 生命+10 / [持续]：每次使用[甜粽]时先加1[灵气]，使用[咸粽]时先加2生命  
  *[Sweet Zongzi] / HP+10 / [Continuous]: Whenever you play a [Sweet Zongzi], add 1 [Qi], and whenever you play a [Salty Zongzi], you add 2 HP*

#### 莲子粽 (Lotus Seeds Zongzi) — id 90
- **Lv1**: [甜粽] / 生命+4（每有1点灵气或1层[内伤]、[恢复]、[食欲]、[食滞]额外加2生命）  
  *[Sweet Zongzi] / HP+4 (for each Qi or 1 stack of [Internal injury], [Regeneration], [Appetite], [Indigestion] add 2 more HP)*
- **Lv2**: [甜粽] / 生命+8（每有1点灵气或1层[内伤]、[恢复]、[食欲]、[食滞]额外加2生命）  
  *[Sweet Zongzi] / HP+8 (for each Qi or 1 stack of [Internal injury], [Regeneration], [Appetite], [Indigestion] add 2 more HP)*
- **Lv3**: [甜粽] / 生命+8（每有1点灵气或1层[内伤]、[恢复]、[食欲]、[食滞]额外加3生命）  
  *[Sweet Zongzi] / HP+8 (for each Qi or 1 stack of [Internal injury], [Regeneration], [Appetite], [Indigestion] add 3 more HP)*

#### 豆沙粽 (Bean Paste Zongzi) — id 91
- **Lv1**: [甜粽] / 清空自身[内伤]和[食滞] / 生命+7（每清1层多加2生命）  
  *[Sweet Zongzi] / Clear [Internal Injury] and [Indigestion] / HP+7 (add 2 more HP for each stack cleared)*
- **Lv2**: [甜粽] / 清空自身[内伤]和[食滞] / 生命+7（每清1层多加3生命）  
  *[Sweet Zongzi] / Clear [Internal Injury] and [Indigestion] / HP+7 (add 3 more HP for each stack cleared)*
- **Lv3**: [甜粽] / 清空自身[内伤]和[食滞] / 生命+7（每清1层多加4生命）  
  *[Sweet Zongzi] / Clear [Internal Injury] and [Indigestion] / HP+7 (add 4 more HP for each stack cleared)*

#### 酸笋粽 (Sour Bamboo Shoots Zongzi) — id 104
- **Lv1**: [咸粽] / 生命+2 / 获得2层[内伤] / [再次行动]  
  *[Salty Zongzi] / HP+2 / Gain 2 stacks of [Internal Injury] / [Chase]*
- **Lv2**: [咸粽] / 生命+6 / 获得2层[内伤] / [再次行动]  
  *[Salty Zongzi] / HP+6 / Gain 2 stacks of [Internal Injury] / [Chase]*
- **Lv3**: [咸粽] / 生命+10 / 获得2层[内伤] / [再次行动]  
  *[Salty Zongzi] / HP+10 / Gain 2 stacks of [Internal Injury] / [Chase]*

#### 板栗粽 (Chestnut Zongzi) — id 105
- **Lv1**: [咸粽] / 耗1[灵气]：将1层[负面状态]转为[食欲] / 重复3次：生命+3  
  *[Salty Zongzi] / Cost 1 [Qi]: Convert 1 stack of [Debuff] to [Appetite] / Repeat 3 times: HP+3*
- **Lv2**: [咸粽] / 耗1[灵气]：将1层[负面状态]转为[食欲] / 重复3次：生命+4  
  *[Salty Zongzi] / Cost 1 [Qi]: Convert 1 stack of [Debuff] to [Appetite] / Repeat 3 times: HP+4*
- **Lv3**: [咸粽] / 耗1[灵气]：将1层[负面状态]转为[食欲] / 重复3次：生命+5  
  *[Salty Zongzi] / Cost 1 [Qi]: Convert 1 stack of [Debuff] to [Appetite] / Repeat 3 times: HP+5*

#### 香辣粽 (Pungent Zongzi) — id 106
- **Lv1**: [咸粽] / [灵气]+1 / 生命+6 / 获得1层[食欲]和[内伤]  
  *[Salty Zongzi] / [Qi]+1 / HP+6 / Gain 1 stacks of [Appetite] and [Internal Injury]*
- **Lv2**: [咸粽] / [灵气]+1 / 生命+9 / 获得2层[食欲]和[内伤]  
  *[Salty Zongzi] / [Qi]+1 / HP+9 / Gain 2 stacks of [Appetite] and [Internal Injury]*
- **Lv3**: [咸粽] / [灵气]+1 / 生命+12 / 获得3层[食欲]和[内伤]  
  *[Salty Zongzi] / [Qi]+1 / HP+12 / Gain 3 stacks of [Appetite] and [Internal Injury]*

#### 瑞雪迎春 (Traces Revitalized) — id 127
- **Lv1**: 6攻（每加过4生命多1攻） / [灵气]+1 / [后招]：[再次行动]  
  *6 ATK (1 more ATK for each 4 HP have added before) / [Qi]+1 / [Post Action]: [Chase]*
- **Lv2**: 6攻（每加过4生命多1攻） / [灵气]+1 / [再次行动] / [后招]：生命+1  
  *6 ATK (1 more ATK for each 4 HP have added before) / [Qi]+1 / [Chase] / [Post Action]: HP+1*
- **Lv3**: 6攻（每加过3生命多1攻） / [灵气]+1 / [再次行动] / [后招]：生命+3  
  *6 ATK (1 more ATK for each 3 HP have added before) / [Qi]+1 / [Chase] / [Post Action]: HP+3*

#### 锟铻熔火环 (Kun Wu Molten Ring) — id 135
*持续 Continuous*  
- **Lv1**: [激活火灵] / [激活土灵] / [持续]：每次减对方生命上限时多减2点；每次加自身[防]时多加2点  
  *[Activate Fire Spirit] / [Activate Earth Spirit] / [Continuous]: Each time your opponent loses Max HP, they lose an additional 2; each time you gain [DEF], you gain an additional 2*
- **Lv2**: [激活火灵] / [激活土灵] / [持续]：每次减对方生命上限时多减3点；每次加自身[防]时多加3点  
  *[Activate Fire Spirit] / [Activate Earth Spirit] / [Continuous]: Each time your opponent loses Max HP, they lose an additional 3; each time you gain [DEF], you gain an additional 3*
- **Lv3**: [激活火灵] / [激活土灵] / [持续]：每次减对方生命上限时多减4点；每次加自身[防]时多加4点  
  *[Activate Fire Spirit] / [Activate Earth Spirit] / [Continuous]: Each time your opponent loses Max HP, they lose an additional 4; each time you gain [DEF], you gain an additional 4*

#### 玄冥重现 (Xuanming Recurring) — id 162
*消耗 Consumable*  
- **Lv1**: 回复至自身上回合开始时的生命，[跳至]自身上一张牌 / [消耗]  
  *Restore your HP to what it was at the start of your last turn / [Skip To] the card in your previous slot / [Consumption]*
- **Lv2**: 回复至自身上回合开始时的生命+5，[跳至]自身上一张牌 / [消耗]  
  *Restore your HP to what it was at the start of your last turn plus 5 / [Skip To] the card in your previous slot / [Consumption]*
- **Lv3**: 回复至自身上回合开始时的生命+10，[跳至]自身上一张牌 / [消耗]  
  *Restore your HP to what it was at the start of your last turn plus 10 / [Skip To] the card in your previous slot / [Consumption]*

#### 八卦炉 (Hexagram Furnace ) — id 228
- **Lv1**: [使用]：耗4体力，获得2张丹药牌  
  *[Use]: Costs 4 [Energy], gain 2 random elixir card*

#### 还魂丹 (Resurrection Elixir) — id 229
- **Lv1**: [出售]：[通宝]+24 / [炼化]：[体力]上限永久+1，[体力]+3  
  *[Sell]: [Coin]+24 / [Absorb]: [Energy]+3, max [Energy]+1 in this game*

#### 吸灵符 (Spirit Absorb Fulu) — id 238
- **Lv1**: [使用]：回复已损失[体力]的一半  
  *[Use]: Restore half of the lost [Energy]*

#### 寒冰咒 (Ice Incantation) — id 239
- **Lv1**: [使用]：重复3次：[通宝]+4  
  *[Use]: Repeat 3 times: [Coin]+4*

#### 养魂玉莲 (Requiem Jade Lotus) — id 248
- **Lv1**: [耐久]2 / [使用]：[体力]+4，每有1点[体力]加1[通宝]  
  *[Durability] 2 / [Use]: [Energy]+4, gain 1 [Coin] for each 1 [Energy]*
- **Lv2**: [耐久]1 / [使用]：[体力]+4，每有1点[体力]加1[通宝]  
  *[Durability] 1 / [Use]: [Energy]+4, gain 1 [Coin] for each 1 [Energy]*
- **Lv3** ⟨template⟩: [耐久]{otherParams[0]} / [使用]：[体力]+{otherParams[1]}，每有1点[体力]加1[通宝]  
  *[Durability] {otherParams[0]} / [Use]: [Energy]+{otherParams[1]}, gain 1 [Coin] for each 1 [Energy]*

#### 狼皇血晶 (Blood Crystal of Wolf King) — id 249
- **Lv1**: [耐久]2 / [使用]：耗2[体力]，每次加通宝时多加4点 / [炼化]：本轮炼化卡牌额外加4[通宝]  
  *[Durability] 2 / [Use]: Costs 2 [Energy], add 2more [Coin] to all cards in the deck that gain [Coin] / [Absorb]: Until the next round begins, gain 4 [Coin] each time you Absorb a card*
- **Lv2**: [耐久]1 / [使用]：耗2[体力]，每次加通宝时多加4点 / [炼化]：本轮炼化卡牌额外加4[通宝]  
  *[Durability] 1 / [Use]: Costs 2 [Energy], add 1more [Coin] to all cards in the deck that gain [Coin] / [Absorb]: Until the next round begins, gain 4 [Coin] each time you Absorb a card*
- **Lv3** ⟨template⟩: [耐久]{otherParams[0]} / [使用]：耗{otherParams[1]}[体力]，每次加通宝时多加{otherParams[2]}点 / [炼化]：本轮炼化卡牌额外加{otherParams[2]}[通宝]  
  *[Durability] {otherParams[0]} / [Use]: Costs {otherParams[1]} [Energy], add {otherParams[0]}more [Coin] to all cards in the deck that gain [Coin] / [Absorb]: Until the next round begins, gain {otherParams[2]} [Coin] each time you Absorb a card*

#### 锦毛鼠 (Brocade Rat) — id 255
- **Lv1**: 只要在卡组中：本轮结束时抽2张牌  
  *As long as in the deck: draw 2cards at the end of this round*

#### 水灵·悠然 (Water Spirit -  Leisurely) — id 258
- **Lv1**: [灵气]+2 / 生命及上限+3 / 若已激活任意[五行]则[再次行动]  
  *[Qi]+2 / HP and Max HP+3 / If any [Five Elements] has been activated, [Chase]*
- **Lv2**: [灵气]+3 / 生命及上限+6 / 若已激活任意[五行]则[再次行动]  
  *[Qi]+3 / HP and Max HP+6 / If any [Five Elements] has been activated, [Chase]*
- **Lv3**: [灵气]+4 / 生命及上限+9 / 若已激活任意[五行]则[再次行动]  
  *[Qi]+4 / HP and Max HP+9 / If any [Five Elements] has been activated, [Chase]*

#### 天降甘霖 (Heavenly Rain) — id 259
- **Lv1**: [炼化]：场上命元＜90的所有角色加5命元，然后自身额外再加20命元  
  *[Absorb]: All players with Destiny＜90 gain 5 Destiny. You gain additional 20 Destiny.*

#### 策马扬鞭 (Whip the Horse, Raise the Whip) — id 357
- **Lv1**: 下2次随机使用的卡牌至少为自身上一个境界  
  *For the next 2 random cards plays, they will be at least one Phase before your current one*
- **Lv2**: 下3次随机使用的卡牌至少为自身上一个境界  
  *For the next 3 random cards plays, they will be at least one Phase before your current one*
- **Lv3**: 下5次随机使用的卡牌至少为自身上一个境界  
  *For the next 5 random cards plays, they will be at least one Phase before your current one*

#### 野马分粽 (Wild Horses Part the Zongzi) — id 358
- **Lv1**: 随机使用2张粽子牌  
  *Randomly play 2 Zongzi cards*
- **Lv2**: 随机使用2张粽子牌  
  *Randomly play 2 Zongzi cards*
- **Lv3**: 随机使用2张粽子牌  
  *Randomly play 2 Zongzi cards*

#### 害群之马 (A Horse That Harms the Herd) — id 366
- **Lv1**: [炼化]：场上随机一名角色减5[命元]（最低减至1），自身随机加3[命元]或减3[命元]（最低减至1）  
  *[Absorb]: Randomly reduce 5 [Destiny] from a player in the game (minimum to 1), and randomly increase or decrease your [Destiny] by 3 (minimum to 1)*

#### 定风波 (Settle the Storm) — id 371
- **Lv1**: 3攻×2（每[激活]过1次[五行]，再多攻击1次）  
  *3 [ATK] × 2 (Attack 1 more time for each time [Five Elements] has been [Activated])*
- **Lv2**: 4攻×2（每[激活]过1次[五行]，再多攻击1次）  
  *4 [ATK] × 2 (Attack 1 more time for each time [Five Elements] has been [Activated])*
- **Lv3**: 5攻×2（每[激活]过1次[五行]，再多攻击1次）  
  *5 [ATK] × 2 (Attack 1 more time for each time [Five Elements] has been [Activated])*

#### 气旋掌 (Cyclone Palm) — id 382
- **Lv1**: 每有15[体魄]加1[灵气] / 2攻×2（每有1[灵气]多1攻）  
  *Gain 1 [Qi] for each 15 [Physique] / 2 ATK × 2 (1 more ATK for each [Qi])*
- **Lv2**: 每有15[体魄]加1[灵气] / 4攻×2（每有1[灵气]多1攻）  
  *Gain 1 [Qi] for each 15 [Physique] / 4 ATK × 2 (1 more ATK for each [Qi])*
- **Lv3**: 每有15[体魄]加1[灵气] / 6攻×2（每有1[灵气]多1攻）  
  *Gain 1 [Qi] for each 15 [Physique] / 6 ATK × 2 (1 more ATK for each [Qi])*


### Phase 4 — 元婴 Immortality

#### 云剑·崩雪 (Cloud Sword - Avalanche) — id 3
- **Lv1**: 4攻 / [连云]：每连续用过1张“云剑”多4攻  
  *4 ATK / [Cloud Hit]: For each consecutive Cloud Sword played, add 4 more ATK*
- **Lv2**: 4攻 / [连云]：每连续用过1张“云剑”多5攻  
  *4 ATK / [Cloud Hit]: For each consecutive Cloud Sword played, add 5 more ATK*
- **Lv3**: 4攻 / [连云]：每连续用过1张“云剑”多6攻  
  *4 ATK / [Cloud Hit]: For each consecutive Cloud Sword played, add 6 more ATK*

#### 瓮中捉鳖 (Within Reach) — id 5
- **Lv1**: 9攻 / 对方每有1层[负面状态]，此牌多2攻  
  *9 ATK / For each stack of [Debuff] the opponent has, this card gets 2 more ATK*
- **Lv2**: 9攻 / 对方每有1层[负面状态]，此牌多3攻  
  *9 ATK / For each stack of [Debuff] the opponent has, this card gets 3 more ATK*
- **Lv3**: 9攻 / 对方每有1层[负面状态]，此牌多4攻  
  *9 ATK / For each stack of [Debuff] the opponent has, this card gets 4 more ATK*

#### 旋灯占卦 (Rotary Divination Hexagram) — id 7
- **Lv1**: [卦象]+4 / 对方生命减2 / 对方灵气减1  
  *[Hexagram]+4 / Opponent lose 2 HP / Opponent lose 1 Qi*
- **Lv2**: [卦象]+5 / 对方生命减3 / 对方灵气减2  
  *[Hexagram]+5 / Opponent lose 3 HP / Opponent lose 2 Qi*
- **Lv3**: [卦象]+6 / 对方生命减4 / 对方灵气减3  
  *[Hexagram]+6 / Opponent lose 4 HP / Opponent lose 3 Qi*

#### 灵猫乱剑 (Spirit Cat Chaos Sword) — id 9
- **Lv1**: 2攻×2 / 每保留1张手牌追加1次攻击（最多追加3次）  
  *2 ATK × 2 / Make an additional attack for every remaining hand card (up to 3)*
- **Lv2**: 1攻×3 / 每保留1张手牌追加1次攻击（最多追加3次）  
  *1 ATK × 3 / Make an additional attack for every remaining hand card (up to 3)*
- **Lv3**: 1攻×4 / 每保留1张手牌追加1次攻击（最多追加3次）  
  *1 ATK × 4 / Make an additional attack for every remaining hand card (up to 3)*

#### 七星定魂 (Heptastar Soulstat) — id 11
- **Lv1**: 对方减4生命 / 令对方无法行动1回合  
  *Opponent loses 4 HP / Make the opponent unable to act for 1 turn*
- **Lv2**: 对方减9生命 / 令对方无法行动1回合  
  *Opponent loses 9 HP / Make the opponent unable to act for 1 turn*
- **Lv3**: 对方减14生命 / 令对方无法行动1回合  
  *Opponent loses 14 HP / Make the opponent unable to act for 1 turn*

#### 云剑·唤雨 (Cloud Sword - Pray Rain) — id 15
- **Lv1**: 2攻×3 / [灵气]+1 / 获得2层[恢复] / [连云]：将最多2层[恢复]转为[加攻]  
  *2 ATK × 3 / [Qi]+1 / Gain 2 [Regeneration] / [Cloud Hit]: Convert up to 2 [Regeneration] to [Increase ATK]*
- **Lv2**: 2攻×4 / [灵气]+1 / 获得2层[恢复] / [连云]：将最多3层[恢复]转为[加攻]  
  *2 ATK × 4 / [Qi]+1 / Gain 2 [Regeneration] / [Cloud Hit]: Convert up to 3 [Regeneration] to [Increase ATK]*
- **Lv3**: 2攻×5 / [灵气]+1 / 获得2层[恢复] / [连云]：将最多4层[恢复]转为[加攻]  
  *2 ATK × 5 / [Qi]+1 / Gain 2 [Regeneration] / [Cloud Hit]: Convert up to 4 [Regeneration] to [Increase ATK]*

#### 水灵·春雨 (Water Spirit - Spring Rain) — id 17
*持续 Continuous*  
- **Lv1**: 生命及上限+4 / [持续]：自身每回合开始时加1层[水势]  
  *HP and Max HP+4 / [Continuous]: At the beginning of your turn, gain 1 stack of [Force of Water]*
- **Lv2**: 生命及上限+10 / [持续]：自身每回合开始时加1层[水势]  
  *HP and Max HP+10 / [Continuous]: At the beginning of your turn, gain 1 stack of [Force of Water]*
- **Lv3**: 生命及上限+16 / [持续]：自身每回合开始时加1层[水势]  
  *HP and Max HP+16 / [Continuous]: At the beginning of your turn, gain 1 stack of [Force of Water]*

#### 金灵·刚劲 (Metal Spirit - Vigorous) — id 18
- **Lv1**: 5攻 / [金灵]：每有1层[锋锐]多1攻，但不触发[锋锐]  
  *5 ATK / [Metal Spirit]: For every stack of [Penetrate] this card add 1 ATK, but will not trigger the effect of [Penetrate]*
- **Lv2**: 10攻 / [金灵]：每有1层[锋锐]多1攻，但不触发[锋锐]  
  *10 ATK / [Metal Spirit]: For every stack of [Penetrate] this card add 1 ATK, but will not trigger the effect of [Penetrate]*
- **Lv3**: 15攻 / [金灵]：每有1层[锋锐]多1攻，但不触发[锋锐]  
  *15 ATK / [Metal Spirit]: For every stack of [Penetrate] this card add 1 ATK, but will not trigger the effect of [Penetrate]*

#### 双鸳逆克 (Overcome with each other) — id 32
- **Lv1**: [灵气]+1 / [防]+3 / 若前一格的牌[五行克制]后一格，则[激活]后一格的[五行]并[再次行动]  
  *[Qi]+1 / [DEF]+3 / If the card in the previous slot has [Overcoming Interaction of Five Elements] with the next slot, [Activate] the [Five Elements] of the next slot and [Chase]*
- **Lv2**: [灵气]+2 / [防]+5 / 若前一格的牌[五行克制]后一格，则[激活]后一格的[五行]并[再次行动]  
  *[Qi]+2 / [DEF]+5 / If the card in the previous slot has [Overcoming Interaction of Five Elements] with the next slot, [Activate] the [Five Elements] of the next slot and [Chase]*
- **Lv3**: [灵气]+3 / [防]+7 / 若前一格的牌[五行克制]后一格，则[激活]后一格的[五行]并[再次行动]  
  *[Qi]+3 / [DEF]+7 / If the card in the previous slot has [Overcoming Interaction of Five Elements] with the next slot, [Activate] the [Five Elements] of the next slot and [Chase]*

#### 守株待兔 (Waiting for Rabbit) — id 42
*消耗 Consumable*  
- **Lv1**: [防]+15 / 50%概率会有一只兔子在此处撞晕（此牌永久变为【影枭兔】，但本轮战斗不生效） / [消耗]  
  *[DEF]+15 / 50% chance to change this card to [Shadow Owl Rabbit] permanently (but not valid in this battle) / [Consumption]*
- **Lv2**: [防]+20 / 75%概率会有一只兔子在此处撞晕（此牌永久变为【影枭兔】，但本轮战斗不生效） / [消耗]  
  *[DEF]+20 / 75% chance to change this card to [Shadow Owl Rabbit] permanently (but not valid in this battle) / [Consumption]*
- **Lv3**: [防]+25 / 100%概率会有一只兔子在此处撞晕（此牌永久变为【影枭兔】，但本轮战斗不生效） / [消耗]  
  *[DEF]+25 / 100% chance to change this card to [Shadow Owl Rabbit] permanently (but not valid in this battle) / [Consumption]*

#### 崩拳·冥夜 (Crash Fist - Styx Night) — id 74
*持续 Continuous*  
- **Lv1**: 获得3层[冥] / [持续]：使用“崩拳”攻击时，自身每有1层[负面状态]多1攻（最多加6)  
  *Gain 3 [Styx] / [Continuous]: When attacking with "Crash Fist", it increases 1 ATK for each stack of [Debuff] you have (up to 6).*
- **Lv2**: 获得4层[冥] / [持续]：使用“崩拳”攻击时，自身每有1层[负面状态]多1攻（最多加9)  
  *Gain 4 [Styx] / [Continuous]: When attacking with "Crash Fist", it increases 1 ATK for each stack of [Debuff] you have (up to 9).*
- **Lv3**: 获得5层[冥] / [持续]：使用“崩拳”攻击时，自身每有1层[负面状态]多1攻（最多加12)  
  *Gain 5 [Styx] / [Continuous]: When attacking with "Crash Fist", it increases 1 ATK for each stack of [Debuff] you have (up to 12).*

#### 冥心入玄 (Meditation of Xuan) — id 81
*持续 Continuous*  
- **Lv1**: [体魄]+2 / [持续]：自身每回合开始时获得2层[内伤]和[恢复]  
  *[Physique]+2 / [Continuous]: At the start of each your turn, you gain 2 [Internal Injury] and 2 [Regeneration]*
- **Lv2**: [体魄]+3 / [持续]：自身每回合开始时获得3层[内伤]和[恢复]  
  *[Physique]+3 / [Continuous]: At the start of each your turn, you gain 3 [Internal Injury] and 3 [Regeneration]*
- **Lv3**: [体魄]+4 / [持续]：自身每回合开始时获得4层[内伤]和[恢复]  
  *[Physique]+4 / [Continuous]: At the start of each your turn, you gain 4 [Internal Injury] and 4 [Regeneration]*

#### 蜜饯果粽 (Preserved Fruit Zongzi) — id 92
- **Lv1**: [甜粽] / 生命+2 / 每用过1张[甜粽]再加2生命和1[灵气]  
  *[Sweet Zongzi] / HP+2 / For each [Sweet Zongzi] used before, add 2 more HP and 1 [Qi]*
- **Lv2**: [甜粽] / 生命+3 / 每用过1张[甜粽]再加3生命和1[灵气]  
  *[Sweet Zongzi] / HP+3 / For each [Sweet Zongzi] used before, add 3 more HP and 1 [Qi]*
- **Lv3**: [甜粽] / 生命+4 / 每用过1张[甜粽]再加3生命和2[灵气]  
  *[Sweet Zongzi] / HP+4 / For each [Sweet Zongzi] used before, add 3 more HP and 2 [Qi]*

#### 水晶冰粽 (Crystal Ice Zongzi) — id 93
- **Lv1**: [甜粽] / [灵气]+2 / 获得1层[食滞] / [再次行动]  
  *[Sweet Zongzi] / [Qi]+2 / Gain 1 stack of [Indigestion] / [Chase]*
- **Lv2**: [甜粽] / [灵气]+4 / 获得2层[食滞] / [再次行动]  
  *[Sweet Zongzi] / [Qi]+4 / Gain 2 stacks of [Indigestion] / [Chase]*
- **Lv3**: [甜粽] / [灵气]+6 / 获得3层[食滞] / [再次行动]  
  *[Sweet Zongzi] / [Qi]+6 / Gain 3 stacks of [Indigestion] / [Chase]*

#### 鲜果宝粽 (Fresh Fruit Zongzi) — id 94
- **Lv1**: [甜粽] / 生命+8 / 下1次获得[内伤]或[食滞]时转为等量[恢复]  
  *[Sweet Zongzi] / HP+8 / Next 1 time you get [Internal injury] or [Indigestion], convert it to an equal amount of [Regeneration]*
- **Lv2**: [甜粽] / 生命+11 / 下2次获得[内伤]或[食滞]时转为等量[恢复]  
  *[Sweet Zongzi] / HP+11 / Next 2 times you get [Internal injury] or [Indigestion], convert it to an equal amount of [Regeneration]*
- **Lv3**: [甜粽] / 生命+14 / 下3次获得[内伤]或[食滞]时转为等量[恢复]  
  *[Sweet Zongzi] / HP+14 / Next 3 times you get [Internal injury] or [Indigestion], convert it to an equal amount of [Regeneration]*

#### 咸蛋黄粽 (Salted Egg Yolk Zongzi) — id 107
- **Lv1**: [咸粽] / 生命+6 / [升级]下2次使用的牌，无法升级时加2[食欲]  
  *[Salty Zongzi] / HP+6 / [Upgrade] next 2 cards before playing them, or gain 2 [Appetite] if unable to upgrade*
- **Lv2**: [咸粽] / 生命+8 / [升级]下3次使用的牌，无法升级时加2[食欲]  
  *[Salty Zongzi] / HP+8 / [Upgrade] next 3 cards before playing them, or gain 2 [Appetite] if unable to upgrade*
- **Lv3**: [咸粽] / 生命+10 / [升级]下4次使用的牌，无法升级时加2[食欲]  
  *[Salty Zongzi] / HP+10 / [Upgrade] next 4 cards before playing them, or gain 2 [Appetite] if unable to upgrade*

#### 海鲜肉粽 (Seafood Zongzi) — id 108
- **Lv1**: [咸粽] / 每有1层[内伤]、[食滞]、[食欲]或[恢复]，此牌少耗1[灵气] / 重复4次：生命+5  
  *[Salty Zongzi] / For each stack of [Internal Injury], [Indigestion], [Appetite], or [Regeneration], this card costs 1 less [Qi] / Repeat 4 times: HP+5*
- **Lv2**: [咸粽] / 每有1层[内伤]、[食滞]、[食欲]或[恢复]，此牌少耗1[灵气] / 重复4次：生命+6  
  *[Salty Zongzi] / For each stack of [Internal Injury], [Indigestion], [Appetite], or [Regeneration], this card costs 1 less [Qi] / Repeat 4 times: HP+6*
- **Lv3**: [咸粽] / 每有1层[内伤]、[食滞]、[食欲]或[恢复]，此牌少耗1[灵气] / 重复5次：生命+6  
  *[Salty Zongzi] / For each stack of [Internal Injury], [Indigestion], [Appetite], or [Regeneration], this card costs 1 less [Qi] / Repeat 5 times: HP+6*

#### 梅菜肉粽 (Pickled Mustard Zongzi) — id 109
- **Lv1**: [咸粽] / 生命+2 / 获得2层[食欲] / 跳过自身下1张牌  
  *[Salty Zongzi] / HP+2 / Gain 2 stacks of [Appetite] / Skip your next 1 card*
- **Lv2**: [咸粽] / 生命+3 / 获得3层[食欲] / 跳过自身下2张牌  
  *[Salty Zongzi] / HP+3 / Gain 3 stacks of [Appetite] / Skip your next 2 cards*
- **Lv3**: [咸粽] / 生命+4 / 获得4层[食欲] / 跳过自身下3张牌  
  *[Salty Zongzi] / HP+4 / Gain 4 stacks of [Appetite] / Skip your next 3 cards*

#### 狂剑·猫爪 (Unrestrained Sword - Cat Claw) — id 125
- **Lv1**: 5攻×2 / [无视防御] / 每用过1次“狂剑”追加1次攻击 / （使用此牌算作2次“狂剑”）  
  *5 ATK × 2 / [Ignore DEF] / For each "Unrestrained Sword" you played in this battle, make an additional attack / (This card count as 2 "Unrestrained Sword")*
- **Lv2**: 7攻×2 / [无视防御] / 每用过1次“狂剑”追加1次攻击 / （使用此牌算作2次“狂剑”）  
  *7 ATK × 2 / [Ignore DEF] / For each "Unrestrained Sword" you played in this battle, make an additional attack / (This card count as 2 "Unrestrained Sword")*
- **Lv3**: 9攻×2 / [无视防御] / 每用过1次“狂剑”追加1次攻击 / （使用此牌算作2次“狂剑”）  
  *9 ATK × 2 / [Ignore DEF] / For each "Unrestrained Sword" you played in this battle, make an additional attack / (This card count as 2 "Unrestrained Sword")*

#### 灯影蚀焰 (Suspicious Flame Flutter) — id 129
- **Lv1**: 施加4层[内伤] / 重复3次：30%概率令对方的[内伤]立刻生效一次  
  *Apply 4 [Internal Injury] / Repeat 3 times: 30% chance to make the opponent's [Internal Injury] take effect immediately*
- **Lv2**: 施加5层[内伤] / 重复3次：30%概率令对方的[内伤]立刻生效一次  
  *Apply 5 [Internal Injury] / Repeat 3 times: 30% chance to make the opponent's [Internal Injury] take effect immediately*
- **Lv3**: 施加6层[内伤] / 重复3次：30%概率令对方的[内伤]立刻生效一次  
  *Apply 6 [Internal Injury] / Repeat 3 times: 30% chance to make the opponent's [Internal Injury] take effect immediately*

#### 千星天爆 (Thousand Star Explosion) — id 130
- **Lv1**: 6攻（每有1点[星力]多4攻） / 自身[星力]减半  
  *6 ATK (4 more ATK for each [Star Power]) / Halve your [Star Power]*
- **Lv2**: 6攻（每有1点[星力]多5攻） / 自身[星力]减半  
  *6 ATK (5 more ATK for each [Star Power]) / Halve your [Star Power]*
- **Lv3**: 6攻（每有1点[星力]多6攻） / 自身[星力]减半  
  *6 ATK (6 more ATK for each [Star Power]) / Halve your [Star Power]*

#### 水火交融 (Harmony of Water and Fire) — id 136
- **Lv1**: 获得1层[水势] / [激活水灵] / [激活火灵] / [再次行动]  
  *Gain 1 [Force of Water] / [Activate Water Spirit] / [Activate Fire Spirit] / [Chase]*
- **Lv2**: 获得2层[水势] / [激活水灵] / [激活火灵] / [再次行动]  
  *Gain 2 [Force of Water] / [Activate Water Spirit] / [Activate Fire Spirit] / [Chase]*
- **Lv3**: 获得3层[水势] / [激活水灵] / [激活火灵] / [再次行动]  
  *Gain 3 [Force of Water] / [Activate Water Spirit] / [Activate Fire Spirit] / [Chase]*

#### 冥夜迷踪步 (Styx Night Footwork) — id 139
*持续 Continuous*  
- **Lv1**: [冥]+2 / [身法]+2 / [持续]：每回合首次失去生命时加1[身法]和1[灵气]  
  *[Styx]+2 / [Agility]+2 / [Continuous]: Add 1 [Qi] and 1 [Agility] for the first HP lost in each turn*
- **Lv2**: [冥]+3 / [身法]+3 / [持续]：每回合首次失去生命时加1[身法]和1[灵气]  
  *[Styx]+3 / [Agility]+3 / [Continuous]: Add 1 [Qi] and 1 [Agility] for the first HP lost in each turn*
- **Lv3**: [冥]+4 / [身法]+4 / [持续]：每回合首次失去生命时加1[身法]和1[灵气]  
  *[Styx]+4 / [Agility]+4 / [Continuous]: Add 1 [Qi] and 1 [Agility] for the first HP lost in each turn*

#### 崩拳·返玄 (Crash Fist - Return to Xuan) — id 140
*持续 Continuous*  
- **Lv1**: 生命+12 / 获得4层[内伤]和[恢复] / [持续]：使用崩拳时加回所耗生命  
  *HP+12 / Gain 4 [Internal Injury] and [Regeneration] / [Continuous]：When Crash Fist costs HP, add it back*
- **Lv2**: 生命+16 / 获得6层[内伤]和[恢复] / [持续]：使用崩拳时加回所耗生命  
  *HP+16 / Gain 6 [Internal Injury] and [Regeneration] / [Continuous]：When Crash Fist costs HP, add it back*
- **Lv3**: 生命+20 / 获得8层[内伤]和[恢复] / [持续]：使用崩拳时加回所耗生命  
  *HP+20 / Gain 8 [Internal Injury] and [Regeneration] / [Continuous]：When Crash Fist costs HP, add it back*

#### 玄冥大还丹 (Xuanming Recover Elixir) — id 156
*消耗 Consumable*  
- **Lv1**: 生命及上限+20 / 自身每失去过4生命就再加1生命及上限 / [消耗]  
  *HP and Max HP + 20 / For every 4 HP lost in this battle, add 1 HP and Max HP / [Consumption]*
- **Lv2**: 生命及上限+25 / 自身每失去过4生命就再加1生命及上限 / [消耗]  
  *HP and Max HP + 25 / For every 4 HP lost in this battle, add 1 HP and Max HP / [Consumption]*
- **Lv3**: 生命及上限+30 / 自身每失去过4生命就再加1生命及上限 / [消耗]  
  *HP and Max HP + 30 / For every 4 HP lost in this battle, add 1 HP and Max HP / [Consumption]*

#### 玄冥回春曲 (Xuanming Regen Tune) — id 158
*持续 Continuous*  
- **Lv1**: [持续]：双方在各自回合结束时加11生命及上限，然后减6生命  
  *[Continuous]: Both players gain 11 HP and Max HP then lose 6 HP at the end of their turn*
- **Lv2**: [持续]：双方在各自回合结束时加14生命及上限，然后减7生命  
  *[Continuous]: Both players gain 14 HP and Max HP then lose 7 HP at the end of their turn*
- **Lv3**: [持续]：双方在各自回合结束时加17生命及上限，然后减8生命  
  *[Continuous]: Both players gain 17 HP and Max HP then lose 8 HP at the end of their turn*

#### 玄冥云烟 (Xuanming Clouds) — id 159
- **Lv1**: 重复2次，每次随机1种效果： / 吸取对方6生命，或施加2层[虚弱]，或获得1层[护体]  
  *Repeat 2 times, each time randomly choosing one of the following effects: / Drain 6 HP from the opponent, apply 2 [Weakened], or gain 1 [Guard Up].*
- **Lv2**: 重复3次，每次随机1种效果： / 吸取对方6生命，或施加2层[虚弱]，或获得1层[护体]  
  *Repeat 3 times, each time randomly choosing one of the following effects: / Drain 6 HP from the opponent, apply 2 [Weakened], or gain 1 [Guard Up].*
- **Lv3**: 重复4次，每次随机1种效果： / 吸取对方6生命，或施加2层[虚弱]，或获得1层[护体]  
  *Repeat 4 times, each time randomly choosing one of the following effects: / Drain 6 HP from the opponent, apply 2 [Weakened], or gain 1 [Guard Up].*

#### 玄冥聚力阵 (Xuanming Forceage Formation) — id 160
*持续 Continuous*  
- **Lv1**: 获得3层[加攻] / [持续]2[次]：自身失去生命时获得1层[加攻]  
  *Gain 3 [Increase ATK] / [Continuous] 2 [Times]: Gain 1 [Increase ATK] when you lose HP*
- **Lv2**: 获得3层[加攻] / [持续]3[次]：自身失去生命时获得1层[加攻]  
  *Gain 3 [Increase ATK] / [Continuous] 3 [Times]: Gain 1 [Increase ATK] when you lose HP*
- **Lv3**: 获得3层[加攻] / [持续]4[次]：自身失去生命时获得1层[加攻]  
  *Gain 3 [Increase ATK] / [Continuous] 4 [Times]: Gain 1 [Increase ATK] when you lose HP*

#### 玄冥雪莲 (Xuanming Snowdrop) — id 161
- **Lv1**: 生命+9 / [防]+12 / 自身每失去过3生命下回合加1[防]  
  *HP+9 / [DEF]+12 / For every 3 HP lost in this battle, add 1 [DEF] in your next turn*
- **Lv2**: 生命+9 / [防]+17 / 自身每失去过3生命下回合加1[防]  
  *HP+9 / [DEF]+17 / For every 3 HP lost in this battle, add 1 [DEF] in your next turn*
- **Lv3**: 生命+9 / [防]+22 / 自身每失去过3生命下回合加1[防]  
  *HP+9 / [DEF]+22 / For every 3 HP lost in this battle, add 1 [DEF] in your next turn*

#### 转势 (Shift Stance) — id 222
- **Lv1**: [身法]+8 / [拳]：多加4[身法] / [棍]：8攻 / 使用后[切换架势]  
  *[Agility]+8 / [Fist]: Gain an additional 4 [Agility] / [Stick]: 8 ATK / [Switch Stance]*
- **Lv2**: [身法]+8 / [拳]：多加6[身法] / [棍]：12攻 / 使用后[切换架势]  
  *[Agility]+8 / [Fist]: Gain an additional 6 [Agility] / [Stick]: 12 ATK / [Switch Stance]*
- **Lv3**: [身法]+8 / [拳]：多加8[身法] / [棍]：16攻 / 使用后[切换架势]  
  *[Agility]+8 / [Fist]: Gain an additional 8 [Agility] / [Stick]: 16 ATK / [Switch Stance]*

#### 洗髓丹 (Talent Elixir) — id 230
- **Lv1**: [出售]：[通宝]+30 / [炼化]：抽2张牌  
  *[Sell]: [Coin]+30 / [Absorb]: Draw 2 cards*

#### 大还丹 (Great Recover Elixir) — id 231
- **Lv1**: [出售]：[通宝]+30 / [炼化]：额外加8[通宝]（每有1[体力]多1）  
  *[Sell]: [Coin]+30 / [Absorb]: Add 8 Extra [Coin] (For each [Energy] gain 1 [Coin] more)*

#### 弱体符 (Weaken Fulu) — id 240
- **Lv1**: [使用]：当前每损失1点[体力]+2[通宝]  
  *[Use]: For every 1 [Energy] lost, add 2 [currency]*

#### 聚气咒 (Spiritage Incantation) — id 241
- **Lv1**: [使用]：[通宝]+3（本局每用过一次此牌及同名牌永久多加3）  
  *[Use]: [Coin]+3 (For each time this card or the same named card is used in this game, gain 3 more)*

#### 逍遥古琴 (Carefree Guqin) — id 250
- **Lv1**: [耐久]2 / [使用]：每次休息时回满[体力]时并加10[通宝]  
  *[Durability] 2 / [Use]: gain 10 [Coin] and fully restore [Energy] when you Rest*
- **Lv2**: [耐久]1 / [使用]：每次休息时回满[体力]时并加10[通宝]  
  *[Durability] 1 / [Use]: gain 10 [Coin] and fully restore [Energy] when you Rest*
- **Lv3** ⟨template⟩: [耐久]{otherParams[0]} / [使用]：每次休息时回满[体力]时并加{otherParams[1]}[通宝]  
  *[Durability] {otherParams[0]} / [Use]: gain {otherParams[1]} [Coin] and fully restore [Energy] when you Rest*

#### 混元封神珠 (Cosmos Seal Divine Orb) — id 251
- **Lv1**: [耐久]4 / [使用]：[通宝]+15（此牌损失1点耐久度后基础通宝翻倍）  
  *[Durability] 4 / [Use]: [Coin]+15(After losing 1 [Durability], the base [Coin] will be doubled.)*
- **Lv2**: [耐久]3 / [使用]：[通宝]+30（此牌损失1点耐久度后基础通宝翻倍）  
  *[Durability] 3 / [Use]: [Coin]+30(After losing 1 [Durability], the base [Coin] will be doubled.)*
- **Lv3**: [耐久]1 / [使用]：[通宝]+120（此牌损失1点耐久度后基础通宝翻倍）  
  *[Durability] 1 / [Use]: [Coin]+120(After losing 1 [Durability], the base [Coin] will be doubled.)*

#### 三尾讙 (Three Tailed Cat) — id 256
- **Lv1**: 只要在卡组中：本轮结束时每有5[通宝]就加1[通宝]（最多200）  
  *As long as in the deck: gain 1 [Coin] for every 5[Coin] at the end of this round (Up to 200)*

#### 粽叶 (Zongzi Leaves) — id 300
- **Lv1**: [炼化]：下场战斗开始时自身加10生命  
  *[Absorb]: At the beginning of the next battle, add 10 HP*
- **Lv2**: [炼化]：下场战斗开始时自身加20生命  
  *[Absorb]: At the beginning of the next battle, add 20 HP*
- **Lv3**: [炼化]：下场战斗开始时自身加40生命  
  *[Absorb]: At the beginning of the next battle, add 40 HP*

#### 桂花香粽 (Osmanthus Zongzi) — id 303
- **Lv1**: [甜粽] / [灵气]+2 / [生命]+2 / 每有3点灵气就获得1层[恢复]  
  *[Sweet Zongzi] / [Qi]+2 / HP+2 / Add 1 stack of [Regeneration] for every 3 [Qi]*
- **Lv2**: [甜粽] / [灵气]+3 / [生命]+4 / 每有3点灵气就获得1层[恢复]  
  *[Sweet Zongzi] / [Qi]+3 / HP+4 / Add 1 stack of [Regeneration] for every 3 [Qi]*
- **Lv3**: [甜粽] / [灵气]+3 / [生命]+4 / 每有2点灵气就获得1层[恢复]  
  *[Sweet Zongzi] / [Qi]+3 / HP+4 / Add 1 stack of [Regeneration] for every 2 [Qi]*

#### 火腿肉粽 (Ham Zongzi) — id 306
*持续 Continuous*  
- **Lv1**: [咸粽] / 生命+5 / [持续]：每加1[灵气]或1层[负面状态]时加2[生命]  
  *[Salty Zongzi] / HP+5 / [Continuous]: Whenever you gain 1 Qi or 1 stack of [Debuff], add 2 HP*
- **Lv2**: [咸粽] / 生命+10 / [持续]：每加1[灵气]或1层[负面状态]时加2[生命]  
  *[Salty Zongzi] / HP+10 / [Continuous]: Whenever you gain 1 Qi or 1 stack of [Debuff], add 2 HP*
- **Lv3**: [咸粽] / 生命+15 / [持续]：每加1[灵气]或1层[负面状态]时加2[生命]  
  *[Salty Zongzi] / HP+15 / [Continuous]: Whenever you gain 1 Qi or 1 stack of [Debuff], add 2 HP*

#### 玲珑剑阵 (Exquisite Sword Formation) — id 332
- **Lv1**: [灵气]+2 / 每有1[灵气]向对方造成2[伤害] / 每有1[灵气]下回合开始时加1[防]  
  *[Qi] + 2 / Deal 2 [DMG] to the opponent for each 1 [Qi] you have / Gain 1 [DEF] at the start of your next turn for each 1 [Qi] you have*
- **Lv2**: [灵气]+3 / 每有1[灵气]向对方造成2[伤害] / 每有1[灵气]下回合开始时加1[防]  
  *[Qi] + 3 / Deal 2 [DMG] to the opponent for each 1 [Qi] you have / Gain 1 [DEF] at the start of your next turn for each 1 [Qi] you have*
- **Lv3**: [灵气]+4 / 每有1[灵气]向对方造成2[伤害] / 每有1[灵气]下回合开始时加1[防]  
  *[Qi] + 4 / Deal 2 [DMG] to the opponent for each 1 [Qi] you have / Gain 1 [DEF] at the start of your next turn for each 1 [Qi] you have*

#### 一马当先 (A Horse at the Head) — id 359
- **Lv1**: [身法]+5 / 随机使用1张任意门派或副职业与“再次行动”或“身法”有关的牌  
  *[Agility]+5 / Randomly play 1 card from any Sect or Side Job related to "Chase" or "Agility"*
- **Lv2**: [身法]+10 / 随机使用1张任意门派或副职业与“再次行动”或“身法”有关的牌  
  *[Agility]+10 / Randomly play 1 card from any Sect or Side Job related to "Chase" or "Agility"*
- **Lv3**: [身法]+15 / 随机使用1张任意门派或副职业与“再次行动”或“身法”有关的牌  
  *[Agility]+15 / Randomly play 1 card from any Sect or Side Job related to "Chase" or "Agility"*

#### 蛛丝马迹 (Spider’s Thread, Horse’s Track) — id 360
- **Lv1**: 随机使用1张名字含“马”的牌 / 随机出[野马分鬃]或[探马掌]时：令对方生命变为10  
  *Randomly play 1 card with "Horse" in its name. / If [Wild Horses Part the Mane] or [Detect-Horse Palms] is played: Set opponent's HP to 10*
- **Lv2**: 随机使用1张名字含“马”的牌 / 随机出[野马分鬃]或[探马掌]时：令对方生命变为5  
  *Randomly play 1 card with "Horse" in its name. / If [Wild Horses Part the Mane] or [Detect-Horse Palms] is played: Set opponent's HP to 5*
- **Lv3**: 随机使用1张名字含“马”的牌 / 随机出[野马分鬃]或[探马掌]时：令对方生命变为1  
  *Randomly play 1 card with "Horse" in its name. / If [Wild Horses Part the Mane] or [Detect-Horse Palms] is played: Set opponent's HP to 1*

#### 心猿意马 (A Restless Heart and a Wandering Horse) — id 364
- **Lv1**: 随机使用1张机缘牌  
  *Randomly play 1 Fortunes card*
- **Lv2**: 随机使用1张机缘牌  
  *Randomly play 1 Fortunes card*
- **Lv3**: 随机使用1张机缘牌  
  *Randomly play 1 Fortunes card*

#### 御风飞闪 (Wind-Riding Flash) — id 383
- **Lv1**: [体魄]+2 / [身法]+8 / 每有1[身法]向对方造成1[伤害]  
  *[Agility]+8 / Deal 1 [DMG] to the opponent for each [Agility]*
- **Lv2**: [体魄]+2 / [身法]+10 / 每有1[身法]向对方造成1[伤害]  
  *[Agility]+10 / Deal 1 [DMG] to the opponent for each [Agility]*
- **Lv3**: [体魄]+2 / [身法]+12 / 每有1[身法]向对方造成1[伤害]  
  *[Agility]+12 / Deal 1 [DMG] to the opponent for each [Agility]*

#### 冯虚御风 (Riding the Wind) — id 392
*持续 Continuous*  
- **Lv1**: 生命+5 / [身法]+5 / [持续]：每加1[身法]时，向对方造成1[伤害]  
  *HP+5 / [Agility]+5 / [Continuous]: Whenever you gain 1 [Agility], deal 1 [DMG] to the opponent*
- **Lv2**: 生命+10 / [身法]+5 / [持续]：每加1[身法]时，向对方造成1[伤害]  
  *HP+10 / [Agility]+5 / [Continuous]: Whenever you gain 1 [Agility], deal 1 [DMG] to the opponent*
- **Lv3**: 生命+15 / [身法]+5 / [持续]：每加1[身法]时，向对方造成1[伤害]  
  *HP+15 / [Agility]+5 / [Continuous]: Whenever you gain 1 [Agility], deal 1 [DMG] to the opponent*


### Phase 5 — 化神 Incarnation

#### 云泉道茶 (Spring Course Tea) — id 1
- **Lv1**: 可以和任意1级牌合成，将其升级  
  *Can be dragged to any Level 1 card to upgrade it*

#### 狂剑·炎舞 (Unrestrained Sword - Flame Dance) — id 2
- **Lv1**: 2攻 / [击伤]：施加1层[外伤] / 若用过“狂剑”则[再次行动]  
  *2 ATK / [Injured]: Apply 1 stacks of [Wound] / If you have played "Unrestrained Sword" card in this battle, [Chase]*
- **Lv2**: 2攻 / [击伤]：施加2层[外伤] / 若用过“狂剑”则[再次行动]  
  *2 ATK / [Injured]: Apply 2 stacks of [Wound] / If you have played "Unrestrained Sword" card in this battle, [Chase]*
- **Lv3**: 2攻 / [击伤]：施加3层[外伤] / 若用过“狂剑”则[再次行动]  
  *2 ATK / [Injured]: Apply 3 stacks of [Wound] / If you have played "Unrestrained Sword" card in this battle, [Chase]*

#### 混元五行 (Five Elements Of World) — id 14
- **Lv1**: 若已激活全部[五行灵]，获得4层[加攻]和4层[护体]  
  *If all [Five Elements] have been activated, gain 4 stacks of [Increase ATK] and 4 stacks of [Guard Up]*
- **Lv2**: 若已激活全部[五行灵]，获得5层[加攻]和5层[护体]  
  *If all [Five Elements] have been activated, gain 5 stacks of [Increase ATK] and 5 stacks of [Guard Up]*
- **Lv3**: 若已激活全部[五行灵]，获得6层[加攻]和6层[护体]  
  *If all [Five Elements] have been activated, gain 6 stacks of [Increase ATK] and 6 stacks of [Guard Up]*

#### 九霄玲珑镯 (Sky Delicate Bracelet) — id 16
- **Lv1**: [防]+9 / 获得1层[护体] / [再次行动]  
  *[DEF]+9 / Gain 1 stack of [Guard Up] / [Chase]*
- **Lv2**: [防]+9 / 获得2层[护体] / [再次行动]  
  *[DEF]+9 / Gain 2 stacks of [Guard Up] / [Chase]*
- **Lv3**: [防]+9 / 获得3层[护体] / [再次行动]  
  *[DEF]+9 / Gain 3 stacks of [Guard Up] / [Chase]*

#### 土灵·山崩 (Earth Spirit - Landslide) — id 21
- **Lv1**: 8攻 / [土灵]：自身[防]减半，每减1点多3[攻]  
  *8 ATK / [Earth Spirit]: [DEF] halved, for each reduced point add 3 more [ATK]*
- **Lv2**: 15攻 / [土灵]：自身[防]减半，每减1点多3[攻]  
  *15 ATK / [Earth Spirit]: [DEF] halved, for each reduced point add 3 more [ATK]*
- **Lv3**: 15攻 / [土灵]：自身[防]减半，每减1点多4[攻]  
  *15 ATK / [Earth Spirit]: [DEF] halved, for each reduced point add 4 more [ATK]*

#### 星月折扇 (Star Moon Folding Fan) — id 23
*持续 Continuous*  
- **Lv1**: 若[灵气]≥1则加1[星力] / 若[星力]≥3则[再次行动] / [持续]：[星位]上的牌[灵气]消耗减1  
  *If [Qi]≥1, [Star Power]+1 / If [Star Power]≥3, [Chase] / [Continuous]: The [Qi] cost of cards on [Star Point] are reduced by 1*
- **Lv2**: 若[灵气]≥1则加2[星力] / 若[星力]≥3则[再次行动] / [持续]：[星位]上的牌[灵气]消耗减1  
  *If [Qi]≥1, [Star Power]+2 / If [Star Power]≥3, [Chase] / [Continuous]: The [Qi] cost of cards on [Star Point] are reduced by 1*
- **Lv3**: 若[灵气]≥1则加3[星力] / 若[星力]≥3则[再次行动] / [持续]：[星位]上的牌[灵气]消耗减1  
  *If [Qi]≥1, [Star Power]+3 / If [Star Power]≥3, [Chase] / [Continuous]: The [Qi] cost of cards on [Star Point] are reduced by 1*

#### 瞒天过海 (Act Underhand) — id 24
- **Lv1**: [灵气]+3 / [防]+8 / 下1次“后招”视作满足条件  
  *[Qi]+3 / The following 1 times [Post Action] are considered to meet the condition.*
- **Lv2**: [灵气]+4 / [防]+12 / 下2次“后招”视作满足条件  
  *[Qi]+4 / The following 2 times [Post Action] are considered to meet the condition.*
- **Lv3**: [灵气]+5 / [防]+16 / 下3次“后招”视作满足条件  
  *[Qi]+5 / The following 3 times [Post Action] are considered to meet the condition.*

#### 狂雷电闪 (Fury Thunder) — id 29
- **Lv1**: 施加1层[破绽] / 若卡组中有其他名字含“雷”的牌则[再次行动]  
  *Apply 1 [Flaw] / If there are other cards in the deck with "Thunder" in their names, [Chase]*
- **Lv2**: 施加2层[破绽] / 若卡组中有其他名字含“雷”的牌则[再次行动]  
  *Apply 2 [Flaw] / If there are other cards in the deck with "Thunder" in their names, [Chase]*
- **Lv3**: 施加3层[破绽] / 若卡组中有其他名字含“雷”的牌则[再次行动]  
  *Apply 3 [Flaw] / If there are other cards in the deck with "Thunder" in their names, [Chase]*

#### 五行传承 (Inheritance of Five Elements) — id 31
- **Lv1**: [炼化]：获得2张金丹期以上的[五行]牌（优先取卡组首张牌的[五行]）  
  *[Absorb]: Gain 2 [Five Elements] cards (Above Virtuoso Phase and Prioritize cards of the same Element as the first card in deck)*

#### 道韵气息 (Daoist Rhyme Aura) — id 46
- **Lv1**: [炼化]：触发道韵预感，并立刻获得所选的牌  
  *[Absorb]: Trigger the Daoist Rhyme Omen (you can select a card to get)*
- **Lv2** ⟨template⟩: [炼化]：触发道韵预感，并立刻获得所选的牌  
  *[Absorb]: Trigger the Daoist Rhyme Omen (you can select a card to get)*
- **Lv3** ⟨template⟩: [炼化]：触发道韵预感，并立刻获得所选的牌  
  *[Absorb]: Trigger the Daoist Rhyme Omen (you can select a card to get)*

#### 纯净鲛珠 (Pure Merpeople Pearl) — id 59
- **Lv1**: 可与任意同等级的鲛珠合成升级  
  *Can be dragged to any Merpeople Pearl Card with the same Level to upgrade it*
- **Lv2**: 可与任意同等级的鲛珠合成升级  
  *Can be dragged to any Merpeople Pearl Card with the same Level to upgrade it*

#### 魔化鲛珠 (Cursed Merpeople Pearl) — id 60
- **Lv1**: 自身[命元]减1 / 重复上一格牌的效果1次  
  *Lose 1 [Destiny] / Repeat the effect of the card in previous slot 1 time*
- **Lv2**: 自身[命元]减5 / 重复上一格牌的效果2次  
  *Lose 5 [Destiny] / Repeat the effect of the card in previous slot 2 times*
- **Lv3**: 自身[命元]减9 / 重复上一格牌的效果3次  
  *Lose 9 [Destiny] / Repeat the effect of the card in previous slot 3 times*

#### 深渊鲛珠 (Abyssal Merpeople Pearl) — id 61
- **Lv1**: 施加2层[内伤]和1层[困缚]  
  *Apply 2 stacks of [Internal Injury] and 1 stack of [Entangled]*
- **Lv2**: 自身[命元]减1 / 施加3层[内伤]和2层[困缚]  
  *Lose 1 [Destiny] / Apply 3 stacks of [Internal Injury] and 2 stacks of [Entangled]*
- **Lv3**: 自身[命元]减3 / 施加4层[内伤]和3层[困缚]  
  *Lose 3 [Destiny] / Apply 4 stacks of [Internal Injury] and 3 stacks of [Entangled]*

#### 狂化鲛珠 (Frenzied Merpeople Pearl) — id 62
- **Lv1**: 获得2层[加攻]和1层[外伤] / [再次行动]  
  *Gain 2 stacks of [Increase ATK] and 1 stacks of [Wound] / [Chase]*
- **Lv2**: 获得3层[加攻]和2层[外伤] / [再次行动]  
  *Gain 3 stacks of [Increase ATK] and 2 stacks of [Wound] / [Chase]*
- **Lv3**: 自身[命元]减1 / 获得4层[加攻]和3层[外伤] / [再次行动]  
  *Lose 1 [Destiny] / Gain 4 stacks of [Increase ATK] and 3 stack of [Wound] / [Chase]*

#### 迷惘鲛珠 (Bewildering Merpeople Pearl) — id 63
- **Lv1**: 生命及上限+8 / 施加1层[虚弱]  
  *HP and Max HP+8 / Apply 1 stack of [Weakened]*
- **Lv2**: 生命及上限+13 / 施加2层[虚弱]  
  *HP and Max HP+13 / Apply 2 stacks of [Weakened]*
- **Lv3**: 生命及上限+18 / 施加3层[虚弱]  
  *HP and Max HP+18 / Apply 3 stacks of [Weakened]*

#### 五彩鲛珠 (Multicolored Merpeople Pearl) — id 64
- **Lv1**: 随机使用1张门派牌的效果  
  *Trigger effect of 1 random Card of your Sect*
- **Lv2**: 随机使用2张门派牌的效果  
  *Trigger effect of 2 random Cards of your Sect*
- **Lv3**: 随机使用3张门派牌的效果  
  *Trigger effect of 3 random Cards of your Sect*

#### 聚灵鲛珠 (Qi-Gathering Merpeople Pearl) — id 65
*持续 Continuous*  
- **Lv1**: [灵气]+1 / [持续]：每回合开始时加1[灵气]  
  *[Qi]+1 / [Continuous]: At the beginning of each your turn, gain 1 [Qi]*
- **Lv2**: [灵气]+1 / [持续]：每回合开始时加2[灵气]  
  *[Qi]+1 / [Continuous]: At the beginning of each your turn, gain 2 [Qi]*
- **Lv3**: [灵气]+1 / [持续]：每回合开始时加3[灵气]  
  *[Qi]+1 / [Continuous]: At the beginning of each your turn, gain 3 [Qi]*

#### 结晶鲛珠 (Crystallized Merpeople Pearl) — id 66
*持续 Continuous*  
- **Lv1**: [防]+6 / [持续]：每[击伤]对方2生命，自身加1[防]  
  *[DEF]+6 / [Continuous]: When you injure the opponent by ATK, for every 2 HP [Injured], you gain 1 [DEF]*
- **Lv2**: [防]+18 / [持续]：每[击伤]对方2生命，自身加1[防]  
  *[DEF]+18 / [Continuous]: When you injure the opponent by ATK, for every 2 HP [Injured], you gain 1 [DEF]*
- **Lv3**: [防]+30 / [持续]：每[击伤]对方2生命，自身加1[防]  
  *[DEF]+30 / [Continuous]: When you injure the opponent by ATK, for every 2 HP [Injured], you gain 1 [DEF]*

#### 镜像鲛珠 (Mirroring Merpeople Pearl) — id 67
*消耗 Consumable*  
- **Lv1**: 将后1格牌（仅限自身门派或副职业牌）的1级复制加入手牌并减1修为 / [消耗]  
  *Gain a Level 1 copy of the card in next slot and lose 1 Cul. (only card of your own Sect or Side Job can be copied) / [Consumption]*
- **Lv2**: 将后1格牌（仅限自身门派或副职业牌）的2级复制加入手牌并减1修为 / [消耗]  
  *Gain a Level 2 copy of the card in next slot and lose 1 Cul. (only card of your own Sect or Side Job can be copied) / [Consumption]*
- **Lv3**: 将后1格牌（仅限自身门派或副职业牌）的2级复制加入手牌并减1修为 / [消耗] / [再次行动]  
  *Gain a Level 2 copy of the card in next slot and lose 1 Cul. (only card of your own Sect or Side Job can be copied) / [Consumption] / [Chase]*

#### 潜袭鲛珠 (Sneak Merpeople Pearl) — id 68
- **Lv1**: 获得1层[护体] / 向对方施加2层[破绽]  
  *Gain 1 stack of [Guard Up] / Apply 2 stacks of [Flaw]*
- **Lv2**: 获得1层[护体] / 向对方施加4层[破绽]  
  *Gain 1 stack of [Guard Up] / Apply 4 stacks of [Flaw]*
- **Lv3**: 获得2层[护体] / 向对方施加4层[破绽]  
  *Gain 2 stacks of [Guard Up] / Apply 4 stacks of [Flaw]*

#### 血修鲛珠 (Blood-cultivated Merpeople Pearl) — id 69
*消耗 Consumable*  
- **Lv1**: 自身[命元]减1 / 修为+1 / 换牌机会+1 / [消耗]  
  *Lose 1 [Destiny] /  Cul. + 1 / Exchange Card Chance + 1 / [Consumption]*
- **Lv2**: 自身[命元]减2 / 修为+1 / 换牌机会+3 / [消耗]  
  *Lose 2 [Destiny] /  Cul. + 1 / Exchange Card Chance + 3 / [Consumption]*
- **Lv3**: 自身[命元]减3 / 修为+2 / 换牌机会+5 / [消耗]  
  *Lose 3 [Destiny] /  Cul. + 2 / Exchange Card Chance + 5 / [Consumption]*

#### 冥月蟾光 (Styx Moon's Glow) — id 75
- **Lv1**: [体魄]+3 / 获得2层[冥] / [身法]+10  
  *[Physique]+3 / Gain 2 [Styx] / [Agility]+10*
- **Lv2**: [体魄]+4 / 获得3层[冥] / [身法]+11  
  *[Physique]+4 / Gain 3 [Styx] / [Agility]+11*
- **Lv3**: [体魄]+5 / 获得4层[冥] / [身法]+12  
  *[Physique]+5 / Gain 4 [Styx] / [Agility]+12*

#### 万玄破魔掌 (Wan Xuan Demon Breaking Palm) — id 82
- **Lv1**: [体魄]+2 / 每有20[体魄]就将1层[负面状态]转为[加攻] / 3攻×3  
  *[Physique]+2 / For every 20 [Physique] convert 1 stack of [Debuff] to [Increase ATK] / 3 ATK×3*
- **Lv2**: [体魄]+3 / 每有20[体魄]就将1层[负面状态]转为[加攻] / 3攻×4  
  *[Physique]+3 / For every 20 [Physique] convert 1 stack of [Debuff] to [Increase ATK] / 3 ATK×4*
- **Lv3**: [体魄]+4 / 每有20[体魄]就将1层[负面状态]转为[加攻] / 3攻×5  
  *[Physique]+4 / For every 20 [Physique] convert 1 stack of [Debuff] to [Increase ATK] / 3 ATK×5*

#### 八宝杂粮粽 (Mixed Grain Zongzi) — id 95
*持续 Continuous*  
- **Lv1**: [甜粽] / [灵气]+2 / [持续]：每次加[灵气]时额外加1点，再加2生命  
  *[Sweet Zongzi] / [Qi]+2 / [Continuous]: each time you gain [Qi], add 1 more [Qi] and 2 HP*
- **Lv2**: [甜粽] / [灵气]+3 / [持续]：每次加[灵气]时额外加1点，再加4生命  
  *[Sweet Zongzi] / [Qi]+3 / [Continuous]: each time you gain [Qi], add 1 more [Qi] and 4 HP*
- **Lv3**: [甜粽] / [灵气]+4 / [持续]：每次加[灵气]时额外加1点，再加6生命  
  *[Sweet Zongzi] / [Qi]+4 / [Continuous]: each time you gain [Qi], add 1 more [Qi] and 6 HP*

#### 仙风归灵粽 (Spirit Zongzi) — id 96
- **Lv1**: [甜粽] / 生命+5 / 耗尽[灵气]，每点多加5生命  
  *[Sweet Zongzi] / HP+5 / Exhaust [Qi], add 5 more HP for each point exhausted*
- **Lv2**: [甜粽] / 生命+6 / 耗尽[灵气]，每点多加6生命  
  *[Sweet Zongzi] / HP+6 / Exhaust [Qi], add 6 more HP for each point exhausted*
- **Lv3**: [甜粽] / 生命+7 / 耗尽[灵气]，每点多加7生命  
  *[Sweet Zongzi] / HP+7 / Exhaust [Qi], add 7 more HP for each point exhausted*

#### 百川琉璃粽 (Water Combined Zongzi) — id 97
- **Lv1**: [甜粽] / 获得2层[恢复] / 生命+5（每有1层[恢复]或[食欲]多加5点）  
  *[Sweet Zongzi] / Gain 2 stacks of [Regeneration] / HP+5 (add 5 more HP for each stack of [Regeneration] or [Appetite])*
- **Lv2**: [甜粽] / 获得3层[恢复] / 生命+6（每有1层[恢复]或[食欲]多加6点）  
  *[Sweet Zongzi] / Gain 3 stacks of [Regeneration] / HP+6 (add 6 more HP for each stack of [Regeneration] or [Appetite])*
- **Lv3**: [甜粽] / 获得4层[恢复] / 生命+7（每有1层[恢复]或[食欲]多加7点）  
  *[Sweet Zongzi] / Gain 4 stacks of [Regeneration] / HP+7 (add 7 more HP for each stack of [Regeneration] or [Appetite])*

#### 秘制三鲜粽 (Assorted Meat Zongzi) — id 110
- **Lv1**: [咸粽] / 重复5次： / 生命+2（每有1层[负面状态]或[食欲]多加1生命）  
  *[Salty Zongzi] / Repeat 5 times:  / HP+2 (Add 1 more HP for each stack of [Debuff] or [Appetite])*
- **Lv2**: [咸粽] / 重复6次： / 生命+2（每有1层[负面状态]或[食欲]多加1生命）  
  *[Salty Zongzi] / Repeat 6 times:  / HP+2 (Add 1 more HP for each stack of [Debuff] or [Appetite])*
- **Lv3**: [咸粽] / 重复7次： / 生命+2（每有1层[负面状态]或[食欲]多加1生命）  
  *[Salty Zongzi] / Repeat 7 times:  / HP+2 (Add 1 more HP for each stack of [Debuff] or [Appetite])*

#### 梅香玉露粽 (Double Plum Zongzi) — id 111
- **Lv1**: [咸粽] / 生命+2 / 下1次使用的牌连续生效两次  
  *[Salty Zongzi] / HP+2 / The next card will trigger twice*
- **Lv2**: [咸粽] / 生命+8 / 下1次使用的牌连续生效两次  
  *[Salty Zongzi] / HP+8 / The next card will trigger twice*
- **Lv3**: [咸粽] / 生命+14 / 下1次使用的牌连续生效两次  
  *[Salty Zongzi] / HP+14 / The next card will trigger twice*

#### 修罗镇魂粽 (Shura Zongzi) — id 112
- **Lv1**: [咸粽] / 获得2层[内伤] / 自身每有1层[负面状态]加1[灵气]和3生命  
  *[Salty Zongzi] / Gain 2 stacks of [Internal Injury] / Add 1 [Qi] and 3 HP for every 1 stack of [Debuff]*
- **Lv2**: [咸粽] / 获得3层[内伤] / 自身每有1层[负面状态]加1[灵气]和4生命  
  *[Salty Zongzi] / Gain 3 stacks of [Internal Injury] / Add 1 [Qi] and 4 HP for every 1 stack of [Debuff]*
- **Lv3**: [咸粽] / 获得4层[内伤] / 自身每有1层[负面状态]加1[灵气]和5生命  
  *[Salty Zongzi] / Gain 4 stacks of [Internal Injury] / Add 1 [Qi] and 5 HP for every 1 stack of [Debuff]*

#### 云剑·龙泉 (Cloud Sword - Dragon Spring) — id 122
- **Lv1**: 2攻×2 / [击伤]：[升级]下2次使用的牌（战斗结束还原） / [连云]：[再次行动]  
  *2 ATK × 2 / [Injured]: [Upgrade] next 2 cards when playing them (restored after the battle) / [Cloud Hit]: [Chase]*
- **Lv2**: 2攻×2 / [击伤]：[升级]下3次使用的牌（战斗结束还原） / [连云]：[再次行动]  
  *2 ATK × 2 / [Injured]: [Upgrade] next 3 cards when playing them (restored after the battle) / [Cloud Hit]: [Chase]*
- **Lv3**: 2攻×2 / [击伤]：[升级]下4次使用的牌（战斗结束还原） / [连云]：[再次行动]  
  *2 ATK × 2 / [Injured]: [Upgrade] next 4 cards when playing them (restored after the battle) / [Cloud Hit]: [Chase]*

#### 云剑·雪影飞 (Cloud Sword - Flying Snow Shade) — id 123
- **Lv1**: 2攻 / [连云]：每连续用过1张“云剑”此牌多攻击1次并加1[灵气]  
  *2 ATK / [Cloud Hit]: For each consecutive Cloud Sword played, gain 1 [Qi] and make an additional ATK*
- **Lv2**: 3攻 / [连云]：每连续用过1张“云剑”此牌多攻击1次并加1[灵气]  
  *3 ATK / [Cloud Hit]: For each consecutive Cloud Sword played, gain 1 [Qi] and make an additional ATK*
- **Lv3**: 4攻 / [连云]：每连续用过1张“云剑”此牌多攻击1次并加1[灵气]  
  *4 ATK / [Cloud Hit]: For each consecutive Cloud Sword played, gain 1 [Qi] and make an additional ATK*

#### 百鸟玲珑镯 (CentiBird Delicate Bracelet) — id 124
- **Lv1**: 获得1层[护体] / 令“灵剑”牌的灵气消耗减1 / [再次行动]  
  *Gain 1 [Guard Up] / The "Spirit Sword" card's Qi cost decrease 1 / [Chase]*
- **Lv2**: [灵气]+2 / 获得1层[护体] / 令“灵剑”牌的灵气消耗减1 / [再次行动]  
  *[Qi]+2 / Gain 1 [Guard Up] / The "Spirit Sword" card's Qi cost decrease 1 / [Chase]*
- **Lv3**: [灵气]+4 / 获得1层[护体] / 令“灵剑”牌的灵气消耗减1 / [再次行动]  
  *[Qi]+4 / Gain 1 [Guard Up] / The "Spirit Sword" card's Qi cost decrease 1 / [Chase]*

#### 澄心剑阵 (Clear Heart Sword Formation) — id 126
- **Lv1**: [防]+2 / 继承金丹和元婴仙命对澄心剑胚的加成 / 若卡组含4张以上“剑阵”则[再次行动]  
  *[DEF]+2 / Inherits Virtuoso and Immortality Phase effects of Clear Heart Sword Embryo / If your deck contains 4 or more "Sword Formation", [Chase]*
- **Lv2**: [防]+7 / 继承金丹和元婴仙命对澄心剑胚的加成 / 若卡组含4张以上“剑阵”则[再次行动]  
  *[DEF]+7 / Inherits Virtuoso and Immortality Phase effects of Clear Heart Sword Embryo / If your deck contains 4 or more "Sword Formation", [Chase]*
- **Lv3**: [防]+12 / 继承金丹和元婴仙命对澄心剑胚的加成 / 若卡组含4张以上“剑阵”则[再次行动]  
  *[DEF]+12 / Inherits Virtuoso and Immortality Phase effects of Clear Heart Sword Embryo / If your deck contains 4 or more "Sword Formation", [Chase]*

#### 天元无极盘 (Ultimate Polaris Hexagram Base) — id 128
*持续 Continuous*  
- **Lv1**: [持续]：自身每回合开始时加1[卦象]和1[星力]  
  *[Continuous]: At the beginning of your turn, add 1 [Hexagram] and 1 [Star Power]*
- **Lv2**: 后2格[成为星位] / [持续]：自身每回合开始时加1[卦象]和1[星力]  
  *The next 2 slots [Become Star Point] / [Continuous]: At the beginning of your turn, add 1 [Hexagram] and 1 [Star Power]*
- **Lv3**: 后4格[成为星位] / [持续]：自身每回合开始时加1[卦象]和1[星力]  
  *The next 4 slots [Become Star Point] / [Continuous]: At the beginning of your turn, add 1 [Hexagram] and 1 [Star Power]*

#### 星月六爻扇 (Star Moon Hexagram Fan) — id 131
*持续 Continuous*  
- **Lv1**: [持续]：每加1[星力]/[卦象]/[灵气]时向对方造成3[伤害]  
  *[Continuous]: Whenever you gain 1 [Star Power] / [Hexagram] / [Qi], deal 3/3/2 [DMG] to the opponent*
- **Lv2**: [星力]+1 / [持续]：每加1[星力]/[卦象]/[灵气]时向对方造成3[伤害]  
  *[Star Power]+1 / [Continuous]: Whenever you gain 1 [Star Power] / [Hexagram] / [Qi], deal 3/3/2 [DMG] to the opponent*
- **Lv3**: [星力]+2 / [持续]：每加1[星力]/[卦象]/[灵气]时向对方造成3[伤害]  
  *[Star Power]+2 / [Continuous]: Whenever you gain 1 [Star Power] / [Hexagram] / [Qi], deal 3/3/2 [DMG] to the opponent*

#### 天髓葫芦 (Heavenly Marrow Gourd) — id 132
- **Lv1**: [灵气]+2 / 生命及上限+3 / 下2次使用五行牌后，若该牌的五行已激活则[再次行动]  
  *[Qi]+2 / HP and Max HP+3 / For the next 2 times after you play a Five Elements card, if the card's Five Elements have been activated, [Chase]*
- **Lv2**: [灵气]+3 / 生命及上限+5 / 下2次使用五行牌后，若该牌的五行已激活则[再次行动]  
  *[Qi]+3 / HP and Max HP+5 / For the next 2 times after you play a Five Elements card, if the card's Five Elements have been activated, [Chase]*
- **Lv3**: [灵气]+4 / 生命及上限+7 / 下2次使用五行牌后，若该牌的五行已激活则[再次行动]  
  *[Qi]+4 / HP and Max HP+7 / For the next 2 times after you play a Five Elements card, if the card's Five Elements have been activated, [Chase]*

#### 混元逆克阵 (Ultimate Overcome Formation) — id 133
*持续 Continuous*  
- **Lv1**: [持续]：每当使用一张[五行]牌时，若[五行克制]后一格的牌，则[激活]后者的[五行]并加2[灵气]和6[防]  
  *[Continuous]: When you play a Five Elements card that has [Overcoming Interaction of Five Elements] with the next slot, [Activate] the [Five Elements] of the next slot, then add 2 [Qi] and 6 [DEF]*
- **Lv2**: [持续]：每当使用一张[五行]牌时，若[五行克制]后一格的牌，则[激活]后者的[五行]并加3[灵气]和8[防]  
  *[Continuous]: When you play a Five Elements card that has [Overcoming Interaction of Five Elements] with the next slot, [Activate] the [Five Elements] of the next slot, then add 3 [Qi] and 8 [DEF]*
- **Lv3**: [持续]：每当使用一张[五行]牌时，若[五行克制]后一格的牌，则[激活]后者的[五行]并加4[灵气]和10[防]  
  *[Continuous]: When you play a Five Elements card that has [Overcoming Interaction of Five Elements] with the next slot, [Activate] the [Five Elements] of the next slot, then add 4 [Qi] and 10 [DEF]*

#### 木灵·万物生 (Wood Spirit - All Things Grow) — id 134
*持续 Continuous*  
- **Lv1**: 生命及上限+3 / [木灵]：[再次行动] / [持续]：自身每回合开始时获得1层[加攻]  
  *HP and Max HP+3 / [Wood Spirit]: [Chase] / [Continuous]: At the beginning of your turn, add 1 [Increase ATK]*
- **Lv2**: 生命及上限+9 / [木灵]：[再次行动] / [持续]：自身每回合开始时获得1层[加攻]  
  *HP and Max HP+9 / [Wood Spirit]: [Chase] / [Continuous]: At the beginning of your turn, add 1 [Increase ATK]*
- **Lv3**: 生命及上限+15 / [木灵]：[再次行动] / [持续]：自身每回合开始时获得1层[加攻]  
  *HP and Max HP+15 / [Wood Spirit]: [Chase] / [Continuous]: At the beginning of your turn, add 1 [Increase ATK]*

#### 浩荡不息 (Unceasing Universe) — id 137
- **Lv1**: 10攻 / [体魄]+3 / 生命+3 / [气势]+3 / [身法]+10  
  *10 ATK / [Physique]+3 / HP+3 / [Force]+3 / [Agility]+10*
- **Lv2**: 10攻 / [体魄]+4 / 生命+4 / [气势]+4 / [身法]+10  
  *10 ATK / [Physique]+4 / HP+4 / [Force]+4 / [Agility]+10*
- **Lv3**: 10攻 / [体魄]+5 / 生命+5 / [气势]+5 / [身法]+10  
  *10 ATK / [Physique]+5 / HP+5 / [Force]+5 / [Agility]+10*

#### 玄心盛气掌 (Soul Overwhelming Palm) — id 138
- **Lv1**: 每有1种不同的[负面状态]加2[气势] / 8攻（每有1[气势]多2攻）  
  *For every different [Debuff] you have, add 2 [Force] / 8 ATK (2 more ATK for each stack of [Force])*
- **Lv2**: 每有1种不同的[负面状态]加3[气势] / 10攻（每有1[气势]多2攻）  
  *For every different [Debuff] you have, add 3 [Force] / 10 ATK (2 more ATK for each stack of [Force])*
- **Lv3**: 每有1种不同的[负面状态]加4[气势] / 12攻（每有1[气势]多2攻）  
  *For every different [Debuff] you have, add 4 [Force] / 12 ATK (2 more ATK for each stack of [Force])*

#### 玄冥镇魂符 (Xuanming Requiem Fulu) — id 157
*消耗 Consumable*  
- **Lv1**: 自身减20%当前生命，令对方减该数值+15的生命及上限 / [消耗]  
  *Reduce your current HP by 20%, and cause the opponent to lose that amount plus 15 HP and Max HP / [Consumption]*
- **Lv2**: 自身减25%当前生命，令对方减该数值+20的生命及上限 / [消耗]  
  *Reduce your current HP by 25%, and cause the opponent to lose that amount plus 20 HP and Max HP / [Consumption]*
- **Lv3**: 自身减30%当前生命，令对方减该数值+25的生命及上限 / [消耗]  
  *Reduce your current HP by 30%, and cause the opponent to lose that amount plus 25 HP and Max HP / [Consumption]*

#### 曳影剑阵 (Yeying Sword Formation) — id 213
- **Lv1**: 2攻×2 / 卡组中每有1张剑阵就追加1次攻击（最多追加3次） / 每次[击伤]加3[防]  
  *2 ATK × 2 / Make an additional attack for every “Sword Formation” in the deck (up to 3)  / Add 3 [DEF] for every attack that [Injured] the opponent*
- **Lv2**: 2攻×2 / 卡组中每有1张剑阵就追加1次攻击（最多追加4次） / 每次[击伤]加3[防]  
  *2 ATK × 2 / Make an additional attack for every “Sword Formation” in the deck (up to 4)  / Add 3 [DEF] for every attack that [Injured] the opponent*
- **Lv3**: 2攻×3 / 卡组中每有1张剑阵就追加1次攻击（最多追加4次） / 每次[击伤]加3[防]  
  *2 ATK × 3 / Make an additional attack for every “Sword Formation” in the deck (up to 4)  / Add 3 [DEF] for every attack that [Injured] the opponent*

#### 孤虚金书 (Solitary Void Golden Scroll) — id 215
- **Lv1**: [灵气]+2 / 生命+6 / <color=#808080><size=15><i>处孤而击虚，则敌虚即破，实相不存</i></size></color>  
  *[Qi]+2 / HP+6*
- **Lv2**: [灵气]+4 / [防]+6 / <color=#808080><size=15><i>处孤而击虚，则敌虚即破，实相不存</i></size></color>  
  *[Qi]+4 / [DEF]+6*
- **Lv3**: [灵气]+4 / 每有1[灵气]就向对方施加1层[内伤]，然后自身[灵气]减半  
  *[Qi]+4 / For each of your [Qi], apply 1 [Internal Injury], then halve your [Qi].*

#### 背孤 (Face Isolation) — id 216
- **Lv1**: 自身下1次被攻击时，先向对方施加1层[虚弱] / [再次行动]  
  *When you are attacked next time, apply 1 [Weakened] to the opponent / [Chase]*

#### 击虚 (Strike Vacuity) — id 217
- **Lv1**: 自身下1次攻击时，先向对方施加1层[破绽] / [再次行动]  
  *When you attack next time, apply 1 [Flaw] to the opponent / [Chase]*

#### 忘忧 (Forget Worries) — id 218
- **Lv1**: 生命及上限+12（每[激活]过1次[木灵]多加2） / 双方各加2层[护体]，各减2层全部[负面状态]，并各无法行动1回合  
  *HP and Max HP + 12(Gain 2 more for each time you have [Activated] [Wood Spirit]) / Both players gain 2 [Guard Up], reduce 2 stacks of all [Debuff] and unable to act for 1 turn.*
- **Lv2**: 生命及上限+18（每[激活]过1次[木灵]多加2） / 双方各加2层[护体]，各减3层全部[负面状态]，并各无法行动1回合  
  *HP and Max HP + 18(Gain 2 more for each time you have [Activated] [Wood Spirit]) / Both players gain 2 [Guard Up], reduce 3 stacks of all [Debuff] and unable to act for 1 turn.*
- **Lv3**: 生命及上限+24（每[激活]过1次[木灵]多加2） / 双方各加2层[护体]，各减4层全部[负面状态]，并各无法行动1回合  
  *HP and Max HP + 24(Gain 2 more for each time you have [Activated] [Wood Spirit]) / Both players gain 2 [Guard Up], reduce 4 stacks of all [Debuff] and unable to act for 1 turn.*

#### 赤金盘龙棍 (Red Gold Dragon Stick) — id 220
- **Lv1**: [拳]：[气势]+4，每有5[体魄]加1生命 / [棍]：4攻×2（每有9[体魄]多1攻） / 使用后[切换架势]  
  *[Fist]: [Force]+4, gain 1 HP for every 5 [Physique] / [Stick]: 4 ATK × 2 (Gain 1 ATK for every 9 [Physique]) / [Switch Stance]*
- **Lv2**: [拳]：[气势]+5，每有5[体魄]加1生命 / [棍]：7攻×2（每有9[体魄]多1攻） / 使用后[切换架势]  
  *[Fist]: [Force]+5, gain 1 HP for every 5 [Physique] / [Stick]: 7 ATK × 2 (Gain 1 ATK for every 9 [Physique]) / [Switch Stance]*
- **Lv3**: [拳]：[气势]+6，每有5[体魄]加1生命 / [棍]：10攻×2（每有9[体魄]多1攻） / 使用后[切换架势]  
  *[Fist]: [Force]+6, gain 1 HP for every 5 [Physique] / [Stick]: 10 ATK × 2 (Gain 1 ATK for every 9 [Physique]) / [Switch Stance]*

#### 冰灵护体丹 (Ice Spirit Guard Elixir) — id 232
- **Lv1**: [出售]：[通宝]+40 / [炼化]：回满[体力]，每回复3点抽1张牌  
  *[Sell]: [Coin]+40 / [Absorb]: Fully restore [Energy], draw 1 card for every 3 recovered*

#### 太虚熔炉 (Furnace of Void) — id 233
- **Lv1**: [使用]：耗6体力，获得3张丹药牌  
  *[Use]: Costs 6 [Energy], gain 3 random elixir card*

#### 镇魂封元符 (Soul Requiem Fulu) — id 242
- **Lv1**: [使用]：耗尽[体力]，每点加4[通宝]  
  *[Use]: Exhaust [Energy], for each point gain 4 [Coin]*

#### 千里神行符 (Divine Walk Fulu) — id 243
- **Lv1**: [使用]：下次加[通宝]时，数量×2  
  *[Use]: Next time you gain [Coin], receive a ×2 bonus*

#### 玄晶护心镜 (Dark Crystal Heart Shield) — id 252
- **Lv1**: [耐久]1 / [使用]：获得后一格牌的复制  
  *[Durability] 1 / [Use]: Gain a copy of the next slot*

#### 九冥镇魔印 (Nether Seal Evil Signet) — id 253
- **Lv1**: [耐久]1 / [使用]：下次加[通宝]时，数量×3 / [炼化]：本轮炼化卡牌获得的[通宝]×2  
  *[Durability] 1 / [Use]: Next time you gain [Coin], receive a ×3 bonus / [Absorb]: Until the next round begins, receive a ×2 [Coin] bonus each time you Absorb a card*
- **Lv2** ⟨template⟩: [耐久]{otherParams[0]} / [使用]：下次加[通宝]时，数量×{otherParams[1]} / [炼化]：本轮炼化卡牌获得的[通宝]×{otherParams[2]}  
  *[Durability] {otherParams[0]} / [Use]: Next time you gain [Coin], receive a ×{otherParams[1]} bonus / [Absorb]: Until the next round begins, receive a ×{otherParams[2]} [Coin] bonus each time you Absorb a card*
- **Lv3** ⟨template⟩: [耐久]{otherParams[0]} / [使用]：下次加[通宝]时，数量×{otherParams[1]} / [炼化]：本轮炼化卡牌获得的[通宝]×{otherParams[2]}  
  *[Durability] {otherParams[0]} / [Use]: Next time you gain [Coin], receive a ×{otherParams[1]} bonus / [Absorb]: Until the next round begins, receive a ×{otherParams[2]} [Coin] bonus each time you Absorb a card*

#### 影枭兔 (Shadow Owl Rabbit) — id 257
- **Lv1**: 下1张牌[使用]或[出售]时连续生效2次  
  *When the next 1 card is triggered by [Use] or [Sell], it will trigger 2times*

#### 五色绳 (Five Colored Strings) — id 299
- **Lv1**: 可与任意同等级的粽子合成升级  
  *Can be dragged to any Zongzi Card with the same Level to upgrade it*
- **Lv2**: 可与任意同等级的粽子合成升级  
  *Can be dragged to any Zongzi Card with the same Level to upgrade it*

#### 天髓珍馐粽 (Heavenly Delicacy Zongzi) — id 301
- **Lv1**: [甜粽] / 下2次使用牌后，若回合内加过生命则[再次行动]  
  *[Sweet Zongzi] / The next 2 times you play a card, [Chase] if HP has been added during the turn*
- **Lv2**: [甜粽] / 下2次使用牌后，若回合内加过生命则[再次行动]  
  *[Sweet Zongzi] / The next 2 times you play a card, [Chase] if HP has been added during the turn*
- **Lv3**: [甜粽] / 下2次使用牌后，若回合内加过生命则[再次行动]  
  *[Sweet Zongzi] / The next 2 times you play a card, [Chase] if HP has been added during the turn*

#### 缤纷玉馔粽 (Various Cate Zongzi) — id 302
- **Lv1**: [咸粽] / 获得1层[食欲] / [再次行动]  
  *[Salty Zongzi] / Gain 1 stack(s) of [Appetite] / [Chase]*
- **Lv2**: [咸粽] / 获得2层[食欲] / [再次行动]  
  *[Salty Zongzi] / Gain 2 stack(s) of [Appetite] / [Chase]*
- **Lv3**: [咸粽] / 获得3层[食欲] / [再次行动]  
  *[Salty Zongzi] / Gain 3 stack(s) of [Appetite] / [Chase]*

#### 幻·镜像鲛珠 (M - Mirroring Merpeople Pearl) — id 321
- **Lv1**: [炼化]：减1修为并获得卡组首格牌的1级复制  
  *[Absorb]: Lose 1 Cultivation and gain 1 Level 1 copy of the card in the first slot*

#### 马到成功 (Horse’s Arrival Brings Success) — id 361
- **Lv1**: 随机使用2张任意门派的秘术牌  
  *Randomly play 2 Secret Enchantment cards from any Sect*
- **Lv2**: 随机使用2张任意门派的秘术牌  
  *Randomly play 2 Secret Enchantment cards from any Sect*
- **Lv3**: 随机使用2张任意门派的秘术牌  
  *Randomly play 2 Secret Enchantment cards from any Sect*

#### 谈马掌 (Effect-Horse Palms) — id 362
- **Lv1**: 随机使用2张任意角色的专属牌  
  *Randomly play 2 Exclusive Cards of any character*
- **Lv2**: 随机使用2张任意角色的专属牌  
  *Randomly play 2 Exclusive Cards of any character*
- **Lv3**: 随机使用2张任意角色的专属牌  
  *Randomly play 2 Exclusive Cards of any character*

#### 木灵斩 (Wood Spirit Slash) — id 373
- **Lv1**: 10攻（每加过1次生命多3攻） / [木灵]：每[击伤]3生命加1生命  
  *10 [ATK] (Add 3 [ATK] for each time HP has been increased) / [Wood Spirit]: For every 3 HP [Injured] by this card, add 1 HP*
- **Lv2**: 16攻（每加过1次生命多3攻） / [木灵]：每[击伤]3生命加1生命  
  *16 [ATK] (Add 3 [ATK] for each time HP has been increased) / [Wood Spirit]: For every 3 HP [Injured] by this card, add 1 HP*
- **Lv3**: 22攻（每加过1次生命多3攻） / [木灵]：每[击伤]3生命加1生命  
  *22 [ATK] (Add 3 [ATK] for each time your HP has been increased) / [Wood Spirit]: For every 3 HP [Injured] by this card, add 1 HP*

#### 火灵斩 (Fire Spirit Slash) — id 374
- **Lv1**: 10攻（每减过对方1次生命上限多3攻） / [火灵]：每[击伤]5生命，减对方1生命及上限  
  *10 [ATK] (Add 3 [ATK] for each time the opponent has lost Max HP) / [Fire Spirit]: For every 5 HP [Injured] by this card, the opponent lose 1 HP and Max HP*
- **Lv2**: 16攻（每减过对方1次生命上限多3攻） / [火灵]：每[击伤]5生命，减对方1生命及上限  
  *16 [ATK] (Add 3 [ATK] for each time the opponent has lost Max HP) / [Fire Spirit]: For every 5 HP [Injured] by this card, the opponent lose 1 HP and Max HP*
- **Lv3**: 22攻（每减过对方1次生命上限多3攻） / [火灵]：每[击伤]5生命，减对方1生命及上限  
  *22 [ATK] (Add 3 [ATK] for each time the opponent has lost Max HP) / [Fire Spirit]: For every 5 HP [Injured] by this card, the opponent lose 1 HP and Max HP*

#### 土灵斩 (Earth Spirit Slash) — id 375
- **Lv1**: 10攻（每加过1次防多3攻） / [土灵]：每[击伤]3生命加1防  
  *10 [ATK] (Add 3 [ATK] for each time you have gained [DEF]) / [Earth Spirit]: For every 3 HP [Injured] by this card, gain 1 [DEF]*
- **Lv2**: 16攻（每加过1次防多3攻） / [土灵]：每[击伤]3生命加1防  
  *16 [ATK] (Add 3 [ATK] for each time you have gained [DEF]) / [Earth Spirit]: For every 3 HP [Injured] by this card, gain 1 [DEF]*
- **Lv3**: 22攻（每加过1次防多3攻） / [土灵]：每[击伤]3生命加1防  
  *22 [ATK] (Add 3 [ATK] for each time you have gained [DEF]) / [Earth Spirit]: For every 3 HP [Injured] by this card, gain 1 [DEF]*

#### 金灵斩 (Metal Spirit Slash) — id 376
- **Lv1**: 10攻（每加过1次[锋锐]多3攻） / [金灵]：每[击伤]4生命加1[锋锐]  
  *10 [ATK] (Add 3 [ATK] for each time you have gained [Penetrate]) / [Metal Spirit]: For every 4 HP [Injured] by this card, gain 1 [Penetrate]*
- **Lv2**: 16攻（每加过1次[锋锐]多3攻） / [金灵]：每[击伤]4生命加1[锋锐]  
  *16 [ATK] (Add 3 [ATK] for each time you have gained [Penetrate]) / [Metal Spirit]: For every 4 HP [Injured] by this card, gain 1 [Penetrate]*
- **Lv3**: 22攻（每加过1次[锋锐]多3攻） / [金灵]：每[击伤]4生命加1[锋锐]  
  *22 [ATK] (Add 3 [ATK] for each time you have gained [Penetrate]) / [Metal Spirit]: For every 4 HP [Injured] by this card, gain 1 [Penetrate]*

#### 水灵斩 (Water Spirit Slash) — id 377
- **Lv1**: 10攻（每加过1次[灵气]或[水势]多3攻） / [水灵]：每[击伤]5生命获得1层[水势]  
  *10 [ATK] (Add 3 [ATK] for each time you have gained [Qi] or [Force of Water]) / [Water Spirit]: For every 5 HP [Injured] by this card, gain 1 [Force of Water]*
- **Lv2**: 16攻（每加过1次[灵气]或[水势]多3攻） / [水灵]：每[击伤]5生命获得1层[水势]  
  *16 [ATK] (Add 3 [ATK] for each time you have gained [Qi] or [Force of Water]) / [Water Spirit]: For every 5 HP [Injured] by this card, gain 1 [Force of Water]*
- **Lv3**: 22攻（每加过1次[灵气]或[水势]多3攻） / [水灵]：每[击伤]5生命获得1层[水势]  
  *22 [ATK] (Add 3 [ATK] for each time you have gained [Qi] or [Force of Water]) / [Water Spirit]: For every 5 HP [Injured] by this card, gain 1 [Force of Water]*

#### 百鸟曳影诀 (CentiBird Swift Shadow Art) — id 388
*持续 Continuous*  
- **Lv1**: [灵气]+3 / [持续]：每失去1[灵气]时加1[剑气]  
  *[Qi]+3 / [Continuous]: Whenever you lose 1 [Qi], add 1 [Sword Qi]*
- **Lv2**: [灵气]+4 / [持续]：每失去1[灵气]时加1[剑气]  
  *[Qi]+4 / [Continuous]: Whenever you lose 1 [Qi], add 1 [Sword Qi]*
- **Lv3**: [灵气]+6 / [持续]：每失去1[灵气]时加1[剑气]  
  *[Qi]+6 / [Continuous]: Whenever you lose 1 [Qi], add 1 [Sword Qi]*

#### 星弈·治孤 (Astral Move - Rescue) — id 389
- **Lv1**: [灵气]+4 / [星位]：施加2层[虚弱]和2层[破绽] / [开局]：[相邻]格[成为星位]，若为空格则放入"星弈•飞"  
  *[Qi]+4 / [Star Point]: Apply 2 stack(s) of [Weakness] and 2 stack(s) of [Flaw] / [Opening]: [Adjacent] slots [Become Star Point]; if empty, place "Astral Move - Flying"*
- **Lv2**: [灵气]+4 / [星位]：施加3层[虚弱]和3层[破绽] / [开局]：[相邻]格[成为星位]，若为空格则放入"星弈•飞"  
  *[Qi]+4 / [Star Point]: Apply 3 stack(s) of [Weakness] and 3 stack(s) of [Flaw] / [Opening]: [Adjacent] slots [Become Star Point]; if empty, place "Astral Move - Flying"*
- **Lv3**: [灵气]+4 / [星位]：施加4层[虚弱]和4层[破绽] / [开局]：[相邻]格[成为星位]，若为空格则放入"星弈•飞"  
  *[Qi]+4 / [Star Point]: Apply 4 stack(s) of [Weakness] and 4 stack(s) of [Flaw] / [Opening]: [Adjacent] slots [Become Star Point]; if empty, place "Astral Move - Flying"*

#### 五行忘忧梦 (Five Elements Carefree Dream) — id 390
- **Lv1**: 生命及上限+6 / 使用五行玉瓶中第一格牌的效果  
  *HP and Max HP+6 / Use the effect of the first card in the Five Elements Pure Vase*
- **Lv2**: 生命及上限+12 / 使用五行玉瓶中第一格牌的效果  
  *HP and Max HP+12 / Use the effect of the first card in the Five Elements Pure Vase*
- **Lv3**: 生命及上限+18 / 使用五行玉瓶中第一格牌的效果  
  *HP and Max HP+18 / Use the effect of the first card in the Five Elements Pure Vase*

#### 闪转腾挪 (Dodge and Weave) — id 391
- **Lv1**: [身法]+8 / [被动]（不可叠加）：每加1[身法]时，额外加1[防]  
  *[Agility]+8 / [Passive] (does not stack): Whenever you gain 1 [Agility], also add 1 [DEF]*
- **Lv2**: [身法]+10 / [被动]（不可叠加）：每加1[身法]时，额外加1[防]  
  *[Agility]+10 / [Passive] (does not stack): Whenever you gain 1 [Agility], also add 1 [DEF]*
- **Lv3**: [身法]+12 / [被动]（不可叠加）：每加1[身法]时，额外加1[防]  
  *[Agility]+12 / [Passive] (does not stack): Whenever you gain 1 [Agility], also add 1 [DEF]*


### Phase 6 — 特殊 Special

#### 魔气爆发 (Demonic Qi Burst) — id 40
- **Lv1**: 20攻 / 对方每有1层[内伤]，此牌多4攻  
  *20 ATK / For each stack of [Internal Injury] the opponent has, this card adds 4 ATK*
- **Lv2**: 25攻 / 对方每有1层[内伤]，此牌多6攻  
  *25 ATK / For each stack of [Internal Injury] the opponent has, this card adds 6 ATK*
- **Lv3**: 30攻 / 对方每有1层[内伤]，此牌多8攻  
  *30 ATK / For each stack of [Internal Injury] the opponent has, this card adds 8 ATK*

#### 魔龙乱舞 (Demonic Dragon's Chaotic Dance) — id 77
- **Lv1**: 3攻×3 / 对方每有1层外伤追加1次攻击  
  *3 ATK×3 / For each stack of [Wound] your opponent has, make an additional attack*
- **Lv2**: 4攻×4 / 对方每有1层外伤追加1次攻击  
  *4 ATK×4 / For each stack of [Wound] your opponent has, make an additional attack*
- **Lv3**: 5攻×5 / 对方每有1层外伤追加1次攻击  
  *5 ATK×5 / For each stack of [Wound] your opponent has, make an additional attack*

#### 龙 (Loong) — id 79
*持续 Continuous*  
- **Lv1**: 获得2层[加攻] / 获得2层[护体] / [持续]：[再次行动]不会被其他效果阻止，且每回合触发次数上限+1  
  *Gain 2 [Increase ATK] / Gain 2 [Guard Up] / [Continuous]: [Chase] won't be prevented by other effect. [Chase] can be triggered 1 more time in each turn.*
- **Lv2**: 获得3层[加攻] / 获得3层[护体] / [持续]：[再次行动]不会被其他效果阻止，且每回合触发次数上限+2  
  *Gain 3 [Increase ATK] / Gain 3 [Guard Up] / [Continuous]: [Chase] won't be prevented by other effect. [Chase] can be triggered 2 more times in each turn.*
- **Lv3**: 获得4层[加攻] / 获得4层[护体] / [持续]：[再次行动]不会被其他效果阻止，且每回合触发次数上限+3  
  *Gain 4 [Increase ATK] / Gain 4 [Guard Up] / [Continuous]: [Chase] won't be prevented by other effect. [Chase] can be triggered 3 more times in each turn.*

#### 粽子试炼 (Zongzi Trial) — id 114
- **Lv1**: 8回合内加满生命，方能通过试炼！  
  *Fill up your HP in 8 turns to pass the trial!*
- **Lv2**: 8回合内加满生命，方能通过试炼！  
  *Fill up your HP in 8 turns to pass the trial!*
- **Lv3**: 8回合内加满生命，方能通过试炼！  
  *Fill up your HP in 8 turns to pass the trial!*

#### 五色补天石 (Nüwa Stone) — id 175
*消耗 Consumable*  
- **Lv1**: [蓄灵]7 / 生命及上限+64 / 自身下1次回合开始时生命加倍 / [消耗]  
  *[Gather Qi] 7 / HP and Max HP + 64 / At the beginning of your next 1 turn, your HP will be doubled. / [Consumption]*

#### 灵墟锁魂塔 (Haotian Pagoda) — id 176
- **Lv1**: [蓄灵]4 / 令对方当前[灵气]、生命、生命上限减半 / 施加4层[困缚]  
  *[Gather Qi] 4 / Reduce the opponent's current [Qi], HP, and Max HP by half / Apply 4 [Entangled]*

#### 灵韵御心琴 (Fuxi Guqin) — id 177
- **Lv1**: 复制对方下1张牌的效果 / 令对方[跳过]下1张牌 / [再次行动]  
  *Copy the effect of your opponent's next card / [Skip] the opponent's next card / [Chase]*

#### 五帝长生印 (Kongtong Seal) — id 178
*消耗 Consumable*  
- **Lv1**: 生命上限永久+5 / 下2次使用可升级的牌时将其永久[升级] / [再次行动] / [消耗]  
  *Max HP+5 in this game. / The next 2 times you play an upgradable card, upgrade it in this game. / [Chase] / [Consumption]*

#### 鸿蒙镇天钟 (Donghuang Zhong) — id 179
- **Lv1**: [蓄灵]6 / 从卡组第一格开始直至此牌，依次重复每一张已用过的牌的效果  
  *[Gather Qi] 6 / Starting from the first card in your deck up to this card, repeat the effect of each card that has already been played.*

#### 百草神炼鼎 (Shennong Ding) — id 180
- **Lv1**: [灵气]+4 / 生命及上限+16 / [被动]：战斗结束后随机获得2张3级的灵植师或炼丹师炼化牌  
  *[Qi]+4 / HP and Max HP + 16 / [Passive]: At the end of battle you gain 2 Lv. 3 cards of Elixirist or Plant Master with [Absorb].*

#### 幽冥化生壶 (Spirit Fusion Pot) — id 181
- **Lv1**: [蓄灵]4 / 对方下4次使用牌时将牌[降级]，若不可降级则改为吸取其9生命及上限 / [开局]：对方下2次使用牌受以上效果影响  
  *[Gather Qi] 4 / [Downgrade] opponent's next 4 cards on play. If a card cannot be downgraded, instead steal 9 HP and Max HP. / [Opening]: Apply above effect to opponent's next 2 cards*

#### 苍穹裂隙 (Crimson Star) — id 182
- **Lv1**: 可与部分卡牌融汇，激发出返虚期的力量  
  *Can fuse with some cards to stimulate the power of the Divinity Phase*

#### 死劫 (Doom Calamity) — id 329
- **Lv1**: 令对方生命变为1 / <#B21D81>[耗尽]</color>  
  *Set the opponent's HP to 1 / <#B21D81>[Exhaust]</color>*

#### 一马平川 (A Horse on Vast Plains) — id 365
- **Lv1**: 随机使用1张返虚期牌  
  *Randomly play 1 card of Divinity Phase*
- **Lv2**: 随机使用1张返虚期牌  
  *Randomly play 1 card of Divinity Phase*
- **Lv3**: 随机使用1张返虚期牌  
  *Randomly play 1 card of Divinity Phase*

#### 马 (Horse) — id 368
- **Lv1**: 20攻 / 10%[概率]追加2026攻（不受[卦象]加成）  
  *20 ATK / 10% chance to deal an extra 2026 ATK (Unaffected by [Hexagram])*
- **Lv2**: 26攻 / 15%[概率]追加2026攻（不受[卦象]加成）  
  *26 ATK / 15% chance to deal an extra 2026 ATK (Unaffected by [Hexagram])*
- **Lv3**: 26攻 / 25%[概率]追加2026攻（不受[卦象]加成）  
  *26 ATK / 25% chance to deal an extra 2026 ATK (Unaffected by [Hexagram])*

#### 龙马精神 (Spirit of the Dragon-Horse) — id 370
*持续 Continuous*  
- **Lv1**: 将[体魄]加至上限 / [持续]：[击伤]、[连云]、[星位]和[五行]效果无条件触发，每当[卦象]为0时加1[卦象]  
  *Set [Physique] to maximum. / [Continuous]: Effects of [Injured], [Cloud Hit], [Star Point], and [Five Elements] trigger unconditionally. Whenever [Hexagram] is 0, gain 1 [Hexagram]*

#### 定风波·解封 (Settle the Storm - Unseal) — id 372
- **Lv1**: 3攻×2（每[激活]过1次[五行]，再多攻击1次） / [开局]：[激活]全部[五行] / [被动]：每[激活]一种[五行]时向对方造成5[伤害]  
  *3 [ATK] × 2 (Attack 1 more time for each time [Five Elements] has been [Activated]) / [Opening]: [Activate] all [Five Elements] / [Passive]: Deal 5 [DMG] when you [Activate] any [Five Elements]*
- **Lv2**: 4攻×2（每[激活]过1次[五行]，再多攻击1次） / [开局]：[激活]全部[五行] / [被动]：每[激活]一种[五行]时向对方造成6[伤害]  
  *4 [ATK] × 2 (Attack 1 more time for each time [Five Elements] has been [Activated]) / [Opening]: [Activate] all [Five Elements] / [Passive]: Deal 6 [DMG] when you [Activate] any [Five Elements]*
- **Lv3**: 5攻×2（每[激活]过1次[五行]，再多攻击1次） / [开局]：[激活]全部[五行] / [被动]：每[激活]一种[五行]时向对方造成7[伤害]  
  *5 [ATK] × 2 (Attack 1 more time for each time [Five Elements] has been [Activated]) / [Opening]: [Activate] all [Five Elements] / [Passive]: Deal 7 [DMG] when you [Activate] any [Five Elements]*


### Phase 0 — ?

#### 道韵腊肉粽 (Daoist Rhyme Preserved Meat Zongzi) — id 393
- **Lv1**: [咸粽] / 清除自身全部[负面状态]，每清除1层加3生命和2层[恢复]  
  *[Salty Zongzi] / Clear all [Debuff] from yourself, and gain 3 HP and 2 layers of [Regeneration] for each layer cleared*
- **Lv2**: [咸粽] / 清除自身全部[负面状态]，每清除1层加4生命和2层[恢复]  
  *[Salty Zongzi] / Clear all [Debuff] from yourself, and gain 4 HP and 2 layers of [Regeneration] for each layer cleared*
- **Lv3**: [咸粽] / 清除自身全部[负面状态]，每清除1层加5生命和2层[恢复]  
  *[Salty Zongzi] / Clear all [Debuff] from yourself, and gain 5 HP and 2 layers of [Regeneration] for each layer cleared*

#### 天劫麻辣粽 (Heavenly Tribulation Spicy Zongzi) — id 394
- **Lv1**: [咸粽] / 每用过1次[咸粽]就重复1次：生命+3  
  *[Salty Zongzi] / Repeat 1 time for every 1 use of [Salty Zongzi]: HP+ 3*
- **Lv2**: [咸粽] / 每用过1次[咸粽]就重复1次：生命+4  
  *[Salty Zongzi] / Repeat 1 time for every 1 use of [Salty Zongzi]: HP+ 4*
- **Lv3**: [咸粽] / 每用过1次[咸粽]就重复1次：生命+5  
  *[Salty Zongzi] / Repeat 1 time for every 1 use of [Salty Zongzi]: HP+ 5*

#### 万象碱水粽 (Myriad Phenomena Alkaline Water Zongzi) — id 395
- **Lv1**: [甜粽] / [生命]+2 / [身法]+5 / 重复手牌最右侧的持续牌的效果  
  *[Sweet Zongzi] / [HP]+2 / [Agility]+5 / Repeat the effect of the Continuous card on the rightmost side of the hand*
- **Lv2**: [甜粽] / [生命]+8 / [身法]+5 / 重复手牌最右侧的持续牌的效果  
  *[Sweet Zongzi] / [HP]+8 / [Agility]+5 / Repeat the effect of the Continuous card on the rightmost side of the hand*
- **Lv3**: [甜粽] / [生命]+14 / [身法]+5 / 重复手牌最右侧的持续牌的效果  
  *[Sweet Zongzi] / [HP]+14 / [Agility]+5 / Repeat the effect of the Continuous card on the rightmost side of the hand*

#### 沁心蜜枣粽 (Refreshing Candied JujubeZongzi) — id 397
- **Lv1**: [甜粽] / [身法]+5 / [生命]+6（每有1[灵气]多加2[生命]）  
  *[Sweet Zongzi] / [Agility]+5 / HP+6 (For every 1[Qi], add 2HP)*
- **Lv2**: [甜粽] / [身法]+5 / [生命]+12（每有1[灵气]多加2[生命]）  
  *[Sweet Zongzi] / [Agility]+5 / HP+12 (For every 1[Qi], add 2HP)*
- **Lv3**: [甜粽] / [身法]+5 / [生命]+18（每有1[灵气]多加2[生命]）  
  *[Sweet Zongzi] / [Agility]+5 / HP+18 (For every 1[Qi], add 2HP)*

#### 无极香辣粽 (Infinite Fragrant Pungent Zongzi) — id 398
- **Lv1**: [咸粽] / [灵气]+3 / 生命+3 / 每有2点[灵气]就加1层[食欲]和[内伤]  
  *[Salty Zongzi] / [Qi]+3 / HP+3 / For every 2 points of [Qi], add 1 layer of [Appetite] and [Internal Injury]*
- **Lv2**: [咸粽] / [灵气]+4 / 生命+4 / 每有2点[灵气]就加1层[食欲]和[内伤]  
  *[Salty Zongzi] / [Qi]+4 / HP+4 / For every 2 points of [Qi], add 1 layer of [Appetite] and [Internal Injury]*
- **Lv3**: [咸粽] / [灵气]+5 / 生命+5 / 每有2点[灵气]就加1层[食欲]和[内伤]  
  *[Salty Zongzi] / [Qi]+5 / HP+5 / For every 2 points of [Qi], add 1 layer of [Appetite] and [Internal Injury]*

#### 仙府大白粽 (Yi Xian Palace Supreme Zongzi) — id 399
- **Lv1**: 加生命上限30%的生命 / <#B21D81>[耗尽]</color> / <color=#808080><size=15><i>弈仙府荣誉出品，吃了都说好（撑死的不算）</i></size></color>  
  *Increase HP by 30% of the maximum HP / <#B21D81>[Exhaust]</color> / <color=#808080><size=15><i>Don't burst your stomach</i></size></color>*


## Dream (梦·) cards — general


### Phase 4 — 元婴 Immortality

#### 梦·冰封雪莲 (Dream - Frozen Snow Lotus) — id 333
- **Lv1**: [防]+10 / 获得1层[护体]  
  *[DEF]+10 / Gain 1 [Guard Up]*
- **Lv2**: [防]+10 / 获得1层[护体] / [先机]：多加1层[护体]  
  *[DEF]+10 / Gain 1 [Guard Up] / [First Use]: Gain 1 more [Guard Up]*

#### 梦·神来之笔 (Dream - Divine Brush) — id 341
- **Lv1**: [防]+2 / 随机使用一张元婴期及以上的灵宠、法宝或秘术牌的效果  
  *[DEF]+2 / Randomly trigger the effect of one Immortality Phase or above Spiritual Pet Card, Talisman Card, or Secret Enchantment Card.*
- **Lv2**: [防]+10 / 随机使用一张元婴期及以上的灵宠、法宝或秘术牌的效果  
  *[DEF]+10 / Randomly trigger the effect of one Immortality Phase or above Spiritual Pet Card, Talisman Card, or Secret Enchantment Card.*

#### 梦·缚仙古藤 (Dream - Entangling Ancient Vine) — id 343
- **Lv1**: 施加1层[外伤] / 下2次攻击[碎防] / [先机]：施加1层[困缚]  
  *Apply 1 [Wound] / Next 2 attacks gain [Smash DEF] / [First Use]: Apply 1 [Entangled]*
- **Lv2**: 施加2层[外伤] / 下2次攻击[碎防] / [先机]：施加1层[困缚]  
  *Apply 2 [Wound] / Next 2 attacks gain [Smash DEF] / [First Use]: Apply 1 [Entangled]*

#### 梦·飞云丹 (Dream - Cloud Elixir) — id 344
*持续 Continuous*  
- **Lv1**: [灵气]+1 / [持续]：自身回合开始时，若对方有[防]，则自身下1次攻击[无视防御]，否则加1[灵气]  
  *[Qi]+1 / [Continuous]: At the beginning of your turn, if the opponent has [DEF], your next 1 attack gain [Ignore DEF]; otherwise, add 1 [Qi]*
- **Lv2**: [灵气]+3 / [持续]：自身回合开始时，若对方有[防]，则自身下1次攻击[无视防御]，否则加1[灵气]  
  *[Qi]+3 / [Continuous]: At the beginning of your turn, if the opponent has [DEF], your next 1 attack gain [Ignore DEF]; otherwise, add 1 [Qi]*

#### 梦·大还丹 (Dream - Great Recover Elixir) — id 345
*持续 Continuous*  
- **Lv1**: 生命及上限+10 / [持续]：自身回合开始时，若生命上限/生命小于对方则加4生命上限/4生命  
  *HP and Max HP+10 / [Continuous]: At the beginning of your turn, if your Max HP/HP is less than the opponent's, add 4 Max HP/4 HP*
- **Lv2**: 生命及上限+15 / [持续]：自身回合开始时，若生命上限/生命小于对方则加8生命上限/8生命  
  *HP and Max HP+15 / [Continuous]: At the beginning of your turn, if your Max HP/HP is less than the opponent's, add 8 Max HP/8 HP*

#### 梦·转弦合调 (Dream - Chord In Tune) — id 346
- **Lv1**: [灵气]+1 / 自身下次[再次行动]时不会被其他效果阻止 / 已用过其他牌则[再次行动]  
  *[Qi]+1 / Your next [Chase] cannot be prevented by other effects / If you have played another card, [Chase]*
- **Lv2**: [灵气]+2 / 自身下次[再次行动]时不会被其他效果阻止 / 已用过其他牌则[再次行动]  
  *[Qi]+2 / Your next [Chase] cannot be prevented by other effects / If you have played another card, [Chase]*

#### 梦·回响阵纹 (Dream - Echo Formation) — id 349
*消耗 Consumable, 持续 Continuous*  
- **Lv1**: 重复手牌中的一张[消耗]牌或[持续]牌的效果  
  *Retrigger the effect of a [Consumption] card or [Continuous] card in your hand*
- **Lv2**: 生命及上限+6 / 重复手牌中的一张[消耗]牌或[持续]牌的效果  
  *HP and Max HP+6 / Retrigger the effect of a [Consumption] card or [Continuous] card in your hand*

#### 梦·寒冰咒 (Dream - Ice Incantation) — id 351
- **Lv1**: 重复2次：对方减5[生命] / 令对方下回合无法加[防]和生命  
  *Repeat 2 times: The opponent loses 5 HP / The opponent cannot gain [DEF] or HP next turn*
- **Lv2**: 重复3次：对方减5[生命] / 令对方下回合无法加[防]和生命  
  *Repeat 3 times: The opponent loses 5 HP / The opponent cannot gain [DEF] or HP next turn*

#### 梦·厄劫缠身 (Dream - Envelop In Disaster) — id 369
- **Lv1**: 施加1层[内伤] / [开局]：对方同格牌[降级]，若无法[降级]则令对方下次使用同格牌时改为[跳过]  
  *Apply 1 [Internal Injury] / [Opening]: [Downgrade] the opponent's card in the same slot, or [Skip] that card if unable*
- **Lv2**: 施加3层[内伤] / [开局]：对方同格牌[降级]，若无法[降级]则令对方下次使用同格牌时改为[跳过]  
  *Apply 3 [Internal Injury] / [Opening]: [Downgrade] the opponent's card in the same slot, or [Skip] that card if unable*

#### 梦·锐金符 (Dream - Sharp Metal Fulu) — id 379
- **Lv1**: 造成13[伤害]（若对方生命≤30，此牌的效果改为令对方生命变为-100）  
  *Deal 13 [DMG] (If the opponent's HP ≤ 30, this card's effect changes to set the opponent's HP to -100)*
- **Lv2**: 造成18[伤害]（若对方生命≤35，此牌的效果改为令对方生命变为-100）  
  *Deal 18 [DMG] (If the opponent's HP ≤ 35, this card's effect changes to set the opponent's HP to -100)*

#### 梦·妙笔生花 (Dream - Wonderful Strokes) — id 386
- **Lv1**: [炼化]：[修为]-4，随机获得4张其他门派的元婴期牌  
  *[Absorb]: [Cultivation]-4, randomly gain 4 Immortality Phase cards from other sects*
- **Lv2**: [炼化]：[修为]-4，随机获得4张其他门派的化神期牌  
  *[Absorb]: [Cultivation]-4, randomly gain 4 Incarnation Phase phase cards from other sects*


### Phase 5 — 化神 Incarnation

#### 梦·不动金刚阵 (Dream - Motionless Tutelary Formation) — id 334
- **Lv1**: 生命及上限+20 / 自身下回合[无法行动]，直至下回合结束前自身生命及上限的损失变为1  
  *HP and Max HP+20 / You [Unable to act] next turn. Until the end of next turn, your HP and Max HP loss becomes 1*

#### 梦·天命重现 (Dream - Heavenly Time Recurring) — id 335
- **Lv1**: 自身减2生命 / 对方已用过牌则[再次行动] / [先机]：令对方[跳至]上1张牌  
  *Reduce your own HP by 2. / If the opponent has already played a card, [Chase] / [First Use]: Make the opponent [Skip To] the previous card*

#### 梦·狂舞曲 (Dream - Craze Dance Tune) — id 340
- **Lv1**: 双方各自下2次使用牌后[再次行动]  
  *Both players [Chase] after their next 2 card plays*

#### 梦·清心咒 (Dream - Calm Incantation) — id 342
- **Lv1**: [灵气]+3 / 自身所有[负面状态]减4层，获得4层[辟邪]  
  *[Qi]+3 / Remove 4 stacks from all your [Debuff]s, gain 4 [Hexproof]*

#### 梦·自在随心 (Dream - At Own Pace) — id 347
- **Lv1**: [炼化]：织梦珊瑚+1  
  *[Absorb]: Dream Coral +1*

#### 梦·天音困仙曲 (Dream - Predicament for Immortals) — id 348
- **Lv1**: 自身减5生命 / [被动]：阻止双方各自前[3]个回合的[再次行动]的效果  
  *Reduce your own HP by 5. / [Passive]: Block both players' [Chase] effects in the first 3 turns*

#### 梦·空间灵田 (Dream - Space Spiritual Field) — id 350
- **Lv1**: 若在后2格，首次使用改为[跳过]此牌 / [被动]：战斗结束时减1修为获得卡组中1张1级[常规牌]的复制  
  *If in the last 2 slots, [Skip] the first play / [Passive]: At the end of battle, lose 1 Cultivation to gain a copy of 1 Lv.1 [Regular Card] from your deck*

#### 梦·天马行空 (Dream - Heavenly Horse Soaring the Skies) — id 363
- **Lv1**: 随机使用1张化神期梦境牌  
  *Randomly play 1 Dream card of Incarnation Phase*

#### 梦·九煞破灵曲 (Dream - Nine Evil Ruptsprite) — id 378
- **Lv1**: 双方减4[灵气] / [被动]：双方各自首个回合的加[灵气]效果减半  
  *Both players lose 4 [Qi] / [Passive]: Both players' [Qi] gain effects are halved in the first turn*

#### 梦·画龙点睛 (Dream - Finishing Touch) — id 384
- **Lv1**: [炼化]：升级[卡组]中的1张副职牌（不限等级）  
  *[Absorb]: Upgrade 1 Side-Job Card in your Deck (no level limit)*

#### 梦·飞枭灵芝 (Dream - Flying Owl Reishi) — id 385
- **Lv1**: [炼化]：下场战斗开始时自身[速度]+3，若自身为后手，则获得[死战之志]效果  
  *[Absorb]: At the start of next battle, your [Speed]+3; if you are going second, gain [Will of Desperate Combat] effect*

#### 梦·弱体符 (Dream - Weaken Fulu) — id 387
*消耗 Consumable*  
- **Lv1**: 施加1层[虚弱] / [再次行动] / [消耗]  
  *Apply 1 [Weakened] / [Chase] / [Consumption]*


### Phase 0 — ?

#### 梦·触类旁通 (Dream - Reason By Analogy) — id 380
- **Lv1** ⟨template⟩: [防]+{def} / 随机使用1张2级的元婴期副职牌 / [被动]：战斗结束时减1[修为]获得首次随机出的牌  
  *[DEF]+{def} / Randomly use 1 Lv2. Immortality Phase Side-Job Card / [Passive]: At the end of battle, lose 1 [Cultivation] to gain the first randomly used card*
- **Lv2** ⟨template⟩: [防]+{def} / 随机使用1张2级的化神期副职牌 / [被动]：战斗结束时减1[修为]获得首次随机出的牌  
  *[DEF]+{def} / Randomly use 1 Lv2. Incarnation Phase Side-Job Card / [Passive]: At the end of battle, lose 1 [Cultivation] to gain the first randomly used card*


## Dream (梦·) cards — 七星阁 Heptastar Pavilion


### Phase 5 — 化神 Incarnation

#### 梦蝶游仙 (Die Ling Shen Ying) — id 168
- **Lv1**: 5攻×2 / 反转自身[出牌方向] / 10%概率[再次行动]  
  *5 ATK × 2 / Reverse self [Card Play Direction] / 10% chance to [Chase]*


## Special / event / spirit-pet cards (id 99xxxxxx)


### Phase 1 — 炼气 Meditation

#### 机缘造化 (Fortunes and Luck) — id 99000000
- **Lv1**: [置换]：获得一张机缘牌  
  *[Exchange]: Draw a Fortunes Card*
- **Lv2**: [置换]：获得一张机缘牌  
  *[Exchange]: Draw a Fortunes Card*
- **Lv3**: [置换]：获得一张机缘牌  
  *[Exchange]: Draw a Fortunes Card*

#### 重宝现世 (Treasures Appear) — id 99000001
- **Lv1**: [置换]：获得一张法宝牌  
  *[Exchange]: Draw a Talisman Card*
- **Lv2**: [置换]：获得一张法宝牌  
  *[Exchange]: Draw a Talisman Card*
- **Lv3**: [置换]：获得一张法宝牌  
  *[Exchange]: Draw a Talisman Card*

#### 灵宠认主 (Spirit Pet Mastered) — id 99000002
- **Lv1**: [置换]：获得一张灵宠牌  
  *[Exchange]: Draw a Spiritual Pet Card*
- **Lv2**: [置换]：获得一张灵宠牌  
  *[Exchange]: Draw a Spiritual Pet Card*
- **Lv3**: [置换]：获得一张灵宠牌  
  *[Exchange]: Draw a Spiritual Pet Card*

#### 秘术传承 (Inheritance of the Secret Enchantment) — id 99000003
- **Lv1**: [置换]：获得一张门派秘术牌  
  *[Exchange]: Draw a Secret Enchantment Card*
- **Lv2**: [置换]：获得一张门派秘术牌  
  *[Exchange]: Draw a Secret Enchantment Card*
- **Lv3**: [置换]：获得一张门派秘术牌  
  *[Exchange]: Draw a Secret Enchantment Card*

#### 神秘宝图 (Mysterious Treasure Map) — id 99000004
- **Lv1**: [置换]：获得一张未知牌  
  *[Exchange]: Draw a Unknown Card*
- **Lv2**: [置换]：获得一张未知牌  
  *[Exchange]: Draw a Unknown Card*
- **Lv3**: [置换]：获得一张未知牌  
  *[Exchange]: Draw a Unknown Card*

#### 灵光一现 (An Epiphany) — id 99000005
- **Lv1**: [置换]：获得一张更高境界的副职牌  
  *[Exchange]: Draw a Higer Phase Side Job Card*
- **Lv2**: [置换]：获得一张更高境界的副职牌  
  *[Exchange]: Draw a Higer Phase Side Job Card*
- **Lv3**: [置换]：获得一张更高境界的副职牌  
  *[Exchange]: Draw a Higer Phase Side Job Card*

#### 玄银甲 (Black Silver Armor) — id 99000100
- **Lv1**: [防]+5 / 然后[防]加倍  
  *[DEF]+5 / then [DEF] is doubled*
- **Lv2**: [防]+8 / 然后[防]加倍  
  *[DEF]+8 / then [DEF] is doubled*
- **Lv3**: [防]+11 / 然后[防]加倍  
  *[DEF]+11 / then [DEF] is doubled*

#### 刺尖枪 (Thorns Spear) — id 99000107
- **Lv1**: 12攻 / 对方每有2点防此牌多1攻  
  *12 ATK / This card gets 1 more ATK for every 2 DEF the opponent have*
- **Lv2**: 16攻 / 对方每有2点防此牌多1攻  
  *16 ATK / This card gets 1 more ATK for every 2 DEF the opponent have*
- **Lv3**: 20攻 / 对方每有2点防此牌多1攻  
  *20 ATK / This card gets 1 more ATK for every 2 DEF the opponent have*

#### 破空雕 (Break Sky Eagle) — id 99000200
*持续 Continuous*  
- **Lv1**: 造成4[伤害] / [持续]：之后每回合向对方造成1[伤害]  
  *Deal 4 [DMG] / [Continuous]: Deal 1 [DMG] at the start of your turn*
- **Lv2**: 造成4[伤害] / [持续]：之后每回合向对方造成2[伤害]  
  *Deal 4 [DMG] / [Continuous]: Deal 2 [DMG] at the start of your turn*
- **Lv3**: 造成4[伤害] / [持续]：之后每回合向对方造成3[伤害]  
  *Deal 4 [DMG] / [Continuous]: Deal 3 [DMG] at the start of your turn*

#### 胖仙狸 (Fat Immortal Raccoon) — id 99000208
*持续 Continuous*  
- **Lv1**: 生命+4 / [持续]：之后每回合加1生命  
  *HP+4 / [Continuous]: Add 1 HP at the start of your turn*
- **Lv2**: 生命+4 / [持续]：之后每回合加2生命  
  *HP+4 / [Continuous]: Add 2 HP at the start of your turn*
- **Lv3**: 生命+4 / [持续]：之后每回合加3生命  
  *HP+4 / [Continuous]: Add 3 HP at the start of your turn*


### Phase 2 — 筑基 Foundation

#### 玉露瓶 (Dew Jade Vase) — id 99000101
- **Lv1**: 生命+11 / [命元]+2  
  *HP+11 / [Destiny]+2*
- **Lv2**: 生命+14 / [命元]+3  
  *HP+14 / [Destiny]+3*
- **Lv3**: 生命+17 / [命元]+4  
  *HP+17 / [Destiny]+4*

#### 无名古剑 (Nameless Ancient Sword) — id 99000108
- **Lv1**: 11攻 / 若自身生命小于12，此牌攻加倍  
  *11 ATK / If your HP is less than 12, this card's ATK is doubled*
- **Lv2**: 15攻 / 若自身生命小于12，此牌攻加倍  
  *15 ATK / If your HP is less than 12, this card's ATK is doubled*
- **Lv3**: 19攻 / 若自身生命小于12，此牌攻加倍  
  *19 ATK / If your HP is less than 12, this card's ATK is doubled*

#### 暗星蝙蝠 (Dark Star Bat) — id 99000201
*持续 Continuous*  
- **Lv1**: [持续]：攻击对方时若[击伤]的生命不大于5，恢复等量生命  
  *[Continuous]: After you attack your opponent, if [Injured] your opponent's HP is not greater than 5, you gain an equal amount of HP*
- **Lv2**: [持续]：攻击对方时若[击伤]的生命不大于7，恢复等量生命  
  *[Continuous]: After you attack your opponent, if [Injured] your opponent's HP is not greater than 7, you gain an equal amount of HP*
- **Lv3**: [持续]：攻击对方时若[击伤]的生命不大于9，恢复等量生命  
  *[Continuous]: After you attack your opponent, if [Injured] your opponent's HP is not greater than 9, you gain an equal amount of HP*

#### 孤夜狼 (Lonely Night Wolf) — id 99000209
*持续 Continuous*  
- **Lv1**: [持续]：自身生命小于一半时，所有牌多4攻  
  *[Continuous]: When your HP is less than half Max Hp, all cards add 4 ATK*
- **Lv2**: [持续]：自身生命小于一半时，所有牌多5攻  
  *[Continuous]: When your HP is less than half Max Hp, all cards add 5 ATK*
- **Lv3**: [持续]：自身生命小于一半时，所有牌多6攻  
  *[Continuous]: When your HP is less than half Max Hp, all cards add 6 ATK*


### Phase 3 — 金丹 Virtuoso

#### 天火炼魂旗 (Fire Soul Refinement Flag) — id 99000102
- **Lv1**: 对方减15生命及上限 / 施加1层[内伤]  
  *Opponent loses 15 HP and Max HP / Apply 1 stack(s) of [Internal Injury]*
- **Lv2**: 对方减15生命及上限 / 施加2层[内伤]  
  *Opponent loses 15 HP and Max HP / Apply 2 stack(s) of [Internal Injury]*
- **Lv3**: 对方减15生命及上限 / 施加3层[内伤]  
  *Opponent loses 15 HP and Max HP / Apply 3 stack(s) of [Internal Injury]*

#### 养魂玉莲 (Requiem Jade Lotus) — id 99000109
- **Lv1**: 生命及上限+15 / 获得1层[恢复]  
  *HP and Max HP+15 / Gain 1 stack(s) of [Regeneration]*
- **Lv2**: 生命及上限+15 / 获得2层[恢复]  
  *HP and Max HP+15 / Gain 2 stack(s) of [Regeneration]*
- **Lv3**: 生命及上限+15 / 获得3层[恢复]  
  *HP and Max HP+15 / Gain 3 stack(s) of [Regeneration]*

#### 狼皇血晶 (Blood Crystal of Wolf King) — id 99000112
- **Lv1**: 自身减15%当前生命 / 获得4层[加攻]  
  *Lose 15% of current HP / Gain 4 stacks of [Increase ATK]*
- **Lv2**: 自身减15%当前生命 / 获得5层[加攻]  
  *Lose 15% of current HP / Gain 5 stacks of [Increase ATK]*
- **Lv3**: 自身减15%当前生命 / 获得6层[加攻]  
  *Lose 15% of current HP / Gain 6 stacks of [Increase ATK]*

#### 地玄龟 (Black Earth Turtle) — id 99000202
*持续 Continuous*  
- **Lv1**: [防]+4 / [持续]：回合开始时[防]只减20%，并加2[防]  
  *[DEF]+4 / [Continuous]: At the beginning of your turn, [DEF] only lose 20% rather than 50% and add extra 2 [DEF]*
- **Lv2**: [防]+8 / [持续]：回合开始时[防]只减20%，并加3[防]  
  *[DEF]+8 / [Continuous]: At the beginning of your turn, [DEF] only lose 20% rather than 50% and add extra 3 [DEF]*
- **Lv3**: [防]+12 / [持续]：回合开始时[防]只减20%，并加4[防]  
  *[DEF]+12 / [Continuous]: At the beginning of your turn, [DEF] only lose 20% rather than 50% and add extra 4 [DEF]*

#### 锦毛鼠 (Brocade Rat) — id 99000203
*持续 Continuous*  
- **Lv1**: 自身减4生命 / [持续]：战斗结束时多抽1张牌  
  *Lose 4 HP / [Continuous]: At the end of battle round, draw extra 1 card(s)*
- **Lv2**: 自身减8生命 / [持续]：战斗结束时多抽2张牌  
  *Lose 8 HP / [Continuous]: At the end of battle round, draw extra 2 card(s)*
- **Lv3**: 自身减12生命 / [持续]：战斗结束时多抽3张牌  
  *Lose 12 HP / [Continuous]: At the end of battle round, draw extra 3 card(s)*


### Phase 4 — 元婴 Immortality

#### 混元封神珠 (Cosmos Seal Divine Orb) — id 99000103
- **Lv1**: 造成9[伤害] / 施加3层[虚弱]  
  *Deal 9 [DMG] / Apply 3 stacks of [Weakened]*
- **Lv2**: 造成9[伤害] / 施加4层[虚弱]  
  *Deal 9 [DMG] / Apply 4 stacks of [Weakened]*
- **Lv3**: 造成9[伤害] / 施加5层[虚弱]  
  *Deal 9 [DMG] / Apply 5 stacks of [Weakened]*

#### 金元三尖枪 (Metal Tri-Thorn Spear) — id 99000110
- **Lv1**: 3攻×3 / 每次攻击后施加1层[破绽]  
  *3 ATK × 3 / Apply 1 stack of [Flaw] after each attack*
- **Lv2**: 5攻×3 / 每次攻击后施加1层[破绽]  
  *5 ATK × 3 / Apply 1 stack of [Flaw] after each attack*
- **Lv3**: 7攻×3 / 每次攻击后施加1层[破绽]  
  *7 ATK × 3 / Apply 1 stack of [Flaw] after each attack*

#### 逍遥古琴 (Carefree Guqin) — id 99000113
*持续 Continuous*  
- **Lv1**: [持续]：双方的[普通攻击]加2攻且获得[再次行动]  
  *[Continuous]: Both player's [Normal Attack] gain [Chase] and add 2 ATK*
- **Lv2**: [持续]：双方的[普通攻击]加5攻且获得[再次行动]  
  *[Continuous]: Both player's [Normal Attack] gain [Chase] and add 5 ATK*
- **Lv3**: [持续]：双方的[普通攻击]加8攻且获得[再次行动]  
  *[Continuous]: Both player's [Normal Attack] gain [Chase] and add 8 ATK*

#### 吞天赤眼兽 (Scarlet-Eye The Sky Consumer) — id 99000205
*持续 Continuous*  
- **Lv1**: [持续]：每回合吸取对方2生命  
  *[Continuous]: At the beginning of your turn, steal 2 HP from the opponent*
- **Lv2**: [持续]：每回合吸取对方3生命  
  *[Continuous]: At the beginning of your turn, steal 3 HP from the opponent*
- **Lv3**: [持续]：每回合吸取对方4生命  
  *[Continuous]: At the beginning of your turn, steal 4 HP from the opponent*

#### 浴火凤凰 (Ashes Phoenix) — id 99000207
*持续 Continuous*  
- **Lv1**: [持续]：下次生命≤0时，复活并回到10生命，同时加10生命上限  
  *[Continuous]: For the next time when the HP is less or equal to 0, revive with 10 HP and add 10 Max HP*
- **Lv2**: [持续]：下次生命≤0时，复活并回到15生命，同时加15生命上限  
  *[Continuous]: For the next time when the HP is less or equal to 0, revive with 15 HP and add 15 Max HP*
- **Lv3**: [持续]：下次生命≤0时，复活并回到20生命，同时加20生命上限  
  *[Continuous]: For the next time when the HP is less or equal to 0, revive with 20 HP and add 20 Max HP*

#### 三尾讙 (Three Tailed Cat) — id 99000212
*持续 Continuous*  
- **Lv1**: 换牌机会+1 / [持续]：自身每回合结束时获得1层[辟邪]  
  *Exchange Card Chance + 1 / [Continuous]: At the end of each your turn, you gain 1 stack of [Hexproof]*
- **Lv2**: 换牌机会+2 / [持续]：自身每回合结束时获得1层[辟邪]  
  *Exchange Card Chance + 2 / [Continuous]: At the end of each your turn, you gain 1 stack of [Hexproof]*
- **Lv3**: 换牌机会+3 / [持续]：自身每回合结束时获得1层[辟邪]  
  *Exchange Card Chance + 3 / [Continuous]: At the end of each your turn, you gain 1 stack of [Hexproof]*


### Phase 5 — 化神 Incarnation

#### 九冥镇魔印 (Nether Seal Evil Signet) — id 99000104
- **Lv1**: 清空对方的[防]和[护体] / 造成30[伤害]  
  *Remove the opponent's all [DEF] and [Guard Up] / Deal 30 [DMG]*
- **Lv2**: 清空对方的[防]和[护体] / 造成36[伤害]  
  *Remove the opponent's all [DEF] and [Guard Up] / Deal 36 [DMG]*
- **Lv3**: 清空对方的[防]和[护体] / 造成42[伤害]  
  *Remove the opponent's all [DEF] and [Guard Up] / Deal 42 [DMG]*

#### 玄晶护心镜 (Dark Crystal Heart Shield) — id 99000106
- **Lv1**: [防]+20 / 获得2层[护体]  
  *[DEF]+20 / Gain 2 stacks of [Guard Up]*
- **Lv2**: [防]+20 / 获得3层[护体]  
  *[DEF]+20 / Gain 3 stacks of [Guard Up]*
- **Lv3**: [防]+20 / 获得4层[护体]  
  *[DEF]+20 / Gain 4 stacks of [Guard Up]*

#### 猎枭古弓 (Bow of Hunting Owl) — id 99000114
- **Lv1**: 12攻 / [击伤]：施加6层[困缚]  
  *12 ATK / [Injured]: Apply 6 stacks of [Entangled]*
- **Lv2**: 14攻 / [击伤]：施加7层[困缚]  
  *14 ATK / [Injured]: Apply 7 stacks of [Entangled]*
- **Lv3**: 16攻 / [击伤]：施加8层[困缚]  
  *16 ATK / [Injured]: Apply 8 stacks of [Entangled]*

#### 七彩灵鹤 (Colorful Spirit Crane) — id 99000204
*持续 Continuous*  
- **Lv1**: [持续]：之后加[灵气]的效果变为2倍  
  *[Continuous]: Add [Qi] effect is multiplied by 2*
- **Lv2**: [灵气]+2 / [持续]：之后加[灵气]的效果变为2倍  
  *[Qi]+2 / [Continuous]: Add [Qi] effect is multiplied by 2*
- **Lv3**: [灵气]+4 / [持续]：之后加[灵气]的效果变为2倍  
  *[Qi]+4 / [Continuous]: Add [Qi] effect is multiplied by 2*

#### 影枭兔 (Shadow Owl Rabbit) — id 99000210
*持续 Continuous*  
- **Lv1**: [持续]：所有牌获得[再次行动]，但触发再次行动前自身减10生命  
  *[Continuous]: All cards gain [Chase] and you will lose 10 HP before the Chase*
- **Lv2**: [持续]：所有牌获得[再次行动]，但触发再次行动前自身减8生命  
  *[Continuous]: All cards gain [Chase] and you will lose 8 HP before the Chase*
- **Lv3**: [持续]：所有牌获得[再次行动]，但触发再次行动前自身减6生命  
  *[Continuous]: All cards gain [Chase] and you will lose 6 HP before the Chase*


### Phase 6 — 特殊 Special

#### 裂虚界元枪 (Void Split Spear) — id 99000105
- **Lv1**: 30攻 / 对方减4[命元]  
  *30 ATK / Opponent loses 4 [Destiny]*
- **Lv2**: 35攻 / 对方减7[命元]  
  *35 ATK / Opponent loses 7 [Destiny]*
- **Lv3**: 40攻 / 对方减10[命元]  
  *40 ATK / Opponent loses 10 [Destiny]*

#### 奇门锁妖塔 (Mysterious Gates Devil Seal Tower) — id 99000111
- **Lv1**: 造成25[伤害] / 对方无法行动1回合  
  *Deal 25 [DMG] / Opponent cannot act for 1 turns*
- **Lv2**: 造成32[伤害] / 对方无法行动1回合  
  *Deal 32 [DMG] / Opponent cannot act for 1 turns*
- **Lv3**: 造成32[伤害] / 对方无法行动2回合  
  *Deal 32 [DMG] / Opponent cannot act for 2 turns*

#### 噬灵虚兽 (Void The Spirit Consumer) — id 99000206
*持续 Continuous*  
- **Lv1**: [持续]：每回合吸取对方1[灵气]  
  *[Continuous]: At the beginning of your turn, steal 1 [Qi] from the opponent*
- **Lv2**: [持续]：每回合吸取对方2[灵气]  
  *[Continuous]: At the beginning of your turn, steal 2 [Qi] from the opponent*
- **Lv3**: [持续]：每回合吸取对方3[灵气]  
  *[Continuous]: At the beginning of your turn, steal 3 [Qi] from the opponent*

#### 幽冥虚魂犬 (Nether Void Canine) — id 99000211
*持续 Continuous*  
- **Lv1**: 造成1[伤害] / [持续]：对方下一张牌变为普通攻击，直到战斗结束  
  *Deal 1 [DMG] / [Continuous]: The next card played by the opponent will be changed to Normal Attack until the end of the battle*
- **Lv2**: 造成5[伤害] / [持续]：对方下一张牌变为普通攻击，直到战斗结束  
  *Deal 5 [DMG] / [Continuous]: The next card played by the opponent will be changed to Normal Attack until the end of the battle*
- **Lv3**: 造成9[伤害] / [持续]：对方下一张牌变为普通攻击，直到战斗结束  
  *Deal 9 [DMG] / [Continuous]: The next card played by the opponent will be changed to Normal Attack until the end of the battle*

#### 万象道种 (Myriad Manifestations Seed) — id 99000213
- **Lv1**: 10攻 / 卡组中每有1种不同境界的牌就追加1次攻击  
  *10 ATK / For each different phase card in your deck, make an additional attack*
- **Lv2**: 13攻 / 卡组中每有1种不同境界的牌就追加1次攻击  
  *13 ATK / For each different phase card in your deck, make an additional attack*
- **Lv3**: 16攻 / 卡组中每有1种不同境界的牌就追加1次攻击  
  *16 ATK / For each different phase card in your deck, make an additional attack*

#### 无名白鹿 (Nameless White Deer) — id 99000214
- **Lv1**: [灵气]+2 / [被动]：双方卡组前2格的持续牌在使用时改为[跳过]  
  *[Qi]+2 / [Passive]: When either player plays a Continuous Card within the first 2 slots of deck, [Skip] that card instead*
- **Lv2**: [灵气]+4 / [被动]：双方卡组前3格的持续牌在使用时改为[跳过]  
  *[Qi]+4 / [Passive]: When either player plays a Continuous Card within the first 3 slots of deck, [Skip] that card instead*
- **Lv3**: [灵气]+6 / [被动]：双方卡组前4格的持续牌在使用时改为[跳过]  
  *[Qi]+6 / [Passive]: When either player plays a Continuous Card within the first 4 slots of deck, [Skip] that card instead*


### Phase 0 — ?

#### 冥淬匕首 (Dark Quench Dagger) — id 99000215
- **Lv1**: 获得1层[内伤] / 2攻 / [击伤]：施加2层[内伤]（自身每有1层[内伤]，就多施加1层）  
  *Gain 1 [Internal Injury] / 2 ATK / [Injured]: Apply 2 [Internal Injury] (1 more for each stack of [Internal Injury] you have)*
- **Lv2**: 获得1层[内伤] / 6攻 / [击伤]：施加2层[内伤]（自身每有1层[内伤]，就多施加1层）  
  *Gain 1 [Internal Injury] / 6 ATK / [Injured]: Apply 2 [Internal Injury] (1 more for each stack of [Internal Injury] you have)*
- **Lv3**: 获得1层[内伤] / 10攻 / [击伤]：施加2层[内伤]（自身每有1层[内伤]，就多施加1层）  
  *Gain 1 [Internal Injury] / 10 ATK / [Injured]: Apply 2 [Internal Injury] (1 more for each stack of [Internal Injury] you have)*

#### 幻羽鹦 (Phantom Feather Parrot) — id 99000216
- **Lv1**: 生命+2 / 复制对方同一格牌的效果  
  *HP+2 / Copy the effect of the opponent's card in the same slot*
- **Lv2**: 生命+6 / 复制对方同一格牌的效果  
  *HP+6 / Copy the effect of the opponent's card in the same slot*
- **Lv3**: 生命+10 / 复制对方同一格牌的效果  
  *HP+10 / Copy the effect of the opponent's card in the same slot*
