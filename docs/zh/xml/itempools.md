---
tags:
  - File
---
# 文件 "itempools.xml"

本页面需要补充内容。你可以使用编辑按钮进行贡献！

**Resource-Folder**{: .xmlInfo }：在模组的resource文件夹中使用此文件尚未经过测试。

**Content-Folder**{: .xmlInfo }：在模组的content文件夹中使用此文件尚未经过测试。


| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
| Id | int | *(可选)*<br> itempool中物品的id<br>使用此变量时不能使用"name"变量。|
| Name | String | *(可选，推荐)* itempool中物品的名称。<br>使用此变量时不能使用"id"变量。 |
| Weight | float | 该物品从池中被抽取的相对“概率”。`默认=1`。如果该值达到"RemoveOn"，该物品将不再被抽取。|
| DecreaseBy | float | 物品可被抽取的次数。`默认=1`<br>每次物品被抽取时，该值会从其Weight中减去。这样在重骰时该物品出现概率会降低，直到weight达到"RemoveOn"。|
| RemoveOn | float | 当Weight达到该值时，物品将不再能被抽取。`默认="0.1"`|

## 物品出现次数计算
物品在itempool中出现的次数由以下公式决定：
```lua
math.ceil( ( Weight - RemoveOn ) / DecreaseBy )
```
（`math.ceil` 会将数字向上取整）

## 示例

???+ example "示例代码"
    下面的代码描述了一个包含3个物品的itempool。

    ```xml
    <ItemPools>
        <Pool Name="myItempool">
                <!--The Sad Onion --- 池中出现1次-->
            <Item Id="1" Weight="1" DecreaseBy="1" RemoveOn="0.1"/>
                <!--The Inner Eye --- 池中出现5次 (10-1)/2 = 4.5 => 5 -->
            <Item Id="2" Weight="11" DecreaseBy="2" RemoveOn="1"/>
                 <!--Spoon Bender --- 池中出现4次 (1-0.1)/0.25 = 3.6 => 4 -->
            <Item Id="3" Weight="1" DecreaseBy="0.25" RemoveOn="0.1"/>
        </Pool>
    </ItemPools>
    ```