---
tags:
  - Class
---
# Class "EntityLaser"

## Class Diagram
--8<-- "rgon/zh/snippets/EntityClassDiagram_NewFunkyMode.md"
## Modified Variables
___
### HomingType {: aria-label='Modified Variables' }
#### int HomingType  {: .copyable aria-label='Modified Variables' }
与默认值相同，但现在返回正确的整数值，而非用户数据。

___

## Functions

### FireSplitTear () {: aria-label='Functions' }
#### [EntityTear](EntityTear.md) FireSplitTear ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity, float DamageMultiplier = 0.5, float SizeMultiplier = 0.6, int Variant = 0, [SplitTearType](enums/SplitTearType.md) splitType = SplitTearType.SPLIT_GENERIC ) {: .copyable aria-label='Functions' }
Fire a new tear that inherits many attributes from this laser (flags, damage, size, color, etc).

This will also trigger the `MC_POST_FIRE_SPLIT_TEAR` callback. For custom effects, a string may be passed in place of the [SplitTearType](enums/SplitTearType.md).

___
### GetDamageMultiplier () {: aria-label='Functions' }
#### float GetDamageMultiplier ( ) {: .copyable aria-label='Functions' }

___
### GetDisableFollowParent () {: aria-label='Functions' }
#### boolean GetDisableFollowParent ( ) {: .copyable aria-label='Functions' }

___
### GetHitList () {: aria-label='Functions' }
#### int GetHitList ( ) {: .copyable aria-label='Functions' }
Returns an array of hit entities using their [Index](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#index) field.

___
### GetOneHit () {: aria-label='Functions' }
#### boolean GetOneHit ( ) {: .copyable aria-label='Functions' }

___
### GetScale () {: aria-label='Functions' }
#### float GetScale ( ) {: .copyable aria-label='Functions' }

___
### GetShrink () {: aria-label='Functions' }
#### boolean GetShrink ( ) {: .copyable aria-label='Functions' }

___
### GetTimeout () {: aria-label='Functions' }
#### int GetTimeout ( ) {: .copyable aria-label='Functions' }

___
### IsMultidimensionalTouched () {: aria-label='Functions' }
#### boolean IsMultidimensionalTouched ( ) {: .copyable aria-label='Functions' }
返回该激光是否通过“多维宝宝”效果创建。

___
### IsPrismTouched () {: aria-label='Functions' }
#### boolean IsPrismTouched ( ) {: .copyable aria-label='Functions' }
返回该激光是否通过“天使棱镜”效果创建。

___
### RecalculateSamplesNextUpdate () {: aria-label='Functions' }
#### void RecalculateSamplesNextUpdate ( ) {: .copyable aria-label='Functions' }
请求在下一次更新时完全重新计算激光的形状。可用于强制激光立即改变其最大距离/半径，而不是逐渐过渡到新值。对 `OneHit` 或非采样激光无效。

___
### ResetSpriteScale () {: aria-label='Functions' }
#### void ResetSpriteScale ( ) {: .copyable aria-label='Functions' }

___
### RotateToAngle () {: aria-label='Functions' }
#### void RotateToAngle ( float Angle, float Speed = 8.0 ) {: .copyable aria-label='Functions' }

___
### SetDamageMultiplier () {: aria-label='Functions' }
#### void SetDamageMultiplier ( float DamageMult ) {: .copyable aria-label='Functions' }

___
### SetDisableFollowParent () {: aria-label='Functions' }
#### void SetDisableFollowParent ( boolean Value ) {: .copyable aria-label='Functions' }

___
### SetPrismTouched () {: aria-label='Functions' }
#### void SetPrismTouched ( boolean IsTouched ) {: .copyable aria-label='Functions' }
设置该激光是否通过“天使棱镜”效果创建。

___
### SetScale () {: aria-label='Functions' }
#### void SetScale ( float Value ) {: .copyable aria-label='Functions' }

___
### SetShrink () {: aria-label='Functions' }
#### void SetShrink ( boolean Value ) {: .copyable aria-label='Functions' }

___
### SetTimeout () {: aria-label='Functions' }
#### void SetTimeout ( int Value ) {: .copyable aria-label='Functions' }

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
