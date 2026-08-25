---
tags:
  - Class
---
# Class "LRoomTileDesc"

???+ info
    你可以通过以下函数获取此类:

    * [Room:GetLRoomTileDesc()](Room.md#getlroomtiledesc)

    ???+ example "Example Code"
        ```lua
        local TileDesc = Game():GetRoom():GetLRoomTileDesc()
        ```
        
## Functions

### GetHighBottomRight () {: aria-label='Functions' }
#### int[2] GetHighBottomRight ( ) {: .copyable aria-label='Functions' }
Returns the grid coordinates of the high half's bottom right corner.

### GetHighTopLeft () {: aria-label='Functions' }
#### int[2] GetHighTopLeft ( ) {: .copyable aria-label='Functions' }
Returns the grid coordinates of the high half's top left corner.

### GetLowBottomRight () {: aria-label='Functions' }
#### int[2] GetLowBottomRight ( ) {: .copyable aria-label='Functions' }
Returns the grid coordinates of the low half's bottom right corner.

### GetLowTopLeft () {: aria-label='Functions' }
#### int[2] GetLowTopLeft ( ) {: .copyable aria-label='Functions' }
Returns the grid coordinates of the low half's top left corner.

### GetRandomTile ( int Seed ) {: aria-label='Functions' }
#### int[2] GetRandomTile ( int Seed ) {: .copyable aria-label='Functions' }
Returns the grid coordinates of a random tile in this L-room.

___
