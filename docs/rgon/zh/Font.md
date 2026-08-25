---
tags:
  - Class
---
# Class "Font"

## Modified Constructors

### Font () {: aria-label='Modified Constructors' }
#### [Font](Font.md),boolean Font ( string FontPath ) {: .copyable aria-label='Modified Constructors' }
新增了可选的 "FontPath" 参数，该函数现在返回两个值：[Font](Font.md) 对象和一个布尔值，用于表示字体是否成功加载。
___
## Modified Functions

### DrawString () {: aria-label='Modified Functions' }
#### void DrawString ( string String, float PositionX, float PositionY, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) RenderColor, int BoxWidth = 0, boolean Center = false ) {: .copyable aria-label='Modified Functions' }
与默认函数相同，但具有更好的输入验证，以防止崩溃。

### DrawStringScaled () {: aria-label='Modified Functions' }
#### void DrawStringScaled ( string String, float PositionX, float PositionY, float ScaleX, float ScaleY, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) RenderColor, int BoxWidth = 0, boolean Center = false ) {: .copyable aria-label='Modified Functions' }
与默认函数相同，但具有更好的输入验证，以防止崩溃。

### DrawStringScaledUTF8 () {: aria-label='Modified Functions' }
#### void DrawStringScaledUTF8 ( string String, float PositionX, float PositionY, float ScaleX, float ScaleY, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) RenderColor, int BoxWidth = 0, boolean Center = false ) {: .copyable aria-label='Modified Functions' }
与默认函数相同，但具有更好的输入验证，以防止崩溃。

### DrawStringUTF8 () {: aria-label='Modified Functions' }
#### void DrawStringUTF8 ( string String, float PositionX, float PositionY, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) RenderColor, int BoxWidth = 0, boolean Center = false ) {: .copyable aria-label='Modified Functions' }
与默认函数相同，但具有更好的输入验证，以防止崩溃。

### GetStringWidth () {: aria-label='Modified Functions' }
#### int GetStringWidth ( string String ) {: .copyable aria-label='Modified Functions' }
与默认函数相同，但具有更好的输入验证，以防止崩溃。

### GetStringWidthUTF8 () {: aria-label='Modified Functions' }
#### int GetStringWidthUTF8 ( string String ) {: .copyable aria-label='Modified Functions' }
与默认函数相同，但具有更好的输入验证，以防止崩溃。