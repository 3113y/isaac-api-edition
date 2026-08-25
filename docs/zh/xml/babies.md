---
tags:
  - File
---
# 文件 "babies.xml"

此文件用于存储联机宝宝（coop-babies）的信息。

将此文件放入模组的 resource 文件夹并删除条目会导致崩溃。

**Resource-Folder**{: .xmlInfo .green}：将此文件放入你的模组 "resource" 文件夹中将会替换原始文件。

**Content-Folder**{: .xmlInfo .red}：将此文件放入你的模组 "content" 文件夹中不会产生任何效果！

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|id|int|宝宝的标识符|
|name|string|宝宝的名称|
|skin|string|宝宝所用 .png 文件的路径|
|achievement|int|解锁该宝宝所需的成就ID|
