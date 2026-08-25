---
tags:
  - File
---
# 文件 "curses.xml"

存储可用诅咒的名称和ID。


**Resource-Folder**{: .xmlInfo .green }：将此文件放入模组的resources文件夹会重命名诅咒。

**Content-Folder**{: .xmlInfo .green }：将此文件放入模组的content文件夹会添加一个新的诅咒。新诅咒必须通过lua应用，因为它无法正常遇到！


| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|id|int|诅咒在游戏中的ID。当文件在content文件夹时会被游戏覆盖。|
|name|string|诅咒的名称|