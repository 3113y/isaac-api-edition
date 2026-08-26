---
tags:
  - Class
---
# Class "ColorParams"

???+ info

    可以通过构造函数访问此类：

    ???+ example "Example Code"
    
        ```lua
        local fiveSecondRedColor = ColorParams(Color(1,0,0,1),255,150,false,false)
        ```

## Constructors

### ColorParams () {: aria-label='Constructors' }
#### [ColorParams](ColorParams.md) ColorParams ( [Color](Color.md) color, int priority, int duration1, int duration2, boolean fadeout, boolean shared ) {: .copyable aria-label='Constructors' }

___

## Functions

### GetColor () {: aria-label='Functions' }
#### [Color](Color.md) GetColor ( ) {: .copyable aria-label='Functions' }

___
### GetDuration () {: aria-label='Functions' }
#### int GetDuration ( ) {: .copyable aria-label='Functions' }
定义这些参数应持续的更新帧数。该值不会影响剩余帧数，但如果启用了 `Fadeout`（淡出），则会影响淡出速度（计算方式为 `Lifespan / Duration`，即“寿命/持续时间”）。

### GetFadeout () {: aria-label='Functions' }
#### boolean GetFadeout ( ) {: .copyable aria-label='Functions' }

___
### GetLifespan () {: aria-label='Functions' }
#### int GetLifespan ( ) {: .copyable aria-label='Functions' }
定义这些参数过期前剩余的更新帧数。在每秒 30 次的非插值更新中，该值每次更新减 1。更改此值会直接影响这些参数过期前的剩余帧数。

___
### GetPriority () {: aria-label='Functions' }
#### int GetPriority ( ) {: .copyable aria-label='Functions' }

___
### GetShared () {: aria-label='Functions' }
#### boolean GetShared ( ) {: .copyable aria-label='Functions' }

___
### SetColor () {: aria-label='Functions' }
#### void SetColor ( [Color](Color.md) Color ) {: .copyable aria-label='Functions' }

___
### SetDuration () {: aria-label='Functions' }
#### void SetDuration ( int Duration ) {: .copyable aria-label='Functions' }

___
### SetFadeout () {: aria-label='Functions' }
#### void SetFadeout ( boolean Value ) {: .copyable aria-label='Functions' }

___
### SetLifespan () {: aria-label='Functions' }
#### void SetLifespan ( int Duration ) {: .copyable aria-label='Functions' }

___
### SetPriority () {: aria-label='Functions' }
#### void SetPriority ( int Priority ) {: .copyable aria-label='Functions' }

___
### SetShared () {: aria-label='Functions' }
#### void SetShared ( boolean Value ) {: .copyable aria-label='Functions' }

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
