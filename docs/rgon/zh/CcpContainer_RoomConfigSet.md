---
tags:
  - Class
search:
  boost: 0.25
---
# Class "RoomConfigSet"

???+ info
    你可以通过以下函数获取此类:

    * [RoomConfigStage.GetRoomSet()](RoomConfigStage.md#getroomset)

    ???+ example "Example Code"

        ```lua
        local roomConfigSet = RoomConfig.GetStage(StbType.BASEMENT):GetRoomSet(0)`
        ```
## Operators

### __len () {: aria-label='Operators' }
[ ](#){: .abrep .tooltip .badge }
长度 (#) 操作。返回列表中实体的数量

___
## Functions
### AddRooms () {: aria-label='Functions' }
#### [RoomConfigRoom](RoomConfigRoom.md)[] AddRooms ( table[] Rooms ) {: .copyable aria-label='Functions' }

Adds the provided Lua Rooms to the RoomConfigSet. For details on how to generate Lua Rooms, refer to the [Custom StageAPI Github page](https://github.com/Meowlala/BOIStageAPI15/tree/master).

The function returns a table containing the placed RoomConfigRoom objects, in the same order as the input `Rooms` table. If a room at a given index could not be converted into a valid RoomConfigRoom, the corresponding entry in the returned table will be nil instead.

___
### Get () {: aria-label='Functions' }
[ ](#){: .abrep .tooltip .badge }
返回列表中指定索引处的 [RoomConfigRoom](https://wofsauge.github.io/IsaacDocs/rep/RoomConfig_Room.html)。

___
### Size {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .abrep .tooltip .badge }
#### const int Size  {: .copyable aria-label='Variables' }

列表中的实体数量.

___