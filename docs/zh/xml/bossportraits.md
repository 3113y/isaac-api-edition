---
tags:
  - File
---
# 文件 "bossportraits.xml"

此文件用于存储Boss在VS界面显示的sprite信息。

**Resource-Folder**{: .xmlInfo }：在模组的resource文件夹中使用此文件尚未经过测试。

**Content-Folder**{: .xmlInfo }：在模组的content文件夹中使用此文件尚未经过测试。

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|id|int|Boss的ID|
|name|string|Boss的名称|
|nameimage|string|Boss名牌sprite的.png文件名|
|portrait|string|Boss sprite的.png文件名|
|pivotX|int|Boss sprite应放置的X轴锚点|
|pivotY|int|Boss sprite应放置的Y轴锚点|
|achievement|int|成就ID，具体用途未知|

**可以通过在boss标签内添加`<alt>`标签来添加Boss的替代立绘。**


`bossportraits.xml` 文件示例：
```xml
<bosses root="gfx/ui/boss/" anm2="versusscreen.anm2">
	<boss id="76" name="Wormwood" nameimage="BossName_Wormwood.png" portrait="Portrait_902.0_Wormwood.png" pivotX="84" pivotY="144">
		<alt stage="28" portrait="Portrait_902.0_Wormwood_Dross.png" />
	</boss>
</bosses>
```
