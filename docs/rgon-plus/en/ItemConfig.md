---
tags:
  - Class
---
# Class "ItemConfig"

## Functions

### CanRerollCollectible () {: aria-label='Functions' }
#### boolean CanRerollCollectible ( int ID ) {: .copyable aria-label='Functions' }
Returns `true` if the collectible can be rerolled.

???- bug "Bug"
    Although this is not a static function, it must be called using `.`, as in `Isaac.GetItemConfig().CanRerollCollectible(1)`.

___    
### GetTaggedItems () {: aria-label='Functions' }
#### [ItemConfig_Item](ItemConfig_Item.md)[] GetTaggedItems ( int Tags ) {: .copyable aria-label='Functions' }
Returns a table of [ItemConfig_Item](ItemConfig_Item.md) objects with the specified tags.

___
### IsValidTrinket () {: aria-label='Functions' }
#### boolean IsValidTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) TrinketType ) {: .copyable aria-label='Functions' }

