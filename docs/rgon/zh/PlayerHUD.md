---
tags:
  - Class
---
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
# Class "PlayerHUD"

???+ info
    你可以使用以下函数获取此类对象：

    * [HUD.GetPlayerHUD()](HUD.md#getplayerhud)

    ???+ example "Example Code"
        ```lua
        local playerHud = HUD.GetPlayerHUD(0)
        ```

## Functions

### GetHeartByIndex () {: aria-label='Functions' }
#### [PlayerHUDHeart](PlayerHUDHeart.md) GetHeartByIndex ( int Index ) {: .copyable aria-label='Functions' }

___
### GetHearts () {: aria-label='Functions' }
#### [PlayerHUDHeart](PlayerHUDHeart.md)[] GetHearts ( ) {: .copyable aria-label='Functions' }
返回由 [PlayerHUDHeart](PlayerHUDHeart.md) 对象组成的表。
### GetHUD () {: aria-label='Functions' }
#### [HUD](HUD.md) GetHUD ( ) {: .copyable aria-label='Functions' }

___
### GetIndex () {: aria-label='Functions' }
#### int GetIndex ( ) {: .copyable aria-label='Functions' }

___
### GetLayout () {: aria-label='Functions' }
#### [PlayerHUDLayout](enums/PlayerHUDLayout.md) GetLayout ( ) {: .copyable aria-label='Functions' }

___
### GetPlayer () {: aria-label='Functions' }
#### [EntityPlayer](EntityPlayer.md) GetPlayer ( ) {: .copyable aria-label='Functions' }

___
### RenderActiveItem () {: aria-label='Functions' }
#### void RenderActiveItem ( [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot, [Vector](Vector.md) Position, float Alpha = 1.0, float Scale = 1.0 ) {: .copyable aria-label='Functions' }

___
