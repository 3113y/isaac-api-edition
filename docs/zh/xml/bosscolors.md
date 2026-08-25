---
tags:
  - File
---
# 文件 "bosscolors.xml"

此文件用于存储所有有效的Boss变体。变体Boss的效果是硬编码的，因此本文件只定义Boss的颜色、缩放比例和生命值倍率。

**Resource-Folder**{: .xmlInfo }：在模组的resource文件夹中使用此文件尚未经过测试。

**Content-Folder**{: .xmlInfo }：在模组的content文件夹中使用此文件尚未经过测试。

## "boss" 标签

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|id|int|Boss在游戏中的ID。|
|variant|int|Boss在游戏中的变体。|

## "color" 标签

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|idx|int|Boss的颜色。可能的值：1-红色，2-苍白，3-绿色，4-青色，5-绿色，6-橙色，7-蓝色，8-青色，9-橙色，10-？，11-深灰绿色，12-黄色，13-深青色，14-红色，15-深灰色，16-深灰色，17-浅灰色，18-黑色，19-红色，20-粉色，21-金色，22-粉色，23-棕色|
|scale|float|Boss的缩放比例会乘以该数值。|
|hp|float|Boss的生命值会乘以该数值。|
|anm2path|string|指定的anm2文件路径，将替代自动上色Boss的方式|
