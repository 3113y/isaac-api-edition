---
tags:
  - File
---
# 文件 "stages.xml"

此文件用于存储游戏关卡/阶段的信息。

**Resource-Folder**{: .xmlInfo .green}：将此文件放入模组的resource文件夹会替换原版文件。

**Content-Folder**{: .xmlInfo .red}：将此文件放入模组的content文件夹无效！

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|id|int|关卡的内部标识符|
|name|string|关卡的显示名称|
|path|string|在“rooms”文件夹下的.stb文件名，**但写作.xml文件路径**（只需将文件名中的.stb替换为.xml）|
|playerspot|string|Boss战过场动画中，显示在玩家角色下方的.png图片路径|
|bossspot|string|同playerspot，但显示在Boss角色下方|