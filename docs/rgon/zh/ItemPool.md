---
tags:
  - Class
---
# Class "ItemPool"

## Modified Functions

### GetCollectible () {: aria-label='Modified Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetCollectible ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType, boolean Decrease = false, int Seed = Random(), [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) DefaultItem = CollectibleType.COLLECTIBLE_NULL, [GetCollectibleFlag](enums/GetCollectibleFlag.md) Flags = 0 ) {: .copyable aria-label='Modified Functions' }
???+ warning "Setting both Ban Flags"
现在可以使用 `Flags` 参数。
同时设置 `BAN_ACTIVE` 和 `BAN_PASSIVE` 标志时，函数始终返回 `DefaultItem` 或 `CollectibleType.COLLECTIBLE_BREAKFAST`。

### AddBibleUpgrade () {: aria-label='Functions' }
#### void AddBibleUpgrade ( int Add, [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType ) {: .copyable aria-label='Functions' }

___
### AddCollectible () {: aria-label='Functions' }
#### void AddCollectible ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType, table | table[] PoolItems ) {: .copyable aria-label='Functions' }

将提供的 Lua PoolItem 对象永久添加到指定池中，效果与在 `itempools.xml` 文件中定义它们相同。

`PoolItems` 参数可以是单个 Lua PoolItem 对象，也可以是由多个对象组成的数组。

???- info "Lua PoolItem format"
    |Field|Type|Comment|
    |:--|:--|:--|
    | itemID | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | `Default = COLLECTIBLE_NULL` |
    | name | string | `Optional`<br /> Alternative to `itemID` |
    | weight | float | `Default = 1.0` |
    | decreaseBy | float | `Default = 0.5` |
    | removeOn | float | `Default = 0.1` |

    All field names are case insensitive

___
### AddTemporaryCollectible () {: aria-label='Functions' }
#### void AddTemporaryCollectible ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType, table | table[] PoolItems ) {: .copyable aria-label='Functions' }

将提供的 Lua PoolItem 对象添加到指定池中，但仅在当前游戏运行期间有效。

The `PoolItems` parameter can be either a single Lua PoolItem object or an array of them.

???- info "Lua PoolItem format"
    |Field|Type|Comment|
    |:--|:--|:--|
    | itemID | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | `Default = COLLECTIBLE_NULL` |
    | name | string | `Optional`<br /> Alternative to `itemID` |
    | weight | float | `Default = 1.0` |
    | decreaseBy | float | `Default = 0.5` |
    | removeOn | float | `Default = 0.1` |

    All field names are case insensitive

???- info "Temporary Collectible behavior"
    临时收藏品会在继续或退出游戏运行时自动添加和移除；使用闪耀沙漏返回先前状态时，也会根据该状态是否包含该收藏品自动处理。

___
### CanSpawnCollectible () {: aria-label='Functions' }
#### boolean CanSpawnCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, boolean ignoreLocked ) {: .copyable aria-label='Functions' }
???+ info "IgnoreLocked"
If `IgnoreLocked` is set to true, this function will return true for items that could appear but are locked behind achievements.
It will still return false if the item was removed from the item pool or if it can't appear because other effects (Tainted Lost offensive items mechanic or NO! trinket effect).

### GetBibleUpgrades () {: aria-label='Functions' }
#### int GetBibleUpgrades ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType ) {: .copyable aria-label='Functions' }
返回添加到池中的圣经类收藏品数量。

### GetCardEx () {: aria-label='Functions' }
#### [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html) GetCardEx ( int Seed, int SpecialChance, int RuneChance, int SuitChance, boolean AllowNonCards ) {: .copyable aria-label='Functions' }
[ItemPool:GetCard()](https://wofsauge.github.io/IsaacDocs/rep/ItemPool.html#getcard) 的增强版本，可分别定义各项概率。

### GetCollectibleFromList () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetCollectibleFromList ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)[] ItemList, int Seed = Random(), [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) DefaultItem = CollectibleType.COLLECTIBLE_BREAKFAST, boolean AddToBlacklist = true, boolean ExcludeActiveItems = false ) {: .copyable aria-label='Functions' }

___
### GetCollectiblesFromPool () {: aria-label='Functions' }
#### table GetCollectiblesFromPool ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType ) {: .copyable aria-label='Functions' }
| initialWeight | float | |
|:--|:--|:--|
| isUnlocked | boolean | |
Returns a table of collectibles registered in the specified pool. The table contains the following fields
|Field|Type|Comment|
| weight | float | |
| removeOn | float | |
| decreaseBy | float | |
| itemID | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | |

### GetNumAvailableTrinkets () {: aria-label='Functions' }
#### int GetNumAvailableTrinkets ( ) {: .copyable aria-label='Functions' }
返回物品池中可用饰品的数量。

### GetNumItemPools () {: aria-label='Functions' }
#### int GetNumItemPools ( ) {: .copyable aria-label='Functions' }
返回游戏中的物品池总数，包括自定义物品池。

### GetPillColor () {: aria-label='Functions' }
#### [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) GetPillColor ( [PillEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/PillEffect.html) ID ) {: .copyable aria-label='Functions' }
目前不会受 PHD、False PHD 等药丸修改效果影响。
返回与指定 `PillEffect` 匹配的 PillColor；如果该效果不在轮换列表中，则返回 -1。

### GetRandomPool () {: aria-label='Functions' }
#### [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) GetRandomPool ( [RNG](RNG.md) RNG, boolean AdvancedSearch = false, [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html)[] Filter = {}, boolean IsWhitelist = false) {: .copyable aria-label='Functions' }
以与 Chaos 相同的方式随机选择一个池：包含更多物品的池比包含较少物品的池拥有更高的选中概率。

默认情况下，此函数遵循与 Chaos 相同的规则，只能返回当前模式的池；将 `Advanced Search` 设为 true 可绕过这些限制。

???+ info "Advanced Search"
    Setting `Advanced Search` to true allows you to make use of the `Filter` parameter.

    默认情况下，`Filter` 是要排除的物品池黑名单；将 `IsWhitelist` 设为 true 后，它会变为可供选择的物品池列表。

???+ example "Pick Pool From List"
    This code picks a random pool from any of the "Beggar" pools

    ```lua
    local PoolList = {
        ItemPoolType.POOL_BEGGAR,
        ItemPoolType.POOL_DEMON_BEGGAR,
        ItemPoolType.POOL_KEY_MASTER,
        ItemPoolType.POOL_BATTERY_BUM,
        ItemPoolType.POOL_BOMB_BUM,
        ItemPoolType.POOL_ROTTEN_BEGGAR
    }

    local rng = RNG() -- replace this with your own rng
    local randomPool = Game():GetItemPool():GetRandomPool(rng, true, PoolList, true)
    ```

???+ example "Pick Pool From Vanilla"
    This code picks a random pool from any of the vanilla

    ```lua
    local itemPool = Game():GetItemPool()

    local CustomPools = {}

    -- Put all custom pools within the Filter
    for i = 31, itemPool:GetNumItemPools() - 1 do
        table.insert(CustomPools, i)
    end

    local rng = RNG(Random()) -- replace this with your own rng
    local randomPool = Game():GetItemPool():GetRandomPool(rng, true, CustomPools, false)
    ```

### GetRemovedCollectibles () {: aria-label='Functions' }
#### table GetRemovedCollectibles ( ) {: .copyable aria-label='Functions' }
local removedCollectibles = itemPool:GetRemovedCollectibles()
返回从所有池中移除的[收藏品](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)表。
if removedCollectibles[CollectibleType.COLLECTIBLE_SAD_ONION] then
end
```lua
```
print("Sad onion removed!")
???- example "Example Code"
This code checks if the sad onion has been removed.

### GetRoomBlacklistedCollectibles () {: aria-label='Functions' }
#### table GetRoomBlacklistedCollectibles ( ) {: .copyable aria-label='Functions' }
print("Sad onion blacklisted!")
返回当前房间中被列入黑名单的[收藏品](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)表。
local blacklistedCollectibles = itemPool:GetRoomBlacklistedCollectibles()
end
```lua
```
???- example "Example Code"
This code checks if the sad onion has been removed.
if blacklistedCollectibles[CollectibleType.COLLECTIBLE_SAD_ONION] then

### HasCollectible () {: aria-label='Functions' }
#### boolean HasCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) {: .copyable aria-label='Functions' }
如果收藏品在物品池中可用，则返回 `true`；否则返回 `false`。

### HasTrinket () {: aria-label='Functions' }
#### boolean HasTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket ) {: .copyable aria-label='Functions' }
如果饰品当前在饰品池中可用，则返回 `true`；否则返回 `false`。

### PickCollectible () {: aria-label='Functions' }
#### table PickCollectible ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType, boolean Decrease = false, [RNG](RNG.md) RNG = RNG(), [GetCollectibleFlag](enums/GetCollectibleFlag.md) Flags = 0 ) {: .copyable aria-label='Functions' }
| initialWeight | float | |
| weight | float | |
| decreaseBy | float | |
| removeOn | float | |
| isUnlocked | boolean | |

???+ info "Differences with GetCollectible"
    For reference GetCollectible() **Gives Up** after either this function has failed to pick an Unlocked collectible 20 times in a row or has failed to produce any result at all (nil).
    
    - Does not generate a [Glitched Item](ProceduralItem.md) when having the `CollectibleType.COLLECTIBLE_TMTRAINER` effect.
    
    - Does not randomize the pool when having the `CollectibleType.COLLECTIBLE_CHAOS` effect.
    
    - Does not attempt to get a collectible from `ItemPoolType.POOL_TREASURE` if **Giving up**.
    
    - Does not morph the collectible into `CollectibleType.COLLECTIBLE_BREAKFAST` if **Giving up**.
    
    - Does not attempt to morph the collectible into `CollectibleType.COLLECTIBLE_BIBLE`, `CollectibleType.COLLECTIBLE_MAGIC_SKIN` or `CollectibleType.COLLECTIBLE_ROSARY`
    
    - Does not trigger the [MC_PRE_GET_COLLECTIBLE](https://wofsauge.github.io/IsaacDocs/rep/enums/ModCallbacks.html?h=modcall#mc_post_get_collectible) and [MC_POST_GET_COLLECTIBLE](https://wofsauge.github.io/IsaacDocs/rep/enums/ModCallbacks.html?h=modcall#mc_post_get_collectible) callback.

___
### RemoveTemporaryCollectible () {: aria-label='Functions' }
#### void RemoveTemporaryCollectible ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType, table | table[] PoolItems ) {: .copyable aria-label='Functions' }

Removes the provided Temporary Collectibles from the specified Pool, assuming they exist.

The PoolItem object **MUST** be equal (in terms of field values) to the one that was added in [AddTemporaryCollectible](ItemPool.md#addtemporarycollectible)

The `PoolItems` parameter can be either a single Lua PoolItem object or an array of them.

???- info "Lua PoolItem format"
    |Field|Type|Comment|
    |:--|:--|:--|
    | itemID | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | `Default = COLLECTIBLE_NULL` |
    | name | string | `Optional`<br /> Alternative to `itemID` |
    | weight | float | `Default = 1.0` |
    | decreaseBy | float | `Default = 0.5` |
    | removeOn | float | `Default = 0.1` |

    All field names are case insensitive

### ResetCollectible () {: aria-label='Functions' }
#### void ResetCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) {: .copyable aria-label='Functions' }
使收藏品重新可用，即使它先前被移除，也能自然生成；同时将该收藏品在每个物品池中的所有实例恢复为其 **initialWeight**。

### SetLastPool () {: aria-label='Functions' }
#### void SetLastPool ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) ) {: .copyable aria-label='Functions' }

___
### UnidentifyPill () {: aria-label='Functions' }
#### void UnidentifyPill ( [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) Pill ) {: .copyable aria-label='Functions' }
将药丸重置为未识别（???）状态。
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
