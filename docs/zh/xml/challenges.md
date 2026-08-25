---
tags:
  - File
---
# 文件 "challenges.xml"

用于存储所有挑战及其部分属性。

**Resource-Folder**{: .xmlInfo .green }：将此文件放入模组的resource文件夹会覆盖原始文件。

**Content-Folder**{: .xmlInfo .green }：将此文件放入模组的content文件夹会添加一个新的**自定义挑战**。


| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|id|int|挑战在游戏中的ID（Content Folder下不需要）|
|name|string|挑战名称|
|startingitems|string list|以逗号分隔（无空格）的物品ID，开局时获得这些物品。|
|startingitems2|string list|玩家2的开局物品。以逗号分隔（无空格）的物品ID，开局时获得这些物品。[ ](#){: .reporplus .tooltip .badge }|
|startingtrinkets|string list|以逗号分隔（无空格）的饰品ID，开局时获得（最多2个）|
|startingcard|string list|开局卡牌的[Card id](../enums/Card.md)<br>默认：-1（无卡牌）|
|startingpill|string list|开局药丸的[PillEffect id](../enums/PillEffect.md)<br>默认：-1（无药丸）|
|playertype|string|玩家类型ID。无法通过此方式定义自定义角色！请使用LUA代码。<br>默认：0（Isaac）|
|endstage|string|挑战的最后一关（使用[LevelStage](../enums/LevelStage.md)内部ID）|
|roomfilter|string list|挑战中不生成的[RoomTypes](../enums/RoomType.md)列表【并非所有房间ID都可用】|
|cursefilter|int|要移除的[curses](../enums/LevelCurse.md)的位掩码。<br>（Darkness = 1, Labyrinth = 2, Lost = 4, Unknown = 8, Cursed = 16, Maze = 32, Blind = 64, Giant = 128）|
|getcurse|int|要强制添加的[curses](../enums/LevelCurse.md)的位掩码（与cursefilter相同）|
|achievements|string list|游玩该挑战所需的成就ID列表|
|altpath|bool|光明/黑暗路径（isaac/satan）的替代楼层|
|canshoot|bool|决定玩家是否能射击<br>默认：true（可射击）|
|redhp|int|为所选角色基础添加红心。2=1颗心。可为负数|
|maxhp|int|为所选角色基础添加红心容器。2=1个心容器。可为负数|
|soulhp|int|为所选角色基础添加魂心容器。2=1个心容器|
|blackhp|int|为所选角色基础添加黑心容器。2=1个心容器|
|coins|int|添加开局硬币数|
|maxdamage|bool|最大伤害激活（最小100）或关闭|
|adddamage|float|+伤害加成|
|minfirerate|float|最小射速或更高|
|minshotspeed|bool|最小射速激活或关闭|
|bigrange|bool|启用高初始射程|
|difficulty|int|[游戏难度](../enums/Difficulty.md) [0: 普通(默认), 1: 困难, 2: Greed, 3: Greedier)<br>Greed和Greedier模式可用，但击败Ultra Greed时会生成大箱子而不是奖杯|
|megasatan|bool|最终Boss为megasatan。为玩家添加钥匙。|
|secretpath|bool|强制Repentance分支路径[ ](#){: .reporplus .tooltip .badge }|

## "challenges.xml" 文件示例：

以下代码会在自定义挑战标签页创建一个名为“My new challenge”的新挑战，终点为Mom's heart/it lives。玩家开局获得Breakfast、Dead Cat和Little Steven，但无法射击。宝箱房和黑暗诅咒被禁用。

```xml
<challenges version="1">
	<challenge playertype="0" name="My new challenge" endstage="8" startingitems="25,81,100" roomfilter="1" cursefilter="1" canshoot="false" />
</challenges>
```
