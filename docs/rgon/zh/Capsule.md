---
tags:
  - Class
---
# Class "Capsule"

[here.](./examples/Capsules.md)可以找到一个使用Capsule类的示例模组

???+ info

    你可以通过以下函数获取此类:
    * [Entity:GetCollisionCapsule()](Entity.md#getcollisioncapsule)
    * [Entity:GetNullCapsule()](Entity.md#getnullcapsule)
        
## Constructors
### Capsule () {: aria-label='Constructors' }
#### [Capsule](Capsule.md) Capsule ( [Vector](Vector.md) Position, [Vector](Vector.md) SizeMult, float Rotation, float Size ) {: .copyable aria-label='Constructors' }
## Functions

### Collide () {: aria-label='Functions' }
#### boolean Collide ( [Capsule](Capsule.md) Capsule, [Vector](Vector.md) Point ) {: .copyable aria-label='Functions' }

___
### GetDirection () {: aria-label='Functions' }
#### [Vector](Vector.md) GetDirection ( ) {: .copyable aria-label='Functions' }

___
### GetF1 () {: aria-label='Functions' }
#### float GetF1 ( ) {: .copyable aria-label='Functions' }
返回胶囊体的大小（与两个构造函数中的 `size` 一致）
### GetF2 () {: aria-label='Functions' }
#### float GetF2 ( ) {: .copyable aria-label='Functions' }

___
### GetPosition () {: aria-label='Functions' }
#### [Vector](Vector.md) GetPosition ( ) {: .copyable aria-label='Functions' }

___
### GetVec2 () {: aria-label='Functions' }
#### [Vector](Vector.md) GetVec2 ( ) {: .copyable aria-label='Functions' }
返回胶囊体的起始位置（可以通过 `position` 设置）

### GetVec3 () {: aria-label='Functions' }
#### [Vector](Vector.md) GetVec3 ( ) {: .copyable aria-label='Functions' }
返回胶囊体的结束位置（可以通过 `targetposition` 设置）