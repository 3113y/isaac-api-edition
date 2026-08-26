---
tags:
  - Class
---
> Documentation prose polished by a constrained language model; API facts and signatures retain their upstream source.

# Class "Pathfinder"

???+ info
    You can obtain this class through the following functions:
	
	* [EntityFamiliar:GetPathfinder()](EntityFamiliar.md#getpathfinder)
    * [EntityNPC:GetPathfinder()](EntityNPC.md#getpathfinder)

    ???+ example "Example code"
        ```lua
        local pathfinder = npc:GetPathfinder()
        ```

???+ warning "Warning"
	The following functions are affected only when using the new `GetPathfinder` method. `EntityNPC.Pathfinder` retains its old behavior for compatibility with existing mods.
___
## Modified Functions

### Find·Grid·Path () {: aria-label='Functions' }
[ ](#){: .tooltip .badge }
#### void FindGridPath ( [Vector](Vector.md) Pos, float Speed, int PathMarker, boolean UseDirectPath ) {: .copyable aria-label='Functions' }
`UseDirectPath` now works as intended: it moves directly toward the target when no grids obstruct the path.

___
### Move·Randomly () {: aria-label='Functions' }
[ ](#){: .tooltip .badge }
#### boolean MoveRandomly ( boolean IgnoreStatusEffects ) {: .copyable aria-label='Functions' }
This now works as intended. After calling it, use [Entity:MultiplyFriction](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#multiplyfriction) with a value below 1; otherwise, the entity will accelerate continuously.

___
### Move·Randomly·Axis·Aligned () {: aria-label='Functions' }
[ ](#){: .tooltip .badge }
#### void MoveRandomlyAxisAligned ( float Speed, boolean IgnoreStatusEffects ) {: .copyable aria-label='Functions' }
This now works as intended. After calling it, use [Entity:MultiplyFriction](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#multiplyfriction) with a value below 1; otherwise, the entity will accelerate continuously.

___
### Move·Randomly·Boss () {: aria-label='Functions' }
[ ](#){: .tooltip .badge }
#### void MoveRandomlyBoss ( boolean IgnoreStatusEffects ) {: .copyable aria-label='Functions' }
This now works as intended. After calling it, use [Entity:MultiplyFriction](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#multiplyfriction) with a value below 1; otherwise, the entity will accelerate continuously.

___
