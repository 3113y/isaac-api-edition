---
tags:
  - File
---
# 文件 "bombcostumes.xml"
[ ](#){: .reporplus .tooltip .badge }

用于根据炸弹的TearFlags为其应用外观。

**Resource-Folder**{: .xmlInfo .red}：在模组的resource文件夹中使用此文件会替换原始文件。

**Content-Folder**{: .xmlInfo .green}：在模组的content文件夹中使用此文件会添加新的炸弹costume。

## "bomb" 标签

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|variant|int|应应用costume的[BombVariant](../enums/BombVariant.md)|

## "rule" 标签

???- info ".anm2 文件"
    对于每个指定的.anm2文件，你需要创建4个.anm2文件，分别对应每种炸弹尺寸：
        Scatter Bombs生成的小炸弹、带Mr. Mega的Scatter Bombs小炸弹、普通尺寸炸弹和Mr. Mega尺寸炸弹。
    例如，当你指定`bomb.anm2`时，实际上需要`bomb0.anm2`、`bomb1.anm2`、`bomb2.anm2`和`bomb3.anm2`这四个文件。

???- info "规则优先级"
    你在此文件中包含的规则会在对应variant的默认规则之后列出。炸弹costume会根据这些规则中的标签（如`body`、`front`等）应用。
    最后一个适用规则中存在的标签会被应用。
    例如：同时拥有道具Blood Bombs和Bomber Boy时，放置的炸弹会显示为Blood Bombs的外观，因为两条规则都指定了`body`标签，且Blood Bombs的规则在Bomber Boy之后。

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|includeFlags|int|需要存在的所有[TearFlag位](../enums/TearFlags.md)，用空格分隔，满足条件才会添加该层|
|excludeFlags|int|需要不存在的所有[TearFlag位](../enums/TearFlags.md)，用空格分隔，满足条件才会添加该层|
|back|string|.anm2文件的路径，相对于给定的anm2root，在炸弹后方显示。例如：`flame.anm2`|
|body|string|.anm2文件的路径，相对于给定的anm2root，替换主炸弹sprite。例如：`bomb.anm2`|
|body2|string|.anm2文件的路径，相对于给定的anm2root，和主炸弹sprite一起显示。例如：`homing.anm2`|
|front|string|.anm2文件的路径，相对于给定的anm2root，显示在主炸弹sprite上方。例如：`tears_blood.anm2`|
|front2|string|.anm2文件的路径，相对于给定的anm2root，显示在主炸弹sprite上方。例如：`fast.anm2`<br>当你不希望已应用的`front`动画被覆盖时使用。|
|overlay|string|.anm2文件的路径，相对于给定的anm2root，显示在整个炸弹最上层。例如：`glitter_sparkle.anm2`|
|suffix|string|添加在图片文件路径末尾、`.png`之前的后缀，用于替换与LayerID 0关联的spritesheet图片<br>例如：`_gold`会将`spritesheet-image bomb.png`替换为`bomb_gold.png`|
|suffix2|string|添加在图片文件路径末尾、在`suffix`之后、`.png`之前的后缀，用于替换与LayerID 0关联的spritesheet图片<br>例如：`_gold`会将`spritesheet-image bomb.png`替换为`bomb_gold.png`|


`bombcostumes.xml` 文件示例：
```xml
<bombcostumes anm2root="gfx/items/pick ups/bombs/">
    <bomb variant="0"> <!-- Normal bomb -->
        <!-- TearFlag 31 == TearFlags.TEAR_GLOW -->
        <rule includeFlags="31" body="glow.anm2" />
    </bomb>
</bombcostumes>
```
