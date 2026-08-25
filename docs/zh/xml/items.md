---
tags:
  - File
---
# 文件 "items.xml"

旧教程: [https://www.reddit.com/r/themoddingofisaac/comments/3mub9c/ways_to_modify_items/](https://www.reddit.com/r/themoddingofisaac/comments/3mub9c/ways_to_modify_items/)

**Resource-Folder**{: .xmlInfo .red}：在模组的resource文件夹中使用此文件会替换原始文件。

**Content-Folder**{: .xmlInfo .green}：在模组的content文件夹中使用此文件会添加新物品。


| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
| id | int | 用于将costume和死亡肖像/收集页面sprite与物品关联。 |
| cache | string | 可选值: [firedelay, damage, speed, range, tearcolor, tearflag, color, size, shotspeed, all, luck, flying, weapon, familiars]。|
| name | string |  |
| description | string |  |
| gfx | string | 物品图片路径。必须为32位深度的.png文件。 |
| tags | string | 多个标签需用空格分隔，见下方可用值及说明。 |
| bombs | int |  |
| keys | int |  |
| coins | int |  |
| hearts | int | 与MaxHearts不同，必须与MaxHearts一起赋值才能获得填充的心容器。 |
| soulhearts | int |  |
| blackhearts | int |  |
| maxhearts | int | 增加的空心之容器数量。 |
| maxcharges | int | 当chargetype为`timed`时，此属性用于定义物品的冷却帧数。 |
| chargetype | string | 可选值: [normal, timed, special]|
| cooldown | int | 该物品关联的CollectibleEffect在被授予后自动移除前的帧数。CollectibleEffect会在主动物品使用时自动授予。 |
| passivecache | bool | 拾取时调用cache评估（用于主动物品，如Mom's Box）。 |
| special | bool |  |
| initcharge | int | 该主动物品首次拾取时应有的初始充能（如Everything Jar[ ](#){: .reporplus .tooltip .badge }）。 |
| devilprice | int | 可选值: ['1','2'] |
| shopprice | int |  |
| addcostumeonpickup | bool |  |
| persistent | bool | 决定物品关联的CollectibleEffect在房间切换或存档继续时是否保留。CollectibleEffect会在主动物品使用时自动授予。默认false。 |
| achievement | int | 该物品与原版成就解锁绑定。 |
| quality | int | 可选值: ['0', '1', '2', '3', '4']。 |
| craftquality | int | 可选值: ['-1', '0', '1', '2', '3', '4']。为-1时该物品不会出现在Bag of Crafting中。 |
| hidden | bool | 防止该物品出现在死亡证明或收集菜单中（如达摩克里斯之剑类型的跟班物品）。 |
| cleareffectsonremove | bool | 移除物品时清除其效果。注意：目前原版物品未使用此属性。 |

## 标签文档

| 标签名 | 说明 |
|:--|:--|
| dead | 死亡类物品（用于寄生虫的解锁） |
| syringe | 注射器类物品（用于小药袋解锁和 针套装） |
| mom | 妈妈类物品（用于妈妈的美瞳解锁和 妈妈套装） |
| tech | 科技类物品（用于科技零解锁） |
| battery | 电池类物品（用于跨接电缆解锁） |
| guppy | 猫类物品（猫套装） |
| fly | 苍蝇类物品（苍蝇套装） |
| bob | Bob类物品（鲍勃套装） |
| mushroom | 蘑菇类物品（蘑菇套装） |
| baby | 宝宝类物品（宝宝套装） |
| angel | 天使类物品（天使套装） |
| devil | 恶魔类物品（恶魔套装） |
| poop | 屎类物品（大便套装） |
| book | 书本类物品（书套装） |
| spider | 蜘蛛类物品（蜘蛛套装） |
| quest | 任务物品（不可重骰或随机获得） |
| monstermanual | 可由怪物手册生成 |
| nogreed | 不会出现在贪婪模式 |
| food | 食物类物品（用于大胃王） |
| tearsup | 提升射速的物品（用于食泪症解锁） |
| offensive | 堕化游魂白名单物品 |
| nokeeper | 店长/堕化店长黑名单物品 |
| nolostbr | 游魂的长子名分黑名单物品 |
| stars | 星星类物品（用于星象房解锁） |
| summonable | 可召唤物品（用于所罗门魔典） |
| nocantrip | 无法在大量过牌！挑战中获得 |
| wisp | 带有灵火的主动物品（自动设置） |
| uniquefamiliar | 独特跟班，无法复制 |
| nochallenge | 不应在挑战中获得的物品 |
| nodaily | 不应在每日挑战中获得的物品（因每日挑战无法获得mod物品，此标签一般无用） |
| lazarusshared | 堕化拉撒路双形态间共享的物品 |
| lazarussharedglobal | 仅通过全局检测（如EntityPlayer:HasCollectible）在堕化拉撒路双形态间共享的物品 |
| noeden | 无法被随机重骰获得的物品 |
