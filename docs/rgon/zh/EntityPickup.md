---
tags:
  - Class
---
# Class "EntityPickup"

## Class Diagram
--8<-- "rgon/zh/snippets/EntityClassDiagram_NewFunkyMode.md"
## Functions

### AddCollectibleCycle () {: aria-label='Functions' }
#### boolean AddCollectibleCycle ( int id ) {: .copyable aria-label='Functions' }

___
### CanReroll () {: aria-label='Functions' }
#### boolean CanReroll ( ) {: .copyable aria-label='Functions' }

___
### GetAlternatePedestal () {: aria-label='Functions' }
#### int GetAlternatePedestal ( ) {: .copyable aria-label='Functions' }

___
### GetCollectibleCycle () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)[] GetCollectibleCycle ( ) {: .copyable aria-label='Functions' }
返回一个表格，其中包含在其收藏品循环（例如错误王冠）中使用的所有 [CollectibleTypes](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)。

### GetDropDelay () {: aria-label='Functions' }
#### int GetDropDelay ( ) {: .copyable aria-label='Functions' }

___
### GetFlipCollectible () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetFlipCollectible ( ) {: .copyable aria-label='Functions' }
如果存在 Flip 保存状态，则返回 [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)，否则返回 `nil`。

___
### GetLootList () {: aria-label='Functions' }
#### [LootList](LootList.md) GetLootList ( boolean shouldAdvance = false ) {: .copyable aria-label='Functions' }
返回拾取物的 [LootList](LootList.md) 的**只读**版本。可以通过使用嗝屁猫之眼收藏品来查看拾取物中的战利品。

`shouldAdvance` 决定是否要前进 loot RNG。

___
### GetMegaChestLeftCollectible () {: aria-label='Functions' }
#### [EntityPickup](EntityPickup.md) GetMegaChestLeftCollectible ( ) {: .copyable aria-label='Functions' }
如果对打开的 Mega Chest 右侧的 EntityPickup 调用，则返回左侧的收藏品；否则返回 `nil`。

___
### GetMegaChestOtherCollectible () {: aria-label='Functions' }
#### [EntityPickup](EntityPickup.md), boolean GetMegaChestRightCollectible ( ) {: .copyable aria-label='Functions' }
如果对属于打开的 Mega Chest 的 EntityPickup 调用，则返回另一个收藏品，以及一个表示当前收藏品是否位于右侧的布尔值；否则返回 `nil`。

___
### GetMegaChestRightCollectible () {: aria-label='Functions' }
#### [EntityPickup](EntityPickup.md) GetMegaChestRightCollectible ( ) {: .copyable aria-label='Functions' }
如果对打开的 Mega Chest 左侧的 EntityPickup 调用，则返回右侧的收藏品；否则返回 `nil`。

___
### GetPickupGhost () {: aria-label='Functions' }
#### [EntityEffect](EntityEffect.md) GetPickupGhost ( ) {: .copyable aria-label='Functions' }
返回通过嗝屁猫之眼可见的 `EffectVariant.PICKUP_GHOST` 实体效果。如果不可见，则返回 `nil`。

### GetPriceSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetPriceSprite ( ) {: .copyable aria-label='Functions' }

___
### GetRandomPickupVelocity () {: aria-label='Functions' }
#### [Vector](Vector.md) GetRandomPickupVelocity ( [Vector](Vector.md) Position, [RNG](RNG.md) RNG = nil, int VelocityType = 0 ) {: .copyable aria-label='Functions' }
`VelocityType` 1 会将拾取物朝下方的锥形区域射出，主要用于乞丐的奖励。
`VelocityType` 0 会将拾取物朝所需位置周围的随机方向射出。
`VelocityType` 似乎也会影响挑战房间中的拾取物，使其速度更慢。

???+ warning "Warning"

    这是一个静态函数，必须通过 `EntityPickup.GetRandomPickupVelocity(Position, RNG, VelocityType)` 调用。

___
### GetVarData () {: aria-label='Functions' }
#### int GetVarData ( ) {: .copyable aria-label='Functions' }

___
### HasFlipData () {: aria-label='Functions' }
#### boolean HasFlipData ( ) {: .copyable aria-label='Functions' }
如果拾取物是收藏品且具有 Flip 保存状态，则返回 `true`。

___
### InitFlipState () {: aria-label='Functions' }
#### void InitFlipState ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) = CollectibleType.COLLECTIBLE_NULL, boolean SetupCollectibleGraphics = true ) {: .copyable aria-label='Functions' }
使用提供的 [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) 为拾取物初始化翻转状态。

___
### IsBlind () {: aria-label='Functions' }
#### boolean IsBlind ( ) {: .copyable aria-label='Functions' }
如果拾取物是收藏品基座且处于隐藏状态，则返回 `true`。对于非收藏品实体拾取物，始终返回 `false`。

???+ warning "Warning"

    此值不考虑盲目诅咒，它仅反映通常在不涉及诅咒的情况下处于盲目状态的拾取物的盲目状态。例如：隐藏路线的额外物品。

___
### MakeShopItem () {: aria-label='Functions' }
#### void MakeShopItem ( int ShopItemID ) {: .copyable aria-label='Functions' }

___
### ReloadGraphics () {: aria-label='Functions' }
#### void ReloadGraphics ( boolean IgnoreBlind ) {: .copyable aria-label='Functions' }

___
### RemoveCollectibleCycle () {: aria-label='Functions' }
#### void RemoveCollectibleCycle ( ) {: .copyable aria-label='Functions' }

___
### SetAlternatePedestal () {: aria-label='Functions' }
#### void SetAlternatePedestal ( int PedestalType ) {: .copyable aria-label='Functions' }
设置物品基座的图形。对非收藏品实体拾取物无效。

___
### SetDropDelay () {: aria-label='Functions' }
#### void SetDropDelay ( int Delay ) {: .copyable aria-label='Functions' }

___
### SetForceBlind () {: aria-label='Functions' }
#### void SetForceBlind ( boolean SetBlind ) {: .copyable aria-label='Functions' }
像盲目诅咒一样隐藏基座物品。对非收藏品实体拾取物无效。

___
### SetNewOptionsPickupIndex () {: aria-label='Functions' }
#### int SetNewOptionsPickupIndex ( ) {: .copyable aria-label='Functions' }
返回新的拾取物索引。

___
### SetupCollectibleGraphics () {: aria-label='Functions' }
[ ](#){: .static .tooltip .badge }
#### static void SetupCollectibleGraphics ( [Sprite](Sprite.md) Sprite, integer Layer, [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, boolean Blind = false, integer Seed = Random(), boolean LoadGraphics = false  ) {: .copyable aria-label='Functions' }
静态方法。用于将精灵对象指定图层的 spritesheet 替换为收藏品精灵。Seed 用于在愚人节挑战中选择随机收藏品。

___
### SetVarData () {: aria-label='Functions' }
#### void SetVarData ( int VarData ) {: .copyable aria-label='Functions' }

___
### TriggerTheresOptionsPickup () {: aria-label='Functions' }
#### void TriggerTheresOptionsPickup ( ) {: .copyable aria-label='Functions' }
移除与目标拾取物具有相同选项组（OptionsPickupIndex）的拾取物。

___
### TryFlip () {: aria-label='Functions' }
#### boolean TryFlip ( ) {: .copyable aria-label='Functions' }
尝试翻转收藏品，例如在使用翻转物品对带有第二个全息收藏品（位于第一个后面）的收藏品基座进行操作时。如果成功则返回 `true`，否则返回 `false`；如果用于非收藏品实体拾取物，也返回 `false`。

___
### TryInitOptionCycle () {: aria-label='Functions' }
#### boolean TryInitOptionCycle ( int NumCycle ) {: .copyable aria-label='Functions' }
使收藏品基座开始循环显示指定数量的收藏品，包括其自身的收藏品类型。

___
### TryRemoveCollectible () {: aria-label='Functions' }
#### boolean TryRemoveCollectible ( ) {: .copyable aria-label='Functions' }
如果成功从基座上移除了一个收藏品，则返回 `true`。如果基座已经为空，或者对非收藏品实体拾取物调用此函数，则返回 `false`。
尝试从物品基座上移除收藏品。

___
### UpdatePickupGhosts () {: aria-label='Functions' }
#### void UpdatePickupGhosts ( ) {: .copyable aria-label='Functions' }
根据拾取物当前的 [LootList](LootList.md) 更新 `EffectVariant.PICKUP_GHOST` 实体效果。

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
