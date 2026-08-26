---
tags:
  - Class
---
# Class "LootList"

## Constructors
### LootList () {: aria-label='Constructors' }
#### [LootList](LootList.md) LootList ( )  {: .copyable aria-label='Constructors' }
返回 `LootList` 中包含的 LootListEntry 条目表。
## Functions

### GetEntries () {: aria-label='Functions' }
#### [LootListEntry](LootListEntry.md)[] GetEntries ( ) {: .copyable aria-label='Functions' }
返回 `LootList` 中包含的 LootListEntry 条目表。

___
### PushEntry () {: aria-label='Functions' }
#### void PushEntry ( [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) Type, int Variant, int SubType, int Seed = Random(), [RNG](RNG.md) RNG = nil ) {: .copyable aria-label='Functions' }
虽然通常用于生成心、炸弹等掉落物的箱子和袋子，但每个 `EntityPickup` 都有一个 `LootList`，你可以将任意类型、变体和子类型作为 LootListEntry 推入其中。
mod:AddCallback(ModCallbacks.MC_PRE_PICKUP_GET_LOOT_LIST, mod.onPrePickupGetLootList)
创建一个 [LootListEntry](LootListEntry.md)，并将其推入 `LootList`。
local lootList = LootList()
local mod = RegisterMod("Delirium Unboxing", 1)
function mod:onPrePickupGetLootList(pickup, shouldAdvance)
end
```lua
这段代码会让所有普通箱子都包含整个游戏中最强的 Boss。作为额外效果，使用 Guppy's Eye 还能看到一幅令人毛骨悚然的图像。
if pickup.Variant ~= PickupVariant.PICKUP_CHEST then return end
return lootList
???+ example "Example Code"
lootList:PushEntry(EntityType.ENTITY_DELIRIUM, 0, 0)
```
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
