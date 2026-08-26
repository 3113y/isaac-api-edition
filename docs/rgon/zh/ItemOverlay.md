---
tags:
  - Global
  - Class
---
# Global Class "ItemOverlay"

???+ info
    可以通过 `ItemOverlay` 全局表获取此类。
    
    **注意：调用这些函数时，必须使用 .（句点）而非 :（冒号）！**
    
    ???+ example "Example Code"
        ```lua
        local overlaysprite = ItemOverlay.GetSprite()
        ```
        
## Functions

### GetDelay () {: aria-label='Functions' }
#### int GetDelay ( ) {: .copyable aria-label='Functions' }

___
### GetMegaMushPlayerSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetMegaMushPlayerSprite ( ) {: .copyable aria-label='Functions' } 

___
### GetOverlayID () {: aria-label='Functions' }
#### [Giantbook](enums/Giantbook.md) GetOverlayID ( ) {: .copyable aria-label='Functions' }
???+ info "Info"
    如果尚未播放过任何动画，则返回 0。
    返回最近播放的 Giantbook 动画；如果当前正在播放动画，则返回当前的 Giantbook。
### GetPlayer () {: aria-label='Functions' }
#### [EntityPlayer](EntityPlayer.md) GetPlayer ( ) {: .copyable aria-label='Functions' }

___
### GetSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetSprite ( ) {: .copyable aria-label='Functions' }

___
### Show () {: aria-label='Functions' }
#### void Show ( [Giantbook](enums/Giantbook.md) GiantbookID, int Delay = 3, [EntityPlayer](EntityPlayer.md) = nil ) {: .copyable aria-label='Functions' }

___
