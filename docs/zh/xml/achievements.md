---
tags:
  - File
---
# 文件 "achievements.xml"

此文件用于存储游戏内成就的一般信息。

**Resource-Folder**{: .xmlInfo .green }：将此文件放入你的模组 "resource" 文件夹中将会替换原始文件。

**Content-Folder**{: .xmlInfo .red }：将此文件放入你的模组 "content" 文件夹中不会产生任何效果！


| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|id|int|成就在游戏中的ID|
|text|string|成就描述|
|gfx|string|基于 "achievements" xml 根节点 "gfxroot" 属性的 .png 文件路径|
|steam_name|string|Steam 上的成就名称|
|steam_description|string|描述（未使用）|
|steam_icon|string|Steam 成就图标的精灵名称|