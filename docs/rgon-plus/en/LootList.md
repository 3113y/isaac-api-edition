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
Returns a table containing the LootListEntries in the `LootList`.

___
### PushEntry () {: aria-label='Functions' }
#### void PushEntry ( [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) Type, int Variant, int SubType, int Seed = Random(), [RNG](RNG.md) RNG = nil ) {: .copyable aria-label='Functions' }
Creates a [LootListEntry](LootListEntry.md) and pushes it into the `LootList`.

Although `LootList` is usually reserved for chests and sacks that give pickups such as hearts and bombs, every `EntityPickup` has one, and you can push any type, variant, and subtype as a LootListEntry.

???+ example "Example Code"
    This code makes every regular chest contain the strongest boss in the game. As a bonus, use Guppy's Eye to see a horrifying image.

    ```lua
		local mod = RegisterMod("Delirium Unboxing", 1)

		function mod:onPrePickupGetLootList(pickup, shouldAdvance)
			if pickup.Variant ~= PickupVariant.PICKUP_CHEST then return end
			local lootList = LootList()
			lootList:PushEntry(EntityType.ENTITY_DELIRIUM, 0, 0)
			return lootList
		end
		mod:AddCallback(ModCallbacks.MC_PRE_PICKUP_GET_LOOT_LIST, mod.onPrePickupGetLootList)
    ```

___
