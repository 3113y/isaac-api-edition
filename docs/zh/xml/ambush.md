---
tags:
  - File
---
# 文件 "ambush.xml"

此文件用于存储挑战房间和Boss Rush的波次系统的生成模式。
[ ](#){: .reporplus .tooltip .badge } 挑战房间使用了更类似贪婪模式波次的新系统，因此本文件仅定义Boss Rush的波次。

**Resource-Folder**{: .xmlInfo .green }：将此文件放入你的模组 "resource" 文件夹中将会替换原始文件。

**Content-Folder**{: .xmlInfo .red }：将此文件放入你的模组 "content" 文件夹中不会产生任何效果！

## "enemy" 标签

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|type|int|要生成的实体类型|
|variant|int|实体的变体|
|count|int|该实体在波次开始时应生成的数量|
|chunks|int|多段实体NPC（如Larry Jr.）应生成的段数|

## "bossrush" 标签

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|numWaves|int|Boss Rush期间出现的总波次数|
|spawnsPerWave|int|每个Boss Rush波次应生成的Boss数量|

## "stage" 标签

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|id|int|伏击波次可生成的楼层章节|
