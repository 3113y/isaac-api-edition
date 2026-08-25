---
tags:
  - Class
---
# Class "LootList"

## Constructors
### LootList () {: aria-label='Constructors' }
#### [LootList](LootList.md) LootList ( )  {: .copyable aria-label='Constructors' }
Returns a table of LootListEntries contained in the `LootList`.
## Functions

### GetEntries () {: aria-label='Functions' }
#### [LootListEntry](LootListEntry.md)[] GetEntries ( ) {: .copyable aria-label='Functions' }
Returns a table of LootListEntries contained in the `LootList`.

___
### PushEntry () {: aria-label='Functions' }
#### void PushEntry ( [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) Type, int Variant, int SubType, int Seed = Random(), [RNG](RNG.md) RNG = nil ) {: .copyable aria-label='Functions' }
While usually reserved for chests and sacks that give pickups like hearts, bombs, etc, every `EntityPickup` has a `LootList` and you can push any type, variant, and subtype as a LootListEntry.
mod:AddCallback(ModCallbacks.MC_PRE_PICKUP_GET_LOOT_LIST, mod.onPrePickupGetLootList)
Creates and pushes a [LootListEntry](LootListEntry.md) into the `LootList`.
local lootList = LootList()
local mod = RegisterMod("Delirium Unboxing", 1)
function mod:onPrePickupGetLootList(pickup, shouldAdvance)
end
```lua
This code makes all regular chests contain the best boss in the entire game. As a bonus, use Guppy's Eye for a horrifying image.
if pickup.Variant ~= PickupVariant.PICKUP_CHEST then return end
return lootList
???+ example "Example Code"
lootList:PushEntry(EntityType.ENTITY_DELIRIUM, 0, 0)
```
