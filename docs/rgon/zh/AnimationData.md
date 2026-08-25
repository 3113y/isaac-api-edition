---
tags:
  - Class
---
# Class "AnimationData"

已加载的 ANM2 文件中一个动画的缓存数据。由所有使用相同 ANM2 的精灵共享，且不可修改.

可通过以下方法获取 [Sprite:GetAnimationData()](Sprite.md#getanimationdata), [Sprite:GetCurrentAnimationData()](Sprite.md#getanimationdata) or [Sprite:GetOverlayAnimationData()](Sprite.md#getanimationdata).

## Functions

### GetAllLayers () {: aria-label='Functions' }
#### [AnimationLayer](AnimationLayer.md)[] GetAllLayers ( ) {: .copyable aria-label='Functions' }
返回一个动画层（AnimationLayers）表，按从下到上的顺序排列（**不**按层ID排序）。

___
### GetLayer () {: aria-label='Functions' }
#### [AnimationLayer](AnimationLayer.md) GetLayer ( int LayerId ) {: .copyable aria-label='Functions' }
通过动画层的ID号获取一个动画层。

___
### GetLength () {: aria-label='Functions' }
#### int GetLength ( ) {: .copyable aria-label='Functions' }
此动画的帧数长度。### GetName () {: aria-label='Functions' }
#### string GetName ( ) {: .copyable aria-label='Functions' }

___
### IsLoopingAnimation () {: aria-label='Functions' }
#### boolean IsLoopingAnimation ( ) {: .copyable aria-label='Functions' }

___