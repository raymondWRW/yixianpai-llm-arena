# YiXianPai Immortal Fate Library (弈仙牌 天命图鉴)

Generated from `card counter with proxy` data: `fates.csv` (306 fates, current CN text per phase), `vendor/yisim-master/localization/1.5.8/immortal_fates.json` (EN text, v1.5.8), `characters.csv`, `tools/derivations_resolved.json` (天衍 derivations, appendix).

**How to read:** 天命 (Immortal Fates) are offered — pick 1 of 4 — each time you break through to a new realm. Most fates have a **version per phase**: the text under *Phase 2/3/4/5* is what the fate does when taken at that breakthrough (later = stronger). Fates with a single line are phase-independent. Types: **general** (any player), **sect** (only that sect's characters), **character** (that character's personal line, one per phase; the offer's first slot), **other** (large shared pool).

**Keyword glossary:** 命元 Destiny · 修为 Cultivation · 生命上限 Max HP · 体魄 Physique · 换牌机会 Exchange chance · 剑意 Sword Intent · 星力 Star Power · 卦象 Hexagram · 五行 Five Elements · 防 DEF · 灵气 Qi · 抽…牌 draw cards.

## Contents

- General fates (通用天命) — 13
- Sect fates — 七星阁 — 8
- Sect fates — 云灵剑宗 — 8
- Sect fates — 五行道盟 — 8
- Sect fates — 锻玄宗 — 8
- Character fates — 南宫生 (五行道盟) — 5
- Character fates — 叶冥冥 (锻玄宗) — 5
- Character fates — 吴策 (七星阁) — 5
- Character fates — 吾行之 (五行道盟) — 5
- Character fates — 姜袭明 (七星阁) — 5
- Character fates — 姬方生 (锻玄宗) — 5
- Character fates — 小布 (锻玄宗) — 5
- Character fates — 屠馗 (锻玄宗) — 5
- Character fates — 慕虎 (五行道盟) — 5
- Character fates — 曜灵 (七星阁) — 5
- Character fates — 李㵘 (锻玄宗) — 5
- Character fates — 杜伶鸳 (五行道盟) — 5
- Character fates — 林小月 (云灵剑宗) — 5
- Character fates — 炎尘 (七星阁) — 5
- Character fates — 炎雪 (云灵剑宗) — 5
- Character fates — 牧逸风 (云灵剑宗) — 5
- Character fates — 祁忘忧 (五行道盟) — 5
- Character fates — 花沁蕊 (五行道盟) — 5
- Character fates — 谭舒雁 (七星阁) — 5
- Character fates — 陆剑心 (云灵剑宗) — 5
- Character fates — 风绪 (七星阁) — 5
- Character fates — 黎承云 (云灵剑宗) — 5
- Character fates — 龙瑶 (云灵剑宗) — 5
- Other fates (shared pool) — 146
- Appendix: 天衍 Derivations

## General fates (通用天命)

#### 锻体 (Bodybuilding) — id 1
- **Phase 2**: 生命上限+5  
  *Max HP+5*
- **Phase 3**: 生命上限+7  
  *Max HP+7*
- **Phase 4**: 生命上限+10  
  *Max HP+10*
- **Phase 5**: 生命上限+12  
  *Max HP+12*

#### 感悟丛生 (Mental Perception) — id 4
- **Phase 2**: 抽1张门派牌  
  *Draw 1 Sect Card(s)*
- **Phase 3**: 抽2张门派牌  
  *Draw 2 Sect Card(s)*
- **Phase 4**: 抽2张门派牌  
  *Draw 2 Sect Card(s)*
- **Phase 5**: 抽3张门派牌  
  *Draw 3 Sect Card(s)*

#### 善假于物 (Tool Governor) — id 5
- **Phase 2**: 抽1张副职牌  
  *Draw 1 Side Job Card(s)*
- **Phase 3**: 抽2张副职牌  
  *Draw 2 Side Job Card(s)*
- **Phase 4**: 抽2张副职牌  
  *Draw 2 Side Job Card(s)*
- **Phase 5**: 抽3张副职牌  
  *Draw 3 Side Job Card(s)*

#### 变换之道 (The Way of Adaptation) — id 6
- **Phase 2**: 换牌机会+6；换牌机会储存上限+6  
  *Exchange Card Chance+6; Exchange Card Chance storage limit + 6*
- **Phase 3**: 换牌机会+8；换牌机会储存上限+8  
  *Exchange Card Chance+8; Exchange Card Chance storage limit + 8*
- **Phase 4**: 换牌机会+10；换牌机会储存上限+10  
  *Exchange Card Chance+10; Exchange Card Chance storage limit + 10*
- **Phase 5**: 换牌机会+12；换牌机会储存上限+12  
  *Exchange Card Chance+12; Exchange Card Chance storage limit + 12*

#### 休养生息 (Recuperate) — id 8
- **Phase 2**: [命元]+14  
  *[Destiny]+14*
- **Phase 3**: [命元]+18  
  *[Destiny]+18*
- **Phase 4**: [命元]+24  
  *[Destiny]+24*
- **Phase 5**: [命元]+30  
  *[Destiny]+30*

#### 云巅雷劫 (Thunder Tribulation) — id 9
- **Phase 2**: 命元减14（最低减到1）；抽2张牌  
  *Lose 14 Destiny (minimum to 1); Draw 2 cards*
- **Phase 3**: 命元减14（最低减到1）；抽3张牌  
  *Lose 14 Destiny (minimum to 1); Draw 3 cards*
- **Phase 4**: 命元减14（最低减到1）；抽4张牌  
  *Lose 14 Destiny (minimum to 1); Draw 4 cards*
- **Phase 5**: 命元减14（最低减到1）；抽5张牌  
  *Lose 14 Destiny (minimum to 1); Draw 5 cards*

#### 顿悟 (Epiphany) — id 12
- **Phase 2**: 修为+2；换牌机会减3  
  *Cultivation+2; Exchange Card Chance decrease 3*
- **Phase 3**: 修为+3；换牌机会减3  
  *Cultivation+3; Exchange Card Chance decrease 3*
- **Phase 4**: 修为+4；换牌机会减3  
  *Cultivation+4; Exchange Card Chance decrease 3*
- **Phase 5**: 修为+6；换牌机会减3  
  *Cultivation+6; Exchange Card Chance decrease 3*

#### 储纳灵气 (Store Qi) — id 13
- **Phase 2**: 战斗开始时加1[灵气]  
  *At the beginning of the battle add 1 [Qi]*
- **Phase 3**: 战斗开始时加1[灵气]  
  *At the beginning of the battle add 1 [Qi]*
- **Phase 4**: 战斗开始时加2[灵气]  
  *At the beginning of the battle add 2 [Qi]*
- **Phase 5**: 战斗开始时加3[灵气]  
  *At the beginning of the battle add 3 [Qi]*

#### 机缘造化 (Fortunes and Luck) — id 53
- **Phase 2**: 获得1张筑基期机缘牌  
  *Gain 1 Foundation Phase Fortunes Card*
- **Phase 3**: 获得1张金丹期机缘牌  
  *Gain 1 Virtuoso Phase Fortunes Card*
- **Phase 4**: 获得1张元婴期机缘牌  
  *Gain 1 Immortality Phase Fortunes Card*
- **Phase 5**: 获得1张化神期机缘牌  
  *Gain 1 Incarnation Phase Fortunes Card*

#### 斩道 (Shattered Dao) — id 56
- **Phase 2**: 修为减6；抽6张牌  
  *Cultivation-6; Draw 6 Cards*
- **Phase 3**: 修为减7；抽7张牌  
  *Cultivation-7; Draw 7 Cards*
- **Phase 4**: 修为减8；抽8张牌  
  *Cultivation-8; Draw 8 Cards*
- **Phase 5**: 修为减10；抽9张牌  
  *Cultivation-10; Draw 9 Cards*

#### 陨星淬体 (Meteor Quench) — id 59
- **Phase 2**: 命元减4（最低减到1）；生命上限+6  
  *Lose 4 Destiny (minimum to 1); Max HP+6*
- **Phase 3**: 命元减6（最低减到1）；生命上限+9  
  *Lose 6 Destiny (minimum to 1); Max HP+9*
- **Phase 4**: 命元减8（最低减到1）；生命上限+13  
  *Lose 8 Destiny (minimum to 1); Max HP+13*
- **Phase 5**: 命元减10（最低减到1）；生命上限+17  
  *Lose 10 Destiny (minimum to 1); Max HP+17*

#### 稳固根基 (Solid Foundation) — id 118
- **Phase 2**: 修为减1；体魄上限减1；命元+6；生命上限+6  
  *Cultivation-1; Physique Cap-1; Destiny+6; Max HP+6*
- **Phase 3**: 修为减1；体魄上限减1；命元+8；生命上限+8  
  *Cultivation-1; Physique Cap-1; Destiny+8; Max HP+8*
- **Phase 4**: 修为减2；体魄上限减2；命元+12；生命上限+12  
  *Cultivation-2; Physique Cap-2; Destiny+12; Max HP+12*
- **Phase 5**: 修为减3；体魄上限减3；命元+15；生命上限+15  
  *Cultivation-3; Physique Cap-3; Destiny+15; Max HP+15*

#### 副职兼修 (Additional Side Job) — id 188
- **Phase 2**: 修为+1；选择一个副职业，牌池中额外加入该副职业筑基期及以上的牌  
  *Cultivation+1; / Choose a Side Job, and add cards of that Side Job at Foundation Phase or above to your card pool.*
- **Phase 3**: 修为+2；选择一个副职业，牌池中额外加入该副职业金丹期及以上的牌  
  *Cultivation+2; / Choose a Side Job, and add cards of that Side Job at Virtuoso Phase or above to your card pool.*
- **Phase 4**: 修为+2；选择一个副职业，牌池中额外加入该副职业元婴期及以上的牌  
  *Cultivation+2; / Choose a Side Job, and add cards of that Side Job at Immortality Phase or above to your card pool.*
- **Phase 5**: 修为+2；选择一个副职业，牌池中额外加入该副职业化神期的牌  
  *Cultivation+2; / Choose a Side Job, and add cards of that Side Job at Incarnation Phase or above to your card pool.*


## Sect fates — 七星阁

#### 卜卦 (Divination) — id 30
- **Phase 2**: 战斗开始时加1[卦象]  
  *At the beginning of the battle, add 1 [Hexagram]*
- **Phase 3**: 战斗开始时加1[卦象]  
  *At the beginning of the battle, add 1 [Hexagram]*
- **Phase 4**: 战斗开始时加2[卦象]  
  *At the beginning of the battle, add 2 [Hexagram]*
- **Phase 5**: 战斗开始时加3[卦象]  
  *At the beginning of the battle, add 3 [Hexagram]*

#### 观星 (Stargaze) — id 31
- **Phase 2**: 命元减6；战斗开始时加1[星力]  
  *Lose 6 Destiny; At the beginning of the battle, add 1 stack of [Star Power]*
- **Phase 3**: 战斗开始时加1[星力]  
  *At the beginning of the battle, add 1 stack of [Star Power]*
- **Phase 4**: 命元+6；战斗开始时加1[星力]  
  *Destiny+6; At the beginning of the battle, add 1 stack of [Star Power]*
- **Phase 5**: 命元+12；战斗开始时加1[星力]  
  *Destiny+12; At the beginning of the battle, add 1 stack of [Star Power]*

#### 星弈传承 (Inheritance of Astral Move) — id 58
- **Phase 2**: 获得1张“星弈”牌  
  *Gain 1 "Astral Move" card(s)*
- **Phase 3**: 获得2张“星弈”牌  
  *Gain 2 "Astral Move" card(s)*
- **Phase 4**: 获得2张“星弈”牌  
  *Gain 2 "Astral Move" card(s)*
- **Phase 5**: 获得3张“星弈”牌  
  *Gain 3 "Astral Move" card(s)*

#### 后发制人 (Post Strike) — id 71
- **Phase 2**: 含[后招]效果的牌在首次使用时加2防和2生命及上限  
  *Cards with [Post Action] effects will add 2 [DEF], HP and Max HP on their first play*
- **Phase 3**: 含[后招]效果的牌在首次使用时加3防和3生命及上限  
  *Cards with [Post Action] effects will add 3 [DEF], HP and Max HP on their first play*
- **Phase 4**: 含[后招]效果的牌在首次使用时加4防和4生命及上限  
  *Cards with [Post Action] effects will add 4 [DEF], HP and Max HP on their first play*
- **Phase 5**: 含[后招]效果的牌在首次使用时加5防和5生命及上限  
  *Cards with [Post Action] effects will add 5 [DEF], HP and Max HP on their first play*

#### 易数化劫 (Changes Of Catastrophe) — id 72
- **Phase 2**: 每当战斗失败时换牌机会+1  
  *When you are defeated in the battle, Exchange Card Chance+1*
- **Phase 3**: 每当战斗失败时换牌机会+2  
  *When you are defeated in the battle, Exchange Card Chance+2*
- **Phase 4**: 每当战斗失败时换牌机会+3且修为+1  
  *When you are defeated in the battle, Exchange Card Chance+3 and Cultivation+1*
- **Phase 5**: 每当战斗失败时换牌机会+5且修为+2  
  *When you are defeated in the battle, Exchange Card Chance+5 and Cultivation+2*

#### 星蚀 (Astral Eclipse) — id 103
- **Phase 2**: 战斗中对方首次获得[负面状态]时，额外加1层  
  *The first time your opponent gains [Debuff] in each battle, apply 1 more stack(s)*
- **Phase 3**: 战斗中对方首次获得[负面状态]时，额外加1层  
  *The first time your opponent gains [Debuff] in each battle, apply 1 more stack(s)*
- **Phase 4**: 战斗中对方首次获得[负面状态]时，额外加2层  
  *The first time your opponent gains [Debuff] in each battle, apply 2 more stack(s)*
- **Phase 5**: 战斗中对方首次获得[负面状态]时，额外加3层  
  *The first time your opponent gains [Debuff] in each battle, apply 3 more stack(s)*

#### 雷霆传承 (Inheritance of Thunder) — id 117
- **Phase 2**: 获得1张名字含“雷”的牌  
  *Gain 1 card(s) with a name containing "Thunder"*
- **Phase 3**: 获得2张名字含“雷”的牌  
  *Gain 2 card(s) with a name containing "Thunder"*
- **Phase 4**: 命元减10（最低减到1）；获得3张名字含“雷”的牌  
  *Lose 10 Destiny (minimum to 1); Gain 3 card(s) with a name containing "Thunder"*
- **Phase 5**: 命元减10（最低减到1）；获得4张名字含“雷”的牌  
  *Lose 10 Destiny (minimum to 1); Gain 4 card(s) with a name containing "Thunder"*

#### 妙手回春 (Rejuvenation) — id 120
- **Phase 2**: 生命上限+3；战斗中每次加生命时先加3临时生命上限  
  *Max HP+3; Each time you add HP in the battle, add 3 temporary Max HP first*
- **Phase 3**: 生命上限+4；战斗中每次加生命时先加4临时生命上限  
  *Max HP+4; Each time you add HP in the battle, add 4 temporary Max HP first*
- **Phase 4**: 生命上限+5；战斗中每次加生命时先加5临时生命上限  
  *Max HP+5; Each time you add HP in the battle, add 5 temporary Max HP first*
- **Phase 5**: 生命上限+6；战斗中每次加生命时先加6临时生命上限  
  *Max HP+6; Each time you add HP in the battle, add 6 temporary Max HP first*


## Sect fates — 云灵剑宗

#### 剑韵修炼 (Sword Rhyme Cultivate) — id 16
- **Phase 2**: 战斗开始时加1[剑意]  
  *At the beginning of the battle add 1 stack(s) of [Sword Intent]*
- **Phase 3**: 修为+1；战斗开始时加1[剑意]  
  *Cultivation+1; At the beginning of the battle add 1 stack(s) of [Sword Intent]*
- **Phase 4**: 修为+2；战斗开始时加1[剑意]  
  *Cultivation+2; At the beginning of the battle add 1 stack(s) of [Sword Intent]*
- **Phase 5**: 修为+2；战斗开始时加2[剑意]  
  *Cultivation+2; At the beginning of the battle add 2 stack(s) of [Sword Intent]*

#### 云剑传承 (Inheritance of Cloud Sword) — id 54
- **Phase 2**: 获得1张“云剑”牌  
  *Gain 1 "Cloud Sword" Card(s)*
- **Phase 3**: 获得2张“云剑”牌  
  *Gain 2 "Cloud Sword" Card(s)*
- **Phase 4**: 获得2张“云剑”牌  
  *Gain 2 "Cloud Sword" Card(s)*
- **Phase 5**: 获得3张“云剑”牌  
  *Gain 3 "Cloud Sword" Card(s)*

#### 灵剑传承 (Inheritance of Spirit Sword) — id 55
- **Phase 2**: 获得1张名字含“灵剑”的牌  
  *Gain 1 Card(s) with the name contains "Spirit Sword"*
- **Phase 3**: 获得2张名字含“灵剑”的牌  
  *Gain 2 Card(s) with the name contains "Spirit Sword"*
- **Phase 4**: 获得2张名字含“灵剑”的牌  
  *Gain 2 Card(s) with the name contains "Spirit Sword"*
- **Phase 5**: 获得3张名字含“灵剑”的牌  
  *Gain 3 Card(s) with the name contains "Spirit Sword"*

#### 剑阵守护 (Sword Formation Guard) — id 57
- **Phase 2**: 使用卡组第一格的牌时加1[防]，且获得1层[水月剑阵]效果（自身下1回合开始时[防]不减半）  
  *When playing the card in your deck's first slot, gain 1 [DEF] and gain 1 stack of [Moon Water Sword Formation] effect (your DEF will not be halved at the beginning of the next turn)*
- **Phase 3**: 使用卡组第一格的牌时加3[防]，且获得1层[水月剑阵]效果（自身下1回合开始时[防]不减半）  
  *When playing the card in your deck's first slot, gain 3 [DEF] and gain 1 stack of [Moon Water Sword Formation] effect (your DEF will not be halved at the beginning of the next turn)*
- **Phase 4**: 使用卡组第一格的牌时加6[防]，且获得1层[水月剑阵]效果（自身下1回合开始时[防]不减半）  
  *When playing the card in your deck's first slot, gain 6 [DEF] and gain 1 stack of [Moon Water Sword Formation] effect (your DEF will not be halved at the beginning of the next turn)*
- **Phase 5**: 使用卡组第一格的牌时加9[防]，且获得1层[水月剑阵]效果（自身下1回合开始时[防]不减半）  
  *When playing the card in your deck's first slot, gain 9 [DEF] and gain 1 stack of [Moon Water Sword Formation] effect (your DEF will not be halved at the beginning of the next turn)*

#### 云之道 (Rule Of The Cloud) — id 69
- **Phase 2**: 每次使用“云剑”时加1防  
  *Each time you play "Cloud Sword" card, add 1 DEF*
- **Phase 3**: 每次使用“云剑”时加2防  
  *Each time you play "Cloud Sword" card, add 2 DEF*
- **Phase 4**: 每次使用“云剑”时加2防  
  *Each time you play "Cloud Sword" card, add 2 DEF*
- **Phase 5**: 每次使用“云剑”时加3防  
  *Each time you play "Cloud Sword" card, add 3 DEF*

#### 狂之执念 (Mad Obsession) — id 70
- **Phase 2**: 获得1张“狂剑”牌  
  *Gain 1 "Unrestrained Sword" Card(s)*
- **Phase 3**: 获得2张“狂剑”牌  
  *Gain 2 "Unrestrained Sword" Card(s)*
- **Phase 4**: 获得1张“狂剑”牌；战斗开始时算作已用过1次“狂剑”  
  *Gain 1 "Unrestrained Sword" Card(s); At the beginning of the battle, it counts as a "Unrestrained Sword" has been played*
- **Phase 5**: 获得2张“狂剑”牌；战斗开始时算作已用过1次“狂剑”  
  *Gain 2 "Unrestrained Sword" Card(s); At the beginning of the battle, it counts as a "Unrestrained Sword" has been played*

#### 剑阵传承 (Inheritance of Sword Formation) — id 116
- **Phase 2**: 获得1张“剑阵”牌  
  *Gain 1 "Sword Formation" card(s)*
- **Phase 3**: 获得2张“剑阵”牌  
  *Gain 2 "Sword Formation" card(s)*
- **Phase 4**: 获得2张“剑阵”牌  
  *Gain 2 "Sword Formation" card(s)*
- **Phase 5**: 获得3张“剑阵”牌  
  *Gain 3 "Sword Formation" card(s)*

#### 剑池问心 (Sword Pool The Heart Ask) — id 119
- **Phase 2**: 命元减4（最低减到1）；获得1张名字含“剑”的2级牌  
  *Lose 4 Destiny (minimum to 1); Gain 1 Level 2 card(s) with a name containing "Sword"*
- **Phase 3**: 命元减8（最低减到1）；获得2张名字含“剑”的2级牌  
  *Lose 8 Destiny (minimum to 1); Gain 2 Level 2 card(s) with a name containing "Sword"*
- **Phase 4**: 命元减9（最低减到1）；获得2张名字含“剑”的2级牌（筑基期以上）  
  *Lose 9 Destiny (minimum to 1); Gain 2 Level 2 card(s) with a name containing "Sword" (Above Foundation Phase)*
- **Phase 5**: 命元减10（最低减到1）；获得3张名字含“剑”的2级牌（金丹期以上）  
  *Lose 10 Destiny (minimum to 1); Gain 3 Level 2 card(s) with a name containing "Sword" (Above Virtuoso Phase)*


## Sect fates — 五行道盟

#### 金灵传承 (Inheritance of Metal Spirit) — id 73
- **Phase 2**: 获得1张“金灵”牌  
  *Gain 1 "Metal Spirit" Card(s)*
- **Phase 3**: 获得2张“金灵”牌  
  *Gain 2 "Metal Spirit" Card(s)*
- **Phase 4**: 获得2张“金灵”牌  
  *Gain 2 "Metal Spirit" Card(s)*
- **Phase 5**: 获得3张“金灵”牌  
  *Gain 3 "Metal Spirit" Card(s)*

#### 木灵传承 (Inheritance of Wood Spirit) — id 74
- **Phase 2**: 获得1张“木灵”牌  
  *Gain 1 "Wood Spirit" Card(s)*
- **Phase 3**: 获得2张“木灵”牌  
  *Gain 2 "Wood Spirit" Card(s)*
- **Phase 4**: 获得2张“木灵”牌  
  *Gain 2 "Wood Spirit" Card(s)*
- **Phase 5**: 获得3张“木灵”牌  
  *Gain 3 "Wood Spirit" Card(s)*

#### 水灵传承 (Inheritance of Water Spirit) — id 75
- **Phase 2**: 获得1张“水灵”牌  
  *Gain 1 "Water Spirit" Card(s)*
- **Phase 3**: 获得2张“水灵”牌  
  *Gain 2 "Water Spirit" Card(s)*
- **Phase 4**: 获得2张“水灵”牌  
  *Gain 2 "Water Spirit" Card(s)*
- **Phase 5**: 获得3张“水灵”牌  
  *Gain 3 "Water Spirit" Card(s)*

#### 火灵传承 (Inheritance of Fire Spirit) — id 76
- **Phase 2**: 获得1张“火灵”牌  
  *Gain 1 "Fire Spirit" Card(s)*
- **Phase 3**: 获得2张“火灵”牌  
  *Gain 2 "Fire Spirit" Card(s)*
- **Phase 4**: 获得2张“火灵”牌  
  *Gain 2 "Fire Spirit" Card(s)*
- **Phase 5**: 获得3张“火灵”牌  
  *Gain 3 "Fire Spirit" Card(s)*

#### 土灵传承 (Inheritance of Earth Spirit) — id 77
- **Phase 2**: 获得1张“土灵”牌  
  *Gain 1 "Earth Spirit" Card(s)*
- **Phase 3**: 获得2张“土灵”牌  
  *Gain 2 "Earth Spirit" Card(s)*
- **Phase 4**: 获得2张“土灵”牌  
  *Gain 2 "Earth Spirit" Card(s)*
- **Phase 5**: 获得3张“土灵”牌  
  *Gain 3 "Earth Spirit" Card(s)*

#### 五行循环 (Cycle Of Five Elements) — id 102
- **Phase 2**: 每当使用[五行]牌时，若被上一张使用的牌[五行]相生，则加3防  
  *When playing a card in the order of [Five Element Generating Interaction], add 3 DEF*
- **Phase 3**: 每当使用[五行]牌时，若被上一张使用的牌[五行]相生，则加1灵气  
  *When playing a card in the order of [Five Element Generating Interaction], add 1 Qi*
- **Phase 4**: 每当使用[五行]牌时，若被上一张使用的牌[五行]相生，则加4生命及上限  
  *When playing a card in the order of [Five Element Generating Interaction], add 4 HP and Max HP*
- **Phase 5**: 每当使用[五行]牌时，若被上一张使用的牌[五行]相生，则加4[锋锐]  
  *When playing a card in the order of [Five Element Generating Interaction], add 4 Penetrate*

#### 相生相成 (Mutual Growth) — id 127
- **Phase 2**: 以[五行相生]顺序使用牌时，临时升级被相生的牌，直到战斗结束（每场战斗限1次)  
  *When playing a card in the order of [Five Element Generating Interaction], upgrade the card until the end of the battle (for each battle trigger only 1 time(s))*
- **Phase 3**: 以[五行相生]顺序使用牌时，临时升级被相生的牌，直到战斗结束（每场战斗限1次)  
  *When playing a card in the order of [Five Element Generating Interaction], upgrade the card until the end of the battle (for each battle trigger only 1 time(s))*
- **Phase 4**: 以[五行相生]顺序使用牌时，临时升级被相生的牌，直到战斗结束（每场战斗限2次)  
  *When playing a card in the order of [Five Element Generating Interaction], upgrade the card until the end of the battle (for each battle trigger only 2 time(s))*
- **Phase 5**: 以[五行相生]顺序使用牌时，临时升级被相生的牌，直到战斗结束（每场战斗限3次)  
  *When playing a card in the order of [Five Element Generating Interaction], upgrade the card until the end of the battle (for each battle trigger only 3 time(s))*

#### 五行专一 (Concentrated Element) — id 128
- **Phase 2**: 若卡组中仅含一种[五行]，战斗中加3[速度]（修为加速度合计高的一方先行动）  
  *If there are [Five Elements] card in your deck and only contains one Element, Add 3 [Speed] (Cultivation+Speed higher player act first)*
- **Phase 3**: 若卡组中仅含一种[五行]，战斗中加4[速度]（修为加速度合计高的一方先行动）  
  *If there are [Five Elements] card in your deck and only contains one Element, Add 4 [Speed] (Cultivation+Speed higher player act first)*
- **Phase 4**: 若卡组中仅含一种[五行]，战斗中加5[速度]（修为加速度合计高的一方先行动）  
  *If there are [Five Elements] card in your deck and only contains one Element, Add 5 [Speed] (Cultivation+Speed higher player act first)*
- **Phase 5**: 若卡组中仅含一种[五行]，战斗中加6[速度]（修为加速度合计高的一方先行动）  
  *If there are [Five Elements] card in your deck and only contains one Element, Add 6 [Speed] (Cultivation+Speed higher player act first)*


## Sect fates — 锻玄宗

#### 崩拳传承 (Inheritance of Crash Fist) — id 143
- **Phase 2**: 获得1张“崩拳”牌  
  *Gain 1 "Crash Fist" Card(s)*
- **Phase 3**: 获得2张“崩拳”牌  
  *Gain 2 "Crash Fist" Card(s)*
- **Phase 4**: 获得2张“崩拳”牌  
  *Gain 2 "Crash Fist" Card(s)*
- **Phase 5**: 获得3张“崩拳”牌  
  *Gain 3 "Crash Fist" Card(s)*

#### 炼体传承 (Inheritance of Physique Building) — id 144
- **Phase 2**: 获得1张加[体魄]的牌  
  *Gain 1 Card(s) of adding Physique*
- **Phase 3**: 获得2张加[体魄]的牌  
  *Gain 2 Card(s) of adding Physique*
- **Phase 4**: 获得2张加[体魄]的牌  
  *Gain 2 Card(s) of adding Physique*
- **Phase 5**: 获得3张加[体魄]的牌  
  *Gain 3 Card(s) of adding Physique*

#### 气势充沛 (Full of Force) — id 145
- **Phase 2**: 战斗开始时加1[气势]  
  *Add 1 [Force] at the start of each battle*
- **Phase 3**: 战斗开始时加1[气势]和1气势上限  
  *Add 1 [Force] and 1 Force Cap at the start of each battle*
- **Phase 4**: 战斗开始时加1[气势]和2气势上限  
  *Add 1 [Force] and 2 Force Cap at the start of each battle*
- **Phase 5**: 战斗开始时加1[气势]和3气势上限  
  *Add 1 [Force] and 3 Force Cap at the start of each battle*

#### 体修入道 (Physique Master) — id 146
- **Phase 2**: 体魄上限+2；[体魄]+5  
  *Physique Cap + 2; [Physique] + 5*
- **Phase 3**: 体魄上限+3；[体魄]+6  
  *Physique Cap + 3; [Physique] + 6*
- **Phase 4**: 体魄上限+4；[体魄]+8  
  *Physique Cap + 4; [Physique] + 8*
- **Phase 5**: 体魄上限+8；[体魄]+12  
  *Physique Cap + 8; [Physique] + 12*

#### 再生之躯 (Regenerating Body) — id 149
- **Phase 2**: 每次使用卡组第一格的牌时加1[体魄]和1生命  
  *When playing the card in your deck's first slot, add 1 [Physique] and 1 HP*
- **Phase 3**: 每次使用卡组第一格的牌时加1[体魄]和2生命  
  *When playing the card in your deck's first slot, add 1 [Physique] and 2 HP*
- **Phase 4**: 每次使用卡组第一格的牌时加2[体魄]和4生命  
  *When playing the card in your deck's first slot, add 2 [Physique] and 4 HP*
- **Phase 5**: 每次使用卡组第一格的牌时加2[体魄]和6生命  
  *When playing the card in your deck's first slot, add 2 [Physique] and 6 HP*

#### 冥心烙印 (Mark of Dark Heart) — id 150
- **Phase 2**: 战斗开始时，自身加1层[内伤]和1层[恢复]  
  *At the start of combat, gain 1 [Internal Injury] and 1 [Regeneration]*
- **Phase 3**: 战斗开始时，自身加2层[内伤]和2层[恢复]  
  *At the start of combat, gain 2 [Internal Injury] and 2 [Regeneration]*
- **Phase 4**: 战斗开始时，自身加2层[内伤]和2层[恢复]  
  *At the start of combat, gain 2 [Internal Injury] and 2 [Regeneration]*
- **Phase 5**: 战斗开始时，自身加3层[内伤]和3层[恢复]  
  *At the start of combat, gain 3 [Internal Injury] and 3 [Regeneration]*

#### 历战不屈 (Unbowed through battle) — id 175
- **Phase 2**: 生命上限+2；每次战斗失败后永久加1生命上限  
  *Max HP + 2; Permanently gain 1 Max HP after each battle you lose*
- **Phase 3**: 生命上限+4；每次战斗失败后永久加1生命上限  
  *Max HP + 4; Permanently gain 1 Max HP after each battle you lose*
- **Phase 4**: 生命上限+7；每次战斗失败后永久加2生命上限  
  *Max HP + 7; Permanently gain 2 Max HP after each battle you lose*
- **Phase 5**: 生命上限+9；每次战斗失败后永久加4生命上限  
  *Max HP + 9; Permanently gain 4 Max HP after each battle you lose*

#### 筋骨健壮 (Firmness Body) — id 176
- **Phase 2**: 体魄上限+2；战斗开始时，每有10[体魄]加1生命  
  *Physique Cap + 2; At the start of each battle, gain 1 HP for every 10 [Physique]*
- **Phase 3**: 体魄上限+2；战斗开始时，每有9[体魄]加1生命  
  *Physique Cap + 2; At the start of each battle, gain 1 HP for every 9 [Physique]*
- **Phase 4**: 体魄上限+3；战斗开始时，每有7[体魄]加1生命  
  *Physique Cap + 3; At the start of each battle, gain 1 HP for every 7 [Physique]*
- **Phase 5**: 体魄上限+4；战斗开始时，每有6[体魄]加1生命  
  *Physique Cap + 4; At the start of each battle, gain 1 HP for every 6 [Physique]*


## Character fates — 南宫生 (五行道盟)

#### 秘印亲和 (Secret Seal Affinity) — id 136 · character phase 1
- 生命上限减2 / 每次突破境界时随机获得1张五行“秘印”（[木灵秘印]/[火灵秘印]/[土灵秘印]/[金灵秘印]/[水灵秘印]），突破至化神期改为自选一张（随机1张为2级）  
  *Max HP reduced by 2. / Gain a random Five Elements "Secret Seal" ([Wood Spirit Secret Seal]/[Fire Spirit Secret Seal]/[Earth Spirit Secret Seal]/[Metal Spirit Secret Seal]/[Water Spirit Secret Seal]) each time you breakthrough the Phase. When you breakthrough to the Incarnation Phase, this changes to selecting one (a random one is Level 2)*

#### 相生之火 (Fire Spirit Generation) — id 137 · character phase 2
- 生命上限减1 / 火灵与其他五行（木/土/金/水）互相视作[相生]  
  *Max HP reduced by 1. / The Fire Spirit and other Five Element (Wood/Earth/Metal/Water) are considered to have a [Five Element Generating Interaction] order mutually.*

#### 五行爆炎 (Five Elements Explosion) — id 138 · character phase 3
- 生命上限减4 / 战斗中每次激活任意五行时，减对方3生命及上限  
  *Max HP reduced by 4. / When you [Activate] any [Five Elements] in battle, reduce the opponent's HP and Max HP by 3*

#### 焰魂归复 (Flame Soul Rebirth) — id 139 · character phase 4
- 生命上限减15 / 每场战斗中生命首次≤0时，复活并将生命及上限变为15  
  *Max HP reduced by 15. / The first time your HP reaching or dropping below 0 in each battle, revive with 15 HP and Max HP.*

#### 疾燃咒印 (Swift Burning Seal) — id 140 · character phase 5
- 生命上限减18 / 每场战斗限1次，使用名字含“印”的牌时将其[消耗]并[再次行动]  
  *Max HP reduced by 18. / The following effect can only be triggered once per battle. When you play a card with "Seal" in its name, consume the card, and [Chase].*


## Character fates — 叶冥冥 (锻玄宗)

#### 阴晴圆缺 (The moon waxes and wanes) — id 178 · character phase 1
- 奇数轮开始时多加1次换牌机会，偶数轮战斗中[速度]+3  
  *At the start of odd-numbered rounds, gain 1 more Exchange Chance. During even-numbered rounds, increase 3 [Speed] in battle.*

#### 入冥 (Entering Styx) — id 179 · character phase 2
- 每场战斗开始时获得1层[冥]状态  
  *At the beginning of each battle, gain 1 stack of [Styx]*

#### 疯魔 (Gone Crazy) — id 180 · character phase 3
- 获得1张[疯魔]  
  *Gain 1 [Gone Crazy]*

#### 冥夜 (Styx Night) — id 181 · character phase 4
- 获得1张[崩拳·冥夜]  
  *Gain 1 [Crash Fist - Styx Night]*

#### 冥月蟾光 (Styx Moon's Glow) — id 182 · character phase 5
- 获得1张[冥月蟾光]  
  *Gain 1 [Styx Moon's Glow]*


## Character fates — 吴策 (七星阁)

#### 算无遗策 (Perfectly Planned) — id 104 · character phase 1
- 游戏开始时获得1张[算无遗策]。 / 每次突破时升级[算无遗策]。 / [算无遗策]被炼化时加12命元，被置换时加4换牌机会。  
  *Initially gain [Perfectly Planned]. / [Perfectly Planned] will be upgraded when you break through the Phase. / If you Absorb it, add 12 Destiny. / If you Exchange it, add 4 Card Exchange Chance.*

#### 以逸待劳 (Rest and Outwit) — id 142 · character phase 2
- 修为+1 / 战斗中因灵气不足而无法出牌时，从加1灵气改为加3[灵气]和3[卦象]  
  *Cultivation+1 / When you cannot play a card due to lack of [Qi] in battle, you will add 3 [Qi] and 3 [Hexagram] instead of adding 1 [Qi]*

#### 计出万全 (Best Choice) — id 141 · character phase 3
- 换牌机会+3 / 每轮首次换牌将优先换出自身境界的牌  
  *Exchange Card Chance+3 / The first time you Exchange Card in each round, you will priority get the card of your Phase*

#### 瞒天过海 (Act Underhand) — id 108 · character phase 4
- [后招]效果在首次使用时有1%概率触发（可被[卦象]加成为100%）  
  *The [Post Action] effect has a 1% chance to trigger on first use (can be added to 100% by [Hexagram])*

#### 星月折扇 (Star Moon Folding Fan) — id 106 · character phase 5
- 换牌机会减3 / 卡组第7格永久成为[星位] / 获得1张[星月折扇]  
  *Lose 3 Exchange Card Chance. / The seventh slot in your deck becomes [Star Point]. / Gain 1 [Star Moon Folding Fan].*


## Character fates — 吾行之 (五行道盟)

#### 战斗历练 (Battle Experience) — id 80 · character phase 1
- 每次战斗胜利后加2换牌机会  
  *Add 2 Exchange Card Chance for each victory battle*

#### 五行印记 (Mark Of Five Elements) — id 82 · character phase 2
- 战斗开始时获得效果：下1次使用[五行]牌时，先[激活]其所属[五行]  
  *At the beginning of the battle you will gain: When you play [Five Elements] next time, activate the [Five Elements] of the card first*

#### 悠然葫芦 (Gourd Of Leisurely) — id 81 · character phase 3
- 获得1张[悠然葫芦]  
  *Gain 1 [Gourd Of Leisurely]*

#### 五行化身 (Avater Of Five Elements) — id 83 · character phase 4
- 下次命元耗尽时，保留1点命元不被淘汰，并减5修为抽5张不同五行的牌（元婴期以上）  
  *When the next Destiny is exhausted, keep 1 Destiny and not be eliminated, then lose 5 Cultivation and draw 5 different Five Elements cards (Above Immortality Phase)*

#### 五行传承 (Inheritance of Five Elements) — id 123 · character phase 5
- 获得1张[五行传承]  
  *Gain 1 [Inheritance of Five Elements]*


## Character fates — 姜袭明 (七星阁)

#### 运筹帷幄 (Strategize) — id 48 · character phase 1
- 首轮多抽1张牌；每轮战斗后少加1点修为，多抽1张牌。  
  *Draw 1 extra card in the first round; gain 1 less Cultivation and draw 1 extra card after each battle.*

#### 占星 (Astrology) — id 61 · character phase 2
- 修为+1 / 战斗中加[卦象]时，若[星力]为0，则加1[星力]。  
  *Cultivation+1 / Whenever you gain [Hexagram], if [Star Power] is 0, then add 1 [Star Power].*

#### 星爆术 (Starburst) — id 50 · character phase 3
- 修为减1，获得2张[星爆术]  
  *Lose 1 Cultivation, gain 2 [Starburst]*

#### 七星定魂 (Heptastar Soulstat) — id 52 · character phase 4
- 若卡组第8格空着，则战斗时放入[七星定魂]  
  *If the 8th slot of deck is empty, temporarily generate [Heptastar Soulstat] to the slot in battle*

#### 布星问卦 (Astral Divination Hexagram) — id 62 · character phase 5
- 修为减1，获得1张“星弈”牌（金丹期以上）； / 战斗中每次使用“星弈”牌时加1[卦象]  
  *Lose 1 Cultivation and gain 1 "Astral Move" Card (Above Virtuoso Phase); / When playing a "Astral Move" card, add 1 [Hexagram]*


## Character fates — 姬方生 (锻玄宗)

#### 禅心锻身 (Zen Mind Forging Body) — id 183 · character phase 1
- 每场战斗开始时加1[体魄]。战斗胜利时额外加1体魄上限（最多加4次）。  
  *Add 1 [Physique] at the start of each battle. Add 1 [Physique] Cap when winning a battle (up to 4 times).*

#### 心体共鸣 (Mind-Body Resonance) — id 184 · character phase 2
- 战斗中每加1点[体魄]时加1防。  
  *Whenever you gain 1 [Physique] in battle, you gain 1 DEF.*

#### 记忆碎片 (Memory Fragment) — id 186 · character phase 3
- 手牌中的1级牌可以和2级牌合成为3级牌，此法合成耗5体魄，体魄不足则无效。（2张牌均在手牌中才能以此法合成）  
  *A level 1 card in your hand can be synthesized with a level 2 card to upgrade to level 3. This method of upgrade costs 5 [Physique], and is invalid if you don't have enough [Physique]. (You must have both cards in your hand to upgrade by this method.)*

#### 冥心入玄 (Meditation of Xuan) — id 185 · character phase 4
- 获得1张[冥心入玄]  
  *Gain 1 [Meditation of Xuan]*

#### 万玄破魔掌 (Wan Xuan Demon Breaking Palm) — id 187 · character phase 5
- 获得1张[万玄破魔掌]  
  *Gain 1 [Wan Xuan Demon Breaking Palm]*


## Character fates — 小布 (锻玄宗)

#### 磨砺不止 (Unyielding Learning) — id 151 · character phase 1
- 每损失7点命元，加1换牌机会  
  *Gain 1 Exchange Chance for every 7 Destiny you lost*

#### 锻体不息 (Unceasing Exercising) — id 152 · character phase 2
- 获得1张[锻体不息]  
  *Gain 1 [Unceasing Exercising]*

#### 灵涌不竭 (Unbounded Qi) — id 153 · character phase 3
- 使用卡牌时若灵气不足，每点灵气耗3生命和1体魄代替（生命或体魄不足则无效）  
  *If you lack Qi when playing a card, spend 3 HP and 1 Physique to substitute each point of Qi (not valid if you don't have enough HP or Physique)*

#### 生机不灭 (Undying Body) — id 154 · character phase 4
- 下次命元耗尽时，保留1点命元不被淘汰，并且生命上限及体魄上限加4  
  *When the next Destiny is exhausted, keep 1 Destiny and not be eliminated, then gain 4 Max HP and Physique Cap*

#### 修玄不泯 (Unwavering Soul) — id 177 · character phase 5
- 战斗中每获得1层[负面状态]时加1生命  
  *Add 1 HP whenever you gain 1 stack of [Debuff] in battle*


## Character fates — 屠馗 (锻玄宗)

#### 锻躯之道 (Forge Body) — id 170 · character phase 1
- 初始手牌包含1张加[体魄]的牌；之后每轮少加1修为并随机抽1张加[体魄]的牌。  
  *The starting hand includes 1 card that adds [Physique]. At the beginning of each subsequent round, lose 1 Cultivation and draw 1 card that adds [Physique].*

#### 盛气凌人 (Overwhelming Power) — id 172 · character phase 2
- 获得1张[盛气凌人]  
  *Gain 1 [Overwhelming Power]*

#### 搏命之勇 (Courage to Fight) — id 171 · character phase 3
- 体魄及体魄上限+3 / 每场战斗开始时获得1层[加攻]和1层[外伤]  
  *Physique and Physique Cap + 3 / Gain 1 [Increase ATK] and 1 [Wound] at the start of each battle*

#### 崩裂之拳 (Cracking Fist) — id 174 · character phase 4
- [耗生命]的牌改为耗生命上限  
  *[HP cost] cards are changed to spend your Max HP*

#### 猛攻之姿 (Stance of Fierce Attack) — id 173 · character phase 5
- 战斗中每次使用加体魄的牌后，追加3攻  
  *Make an additional 3 ATK after each time you play a card that adds [Physique]*


## Character fates — 慕虎 (五行道盟)

#### 猛虎之躯 (The Body of Fierce Tiger) — id 125 · character phase 1
- 每次突破境界后分别多加2/3/4/5生命上限； / 战斗开始时若自身生命≥120，升级卡组中1张1级牌（优先取自身专属仙命牌，其次取最靠左的牌），战斗结束后还原  
  *Each time you break through the Phase add 2/3/4/5 more Max HP;  /  At the beginning of the battle if your HP ≥ 120, upgrade a Level 1 card in your deck (priority to upgrade your Immortal Fate card, followed by the most left card), and restored at the end of the battle.*

#### 木灵炼体 (Quench Of Wood Spirit) — id 89 · character phase 2
- 炼化“木灵”牌时加2生命上限（最多加8点）  
  *When you Absorb a "Wood Spirit" card, your Max HP increases by 2 (up to a maximum of 8).*

#### 锟铻金环 (Kun Wu Metal Ring) — id 132 · character phase 3
- 获得1张[锟铻金环]  
  *Gain 1 [Kun Wu Metal Ring]*

#### 刚劲 (Vigorous) — id 91 · character phase 4
- 获得1张[金灵•刚劲]  
  *Gain 1 [Metal Spirit - Vigorous]*

#### 山崩 (Landslide) — id 100 · character phase 5
- 获得1张[土灵•山崩]  
  *Gain 1 [Earth Spirit - Landslide]*


## Character fates — 曜灵 (七星阁)

#### 先天灵躯 (Innate Spirit Body) — id 37 · character phase 1
- 每次突破后抽1张新境界的牌，但是少加1生命上限  
  *Each time break through the Phase draw a card of new Phase, but decrease 1 Max HP to add*

#### 绛纱守护 (Crimson Yarn Guard) — id 105 · character phase 2
- 战败受到的命元伤害≥15时，免疫此命元伤害（限1次）  
  *If Destiny damage is bigger or equal to 15 when defeated, resist this Destiny damage (Only Trigger Once)*

#### 灯焰飞舞 (Flame Flutter) — id 39 · character phase 3
- 获得1张[灯焰飞舞]  
  *Gain 1 [Flame Flutter]*

#### 旋灯占卦 (Rotary Divination Hexagram) — id 40 · character phase 4
- 获得1张[旋灯占卦]  
  *Gain 1 [Rotary Divination Hexagram]*

#### 灯灵觉醒 (Lantern Spirit Awakening) — id 28 · character phase 5
- 修为减1，抽1张牌； / 之后每轮多抽1张牌  
  *Lose 1 Cultivation, and draw 1 card; / After this round, draw 1 more card for each round*


## Character fates — 李㵘 (锻玄宗)

#### 凡躯 (Mortal Body) — id 204 · character phase 1
- 炼化卡牌时无法获得[修为]，改为加1[体魄]（不超过上限） / 战斗中无法获得[灵气]，改为加等量[体魄] / 初始获得1张[双节棍]，化神期后变为[赤金盘龙棍]  
  *When Absorb cards, you cannot gain [Cultivation], instead add 1 [Physique] (up to the cap). / During battles, you cannot gain [Qi], instead add an equivalent amount of [Physique]. / Initially gain 1 [Double Stick], which changes to [Red Gold Dragon Stick] after reaching the Incarnation Phase.*

#### 拆招 (Counter Move) — id 205 · character phase 2
- 获得1张[拆招]  
  *Gain 1 [Counter Move]*

#### 志坚 (Indomitable Will) — id 206 · character phase 3
- [拳]：自身受到的攻减1；自身获得[外伤]时少加1层[外伤] / [棍]：自身所有攻加1；自身获得[减攻]时少加1层[减攻]  
  *[Fist]: Reduce incoming ATK by 1; when gaining [Wound], reduce the stack count by 1. / [Staff]: Increase all ATK by 1; when gaining [Decrease ATK], reduce the stack count by 1.*

#### 转势 (Shift Stance) — id 207 · character phase 4
- 修为减1，获得2张[转势]  
  *Lose 1 Cultivation and gain 2 [Shift Stance]*

#### 灵炁奔涌 (Surge of Qi) — id 209 · character phase 5
- [拳]：每次加[气势]时加2[身法]（每回合限1次） / [棍]：每次[再次行动]时加1[灵气]和2生命  
  *[Fist]: Each time you gain [Force], add 2 [Agility] (once per turn) / [Stick]: Each time you [Chase], gain 1 [Qi] and 2 HP*


## Character fates — 杜伶鸳 (五行道盟)

#### 先天五行•土 (Innate Element - Earth) — id 50109 · character phase 1
- 先天五行为土。每次突破境界后获得1张土灵牌（不低于自身上个境界）。

#### 先天印记 (Innate Mark) — id 110 · character phase 2
- 战斗开始时[激活]先天五行  
  *At the beginning of the battle Activate your Innate Element*

#### 先天灵阵 (Innate Spirit Formation) — id 111 · character phase 3
- 获得1张先天五行对应的2级灵阵牌（[木灵阵]/[火灵阵]/[土灵阵]/[金灵阵]/[水灵阵]）  
  *Gain a Level 2 Spirit Formation card of your Innate Element([Wood Spirit Formation]/[Fire Spirit Formation]/[Earth Spirit Formation]/[Metal Spirit Formation]/[Water Spirit Formation])*

#### 双鸳逆克 (Overcome with each other) — id 124 · character phase 4
- 修为减1，获得2张[双鸳逆克]  
  *Lose 1 Cultivation, gain 2 [Overcome with each other]*

#### 五行元灵 (Five Elements Anima) — id 112 · character phase 5
- 每种五行在首次激活时触发额外效果： / 木灵：获得1层[加攻] / 火灵：对方减7生命及上限 / 土灵：防+12 / 金灵：获得4层[锋锐] / 水灵：获得2层[水势]  
  *When [Activate] each [Five Elements] for the first time, trigger additional effects:  / Wood Spirit: Gain 1 stack of [Increase ATK] / Fire Spirit: Opponent loses 7 HP and Max HP / Earth Spirit: DEF+12 / Metal Spirit: Gain 4 stacks of [Penetrate] / Water Spirit: Gain 2 stacks of [Force of Water]*


## Character fates — 林小月 (云灵剑宗)

#### 好奇心 (Curiosity) — id 129 · character phase 1
- 使用最后1次换牌机会时，会换到随机惊喜并加1次换牌机会（最多触发9次）  
  *When you use your last Exchange Chance to change a card, you will change to a random surprise card and gain 1 Exchange Chance (up to 9 times)*

#### 猫爪 (Cat Paw) — id 44 · character phase 2
- 获得1张[云剑•猫爪]  
  *Gain 1 [Cloud Sword - Cat Paw]*

#### 猫魂庇佑 (Cat Soul Bless) — id 45 · character phase 3
- 战败受到的[命元]伤害为偶数时，伤害减半  
  *When defeated in battle, if the damage of [Destiny] is an even number, halve the damage*

#### 灵猫乱剑 (Spirit Cat Chaos Sword) — id 46 · character phase 4
- 获得1张[灵猫乱剑]  
  *Gain 1 [Spirit Cat Chaos Sword]*

#### 灵猫踏云 (Lithe As Cat) — id 15 · character phase 5
- 修为减1，获得1张“云剑”牌（金丹期以上）； / 战斗中每次使用“云剑”时加1灵气。  
  *Lose 1 Cultivation and gain 1 "Cloud Sword" Card (Above Virtuoso Phase); / Each time you play "Cloud Sword" card, add 1 Qi.*


## Character fates — 炎尘 (七星阁)

#### 血脉威能 (Bloodline Power) — id 114 · character phase 1
- 每造成28点命元伤害，抽1张牌（初始计数16）  
  *Draw 1 card for every 28 Destiny damage dealt by you (initial count 16)*

#### 燃命之焰 (Flame of life) — id 115 · character phase 2
- 修为+1 / 战斗胜利时，多造成4命元伤害  
  *Cultivation+1 / When you win the battle, deal 4 more Destiny damage*

#### 无极卦盘 (Ultimate Hexagram Base) — id 121 · character phase 3
- 获得1张[无极卦盘]  
  *Gain 1 [Ultimate Hexagram Base]*

#### 瓮中捉鳖 (Within Reach) — id 35 · character phase 4
- 获得1张[瓮中捉鳖]  
  *Gain 1 [Within Reach]*

#### 狂雷电闪 (Fury Thunder) — id 122 · character phase 5
- 获得1张[狂雷电闪]  
  *Gain 1 [Fury Thunder]*


## Character fates — 炎雪 (云灵剑宗)

#### 血脉潜能 (Bloodline Potential) — id 19 · character phase 1
- 每损失18点命元，抽1张牌（初始计数12）  
  *Draw 1 card for every 18 Destiny you lost (initial count 12)*

#### 炽火炎刃 (Fire Flame Blade) — id 67 · character phase 2
- 每次攻击时减对方1生命上限，且必定触发[击伤]效果  
  *Each of your attack reduces 1 Max HP of your opponent, and you will always trigger the [Injured] effect.*

#### 流冰寒刃 (Drift Ice Blade) — id 68 · character phase 3
- 每次攻击时自身加1防（自身没有防时多加1防）  
  *Each of your attack will add 1 [DEF] (1 more DEF if you have no DEF)*

#### 崩雪 (Avalanche) — id 23 · character phase 4
- 获得1张[云剑•崩雪]  
  *Gain 1 [Cloud Sword - Avalanche]*

#### 炎舞 (Flame Dance) — id 22 · character phase 5
- 获得1张[狂剑•炎舞]  
  *Gain 1 [Unrestrained Sword - Flame Dance]*


## Character fates — 牧逸风 (云灵剑宗)

#### 云雾变幻 (Shift As Cloud) — id 18 · character phase 1
- 每轮首次换牌不消耗换牌机会  
  *The first card exchanged each round doesn't consume an Exchange Chance*

#### 剑不出鞘 (Sword In Sheathed) — id 66 · character phase 2
- 自身回合若未攻击，则加3防  
  *If you do not attack during your turn, gain 3 [DEF] at the end of turn.*

#### 云海连绵 (Endurance As Cloud Sea) — id 14 · character phase 3
- 立刻获得1张“云剑”牌； / 战斗中[连云]效果未前置“云剑”也可触发，且使用其他牌不中断连续使用“云剑”的计数。  
  *Gain 1 "Cloud Sword" Card. / [Cloud Hit] effect can be triggered even if there is no "Cloud Sword" played first. / Successive count of "Cloud Sword" played will not be reset by the use of other cards.*

#### 云影化身 (Shade Of Cloud) — id 7 · character phase 4
- 下次命元耗尽时，保留1点命元不被淘汰，并且换牌机会加5  
  *When the next Destiny is exhausted, keep 1 Destiny and not be eliminated, then add 5 Exchange Card Chance*

#### 云泉道茶 (Spring Course Tea) — id 17 · character phase 5
- 修为减1，获得2张[云泉道茶]  
  *Lose 1 Cultivation, gain 2 [Spring Course Tea]*


## Character fates — 祁忘忧 (五行道盟)

#### 五行玉瓶 (Five Elements Pure Vase) — id 199 · character phase 1
- 点击角色或此仙命图标打开五行玉瓶，可在其中存放3张牌（放入牌时加1修为，取出时减1修为）。 / 战斗开始时[激活]五行玉瓶中第一格牌的所属[五行]。  
  *Click on the character or this Immortal Fate icon to open the Pure Vase, where you can store 3 cards (gain 1 Cultivation when inserting a card, lose 1 Cultivation when removing a card). / At the beginning of the battle, activate the [Five Elements] of the card stored in the first slot of Pure Vase.*

#### 百草生息 (Herbs Flourish) — id 200 · character phase 2
- 战斗中每次使用不含五行的牌时[激活木灵]；战斗中每次[激活木灵]时加2生命上限  
  *Whenever you play a card without any Five Elements, [Activate Wood Spirit]; Whenever you [Activate Wood Spirit], add 2 Max HP*

#### 天降甘霖 (Heavenly Rain) — id 201 · character phase 3
- 获得1张[天降甘霖]  
  *Gain 1 [Heavenly Rain]*

#### 五行聚灵 (Five Elements Gather Qi) — id 202 · character phase 4
- 战斗中[激活]五行时加1灵气（每种五行限1次）  
  *Add 1 Qi whenever you [Activate] Five Elements during battle (limited to once per Five Elements type)*

#### 忘忧 (Forget Worries) — id 203 · character phase 5
- 获得1张[忘忧]； / 每场战斗开始时[激活木灵]  
  *Gain 1 [Forget Worries];  / At the beginning of each battle [Activate Wood Spirit]*


## Character fates — 花沁蕊 (五行道盟)

#### 桃枝如意 (Peach Branch Ruyi) — id 134 · character phase 1
- 战斗开始时获得1层护体  
  *At the beginning of the battle, gain 1 stack of [Guard Up]*

#### 桃花印 (Peach Blossom Seal) — id 98 · character phase 2
- 获得1张[木灵•桃花印]  
  *Gain 1 [Wood Spirit - Peach Blossom Seal]*

#### 水灵印记 (Mark Of Water Spirit) — id 99 · character phase 3
- 战斗开始时[激活水灵]并加1[灵气]  
  *At the beginning of the battle [Activate Water Spirit] and add 1 [Qi]*

#### 春雨 (Spring Rain) — id 90 · character phase 4
- 获得1张[水灵•春雨]  
  *Gain 1 [Water Spirit - Spring Rain]*

#### 花舞 (Blossom Dance) — id 101 · character phase 5
- 每当使用[五行]牌时，若被上一张使用的牌[五行]相生，则加1灵气和1生命及上限；使用[木灵•桃花印]时若触发以上效果则[再次行动]。  
  *When playing a card in the order of [Five Element Generating Interaction], add 1 Qi, 1 Max Hp and 1 HP; If the above effect is triggered when playing [Wood Spirit - Peach Blossom Seal], [Chase].*


## Character fates — 谭舒雁 (七星阁)

#### 勤学苦练 (Study Hard) — id 29 · character phase 1
- 每炼化8张牌，抽1张牌  
  *For every 8 cards Absorb, draw 1 card*

#### 飞鸿踏雪 (Only Traces) — id 63 · character phase 2
- 获得1张[飞鸿踏雪]  
  *Gain 1 [Only Traces]*

#### 雪羽清风 (Birdie Wind) — id 64 · character phase 3
- 修为减1，随机获得1张可加生命的门派牌；战斗中每次自身生命变化时加1[防]  
  *Lose 1 Cultivation, and randomly gain 1 sect card that can add HP; Add 1 DEF for each time your HP changes in battle*

#### 雁影化身 (Avatar of Bird Shade) — id 65 · character phase 4
- 下次命元耗尽时，保留1点命元不被淘汰，并减1修为获得1张[飞鸿踏雪]  
  *When the next Destiny is exhausted, keep 1 Destiny and not be eliminated, then lose 1 Cultivation and gain 1 [Only Traces]*

#### 斩断俗尘 (Cut Off Mundane) — id 42 · character phase 5
- 抽牌和换牌时不再出现炼气期的牌  
  *You will no longer get the Meditation Phase card when draw or exchange card*


## Character fates — 陆剑心 (云灵剑宗)

#### 铸剑师 (Swordsmith) — id 92 · character phase 1
- 游戏开始时获得一张[澄心剑胚]。每轮战斗后[澄心剑胚]加1攻（最多加18攻）。  
  *At the beginning of the game get a [Clear Heart Sword Embryo]. After each battle round, [Clear Heart Sword Embryo] increase 1 ATK (up to increase 18 ATK).*

#### 稳固剑锋 (Stable Blade) — id 20093 · character phase 2
- **Phase 2**: [澄心剑胚]附加效果：减2攻但附加“防+9”
- **Phase 4**: [澄心剑胚]附加效果：减2攻但附加“防+9”  
  *[Clear Heart Sword Embryo] gain the effect: Reduce 2 ATK but add "DEF+9"*

#### 锐意剑纹 (Intense Sword Pattern) — id 30094 · character phase 3
- **Phase 2**: [澄心剑胚]附加效果：减2攻但附加“[剑意]+4”
- **Phase 5**: [澄心剑胚]附加效果：减2攻但附加“[剑意]+4”  
  *[Clear Heart Sword Embryo] gain the effect: Reduce 2 ATK but add "[Sword Intent]+4"*

#### 灵威凝铸 (Spiritual Power Forging) — id 30095 · character phase 4
- **Phase 2**: [澄心剑胚]附加效果：耗1灵气：追加4攻×2
- **Phase 5**: [澄心剑胚]附加效果：耗1灵气：追加4攻×2  
  *[Clear Heart Sword Embryo] gain the effect: Cost 1 Qi to make 2 additional attacks of 4 ATK each*

#### 无极之心 (Ultimate Heart) — id 30096 · character phase 5
- **Phase 2**: [澄心剑胚]定名为“澄心•无极”，附加效果“此牌效果中的所有数字加1”
- **Phase 5**: [澄心剑胚]定名为“澄心•无极”，附加效果“此牌效果中的所有数字加1”  
  *Name [Clear Heart Sword Embryo] as "Clear Heart - Ultimate" with additional effect "All numerical values in this card's effect are increased by 1"*


## Character fates — 风绪 (七星阁)

#### 风行天上 (Wind in Sky) — id 194 · character phase 1
- 每次突破境界后减4修为并抽4张牌  
  *Each time you break through the Phase, lose 4 Cul. and draw 4 cards*

#### 阴符玉简 (Jade Scroll of Yin Symbol) — id 196 · character phase 2
- 获得1张[阴符玉简]  
  *Gain 1 [Jade Scroll of Yin Symbol]*

#### 灵卦自衍 (Spirit Hexagram Evolves) — id 195 · character phase 3
- 自身回合中若加过[灵气]，回合结束时加1[卦象]  
  *If you have added [Qi] in your turn, gain 1 [Hexagram] at the end of the turn*

#### 易卦自解 (Hexagrams Explain) — id 197 · character phase 4
- 战斗开始时若卡组中含以下八卦牌合计正好为2张，使用时增加对应效果： / 震卦：施加4层破绽 / 坤卦：施加2层虚弱 / 巽卦：灵气+4 / 艮卦：生命及上限+10 / 坎卦：多加4格成为星位 / 兑卦：施加3层内伤 / 离卦：卦象+1 / 乾卦：再次行动  
  *At the start of battle, if your deck contains exactly the following 2 Hexagram cards, those cards increase the corresponding effect: / Zhen Hexagram: Apply 4 stacks of [Flaw] / Earth Hexagram: Apply 2 stacks of [Weakened] / Wind Hexagram: Qi+4 / Mountain Hexagram: HP and Max HP + 10 / Water Hexagram: Make 4 more slots in your deck [Become Star Point] / Lake Hexagram: Apply 3 stacks of [Internal Injury] / Flame Hexagram: [Hexagram]+1 / Heaven Hexagram: [Chase]*

#### 孤虚金书 (Solitary Void Golden Scroll) — id 198 · character phase 5
- 获得1张[孤虚金书]。 / 战斗开始时：若[孤虚金书]前一格为空则放入[背孤]，若后一格为空则放入[击虚]，前后每有一格未能放入牌就改为让[孤虚金书]升1级（战斗结束还原）。  
  *Gain 1 [Solitary Void Golden Scroll]. / At the beginning of the battle: If the previous slot of [Solitary Void Golden Scroll] is empty, temporarily generate [Face Isolation], and if the next slot is empty, temporarily generate [Strike Vacuity]. For each slot without generation, upgrade [Solitary Void Golden Scroll] by 1 level (restored after the battle).*


## Character fates — 黎承云 (云灵剑宗)

#### 悟剑天赋 (Swordplay Talent) — id 189 · character phase 1
- 游戏开始时随机领悟3张“剑”牌（金丹、元婴、化神各1张）。到达对应境界后获得1张所领悟的牌。  
  *At the beginning of the game, randomly comprehend 3 "Sword" cards (one in Virtuoso Phase, one in Immortality Phase and one in Incarnation Phase). After reaching each Phase, obtain 1 card comprehended in that Phase.*

#### 八方来风 (Wind Rose) — id 191 · character phase 2
- [速度]+1（每保留1张手牌多加1，最多计7张手牌）  
  *[Speed]+1 (for every hand card held, add 1 more [Speed], up to 7 hand cards)*

#### 观壁悟道 (Dao of Ruiying) — id 190 · character phase 3
- 修为+1； / 额外领悟1张金丹期或以上的随机“剑”牌加入悟剑天赋。  
  *Cultivation+1; / Extra comprehend a random "Sword" card with Virtuoso Phase or above and add it to the Swordplay Talent.*

#### 剑招融汇 (Chengyun's Fusion Style) — id 192 · character phase 4
- 悟剑天赋中领悟的牌（及同名牌）在战斗中可同时视作“云剑”“狂剑”“灵剑”和“剑阵”  
  *The cards comprehended by Swordplay Talent can be regarded as "Cloud Sword", "Unrestrained Sword", "Spirit Sword", and "Sword Formation" in battle.*

#### 曳影剑阵 (Yeying Sword Formation) — id 193 · character phase 5
- 获得1张[曳影剑阵]； / [曳影剑阵]将同时视作“云剑”“狂剑”“灵剑”和“剑阵”。  
  *Gain 1 [Yeying Sword Formation]; / [Yeying Sword Formation] will be regarded as "Cloud Sword", "Unrestrained Sword", "Spirit Sword", and "Sword Formation" in battle.*


## Character fates — 龙瑶 (云灵剑宗)

#### 龙脉传承 (Inheritance of Dragonling) — id 24 · character phase 1
- 首轮多抽2张牌，突破至化神期后再抽2张牌  
  *Draw 2 more cards in the first round, and then draw 2 cards after break through the Immortality Phase.*

#### 珊瑚剑 (Coral Sword) — id 25 · character phase 2
- 战斗开始时获得状态：下2次攻击[无视防御]  
  *At the beginning of the battle, gain effect: The following 2 times attack will [Ignore DEF]*

#### 龙鳞 (Dragon Scale) — id 27 · character phase 3
- 战败受到大于20的[命元]伤害时，减少至20。 / 战斗结束后若自身命元首次≤20，永久升级卡组中随机1张1级牌（优先取自身仙命专属牌）  
  *When taking [Destiny] damage greater than 20 in battle, reduce to 20. / After the battle ends, if your [Destiny] is ≤ 20 for the first time, permanently upgrade 1 random Level 1 card in your deck (prioritizing your Immortal Fate card).*

#### 唤雨 (Pray Rain) — id 85 · character phase 4
- 获得1张[云剑•唤雨]  
  *Gain 1 [Cloud Sword - Pray Rain]*

#### 九霄玲珑镯 (Sky Delicate Bracelet) — id 86 · character phase 5
- 获得1张[九霄玲珑镯]  
  *Gain 1 [Sky Delicate Bracelet]*


## Other fates (shared pool)

#### 融会贯通 (Integrating Knowledge) — id 2
- **Phase 2**: 抽1张牌  
  *Draw 1 Card(s)*
- **Phase 3**: 抽2张牌  
  *Draw 2 Card(s)*
- **Phase 4**: 抽2张牌  
  *Draw 2 Card(s)*
- **Phase 5**: 抽3张牌  
  *Draw 3 Card(s)*

#### 戒备防守 (Be On Guard) — id 3
- 战斗开始时加8防  
  *At the beginning of the battle add 8 [DEF]*

#### 道韵传承 (Inheritance of the Daoist Rhyme) — id 10
- **Phase 2**: 抽1张筑基期牌  
  *Draw 1 Foundation Phase Card(s)*
- **Phase 3**: 抽1张金丹期牌；修为+1  
  *Draw 1 Virtuoso Phase Card(s); Cultivation+1*
- **Phase 4**: 抽1张元婴期牌；修为+1  
  *Draw 1 Immortality Phase Card(s); Cultivation+1*
- **Phase 5**: 抽1张化神期牌；修为+2  
  *Draw 1 Incarnation Phase Card(s); Cultivation+2*

#### 博采众长 (Learn From Others) — id 11
- 抽3张牌  
  *Draw 3 Card(s)*

#### 精进 (Diligent) — id 20
- 随机升级一张牌  
  *Upgrade 1 card randomly*

#### 冷静 (Calm) — id 21
- 修为+3  
  *Cultivation+3*

#### 泪天镯 (Tears Bracelet) — id 26
- 战斗开始时获得1层[护体]  
  *At the beginning of the battle, gain 1 stack(s) of [Guard Up]*

#### 生机绽放 (Vitality Blossom) — id 32
- 

#### 北斗星盘 (Dipper Astrolabe) — id 33
- 修为+1；卡组第7格成为[星位]  
  *Cultivation+1; The seventh slot in your deck becomes [Star Point] slot*

#### 七星灯 (Heptastar Lantern) — id 34
- 获得1张[七星灯]  
  *Gain 1 [Heptastar Lantern]*

#### 聚灵卦 (Spiritage Hexagram) — id 36
- 使用加[卦象]的牌时加2[灵气]  
  *Add 2 [Qi] when playing a card with [Hexagram]*

#### 稳固防御 (Solid Defense) — id 38
- 每次加防时多加1点  
  *For each time gain DEF, add 2 more DEF*

#### 枯木逢春 (Revitalized) — id 41
- 

#### 好奇心 (Curiosity) — id 43
- 初始换牌机会+10；换牌机会可无限储存  
  *Initial Exchange Card Chance+10; Exchange Card Chance has no store limitation*

#### 剑灵极影 (Sword Spirit Shadow) — id 47
- 单次加3点及以上灵气后[再次行动]（每场战斗限1次）  
  *Add 3 or more Qi in one turn, then [Chase] (Can only trigger once for each round)*

#### 观星 (Stargaze) — id 49
- 战斗中首次使用“星弈”牌时，那一格成为星位直到战斗结束  
  *When the first time playing "Astral Move" card in each battle round, that slot will become a Star Point slot until the end of the battle round*

#### 星蚀 (Astral Eclipse) — id 51
- 对方每被加1层[负面状态]时减1生命  
  *For each stack of [Debuff] apply to the opponent, the opponent loses1 HP*

#### 木灵之躯 (Body of Wood Spirit) — id 60
- **Phase 2**: 使用卡组第一格的牌时加10生命上限  
  *Add 10 Max HP when the card in the deck in the first slot is played*
- **Phase 3**: 使用卡组第一格的牌时加10生命上限  
  *Add 10 Max HP when the card in the deck in the first slot is played*
- **Phase 4**: 使用卡组第一格的牌时加15生命上限  
  *Add 15 Max HP when the card in the deck in the first slot is played*
- **Phase 5**: 使用卡组第一格的牌时加20生命上限  
  *Add 20 Max HP when the card in the deck in the first slot is played*

#### 舍身化道 (Sacrificing Into Dao) — id 78
- **Phase 2**: 生命上限减2；抽2张门派牌  
  *Max HP reduced by 2; Draw 2 Sect Card(s)*
- **Phase 3**: 生命上限减3；抽3张门派牌  
  *Max HP reduced by 3; Draw 3 Sect Card(s)*
- **Phase 4**: 生命上限减4；抽4张门派牌  
  *Max HP reduced by 4; Draw 4 Sect Card(s)*
- **Phase 5**: 生命上限减5；抽5张门派牌  
  *Max HP reduced by 5; Draw 5 Sect Card(s)*

#### 元灵沟通 (In Touch Anima) — id 79
- **Phase 2**: 每次激活任意五行时加3防  
  *Each time any Five Elements are activated add 3 DEF*
- **Phase 3**: 每次激活任意五行时加3生命  
  *Each time any Five Elements are activated add 3 HP*
- **Phase 4**: 每次激活任意五行时加4层[锋锐]  
  *Each time any Five Elements are activated add 4 stacks of [Penetrate]*
- **Phase 5**: 每次激活任意五行时加2灵气  
  *Each time any Five Elements are activated add 2 Qi*

#### 五行凝炼 (Combine Of Five Elements) — id 84
- 下一次炼化[五行]牌时，获得3张与其相同[五行]的牌（金丹期以上）  
  *Next time when you Absorb the [Five Elements] card, gain 3 of the same [Five Elemnets] cards as absorbed (above Virtuoso Phase)*

#### 灵阵精通 (Spirit Formation Mastered) — id 87
- 每次突破时，随机获得一张[五行]（金/木/水/火/土）灵阵  
  *Each time you break through, draw a random [Five Elements] (Metal/Wood/Water/Fire/Earth) Spirit Formation card*

#### 土灵印记 (Mark Of Earth Spirit) — id 88
- 战斗开始时[激活土灵]并加6防  
  *At the beginning of the battle [Activate Earth Spirit] and add 6 DEF*

#### 剑锋锻造 (Blade Forging) — id 93
- 为[澄心剑胚]选一项效果 / 锐利：攻+3 / 稳固：减2攻但附加“防+9”  
  *Choose an effect for [Clear Heart Sword Embryo] / Sharpness: ATK+3 / Stable: Reduce 2 ATK but add "DEF+9"*

#### 剑纹雕琢 (Sword Pattern Carving) — id 94
- 为[澄心剑胚]选一项效果 / 追击：追加5攻 / 蓄攻：获得1层[加攻] / 锐意：减2攻但附加“[剑意]+4”  
  *Choose an effect for [Clear Heart Sword Embryo] / Chain Attack: Make an additional 5 ATK / Charge: Gain 1 stack of [Increase ATK] / Intense: Reduce 2 ATK but add "[Sword Intent]+4"*

#### 灵气凝铸 (Qi Forging) — id 95
- 为[澄心剑胚]选一项效果 / 聚灵：灵气+2 / 御灵：每点灵气加3防 / 灵威：耗1灵气，追加4攻×2  
  *Choose an effect for [Clear Heart Sword Embryo] / Spiritage: Qi+2 / Spiritstat: Gain 3 DEF for each Qi / Spiritual Power: Cost 1 Qi to make 2 additional attacks of 4 ATK each*

#### 剑心淬炼 (Quench Of Sword Heart) — id 96
- 为[澄心剑胚]选择定名与效果： / 狂剑•澄心：加3攻，下1张牌算作狂剑 / 云剑•澄心：减7攻，下1张云剑获得[再次行动] / 澄心•无极：此牌效果中的所有数字加1  
  *Choose a name and effect for [Clear Heart Sword Embryo] / Unrestrained Sword - Clear Heart: Increase 3 ATK, and next card count as Unrestrained Sword / Cloud Sword - Clear Heart: Reduce 7 ATK, and next Cloud Sword gain [Chase] / Clear Heart - Ultimate: All numerical values in this card's effect are increased by 1*

#### 生机之种 (Seed Of Vitality) — id 97
- 初始修为+2 / 每次突破境界后加5命元  
  *Initial Cultivation+2 / Each time break through the Phase add 5 Destiny*

#### 无中生有 (Out Of Nothing) — id 107
- 若剩余换牌机会为0，下轮开始时多加1～2次换牌机会  
  *If Exchange Card Chance is 0, add 1～2 more Exchange Card Chance next round*

#### 先天五行 (Innate Element) — id 109
- 游戏开始时随机1种先天五行，每次突破境界后获得1张该五行的牌（不低于自身上个境界）。  
  *At the beginning of the game gain a random Innate Element from Five Elements. After each Phase break through you will gain 1 card (at least your previous Phase) related to Innate Element.*

#### 火灵炼体 (Quench Of Fire Spirit) — id 126
- 炼化“火灵”牌时加1生命上限（累计最多加7点）  
  *When Absorb "Fire Spirit" card, add 1 Max HP (Accumulated up to 7)*

#### 相生五灵阵 (Five Elements Generating Spirit Formation) — id 130
- 使用五行（木/火/土/金/水）灵阵后，其持续效果也可以被相生五行（火/土/金/水/木）的牌触发  
  *After using the Five Elements (Wood/Fire/Earth/Metal/Water) Spirit Formation, its Continuous effect can be triggered by other Five Elements (Fire/Earth/Metal/Water/Wood) which have a generating interaction with it*

####  — id 131
- 

#### 五行润养 (Five Elements Infuse) — id 133
- 每轮开始时，卡组中每有1种不同五行就加1命元。此法累积15点以上命元后加1修为，然后此仙命变为“桃枝如意”（战斗开始时获得1层护体）。  
  *At the beginning of each round, add 1 Destiny for each different [Five Elements] in your deck. If you accumulate 15 or more Destiny by this way, you gain 1 Cul. and change this Immortal Fate to "Peach Branch Ruyi" (At the beginning of the battle, gain 1 stack of [Guard Up]).*

#### 生机卦诀 (Vitality Hexagram) — id 135
- 每次加卦象时加等量生命  
  *Whenever you gain Hexagram, add the same amount of HP*

####  — id 147
- 

####  — id 148
- 

####  — id 155
- 

####  — id 156
- 

#### 晚霞 (Sunset Glow) — id 157
- **Phase 2**: 到达元婴期后获得1张[云剑·晚霞]  
  *Gain 1 [Cloud Sword - Sunset Glow] after reaching Immortality Phase.*
- **Phase 3**: 到达元婴期后获得1张[云剑·晚霞]，且之后可能抽到此牌（最多1张）。  
  *Gain 1 [Cloud Sword - Sunset Glow] after reaching Immortality Phase, and you may gain up to 1 copy of this card in the rest of the game.*
- **Phase 4**: 获得1张[云剑·晚霞]，且之后可能抽到此牌（最多2张）。  
  *Gain 1 [Cloud Sword - Sunset Glow], and you may gain up to 2 copies of this card in the rest of the game.*
- **Phase 5**: 获得1张[云剑·晚霞]，且之后可能抽到此牌（最多3张）。  
  *Gain 1 [Cloud Sword - Sunset Glow], and you may gain up to 3 copies of this card in the rest of the game.*

#### 青龙剑阵 (Azure Dragon Sword Formation) — id 158
- **Phase 2**: 到达元婴期后获得1张[青龙剑阵]  
  *Gain 1 [Azure Dragon Sword Formation] after reaching Immortality Phase.*
- **Phase 3**: 到达元婴期后获得1张[青龙剑阵]，且之后可能抽到此牌（最多1张）。  
  *Gain 1 [Azure Dragon Sword Formation] after reaching Immortality Phase, and you may gain up to 1 copy of this card in the rest of the game.*
- **Phase 4**: 获得1张[青龙剑阵]，且之后可能抽到此牌（最多2张）。  
  *Gain 1 [Azure Dragon Sword Formation], and you may gain up to 2 copies of this card in the rest of the game.*
- **Phase 5**: 获得1张[青龙剑阵]，且之后可能抽到此牌（最多3张）。  
  *Gain 1 [Azure Dragon Sword Formation], and you may gain up to 3 copies of this card in the rest of the game.*

#### 百兽灵剑阵 (Beast Spirit Sword Formation) — id 159
- **Phase 2**: 到达化神期后获得1张[百兽灵剑阵]  
  *Gain 1 [Beast Spirit Sword Formation] after reaching Incarnation Phase.*
- **Phase 3**: 到达化神期后获得1张[百兽灵剑阵]，且之后可能抽到此牌（最多1张）。  
  *Gain 1 [Beast Spirit Sword Formation] after reaching Incarnation Phase, and you may gain up to 1 copy of this card in the rest of the game.*
- **Phase 4**: 到达化神期后获得1张[百兽灵剑阵]，且之后可能抽到此牌（最多2张）。  
  *Gain 1 [Beast Spirit Sword Formation] after reaching Incarnation Phase, and you may gain up to 2 copies of this card in the rest of the game.*
- **Phase 5**: 获得1张[百兽灵剑阵]，且之后可能抽到此牌（最多3张）。  
  *Gain 1 [Beast Spirit Sword Formation], and you may gain up to 3 copies of this card in the rest of the game.*

#### 狂龙吞云 (Dragon Devours Clouds) — id 160
- **Phase 2**: 到达化神期后获得1张[狂龙吞云]  
  *Gain 1 [Dragon Devours Clouds] after reaching Incarnation Phase.*
- **Phase 3**: 到达化神期后获得1张[狂龙吞云]，且之后可能抽到此牌（最多1张）。  
  *Gain 1 [Dragon Devours Clouds] after reaching Incarnation Phase, and you may gain up to 1 copy of this card in the rest of the game.*
- **Phase 4**: 到达化神期后获得1张[狂龙吞云]，且之后可能抽到此牌（最多2张）。  
  *Gain 1 [Dragon Devours Clouds] after reaching Incarnation Phase, and you may gain up to 2 copies of this card in the rest of the game.*
- **Phase 5**: 获得1张[狂龙吞云]，且之后可能抽到此牌（最多3张）。  
  *Gain 1 [Dragon Devours Clouds], and you may gain up to 3 copies of this card in the rest of the game.*

#### 灵卦术 (Spiritual Divination) — id 161
- **Phase 2**: 到达元婴期后获得1张[灵卦术]  
  *Gain 1 [Spiritual Divination] after reaching Immortality Phase.*
- **Phase 3**: 到达元婴期后获得1张[灵卦术]，且之后可能抽到此牌（最多1张）。  
  *Gain 1 [Spiritual Divination] after reaching Immortality Phase, and you may gain up to 1 copy of this card in the rest of the game.*
- **Phase 4**: 获得1张[灵卦术]，且之后可能抽到此牌（最多2张）。  
  *Gain 1 [Spiritual Divination], and you may gain up to 2 copies of this card in the rest of the game.*
- **Phase 5**: 获得1张[灵卦术]，且之后可能抽到此牌（最多3张）。  
  *Gain 1 [Spiritual Divination], and you may gain up to 3 copies of this card in the rest of the game.*

#### 摘花飞叶 (Throw Petals) — id 162
- **Phase 2**: 到达元婴期后获得1张[摘花飞叶]  
  *Gain 1 [Throw Petals] after reaching Immortality Phase.*
- **Phase 3**: 到达元婴期后获得1张[摘花飞叶]，且之后可能抽到此牌（最多1张）。  
  *Gain 1 [Throw Petals] after reaching Immortality Phase, and you may gain up to 1 copy of this card in the rest of the game.*
- **Phase 4**: 获得1张[摘花飞叶]，且之后可能抽到此牌（最多2张）。  
  *Gain 1 [Throw Petals], and you may gain up to 2 copies of this card in the rest of the game.*
- **Phase 5**: 获得1张[摘花飞叶]，且之后可能抽到此牌（最多3张）。  
  *Gain 1 [Throw Petals], and you may gain up to 3 copies of this card in the rest of the game.*

#### 双飞燕 (Twin Swallows) — id 163
- **Phase 2**: 到达化神期后获得1张[星弈·双飞燕]  
  *Gain 1 [Astral Move - Twin Swallows] after reaching Incarnation Phase.*
- **Phase 3**: 到达化神期后获得1张[星弈·双飞燕]，且之后可能抽到此牌（最多1张）。  
  *Gain 1 [Astral Move - Twin Swallows] after reaching Incarnation Phase, and you may gain up to 1 copy of this card in the rest of the game.*
- **Phase 4**: 到达化神期后获得1张[星弈·双飞燕]，且之后可能抽到此牌（最多2张）。  
  *Gain 1 [Astral Move - Twin Swallows] after reaching Incarnation Phase, and you may gain up to 2 copies of this card in the rest of the game.*
- **Phase 5**: 获得1张[星弈·双飞燕]，且之后可能抽到此牌（最多3张）。  
  *Gain 1 [Astral Move - Twin Swallows], and you may gain up to 3 copies of this card in the rest of the game.*

#### 滴水穿石 (Water Drop Erosion) — id 164
- **Phase 2**: 到达化神期后获得1张[滴水穿石]  
  *Gain 1 [Water Drop Erosion] after reaching Incarnation Phase.*
- **Phase 3**: 到达化神期后获得1张[滴水穿石]，且之后可能抽到此牌（最多1张）。  
  *Gain 1 [Water Drop Erosion] after reaching Incarnation Phase, and you may gain up to 1 copy of this card in the rest of the game.*
- **Phase 4**: 到达化神期后获得1张[滴水穿石]，且之后可能抽到此牌（最多2张）。  
  *Gain 1 [Water Drop Erosion] after reaching Incarnation Phase, and you may gain up to 2 copies of this card in the rest of the game.*
- **Phase 5**: 获得1张[滴水穿石]，且之后可能抽到此牌（最多3张）。  
  *Gain 1 [Water Drop Erosion], and you may gain up to 3 copies of this card in the rest of the game.*

#### 野渡之印 (Wild Crossing Seal) — id 165
- **Phase 2**: 到达元婴期后获得1张[野渡之印]  
  *Gain 1 [Wild Crossing Seal] after reaching Immortality Phase.*
- **Phase 3**: 到达元婴期后获得1张[野渡之印]，且之后可能抽到此牌（最多1张）。  
  *Gain 1 [Wild Crossing Seal] after reaching Immortality Phase, and you may gain up to 1 copy of this card in the rest of the game.*
- **Phase 4**: 获得1张[野渡之印]，且之后可能抽到此牌（最多2张）。  
  *Gain 1 [Wild Crossing Seal], and you may gain up to 2 copies of this card in the rest of the game.*
- **Phase 5**: 获得1张[野渡之印]，且之后可能抽到此牌（最多3张）。  
  *Gain 1 [Wild Crossing Seal], and you may gain up to 3 copies of this card in the rest of the game.*

#### 熔岩之印 (Lava Seal) — id 166
- **Phase 2**: 到达元婴期后获得1张[熔岩之印]  
  *Gain 1 [Lava Seal] after reaching Immortality Phase.*
- **Phase 3**: 到达元婴期后获得1张[熔岩之印]，且之后可能抽到此牌（最多1张）。  
  *Gain 1 [Lava Seal] after reaching Immortality Phase, and you may gain up to 1 copy of this card in the rest of the game.*
- **Phase 4**: 获得1张[熔岩之印]，且之后可能抽到此牌（最多2张）。  
  *Gain 1 [Lava Seal], and you may gain up to 2 copies of this card in the rest of the game.*
- **Phase 5**: 获得1张[熔岩之印]，且之后可能抽到此牌（最多3张）。  
  *Gain 1 [Lava Seal], and you may gain up to 3 copies of this card in the rest of the game.*

#### 滚石之印 (Boulder Seal) — id 167
- **Phase 2**: 到达化神期后获得1张[滚石之印]  
  *Gain 1 [Boulder Seal] after reaching Incarnation Phase.*
- **Phase 3**: 到达化神期后获得1张[滚石之印]，且之后可能抽到此牌（最多1张）。  
  *Gain 1 [Boulder Seal] after reaching Incarnation Phase, and you may gain up to 1 copy of this card in the rest of the game.*
- **Phase 4**: 到达化神期后获得1张[滚石之印]，且之后可能抽到此牌（最多2张）。  
  *Gain 1 [Boulder Seal] after reaching Incarnation Phase, and you may gain up to 2 copies of this card in the rest of the game.*
- **Phase 5**: 获得1张[滚石之印]，且之后可能抽到此牌（最多3张）。  
  *Gain 1 [Boulder Seal], and you may gain up to 3 copies of this card in the rest of the game.*

#### 斩浪之印 (Wave Cutter Seal) — id 168
- **Phase 2**: 到达化神期后获得1张[斩浪之印]  
  *Gain 1 [Wave Cutter Seal] after reaching Incarnation Phase.*
- **Phase 3**: 到达化神期后获得1张[斩浪之印]，且之后可能抽到此牌（最多1张）。  
  *Gain 1 [Wave Cutter Seal] after reaching Incarnation Phase, and you may gain up to 1 copy of this card in the rest of the game.*
- **Phase 4**: 到达化神期后获得1张[斩浪之印]，且之后可能抽到此牌（最多2张）。  
  *Gain 1 [Wave Cutter Seal] after reaching Incarnation Phase, and you may gain up to 2 copies of this card in the rest of the game.*
- **Phase 5**: 获得1张[斩浪之印]，且之后可能抽到此牌（最多3张）。  
  *Gain 1 [Wave Cutter Seal], and you may gain up to 3 copies of this card in the rest of the game.*

####  — id 169
- 

#### 得炁 (Attain Qi) — id 208
- 加回因“凡躯”而少加的修为，然后“凡躯”转变为“灵炁奔涌”（拳：每次加气势时加2身法（每回合限1次）；棍：每次再次行动时加1灵气和2生命）  
  *Restore lost Cultivation due to 'Mortal Body', then transform 'Mortal Body' into 'Surge of Qi' ([Fist]: Each time you gain [Force], add 2 [Agility] (once per turn); [Stick]: Each time you [Chase], gain 1 [Qi] and 2 HP).*

#### 启动资金 (Initial Capital) — id 9001
- 初始获得{otherParams[0]}通宝，炼化卡牌时+{otherParams[1]}通宝  
  *Gain {otherParams[0]} Coins when the game starts, gain {otherParams[1]} coin when absorbing a card.*

#### 天降横财 (Windfall) — id 9002
- 获得{otherParams[0]}通宝  
  *Gain {otherParams[0]} Coins*

#### 炼化专精 (Mastery of Absorbing) — id 9003
- 炼化卡牌时额外+{otherParams[0]}通宝  
  *Gain {otherParams[0]} more Coins when absorbing a card*

#### 炼丹天赋 (Elixirist Talent) — id 9004
- 每轮首次炼丹时（使用[炼丹炉]或[八卦炉]或[太虚熔炉]），多获得{otherParams[0]}张  
  *For the first time brew elixirs (using [Furnace ] or [Hexagram Furnace ] or [Furnace of Void]) per round, obtain  {otherParams[0]} more Elixir card*

#### 符咒天赋 (Fuluist Talent) — id 9005
- 使用符咒牌加通宝时数量×1{otherParams[0]}%（向上取整）  
  *Gain 1{otherParams[0]}% Coins when using Fuluist cards to gain Coins (Ceil)*

#### 法宝精通 (Talisman Talent) — id 9006
- 使用法宝时有{otherParams[0]}%概率不消耗耐久  
  *There is a {otherParams[0]}% chance that using Talisman cards will not consume Durability*

#### 镇店神兽 (Guardian Beast) — id 9007
- 获得1张【{otherParams[0]}】  
  *Gain 1 【{otherParams[0]}】*

#### 锐利剑锋 (Sharp Blade) — id 10093
- **Phase 2**: [澄心剑胚]附加效果：攻+3
- **Phase 3**: [澄心剑胚]附加效果：攻+3  
  *[Clear Heart Sword Embryo] gain the effect: ATK+3*

#### 追击剑纹 (Chain Sword Pattern) — id 10094
- **Phase 2**: [澄心剑胚]附加效果：追加5攻
- **Phase 3**: [澄心剑胚]附加效果：追加5攻  
  *[Clear Heart Sword Embryo] gain the effect: Make an additional 5 ATK*

#### 聚灵凝铸 (Spiritage Forging) — id 10095
- **Phase 2**: [澄心剑胚]附加效果：灵气+2
- **Phase 3**: [澄心剑胚]附加效果：灵气+2  
  *[Clear Heart Sword Embryo] gain the effect: Qi+2*

#### 狂剑之心 (Unrestrained Sword Heart) — id 10096
- **Phase 2**: [澄心剑胚]定名为“狂剑•澄心”，加3攻，附加效果“下1张牌算作狂剑”
- **Phase 3**: [澄心剑胚]定名为“狂剑•澄心”，加3攻，附加效果“下1张牌算作狂剑”  
  *Name [Clear Heart Sword Embryo] as "Unrestrained Sword - Clear Heart", and increase 3 ATK with additional effect "Next card count as Unrestrained Sword"*

#### 先天五行•金 (Innate Element - Metal) — id 10109
- **Phase 2**: 先天五行为金。每次突破境界后获得1张金灵牌（不低于自身上个境界）。
- **Phase 3**: 先天五行为金。每次突破境界后获得1张金灵牌（不低于自身上个境界）。  
  *Innate Element is Metal. Gain 1 Metal Spirit card (at least your previous Phase) when break through the Phase.*

#### 崩拳传承 (Inheritance of Crash Fist) — id 10143
- 获得{otherParams[0]}张“崩拳”牌  
  *Gain {otherParams[0]} "Crash Fist" Card(s)*

#### 炼体传承 (Inheritance of Physique Building) — id 10144
- 获得{otherParams[0]}张加[体魄]的牌  
  *Gain {otherParams[0]} Card(s) of adding Physique*

#### 气势充沛 (Full of Force) — id 10145
- 战斗开始时加{otherParams[0]}[气势]和{otherParams[1]}气势上限  
  *Add {otherParams[0]} [Force] and {otherParams[1]} Force Cap at the start of each battle*

#### 体修入道 (Physique Master) — id 10146
- 体魄上限+{otherParams[1]}；[体魄]+{otherParams[0]}  
  *Physique Cap + {otherParams[1]}; [Physique] + {otherParams[0]}*

#### 再生之躯 (Regenerating Body) — id 10149
- 每次使用卡组第一格的牌时加{otherParams[0]}[体魄]和{otherParams[1]}生命  
  *When playing the card in your deck's first slot, add {otherParams[0]} [Physique] and {otherParams[1]} HP*

#### 冥心烙印 (Mark of Dark Heart) — id 10150
- 战斗开始时，自身加{otherParams[0]}层[内伤]和{otherParams[1]}层[恢复]  
  *At the start of combat, gain {otherParams[0]} [Internal Injury] and {otherParams[1]} [Regeneration]*

#### 晚霞 (Sunset Glow) — id 10157
- 到达元婴期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Immortality Phase, and you may gain up to {otherParams[2]} copy of this card in the rest of the game.*

#### 青龙剑阵 (Azure Dragon Sword Formation) — id 10158
- 到达元婴期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Immortality Phase, and you may gain up to {otherParams[2]} copy of this card in the rest of the game.*

#### 百兽灵剑阵 (Beast Spirit Sword Formation) — id 10159
- 到达化神期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Incarnation Phase, and you may gain up to {otherParams[2]} copy of this card in the rest of the game.*

#### 狂龙吞云 (Dragon Devours Clouds) — id 10160
- 到达化神期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Incarnation Phase, and you may gain up to {otherParams[2]} copy of this card in the rest of the game.*

#### 灵卦术 (Spiritual Divination) — id 10161
- 到达元婴期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Immortality Phase, and you may gain up to {otherParams[2]} copy of this card in the rest of the game.*

#### 摘花飞叶 (Throw Petals) — id 10162
- 到达元婴期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Immortality Phase, and you may gain up to {otherParams[2]} copy of this card in the rest of the game.*

#### 双飞燕 (Twin Swallows) — id 10163
- 到达化神期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Incarnation Phase, and you may gain up to {otherParams[2]} copy of this card in the rest of the game.*

#### 滴水穿石 (Water Drop Erosion) — id 10164
- 到达化神期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Incarnation Phase, and you may gain up to {otherParams[2]} copy of this card in the rest of the game.*

#### 野渡之印 (Wild Crossing Seal) — id 10165
- 到达元婴期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Immortality Phase, and you may gain up to {otherParams[2]} copy of this card in the rest of the game.*

#### 熔岩之印 (Lava Seal) — id 10166
- 到达元婴期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Immortality Phase, and you may gain up to {otherParams[2]} copy of this card in the rest of the game.*

#### 滚石之印 (Boulder Seal) — id 10167
- 到达化神期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Incarnation Phase, and you may gain up to {otherParams[2]} copy of this card in the rest of the game.*

#### 斩浪之印 (Wave Cutter Seal) — id 10168
- 到达化神期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Incarnation Phase, and you may gain up to {otherParams[2]} copy of this card in the rest of the game.*

#### 历战不屈 (Unbowed through battle) — id 10175
- 生命上限+{otherParams[0]}；每次战斗失败后永久加{otherParams[1]}生命上限  
  *Max HP + {otherParams[0]}; Permanently gain {otherParams[1]} Max HP after each battle you lose*

#### 筋骨健壮 (Firmness Body) — id 10176
- 体魄上限+{otherParams[0]}；战斗开始时，每有{otherParams[1]}[体魄]加1生命  
  *Physique Cap + {otherParams[0]}; At the start of each battle, gain 1 HP for every {otherParams[1]} [Physique]*

#### 天降横财 (Windfall) — id 19002
- 获得{otherParams[0]}通宝  
  *Gain {otherParams[0]} Coins*

#### 炼化专精 (Mastery of Absorbing) — id 19003
- 炼化卡牌时额外+{otherParams[0]}通宝  
  *Gain {otherParams[0]} more Coins when absorbing a card*

#### 炼丹天赋 (Elixirist Talent) — id 19004
- 每轮首次炼丹时（使用[炼丹炉]或[八卦炉]或[太虚熔炉]），多获得{otherParams[0]}张  
  *For the first time brew elixirs (using [Furnace ] or [Hexagram Furnace ] or [Furnace of Void]) per round, obtain  {otherParams[0]} more Elixir card*

#### 符咒天赋 (Fuluist Talent) — id 19005
- 使用符咒牌加通宝时数量×1{otherParams[0]}%（向上取整）  
  *Gain 1{otherParams[0]}% Coins when using Fuluist cards to gain Coins (Ceil)*

#### 镇店神兽 (Guardian Beast) — id 19007
- 获得1张【{otherParams[0]}】  
  *Gain 1 【{otherParams[0]}】*

#### 蓄攻剑纹 (Charge Sword Pattern) — id 20094
- **Phase 2**: [澄心剑胚]附加效果：获得1层[加攻]
- **Phase 4**: [澄心剑胚]附加效果：获得1层[加攻]  
  *[Clear Heart Sword Embryo] gain the effect: Gain 1 stack of [Increase ATK]*

#### 御灵凝铸 (Spiritstat Forging) — id 20095
- **Phase 2**: [澄心剑胚]附加效果：每点灵气加3防
- **Phase 4**: [澄心剑胚]附加效果：每点灵气加3防  
  *[Clear Heart Sword Embryo] gain the effect: Gain 3 DEF for each Qi*

#### 云剑之心 (Cloud Sword Heart) — id 20096
- **Phase 2**: [澄心剑胚]定名为“云剑•澄心”，减7攻，附加效果“下1张云剑获得[再次行动]”
- **Phase 4**: [澄心剑胚]定名为“云剑•澄心”，减7攻，附加效果“下1张云剑获得[再次行动]”  
  *Name [Clear Heart Sword Embryo] as "Cloud Sword - Clear Heart", and reduce 7 ATK with additional effect "Next Cloud Sword gain [Chase]"*

#### 先天五行•水 (Innate Element - Water) — id 20109
- **Phase 2**: 先天五行为水。每次突破境界后获得1张水灵牌（不低于自身上个境界）。
- **Phase 4**: 先天五行为水。每次突破境界后获得1张水灵牌（不低于自身上个境界）。  
  *Innate Element is Water. Gain 1 Water Spirit card (at least your previous Phase) when break through the Phase.*

#### 崩拳传承 (Inheritance of Crash Fist) — id 20143
- 获得{otherParams[0]}张“崩拳”牌  
  *Gain {otherParams[0]} "Crash Fist" Card(s)*

#### 炼体传承 (Inheritance of Physique Building) — id 20144
- 获得{otherParams[0]}张加[体魄]的牌  
  *Gain {otherParams[0]} Card(s) of adding Physique*

#### 气势充沛 (Full of Force) — id 20145
- 战斗开始时加{otherParams[0]}[气势]和{otherParams[1]}气势上限  
  *Add {otherParams[0]} [Force] and {otherParams[1]} Force Cap at the start of each battle*

#### 体修入道 (Physique Master) — id 20146
- 体魄上限+{otherParams[1]}；[体魄]+{otherParams[0]}  
  *Physique Cap + {otherParams[1]}; [Physique] + {otherParams[0]}*

#### 再生之躯 (Regenerating Body) — id 20149
- 每次使用卡组第一格的牌时加{otherParams[0]}[体魄]和{otherParams[1]}生命  
  *When playing the card in your deck's first slot, add {otherParams[0]} [Physique] and {otherParams[1]} HP*

#### 冥心烙印 (Mark of Dark Heart) — id 20150
- 战斗开始时，自身加{otherParams[0]}层[内伤]和{otherParams[1]}层[恢复]  
  *At the start of combat, gain {otherParams[0]} [Internal Injury] and {otherParams[1]} [Regeneration]*

#### 晚霞 (Sunset Glow) — id 20157
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 青龙剑阵 (Azure Dragon Sword Formation) — id 20158
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 百兽灵剑阵 (Beast Spirit Sword Formation) — id 20159
- 到达化神期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Incarnation Phase, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 狂龙吞云 (Dragon Devours Clouds) — id 20160
- 到达化神期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Incarnation Phase, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 灵卦术 (Spiritual Divination) — id 20161
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 摘花飞叶 (Throw Petals) — id 20162
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 双飞燕 (Twin Swallows) — id 20163
- 到达化神期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Incarnation Phase, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 滴水穿石 (Water Drop Erosion) — id 20164
- 到达化神期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Incarnation Phase, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 野渡之印 (Wild Crossing Seal) — id 20165
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 熔岩之印 (Lava Seal) — id 20166
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 滚石之印 (Boulder Seal) — id 20167
- 到达化神期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Incarnation Phase, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 斩浪之印 (Wave Cutter Seal) — id 20168
- 到达化神期后获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】 after reaching Incarnation Phase, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 历战不屈 (Unbowed through battle) — id 20175
- 生命上限+{otherParams[0]}；每次战斗失败后永久加{otherParams[1]}生命上限  
  *Max HP + {otherParams[0]}; Permanently gain {otherParams[1]} Max HP after each battle you lose*

#### 筋骨健壮 (Firmness Body) — id 20176
- 体魄上限+{otherParams[0]}；战斗开始时，每有{otherParams[1]}[体魄]加1生命  
  *Physique Cap + {otherParams[0]}; At the start of each battle, gain 1 HP for every {otherParams[1]} [Physique]*

#### 天降横财 (Windfall) — id 29002
- 获得{otherParams[0]}通宝  
  *Gain {otherParams[0]} Coins*

#### 炼化专精 (Mastery of Absorbing) — id 29003
- 炼化卡牌时额外+{otherParams[0]}通宝  
  *Gain {otherParams[0]} more Coins when absorbing a card*

#### 炼丹天赋 (Elixirist Talent) — id 29004
- 每轮首次炼丹时（使用[炼丹炉]或[八卦炉]或[太虚熔炉]），多获得{otherParams[0]}张  
  *For the first time brew elixirs (using [Furnace ] or [Hexagram Furnace ] or [Furnace of Void]) per round, obtain  {otherParams[0]} more Elixir card*

#### 符咒天赋 (Fuluist Talent) — id 29005
- 使用符咒牌加通宝时数量×1{otherParams[0]}%（向上取整）  
  *Gain 1{otherParams[0]}% Coins when using Fuluist cards to gain Coins (Ceil)*

#### 镇店神兽 (Guardian Beast) — id 29007
- 获得1张【{otherParams[0]}】  
  *Gain 1 【{otherParams[0]}】*

#### 先天五行•木 (Innate Element - Wood) — id 30109
- **Phase 2**: 先天五行为木。每次突破境界后获得1张木灵牌（不低于自身上个境界）。
- **Phase 5**: 先天五行为木。每次突破境界后获得1张木灵牌（不低于自身上个境界）。  
  *Innate Element is Wood. Gain 1 Wood Spirit card (at least your previous Phase) when break through the Phase.*

#### 崩拳传承 (Inheritance of Crash Fist) — id 30143
- 获得{otherParams[0]}张“崩拳”牌  
  *Gain {otherParams[0]} "Crash Fist" Card(s)*

#### 炼体传承 (Inheritance of Physique Building) — id 30144
- 获得{otherParams[0]}张加[体魄]的牌  
  *Gain {otherParams[0]} Card(s) of adding Physique*

#### 气势充沛 (Full of Force) — id 30145
- 战斗开始时加{otherParams[0]}[气势]和{otherParams[1]}气势上限  
  *Add {otherParams[0]} [Force] and {otherParams[1]} Force Cap at the start of each battle*

#### 体修入道 (Physique Master) — id 30146
- 体魄上限+{otherParams[1]}；[体魄]+{otherParams[0]}  
  *Physique Cap + {otherParams[1]}; [Physique] + {otherParams[0]}*

#### 再生之躯 (Regenerating Body) — id 30149
- 每次使用卡组第一格的牌时加{otherParams[0]}[体魄]和{otherParams[1]}生命  
  *When playing the card in your deck's first slot, add {otherParams[0]} [Physique] and {otherParams[1]} HP*

#### 冥心烙印 (Mark of Dark Heart) — id 30150
- 战斗开始时，自身加{otherParams[0]}层[内伤]和{otherParams[1]}层[恢复]  
  *At the start of combat, gain {otherParams[0]} [Internal Injury] and {otherParams[1]} [Regeneration]*

#### 晚霞 (Sunset Glow) — id 30157
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 青龙剑阵 (Azure Dragon Sword Formation) — id 30158
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 百兽灵剑阵 (Beast Spirit Sword Formation) — id 30159
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 狂龙吞云 (Dragon Devours Clouds) — id 30160
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 灵卦术 (Spiritual Divination) — id 30161
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 摘花飞叶 (Throw Petals) — id 30162
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 双飞燕 (Twin Swallows) — id 30163
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 滴水穿石 (Water Drop Erosion) — id 30164
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 野渡之印 (Wild Crossing Seal) — id 30165
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 熔岩之印 (Lava Seal) — id 30166
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 滚石之印 (Boulder Seal) — id 30167
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 斩浪之印 (Wave Cutter Seal) — id 30168
- 获得1张【{otherParams[0]}】，且之后可能抽到此牌（最多{otherParams[2]}张）。  
  *Gain 1 【{otherParams[0]}】, and you may gain up to {otherParams[2]} copies of this card in the rest of the game.*

#### 历战不屈 (Unbowed through battle) — id 30175
- 生命上限+{otherParams[0]}；每次战斗失败后永久加{otherParams[1]}生命上限  
  *Max HP + {otherParams[0]}; Permanently gain {otherParams[1]} Max HP after each battle you lose*

#### 筋骨健壮 (Firmness Body) — id 30176
- 体魄上限+{otherParams[0]}；战斗开始时，每有{otherParams[1]}[体魄]加1生命  
  *Physique Cap + {otherParams[0]}; At the start of each battle, gain 1 HP for every {otherParams[1]} [Physique]*

#### 天降横财 (Windfall) — id 39002
- 获得{otherParams[0]}通宝  
  *Gain {otherParams[0]} Coins*

#### 炼化专精 (Mastery of Absorbing) — id 39003
- 炼化卡牌时额外+{otherParams[0]}通宝  
  *Gain {otherParams[0]} more Coins when absorbing a card*

#### 炼丹天赋 (Elixirist Talent) — id 39004
- 每轮首次炼丹时（使用[炼丹炉]或[八卦炉]或[太虚熔炉]），多获得{otherParams[0]}张  
  *For the first time brew elixirs (using [Furnace ] or [Hexagram Furnace ] or [Furnace of Void]) per round, obtain  {otherParams[0]} more Elixir card*

#### 符咒天赋 (Fuluist Talent) — id 39005
- 使用符咒牌加通宝时数量×1{otherParams[0]}%（向上取整）  
  *Gain 1{otherParams[0]}% Coins when using Fuluist cards to gain Coins (Ceil)*

#### 镇店神兽 (Guardian Beast) — id 39007
- 获得1张【{otherParams[0]}】  
  *Gain 1 【{otherParams[0]}】*

#### 先天五行•火 (Innate Element - Fire) — id 40109
- 先天五行为火。每次突破境界后获得1张火灵牌（不低于自身上个境界）。


## Appendix: 天衍 Derivations (Dao derivations / 道韵-style grants)

353 entries from `tools/derivations_resolved.json`. `kind` = activation type; 【N】 in raw text refers to card id N.


### Category 0

| id | Name | Kind | Effect (CN) | Effect (EN) |
|---|---|---|---|---|
| 12 | 我命由我 (My Fate, My Choice) | 被动/通用 | 突破境界时可刷新全部仙命选项（累计限5次） | On breakthrough, can refresh all Immortal Fate options (cumulative limit 5 times). |
| 14 | 根骨奇佳 (Exceptional Roots) | 被动/通用 | 突破境界所需的修为和体魄减2 | Reduces the Cultivation and Physique required for Breakthrough by 2 |
| 15 | 稳定突破 (Stable Breakthrough) | 被动/通用 | 换牌机会储存上限减10；到达第3/5/8/11轮后，可无视修为突破至筑基/金丹/元婴/化神期 | Exchange Chance storage cap -10. After round 3/5/8/11, can break through to Foundation/Virtuoso/Immortality/Incarnation regardless of Cultivation. |
| 16 | 记忆修炼 (Memory Cultivation) | 被动/通用 | 修为+1；换牌机会储存上限加20；手牌上限加20 | +1 Cultivation, +20 Exchange Chance storage cap, +20 hand size. |
| 18 | 双重道韵 (Double Daoist Rhyme) | 被动/通用 | 下1次通过道韵预感获得牌时，额外获得1张相同的牌 | Gain an extra copy of the next card you gain from Daoist Rhyme Omen. |
| 19 | 隐忍 (Forbearance) | 被动/通用 | 每轮开始时，若上一轮自身未进行过换牌，则换牌机会+1 | Each round, if you didn't exchange last round, +1 Exchange Chance. |
| 21 | 广结善缘 (Build Good Karma) | 被动/通用 | 每次战斗胜利时，向对方造成的命元伤害减1（至少为1），自身加1次换牌机会 | On victory, Destiny damage to opponent reduced by 1 (min 1), gain 1 Exchange Chance. |
| 26 | 稳固防御 (Solid Defense) | 被动/通用 | 战斗中每次加防时多加1 | In battle, +1 DEF per DEF gain. |
| 27 | 徐如林 (Calm as a Forest) | 被动/通用 | 若手牌不为空，战斗开始时加12%生命及等量生命上限 | Battle start: if hand is not empty, +12% HP and Max HP. |
| 29 | 疾如风 (Swift as Wind) | 被动/通用 | 若手牌为空，【KEYWORD_速度】+4 | If hand is empty, 【KEYWORD_速度】+4. |
| 31 | 全能副职 (Omni Side Job) | 被动/通用 | 换牌机会+7；向牌池中加入所有其他副职业的元婴期和化神期牌各4张 | Exchange Card Chance + 7; Add 4 each of Immortality and Incarnation phase cards from all other side jobs to the pool. |
| 32 | 逍遥点穴手 (Free Spirit Pressure Point) | 被动/通用 | 每次使用普通攻击时，令对方失去3层【KEYWORD_加攻】和3层【KEYWORD_护体】 | Each basic attack removes 3 stacks of 【KEYWORD_加攻】 and 3 stacks of 【KEYWORD_护体】 from opponent. |
| 33 | 逍遥护身诀 (Free Spirit Shield) | 被动/通用 | 每张普通攻击在首次使用时获得2层【KEYWORD_护体】 | Each basic attack gains 2 stacks of 【KEYWORD_护体】 on first use. |
| 36 | 逍遥神力掌 (Free Spirit Power Palm) | 被动/通用 | 每次使用普通攻击时获得2层【KEYWORD_加攻】 | Each basic attack gains 2 stacks of 【KEYWORD_加攻】. |
| 39 | 承载之躯 (Carrier Body) | 被动/通用 | 生命上限+2；卡组中可额外放置1张【KEYWORD_持续】或【KEYWORD_消耗】牌 | +2 Max HP. Can place 1 extra 【KEYWORD_持续】 or 【KEYWORD_消耗】 cards in deck. |
| 84 | 天衍-剑不出鞘 (Heavenly Derivation - Sword In Sheathed) | 被动/通用 | 自身回合若未攻击，回合结束时加1【KEYWORD_剑意】 | If you did not attack during your turn, gain 1 【KEYWORD_剑意】 at end of turn. |
| 85 | 天衍-云雾变幻 (Heavenly Derivation - Shift As Cloud) | 被动/通用 | 换牌机会储存无上限； / 每轮开始时，若上一轮未使用【TALENT_18】的效果换牌，额外加2换牌机会 | No Exchange Chance storage cap. Each round, if 【TALENT_18】 was not used to exchange cards last round, gain 2 extra Exchange Chance. |
| 89 | 流风回雪 (Flowing Wind Returning Snow) | 被动/通用 | 战斗开始时算作已用过1次云剑并加2【KEYWORD_云海】 | Battle start: count as having used Cloud Sword 1 times and gain 2 【KEYWORD_云海】. |
| 95 | 天衍-好奇心 (Heavenly Derivation - Curiosity) | 被动/通用 | 每次战斗失败后，【TALENT_129】增加1次触发机会 | After each battle loss, 【TALENT_129】 gains 1 extra trigger chance. |
| 97 | 天衍-灵猫踏云 (Heavenly Derivation - Lithe As Cat) | 被动/通用 | 每次使用云剑时获得1层【KEYWORD_云海】 | Each time a Cloud Sword is used, gain 1 stack of 【KEYWORD_云海】. |
| 99 | 剑心演武 (Sword Heart Martial Display) | 被动/通用 | 战斗开始时若【澄心剑胚】与云剑相邻，则下轮开始抽牌时优先抽1张云剑；若【澄心剑胚】与狂剑相邻，则下轮开始抽牌时优先抽1张狂剑 | Battle start: if 【澄心剑胚】 is adjacent to a Cloud Sword, prioritize drawing 1 Cloud Sword next round; if 【澄心剑胚】 is adjacent to an Unrestrained Sword, prioritize drawing 1 Unrestrained Sword next round. |
| 100 | 淬剑-灵气 (Tempered Blade - Qi) | 被动/通用 | 使用【澄心剑胚】时加1【KEYWORD_灵气】 | When using 【澄心剑胚】, gain 1 【KEYWORD_灵气】. |
| 101 | 淬剑-剑气 (Tempered Blade - Sword Qi) | 被动/通用 | 使用【澄心剑胚】时加2【KEYWORD_剑气】 | When using 【澄心剑胚】, gain 2 【KEYWORD_剑气】. |
| 102 | 淬剑-清心 (Tempered Blade - Clear Mind) | 被动/通用 | 使用【澄心剑胚】时自身所有【KEYWORD_负面状态】减2层 | When using 【澄心剑胚】, reduce all 【KEYWORD_负面状态】 by 2 stacks. |
| 103 | 淬剑-水月 (Tempered Blade - Moon Water) | 被动/通用 | 使用【澄心剑胚】时获得2层【KEYWORD_水月】效果 | When using 【澄心剑胚】, gain 2 stacks of 【KEYWORD_水月】. |
| 104 | 天衍-铸剑师 (Heavenly Derivation - Swordsmith) | 被动/通用 | 无视仙命【TALENT_92】的次数上限，且【澄心剑胚】每轮多加1攻 | Ignore 【TALENT_92】 use limit. 【澄心剑胚】 gains +1 ATK each round. |
| 106 | 剑影互通 (Sword Shadow Exchange) | 被动/通用 | 可在手牌中将2级“剑”牌拖动到同境界的1级“剑”牌上合成，令1级“剑”牌升级 | Drag a Lv.2 sword onto a same-phase Lv.1 sword in hand to upgrade it. |
| 109 | 护体剑阵 (Bodyguard Sword Formation) | 被动/通用 | 每场战斗首次使用剑阵时加5【KEYWORD_防】和1层【KEYWORD_护体】 | First time using a Sword Formation each battle, gain 5 【KEYWORD_防】 and 1 stacks of 【KEYWORD_护体】. |
| 110 | 天衍-勤学苦练 (Heavenly Derivation - Study Hard) | 被动/通用 | 合成卡牌时也会增加【TALENT_29】1次计数 | Fusing cards also counts toward 【TALENT_29】. |
| 116 | 天衍-先天灵躯 (Heavenly Derivation - Innate Spirit Body) | 被动/通用 | 突破境界时【TALENT_37】抽牌的效果改为从随机3张同境界的牌中选择1张获得 | When breaking through, 【TALENT_37】's draw effect changes to choosing 1 from 3 random cards of the same phase. |
| 119 | 天衍-运筹帷幄 (Heavenly Derivation - Strategize) | 被动/通用 | 手牌上限+10；每轮少加1修为，多抽1张牌 | +10 hand size. Each round: -1 Cultivation, +1 draw. |
| 120 | 天衍-七星定魂 (Heavenly Derivation - Heptastar Soulstat) | 被动/通用 | 若卡组第8格空着，则战斗开始时放入【七星定魂】，若已有【七星定魂】则改为将其升级 | If deck slot 8 is empty, place 【七星定魂】 there at battle start; if 【七星定魂】 is already there, upgrade it instead. |
| 121 | 七星伤魂 (Seven Stars Soul Wound) | 被动/通用 | 每次使用卡组第8格的牌时，向对方施加2层【KEYWORD_内伤】 | Each time the card in deck slot 8 is used, inflict 2 stacks of 【KEYWORD_内伤】 to opponent. |
| 124 | 天衍-计出万全 (Heavenly Derivation - Best Choice) | 被动/通用 | 使用最后1次换牌机会进行换牌时优先换到自身当前境界的牌 | When using the last Exchange Chance, prioritize exchanging for a card of your current phase. |
| 126 | 天衍-卜卦 (Heavenly Derivation - Divination) | 被动/通用 | 战斗结束时，保存剩余【KEYWORD_卦象】（最多4），下场战斗开始时获得保存的【KEYWORD_卦象】 | Battle end: save remaining 【KEYWORD_卦象】 (max 4); next battle, gain the saved 【KEYWORD_卦象】. |
| 128 | 抽刀断水 (Draw Sword to Cut Water) | 被动/通用 | 每次使用金灵牌时加1【KEYWORD_灵气】 | Each time you use a Metal Spirit card, gain 1 【KEYWORD_灵气】. |
| 131 | 天衍-先天印记 (Heavenly Derivation - Innate Mark) | 被动/通用 | 战斗开始时，【KEYWORD_激活】先天五行[相生]的【KEYWORD_五行】和[克制]的【KEYWORD_五行】 | Battle start: 【KEYWORD_激活】 the innate Five Elements [generating] element and [overcoming] element. |
| 133 | 相生灵阵 (Generating Spirit Formation) | 被动/通用 | 五行（木/火/土/金/水）灵阵的[持续]效果除了相同五行，还可以被其相生五行（火/土/金/水/木）的牌触发 | The [continuous] effect of Five Elements (Wood/Fire/Earth/Metal/Water) Spirit Formations can also be triggered by the element it generates (Fire/Earth/Metal/Water/Wood). |
| 137 | 凝水化刃 (Condensed Water Blade) | 被动/通用 | 【KEYWORD_水势】造成[伤害]的效果改为一次攻击，且【KEYWORD_击伤】对方时扣减的生命多50% | 【KEYWORD_水势】 damage effect becomes an attack instead, and HP deducted when 【KEYWORD_击伤】 opponent increased by 50%. |
| 138 | 天衍-木灵印记 (Heavenly Derivation - Mark of Wood Spirit) | 被动/通用 | 战斗开始时【KEYWORD_激活木灵】并加1【KEYWORD_灵气】 | Battle start: 【KEYWORD_激活木灵】 and gain 1 【KEYWORD_灵气】. |
| 140 | 天衍-猛虎之躯 (Heavenly Derivation - The Body of Fierce Tiger) | 被动/通用 | 战斗开始时，自身每有10生命，就额外加1生命及上限 | Battle start: for every 10 HP you have, gain 1 extra HP and max HP. |
| 143 | 天衍-土灵印记 (Heavenly Derivation - Mark of Earth Spirit) | 被动/通用 | 战斗开始时【KEYWORD_激活土灵】并加4【KEYWORD_防】 | Battle start: 【KEYWORD_激活土灵】 and gain 4 【KEYWORD_防】. |
| 145 | 天衍-秘印亲和 (Heavenly Derivation - Secret Seal Affinity) | 被动/通用 | 突破至金丹期和元婴期时，【TALENT_136】也可自选“秘印” | When breaking through to Virtuoso and Immortality, 【TALENT_136】 can also select 'Secret Seal' cards. |
| 146 | 天衍-火灵印记 (Heavenly Derivation - Mark of Fire Spirit) | 被动/通用 | 战斗开始时【KEYWORD_激活火灵】并减对方2生命上限 | Battle start: 【KEYWORD_激活火灵】 and reduce opponent's max HP by 2. |
| 147 | 混元异火 (Primordial Strange Fire) | 被动/通用 | 计算卡组中不同[五行]数量时，[火灵]算作2种[五行] | When counting different [Five Elements] in deck, [Fire Spirit] counts as 2 types of [Five Elements]. |
| 148 | 荆棘伴生 (Thorn Companion) | 被动/通用 | 每当获得【KEYWORD_加攻】时，其中1层转为【KEYWORD_木刺】 | Each time you gain 【KEYWORD_加攻】, 1 stack becomes 【KEYWORD_木刺】. |
| 149 | 魂体不竭 (Inexhaustible Soul Body) | 被动/通用 | 战斗中每次自身【KEYWORD_耗生命】时，加1【KEYWORD_体魄】 | In battle, each time you 【KEYWORD_耗生命】, gain 1 【KEYWORD_体魄】. |
| 151 | 灵香缭绕 (Incense Swirl) | 被动/通用 | 每场战斗开始时获得2层【KEYWORD_辟邪】 | Each battle: gain 2 stacks of 【KEYWORD_辟邪】. |
| 152 | 灵烟化爪 (Spirit Smoke Claws) | 被动/通用 | 描述中含“灵气”的牌多2攻 | Cards with 'Qi' in description gain +2 ATK. |
| 153 | 天衍-崩裂之拳 (Heavenly Derivation - Cracking Fist) | 被动/通用 | 使用【KEYWORD_耗生命】的牌时，向对方造成所需【KEYWORD_耗生命】40%的[伤害] | When using a card with 【KEYWORD_耗生命】, deal [DMG] equal to 40% of the required 【KEYWORD_耗生命】 to opponent. |
| 154 | 天衍-锻躯之道 (Heavenly Derivation - Forge Body) | 被动/通用 | 炼化含加【KEYWORD_体魄】效果的牌时，自身加2【KEYWORD_体魄】（不超过上限） | When absorbing a card with 【KEYWORD_体魄】-boosting effects, gain 2 【KEYWORD_体魄】 (not exceeding cap). |
| 155 | 掌法感悟 (Palm Technique Insight) | 被动/通用 | 每次战斗后，将卡组中名字含“掌”的1级牌升至2级 | After each battle, upgrade level 1 cards with 'Palm' in their name in deck to level 2. |
| 160 | 以冥化灵 (Styx to Qi Conversion) | 被动/通用 | 使用卡牌时若【KEYWORD_灵气】不足，可消耗自身的【KEYWORD_冥】代替【KEYWORD_灵气】 | When using a card without enough 【KEYWORD_灵气】, can consume 【KEYWORD_冥】 in place of 【KEYWORD_灵气】. |
| 161 | 天衍-入冥 (Heavenly Derivation - Entering Styx) | 被动/通用 | 每场战斗开始时获得2层【KEYWORD_冥】 | Each battle: gain 2 stacks of 【KEYWORD_冥】. |
| 163 | 禅心聚灵 (Zen Mind Qi Gathering) | 被动/通用 | 加【KEYWORD_体魄】时，额外加1【KEYWORD_灵气】（每回合限1次） | When gaining 【KEYWORD_体魄】, also gain 1 【KEYWORD_灵气】 (once per turn). |
| 166 | 天衍-禅心锻身 (Heavenly Derivation - Zen Mind Forging Body) | 被动/通用 | 仙命【TALENT_183】在每场战斗开始时多加1【KEYWORD_体魄】，且胜利时加【KEYWORD_体魄】上限的效果取消次数限制 | 【TALENT_183】 gains 1 extra 【KEYWORD_体魄】 at battle start, and the Physique cap increase on victory has no use limit. |
| 299 | 天衍-风行天上 (Heavenly Derivation - Wind in Sky) | 被动/通用 | 触发仙命【TALENT_194】抽牌时，优先抽取自身未获得过且不低于上个境界的牌 | 【TALENT_194】 draws prioritize cards you haven't obtained that are not below previous phase. |
| 303 | 天衍-五行刀斩 (Heavenly Derivation - Five Elements Blade Slash) | 被动/通用 | 到达第12轮后：修为减1，选择并获得1张五行斩（【木灵斩】/【火灵斩】/【土灵斩】/【金灵斩】/【水灵斩】） | After reaching round 12: Cultivation -1, choose and gain 1 Five Elements Slash (【木灵斩】/【火灵斩】/【土灵斩】/【金灵斩】/【水灵斩】). |
| 309 | 天衍-五行玉瓶 (Heavenly Derivation - Five Elements Pure Vase) | 被动/通用 | 战斗开始时额外【KEYWORD_激活】五行玉瓶中第2格牌的【KEYWORD_五行】 | Battle start: additionally 【KEYWORD_激活】 the 【KEYWORD_五行】 of the card in Five Elements Pure Vase slot 2. |
| 310 | 天衍-五行聚灵 (Heavenly Derivation - Five Elements Gather Qi) | 被动/通用 | 战斗中每次【KEYWORD_激活】【KEYWORD_五行】时，若该【KEYWORD_五行】已【KEYWORD_激活】过则加1【KEYWORD_灵气】（每回合限1次） | In battle, each time a 【KEYWORD_五行】 is 【KEYWORD_激活】, if that element was already 【KEYWORD_激活】, gain 1 Qi (once per turn). |
| 319 | 琴心剑胆 (Zither Heart Sword Courage) | 被动/通用 | 将自身副职业切换为琴师；所有琴师牌也视作狂剑 | Switch your side job to Musician. All Musician cards also count as Unrestrained Sword. |
| 320 | 霜寒水月 (Frost Chill Moon Water) | 被动/通用 | 每次使用云剑时，获得1层【KEYWORD_水月】 | Each time you use a Cloud Sword, gain 1 stack of 【KEYWORD_水月】. |
| 321 | 玲珑游 (Delicate Wander) | 被动/通用 | 描述中含“再次行动”的牌【KEYWORD_灵气】消耗减1 | Cards with 'Chase' in description cost 1 less 【KEYWORD_灵气】. |
| 324 | 淬剑-云海 (Tempered Blade - Cloud Sea) | 被动/通用 | 使用【澄心剑胚】时加5【KEYWORD_云海】 | When using 【澄心剑胚】, gain 5 【KEYWORD_云海】. |
| 325 | 狂剑聚灵 (Unrestrained Sword Qi Gathering) | 被动/通用 | 每次使用狂剑时加1【KEYWORD_灵气】 | Each time you use an Unrestrained Sword, gain 1 【KEYWORD_灵气】. |
| 326 | 雁栖 (Goose Perch) | 被动/通用 | 每场战斗首次加生命或生命上限后，额外加当时生命上限20%的生命 | After first HP or Max HP gain each battle, gain additional HP equal to 20% of current Max HP. |
| 327 | 恃风雷 (Rely on Wind and Thunder) | 被动/通用 | 战斗开始时，升级卡组中第1张描述含“再次行动”或名字含“雷”的牌，战斗结束后还原 | Battle start: Upgrade the first card in deck with 'Chase' in description or 'Thunder' in name. Revert after battle. |
| 328 | 金仓纳福 (Golden Granary Receives Blessings) | 被动/通用 | 每轮开始时抽到的牌中随机1张升至2级 | At round start, upgrade 1 random drawn card to level 2. |
| 329 | 谋定后动 (Plan Before Acting) | 被动/通用 | 战斗开始时若自身为后手行动，则下1次的【KEYWORD_后招】效果可直接触发 | If you act second at battle start, the next 【KEYWORD_后招】 effect triggers immediately. |
| 330 | 料敌机先 (Anticipate Enemy's Move) | 被动/通用 | 使用【算无遗策】时，获得3层临时【KEYWORD_护体】，自身下个回合开始失去临时【KEYWORD_护体】 | When using 【算无遗策】, gain 3 temporary 【KEYWORD_护体】 stacks. Lose temporary 【KEYWORD_护体】 at the start of your next turn. |
| 331 | 七星连珠 (Seven Stars Alignment) | 被动/通用 | 每场战斗前7次使用星弈牌时，令后一格【KEYWORD_成为星位】 | For the first 7 Astral Move cards used each battle, the next slot 【KEYWORD_成为星位】. |
| 332 | 引虚 (Draw Void) | 被动/通用 | 含“后招”效果的牌在首次使用时向对方施加1层【KEYWORD_虚弱】 | When a card with 'Post Action' effect is used for the first time, inflict 1 stack of 【KEYWORD_虚弱】 on opponent. |
| 333 | 天衍-金灵印记 (Heavenly Derivation - Mark of Metal Spirit) | 被动/通用 | 战斗开始时【KEYWORD_激活金灵】并加2【KEYWORD_锋锐】 | Battle start: 【KEYWORD_激活金灵】 and gain 2 【KEYWORD_锋锐】. |
| 334 | 百草织霞 (Hundred Herbs Weave Sunset Glow) | 被动/通用 | 战斗开始时，升级卡组中第1张木灵牌，战斗结束后还原 | Battle start: Upgrade the first Wood Spirit card in deck. Revert after battle. |
| 335 | 无尽棍势 (Endless Staff Stance) | 被动/通用 | 锁定自身【KEYWORD_架势】为【KEYWORD_棍】；[切换架势]的效果改为【KEYWORD_气势】上限+1 | Lock your 【KEYWORD_架势】 to 【KEYWORD_棍】. [Switch Stance] effect changes to +1 【KEYWORD_气势】 cap. |
| 336 | 风灵展翼 (Wind Spirit Spread Wings) | 被动/通用 | 战斗中首次加【KEYWORD_灵气】时，额外加5【KEYWORD_身法】 | First time gaining 【KEYWORD_灵气】 in battle, also gain 5 【KEYWORD_身法】. |
| 337 | 灵之羽 (Spirit Feather) | 被动/通用 | 每次使用【灵羽】时额外加1【KEYWORD_灵气】 | Each time you use 【灵羽】, gain 1 extra 【KEYWORD_灵气】. |
| 340 | 乘雁而行 (Ride the Wild Goose) | 被动/通用 | 战斗开始时生命上限+20；每次触发【KEYWORD_再次行动】后生命+2 | Battle start: +20 Max HP. After each 【KEYWORD_再次行动】 trigger, +2 HP. |
| 342 | 灯焰催心 (Flame Flutter Heart Torment) | 被动/通用 | 战斗开始时，令对方下3次获得【KEYWORD_内伤】时多加1层 | Battle start: For the next 3 times opponent gains 【KEYWORD_内伤】, they gain 1 extra stack. |
| 343 | 天衍-五行润养 (Heavenly Derivation - Five Elements Nourish) | 被动/通用 | 战斗开始时若卡组中含3种及以上【KEYWORD_五行】，下轮多加1生命上限；若卡组中含5种及以上【KEYWORD_五行】，下轮多加1换牌机会 | Battle start: If deck contains 3+ types of 【KEYWORD_五行】, next round +1 Max HP. If deck contains 5+ types of 【KEYWORD_五行】, next round +1 Exchange Chance. |
| 344 | 朱雀之泪 (Vermilion Bird's Tear) | 被动/通用 | 自身回合开始时，若生命≤20，获得1层【KEYWORD_护体】（每场战斗限1次） | At your turn start, if HP ≤ 20, gain 1 stack of 【KEYWORD_护体】 (once per battle). |
| 345 | 灵气引燃 (Qi Ignition) | 被动/通用 | 修为减1，获得1张【火灵秘印】； / 每次使用【火灵秘印】时，每有1【KEYWORD_灵气】额外减对方1生命及上限 | Lose 1 Cultivation, gain 1 【火灵秘印】; / Each time you use 【火灵秘印】, for each 【KEYWORD_灵气】 you have, reduce opponent's HP and Max HP by an additional 1. |
| 346 | 天衍-磨砺不止 (Heavenly Derivation - Continuous Sharpening) | 被动/通用 | 触发仙命【TALENT_151】获得换牌机会时，额外加等量【KEYWORD_体魄】上限 | When 【TALENT_151】 grants Exchange Chance, also gain an equal amount of 【KEYWORD_体魄】 cap. |
| 347 | 热血化气 (Hot Blood Turns to Qi) | 被动/通用 | 使用【KEYWORD_耗生命】的牌时加1【KEYWORD_灵气】（每回合限1次） | When using a card with 【KEYWORD_耗生命】, gain 1 【KEYWORD_灵气】 (once per turn). |
| 348 | 盈月飞影 (Full Moon Flying Shadow) | 被动/通用 | 仅需9【KEYWORD_身法】即可触发【KEYWORD_再次行动】 | Only need 9 【KEYWORD_身法】 to trigger 【KEYWORD_再次行动】. |
| 349 | 拳风破空 (Fist Wind Breaks the Sky) | 被动/通用 | 锁定自身【KEYWORD_架势】为【KEYWORD_拳】；[切换架势]的效果改为向对方造成3【KEYWORD_伤害】 | Lock your 【KEYWORD_架势】 to 【KEYWORD_拳】. [Switch Stance] effect changes to dealing 3 【KEYWORD_伤害】 to opponent. |
| 353 | 天衍-休养生息 (Heavenly Derivation - Recuperate) | 被动/通用 | 命元+18；生命上限+2；换牌机会+2； | +18 Destiny; +2 Max HP; +2 Exchange Chance |

### Category 1

| id | Name | Kind | Effect (CN) | Effect (EN) |
|---|---|---|---|---|
| 1 | 生命底蕴 (Life Reserve) | 主动-限次 | 主动使用（限1次）：获得当前轮次数的生命上限 | Use (1 charges): Gain Max HP equal to current round number. |
| 2 | 换牌底蕴 (Card Exchange Reserve) | 主动-限次 | 主动使用（限1次）：获得当前轮次数的换牌机会 | Use (1 charges): Gain Exchange Chance equal to current round number. |
| 3 | 命元底蕴 (Destiny Reserve) | 主动-限次 | 主动使用（限1次）：获得当前轮次数+8的命元 | Use (1 charges): Gain Destiny equal to current round number + 8. |
| 4 | 境界感悟 (Phase Insight) | 主动-限次 | 主动使用（限1次）：换牌机会+1，抽1张自身当前境界的门派牌 | Use (1 charges): +1 Exchange Chance. Draw 1 sect cards of your current phase. |
| 6 | 记忆案卷 (Memory Scrolls) | 主动-限次 | 主动使用（限1次）：修为减1，选择自身当前牌池中1张门派牌获得 | Use (1 charges): -1 Cultivation. Choose 1 sect card from your current card pool. |
| 7 | 斩道之法 (Dao Severing Method) | 主动-限次 | 主动使用（限2次）：修为减3，抽3张牌 | Use (2 charges): -3 Cultivation. Draw 3 cards. |
| 9 | 钻研副职 (Side Job Research) | 主动-限次 | 主动使用（限1次）：修为减1，选择自身当前牌池中1张副职牌获得 | Use (1 charges): -1 Cultivation. Choose 1 side job card from your current card pool. |
| 11 | 另辟蹊径 (Blaze a New Trail) | 主动-限次 | 主动使用（限2次）：将手牌中所有牌随机变为其他牌 | Use (2 charges): Transform all cards in hand into random cards. |
| 20 | 偷袭 (Ambush) | 主动-限次 | 主动使用（限2次）：下场战斗自身临时加6【KEYWORD_速度】 | Use (2 charges): Next battle: +6 【KEYWORD_速度】. |
| 22 | 临阵顿悟 (Battlefield Epiphany) | 主动-限次 | 主动使用（限1次）：下次突破境界所需的修为和体魄减5 | Use (1 charges): Reduces the Cultivation and Physique required for the next Phase Breakthrough by 5 |
| 23 | 强身健体 (Strengthen the Body) | 主动-限次 | 主动使用（限1次）：将【KEYWORD_体魄】加至当前体魄上限-5 | Use (1 charges): Raise 【KEYWORD_体魄】 to current Physique cap - 5. |
| 24 | 云剑修行 (Cloud Sword Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张云剑 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 Cloud Sword card. |
| 28 | 静心悟道 (Calm Enlightenment) | 主动-限次 | 主动使用（限1次）：升级卡组中第一张1级牌 | Use (1 charges): Upgrade the first level 1 card in deck. |
| 30 | 副职转换 (Side Job Change) | 主动-限次 | 主动使用（限1次）：重新选择自身的副职业，移除牌池中剩余的旧副职业的牌以及低于自身上个境界的副职业牌 | Use (1 charge): Reselect your side job. Remove remaining old side job cards and side job cards below your previous phase from pool. |
| 34 | 狂剑修行 (Unrestrained Sword Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张狂剑 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 Unrestrained Sword card. |
| 38 | 偷师学艺 (Learn from Opponent) | 主动-限次 | 主动使用（限1次）：修为减1，从上轮对手的卡组中选择1张[常规牌]获得 | Use (1 charges): -1 Cultivation. Choose 1 [regular] card from last opponent's deck. |
| 40 | 境界专精 (Phase Mastery) | 主动-限次 | 主动使用（限1次）：牌池中当前境界的所有牌数量加4 | Use (1 charges): Increase count of all current phase cards in pool by 4. |
| 41 | 梦境追忆 (Dream Recall) | 主动-限次 | 主动使用（限1次）：修为减1，从随机3张梦境牌中选择1张获得；每次突破境界时，自动提升手牌或卡组中梦境牌的境界 | Use (1 charges): -1 Cultivation. Choose 1 from 3 random Dream cards. On breakthrough, automatically raise the Phase of Dream cards in hand or deck. |
| 42 | 剑阵修行 (Sword Formation Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张剑阵牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 Sword Formation card. |
| 43 | 剑意修行 (Sword Intent Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张描述中含【KEYWORD_剑意】相关效果的门派牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 sect card with 【KEYWORD_剑意】-related effects. |
| 44 | 连击修行 (Combo Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张默认攻击次数≥2的门派牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 sect card with default attack count ≥2. |
| 45 | 星弈修行 (Astral Move Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张星弈牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 Astral Move card. |
| 46 | 卦象修行 (Hexagram Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张描述中含【KEYWORD_卦象】相关效果的门派牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 sect card with 【KEYWORD_卦象】-related effects. |
| 47 | 雷法修行 (Thunder Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张雷牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 Thunder card. |
| 48 | 后招修行 (Post Action Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张描述中含【KEYWORD_后招】相关效果的门派牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 sect card with 【KEYWORD_后招】-related effects. |
| 49 | 生命修行 (HP Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张描述中含生命相关效果的门派牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 sect card with HP-related effects. |
| 50 | 木灵修行 (Wood Spirit Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张木灵牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 Wood Spirit card. |
| 51 | 火灵修行 (Fire Spirit Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张火灵牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 Fire Spirit card. |
| 52 | 土灵修行 (Earth Spirit Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张土灵牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 Earth Spirit card. |
| 53 | 金灵修行 (Metal Spirit Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张金灵牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 Metal Spirit card. |
| 54 | 水灵修行 (Water Spirit Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张水灵牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 Water Spirit card. |
| 56 | 崩拳修行 (Crash Fist Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张崩拳牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 Crash Fist card. |
| 57 | 气势修行 (Force Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张描述中含【KEYWORD_气势】相关效果的门派牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 sect card with 【KEYWORD_气势】-related effects. |
| 58 | 体魄修行 (Physique Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张描述中含【KEYWORD_体魄】相关效果的门派牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 sect card with 【KEYWORD_体魄】-related effects. |
| 59 | 身法修行 (Agility Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张描述中含【KEYWORD_身法】相关效果的门派牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 sect card with 【KEYWORD_身法】-related effects. |
| 60 | 灵气修行 (Qi Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张描述中含【KEYWORD_灵气】相关效果的门派牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 sect card with 【KEYWORD_灵气】-related effects. |
| 61 | 防御修行 (Defense Practice) | 主动-限次 | 主动使用（限3次）：修为减1，换牌机会+1，抽1张描述中含【KEYWORD_防】相关效果的门派牌 | Use (3 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 sect card with 【KEYWORD_防】-related effects. |
| 62 | 元婴修行 (Immortality Practice) | 主动-限次 | 主动使用（限4次）：修为减1，换牌机会+1，抽1张门派牌（优先取元婴期） | Use (4 charges): -1 Cultivation, +1 Exchange Chance. Draw 1 sect card (Immortality preferred). |
| 82 | 以茶会友 (Tea Gathering) | 主动-限次 | 主动使用（限1次）：自身获得2张【云泉道茶】，其他角色在下轮开始时各获得1张【云泉道茶】 | Use (1 charges): Gain 2 copies of 【云泉道茶】; other characters each gain 1 copy of 【云泉道茶】 next round. |
| 88 | 天衍-血脉潜能 (Heavenly Derivation - Bloodline Potential) | 主动-限次 | 主动使用（限1次）：命元+3，换牌机会+1； / 每次触发【TALENT_19】抽牌后，本天衍仙命的剩余可使用次数+1 | Use (1 charges): +3 Destiny, +1 Exchange Chance; each 【TALENT_19】 draw trigger restores 1 use. |
| 105 | 剑招修行 (Sword Arts Practice) | 主动-限次 | 主动使用（限2次）：修为减4，随机获得“云剑”“狂剑”“灵剑”“剑阵”牌各一张 | Use (2 charges): -4 Cultivation. Gain 1 each of Cloud Sword, Unrestrained Sword, Spirit Sword, and Sword Formation cards. |
| 107 | 天衍-悟剑天赋 (Heavenly Derivation - Swordplay Talent) | 主动-限次 | 主动使用（限1次）：修为减1，从随机3张自身当前境界或上个境界的“剑”牌中选择1张获得并加入仙命【TALENT_189】领悟的牌中 | Use (1 charges): -1 Cultivation. Choose 1 from 3 random sword cards of current or previous phase, and add it to 【TALENT_189】's comprehended cards. |
| 113 | 天衍-血脉威能 (Heavenly Derivation - Bloodline Power) | 主动-限次 | 主动使用（限1次）：修为减1，从随机3张自身当前境界或上个境界的牌中选择1张获得； / 每次触发【TALENT_114】抽牌后，重置本天衍仙命的使用次数 | Use (1 charges): -1 Cultivation. Choose 1 from 3 random cards of current or previous phase. Each 【TALENT_114】 draw trigger resets uses. |
| 132 | 天衍-先天五行 (Heavenly Derivation - Innate Element) | 主动-限次 | 主动使用（限1次）：从随机5张不同【KEYWORD_五行】的牌中选择1张获得，并将自身的【TALENT_109】改为该【KEYWORD_五行】 | Use (1 charges): Choose 1 from 5 random cards of different 【KEYWORD_五行】, and change your 【TALENT_109】 to that element. |
| 259 | 阵纹雕琢 (Formation Rune Engraving) | 主动-限次 | 主动使用（限2次）：升级卡组中第1张【KEYWORD_持续】牌 | Use (2 charges): Upgrade the first 【KEYWORD_持续】 card in deck. |
| 260 | 变异浇灌 (Mutant Watering) | 主动-限次 | 主动使用（限2次）：令手牌中随机1张可[变异]的灵植牌[变异] | Use (2 charges): [Mutate] 1 random spirit plant card in hand that can [Mutate]. |
| 273 | 随心悟道 (Spontaneous Enlightenment) | 主动-限次 | 主动使用（限1次）：随机升级手牌或卡组中的1张元婴期或化神期牌 | Use (1 charges): Upgrade 1 random Immortality or Incarnation card in hand or deck. |
| 274 | 炼气强化 (Meditation Enhancement) | 主动-限次 | 主动使用（限2次）：随机升级手牌或卡组中1张炼气期【KEYWORD_常规牌】 | Use (2 charges): Upgrade 1 random Meditation phase 【KEYWORD_常规牌】 in hand or deck. |
| 339 | 天衍-斩断俗尘 (Heavenly Derivation - Sever Mundane Ties) | 主动-限次 | 主动使用（限1次）：剩余换牌机会减半，删除当前牌池中所有筑基期牌 | Use (1 charges): Halve remaining Exchange Chance. Remove all Foundation phase cards from current pool. |
| 341 | 逆转乾坤 (Reverse Fate) | 主动-限次 | 主动使用（限2次）：将手牌中1张【坤卦】变为1级【乾卦】并送入未来，到第12轮返回手牌（已到第12轮后改为下1轮返回手牌） | Use (2 charges): Transform 1 【坤卦】 in hand into level 1 【乾卦】 and send to future. It returns to hand on round 12 (if already past 12, returns next round). |

### Category 2

| id | Name | Kind | Effect (CN) | Effect (EN) |
|---|---|---|---|---|
| 5 | 勤修 (Diligent Training) | 主动-冷却 | 主动使用（冷却6轮）：修为+1，生命上限减2 | Use (6-round cooldown): Cultivation +1, Max HP -2. |
| 10 | 副职大师 (Side Job Master) | 主动-冷却 | 主动使用（冷却2轮）：修为减1，抽1张副职牌（优先取元婴期以上） | Use (2-round cooldown): -1 Cultivation. Draw 1 side job card (Prioritize Immortality phase or higher). |
| 13 | 三思抉择 (Thrice-Pondered Choice) | 主动-冷却 | 主动使用（冷却3轮）：修为减1，从随机3张牌中选择1张获得 | Use (3-round cooldown): -1 Cultivation. Choose 1 card from 3 random cards. |
| 25 | 云剑大师 (Cloud Sword Master) | 主动-冷却 | 主动使用（冷却2轮）：修为减1，抽1张云剑牌（优先取元婴期以上） | Use (2-round cooldown): -1 Cultivation. Draw 1 Cloud Sword card (Prioritize Immortality phase or higher). |
| 35 | 剑阵大师 (Sword Formation Master) | 主动-冷却 | 主动使用（冷却2轮）：修为减1，抽1张剑阵牌（优先取元婴期以上） | Use (2-round cooldown): -1 Cultivation. Draw 1 Sword Formation card (Prioritize Immortality phase or higher). |
| 37 | 天衍-触类旁通 (Heavenly Derivation - Comprehensive Learning) | 主动-冷却 | 主动使用（冷却2轮）：修为减1，从随机5张其他副职业牌（金丹期以上）中选择1张获得 | Use (2-round cooldown): -1 Cultivation. Choose 1 from 5 random side job cards (Virtuoso+). |
| 55 | 五行大师 (Five Elements Master) | 主动-冷却 | 主动使用（冷却2轮）：修为减1，抽1张【KEYWORD_五行】牌（优先取元婴期以上，且和卡组第一格所属五行相同的牌） | Use (2-round cooldown): -1 Cultivation. Draw 1 【KEYWORD_五行】 card (Prioritize Immortality or above, matching deck slot 1 element). |
| 135 | 灵阵回响 (Spirit Formation Echo) | 主动-冷却 | 每场战斗中首次使用名字含“灵阵”的牌后重复一次其效果，但自身下1回合无法行动 / 主动使用：禁用本天衍仙命的效果；再次使用解除禁用 | First time using a card with 'Spirit Formation' in its name each battle, repeat its effect, but you cannot act next round. / Use: Disable the effect of this Heavenly Derivation Fate; use again to lift the disablement |
| 164 | 枯荣往复 (Wither and Bloom Cycle) | 主动-冷却 | 双方在各自回合开始时触发的每层【KEYWORD_恢复】/【KEYWORD_内伤】效果从加/减1生命改为2生命。 / 主动使用：禁用本天衍仙命的效果；再次使用解除禁用 | Each stack of 【KEYWORD_恢复】/【KEYWORD_内伤】 triggered at the start of each player's turn changes from +/-1 HP to +/-2 HP. / Use: Disable the effect of this Heavenly Derivation Fate; use again to lift the disablement |
| 264 | 灵剑大师 (Spirit Sword Master) | 主动-冷却 | 主动使用（冷却2轮）：修为减1，抽1张灵剑牌（优先取元婴期以上） | Use (2-round cooldown): -1 Cultivation. Draw 1 Spirit Sword card (Prioritize Immortality phase or higher). |
| 265 | 剑意大师 (Sword Intent Master) | 主动-冷却 | 主动使用（冷却2轮）：修为减1，抽1张描述中含【KEYWORD_剑意】相关效果的门派牌（优先取元婴期以上） | Use (2-round cooldown): -1 Cultivation. Draw 1 sect card with 【KEYWORD_剑意】 effects (Prioritize Immortality phase or higher). |
| 266 | 混元大师 (Primordial Master) | 主动-冷却 | 主动使用（冷却2轮）：修为减1，抽1张名字中含“混元”的门派牌 | Use (2-round cooldown): -1 Cultivation. Draw 1 sect card with 'Primordial' in its name. |
| 267 | 星弈大师 (Astral Move Master) | 主动-冷却 | 主动使用（冷却2轮）：修为减1，抽1张星弈牌（优先取元婴期以上） | Use (2-round cooldown): -1 Cultivation. Draw 1 Astral Move card (Prioritize Immortality phase or higher). |
| 268 | 卦象大师 (Hexagram Master) | 主动-冷却 | 主动使用（冷却2轮）：修为减1，抽1张描述中含【KEYWORD_卦象】相关效果的门派牌（优先取元婴期以上） | Use (2-round cooldown): -1 Cultivation. Draw 1 sect card with 【KEYWORD_卦象】 effects (Prioritize Immortality phase or higher). |
| 269 | 崩拳大师 (Crash Fist Master) | 主动-冷却 | 主动使用（冷却2轮）：修为减1，抽1张崩拳牌（优先取元婴期以上） | Use (2-round cooldown): -1 Cultivation. Draw 1 Crash Fist card (Prioritize Immortality phase or higher). |
| 270 | 体魄大师 (Physique Master) | 主动-冷却 | 主动使用（冷却2轮）：修为减1，抽1张描述中含【KEYWORD_体魄】相关效果的门派牌（优先取元婴期以上） | Use (2-round cooldown): -1 Cultivation. Draw 1 sect card with 【KEYWORD_体魄】 effects (Prioritize Immortality phase or higher). |
| 271 | 修玄大师 (Mystery Cultivation Master) | 主动-冷却 | 主动使用（冷却2轮）：修为减1，抽1张描述中含【KEYWORD_负面状态】相关效果的门派牌（优先取元婴期以上） | Use (2-round cooldown): -1 Cultivation. Draw 1 sect card with 【KEYWORD_负面状态】 effects (Prioritize Immortality phase or higher). |
| 272 | 再动大师 (Chase Master) | 主动-冷却 | 主动使用（冷却2轮）：修为减1，抽1张描述中含【KEYWORD_再次行动】或【KEYWORD_身法】相关效果的门派牌（优先取元婴期以上） | Use (2-round cooldown): -1 Cultivation. Draw 1 sect card with 【KEYWORD_再次行动】 or 【KEYWORD_身法】 effects (Prioritize Immortality phase or higher). |
| 298 | 护身法宝 (Protective Artifact) | 主动-冷却 | 主动使用（冷却2轮）：下场战斗开始时，获得2层【KEYWORD_护体】 | Use (2-round cooldown): Next battle: gain 2 stacks of 【KEYWORD_护体】. |
| 301 | 背孤击虚 (Strike the Void from Behind) | 主动-冷却 | 到达第13轮后：修为减1，获得1张【背孤】； / 主动使用（第13轮解锁）：将【背孤】变为【击虚】，或反向变回 | Round 13+: -1 Cultivation, gain 1 【背孤】. / Use (unlocks round 13): Transform 【背孤】 into 【击虚】, or reverse. |
| 322 | 猫之狂念 (Cat's Madness) | 主动-冷却 | 名字含“猫”的牌也视作狂剑； / 主动使用（冷却3轮）：将手牌中1张名字含猫的牌变为随机狂剑（继承等级）；若没有可转变的牌，则改为减1修为，抽1张狂剑 | Cards with 'Cat' in name also count as Unrestrained Sword. / Use (3-round cooldown): Transform 1 cat card in hand into a random Unrestrained Sword (inherits level); If there are no transformable cards, instead lose 1 Cultivation and draw 1 Unrestrained Sword card. |
| 323 | 地火锻心 (Earth Fire Forge Heart) | 主动-冷却 | 主动使用（冷却1轮）：选择一个自身已有的【澄心剑胚】相关仙命，重新选择其选项 | Use (1-round cooldown): Select an chosen Immortal Fate related to 【澄心剑胚】 and reselect its options. |
| 350 | 铜镜（能品） (Bronze Mirror (Capacity Grade)) | 主动-冷却 | 主动使用（冷却3轮）：修为减1，命元减2（最低减至1），选择手牌或卡组中一张金丹期或以下境界的【KEYWORD_常规牌】，获得其1级复制 | Use (3-round cooldown): -1 Cultivation, -2 Destiny (min 1). Choose a Virtuoso or lower phase 【KEYWORD_常规牌】 in hand or deck, gain a level 1 copy. |
| 351 | 铜镜（妙品） (Bronze Mirror (Marvel Grade)) | 主动-冷却 | 主动使用（冷却3轮）：修为减1，命元减4（最低减至1），选择手牌或卡组中一张元婴期或以下境界的【KEYWORD_常规牌】，获得其1级复制 | Use (3-round cooldown): -1 Cultivation, -4 Destiny (min 1). Choose an Immortality or lower phase 【KEYWORD_常规牌】 in hand or deck, gain a level 1 copy. |
| 352 | 铜镜（神品） (Bronze Mirror (Divine Grade)) | 主动-冷却 | 主动使用（冷却3轮）：修为减1，命元减6（最低减至1），选择手牌或卡组中一张化神期或以下境界的【KEYWORD_常规牌】，获得其1级复制 | Use (3-round cooldown): -1 Cultivation, -6 Destiny (min 1). Choose an Incarnation or lower phase 【KEYWORD_常规牌】 in hand or deck, gain a level 1 copy. |

### Category 3

| id | Name | Kind | Effect (CN) | Effect (EN) |
|---|---|---|---|---|
| 170 | 云剑·龙泉 (Cloud Sword - Dragon Spring) | 被动 | 可在手牌中根据公式合成卡牌： / 【云泉道茶】+【云剑•游龙】=【云剑•龙泉】 | Fuse in hand: 【云泉道茶】+【云剑•游龙】=【云剑•龙泉】. |
| 171 | 云剑·雪影飞 (Cloud Sword - Flying Snow Shade) | 被动 | 可在手牌中根据公式合成卡牌： / 【云剑•崩雪】+【飞灵闪影剑】=【云剑•雪影飞】 | Fuse in hand: 【云剑•崩雪】+【飞灵闪影剑】=【云剑•雪影飞】. |
| 172 | 百鸟玲珑镯 (CentiBird Delicate Bracelet) | 被动 | 可在手牌中根据公式合成卡牌： / 【九霄玲珑镯】+【百鸟灵剑诀】=【百鸟玲珑镯】 | Fuse in hand: 【九霄玲珑镯】+【百鸟灵剑诀】=【百鸟玲珑镯】. |
| 173 | 狂剑·猫爪 (Unrestrained Sword - Cat Claw) | 被动 | 可在手牌中根据公式合成卡牌： / 【云剑•猫爪】+【狂剑•二式】=【狂剑•猫爪】 | Fuse in hand: 【云剑•猫爪】+【狂剑•二式】=【狂剑•猫爪】. |
| 174 | 澄心剑阵 (Clear Heart Sword Formation) | 被动 | 可在手牌中根据公式合成卡牌： / 【御空剑阵】+【连环剑阵】=【澄心剑阵】 | Fuse in hand: 【御空剑阵】+【连环剑阵】=【澄心剑阵】. |
| 175 | 百鸟曳影诀 (CentiBird Swift Shadow Art) | 被动 | 可在手牌中根据公式合成卡牌： / 【曳影剑阵】+【百鸟灵剑诀】=【百鸟曳影诀】 | Fuse in hand: 【曳影剑阵】+【百鸟灵剑诀】=【百鸟曳影诀】. |
| 176 | 瑞雪迎春 (Traces Revitalized) | 被动 | 可在手牌中根据公式合成卡牌： / 【飞鸿踏雪】+【枯木逢春】=【瑞雪迎春】 | Fuse in hand: 【飞鸿踏雪】+【枯木逢春】=【瑞雪迎春】. |
| 177 | 天元无极盘 (Polaris Ultimate Base) | 被动 | 可在手牌中根据公式合成卡牌： / 【无极卦盘】+【天元心法】=【天元无极盘】 | Fuse in hand: 【无极卦盘】+【天元心法】=【天元无极盘】. |
| 178 | 灯影蚀焰 (Suspicious Flame Flutter) | 被动 | 可在手牌中根据公式合成卡牌： / 【灯焰飞舞】+【杯弓蛇影】=【灯影蚀焰】 | Fuse in hand: 【灯焰飞舞】+【杯弓蛇影】=【灯影蚀焰】. |
| 179 | 千星天爆 (Thousand Star Explosion) | 被动 | 可在手牌中根据公式合成卡牌： / 【星爆术】+【星轨推衍】=【千星天爆】 | Fuse in hand: 【星爆术】+【星轨推衍】=【千星天爆】. |
| 180 | 星月六爻扇 (Star Moon Six Lines Fan) | 被动 | 可在手牌中根据公式合成卡牌： / 【星月折扇】+【六爻绝阵】=【星月六爻扇】 | Fuse in hand: 【星月折扇】+【六爻绝阵】=【星月六爻扇】. |
| 181 | 星弈·治孤 (Astral Move - Rescue) | 被动 | 可在手牌中根据公式合成卡牌： / 【孤虚金书】+【星弈•飞】=【星弈•治孤】 | Fuse in hand: 【孤虚金书】+【星弈•飞】=【星弈•治孤】. |
| 182 | 天髓葫芦 (Heavenly Marrow Gourd) | 被动 | 可在手牌中根据公式合成卡牌： / 【悠然葫芦】+【五行天髓诀】=【天髓葫芦】 | Fuse in hand: 【悠然葫芦】+【五行天髓诀】=【天髓葫芦】. |
| 183 | 混元逆克阵 (Primordial Reverse Overcome Formation) | 被动 | 可在手牌中根据公式合成卡牌： / 【双鸳逆克】+【混元无极阵】=【混元逆克阵】 | Fuse in hand: 【双鸳逆克】+【混元无极阵】=【混元逆克阵】. |
| 184 | 木灵·万物生 (Wood Spirit - All Things Grow) | 被动 | 可在手牌中根据公式合成卡牌： / 【水灵•春雨】+【木灵•柳纷飞】=【木灵•万物生】 | Fuse in hand: 【水灵•春雨】+【木灵•柳纷飞】=【木灵•万物生】. |
| 185 | 锟铻熔火环 (Kun Wu Molten Ring) | 被动 | 可在手牌中根据公式合成卡牌： / 【锟铻金环】+【火灵印】=【锟铻熔火环】 | Fuse in hand: 【锟铻金环】+【火灵印】=【锟铻熔火环】. |
| 186 | 水火交融 (Harmony of Water and Fire) | 被动 | 可在手牌中根据公式合成卡牌： / 【水灵秘印】+【火灵•瞬燃】=【水火交融】 | Fuse in hand: 【水灵秘印】+【火灵•瞬燃】=【水火交融】. |
| 187 | 五行忘忧梦 (Five Elements Carefree Dream) | 被动 | 可在手牌中根据公式合成卡牌： / 【忘忧】+【五行流转】=【五行忘忧梦】 | Fuse in hand: 【忘忧】+【五行流转】=【五行忘忧梦】. |
| 188 | 浩荡不息 (Unceasing Universe) | 被动 | 可在手牌中根据公式合成卡牌： / 【锻体不息】+【天地浩荡】=【浩荡不息】 | Fuse in hand: 【锻体不息】+【天地浩荡】=【浩荡不息】. |
| 189 | 玄心盛气掌 (Soul Overwhelming Palm) | 被动 | 可在手牌中根据公式合成卡牌： / 【盛气凌人】+【玄心斩魄】=【玄心盛气掌】 | Fuse in hand: 【盛气凌人】+【玄心斩魄】=【玄心盛气掌】. |
| 190 | 冥夜迷踪步 (Styx Night Footwork) | 被动 | 可在手牌中根据公式合成卡牌： / 【崩拳·冥夜】+【灵玄迷踪步】=【冥夜迷踪步】 | Fuse in hand: 【崩拳·冥夜】+【灵玄迷踪步】=【冥夜迷踪步】. |
| 191 | 崩拳·返玄 (Crash Fist - Return to Xuan) | 被动 | 可在手牌中根据公式合成卡牌： / 【冥心入玄】+【崩拳•弹】=【崩拳•返玄】 | Fuse in hand: 【冥心入玄】+【崩拳•弹】=【崩拳•返玄】. |
| 192 | 闪转腾挪 (Dodge and Weave) | 被动 | 可在手牌中根据公式合成卡牌： / 【转势】+【崩拳•闪击】=【闪转腾挪】 | Fuse in hand: 【转势】+【崩拳•闪击】=【闪转腾挪】. |
| 193 | 冯虚御风 (Riding the Wind) | 被动 | 可在手牌中根据公式合成卡牌： / 【御风飞闪】+【灵玄迷踪步】=【冯虚御风】 | Fuse in hand: 【御风飞闪】+【灵玄迷踪步】=【冯虚御风】. |

### Category 4

| id | Name | Kind | Effect (CN) | Effect (EN) |
|---|---|---|---|---|
| 8 | 命途-副职兼修 (Fate Path - Additional Side Job) | 被动 | 每次突破时仙命选项必然包含【TALENT_188】 | Each breakthrough, Immortal Fate options always include 【TALENT_188】. |
| 63 | 命途-机缘造化 (Fate Path - Fortunes and Luck) | 被动 | 每次突破时仙命选项必然包含【TALENT_53】；[炼化]机缘牌时额外加5换牌机会 | Each breakthrough, Immortal Fate options always include 【TALENT_53】; Absorbing fortune cards grants 5 extra Exchange Chance. |
| 64 | 命途-陨星淬体 (Fate Path - Meteor Quench) | 被动 | 每次突破时仙命选项必然包含【TALENT_59】；【TALENT_59】扣减的命元减半 | Each breakthrough, Immortal Fate options always include 【TALENT_59】; 【TALENT_59】 Destiny cost halved. |
| 65 | 命途-云巅雷劫 (Fate Path - Thunder Tribulation) | 被动 | 每次突破时仙命选项必然包含【TALENT_9】 | Each breakthrough, Immortal Fate options always include 【TALENT_9】 |
| 66 | 命途-变换之道 (Fate Path - The Way of Adaptation) | 被动 | 每轮多加1次换牌机会但换牌机会储存上限变为1；每次突破时仙命选项必然包含【TALENT_6】 | Gain 1 extra Exchange Chance each round but Exchange Chance storage cap becomes 1; each breakthrough, Immortal Fate options always include 【TALENT_6】. |
| 67 | 命途-储纳灵气 (Fate Path - Store Qi) | 被动 | 每次突破时仙命选项必然包含【TALENT_13】 | Each breakthrough, Immortal Fate options always include 【TALENT_13】. |
| 68 | 命途-狂之执念 (Fate Path - Mad Obsession) | 被动 | 每次突破时仙命选项必然包含【TALENT_70】 | Each breakthrough, Immortal Fate options always include 【TALENT_70】. |
| 69 | 命途-云之道 (Fate Path - Rule Of The Cloud) | 被动 | 每次突破时仙命选项必然包含【TALENT_69】；选择【TALENT_69】时减1修为，抽1张当前境界的云剑牌 | Each breakthrough, Immortal Fate options always include 【TALENT_69】; when 【TALENT_69】 is selected, -1 Cultivation, draw 1 Cloud Sword card of current phase. |
| 70 | 命途-剑韵修炼 (Fate Path - Sword Rhyme Cultivate) | 被动 | 每次突破时仙命选项必然包含【TALENT_16】；选择【TALENT_16】时减1修为，抽1张描述中含【KEYWORD_剑意】相关效果的牌 | Each breakthrough, Immortal Fate options always include 【TALENT_16】; when 【TALENT_16】 is selected, -1 Cultivation, draw 1 card with 【KEYWORD_剑意】-related effects. |
| 71 | 命途-剑阵守护 (Fate Path - Sword Formation Guard) | 被动 | 每次突破时仙命选项必然包含【TALENT_57】 | Each breakthrough, Immortal Fate options always include 【TALENT_57】. |
| 72 | 命途-卜卦 (Fate Path - Divination) | 被动 | 每次突破时仙命选项必然包含【TALENT_30】 | Each breakthrough, Immortal Fate options always include 【TALENT_30】. |
| 73 | 命途-观星 (Fate Path - Stargaze) | 被动 | 每次突破时仙命选项必然包含【TALENT_31】 | Each breakthrough, Immortal Fate options always include 【TALENT_31】. |
| 74 | 命途-星蚀 (Fate Path - Astral Eclipse) | 被动 | 每次突破时仙命选项必然包含【TALENT_103】 | Each breakthrough, Immortal Fate options always include 【TALENT_103】. |
| 75 | 命途-妙手回春 (Fate Path - Rejuvenation) | 被动 | 每次突破时仙命选项必然包含【TALENT_120】；选择【TALENT_120】时修为减1，抽1张描述中含生命相关效果的门派牌 | Each breakthrough, Immortal Fate options always include 【TALENT_120】; when 【TALENT_120】 is selected, -1 Cultivation, draw 1 sect card with HP-related effects. |
| 76 | 命途-五行循环 (Fate Path - Cycle Of Five Elements) | 被动 | 每次突破时仙命选项必然包含【TALENT_102】 | Each breakthrough, Immortal Fate options always include 【TALENT_102】. |
| 77 | 命途-五行专一 (Fate Path - Concentrated Element) | 被动 | 每次突破时仙命选项必然包含【TALENT_128】 | Each breakthrough, Immortal Fate options always include 【TALENT_128】. |
| 78 | 命途-体修入道 (Fate Path - Physique Master) | 被动 | 体魄上限+1；每次突破时仙命选项必然包含【TALENT_146】 | +1 Physique cap. On breakthrough, Immortal Fate options always include 【TALENT_146】. |
| 79 | 命途-气势充沛 (Fate Path - Full of Force) | 被动 | 每次突破时仙命选项必然包含【TALENT_145】；选择【TALENT_145】时减1修为，抽1张描述中含【KEYWORD_气势】相关效果的牌 | Each breakthrough, Immortal Fate options always include 【TALENT_145】; when 【TALENT_145】 is selected, -1 Cultivation, draw 1 card with 【KEYWORD_气势】-related effects. |
| 80 | 命途-冥心烙印 (Fate Path - Mark of Dark Heart) | 被动 | 每次突破时仙命选项必然包含【TALENT_150】；选择【TALENT_150】时减1修为，抽1张描述中含[负面状态]相关效果的门派牌 | Each breakthrough, Immortal Fate options always include 【TALENT_150】; when 【TALENT_150】 is selected, -1 Cultivation, draw 1 sect card with Debuff-related effects. |
| 81 | 命途-再生之躯 (Fate Path - Regenerating Body) | 被动 | 每次突破时仙命选项必然包含【TALENT_149】 | Each breakthrough, Immortal Fate options always include 【TALENT_149】. |

### Category 5

| id | Name | Kind | Effect (CN) | Effect (EN) |
|---|---|---|---|---|
| 17 | 道韵气息 (Daoist Rhyme Aura) | 战斗 | 到达第13轮后：修为减2，获得2张【道韵气息】 | Round 13+: -2 Cultivation, gain 2 【道韵气息】. |
| 83 | 天衍-云泉道茶 (Heavenly Derivation - Spring Course Tea) | 战斗 | 到达第13轮后：修为减2，获得2张【云泉道茶】 | Round 13+: -2 Cultivation, gain 2 【云泉道茶】. |
| 86 | 天衍-炎舞 (Heavenly Derivation - Flame Dance) | 战斗 | 到达第13轮后：修为减1，获得1张【狂剑•炎舞】 | Round 13+: -1 Cultivation, gain 1 【狂剑•炎舞】. |
| 87 | 天衍-崩雪 (Heavenly Derivation - Avalanche) | 战斗 | 到达第10轮后：修为减1，获得1张【云剑•崩雪】 | Round 10+: -1 Cultivation, gain 1 【云剑•崩雪】. |
| 90 | 天衍-九霄玲珑镯 (Heavenly Derivation - Sky Delicate Bracelet) | 战斗 | 到达第13轮后：修为减1，获得1张【九霄玲珑镯】 | Round 13+: -1 Cultivation, gain 1 【九霄玲珑镯】. |
| 91 | 天衍-唤雨 (Heavenly Derivation - Pray Rain) | 战斗 | 到达第10轮后：修为减1，获得1张【云剑•唤雨】 | Round 10+: -1 Cultivation, gain 1 【云剑•唤雨】. |
| 92 | 天衍-潜龙 (Heavenly Derivation - Hidden Loong) | 战斗 | 修为减2，获得2张【云剑•潜龙】 | -2 Cultivation, gain 2 【云剑•潜龙】. |
| 93 | 天衍-玲珑剑阵 (Heavenly Derivation - Exquisite Sword Formation) | 战斗 | 到达第9轮后：修为减1，获得1张【玲珑剑阵】 | Round 9+: -1 Cultivation, gain 1 【玲珑剑阵】. |
| 94 | 天衍-猫爪 (Heavenly Derivation - Cat Paw) | 战斗 | 到达第4轮后：修为减2，获得2张【云剑•猫爪】 | Round 4+: -2 Cultivation, gain 2 【云剑•猫爪】. |
| 96 | 天衍-灵猫乱剑 (Heavenly Derivation - Spirit Cat Chaos Sword) | 战斗 | 到达第11轮后：修为减1，获得1张【灵猫乱剑】 | Round 11+: -1 Cultivation, gain 1 【灵猫乱剑】. |
| 98 | 天衍-飞砂 (Heavenly Derivation - Flying Sand) | 战斗 | 修为减2，获得2张【云剑•飞砂】 | -2 Cultivation, gain 2 【云剑•飞砂】. |
| 108 | 天衍-曳影剑阵 (Heavenly Derivation - Swift Shadow Sword Formation) | 战斗 | 到达第12轮后：修为减1，获得1张【曳影剑阵】；【曳影剑阵】将同时视作“云剑”“狂剑”“灵剑”和“剑阵” | Round 12+: -1 Cultivation, gain 1 【曳影剑阵】; 【曳影剑阵】 counts as Cloud Sword, Unrestrained Sword, Spirit Sword, and Sword Formation simultaneously. |
| 111 | 天衍-飞鸿踏雪 (Heavenly Derivation - Only Traces) | 战斗 | 到达第10轮后：修为减1，获得1张【飞鸿踏雪】 | Round 10+: -1 Cultivation, gain 1 【飞鸿踏雪】. |
| 112 | 天衍-瓮中捉鳖 (Heavenly Derivation - Within Reach) | 战斗 | 到达第10轮后：修为减1，获得1张【瓮中捉鳖】 | Round 10+: -1 Cultivation, gain 1 【瓮中捉鳖】. |
| 114 | 天衍-无极卦盘 (Heavenly Derivation - Ultimate Hexagram Base) | 战斗 | 到达第6轮后：修为减1，获得1张【无极卦盘】 | Round 6+: -1 Cultivation, gain 1 【无极卦盘】. |
| 115 | 天衍-狂雷电闪 (Heavenly Derivation - Fury Thunder) | 战斗 | 到达第13轮后：修为减1，获得1张【狂雷电闪】 | Round 13+: -1 Cultivation, gain 1 【狂雷电闪】. |
| 117 | 天衍-灯焰飞舞 (Heavenly Derivation - Flame Flutter) | 战斗 | 到达第6轮后：修为减1，获得1张【灯焰飞舞】 | Round 6+: -1 Cultivation, gain 1 【灯焰飞舞】. |
| 118 | 天衍-旋灯占卦 (Heavenly Derivation - Rotary Divination Hexagram) | 战斗 | 到达第10轮后：修为减1，获得1张【旋灯占卦】 | Round 10+: -1 Cultivation, gain 1 【旋灯占卦】. |
| 122 | 天衍-星爆术 (Heavenly Derivation - Starburst) | 战斗 | 到达第7轮后：修为减2，获得2张【星爆术】 | Round 7+: -2 Cultivation, gain 2 【星爆术】. |
| 123 | 天衍-星月折扇 (Heavenly Derivation - Star Moon Folding Fan) | 战斗 | 到达第11轮后：修为减1，获得1张【星月折扇】 | Round 11+: -1 Cultivation, gain 1 【星月折扇】. |
| 125 | 天衍-算无遗策 (Heavenly Derivation - Perfectly Planned) | 战斗 | 修为减1，获得1张【算无遗策】 | -1 Cultivation, gain 1 【算无遗策】. |
| 129 | 天衍-悠然葫芦 (Heavenly Derivation - Gourd Of Leisurely) | 战斗 | 到达第5轮后：修为减1，获得1张【悠然葫芦】 | Round 5+: -1 Cultivation, gain 1 【悠然葫芦】. |
| 130 | 天衍-五行传承 (Heavenly Derivation - Inheritance of Five Elements) | 战斗 | 到达第14轮后：修为减1，获得1张【五行传承】 | Round 14+: -1 Cultivation, gain 1 【五行传承】. |
| 134 | 天衍-双鸳逆克 (Heavenly Derivation - Overcome with each other) | 战斗 | 到达第9轮后：修为减2，获得2张【双鸳逆克】 | Round 9+: -2 Cultivation, gain 2 【双鸳逆克】. |
| 136 | 天衍-桃花印 (Heavenly Derivation - Peach Blossom Seal) | 战斗 | 修为减1，获得1张【木灵•桃花印】 | -1 Cultivation, gain 1 【木灵•桃花印】. |
| 139 | 天衍-春雨 (Heavenly Derivation - Spring Rain) | 战斗 | 到达第9轮后：修为减1，获得1张【水灵•春雨】 | Round 9+: -1 Cultivation, gain 1 【水灵•春雨】. |
| 141 | 天衍-山崩 (Heavenly Derivation - Landslide) | 战斗 | 到达第13轮后：修为减1，获得1张【土灵•山崩】 | Round 13+: -1 Cultivation, gain 1 【土灵•山崩】. |
| 142 | 天衍-锟铻金环 (Heavenly Derivation - Kun Wu Metal Ring) | 战斗 | 到达第6轮后：修为减1，获得1张【锟铻金环】 | Round 6+: -1 Cultivation, gain 1 【锟铻金环】. |
| 144 | 天衍-刚劲 (Heavenly Derivation - Vigorous) | 战斗 | 到达第10轮后：修为减1，获得1张【金灵•刚劲】 | Round 10+: -1 Cultivation, gain 1 【金灵•刚劲】. |
| 150 | 天衍-锻体不息 (Heavenly Derivation - Unceasing Exercising) | 战斗 | 到达第4轮后：修为减2，获得2张【锻体不息】 | Round 4+: -2 Cultivation, gain 2 【锻体不息】. |
| 156 | 天衍-盛气凌人 (Heavenly Derivation - Overwhelming Power) | 战斗 | 修为减1，获得1张【盛气凌人】 | -1 Cultivation, gain 1 【盛气凌人】. |
| 157 | 天衍-疯魔 (Heavenly Derivation - Gone Crazy) | 战斗 | 到达第5轮后：修为减1，获得1张【疯魔】 | Round 5+: -1 Cultivation, gain 1 【疯魔】. |
| 158 | 天衍-冥夜 (Heavenly Derivation - Styx Night) | 战斗 | 到达第10轮后：修为减1，获得1张【崩拳·冥夜】 | Round 10+: -1 Cultivation, gain 1 【崩拳·冥夜】. |
| 159 | 天衍-冥月蟾光 (Heavenly Derivation - Styx Moon's Glow) | 战斗 | 到达第12轮后：修为减1，获得1张【冥月蟾光】 | Round 12+: -1 Cultivation, gain 1 【冥月蟾光】. |
| 162 | 天衍-万玄破魔掌 (Heavenly Derivation - Wan Xuan Demon Breaking Palm) | 战斗 | 到达第13轮后：修为减1，获得1张【万玄破魔掌】 | Round 13+: -1 Cultivation, gain 1 【万玄破魔掌】. |
| 165 | 天衍-冥心入玄 (Heavenly Derivation - Meditation of Xuan) | 战斗 | 到达第8轮后：修为减1，获得1张【冥心入玄】 | Round 8+: -1 Cultivation, gain 1 【冥心入玄】. |
| 167 | 天衍-拆招 (Heavenly Derivation - Counter Move) | 战斗 | 修为减1，获得1张【拆招】 | -1 Cultivation, gain 1 【拆招】. |
| 168 | 天衍-双节棍 (Heavenly Derivation - Double Stick) | 战斗 | 修为减1，获得1张【双节棍】 | -1 Cultivation, gain 1 【双节棍】. |
| 169 | 天衍-转势 (Heavenly Derivation - Shift Stance) | 战斗 | 到达第10轮后：修为减2，获得2张【转势】 | Round 10+: -2 Cultivation, gain 2 【转势】. |
| 296 | 影枭兔 (Shadow Owl Rabbit) | 战斗 | 到达第14轮后：修为减1，获得1张【影枭兔】 | Round 14+: -1 Cultivation, gain 1 【影枭兔】. |
| 297 | 龙 (Loong) | 战斗 | 到达第15轮后：修为减1，获得1张【龙】 | Round 15+: -1 Cultivation, gain 1 【龙】. |
| 300 | 天衍-阴符玉简 (Heavenly Derivation - Jade Scroll of Yin Symbol) | 战斗 | 修为减1，获得1张【阴符玉简】 | -1 Cultivation, gain 1 【阴符玉简】. |
| 302 | 天衍-定风波 (Heavenly Derivation - Settle the Storm) | 战斗 | 到达第5轮后：修为减1，获得1张【定风波】 | Round 5+: -1 Cultivation, gain 1 【定风波】. |
| 304 | 天衍-灵羽 (Heavenly Derivation - Spirit Feather) | 战斗 | 到达第7轮后：修为减2，获得2张【灵羽】 | Round 7+: -2 Cultivation, gain 2 【灵羽】. |
| 305 | 天衍-气旋掌 (Heavenly Derivation - Cyclone Palm) | 战斗 | 到达第9轮后：修为减1，获得1张【气旋掌】 | Round 9+: -1 Cultivation, gain 1 【气旋掌】. |
| 306 | 天衍-御风飞闪 (Heavenly Derivation - Wind-Riding Flash) | 战斗 | 到达第10轮后：修为减1，获得1张【御风飞闪】 | Round 10+: -1 Cultivation, gain 1 【御风飞闪】. |
| 307 | 天衍-天降甘霖 (Heavenly Derivation - Heavenly Rain) | 战斗 | 到达第5轮后：修为减1，获得1张【天降甘霖】 | Round 5+: -1 Cultivation, gain 1 【天降甘霖】. |
| 308 | 天衍-忘忧 (Heavenly Derivation - Forget Worries) | 战斗 | 到达第12轮后：修为减1，获得1张【忘忧】 | Round 12+: -1 Cultivation, gain 1 【忘忧】. |
| 338 | 天衍-孤虚金书 (Heavenly Derivation - Solitary Void Golden Tome) | 战斗 | 到达第13轮后：修为减1，获得1张【孤虚金书】； / 战斗开始时若【孤虚金书】前一格为空则放入【背孤】，若后一格为空则放入【击虚】，前后每有一格未能放入牌就改为让【孤虚金书】升1级（战斗结束还原） | Round 13+: -1 Cultivation, gain 1 【孤虚金书】. Battle start: if previous slot of 【孤虚金书】 is empty, place 【背孤】 there; if next slot is empty, place 【击虚】 there. For each slot that cannot be filled, upgrade 【孤虚金书】 by 1 level (revert after battle). |

### Category 6

| id | Name | Kind | Effect (CN) | Effect (EN) |
|---|---|---|---|---|
| 127 | 水灵•悠然 (Water Spirit - Leisurely) | 被动 | 牌池中加入6张【水灵•悠然】；第10轮后若自身符合境界且没有【水灵•悠然】，则该轮抽牌时优先抽取1张 | Add 6 【水灵•悠然】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 194 | 幻•暗鸦灵剑 (Mirage: Raven Spirit Sword) | 被动 | 牌池中加入6张【幻•暗鸦灵剑】；第10轮后若自身符合境界且没有【幻•暗鸦灵剑】，则该轮抽牌时优先抽取1张 | Add 6 【幻•暗鸦灵剑】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 195 | 幻•轻剑 (Mirage: Light Sword) | 被动 | 牌池中加入8张【幻•轻剑】；第9轮后若自身符合境界且没有【幻•轻剑】，则该轮抽牌时优先抽取1张 | Add 8 【幻•轻剑】 to pool. After round 9, auto-draw 1 if at correct phase and missing it. |
| 196 | 幻•引气剑 (Mirage: Spiritage Sword) | 被动 | 牌池中加入6张【幻•引气剑】；第10轮后若自身符合境界且没有【幻•引气剑】，则该轮抽牌时优先抽取1张 | Add 6 【幻•引气剑】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 197 | 幻•云剑探云 (Mirage: Cloud Sword - Touch Sky) | 被动 | 牌池中加入6张【幻•云剑探云】；第13轮后若自身符合境界且没有【幻•云剑探云】，则该轮抽牌时优先抽取1张 | Add 6 【幻•云剑探云】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 198 | 幻•斩草除根 (Mirage: Cutting Weeds) | 被动 | 牌池中加入6张【幻•斩草除根】；第10轮后若自身符合境界且没有【幻•斩草除根】，则该轮抽牌时优先抽取1张 | Add 6 【幻•斩草除根】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 199 | 幻•流水无情 (Mirage: Ruthless Water) | 被动 | 牌池中加入6张【幻•流水无情】；第10轮后若自身符合境界且没有【幻•流水无情】，则该轮抽牌时优先抽取1张 | Add 6 【幻•流水无情】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 200 | 幻•斗转星移 (Mirage: Shifting Stars) | 被动 | 牌池中加入6张【幻•斗转星移】；第13轮后若自身符合境界且没有【幻•斗转星移】，则该轮抽牌时优先抽取1张 | Add 6 【幻•斗转星移】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 201 | 幻•火灵聚炎 (Mirage: Fire Spirit - Flame Eater) | 被动 | 牌池中加入8张【幻•火灵聚炎】；第9轮后若自身符合境界且没有【幻•火灵聚炎】，则该轮抽牌时优先抽取1张 | Add 8 【幻•火灵聚炎】 to pool. After round 9, auto-draw 1 if at correct phase and missing it. |
| 202 | 幻•水灵波澜 (Mirage: Water Spirit - Billows) | 被动 | 牌池中加入6张【幻•水灵波澜】；第13轮后若自身符合境界且没有【幻•水灵波澜】，则该轮抽牌时优先抽取1张 | Add 6 【幻•水灵波澜】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 203 | 幻•木灵复苏 (Mirage: Wood Spirit - Recovery) | 被动 | 牌池中加入8张【幻•木灵复苏】；第9轮后若自身符合境界且没有【幻•木灵复苏】，则该轮抽牌时优先抽取1张 | Add 8 【幻•木灵复苏】 to pool. After round 9, auto-draw 1 if at correct phase and missing it. |
| 204 | 幻•金灵针 (Mirage: Metal Spirit - Needle) | 被动 | 牌池中加入6张【幻•金灵针】；第10轮后若自身符合境界且没有【幻•金灵针】，则该轮抽牌时优先抽取1张 | Add 6 【幻•金灵针】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 205 | 幻•血气方刚 (Mirage: Youthful Vigor) | 被动 | 牌池中加入8张【幻•血气方刚】；第9轮后若自身符合境界且没有【幻•血气方刚】，则该轮抽牌时优先抽取1张 | Add 8 【幻•血气方刚】 to pool. After round 9, auto-draw 1 if at correct phase and missing it. |
| 206 | 幻•锻骨 (Mirage: Exercise Bones) | 被动 | 牌池中加入6张【幻•锻骨】；第10轮后若自身符合境界且没有【幻•锻骨】，则该轮抽牌时优先抽取1张 | Add 6 【幻•锻骨】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 207 | 幻•气沉丹田 (Mirage: Sinking Qi) | 被动 | 牌池中加入6张【幻•气沉丹田】；第10轮后若自身符合境界且没有【幻•气沉丹田】，则该轮抽牌时优先抽取1张 | Add 6 【幻•气沉丹田】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 208 | 幻•云剑无锋 (Mirage: Cloud Sword - Conceal) | 被动 | 牌池中加入6张【幻•云剑无锋】；第13轮后若自身符合境界且没有【幻•云剑无锋】，则该轮抽牌时优先抽取1张 | Add 6 【幻•云剑无锋】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 209 | 幻•飞星刺 (Mirage: Astral Fleche) | 被动 | 牌池中加入6张【幻•飞星刺】；第13轮后若自身符合境界且没有【幻•飞星刺】，则该轮抽牌时优先抽取1张 | Add 6 【幻•飞星刺】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 210 | 幻•五行流转 (Mirage: Five Elements Circulation) | 被动 | 牌池中加入8张【幻•五行流转】；第12轮后若自身符合境界且没有【幻•五行流转】，则该轮抽牌时优先抽取1张 | Add 8 【幻•五行流转】 to pool. After round 12, auto-draw 1 if at correct phase and missing it. |
| 211 | 幻•双鬼拍门 (Mirage: Double Trouble) | 被动 | 牌池中加入6张【幻•双鬼拍门】；第13轮后若自身符合境界且没有【幻•双鬼拍门】，则该轮抽牌时优先抽取1张 | Add 6 【幻•双鬼拍门】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 212 | 幻•罗刹扑 (Mirage: Rakshasa Pouncing) | 被动 | 牌池中加入8张【幻•罗刹扑】；第12轮后若自身符合境界且没有【幻•罗刹扑】，则该轮抽牌时优先抽取1张 | Add 8 【幻•罗刹扑】 to pool. After round 12, auto-draw 1 if at correct phase and missing it. |
| 213 | 幻•藕断丝连 (Mirage: Incessant) | 被动 | 牌池中加入8张【幻•藕断丝连】；第12轮后若自身符合境界且没有【幻•藕断丝连】，则该轮抽牌时优先抽取1张 | Add 8 【幻•藕断丝连】 to pool. After round 12, auto-draw 1 if at correct phase and missing it. |
| 214 | 幻•土灵群山 (Mirage: Earth Spirit - Mountains) | 被动 | 牌池中加入8张【幻•土灵群山】；第12轮后若自身符合境界且没有【幻•土灵群山】，则该轮抽牌时优先抽取1张 | Add 8 【幻•土灵群山】 to pool. After round 12, auto-draw 1 if at correct phase and missing it. |
| 215 | 幻•坤卦 (Mirage: Earth Hexagram) | 被动 | 牌池中加入8张【幻•坤卦】；第9轮后若自身符合境界且没有【幻•坤卦】，则该轮抽牌时优先抽取1张 | Add 8 【幻•坤卦】 to pool. After round 9, auto-draw 1 if at correct phase and missing it. |
| 216 | 幻•崩拳戳 (Mirage: Crash Fist - Poke) | 被动 | 牌池中加入6张【幻•崩拳戳】；第13轮后若自身符合境界且没有【幻•崩拳戳】，则该轮抽牌时优先抽取1张 | Add 6 【幻•崩拳戳】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 217 | 幻•飞牙剑 (Mirage: Flying Fang Sword) | 被动 | 牌池中加入6张【幻•飞牙剑】；第10轮后若自身符合境界且没有【幻•飞牙剑】，则该轮抽牌时优先抽取1张 | Add 6 【幻•飞牙剑】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 218 | 幻•星罗棋布 (Mirage: Dotted Around) | 被动 | 牌池中加入6张【幻•星罗棋布】；第10轮后若自身符合境界且没有【幻•星罗棋布】，则该轮抽牌时优先抽取1张 | Add 6 【幻•星罗棋布】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 219 | 幻•浑天印 (Mirage: Cosmos Seal) | 被动 | 牌池中加入8张【幻•浑天印】；第12轮后若自身符合境界且没有【幻•浑天印】，则该轮抽牌时优先抽取1张 | Add 8 【幻•浑天印】 to pool. After round 12, auto-draw 1 if at correct phase and missing it. |
| 220 | 幻•岿然不动 (Mirage: Standing Firm) | 被动 | 牌池中加入8张【幻•岿然不动】；第9轮后若自身符合境界且没有【幻•岿然不动】，则该轮抽牌时优先抽取1张 | Add 8 【幻•岿然不动】 to pool. After round 9, auto-draw 1 if at correct phase and missing it. |
| 221 | 幻•落花有意 (Mirage: Flower Sentient) | 被动 | 牌池中加入4张【幻•落花有意】；第13轮后若自身符合境界且没有【幻•落花有意】，则该轮抽牌时优先抽取1张 | Add 4 【幻•落花有意】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 222 | 幻•云舞诀 (Mirage: Cloud Dance Rhythm) | 被动 | 牌池中加入6张【幻•云舞诀】；第13轮后若自身符合境界且没有【幻•云舞诀】，则该轮抽牌时优先抽取1张 | Add 6 【幻•云舞诀】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 223 | 幻•浩然正气 (Mirage: Magnanimous Righteousness) | 被动 | 牌池中加入6张【幻•浩然正气】；第13轮后若自身符合境界且没有【幻•浩然正气】，则该轮抽牌时优先抽取1张 | Add 6 【幻•浩然正气】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 224 | 幻•狂剑盘龙 (Mirage: Unrestrained Sword - Dragon Coiled) | 被动 | 牌池中加入8张【幻•狂剑盘龙】；第12轮后若自身符合境界且没有【幻•狂剑盘龙】，则该轮抽牌时优先抽取1张 | Add 8 【幻•狂剑盘龙】 to pool. After round 12, auto-draw 1 if at correct phase and missing it. |
| 225 | 幻•金灵印 (Mirage: Metal Spirit Seal) | 被动 | 牌池中加入6张【幻•金灵印】；第13轮后若自身符合境界且没有【幻•金灵印】，则该轮抽牌时优先抽取1张 | Add 6 【幻•金灵印】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 226 | 幻•土灵阵 (Mirage: Earth Spirit Formation) | 被动 | 牌池中加入8张【幻•土灵阵】；第9轮后若自身符合境界且没有【幻•土灵阵】，则该轮抽牌时优先抽取1张 | Add 8 【幻•土灵阵】 to pool. After round 9, auto-draw 1 if at correct phase and missing it. |
| 227 | 幻•崩拳缠 (Mirage: Crash Fist - Entangle) | 被动 | 牌池中加入6张【幻•崩拳缠】；第13轮后若自身符合境界且没有【幻•崩拳缠】，则该轮抽牌时优先抽取1张 | Add 6 【幻•崩拳缠】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 228 | 幻•两仪阵 (Mirage: Yin Yang Formation) | 被动 | 牌池中加入8张【幻•两仪阵】；第12轮后若自身符合境界且没有【幻•两仪阵】，则该轮抽牌时优先抽取1张 | Add 8 【幻•两仪阵】 to pool. After round 12, auto-draw 1 if at correct phase and missing it. |
| 229 | 幻•灵犀剑阵 (Mirage: Consonance Sword Formation) | 被动 | 牌池中加入6张【幻•灵犀剑阵】；第13轮后若自身符合境界且没有【幻•灵犀剑阵】，则该轮抽牌时优先抽取1张 | Add 6 【幻•灵犀剑阵】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 230 | 幻•火灵印 (Mirage: Fire Spirit Seal) | 被动 | 牌池中加入8张【幻•火灵印】；第9轮后若自身符合境界且没有【幻•火灵印】，则该轮抽牌时优先抽取1张 | Add 8 【幻•火灵印】 to pool. After round 9, auto-draw 1 if at correct phase and missing it. |
| 231 | 幻•死缠烂打 (Mirage: Endless Entanglement) | 被动 | 牌池中加入8张【幻•死缠烂打】；第9轮后若自身符合境界且没有【幻•死缠烂打】，则该轮抽牌时优先抽取1张 | Add 8 【幻•死缠烂打】 to pool. After round 9, auto-draw 1 if at correct phase and missing it. |
| 232 | 幻•勤拙剑 (Mirage: Diligent Sword) | 被动 | 牌池中加入8张【幻•勤拙剑】；第9轮后若自身符合境界且没有【幻•勤拙剑】，则该轮抽牌时优先抽取1张 | Add 8 【幻•勤拙剑】 to pool. After round 9, auto-draw 1 if at correct phase and missing it. |
| 233 | 幻•生机绽放 (Mirage: Vitality Blossom) | 被动 | 牌池中加入6张【幻•生机绽放】；第10轮后若自身符合境界且没有【幻•生机绽放】，则该轮抽牌时优先抽取1张 | Add 6 【幻•生机绽放】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 234 | 云剑·晚霞 (Cloud Sword - Sunset Glow) | 被动 | 牌池中加入4张【云剑·晚霞】；第10轮后若自身符合境界且没有【云剑·晚霞】，则该轮抽牌时优先抽取1张 | Add 4 【云剑·晚霞】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 235 | 青龙剑阵 (Azure Dragon Sword Formation) | 被动 | 牌池中加入6张【青龙剑阵】；第10轮后若自身符合境界且没有【青龙剑阵】，则该轮抽牌时优先抽取1张 | Add 6 【青龙剑阵】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 236 | 百兽灵剑阵 (Beast Spirit Sword Formation) | 被动 | 牌池中加入6张【百兽灵剑阵】；第13轮后若自身符合境界且没有【百兽灵剑阵】，则该轮抽牌时优先抽取1张 | Add 6 【百兽灵剑阵】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 237 | 狂龙吞云 (Dragon Devours Clouds) | 被动 | 牌池中加入8张【狂龙吞云】；第12轮后若自身符合境界且没有【狂龙吞云】，则该轮抽牌时优先抽取1张 | Add 8 【狂龙吞云】 to pool. After round 12, auto-draw 1 if at correct phase and missing it. |
| 238 | 灵卦术 (Spiritual Hexagram Divination) | 被动 | 牌池中加入6张【灵卦术】；第10轮后若自身符合境界且没有【灵卦术】，则该轮抽牌时优先抽取1张 | Add 6 【灵卦术】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 239 | 摘花飞叶 (Throw Petals) | 被动 | 牌池中加入6张【摘花飞叶】；第10轮后若自身符合境界且没有【摘花飞叶】，则该轮抽牌时优先抽取1张 | Add 6 【摘花飞叶】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 240 | 星弈·双飞燕 (Astral Move - Twin Swallows) | 被动 | 牌池中加入6张【星弈·双飞燕】；第13轮后若自身符合境界且没有【星弈·双飞燕】，则该轮抽牌时优先抽取1张 | Add 6 【星弈·双飞燕】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 241 | 滴水穿石 (Water Drop Erosion) | 被动 | 牌池中加入6张【滴水穿石】；第13轮后若自身符合境界且没有【滴水穿石】，则该轮抽牌时优先抽取1张 | Add 6 【滴水穿石】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 242 | 野渡之印 (Wild Crossing Seal) | 被动 | 牌池中加入8张【野渡之印】；第9轮后若自身符合境界且没有【野渡之印】，则该轮抽牌时优先抽取1张 | Add 8 【野渡之印】 to pool. After round 9, auto-draw 1 if at correct phase and missing it. |
| 243 | 熔岩之印 (Lava Seal) | 被动 | 牌池中加入6张【熔岩之印】；第10轮后若自身符合境界且没有【熔岩之印】，则该轮抽牌时优先抽取1张 | Add 6 【熔岩之印】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 244 | 滚石之印 (Boulder Seal) | 被动 | 牌池中加入6张【滚石之印】；第13轮后若自身符合境界且没有【滚石之印】，则该轮抽牌时优先抽取1张 | Add 6 【滚石之印】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 245 | 斩浪之印 (Wave Cutter Seal) | 被动 | 牌池中加入8张【斩浪之印】；第12轮后若自身符合境界且没有【斩浪之印】，则该轮抽牌时优先抽取1张 | Add 8 【斩浪之印】 to pool. After round 12, auto-draw 1 if at correct phase and missing it. |
| 246 | 玄灵附身 (Dark Spirit Possession) | 被动 | 牌池中加入6张【玄灵附身】；第10轮后若自身符合境界且没有【玄灵附身】，则该轮抽牌时优先抽取1张 | Add 6 【玄灵附身】 to pool. After round 10, auto-draw 1 if at correct phase and missing it. |
| 247 | 崩拳•伏虎 (Crash Fist - Tiger Subdue) | 被动 | 牌池中加入8张【崩拳•伏虎】；第9轮后若自身符合境界且没有【崩拳•伏虎】，则该轮抽牌时优先抽取1张 | Add 8 【崩拳•伏虎】 to pool. After round 9, auto-draw 1 if at correct phase and missing it. |
| 248 | 瞬影击 (Instant Shadow Strike) | 被动 | 牌池中加入8张【瞬影击】；第12轮后若自身符合境界且没有【瞬影击】，则该轮抽牌时优先抽取1张 | Add 8 【瞬影击】 to pool. After round 12, auto-draw 1 if at correct phase and missing it. |
| 249 | 逍遥无影拳 (Carefree Shadowless Fist) | 被动 | 牌池中加入6张【逍遥无影拳】；第13轮后若自身符合境界且没有【逍遥无影拳】，则该轮抽牌时优先抽取1张 | Add 6 【逍遥无影拳】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 250 | 悟道丹 (Enlightenment Elixir) | 被动 | 牌池中额外加入4张【悟道丹】；第13轮后若自身符合境界且没有【悟道丹】，则该轮抽牌时优先抽取1张 | Add 4 【悟道丹】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 251 | 冰灵护体丹 (Ice Spirit Guard Elixir) | 被动 | 牌池中额外加入4张【冰灵护体丹】；第13轮后若自身符合境界且没有【冰灵护体丹】，则该轮抽牌时优先抽取1张 | Add 4 【冰灵护体丹】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 252 | 万邪入体咒 (Myriad Evils Body Hex) | 被动 | 牌池中额外加入4张【万邪入体咒】；第13轮后若自身符合境界且没有【万邪入体咒】，则该轮抽牌时优先抽取1张 | Add 4 【万邪入体咒】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 253 | 千里神行符 (Thousand-Mile Swift Talisman) | 被动 | 牌池中额外加入4张【千里神行符】；第13轮后若自身符合境界且没有【千里神行符】，则该轮抽牌时优先抽取1张 | Add 4 【千里神行符】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 254 | 转弦合调 (String Shifting Harmony) | 被动 | 牌池中额外加入4张【转弦合调】；第13轮后若自身符合境界且没有【转弦合调】，则该轮抽牌时优先抽取1张 | Add 4 【转弦合调】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 255 | 天音困仙曲 (Celestial Immortal-Trapping Melody) | 被动 | 牌池中额外加入4张【天音困仙曲】；第13轮后若自身符合境界且没有【天音困仙曲】，则该轮抽牌时优先抽取1张 | Add 4 【天音困仙曲】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 256 | 画龙点睛 (Painting the Dragon's Eyes) | 被动 | 牌池中额外加入4张【画龙点睛】；第13轮后若自身符合境界且没有【画龙点睛】，则该轮抽牌时优先抽取1张 | Add 4 【画龙点睛】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 257 | 运笔如飞 (Swift Brushwork) | 被动 | 牌池中额外加入4张【运笔如飞】；第13轮后若自身符合境界且没有【运笔如飞】，则该轮抽牌时优先抽取1张 | Add 4 【运笔如飞】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 258 | 须弥阵纹 (Sumeru Formation Rune) | 被动 | 牌池中额外加入4张【须弥阵纹】；第13轮后若自身符合境界且没有【须弥阵纹】，则该轮抽牌时优先抽取1张 | Add 4 【须弥阵纹】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 261 | 空间灵田 (Spatial Spirit Field) | 被动 | 牌池中额外加入4张【空间灵田】；第13轮后若自身符合境界且没有【空间灵田】，则该轮抽牌时优先抽取1张 | Add 4 【空间灵田】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 262 | 厄劫缠身 (Calamity-Ridden) | 被动 | 牌池中额外加入4张【厄劫缠身】；第13轮后若自身符合境界且没有【厄劫缠身】，则该轮抽牌时优先抽取1张 | Add 4 【厄劫缠身】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |
| 263 | 命运轮回 (Fate Reincarnation) | 被动 | 牌池中额外加入4张【命运轮回】；第13轮后若自身符合境界且没有【命运轮回】，则该轮抽牌时优先抽取1张 | Add 4 【命运轮回】 to pool. After round 13, auto-draw 1 if at correct phase and missing it. |

### Category 7

| id | Name | Kind | Effect (CN) | Effect (EN) |
|---|---|---|---|---|
| 275 | 狂剑道韵 (Omen of Unrestrained Sword) | 特殊 | 道韵预感必然包含【狂剑•二式】和【狂剑•零式】 | Daoist Rhyme Omen always offers 【狂剑•二式】 and 【狂剑•零式】. |
| 276 | 云剑道韵 (Omen of Cloud Sword) | 特殊 | 道韵预感必然包含【云剑•月影】和【云剑•游龙】 | Daoist Rhyme Omen always offers 【云剑•月影】 and 【云剑•游龙】. |
| 277 | 灵剑道韵 (Omen of Spirit Sword) | 特殊 | 道韵预感必然包含【巨鲲灵剑】和【万法归灵剑】 | Daoist Rhyme Omen always offers 【巨鲲灵剑】 and 【万法归灵剑】. |
| 278 | 剑意道韵 (Omen of Sword Intent) | 特殊 | 道韵预感必然包含【流云乱剑】和【剑意激荡】 | Daoist Rhyme Omen always offers 【流云乱剑】 and 【剑意激荡】. |
| 279 | 剑阵道韵 (Omen of Sword Formation) | 特殊 | 道韵预感必然包含【连环剑阵】和【御空剑阵】 | Daoist Rhyme Omen always offers 【连环剑阵】 and 【御空剑阵】. |
| 280 | 木灵道韵 (Omen of Wood Spirit) | 特殊 | 道韵预感必然包含【木灵•暗香】和【木灵•柳纷飞】 | Daoist Rhyme Omen always offers 【木灵•暗香】 and 【木灵•柳纷飞】. |
| 281 | 火灵道韵 (Omen of Fire Spirit) | 特殊 | 道韵预感必然包含【火灵•瞬燃】和【火灵•烈燎原】 | Daoist Rhyme Omen always offers 【火灵•瞬燃】 and 【火灵•烈燎原】. |
| 282 | 土灵道韵 (Omen of Earth Spirit) | 特殊 | 道韵预感必然包含【土灵•流沙】和【土灵•合八荒】 | Daoist Rhyme Omen always offers 【土灵•流沙】 and 【土灵•合八荒】. |
| 283 | 金灵道韵 (Omen of Metal Spirit) | 特殊 | 道韵预感必然包含【金灵•飞梭】和【金灵•巨鼎落】 | Daoist Rhyme Omen always offers 【金灵•飞梭】 and 【金灵•巨鼎落】. |
| 284 | 水灵道韵 (Omen of Water Spirit) | 特殊 | 道韵预感必然包含【水灵•腾浪】和【水灵•纳百川】 | Daoist Rhyme Omen always offers 【水灵•腾浪】 and 【水灵•纳百川】. |
| 285 | 混元道韵 (Omen of Primordial) | 特殊 | 道韵预感必然包含【混元碎击】和【混元无极阵】 | Daoist Rhyme Omen always offers 【混元碎击】 and 【混元无极阵】. |
| 286 | 星弈道韵 (Omen of Astral Move) | 特殊 | 道韵预感必然包含【星弈•虎】和【天元心法】 | Daoist Rhyme Omen always offers 【星弈•虎】 and 【天元心法】. |
| 287 | 卦象道韵 (Omen of Hexagram) | 特殊 | 道韵预感必然包含【六爻绝阵】和【乾卦】 | Daoist Rhyme Omen always offers 【六爻绝阵】 and 【乾卦】. |
| 288 | 生机道韵 (Omen of Vitality) | 特殊 | 道韵预感必然包含【静气心法】和【气吞山河】 | Daoist Rhyme Omen always offers 【静气心法】 and 【气吞山河】. |
| 289 | 后招道韵 (Omen of Post Action) | 特殊 | 道韵预感必然包含【金蝉脱壳】和【黄雀在后】 | Daoist Rhyme Omen always offers 【金蝉脱壳】 and 【黄雀在后】. |
| 290 | 内伤道韵 (Omen of Internal Injury) | 特殊 | 道韵预感必然包含【杯弓蛇影】和【灵蛇绕柱】 | Daoist Rhyme Omen always offers 【杯弓蛇影】 and 【灵蛇绕柱】. |
| 291 | 锻体道韵 (Omen of Body Forging) | 特殊 | 道韵预感必然包含【锻髓】和【百杀破境掌】 | Daoist Rhyme Omen always offers 【锻髓】 and 【百杀破境掌】. |
| 292 | 崩拳道韵 (Omen of Crash Fist) | 特殊 | 道韵预感必然包含【崩灭心法】和【崩拳•闪击】 | Daoist Rhyme Omen always offers 【崩灭心法】 and 【崩拳•闪击】. |
| 293 | 气势道韵 (Omen of Force) | 特殊 | 道韵预感必然包含【冲霄破浪】和【威震四方】 | Daoist Rhyme Omen always offers 【冲霄破浪】 and 【威震四方】. |
| 294 | 冥玄道韵 (Omen of Styx Mystery) | 特殊 | 道韵预感必然包含【玄手夺魂】和【修罗吼】 | Daoist Rhyme Omen always offers 【玄手夺魂】 and 【修罗吼】. |
| 295 | 身法道韵 (Omen of Agility) | 特殊 | 道韵预感必然包含【冥影身法】和【鹤步】 | Daoist Rhyme Omen always offers 【冥影身法】 and 【鹤步】. |

### Category 8

| id | Name | Kind | Effect (CN) | Effect (EN) |
|---|---|---|---|---|
| 311 | 极·云剑柔心 (Ultimate: Cloud Sword - Softheart) | build | 选择时减1修为，获得1张【云剑•柔心】 / 主动使用（第13轮解锁）：将手牌中的【云剑•柔心】变为【极•云剑柔心】，或反向变回 | When chosen: -1 Cultivation, gain 1 【云剑•柔心】. Use (unlocks round 13): Transform 【云剑•柔心】 in hand into 【极•云剑柔心】, or reverse. |
| 312 | 极·暗鸦灵剑  (Ultimate: Raven Spirit Sword) | build | 选择时减1修为，获得1张【暗鸦灵剑】 / 主动使用（第13轮解锁）：将手牌中的【暗鸦灵剑】变为【极•暗鸦灵剑】，或反向变回 | When chosen: -1 Cultivation, gain 1 【暗鸦灵剑】. Use (unlocks round 13): Transform 【暗鸦灵剑】 in hand into 【极•暗鸦灵剑】, or reverse. |
| 313 | 极·静气心法  (Ultimate: Stillness Citta-Dharma) | build | 选择时减1修为，获得1张【静气心法】 / 主动使用（第13轮解锁）：将手牌中的【静气心法】变为【极•静气心法】，或反向变回 | When chosen: -1 Cultivation, gain 1 【静气心法】. Use (unlocks round 13): Transform 【静气心法】 in hand into 【极•静气心法】, or reverse. |
| 314 | 极·两仪阵  (Ultimate: Yin Yang Formation) | build | 选择时减1修为，获得1张【两仪阵】 / 主动使用（第13轮解锁）：将手牌中的【两仪阵】变为【极•两仪阵】，或反向变回 | When chosen: -1 Cultivation, gain 1 【两仪阵】. Use (unlocks round 13): Transform 【两仪阵】 in hand into 【极•两仪阵】, or reverse. |
| 315 | 极·水灵阵  (Ultimate: Water Spirit Formation) | build | 选择时减1修为，获得1张【水灵阵】 / 主动使用（第13轮解锁）：将手牌中的【水灵阵】变为【极•水灵阵】，或反向变回 | When chosen: -1 Cultivation, gain 1 【水灵阵】. Use (unlocks round 13): Transform 【水灵阵】 in hand into 【极•水灵阵】, or reverse. |
| 316 | 极·木灵巡林  (Ultimate: Wood Spirit - Forest Guard) | build | 选择时减1修为，获得1张【木灵•巡林】 / 主动使用（第13轮解锁）：将手牌中的【木灵•巡林】变为【极•木灵巡林】，或反向变回 | When chosen: -1 Cultivation, gain 1 【木灵•巡林】. Use (unlocks round 13): Transform 【木灵•巡林】 in hand into 【极•木灵巡林】, or reverse. |
| 317 | 极·崩天步  (Ultimate: Crash Footwork) | build | 选择时减1修为，获得1张【崩天步】 / 主动使用（第13轮解锁）：将手牌中的【崩天步】变为【极•崩天步】，或反向变回 | When chosen: -1 Cultivation, gain 1 【崩天步】. Use (unlocks round 13): Transform 【崩天步】 in hand into 【极•崩天步】, or reverse. |
| 318 | 极·迎风掌  (Ultimate: Windward Palms) | build | 选择时减1修为，获得1张【迎风掌】 / 主动使用（第13轮解锁）：将手牌中的【迎风掌】变为【极•迎风掌】，或反向变回 | When chosen: -1 Cultivation, gain 1 【迎风掌】. Use (unlocks round 13): Transform 【迎风掌】 in hand into 【极•迎风掌】, or reverse. |