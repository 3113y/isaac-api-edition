---
tags:
  - Class
---
# Class "GridEntity"

## Modified Functions

### ToTNT () {: aria-label='Modified Functions' }
#### [GridEntityTNT](https://wofsauge.github.io/IsaacDocs/rep/GridEntityTNT.html) ToTNT ( ) {: .copyable aria-label='Modified Functions' }
修改函数以改善网格实体更新回调的行为。

___
### GetRenderPosition () {: aria-label='Functions' }
#### [Vector](Vector.md) GetRenderPosition ( ) {: .copyable aria-label='Functions' }

___
### GetWaterClipFlags () {: aria-label='Functions' }
#### [WaterClipFlag](enums/WaterClipFlag.md) GetWaterClipFlags ( ) {: .copyable aria-label='Functions' }
获取一个位集，用于指示此网格实体应渲染在水面上方还是下方。

可以使用 `ResetWaterClipFlags()` 恢复原版状态。

___
### HurtDamage () {: aria-label='Functions' }
#### void HurtDamage ( [Entity](Entity.md) Entity, int PlayerDamage, int DamageFlags, float Damage, boolean ignoreGridCollision ) {: .copyable aria-label='Functions' }

___
### IsBreakableRock () {: aria-label='Functions' }
#### void IsBreakableRock ( ) {: .copyable aria-label='Functions' }

___
### ResetWaterClipFlags () {: aria-label='Functions' }
#### void ResetWaterClipFlags ( ) {: .copyable aria-label='Functions' }
将水面渲染恢复为默认的原版状态。参见 `SetWaterClipFlags()`。

___
### SetWaterClipFlags () {: aria-label='Functions' }
#### void SetWaterClipFlags ( [WaterClipFlag](enums/WaterClipFlag.md) Flags ) {: .copyable aria-label='Functions' }
允许修改此网格实体应渲染在水面上方还是下方。

请注意，这也会禁用原版对这些标志的自动更改，例如便便被破坏后切换为在水面下方渲染。

可以使用 `ResetWaterClipFlags()` 恢复原版状态。

___
### ToDecoration () {: aria-label='Functions' }
#### [GridEntityDecoration](GridEntityDecoration.md) ToDecoration ( ) {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityDecoration](GridEntityDecoration.md)对象。
???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___
### ToFire () {: aria-label='Functions' }
#### [GridEntityFire](GridEntityFire.md) ToFire ( ) {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityFire](GridEntityFire.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___
### ToGravity () {: aria-label='Functions' }
#### [GridEntityGravity](GridEntityGravity.md) ToGravity ( ) {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityGravity](GridEntityGravity.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___
### ToLock () {: aria-label='Functions' }
#### [GridEntityLock](GridEntityLock.md) ToLock ( ) {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityLock](GridEntityLock.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___
### ToStairs () {: aria-label='Functions' }
#### [GridEntityStairs](GridEntityStairs.md) ToStairs ( ) {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityStairs](GridEntityStairs.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___
### ToStatue () {: aria-label='Functions' }
#### [GridEntityStatue](GridEntityStatue.md) ToStatue ( ) {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityStatue](GridEntityStatue.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___
### ToTeleporter () {: aria-label='Functions' }
#### [GridEntityTeleporter](GridEntityTeleporter.md) ToTeleporter ( ) {: .copyable aria-label='Functions' }   
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityTeleporter](GridEntityTeleporter.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___
### ToTrapDoor () {: aria-label='Functions' }
#### [GridEntityTrapDoor](GridEntityTrapDoor.md) ToTrapDoor ( ) {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityTrapDoor](GridEntityTrapDoor.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___
### ToWall () {: aria-label='Functions' }
#### [GridEntityWall](GridEntityWall.md) ToWall ( ) {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityWall](GridEntityWall.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___
### ToWeb () {: aria-label='Functions' }
#### [GridEntityWeb](GridEntityWeb.md) ToWeb ( ) {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityWeb](GridEntityWeb.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
