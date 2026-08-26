---
tags:
  - Class
search:
  boost: 0.25
---
> Documentation prose polished by a constrained language model; API facts and signatures retain their upstream source.

# Class "RoomConfigSet"

???+ info
    You can get this class by using the following function:

    * [RoomConfigStage.GetRoomSet()](RoomConfigStage.md#getroomset)

    ???+ example "Example Code"
        `local roomConfigSet = RoomConfig.GetStage(StbType.BASEMENT):GetRoomSet(0)`

## Operators
### __len () {: aria-label='Operators' }
[ ](#){: .abrep .tooltip .badge }
#### int __len ( ) {: .copyable aria-label='Operators' }

The length (#) operation. Returns the number of entities in the list.

___
## Functions
### AddRooms () {: aria-label='Functions' }
#### [RoomConfigRoom](RoomConfigRoom.md)[] AddRooms ( table[] Rooms ) {: .copyable aria-label='Functions' }

Adds the provided Lua rooms to the RoomConfigSet. For details on generating Lua rooms, refer to the [Custom StageAPI GitHub page](https://github.com/Meowlala/BOIStageAPI15/tree/master).

The function returns a table containing the placed RoomConfigRoom objects, in the same order as the input `Rooms` table. If a room at a given index could not be converted into a valid RoomConfigRoom, the corresponding entry in the returned table will be nil instead.

___
### Get () {: aria-label='Functions' }
[ ](#){: .abrep .tooltip .badge }
#### [RoomConfigRoom](RoomConfigRoom.md) Get ( int idx ) {: .copyable aria-label='Functions' }

Returns a [RoomConfigRoom](https://wofsauge.github.io/IsaacDocs/rep/RoomConfig_Room.html) at the specified index in the list.

___
### LoadStb () {: aria-label='Functions' }
#### [RoomConfigRoom](RoomConfigRoom.md)[] LoadStb ( string StbFileName ) {: .copyable aria-label='Functions' }

Adds the rooms from the provided `.stb` file to the RoomConfigSet. Files can only be loaded starting from the `.../content(-repentogon)/rooms/` folder of all mods (so you should not include `content/rooms/` in your path).

If files from multiple mods match the filename, they will all be loaded.

___
## Variables
### Size {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .abrep .tooltip .badge }
#### const int Size  {: .copyable aria-label='Variables' }

The number of entities in the list.

___
