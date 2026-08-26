---
tags:
  - Class
---
# Class "PocketItem"

???+ info
    你可以通过以下函数获取此类:

    * [EntityPlayer:GetPocketItem()](EntityPlayer.md#getpocketitem)

    ???+ example "Example Code"
        ```lua
        local pocket = Isaac.GetPlayer(0):GetPocketItem(0)
        ```
## Functions

### GetSlot () {: aria-label='Functions' }
#### int GetSlot ( ) {: .copyable aria-label='Functions' }
local pocketItem = player:GetPocketItem(PillCardSlot.PRIMARY)
对于药丸，返回 [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html)。
if pocketItem:GetType() == PocketItemType.ACTIVE_ITEM then
对于口袋主动道具，返回对应的 [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html)**+1**（即 `ActiveSlot.SLOT_POCKET + 1` 或 `ActiveSlot.SLOT_POCKET2 + 1`）。
返回此口袋道具的标识值，具体取决于 PocketItemType。
local activeItemID = player:GetActiveItem(activeSlot)
end
如果口袋栏位为空，则返回 `0`。
对于卡牌，返回 [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html)。
```lua
???+ example "Example code to obtain the [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) of the pocket active item in a given pocket slot:"
local activeSlot = pocketItem:GetSlot() - 1
```

### GetType () {: aria-label='Functions' }
#### [PocketItemType](enums/PocketItemType.md) GetType ( ) {: .copyable aria-label='Functions' }
如果栏位当前为空，此值可能不可靠，因为游戏有时不会将其清零。
返回 [PocketItemType](enums/PocketItemType.md)。
