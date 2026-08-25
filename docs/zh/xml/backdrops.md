---
tags:
  - File
---
# 文件 "backdrops.xml"

此文件用于存储各个关卡中使用的backdrop和sprite的信息。

旧教程: https://www.reddit.com/r/themoddingofisaac/comments/34bhi4/backdrops_explained/

**Resource-Folder**{: .xmlInfo }：在模组的resource文件夹中使用此文件尚未经过测试。

**Content-Folder**{: .xmlInfo }：在模组的content文件夹中使用此文件尚未经过测试。

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|id|int|关卡的ID|
|gfx|string|主backdrop文件的.png文件名|
|walls|int|backdrop文件中wall sprite的数量|
|wallvariants|int|每个wall sprite包含的wall tile数量|
|floors|int|backdrop文件中floor sprite的数量|
|floorvariants|int|floor的变体数量|
|lfloorgfx|string|特殊L型floor sprite的.png文件名|
|nfloorgfx|string|特殊长型或窄型floor sprite的.png文件名|
|props|string|本关卡使用的props的Anm2文件名|
|rocks|string|本关卡使用的rock sprite的.png文件名|
|pit|string|本关卡使用的pit sprite的.png文件名|
|bridge|string|本关卡使用的bridge sprite的.png文件名|
|door|string|本关卡使用的door sprite的.png文件名|
|holeinwall|string|本关卡使用的hole-in-wall sprite的.png文件名|
|watergfx|string|本关卡使用的water sprite的.png文件名|
|waterpit|string|本关卡使用的water-holding pit的.png文件名|
|spikes|string|本关卡使用的spike sprite的.png文件名|
|reversewatergfx|boolean|本关卡的water gfx动画是否需要反转|
|waterpitsmode|string|**用途尚不明确...** 可能的值: [0,1,2]|