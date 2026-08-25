---
tags:
  - Class
---
# Class "ColorModifier"

[here.](./examples/ColorModifiers.md)可以找到一个使用ColorModifier类的示例模组

???+ info

    你可以通过其构造函数获取此类:

    ???+ example "Example Code"
    
        ```lua
        local tintRed = ColorModifier(1,0,0,0.33,0,1)
        ```

## Constructors

### ColorModifier () {: aria-label='Constructors' }
#### [ColorModifier](ColorModifier.md) ColorModifier ( float R = 1, float G = 1, float B = 1, float A = 0, float Brightness = 0, float Contrast = 1 ) {: .copyable aria-label='Constructors' }
## Variables

???+ warning "Warning"

    这充当强度乘数，并且为了使 RGB 产生任何效果，它必须不为零！

___
### A {: aria-label='Variables' }
#### float A {: .copyable aria-label='Variables'}
???+ warning "Warning"

    这充当强度乘数，并且为了使 RGB 产生任何效果，它必须不为零！

___
### B {: aria-label='Variables' }
#### float B {: .copyable aria-label='Variables'}

___
### Brightness {: aria-label='Variables' }
#### float Brightness {: .copyable aria-label='Variables'}

___
### Contrast {: aria-label='Variables' }
#### float Contrast {: .copyable aria-label='Variables'}

___
### G {: aria-label='Variables' }
#### float G {: .copyable aria-label='Variables'}

___
### R {: aria-label='Variables' }
#### float R {: .copyable aria-label='Variables'}

___

## Operators

### __add () {: aria-label='Operators' }
#### [ColorModifier](ColorModifier.md) __add ( [ColorModifier](ColorModifier.md) right ) {: .copyable aria-label='Operators' }
定义了使用 `+` 运算符对两个 [ColorModifier](ColorModifier.md) 对象进行加法运算。

___
### __div () {: aria-label='Operators' }
#### [ColorModifier](ColorModifier.md) __div ( [ColorModifier](ColorModifier.md) right ) {: .copyable aria-label='Operators' }
定义了使用 `/` 运算符对一个 [ColorModifier](ColorModifier.md) 对象和一个 `float` 类型数值进行除法运算。`ColorModifier` 必须位于运算符左侧。

___
### __eq () {: aria-label='Operators' }
#### [ColorModifier](ColorModifier.md) __eq ( [ColorModifier](ColorModifier.md) right ) {: .copyable aria-label='Operators' }
定义了使用 `==` 运算符判断两个 [ColorModifier](ColorModifier.md) 对象是否相等。

___
### __mul () {: aria-label='Operators' }
#### [ColorModifier](ColorModifier.md) __mul ( [ColorModifier](ColorModifier.md) right ) {: .copyable aria-label='Operators' }
定义了使用 `*` 运算符对一个 [ColorModifier](ColorModifier.md) 对象和一个 `float` 类型数值进行乘法运算。`ColorModifier` 必须位于运算符左侧。

___
### __sub () {: aria-label='Operators' }
#### [ColorModifier](ColorModifier.md) __sub ( [ColorModifier](ColorModifier.md) right ) {: .copyable aria-label='Operators' }
定义了使用 `-` 运算符对两个 [ColorModifier](ColorModifier.md) 对象进行减法运算。

___