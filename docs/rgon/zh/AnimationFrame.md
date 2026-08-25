---
tags:
  - Class
---
# Class "AnimationFrame"

来自 ANM2 文件的动画某一层单个帧的缓存数据。由所有使用相同 ANM2 的精灵共享，且不可修改。

请注意，插值和根动画已预先计算并包含在这些值中。

此外，这些值与 ANM2 编辑器中可见的值相对应，并且命名方式相同.

可通过 [AnimationLayer:GetFrame()](AnimationLayer.md#getframe) 获取.

## Functions

### GetColor () {: aria-label='Functions' }
#### [const Color](Color.md) GetColor ( ) {: .copyable aria-label='Functions' }

___
### GetCrop () {: aria-label='Functions' }
#### [const Vector](Vector.md) GetCrop ( ) {: .copyable aria-label='Functions' }

___
### GetEndFrame () {: aria-label='Functions' }
#### int GetEndFrame ( ) {: .copyable aria-label='Functions' }
也就是说，本动画帧（AnimationFrame）在此帧之后将不再显示。
请注意，“结束帧”是下一动画帧（AnimationFrame）的起始帧。### GetHeight () {: aria-label='Functions' }
#### float GetHeight ( ) {: .copyable aria-label='Functions' }

___
### GetPivot () {: aria-label='Functions' }
#### [const Vector](Vector.md) GetPivot ( ) {: .copyable aria-label='Functions' }

___
### GetPos () {: aria-label='Functions' }
#### [const Vector](Vector.md) GetPos ( ) {: .copyable aria-label='Functions' }

___
### GetRotation () {: aria-label='Functions' }
#### float GetRotation ( ) {: .copyable aria-label='Functions' }

___
### GetScale () {: aria-label='Functions' }
#### [const Vector](Vector.md) GetScale ( ) {: .copyable aria-label='Functions' }

___
### GetStartFrame () {: aria-label='Functions' }
#### int GetStartFrame ( ) {: .copyable aria-label='Functions' }

___
### GetWidth () {: aria-label='Functions' }
#### float GetWidth ( ) {: .copyable aria-label='Functions' }

___
### IsInterpolated () {: aria-label='Functions' }
#### boolean IsInterpolated ( ) {: .copyable aria-label='Functions' }

___
### IsVisible () {: aria-label='Functions' }
#### boolean IsVisible ( ) {: .copyable aria-label='Functions' }

___
