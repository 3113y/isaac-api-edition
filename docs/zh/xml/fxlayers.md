---
tags:
  - File
---
# 文件 "fxlayers.xml"

用于存储关卡中使用的overlay信息。与其他Isaac XML不同，本文件没有一个总的根元素包裹所有内容，而是分为fxLayers、fxRays和fxParams三个元素。

**Resource-Folder**{: .xmlInfo .green}：将此文件放入模组的resource文件夹会覆盖原始文件。

**Content-Folder**{: .xmlInfo }：在模组的content文件夹中使用此文件尚未经过测试。


# fxLayers
## "fx" 标签
| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|id|string||
|path|string|overlay图片的路径。必须为32位深度的.png文件。|
|numLayers|integer|*todo*|
|xMin|float||
|xMax|float||
|yMin|float||
|yMax|float||
|layer|string|可选值: [lighting, foreground, background, behind]|
|stage|integer|可选值: [1-Basement, 2-Caves, 3-Depths, 4-Womb, 5-Blue Womb, 6-Sheol, 7-Chest, 8-Void, 9-Home]|
|altStages|integer|位掩码，1 << [0-原版, 1-WOTL, 2-Afterbirth, 3-未用(旧Greed模式), 4-Repentance, 5-Repentance Alt, 6-特殊(仅用于Abandoned Mineshaft)]|
|parallax|float|overlay会随玩家反方向移动|
|onlyDefaultBackdrop|boolean|*todo*|
|blendMode|integer|*todo*|
|useBGShader|boolean|*todo*|

## "gfx" 标签
"fx" 元素的可选子元素，用于指定overlay。一个"fx"元素可以添加多个"gfx"子元素，具有相同roomshape的会随机选择一个显示。

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|path|string|overlay图片的路径。必须为32位深度的.png文件。|
|roomshape|integer|在RoomShape枚举值对应的房间中出现。|
