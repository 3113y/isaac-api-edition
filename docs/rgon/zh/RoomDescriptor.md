---
tags:
  - Class
---
# Class "RoomDescriptor"

## Modified Variables

### AllowedDoors {: aria-label='Modified Variables' }
#### DoorSet AllowedDoors {: .copyable aria-label='Modified Variables' }
现在可以正确返回值。

返回一个位掩码，表示当前启用的门槽位。

通常只有当前实际存在门时，该门才会包含在此位掩码中，即使房间允许在该槽位设置门也是如此。

???+ example "Example"
    This tests if the DoorSlot `LEFT0` is enabled.
    ```lua
    if roomDesc.AllowedDoors & (1 << DoorSlot.LEFT0) ~= 0 then
        print("Room has a door in slot LEFT0")
    end
    ```

___

## Functions

### AddRestrictedGridIndex () {: aria-label='Functions' }
#### void AddRestrictedGridIndex ( int GridIndex ) {: .copyable aria-label='Functions' }

___
### GetDecoSaveState () {: aria-label='Functions' }
#### [EntitiesSaveStateVector](EntitiesSaveStateVector.md) GetDecoSaveState ( ) {: .copyable aria-label='Functions' }

___
### GetDimension () {: aria-label='Functions' }
#### [Dimension](https://wofsauge.github.io/IsaacDocs/rep/enums/Dimension.html) GetDimension ( ) {: .copyable aria-label='Functions' }
返回该房间所在的 [Dimension](enums/Dimension.md)。

### GetEntitiesSaveState () {: aria-label='Functions' }
#### [EntitiesSaveStateVector](EntitiesSaveStateVector.md) GetEntitiesSaveState ( ) {: .copyable aria-label='Functions' }

___
### GetGridEntitiesSaveState () {: aria-label='Functions' }
#### [GridEntitiesSaveStateVector](GridEntitiesSaveStateVector.md) GetGridEntitiesSaveState ( ) {: .copyable aria-label='Functions' }

___
### GetNeighboringRooms () {: aria-label='Functions' }
#### table GetNeighboringRooms ( ) {: .copyable aria-label='Functions' }
if roomType == RoomType.ROOM_SECRET or roomType == RoomType.ROOM_SUPERSECRET or roomType == RoomType.ROOM_ULTRASECRET then
return false
返回一个表，将 [DoorSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/DoorSlot.html) 映射到该房间当前所有邻居的 [RoomDescriptor](https://wofsauge.github.io/IsaacDocs/rep/RoomDescriptor.html)。
end
遍历此表时不要使用 `ipairs`，应使用 `pairs`！
```lua
local function HasSecretRoomNeighbor(roomDesc)
local roomType = neighborDesc.Data.Type
return true
-- Returns true if the room has a neighboring secret room.
for doorSlot, neighborDesc in pairs(roomDesc:GetNeighboringRooms()) do
???- example "Example Code"
```

### GetRestrictedGridIndexes () {: aria-label='Functions' }
#### int[] GetRestrictedGridIndexes ( ) {: .copyable aria-label='Functions' }

___
### GetTaintedKeeperCoinSpawns () {: aria-label='Functions' }
#### int GetTaintedKeeperCoinSpawns ( ) {: .copyable aria-label='Functions' }
当计数器达到 10 时，防止玩家重新进入房间时被击杀的敌人生成硬币。

___
### InitSeeds () {: aria-label='Functions' }
#### void InitSeeds ( [RNG](RNG.md) RNG ) {: .copyable aria-label='Functions' }

___
### SetTaintedKeeperCoinSpawns () {: aria-label='Functions' }
#### void SetTaintedKeeperCoinSpawns ( int Num ) {: .copyable aria-label='Functions' }

___

## Variables

### BossDeathSeed {: aria-label='Variables' }
#### const int BossDeathSeed {: .copyable aria-label='Variables' }

___
### Doors {: aria-label='Variables' }
#### const int[] Doors {: .copyable aria-label='Variables' }
用于检查房间中的每个 [DoorSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/DoorSlot.html) 连接到哪个关卡网格索引。

例如，`roomdesc.Doors[DoorSlot.UP0]` 会返回上方门所连接的关卡网格索引。

如果 [RoomShape](https://wofsauge.github.io/IsaacDocs/rep/enums/RoomShape.html) 不允许在该槽位设置门，则值为 `-1`。

请注意，即使当前没有门，或房间本身不允许在该槽位设置门，此属性通常仍会提供有效索引。

___
