---
tags:
  - Class
---
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
# Class "Pathfinder"

???+ info
    可通过以下函数获取此类：
	
	* [EntityFamiliar:GetPathfinder()](EntityFamiliar.md#getpathfinder)
    * [EntityNPC:GetPathfinder()](EntityNPC.md#getpathfinder)

    ???+ example "示例代码"
        ```lua
        local pathfinder = npc:GetPathfinder()
        ```

???+ warning "警告"
	以下函数仅在使用新的 `GetPathfinder` 方法时受影响！为兼容现有模组，`EntityNPC.Pathfinder` 仍保留旧行为。
___
## Modified Functions

### Find·Grid·Path () {: aria-label='Functions' }
[ ](#){: .tooltip .badge }
#### void FindGridPath ( [Vector](Vector.md) Pos, float Speed, int PathMarker, boolean UseDirectPath ) {: .copyable aria-label='Functions' }
`UseDirectPath` 现在按预期工作（目标路径未被网格阻挡时会直接向目标移动）。

___
### Move·Randomly () {: aria-label='Functions' }
[ ](#){: .tooltip .badge }
#### boolean MoveRandomly ( boolean IgnoreStatusEffects ) {: .copyable aria-label='Functions' }
现在按预期工作。调用此函数后，请确保使用小于 1 的值调用 [Entity:MultiplyFriction](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#multiplyfriction)，否则实体会持续加速。

___
### Move·Randomly·Axis·Aligned () {: aria-label='Functions' }
[ ](#){: .tooltip .badge }
#### void MoveRandomlyAxisAligned ( float Speed, boolean IgnoreStatusEffects ) {: .copyable aria-label='Functions' }
现在按预期工作。调用此函数后，请确保使用小于 1 的值调用 [Entity:MultiplyFriction](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#multiplyfriction)，否则实体会持续加速。

___
### Move·Randomly·Boss () {: aria-label='Functions' }
[ ](#){: .tooltip .badge }
#### void MoveRandomlyBoss ( boolean IgnoreStatusEffects ) {: .copyable aria-label='Functions' }
现在按预期工作。调用此函数后，请确保使用小于 1 的值调用 [Entity:MultiplyFriction](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#multiplyfriction)，否则实体会持续加速。

___
