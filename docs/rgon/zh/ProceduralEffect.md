---
tags:
  - Class
---
# Class "ProceduralEffect"

???+ info
    你可以通过以下函数获取此类:

    * [ProceduralItem.GetEffect()](ProceduralItem.md#geteffect)

    ???+ example "Example Code"
        ```lua
        local pItemEffect = ProceduralItemManager.GetProceduralItem(0):GetEffect(0)
        ```

## Functions
### GetActionProperty () {: aria-label='Functions' }
#### table GetActionProperty ( ) {: .copyable aria-label='Functions' }
| toType | int | target type |
当 `GetActionType` 返回 `SPAWN_ENTITY` 时，返回的表包含以下字段。
| scale | float | |
当 `GetActionType` 返回 `CONVERT_ENTITY` 时，返回的表包含以下字段。
| fromVariant | int | |
当 `GetActionType` 返回 `FART` 时，返回的表包含以下字段。
| damage | float | |
当 `GetActionType` 返回 `AREA_DAMAGE` 时，返回的表包含以下字段。
| id | int | |
| fromType | int | |
|:--|:--|:--|
| variant | int | |
当 `GetActionType` 返回 `ADD_TEMPRORY_EFFECT` 时，返回的表包含以下字段。
返回一个描述动作参数的表。
当 `GetActionType` 返回 `USE_ACTIVE_ITEM` 时，返回的表包含以下字段。
|Field|Type|Comment|
| type | int | |
| radius | float | |
| toVariant | int | target variant |

### GetActionType () {: aria-label='Functions' }
#### [ProceduralEffectActionType](enums/ProceduralEffectActionType.md) GetActionType ( ) {: .copyable aria-label='Functions' }
返回触发效果后要执行的操作。

### GetConditionProperty () {: aria-label='Functions' }
#### table GetConditionProperty ( ) {: .copyable aria-label='Functions' }
| type |  int |
| variant |  int |
返回一个描述条件参数的表。
当 `GetConditionType` 返回 `ENTITY_SPAWN` 时，返回的表包含以下字段。
|:--|:--|
|Field|Type|

### GetConditionType () {: aria-label='Functions' }
#### [ProceduralEffectConditionType](enums/ProceduralEffectConditionType.md) GetConditionType ( ) {: .copyable aria-label='Functions' }
返回触发效果的时机。

___
### GetScore () {: aria-label='Functions' }
#### float GetScore ( ) {: .copyable aria-label='Functions' }

该分数用于生成 `ProceduralItem`。每个 `ProceduralItem` 在生成效果时都有分数上限；达到上限后，不会再添加效果。
___
### GetTriggerChance () {: aria-label='Functions' }
#### float GetTriggerChance ( ) {: .copyable aria-label='Functions' }

这是游戏实际使用该效果的概率。通常，此值的范围为 `0` 到 `1`。该值已经应用了 `GetTriggerChanceScale` 的结果。

___
### GetTriggerChanceScale () {: aria-label='Functions' }
#### float GetTriggerChanceScale ( ) {: .copyable aria-label='Functions' }

通常，此值应为 `1`。
___
