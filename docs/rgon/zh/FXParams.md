---
tags:
  - Class
---
# Class "FXParams"

???+ info
    你可以通过以下函数获取此类:

    * [Room:GetFXParams()](Room.md#getfxparams)

    ???+ example "Example Code"
        ```lua
        local fxparams = Game():GetRoom():GetFXParams()
        ```

## Variables
### ColorModifier {: aria-label='Variables' }
#### [ColorModifier](ColorModifier.md) ColorModifier {: .copyable aria-label='Variables'}
获取《忏悔》引入的色彩校正的可修改副本。此副本存储的是 `fxlayers.xml` 中使用的值，而非原始值（有关原始值，请参见 [GetCurrentColorModifier](Game.md#getcurrentcolormodifier)）。

此处所做的更改**不会**自动应用；请使用 [UpdateColorModifier](Room.md#updatecolormodifier) 来应用这些更改。
___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
### LightColor {: aria-label='Variables' }
#### [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) LightColor {: .copyable aria-label='Variables'}

___
### ShadowAlpha {: aria-label='Variables' }
#### float ShadowAlpha {: .copyable aria-label='Variables'}

___
### ShadowColor {: aria-label='Variables' }
#### [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) ShadowColor {: .copyable aria-label='Variables'}

___
### UseWaterV2 {: aria-label='Variables' }
#### boolean UseWaterV2 {: .copyable aria-label='Variables'}
如果启用，水将使用 Downpour 和 Dross 中出现的反射着色器.
___
### WaterColor {: aria-label='Variables' }
#### [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) WaterColor {: .copyable aria-label='Variables'}

___
### WaterColorMultiplier {: aria-label='Variables' }
#### [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) WaterColorMultiplier {: .copyable aria-label='Variables'}

___
### WaterEffectColor {: aria-label='Variables' }
#### [Color](Color.md) WaterEffectColor {: .copyable aria-label='Variables'}

___
