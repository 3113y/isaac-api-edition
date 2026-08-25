---
tags:
  - File
---
# 文件 "minibosses.xml"

此文件用于存储特定小Boss房间中小Boss的名称。该名称会在“streak”动画中显示，如“Isaac vs. MINIBOSS_NAME”。

**Resource-Folder**{: .xmlInfo .green}：将此文件放入你的模组 "resource" 文件夹会替换原始文件。

**Content-Folder**{: .xmlInfo .red}：将此文件放入你的模组 "content" 文件夹没有任何效果！


| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|id|int|触发该streak的房间ID。RoomID应以10为步进。<br>**示例**：`2020`<br><br>不以0结尾的ID会自动归类到以0结尾的ID。<br>**示例**：`2023`会归类到`2020`。|
|name|string|将在streak动画中显示的名称|