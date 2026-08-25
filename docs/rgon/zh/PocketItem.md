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
For pills, returns [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html).
if pocketItem:GetType() == PocketItemType.ACTIVE_ITEM then
For pocket active items, returns the corresponding [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html)**+1** (so `ActiveSlot.SLOT_POCKET + 1` or `ActiveSlot.SLOT_POCKET2 + 1`).
Returns an identifying value for this pocket item. Varies depending on the PocketItemType.
local activeItemID = player:GetActiveItem(activeSlot)
end
Returns `0` if the pocket slot is empty.
For cards, returns [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html).
```lua
???+ example "Example code to obtain the [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) of the pocket active item in a given pocket slot:"
local activeSlot = pocketItem:GetSlot() - 1
```

### GetType () {: aria-label='Functions' }
#### [PocketItemType](enums/PocketItemType.md) GetType ( ) {: .copyable aria-label='Functions' }
This value is unreliable if the slot is currently empty, as the game sometimes does not clear it.
Returns the [PocketItemType](enums/PocketItemType.md).
