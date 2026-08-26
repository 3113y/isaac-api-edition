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
返回玩家收藏品对应的 [HistoryItems](HistoryItem.md) 表格。

___
### RemoveHistoryItemByIndex () {: aria-label='Functions' }
#### boolean RemoveHistoryItemByIndex ( int Index ) {: .copyable aria-label='Functions' }
从屏幕右侧的物品历史记录器中移除一个物品。请注意，这不会移除该物品对玩家的效果。
如果成功移除物品，则返回 `true`；否则返回 `false`。

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
