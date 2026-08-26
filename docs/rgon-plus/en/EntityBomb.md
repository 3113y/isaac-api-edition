---
tags:
  - Class
---
> Documentation prose polished by a constrained language model; API facts and signatures retain their upstream source.

# Class "EntityBomb"

## Class Diagram
--8<-- "rgon-plus/en/snippets/EntityClassDiagram_NewFunkyMode.md"
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
Returns the target angle for rocket bombs. It affects both their movement and sprite orientation.

___
### GetRocketSpeed () {: aria-label='Functions' }
#### float GetRocketSpeed ( ) {: .copyable aria-label='Functions' }
Returns the target speed for rocket bombs. Under normal conditions, it increases by 1 every frame.

___
### GetScale () {: aria-label='Functions' }
#### float GetScale ( ) {: .copyable aria-label='Functions' }
Used to apply the animation set for the bomb costume.

___
### IsLoadingCostumes () {: aria-label='Functions' }
#### boolean IsLoadingCostumes ( ) {: .copyable aria-label='Functions' }

___
### IsPrismTouched () {: aria-label='Functions' }
#### boolean IsPrismTouched ( ) {: .copyable aria-label='Functions' }
Returns whether the bomb was created by the Angelic Prism effect.

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
Sets whether the bomb was created by the Angelic Prism effect.

___
### SetRocketAngle () {: aria-label='Functions' }
#### void SetRocketAngle ( float Angle ) {: .copyable aria-label='Functions' }
Sets the target angle for a rocket bomb. It affects both its movement and sprite orientation.

___
### SetRocketSpeed () {: aria-label='Functions' }
#### void SetRocketSpeed ( float Speed ) {: .copyable aria-label='Functions' }
Sets the target speed for a rocket bomb. Under normal conditions, it increases by 1 every frame.

___
### SetScale () {: aria-label='Functions' }
#### void SetScale ( float Scale ) {: .copyable aria-label='Functions' }
Should be used with the [SetLoadCostumes](#setloadcostumes) method.

___
### UpdateDirtColor () {: aria-label='Functions' }
#### void UpdateDirtColor ( ) {: .copyable aria-label='Functions' }

___
