---
tags:
  - Class
---
> Documentation prose polished by a constrained language model; API facts and signatures retain their upstream source.

# Class "PocketItem"

???+ info
You can obtain this class through the following function:

    * [EntityPlayer:GetPocketItem()](EntityPlayer.md#getpocketitem)

    ???+ example "Example Code"
        ```lua
        local pocket = Isaac.GetPlayer(0):GetPocketItem(0)
        ```
## Functions

### GetSlot () {: aria-label='Functions' }
#### int GetSlot ( ) {: .copyable aria-label='Functions' }
Returns an identifying value for this pocket item; the value varies by PocketItemType.

Returns `0` if the pocket slot is empty.

For cards, returns [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html).

For pills, returns [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html).

For pocket active items, returns the corresponding [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html)**+1** (that is, `ActiveSlot.SLOT_POCKET + 1` or `ActiveSlot.SLOT_POCKET2 + 1`).

???+ example "Example code to obtain the [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) of the pocket active item in a given pocket slot:"
	```lua
	local pocketItem = player:GetPocketItem(PillCardSlot.PRIMARY)
	if pocketItem:GetType() == PocketItemType.ACTIVE_ITEM then
	  local activeSlot = pocketItem:GetSlot() - 1
	  local activeItemID = player:GetActiveItem(activeSlot)
	end
	```

___
### GetType () {: aria-label='Functions' }
#### [PocketItemType](enums/PocketItemType.md) GetType ( ) {: .copyable aria-label='Functions' }
Returns the [PocketItemType](enums/PocketItemType.md).

This value is unreliable when the slot is empty because the game sometimes fails to clear it.

___
