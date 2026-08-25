---
tags:
  - Global
  - Class
---
# Global Class "MenuManager"

???+ info
    You can get this class by using the `MenuManager` global table.

    **注意：调用这些函数时，必须使用 .（句点）而非 :（冒号）！**
    
    ???+ example "Example Code"
        ```lua
        local sprite = MenuManager.GetBackWidgetSprite()
        ```

## Functions

### GetActiveMenu () {: aria-label='Functions' }
#### [MainMenuType](../enums/MainMenuType.md) GetActiveMenu ( ) {: .copyable aria-label='Functions' }
Returns the MainMenuType of the currently active (visible) section of the main menu.

___
### GetBackWidgetSprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetBackWidgetSprite ( ) {: .copyable aria-label='Functions' }

___
### GetColorModifierLerpAmount () {: aria-label='Functions' }
#### [ColorModifier](../ColorModifier.md) GetColorModifierLerpAmount ( ) {: .copyable aria-label='Functions' }

???+ info "Info"
    This is formatted as the absolute rate of change (ie, all values are positive).

___
### GetCurrentColorModifier () {: aria-label='Functions' }
#### [ColorModifier](../ColorModifier.md) GetCurrentColorModifier ( ) {: .copyable aria-label='Functions' }

___
### GetInputMask () {: aria-label='Functions' }
#### [ButtonActionBitwise](../enums/ButtonActionBitwise.md) GetInputMask ( ) {: .copyable aria-label='Functions' }
Returns the input mask of allowed inputs on the main menu.

___
### GetSelectWidgetSprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetSelectWidgetSprite ( ) {: .copyable aria-label='Functions' }

___
### GetShadowSprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetShadowSprite ( ) {: .copyable aria-label='Functions' }
Shadow decoration that looks like isaacs head.

___
### GetTargetColorModifier () {: aria-label='Functions' }
#### [ColorModifier](../ColorModifier.md) GetTargetColorModifier ( ) {: .copyable aria-label='Functions' }

___
### GetViewPosition () {: aria-label='Functions' }
#### [Vector](../Vector.md) GetViewPosition ( ) {: .copyable aria-label='Functions' }

___
### IsActive () {: aria-label='Functions' }
#### void IsActive () {: .copyable aria-label='Functions' }
Returns True when MenuManager is ready to be used a.k.a if you can use the menuman/mainmenu functionality (normally, if you are at the main menu).

___
### SetActiveMenu () {: aria-label='Functions' }
#### int SetActiveMenu ([MainMenuType](../enums/MainMenuType.md) Menu ) {: .copyable aria-label='Functions' }
Changes the active menu on the main menu to match the given `MainMenuType`.

___
### SetColorModifier () {: aria-label='Functions' }
#### void SetColorModifier ( [ColorModifier](../ColorModifier.md) ColorModifier, boolean Lerp = true, float Rate = 0.015 ) {: .copyable aria-label='Functions' }

___
### SetInputMask () {: aria-label='Functions' }
#### void SetInputMask ( [ButtonActionBitwise](../enums/ButtonActionBitwise.md) InputMask ) {: .copyable aria-label='Functions' }
Sets the input mask of allowed inputs on the main menu. Useful for custom menus.

___
### SetViewPosition () {: aria-label='Functions' }
#### void SetViewPosition ( [Vector](../Vector.md) Position ) {: .copyable aria-label='Functions' }

___
