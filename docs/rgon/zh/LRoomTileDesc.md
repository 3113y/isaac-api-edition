---
tags:
  - Class
---
# Class "LRoomTileDesc"

???+ info
    你可以通过以下函数获取此类：

    * [Room:GetLRoomTileDesc()](Room.md#getlroomtiledesc)

    ???+ example "Example Code"
        ```lua
        local TileDesc = Game():GetRoom():GetLRoomTileDesc()
        ```
        
## Functions

### GetHighBottomRight () {: aria-label='Functions' }
#### int[2] GetHighBottomRight ( ) {: .copyable aria-label='Functions' }
返回高半区右下角的网格坐标。

### GetHighTopLeft () {: aria-label='Functions' }
#### int[2] GetHighTopLeft ( ) {: .copyable aria-label='Functions' }
返回高半区左上角的网格坐标。

### GetLowBottomRight () {: aria-label='Functions' }
#### int[2] GetLowBottomRight ( ) {: .copyable aria-label='Functions' }
返回低半区右下角的网格坐标。

### GetLowTopLeft () {: aria-label='Functions' }
#### int[2] GetLowTopLeft ( ) {: .copyable aria-label='Functions' }
返回低半区左上角的网格坐标。

### GetRandomTile ( int Seed ) {: aria-label='Functions' }
#### int[2] GetRandomTile ( int Seed ) {: .copyable aria-label='Functions' }
返回此 L 形房间中随机图块的网格坐标。

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
