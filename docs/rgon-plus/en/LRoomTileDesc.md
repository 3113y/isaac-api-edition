---
tags:
  - Class
---
# Class "LRoomTileDesc"

???+ info
    You can obtain this class through the following function:

    * [Room:GetLRoomTileDesc()](Room.md#getlroomtiledesc)

    ???+ example "Example Code"
        ```lua
        local TileDesc = Game():GetRoom():GetLRoomTileDesc()
        ```
        
## Functions

### GetHighBottomRight () {: aria-label='Functions' }
#### int[2] GetHighBottomRight ( ) {: .copyable aria-label='Functions' }
Returns the grid coordinates of the bottom-right corner of the high half.

___
### GetHighTopLeft () {: aria-label='Functions' }
#### int[2] GetHighTopLeft ( ) {: .copyable aria-label='Functions' }
Returns the grid coordinates of the top-left corner of the high half.

___
### GetLowBottomRight () {: aria-label='Functions' }
#### int[2] GetLowBottomRight ( ) {: .copyable aria-label='Functions' }
Returns the grid coordinates of the bottom-right corner of the low half.

___
### GetLowTopLeft () {: aria-label='Functions' }
#### int[2] GetLowTopLeft ( ) {: .copyable aria-label='Functions' }
Returns the grid coordinates of the top-left corner of the low half.

___
### GetRandomTile ( int Seed ) {: aria-label='Functions' }
#### int[2] GetRandomTile ( int Seed ) {: .copyable aria-label='Functions' }
Returns the grid coordinates of a random tile in this L-shaped room.

___
