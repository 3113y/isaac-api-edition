---
tags:
  - File
---
# 文件 "entities2.xml"

本页面需要补充内容。你可以使用编辑按钮进行贡献！

旧教程: [https://www.reddit.com/r/themoddingofisaac/comments/36o00t/entitys_explained_how_to_add_entity_variants/](https://www.reddit.com/r/themoddingofisaac/comments/36o00t/entitys_explained_how_to_add_entity_variants/)

**Resource-Folder**{: .xmlInfo }：在模组的resource文件夹中使用此文件尚未经过测试。

**Content-Folder**{: .xmlInfo }：在模组的content文件夹中使用此文件尚未经过测试。


| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
| name | str ||
| id | int | 实体类型。最大值：4095 |
| variant | int | 实体的变体。最大值为4095。如果留空，游戏会自动选择下一个可用编号。 |
| subtype | int | 实体的SubType。最大值为255。（原因是.stb格式的哈希表生成器需要特定位深。） |
| anm2path | string | anm2文件的路径，相对于给定的anm2root。例如：`001.000_Player.anm2` |
| baseHP | int ||
| boss | int |是否为Boss。可选值：['0', '1'] |
| bossID | int ||
| champion | int |是否允许该实体有精英变体。可选值：['0', '1'] |
| collisionDamage | float ||
| collisionMass | float ||
| collisionRadius | float | 碰撞圆的半径。用于实体<-->实体和实体<-->地形的碰撞。这会改变`Entity.Size`字段。 |
| collisionRadiusXMulti | float | 碰撞圆X方向的缩放。可用于实现椭圆形碰撞箱 |
| collisionRadiusYMulti | float | 碰撞圆Y方向的缩放。可用于实现椭圆形碰撞箱 |
| collisionInterval | int | 下次碰撞检测前的游戏帧数。默认=1 |
| numGridCollisionPoints | int | 碰撞圆边缘用于检测与地形碰撞的点数。 |
| friction | float | 实体的“滑溜度”。默认=1。值越低越滑，类似在冰上。值越高越不滑。为0时无法移动。 |
| shadowSize | float ||
| stageHP | int ||
| tags | string | 可选值：['nodelirium', 'spider', 'explosive_soul', 'cansacrifice', 'ghost', 'brimstone_soul', 'homing_soul', 'fly', 'noreroll']<br>详见下方标签说明章节。 |
| gridCollision | string | 可选值：['nopits', 'ground', 'none', 'walls', 'floor'] |
| portrait | int ||
| hasFloorAlts | bool | 若为true，则该实体会使用特定楼层的sprite（如存在）。详见下方章节。 |
| reroll | bool ||
| shutdoors | bool ||
| shieldStrength | int ||
| gibAmount | int ||
| gibFlags | string | 可用值：['poop'] |
| bestiaryAnim | string ||
| bestiaryOverlay | string ||

## 标签说明

| 标签名 | 说明 |
|:--|:--|
|cansacrifice| 标记可用于献祭祭坛的跟班|
|nodelirium| 该Boss不会被精神错乱选中变化|
|fly|被粪臭素友好化的敌人（不影响别西卜套装）|
|spider|被爆裂虫卵友好化的敌人|
|ghost|驱魔护符可在<50%血量时特殊击杀的敌人|
|noreroll| 免疫D10重骰和Ace卡牌|
|brimstone_soul| 该敌人生成的友好球灵火会发射细长鲜血激光柱|
|explosive_soul| 该敌人生成的友好球灵火会发射爆炸泪弹|
|homing_soul| 该敌人生成的友好球灵火会发射追踪泪弹|


## 楼层专属sprite
如果实体的 `hasFloorAlts` 属性为 `true`，游戏会尝试根据当前关卡为该实体加载带有额外后缀的spritesheet。关卡的后缀由 stages.xml 文件中的 `suffix` 属性定义。如果找不到对应sprite，则加载默认spritesheet.

**示例：**
原始Gaper sprite：monster_017_gaper.png

Downpour楼层sprite：monster_017_gaper_downpour.png

**各楼层后缀：**

| 楼层名称 | 后缀 |
|:--|:--|
|Flooded Caves|_downpour|
|Downpour|_downpour|
|Dross|_dross|
|Ashpit|_ashpit|
|Mausoleum|_mausoleum|
|Gehenna|_gehenna|

## `<gibs>` 标签
`<gibs>` 标签用于定义实体被击杀或销毁时生成的gibs。

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
| amount | int | 生成gibs的数量|
| blood | int | 可选值: [0,1]，0为关闭，1为开启|
| bone | int |可选值: [0,1]，0为关闭，1为开启|
| chain | int |可选值: [0,1]，0为关闭，1为开启|
| colorblood | int |可选值: [0,1]，0为关闭，1为开启|
| dust | int |可选值: [0,1]，0为关闭，1为开启|
| eye | int |可选值: [0,1]，0为关闭，1为开启|
| gut | int |可选值: [0,1]，0为关闭，1为开启|
| huge | int |可选值: [0,1]，0为关闭，1为开启|
| large | int |可选值: [0,1]，0为关闭，1为开启|
| poop | int |可选值: [0,1]，0为关闭，1为开启|
| rock | int |可选值: [0,1]，0为关闭，1为开启|
| rock_small | int |可选值: [0,1]，0为关闭，1为开启|
| small | int |可选值: [0,1]，0为关闭，1为开启|
| sound_baby | int |可选值: [0,1]，0为关闭，1为开启|
| sound_bone | int |可选值: [0,1]，0为关闭，1为开启|
| worm | int |可选值: [0,1]，0为关闭，1为开启|
