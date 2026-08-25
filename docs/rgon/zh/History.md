---
tags:
  - Class
---
# Class "History"

???+ info

    你可以通过以下函数获取此类:

    * [EntityPlayer:GetHistory()](EntityPlayer.md#gethistory)

    ???+ example "Example Code"

        ```lua
        local history = Isaac.GetPlayer(0):GetHistory()
        ```
        
## Functions

### GetCollectiblesHistory () {: aria-label='Functions' }
#### [HistoryItems](HistoryItem.md)[] GetCollectiblesHistory ( ) {: .copyable aria-label='Functions' }
返回收藏品[HistoryItems](HistoryItem.md)的表格.

___
### RemoveHistoryItemByIndex () {: aria-label='Functions' }
#### boolean RemoveHistoryItemByIndex ( int Index ) {: .copyable aria-label='Functions' }
从屏幕右侧的物品历史追踪器中移除一个物品。请注意，这不会从玩家身上移除该物品的效果。
如果物品被成功移除，返回`true`；否则，返回`false`.

___