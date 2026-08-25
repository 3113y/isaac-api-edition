---
tags:
  - Class
---
# Class "Room"
## Modified Functions

### GetBackdropType () {: aria-label='Modified Functions' }
#### [BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html) GetBackdropType ( ) {: .copyable aria-label='Modified Functions' }

___
### GetLRoomAreaDesc () {: aria-label='Modified Functions' }
#### [LRoomAreaDesc](LRoomAreaDesc.md) GetLRoomAreaDesc ( ) {: .copyable aria-label='Modified Functions' }
Now returns a usable class. Describes the corners of an L-room shape (as divided horizontally into two rectangles), in worldspace.

### GetLRoomTileDesc () {: aria-label='Modified Functions' }
#### [LRoomTileDesc](LRoomTileDesc.md) GetLRoomTileDesc ( ) {: .copyable aria-label='Modified Functions' }
Now returns a usable class. Describes the corners of an L-room shape (as divided horizontally into two rectangles), in grid coordinates.

### SpawnGridEntity () {: aria-label='Modified Functions' }
#### boolean SpawnGridEntity ( int GridIndex, [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) Type, int Variant = 0, int Seed = nil, int VarData = 0 ) {: .copyable aria-label='Modified Functions' }
No longer crashes if an invalid `GridIndex` is used. All arguments beyond `Type` are optional. An overload has been added to allow spawning a new grid entity using an existing `GridEntityDesc`.

### TrySpawnSpecialQuestDoor () {: aria-label='Modified Functions' }
#### boolean TrySpawnSpecialQuestDoor ( boolean IgnoreStageType = false ) {: .copyable aria-label='Modified Functions' }
An `IgnoreStageType` parameter has been added to allow spawning the Mirror & Mineshaft door outside of `STAGETYPE_REPENTANCE` and `STAGETYPE_REPENTANCE_B` stages. Note that the `KNIFE_PUZZLE` [dimension](Level.md?#dimension-getdimension) must be set up properly for these doors not to crash on entry!

### CanPickupGridEntity () {: aria-label='Functions' }
#### boolean CanPickupGridEntity ( int GridIndex ) {: .copyable aria-label='Functions' }
Returns true if the gridentity at the given position can be picked up.

### CanSpawnObstacleAtPosition () {: aria-label='Functions' }
#### boolean CanSpawnObstacleAtPosition ( int GridIndex, boolean Force ) {: .copyable aria-label='Functions' }

___
### ClearBossHazards () {: aria-label='Functions' }
#### void ClearBossHazards ( boolean IgnoreNPCs = true, [Entity](Entity.md) Source = nil ) {: .copyable aria-label='Functions' }
Kills all projectiles. Kills all non-friendly NPCs capable of keeping doors closed as well if `IgnoreNPCs` is false.

___
### DoLightningStrike () {: aria-label='Functions' }
#### void DoLightningStrike ( int Seed = RandomSeed ) {: .copyable aria-label='Functions' }
Creates a lightning effect as seen in Downpour. `Seed` determines [intensity](Room.md#getlightningintensity) (`1.3 + RandomFloat()*.6`) and sound pitch (`0.9 + RandomFloat()*0.2`).

### GetBackdrop () {: aria-label='Functions' }
#### [Backdrop](Backdrop.md) GetBackdrop ( ) {: .copyable aria-label='Functions' }
Returns a [Backdrop](Backdrop.md) object.

### GetBossVictoryJingle () {: aria-label='Functions' }
#### [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) GetBossVictoryJingle ( ) {: .copyable aria-label='Functions' }

___
### GetCamera () {: aria-label='Functions' }
#### [Camera](Camera.md) GetCamera ( ) {: .copyable aria-label='Functions' }
Returns a [Camera](Camera.md) object.

### GetChampionBossChance () {: aria-label='Functions' }
#### float GetChampionBossChance ( ) {: .copyable aria-label='Functions' }
Return the probability that boss spawns in this room will be champions.

### GetEffects () {: aria-label='Functions' }
#### [TemporaryEffects](https://wofsauge.github.io/IsaacDocs/rep/TemporaryEffects.html) GetEffects ( ) {: .copyable aria-label='Functions' }

___
### GetFloorColor () {: aria-label='Functions' }
#### [Color](Color.md) GetFloorColor ( ) {: .copyable aria-label='Functions' }

___
### GetFXLayers () {: aria-label='Functions' }
#### [FXLayers](FXLayers.md) GetFXLayers ( ) {: .copyable aria-label='Functions' }

___
### GetFXParams () {: aria-label='Functions' }
#### [FXParams](FXParams.md) GetFXParams ( ) {: .copyable aria-label='Functions' }

___
### GetGreedWaveTimer () {: aria-label='Functions' }
#### int GetGreedWaveTimer ( ) {: .copyable aria-label='Functions' }

___
### GetGridIndexByTile () {: aria-label='Functions' }
#### int GetGridIndexByTile ( int GridRow, int GridColumn ) {: .copyable aria-label='Functions' }
#### int GetGridIndexByTile ( int[2] Tile ) {: .copyable aria-label='Functions' }

___
### GetItemPool () {: aria-label='Functions' }
#### [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType GetItemPool ( int Seed = Random(), boolean Raw = false ) {: .copyable aria-label='Functions' }
Retrieves the [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) the game would use to generate random collectibles in the current room. Unlike [ItemPool.GetPoolForRoom()](https://wofsauge.github.io/IsaacDocs/rep/ItemPool.html#getpoolforroom), this takes into account the pool set using [SetItemPool()](Room.md#setitempool), and runs the game's pool selection code, which handles unique cases (ex. Boss Room + Used Satanic Bible = Devil Pool).

### GetLightningIntensity () {: aria-label='Functions' }
#### float GetLightningIntensity ( ) {: .copyable aria-label='Functions' }
This is set by the game in a random range between `1.3` and `2.1`, and decays by `value * .75` per render.
Gets the intensity of the lightning effect used in Downpour. This variable will affect the visibility of Wraiths.

### GetNumRainSpawners () {: aria-label='Functions' }
#### int GetNumRainSpawners ( ) {: .copyable aria-label='Functions' }
???+ info
There's more to this than just the number of them, but I'm having trouble identifying how this works.
The number of areas in a room that spawn rain effects in a tight radius.

### GetRail () {: aria-label='Functions' }
#### [StbRailVariant](enums/StbRailVariant.md) GetRail ( int GridIndex ) {: .copyable aria-label='Functions' }

___
### GetRailManager () {: aria-label='Functions' }
#### [RailManager](RailManager.md) GetRailManager ( ) {: .copyable aria-label='Functions' }

___
### GetRainIntensity () {: aria-label='Functions' }
#### float GetRainIntensity ( ) {: .copyable aria-label='Functions' }
Used by the positional rain effect spawners in Downpour. No noticable effect beyond `1.0`.

### GetRoomClearDelay () {: aria-label='Functions' }
#### int GetRoomClearDelay ( ) {: .copyable aria-label='Functions' }

___
### GetShopItemPrice () {: aria-label='Functions' }
#### int GetShopItemPrice ( int EntityVariant, int EntitySubType, int ShopItemID ) {: .copyable aria-label='Functions' }
Returns the price of the item.

The game typically uses `1` or `-1` for its values depending on current strength and direction. You can technically go higher than this for some interesting results. Arbitrary directions are fully supported as well.

`Vector(0, 0)` will remove the current.
___
### TriggerOutput () {: aria-label='Functions' }
#### void TriggerOutput ( [RoomEventOutput](enums/RoomEventOutput.md) GroupIdx) {: .copyable aria-label='Functions' }

___
### TriggerRestock () {: aria-label='Functions' }
#### void TriggerRestock ( int GridIndex, int ShopItemIdx) {: .copyable aria-label='Functions' }
Sets up the shop item to be spawned with an increased price upon the next call of ShopRestockPartial.

___
### TryGetShopDiscount () {: aria-label='Functions' }
#### int TryGetShopDiscount ( int ShopItemIdx, int Price ) {: .copyable aria-label='Functions' }

___
### UpdateColorModifier () {: aria-label='Functions' }
#### void UpdateColorModifier ( boolean Process = true, boolean Lerp = true, float Rate = 0.015 ) {: .copyable aria-label='Functions' }
`Process` runs the color correction through some additional modifications for lava and the abandoned mineshaft sequence.
Updates the room's color correction with the copy of [ColorModifier](ColorModifier.md) stored in [FXParams](FXParams.md).
