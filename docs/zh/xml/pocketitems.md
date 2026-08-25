---
tags:
  - File
---
# 文件 "pocketitems.xml"

**Resource-Folder**{: .xmlInfo .red}：在模组的resource文件夹中使用此文件会替换原始文件。

**Content-Folder**{: .xmlInfo .green }：在content文件夹中使用会添加新卡牌和药丸效果。

`pocketitems.xml` 用于两个截然不同的目的：添加卡牌和添加药丸效果。这两者的xml语法不同，见下文。

## 卡牌与符文

卡牌用 `<card ... />` 标记，例如：

```xml
<card type="tarot" pickup="1" description="Where journey begins" id="1" name="0 - The Fool" announcer="375" announcerdelay="60" mimiccharge="2" />
```
符文与卡牌属性相同，但用 `<rune ... />` 或 type="rune" 标记。在原版文件中，除soul stone外所有符文都用`<rune>`标签和type。soul stone用`<card>`标签和`rune`类型，但行为与其他符文一致。符文示例：
```xml
<rune type="rune" pickup="3" achievement="89" description="Some description" id="32" name="Some Rune" announcer="341" mimiccharge="2" />
```


| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|name|string|卡牌名称|
|description|string|卡牌描述|
|hud|string|卡牌正面动画在`content/gfx/ui_cardfronts.anm2`中的名称，仅mod中使用。|
|type|string|`tarot`、`tarot_reverse`、`suit`、`special`、`rune`或`object`。除`object`和`rune`外的类型可用Blank Card模仿，`rune`类型可用Clear Rune模仿。[ ](#){: .reporplus .tooltip .badge }|
|mimiccharge|int|用Blank Card/Clear Rune模仿时所需充能。[ ](#){: .reporplus .tooltip .badge }|
|pickup|int|该卡牌pickup对应的entities2.xml子类型。[ ](#){: .reporplus .tooltip .badge }|
|announcer|int|使用卡牌时播放的音效ID|
|announcerdelay|int|卡牌使用与音效播放之间的帧延迟|
|achievement|int|与原版成就绑定的卡牌|
|greedmode|bool|该pocketitem是否可在greedmode获得。默认true|

在Afterbirth+和Repentance中，添加自定义卡牌时必须包含`hud`标签，并在mod的`content/gfx/`文件夹下添加名为`ui_cardfronts.anm2`的anm2。该anm2需包含与`hud`标签同名的动画，作为卡牌正面显示在HUD中。卡牌添加后，可通过lua的`Isaac.GetCardIdByName(string cardHudName)`函数获取其id，参数为`hud`标签指定的名称。

**如果卡牌背面与已有pickup相同**，应将`pickup`设为已有pickup的子类型，无需关心entities2.xml。否则可在Repentance中用`pickup`标签，通过一个anm2设置卡牌HUD和pickup外观。为此需在entities2.xml中添加对应的tarot卡类型和variant（5.300），subtype与`pickup`一致，如下：

在`pocketitems.xml`：
```xml
<card type="object" name="Custom Object" description="" hud="Custom Object" pickup="160"/>
```

在`content/entities2.xml`：
```xml
<entities anm2root="gfx/" version="5">
<entity anm2path="custom_object.anm2" baseHP="0" boss="0" champion="0" collisionDamage="0" collisionMass="3" collisionRadius="12" friction="1" id="5" name="Custom Object" numGridCollisionPoints="24" shadowSize="16" stageHP="0" variant="300" subtype="160">
   <preload-snd id="8" /> <!-- BOOK_PAGE_TURN_12 -->
</entity>
</entities>
```

entities2.xml中指定的anm2应包含HUD和HUDSmall动画，以及常规pickup动画。可参考原版资源中的`gfx/05.301_tarot card.anm2`！即使entities2.xml放在content目录，anm2文件也应放在resources目录，否则游戏无法找到。例如上述entities2.xml，动画文件应放在`resources/gfx/custom_object.anm2`。

注意entities2.xml和`pickup`标签用到的subtype**不能**用于生成卡牌，否则会导致游戏崩溃。必须通过卡牌id生成/给予卡牌，可用`Isaac.GetCardIdByName(string cardHudName)`获取。如需在控制台查看当前id，可输入`g kID`并查找自动补全；原版最后一张卡是`k97`（Soul of Jacob），mod卡id从`k98`开始。

与Afterbirth+不同，pocketitems.xml中添加的卡牌会自动加入卡池。

## 药丸效果

药丸效果比卡牌更易添加，且创建后会自动加入药丸池。用`<pilleffect ... />`标记，例如：

```xml
<pilleffect announcer2="760" id="0" name="Bad Gas" announcer="328" class="1+" mimiccharge="1" />
```


| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|name|string|药丸效果名称|
|description|string|药丸效果描述（可选，用于I found pills）[ ](#){: .reporplus .tooltip .badge }|
|class|string|0-3，分别表示笑话、轻微、中等、重大效果。可加`+`或`-`表示正/负面，不加表示中性。[ ](#){: .reporplus .tooltip .badge }|
|mimiccharge|int|用Placebo模仿时所需充能[ ](#){: .reporplus .tooltip .badge }|
|announcer|int|使用药丸时播放的音效ID|
|announcer2|int|作为horse pill使用时播放的音效ID[ ](#){: .reporplus .tooltip .badge }|
|announcerdelay|int|药丸使用与音效播放之间的帧延迟|
|achievement|int|与原版成就绑定的药丸效果|
|greedmode|bool|该pocketitem是否可在greedmode获得。默认true|


`pocketitems.xml` 文件示例，添加一张新卡牌和一个新药丸效果：

```xml
<pocketitems>
  <card type="object" name="Custom Object" description="It's custom!" hud="Custom Object" pickup="160"/>
  <pilleffect name="Damage Up" class="3+" mimiccharge="12" />
</pocketitems>
```
