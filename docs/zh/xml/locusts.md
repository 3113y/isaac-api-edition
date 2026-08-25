---
tags:
  - File
---
# 文件 "locusts.xml"
此文件用于定义由无底坑(堕化亚玻伦初始道具)生成的无底坑蝗虫的属性。

**Resource-Folder**{: .xmlInfo .red}：在模组的resource文件夹中使用此文件会替换原始文件。

**Content-Folder**{: .xmlInfo .green}：在模组的content文件夹中使用此文件会添加新的locust。


### "color" 节点
用于定义无底坑蝗虫可拥有的颜色。

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
| name | str | 颜色名称，在"locust"节点中引用|
| r | int | 红色分量 |
| g | int | 绿色分量 |
| b | int | 蓝色分量 |
| or | int | 红色偏移量 |
| og | int | 蓝色偏移量 |
| ob | int | 绿色偏移量 |

### "scale" 节点
用于根据物品品质定义无底坑蝗虫的默认缩放比例。

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
| scale | float | 对应品质的缩放比例 |
| quality | int | 物品品质 |


### "locust" 节点
用于定义由指定ID物品生成的无底坑蝗虫的特殊属性。

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
| id | int | 无底坑吞噬的Collectible的ID |
| backColor | string | |
| backGfx | string | 无底坑蝗虫应使用的特殊背面spritesheet |
| collisionInterval | int | 影响接触伤害的间隔 |
| color | string | 无底坑蝗虫使用的颜色名称 |
| count | int | 生成的无底坑蝗虫数量 |
| damageMultiplier | float | 固定伤害倍率 |
| damageMultiplier2 | float | 有概率造成更高伤害 |
| gfx | string | 无底坑蝗虫应使用的特殊spritesheet |
| locustFlags | string | 要应用的无底坑蝗虫效果ID。如果未定义`procChance`则必定应用。可用空格分隔多个ID，如"1 15" |
| locustFlags2 | string | 要应用的无底坑蝗虫效果ID。根据`procChance`或`procChance2`应用。可用空格分隔多个ID，如"1 15"  |
| locustFlags3 | string | 要应用的无底坑蝗虫效果ID。根据`procChance3`应用。可用空格分隔多个ID，如"1 15"  |
| mutexFlags1 | int | *Bug: 会导致游戏崩溃* |
| mutexFlags2 | int | 互斥处理。如果设为x，则flag 2在flag x被触发时无法被触发 |
| mutexFlags3 | int | *目前无效* |
| speed | float | 无底坑蝗虫的速度倍率（默认1） |
| shootBackGfx | string ||
| shootGfx | string | 无底坑蝗虫蓄力时使用的.anm2 |
| shootOverlayGfx | string ||
| overlayColor | string | 叠加特效使用的颜色名称 |
| overlayGfx | string |locust应使用的特殊叠加spritesheet |
| tearFlags | int | 要应用的[TearFlag](../enums/TearFlags.md)的ID。如果未定义`procChance`则必定应用 |
| tearFlags2 | int |要应用的[TearFlag](../enums/TearFlags.md)的ID。根据`procChance`或`procChance2`应用 |
| tearFlags3 | int |要应用的[TearFlag](../enums/TearFlags.md)的ID。根据`procChance3`应用 |
| procChance | float | 应用`tearFlags`和`locustFlags`的概率（默认1） |
| procChance2 | float | 应用`tearFlags2`和`locustFlags2`的概率 |
| procChance3 | float | 应用`tearFlags3`和`locustFlags3`的概率 |
| scale | float | locust的体型倍率 |


### locustFlags 效果一览
| id | 效果 |
|:--|:--|
| 0 | 攻击敌人时生成爆炸 |
| 1 | 随机效果 |
| 2 | 多个locust表现为一个（？）- 用于生成多个locust的物品 |
| 3 | 命中时重骰敌人 |
| 4 | 攻击敌人时对全房间敌人造成伤害 |
| 5 | 攻击敌人时抹除该敌人类型 |
| 6 | locust攻击时周围有刀环绕 |
| 7 | 尖叫，对周围敌人造成伤害 |
| 8 | 生成Maw of the void黑洞环 |
| 9 | 蓄力时获得弹幕驱散光环 |
| 10 | 攻击敌人时生成毒屁 |
| 11 | 攻击敌人时生成普通屁 |
| 12 | 攻击敌人时生成反重力硫磺火 |
| 13 | 攻击敌人时生成绿色水迹 |
| 14 | 攻击敌人时生成黄色水迹 |
| 15 | 攻击敌人时生成红色水迹 |
| 16 | 攻击敌人时生成蓝色水迹 |
| 17 | 攻击敌人时生成五芒星 |
| 18 | 吸收拾取物提升伤害 |
