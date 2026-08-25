---
tags:
  - Class
---
# Class "EntityConfigEntity"

???+ info

    你可以通过以下函数获取此类:

    * [EntityConfig.GetEntity()](EntityConfig.md#getentity)

    ???+ example "Example Code"
    
        ```lua
        local gaperConfig = EntityConfig.GetEntity(EntityType.ENTITY_GAPER)
        ```
        
## Functions

### CanBeChampion () {: aria-label='Functions' }
#### boolean CanBeChampion ( ) {: .copyable aria-label='Functions' }

___
### CanBeRerolledInto () {: aria-label='Functions' }
#### boolean CanBeRerolledInto ( ) {: .copyable aria-label='Functions' }

___
### CanShutDoors () {: aria-label='Functions' }
#### boolean CanShutDoors ( ) {: .copyable aria-label='Functions' }

___
### GetAnm2Path () {: aria-label='Functions' }
#### string GetAnm2Path ( ) {: .copyable aria-label='Functions' }

___
### GetBaseHP () {: aria-label='Functions' }
#### float GetBaseHP ( ) {: .copyable aria-label='Functions' }

___
### GetBestiaryAnimation () {: aria-label='Functions' }
#### string GetBestiaryAnimation ( ) {: .copyable aria-label='Functions' }

___
### GetBestiaryAnm2Path () {: aria-label='Functions' }
#### string GetBestiaryAnm2Path ( ) {: .copyable aria-label='Functions' }

___
### GetBestiaryFloorAlt () {: aria-label='Functions' }
#### string GetBestiaryFloorAlt ( ) {: .copyable aria-label='Functions' }

___
### GetBestiaryOffset () {: aria-label='Functions' }
#### [const Vector](Vector.md) GetBestiaryOffset ( ) {: .copyable aria-label='Functions' }

___
### GetBestiaryOverlay () {: aria-label='Functions' }
#### string GetBestiaryOverlay ( ) {: .copyable aria-label='Functions' }

___
### GetBestiaryScale () {: aria-label='Functions' }
#### float GetBestiaryScale ( ) {: .copyable aria-label='Functions' }

___
### GetBossID () {: aria-label='Functions' }
#### [BossType](enums/BossType.md) GetBossID ( ) {: .copyable aria-label='Functions' }

___
### GetCollisionDamage () {: aria-label='Functions' }
#### float GetCollisionDamage ( ) {: .copyable aria-label='Functions' }

___
### GetCollisionInterval () {: aria-label='Functions' }
#### int GetCollisionInterval ( ) {: .copyable aria-label='Functions' }

___
### GetCollisionRadius () {: aria-label='Functions' }
#### float GetCollisionRadius ( ) {: .copyable aria-label='Functions' }
也称为 “大小”。

### GetCollisionRadiusMultiplier () {: aria-label='Functions' }
#### [const Vector](Vector.md) GetCollisionRadiusMultiplier ( ) {: .copyable aria-label='Functions' }
也称为 “大小乘数”。

### GetCustomTags () {: aria-label='Functions' }
#### table GetCustomTags ( ) {: .copyable aria-label='Functions' }
返回一个表格，其中包含实体在 [entities2.xml](xml/entities.md) 的 `customtags` 属性中指定的所有字符串。标签始终以全小写形式提供。有关 `customtags` 的更多信息，请参阅 [entities2.xml](xml/entities.md)。

___
### GetDevolvedEntity () {: aria-label='Functions' }
#### [EntityConfigEntity](EntityConfigEntity.md) GetDevolvedEntity ( ) {: .copyable aria-label='Functions' }
Returns the [EntityConfigEntity](EntityConfigEntity.md) that this entity would "devolve" into when D10 is used.

Returns nil if the entity has no devolution and would die instead.

___
### GetEntityTags () {: aria-label='Functions' }
#### int GetEntityTags ( ) {: .copyable aria-label='Functions' }
返回此实体的 [EntityTag](enums/EntityTag.md) 位掩码。

### GetFriction () {: aria-label='Functions' }
#### float GetFriction ( ) {: .copyable aria-label='Functions' }

___
### GetGibFlags () {: aria-label='Functions' }
#### int GetGibFlags ( ) {: .copyable aria-label='Functions' }
返回此实体的 [GibFlag](enums/GibFlag.md) 位掩码。

### GetGibsAmount () {: aria-label='Functions' }
#### int GetGibsAmount ( ) {: .copyable aria-label='Functions' }

___
### GetGridCollisionPoints () {: aria-label='Functions' }
#### int GetGridCollisionPoints ( ) {: .copyable aria-label='Functions' }

___
### GetMass () {: aria-label='Functions' }
#### float GetMass ( ) {: .copyable aria-label='Functions' }

___
### GetModName () {: aria-label='Functions' }
#### string GetModName ( ) {: .copyable aria-label='Functions' }
对于原版实体，返回 nil。
实体所属模组的名称字符串。

### GetName () {: aria-label='Functions' }
#### string GetName ( ) {: .copyable aria-label='Functions' }

___
### GetPortraitID () {: aria-label='Functions' }
#### int GetPortraitID ( ) {: .copyable aria-label='Functions' }

___
### GetShadowSize () {: aria-label='Functions' }
#### float GetShadowSize ( ) {: .copyable aria-label='Functions' }
请注意，此值是 XML 中指定的 “shadowSize” 除以 100 的结果。

### GetShieldStrength () {: aria-label='Functions' }
#### float GetShieldStrength ( ) {: .copyable aria-label='Functions' }
实体拥有的护甲值。

### GetStageHP () {: aria-label='Functions' }
#### float GetStageHP ( ) {: .copyable aria-label='Functions' }

___
### GetSubType () {: aria-label='Functions' }
#### int GetSubType ( ) {: .copyable aria-label='Functions' }

___
### GetType () {: aria-label='Functions' }
#### int GetType ( ) {: .copyable aria-label='Functions' }

___
### GetVariant () {: aria-label='Functions' }
#### int GetVariant ( ) {: .copyable aria-label='Functions' }

___
### HasCustomTag () {: aria-label='Functions' }
#### boolean HasCustomTag ( string tag ) {: .copyable aria-label='Functions' }
如果实体在 [entities2.xml](xml/entities.md) 的 `customtags` 属性中指定了提供的字符串，则返回 true。大小写无关紧要。有关 `customtags` 的更多信息，请参阅 [entities2.xml](xml/entities.md)。

### HasEntityTags () {: aria-label='Functions' }
#### boolean HasEntityTags ( int Tags ) {: .copyable aria-label='Functions' }
如果实体具有提供的位集中指定的所有 [EntityTag](enums/EntityTag.md)，则返回 true。

### HasFloorAlts () {: aria-label='Functions' }
#### boolean HasFloorAlts ( ) {: .copyable aria-label='Functions' }

___
### HasGibFlags () {: aria-label='Functions' }
#### boolean HasGibFlags ( int Flags ) {: .copyable aria-label='Functions' }
如果实体具有提供的位集中指定的所有 [GibFlag](enums/GibFlag.md)，则返回 true。### IsBoss () {: aria-label='Functions' }
#### boolean IsBoss ( ) {: .copyable aria-label='Functions' }

___

