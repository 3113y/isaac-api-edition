---
tags:
  - Class
---
# Class "EntityFamiliar"

## Class Diagram
--8<-- "rgon/zh/snippets/EntityClassDiagram_NewFunkyMode.md"
## Functions

### CanBeDamagedByEnemies () {: aria-label='Functions' }
#### boolean CanBeDamagedByEnemies ( ) {: .copyable aria-label='Functions' }

___
### CanBeDamagedByLasers () {: aria-label='Functions' }
#### boolean CanBeDamagedByLasers ( ) {: .copyable aria-label='Functions' }

___
### CanBeDamagedByProjectiles () {: aria-label='Functions' }
#### boolean CanBeDamagedByProjectiles ( ) {: .copyable aria-label='Functions' }

___
### CanBlockProjectiles () {: aria-label='Functions' }
#### boolean CanBlockProjectiles ( ) {: .copyable aria-label='Functions' }

___
### CanCharm () {: aria-label='Functions' }
#### boolean CanCharm ( ) {: .copyable aria-label='Functions' }

___
### GetActiveWeaponEntity () {: aria-label='Functions' }
#### [Entity](Entity.md) GetActiveWeaponEntity ( ) {: .copyable aria-label='Functions' }
Returns the Entity associated with the familiar's active [Weapon](Weapon.md).

Returns `nil` if it cannot be found.

___
### GetActiveWeaponNumFired () {: aria-label='Functions' }
#### int GetActiveWeaponNumFired ( ) {: .copyable aria-label='Functions' }
Returns the amount of times the familiar's active [Weapon](Weapon.md) has been fired.

___
### GetDirtColor () {: aria-label='Functions' }
#### [Color](Color.md) GetDirtColor ( ) {: .copyable aria-label='Functions' }

___
### GetFollowerPriority () {: aria-label='Functions' }
#### [FollowerPriority](enums/FollowerPriority.md) GetFollowerPriority ( ) {: .copyable aria-label='Functions' }

___
### GetItemConfig () {: aria-label='Functions' }
#### [ItemConfigItem](ItemConfig_Item.md) GetItemConfig ( ) {: .copyable aria-label='Functions' }
返回赋予此跟班的道具所对应的 ItemConfigItem 对象。

如果跟班不是由道具生成的，则返回 nil。

___
### GetMoveDelayNum () {: aria-label='Functions' }
#### int GetMoveDelayNum ( ) {: .copyable aria-label='Functions' }
返回跟班相对于玩家移动的延迟帧数。30 帧 = 1 秒。

___
### GetMultiplier () {: aria-label='Functions' }
#### float GetMultiplier ( ) {: .copyable aria-label='Functions' }
返回跟班的“乘数”；该值会受到 **BFFS!** 或 **Hive Mind** 等效果的影响，通常用于乘算跟班伤害等属性。

???- info "乘数"

    - **堕化拉撒路长子权**：x0.25
    - **BFFS!** 和 **Hive Mind**：x2.0
    - **堕化伯大尼**：x0.75

___
### GetPathfinder () {: aria-label='Functions' }
#### [PathFinder](https://wofsauge.github.io/IsaacDocs/rep/PathFinder.html) GetPathfinder ( ) {: .copyable aria-label='Functions' }

___
### GetRandomWisp () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetRandomWisp ( [RNG](RNG.md) RNG ) {: .copyable aria-label='Functions' }
???+ warning "Warning"
    This is a static function and must be called via `EntityFamiliar.GetRandomWisp(RNG)`.

___
### GetWeapon () {: aria-label='Functions' }
#### [Weapon](Weapon.md) GetWeapon ( ) {: .copyable aria-label='Functions' }
对于不模仿玩家攻击的跟班（如魅魔等），返回 `nil`。

___
### InvalidateCachedMultiplier () {: aria-label='Functions' }
#### void InvalidateCachedMultiplier ( ) {: .copyable aria-label='Functions' }
当下一次调用 [GetMultiplier](EntityFamiliar.md#getmultiplier) 时，触发 [MC_EVALUATE_FAMILIAR_MULTIPLIER](enums/ModCallbacks.md#mc_evaluate_familiar_multiplier) 来重新计算/允许修改乘数。

___
### IsCharmed () {: aria-label='Functions' }
#### boolean IsCharmed ( ) {: .copyable aria-label='Functions' }

___
### IsLilDelirium () {: aria-label='Functions' }
#### boolean IsLilDelirium ( ) {: .copyable aria-label='Functions' }

___
### RemoveFromPlayer () {: aria-label='Functions' }
#### void RemoveFromPlayer ( ) {: .copyable aria-label='Functions' }

___
### SetLilDelirium () {: aria-label='Functions' }
#### void SetLilDelirium ( boolean isLilDelirium ) {: .copyable aria-label='Functions' }

___
### SetMoveDelayNum () {: aria-label='Functions' }
#### void SetMoveDelayNum ( int Delay ) {: .copyable aria-label='Functions' }
设置跟班相对于玩家移动的延迟帧数。30 帧 = 1 秒。

___
### TriggerRoomClear () {: aria-label='Functions' }
#### void TriggerRoomClear ( ) {: .copyable aria-label='Functions' }

___
### TryAimAtMarkedTarget () {: aria-label='Functions' }
#### [Vector](Vector.md) TryAimAtMarkedTarget ( [Vector](Vector.md) AimDirection, [Direction](https://wofsauge.github.io/IsaacDocs/rep/enums/Direction.html) Direction = Direction.NO_DIRECTION ) {: .copyable aria-label='Functions' }
#### boolean, table TryAimAtMarkedTarget ( [Vector](Vector.md) AimDirection = nil, [Direction](https://wofsauge.github.io/IsaacDocs/rep/enums/Direction.html) Direction = Direction.NO_DIRECTION, [Vector](Vector.md) TargetPos = nil ) {: .copyable aria-label='Functions' }
如果存在来自 Marked 或 Eye of the Occult/Gello 目标的玩家标记，则返回 `true`，否则返回 `false`。
返回包含修改后 AimDirection、Direction 和 TargetPos 的表。

旧版本会返回修改后的 TargetPos；如果失败，则返回 `nil`。

___
### UpdateDirtColor () {: aria-label='Functions' }
#### void UpdateDirtColor ( ) {: .copyable aria-label='Functions' }

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
