---
tags:
  - Class
---
# Class "Sprite"

## Modified Constructors

### Sprite () {: aria-label='Modified Constructors' }
#### [Sprite](Sprite.md),boolean Sprite ( string ANM2Path, boolean LoadGraphics = true ) {: .copyable aria-label='Modified Constructors' }

Added two optional arguments, the function now returns two values: [Sprite](Sprite.md) object and the boolean signifying whether the sprite was loaded successfully or not.
___
## Modified Functions

### ReplaceSpritesheet () {: aria-label='Modified Functions' }
#### void ReplaceSpritesheet ( int LayerId, string PngFilename, boolean LoadGraphics = false ) {: .copyable aria-label='Modified Functions' }
现在接受一个可选的 `bool` 参数，用于确定在替换精灵表单后是否调用 `Sprite:LoadGraphics`。在大多数情况下，你会希望这样做。

### SetOverlayFrame () {: aria-label='Modified Functions' }
#### void SetOverlayFrame ( int FrameNum ) {: .copyable aria-label='Modified Functions' }
`SetOverlayFrame()` 的新重载，用于设置当前动画的帧而不停止动画，类似于 `SetFrame()` 的重载。

### Stop () {: aria-label='Modified Functions' }
#### void Stop ( boolean StopOverlay = true ) {: .copyable aria-label='Modified Functions' }
现在接受一个可选的 `bool` 参数，用于确定是否也停止覆盖动画。默认值为 true。

### ClearCustomChampionShader () {: aria-label='Functions' }
#### void ClearCustomChampionShader ( ) {: .copyable aria-label='Functions' }
移除由 `sprite:SetCustomChampionShader(path)` 应用的任何自定义 `coloroffset_champion` 着色器。

### ClearCustomShader () {: aria-label='Functions' }
#### void ClearCustomShader ( ) {: .copyable aria-label='Functions' }
移除由 `sprite:SetCustomShader(path)` 应用的任何自定义 `coloroffset` 着色器。

### Continue () {: aria-label='Functions' }
#### void Continue ( boolean ContinueOverlay = true ) {: .copyable aria-label='Functions' }
如果动画当前已停止，则使其从当前帧继续播放。不会重新启动已完成的非循环动画。

### ContinueOverlay () {: aria-label='Functions' }
#### void ContinueOverlay ( ) {: .copyable aria-label='Functions' }
与上述功能相同，但仅适用于覆盖动画。

### GetAllAnimationData () {: aria-label='Functions' }
#### [AnimationData](AnimationData.md)[] GetAllAnimationData ( ) {: .copyable aria-label='Functions' }
返回一个表示此 anm2 文件中所有动画的 [AnimationData](AnimationData.md) 表。

### GetAllLayers () {: aria-label='Functions' }
#### [LayerStates](LayerState.md)[] GetAllLayers ( ) {: .copyable aria-label='Functions' }
返回此精灵中所有 [LayerStates](LayerState.md) 的表。
___
### GetAnimationData () {: aria-label='Functions' }
#### [AnimationData](AnimationData.md) GetAnimationData ( string AnimationName ) {: .copyable aria-label='Functions' }

___
### GetCurrentAnimationData () {: aria-label='Functions' }
#### [AnimationData](AnimationData.md) GetCurrentAnimationData ( ) {: .copyable aria-label='Functions' }

___
### GetLayer () {: aria-label='Functions' }
#### [LayerState](LayerState.md) GetLayer ( int LayerId ) {: .copyable aria-label='Functions' }
返回提供的图层 ID 的图层数据。

### GetLayerFrameData () {: aria-label='Functions' }
#### [AnimationFrame](AnimationFrame.md) GetLayerFrameData ( int Layer ) {: .copyable aria-label='Functions' }
返回指定图层上当前显示的 [AnimationFrame](AnimationFrame.md)。

### GetNullFrame () {: aria-label='Functions' }
#### [NullFrame](NullFrame.md) GetNullFrame ( string LayerName ) {: .copyable aria-label='Functions' }
返回提供的图层名称的 [NullFrame](NullFrame.md)。

### GetOverlayAnimationData () {: aria-label='Functions' }
#### [AnimationData](AnimationData.md) GetOverlayAnimationData ( ) {: .copyable aria-label='Functions' }
返回当前播放的覆盖动画的 [AnimationData](AnimationData.md)。

### GetOverlayLayerFrameData () {: aria-label='Functions' }
#### [AnimationFrame](AnimationFrame.md) GetOverlayLayerFrameData ( int Layer ) {: .copyable aria-label='Functions' }
返回覆盖动画指定图层上当前显示的 [AnimationFrame](AnimationFrame.md)。

### GetOverlayNullFrame () {: aria-label='Functions' }
#### [NullFrame](NullFrame.md) GetOverlayNullFrame ( string LayerName ) {: .copyable aria-label='Functions' }
返回覆盖动画提供的图层名称的 [NullFrame](NullFrame.md)。

### GetRenderFlags () {: aria-label='Functions' }
#### [AnimRenderFlags](enums/AnimRenderFlags.md) GetRenderFlags ( ) {: .copyable aria-label='Functions' }

___
### HasCustomChampionShader () {: aria-label='Functions' }
#### boolean HasCustomChampionShader ( string ShaderPath ) {: .copyable aria-label='Functions' }
如果指定的自定义冠军着色器当前已加载，则返回 true（请参阅下面的 `SetCustomChampionShader`）。如果未提供字符串，则如果应用了任何自定义冠军着色器，则返回 true。

### HasCustomShader () {: aria-label='Functions' }
#### boolean HasCustomShader ( string ShaderPath ) {: .copyable aria-label='Functions' }
如果指定的自定义着色器当前已加载，则返回 true（请参阅下面的 `SetCustomShader`）。如果未提供字符串，则如果应用了任何自定义着色器，则返回 true。

### IsOverlayEventTriggered () {: aria-label='Functions' }
#### boolean IsOverlayEventTriggered ( string EventName ) {: .copyable aria-label='Functions' }
如果当前播放的覆盖动画刚刚到达具有提供名称的事件，则返回 `true`。

### SetCustomChampionShader () {: aria-label='Functions' }
#### void SetCustomChampionShader ( string ShaderPath ) {: .copyable aria-label='Functions' }
仅当实体实际上是精英怪时，游戏才会使用自定义精英怪着色器。
你还可以通过 [LayerState](LayerState.md) 设置每层的着色器。
为这个精灵指定一个自定义精英怪着色器文件，以代替通常的 `coloroffset_champion` 着色器。提供的路径预计从 `.../resources/` 开始，并在该位置找到 .vs 和 .fs 文件。例如：`sprite:SetCustomChampionShader("shaders/my_shader")` 将加载 `.../resources/shaders/my_shader.vs` 和 `.../resources/shaders/my_shader.fs`。
请注意，自定义着色器必须采用游戏使用的默认 `coloroffset_champion` 着色器完全相同的输入（与 `coloroffset` 相比，它有一个额外的输入）。


### SetCustomShader () {: aria-label='Functions' }
#### void SetCustomShader ( string ShaderPath ) {: .copyable aria-label='Functions' }
请注意，自定义着色器必须采用游戏使用的默认 `coloroffset` 着色器完全相同的输入。gold和教条着色器也使用相同的输入，可以作为很好的参考。
如果实体是精英怪，或者它应用了gold/教条着色器，游戏将不会使用此自定义着色器。
你还可以通过 [LayerState](LayerState.md) 设置每层的着色器。
为这个精灵指定一个自定义着色器文件，以代替默认的 `coloroffset` 着色器。提供的路径预计从 `.../resources/` 开始，并在该位置找到 .vs 和 .fs 文件。例如：`sprite:SetCustomShader("shaders/my_shader")` 将加载 `.../resources/shaders/my_shader.vs` 和 `.../resources/shaders/my_shader.fs`。
### SetOverlayLayerFrame () {: aria-label='Functions' }
### SetOverlayLayerFrame () {: aria-label='Functions' }
#### void SetOverlayLayerFrame ( int Layer, int Frame ) {: .copyable aria-label='Functions' }

___
### SetRenderFlags () {: aria-label='Functions' }
#### void SetRenderFlags ( [AnimRenderFlags](enums/AnimRenderFlags.md) Flags ) {: .copyable aria-label='Functions' }

___
### StopOverlay () {: aria-label='Functions' }
#### void StopOverlay ( ) {: .copyable aria-label='Functions' }

___
### WasOverlayEventTriggered () {: aria-label='Functions' }
#### boolean WasOverlayEventTriggered ( string EventName ) {: .copyable aria-label='Functions' }

___
