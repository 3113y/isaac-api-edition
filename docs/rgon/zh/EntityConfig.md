---
tags:
  - Global
  - Class
---
# Global Class "EntityConfig"

???+ info
    These functions can be accessed via the `EntityConfig` global table.

    **注意：调用这些函数时，必须使用 .（句点）而非 :（冒号）！**

    ???+ example "Example Code"
    
        ```lua
        local gaperConfig = EntityConfig.GetEntity(EntityType.ENTITY_GAPER)
        ```
        
## Functions

### GetBaby () {: aria-label='Functions' }
#### [EntityConfigBaby](EntityConfigBaby.md) GetBaby ( [BabySubType](https://wofsauge.github.io/IsaacDocs/rep/enums/BabySubType.html) Type ) {: .copyable aria-label='Functions' }
如果不存在具有指定 ID 的合作宝宝，则返回 nil。

___
### GetEntity () {: aria-label='Functions' }
#### [EntityConfigEntity](EntityConfigEntity.md) GetEntity ( [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) Type, int Variant = -1, int SubType = -1 ) {: .copyable aria-label='Functions' }
如果不存在具有指定类型的实体，则返回 nil。
提供变体（Variant）和/或子类型（SubType）是可选的。如果请求了不存在的变体/子类型，则返回该实体的基础版本。

___
### GetMaxBabyID () {: aria-label='Functions' }
#### int GetMaxBabyID ( ) {: .copyable aria-label='Functions' }
返回当前分配给有效合作宝宝的最高 ID（对应子类型）。

___
### GetMaxPlayerType () {: aria-label='Functions' }
#### int GetMaxPlayerType ( ) {: .copyable aria-label='Functions' }
返回当前分配给有效角色的最高玩家类型（PlayerType）。

___
### GetPlayer () {: aria-label='Functions' }
#### [EntityConfigPlayer](EntityConfigPlayer.md) GetPlayer ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) PlayerType ) {: .copyable aria-label='Functions' }
如果不存在具有指定玩家类型的角色，则返回 nil。

___