---
tags:
  - Class
---
# Class "EntityBomb"

## Class Diagram
--8<-- "rgon/zh/snippets/EntityClassDiagram_NewFunkyMode.md"
## Functions

### GetCostumeLayerSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetCostumeLayerSprite ( [BombCostumeLayer](enums/BombCostumeLayer.md) LayerID ) {: .copyable aria-label='Functions' }

___
### GetExplosionCountdown () {: aria-label='Functions' }
#### int GetExplosionCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetFallAcceleration () {: aria-label='Functions' }
#### float GetFallAcceleration ( ) {: .copyable aria-label='Functions' }

___
### GetFallSpeed () {: aria-label='Functions' }
#### float GetFallSpeed ( ) {: .copyable aria-label='Functions' }

___
### GetHitList () {: aria-label='Functions' }
#### int[] GetHitList ( ) {: .copyable aria-label='Functions' }
Returns an array of hit entities using their [Index](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#index) field.

___
### GetRocketAngle () {: aria-label='Functions' }
#### float GetRocketAngle ( ) {: .copyable aria-label='Functions' }
火箭炸弹的目标角度。它会影响火箭炸弹的移动和精灵图的朝向。

___
### GetRocketSpeed () {: aria-label='Functions' }
#### float GetRocketSpeed ( ) {: .copyable aria-label='Functions' }
火箭炸弹的目标速度。自然情况下，其速度每帧增加1。

___
### GetScale () {: aria-label='Functions' }
#### float GetScale ( ) {: .copyable aria-label='Functions' }
用于应用炸弹外观的动画集。

___
### IsLoadingCostumes () {: aria-label='Functions' }
#### boolean IsLoadingCostumes ( ) {: .copyable aria-label='Functions' }

___
### IsPrismTouched () {: aria-label='Functions' }
#### boolean IsPrismTouched ( ) {: .copyable aria-label='Functions' }
返回该炸弹是否是通过天使棱镜效果创建的。

___
### SetFallAcceleration () {: aria-label='Functions' }
#### void SetFallAcceleration ( float Acceleration ) {: .copyable aria-label='Functions' }

___
### SetFallSpeed () {: aria-label='Functions' }
#### void SetFallSpeed ( float Speed ) {: .copyable aria-label='Functions' }

___
### SetLoadCostumes () {: aria-label='Functions' }
#### void SetLoadCostumes ( boolean Load = true ) {: .copyable aria-label='Functions' }

___
### SetPrismTouched () {: aria-label='Functions' }
#### void SetPrismTouched ( boolean IsTouched ) {: .copyable aria-label='Functions' }
设置该炸弹是否是通过天使棱镜效果创建的。

___
### SetRocketAngle () {: aria-label='Functions' }
#### void SetRocketAngle ( float Angle ) {: .copyable aria-label='Functions' }
设置火箭炸弹的目标角度。它会影响火箭炸弹的移动和精灵图的朝向。

___
### SetRocketSpeed () {: aria-label='Functions' }
#### void SetRocketSpeed ( float Speed ) {: .copyable aria-label='Functions' }
设置火箭炸弹的目标速度。请注意，其速度自然情况下每帧会增加1。

___
### SetScale () {: aria-label='Functions' }
#### void SetScale ( float Scale ) {: .copyable aria-label='Functions' }
应与 [SetLoadCostumes](#setloadcostumes) 方法一起使用。

___
### UpdateDirtColor () {: aria-label='Functions' }
#### void UpdateDirtColor ( ) {: .copyable aria-label='Functions' }

___
