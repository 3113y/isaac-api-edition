---
tags:
  - Class
---
# Class "ProceduralItem"

???+ info
    你可以通过以下函数获取此类:

    * [ProceduralItemManager.GetProceduralItem()](ProceduralItemManager.md#getproceduralitem)

    ???+ example "Example Code"
        ```lua
        local pItem = ProceduralItemManager.GetProceduralItem(0)
        ```

## Functions
### GetDamage () {: aria-label='Functions' }
#### float GetDamage ( ) {: .copyable aria-label='Functions' }

___
### GetEffect () {: aria-label='Functions' }
#### [ProceduralEffect](ProceduralEffect.md) GetEffect ( int Index ) {: .copyable aria-label='Functions' }

___
### GetEffectCount () {: aria-label='Functions' }
#### int GetEffectCount ( ) {: .copyable aria-label='Functions' }

___
### GetFireDelay () {: aria-label='Functions' }
#### float GetFireDelay ( ) {: .copyable aria-label='Functions' }

___
### GetID () {: aria-label='Functions' }
#### int GetID ( ) {: .copyable aria-label='Functions' }

___
### GetItem () {: aria-label='Functions' }
#### [ItemConfigItem](ItemConfig_Item.md) GetItem ( ) {: .copyable aria-label='Functions' }
Get the item config of the current glitched item.

### GetLuck () {: aria-label='Functions' }
#### float GetLuck ( ) {: .copyable aria-label='Functions' }

___
### GetRange () {: aria-label='Functions' }
#### float GetRange ( ) {: .copyable aria-label='Functions' }

___
### GetShotSpeed () {: aria-label='Functions' }
#### float GetShotSpeed ( ) {: .copyable aria-label='Functions' }

___
### GetSpeed () {: aria-label='Functions' }
#### float GetSpeed ( ) {: .copyable aria-label='Functions' }

___
### GetTargetItem () {: aria-label='Functions' }
#### [ItemConfigItem](ItemConfig_Item.md) GetTargetItem ( ) {: .copyable aria-label='Functions' }
Returns the item config that was randomly selected by the current glitched item, or `nil` if it doesn't exist.
