---
tags:
  - Class
---
# Class "EntityKnife"

## Class Diagram
--8<-- "rgon/zh/snippets/EntityClassDiagram_NewFunkyMode.md"
## Functions

### FireSplitTear () {: aria-label='Functions' }
#### [EntityTear](EntityTear.md) FireSplitTear ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity, float DamageMultiplier = 0.5, float SizeMultiplier = 0.6, int Variant = 0, [SplitTearType](enums/SplitTearType.md) splitType = SplitTearType.SPLIT_GENERIC ) {: .copyable aria-label='Functions' }
Fire a new tear that inherits many attributes from this knife (flags, damage, size, color, etc).

This will also trigger the `MC_POST_FIRE_SPLIT_TEAR` callback. For custom effects, a string may be passed in place of the [SplitTearType](enums/SplitTearType.md).

___
### GetHitboxParentKnife () {: aria-label='Functions' }
#### [EntityKnife](EntityKnife.md) GetHitboxParentKnife ( ) {: .copyable aria-label='Functions' }
对于由近战武器“挥砍”（骨棒、灵魂之剑等）创建的“hitbox” [EntityKnife](EntityKnife.md)（[KnifeSubType.CLUB_HITBOX](enums/KnifeSubType.md)），此函数会返回该近战武器的“主” [EntityKnife](EntityKnife.md)。其他情况下返回 `nil`；通过其他方式生成的 hitbox 实体也会返回 `nil`。

___
### GetHitList () {: aria-label='Functions' }
#### int[] GetHitList ( ) {: .copyable aria-label='Functions' }
Returns an array of hit entities using their [Index](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#index) field.

___
### GetIsSpinAttack () {: aria-label='Functions' }
#### boolean GetIsSpinAttack ( ) {: .copyable aria-label='Functions' }

___
### GetIsSwinging () {: aria-label='Functions' }
#### boolean GetIsSwinging ( ) {: .copyable aria-label='Functions' }

___
### IsMultidimensionalTouched () {: aria-label='Functions' }
#### boolean IsMultidimensionalTouched ( ) {: .copyable aria-label='Functions' }
返回该匕首是否由“多维宝贝”效果创建。

___
### IsPrismTouched () {: aria-label='Functions' }
#### boolean IsPrismTouched ( ) {: .copyable aria-label='Functions' }
返回该匕首是否由“天使棱镜”效果创建。

___
### SetHitboxParentKnife () {: aria-label='Functions' }
#### void SetHitboxParentKnife ( [EntityKnife](EntityKnife.md) Knife ) {: .copyable aria-label='Functions' }
允许为 `GetHitboxParentKnife` 设置自定义值。此功能仅适用于让近战武器（骨棒、灵魂之剑等）的“hitbox” [EntityKnife](EntityKnife.md)（[KnifeSubType.CLUB_HITBOX](enums/KnifeSubType.md)）指向其“主” [EntityKnife](EntityKnife.md)。

请注意，设置此值不会影响任何原版逻辑；该引用仅为方便模组作者而存在，请合理使用。

___
### SetIsSpinAttack () {: aria-label='Functions' }
#### void SetIsSpinAttack ( boolean isSpinAttack ) {: .copyable aria-label='Functions' }

___
### SetIsSwinging () {: aria-label='Functions' }
#### void SetIsSwinging ( boolean isSwinging ) {: .copyable aria-label='Functions' }

___
### SetMultidimensionalTouched () {: aria-label='Functions' }
#### void SetMultidimensionalTouched ( boolean IsTouched ) {: .copyable aria-label='Functions' }
设置该匕首是否由“多维宝贝”效果创建。

___
### SetPrismTouched () {: aria-label='Functions' }
#### void SetPrismTouched ( boolean IsTouched ) {: .copyable aria-label='Functions' }
设置该匕首是否由“天使棱镜”效果创建。

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
