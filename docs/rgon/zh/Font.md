---
tags:
  - Class
---
# Class "Font"

## Modified Constructors

### Font () {: aria-label='Modified Constructors' }
#### [Font](Font.md),boolean Font ( string FontPath ) {: .copyable aria-label='Modified Constructors' }
新增可选的 "FontPath" 参数；该函数现在返回两个值：[Font](Font.md) 对象，以及一个表示字体是否成功加载的布尔值。
___
## Modified Functions

### DrawString () {: aria-label='Modified Functions' }
#### void DrawString ( string String, float PositionX, float PositionY, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) RenderColor, int BoxWidth = 0, boolean Center = false ) {: .copyable aria-label='Modified Functions' }
与默认函数相同，但增加了更完善的输入验证，以防止崩溃。

### DrawStringScaled () {: aria-label='Modified Functions' }
#### void DrawStringScaled ( string String, float PositionX, float PositionY, float ScaleX, float ScaleY, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) RenderColor, int BoxWidth = 0, boolean Center = false ) {: .copyable aria-label='Modified Functions' }
与默认函数相同，但增加了更完善的输入验证，以防止崩溃。

### DrawStringScaledUTF8 () {: aria-label='Modified Functions' }
#### void DrawStringScaledUTF8 ( string String, float PositionX, float PositionY, float ScaleX, float ScaleY, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) RenderColor, int BoxWidth = 0, boolean Center = false ) {: .copyable aria-label='Modified Functions' }
与默认函数相同，但增加了更完善的输入验证，以防止崩溃。

### DrawStringUTF8 () {: aria-label='Modified Functions' }
#### void DrawStringUTF8 ( string String, float PositionX, float PositionY, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) RenderColor, int BoxWidth = 0, boolean Center = false ) {: .copyable aria-label='Modified Functions' }
与默认函数相同，但增加了更完善的输入验证，以防止崩溃。

### GetStringWidth () {: aria-label='Modified Functions' }
#### int GetStringWidth ( string String ) {: .copyable aria-label='Modified Functions' }
与默认函数相同，但增加了更完善的输入验证，以防止崩溃。

### GetStringWidthUTF8 () {: aria-label='Modified Functions' }
#### int GetStringWidthUTF8 ( string String ) {: .copyable aria-label='Modified Functions' }
与默认函数相同，但增加了更完善的输入验证，以防止崩溃。
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
