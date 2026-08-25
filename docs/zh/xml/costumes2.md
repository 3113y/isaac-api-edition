---
tags:
  - File
---
# 文件 "costumes2.xml"

定义Costume信息。

**Resource-Folder**{: .xmlInfo .green }：将此文件放入模组的resource文件夹会覆盖原始文件。

**Content-Folder**{: .xmlInfo .green }：将此文件放入模组的content文件夹会添加新的Costume。更多信息请参见“添加Costume”教程。

## Costume 参考指南
Connor 制作了一份非常实用的表格，列出了当前游戏中所有Costume。表格包含它们的ID、类型、优先级、层信息以及每个Costume的预览图。

这些信息可以帮助你更好地创建新Costume，了解可能产生冲突的Costume或应设置的优先级。

[--> Connor制作的“Isaac Costumes Reference” <---](https://docs.google.com/spreadsheets/d/1NGa3IARRSvs5XF9lxbYWFnbI77xO1m2YYaKEoB6OyVI/edit?usp=sharing)

## Anm2层结构
Costume的渲染顺序由其anm2文件中的特定“层”定义。每个层同一时间只能渲染一个sprite。一个Costume可以在多个层上有部件（例如“Spoon Bender”的脸、第三只眼和火焰都在不同的层上）。

**层名称**

从下到上：glow < back < body < body{0..1} < head < head{0..5} < top0 < extra

## 属性

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|id|int|Costume在游戏中的ID。当文件在content文件夹时会被游戏覆盖。|
|anm2path|string|.anm2文件的路径|
|type|string|Costume类型。可用值：[none, passive, active, familiar, trinket]|
|priority|int|Costume的优先级，数值越大优先级越高|
|overwriteColor|bool|是否覆盖角色身体颜色（默认：false）|
|isFlying|bool|是否显示为飞行角色（默认：false）|
|skinColor|int|Costume的皮肤色（默认：0）|
|hasSkinAlt|bool|Costume是否有所有皮肤色的替代版本（默认：false）|
|hasOverlay|bool|Costume是否有叠加特效（默认：false）|
|forceBodyColor|bool|强制身体颜色（默认：false）[ ](#){: .reporplus .tooltip .badge }|
|forceHeadColor|bool|强制头部颜色（默认：false）[ ](#){: .reporplus .tooltip .badge }|
