---
tags:
  - Class
---
# Class "EntityConfigPlayer"

???+ info

    你可以通过以下函数获取此类:

    * [EntityConfig.GetPlayer()](EntityConfig.md#getplayer)

    ???+ example "Example Code"

        ```lua
        local cainConfig = EntityConfig.GetPlayer(PlayerType.PLAYER_CAIN)
        ```
        
## Functions

### CanShoot () {: aria-label='Functions' }
#### boolean CanShoot ( ) {: .copyable aria-label='Functions' }

___
### GetAchievementID () {: aria-label='Functions' }
#### [Achievement](enums/Achievement.md) GetAchievementID ( ) {: .copyable aria-label='Functions' }
如果角色未被原版成就锁定，则返回 -1（若为“隐藏”的原版角色，则返回 -2）。

___
### GetBirthrightDescription () {: aria-label='Functions' }
#### string GetBirthrightDescription ( ) {: .copyable aria-label='Functions' }

___
### GetBlackHearts () {: aria-label='Functions' }
#### int GetBlackHearts ( ) {: .copyable aria-label='Functions' }

___
### GetBombs () {: aria-label='Functions' }
#### int GetBombs ( ) {: .copyable aria-label='Functions' }

___
### GetBrokenHearts () {: aria-label='Functions' }
#### int GetBrokenHearts ( ) {: .copyable aria-label='Functions' }

___
### GetCard () {: aria-label='Functions' }
#### [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html) GetCard ( ) {: .copyable aria-label='Functions' }
不包括通过解锁获得的起始卡牌。

不包括模组添加的卡牌。

如果角色没有任何原版起始卡牌，则返回 0。

___
### GetCoins () {: aria-label='Functions' }
#### int GetCoins ( ) {: .copyable aria-label='Functions' }

___
### GetCollectibles () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)[] GetCollectibles ( ) {: .copyable aria-label='Functions' }
返回一个包含角色起始物品的 [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) 类型的表。

___
### GetCostumeID () {: aria-label='Functions' }
#### int GetCostumeID ( ) {: .copyable aria-label='Functions' }
如果角色没有任何通过 XML 定义的起始服装（如玛吉的头发），则返回 -1。

___
### GetCostumeSuffix () {: aria-label='Functions' }
#### string GetCostumeSuffix ( ) {: .copyable aria-label='Functions' }
用于角色特定服装精灵图的目录后缀。

___
### GetExtraPortraitPath () {: aria-label='Functions' }
#### string GetExtraPortraitPath ( ) {: .copyable aria-label='Functions' }
指向一个 `.anm2` 文件的路径，该文件显示在角色的关卡过渡和 Boss 对战屏幕肖像之上。

___
### GetKeys () {: aria-label='Functions' }
#### int GetKeys ( ) {: .copyable aria-label='Functions' }

___
### GetModdedControlsSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetModdedControlsSprite ( ) {: .copyable aria-label='Functions' }
对于原版角色或没有相应动画的角色，返回 nil。

请注意，此精灵图由同一模组中的其他角色共享 - 存在一个与该角色同名的动画。

返回用于模组角色起始房间控制界面的精灵图。

___
### GetModdedCoopMenuSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetModdedCoopMenuSprite ( ) {: .copyable aria-label='Functions' }
对于原版角色或没有相应动画的角色，返回 nil。

请注意，此精灵图由同一模组中的其他角色共享 - 存在一个与该角色同名的动画。

返回用于模组角色在合作角色选择轮中的图标的精灵图。

___
### GetModdedGameOverSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetModdedGameOverSprite ( ) {: .copyable aria-label='Functions' }
对于原版角色或没有相应动画的角色，返回 nil。

请注意，此精灵图由同一模组中的其他角色共享 - 存在一个与该角色同名的动画。

返回用于模组角色游戏结束屏幕（即他们的名字）的精灵图。

___
### GetModdedMenuBackgroundSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetModdedMenuBackgroundSprite ( ) {: .copyable aria-label='Functions' }
对于原版角色或没有相应动画的角色，返回 nil。

请注意，此精灵图由同一模组中的其他角色共享 - 存在一个与该角色同名的动画。

返回用于模组角色角色选择屏幕的精灵图。

___
### GetModdedMenuPortraitSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetModdedMenuPortraitSprite ( ) {: .copyable aria-label='Functions' }
对于原版角色或没有相应动画的角色，返回 nil。

请注意，此精灵图由同一模组中的其他角色共享 - 存在一个与该角色同名的动画。

返回用于模组角色角色选择肖像的精灵图。

___
### GetName () {: aria-label='Functions' }
#### string GetName ( ) {: .copyable aria-label='Functions' }

___
### GetNameImagePath () {: aria-label='Functions' }
#### string GetNameImagePath ( ) {: .copyable aria-label='Functions' }
指向用于 Boss 对战屏幕上角色名字的 PNG 文件的路径。

___
### GetPill () {: aria-label='Functions' }
#### [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) GetPill ( ) {: .copyable aria-label='Functions' }
不包括通过解锁获得的起始药丸。

___
### GetPlayerType () {: aria-label='Functions' }
#### int GetPlayerType ( ) {: .copyable aria-label='Functions' }

___
### GetPocketActive () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetPocketActive ( ) {: .copyable aria-label='Functions' }
不包括模组添加的物品。

___
### GetPortraitPath () {: aria-label='Functions' }
#### string GetPortraitPath ( ) {: .copyable aria-label='Functions' }
指向用于角色主要关卡过渡和 Boss 对战屏幕肖像的 PNG 文件的路径。

___
### GetRedHearts () {: aria-label='Functions' }
#### int GetRedHearts ( ) {: .copyable aria-label='Functions' }

___
### GetSkinColor () {: aria-label='Functions' }
#### [SkinColor](https://wofsauge.github.io/IsaacDocs/rep/enums/SkinColor.html) GetSkinColor ( ) {: .copyable aria-label='Functions' }

___
### GetSkinPath () {: aria-label='Functions' }
#### string GetSkinPath ( ) {: .copyable aria-label='Functions' }
指向用于角色主要精灵图的 PNG 文件的路径。

___
### GetSoulHearts () {: aria-label='Functions' }
#### int GetSoulHearts ( ) {: .copyable aria-label='Functions' }

___
### GetTaintedCounterpart () {: aria-label='Functions' }
#### [EntityConfigPlayer](EntityConfigPlayer.md) GetTaintedCounterpart ( ) {: .copyable aria-label='Functions' }
对于非堕化角色，返回其堕化对应角色；如果没有，则返回 nil。

对于堕化角色，返回其非堕化对应角色。

___
### GetTrinket () {: aria-label='Functions' }
#### [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) GetTrinket ( ) {: .copyable aria-label='Functions' }
不包括通过解锁获得的起始饰品。

不包括模组添加的饰品。

___
### IsHidden () {: aria-label='Functions' }
#### boolean IsHidden ( ) {: .copyable aria-label='Functions' }
如果角色在角色选择屏幕上不可见/不可选，则返回 true。

不包括那些只有在解锁前才隐藏的角色。

___
### IsTainted () {: aria-label='Functions' }
#### boolean IsTainted ( ) {: .copyable aria-label='Functions' }

___