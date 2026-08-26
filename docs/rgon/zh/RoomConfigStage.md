---
tags:
  - Class
---
# Class "RoomConfigStage"

???+ info
    你可以通过以下函数获取此类:

    - [RoomConfig.GetStage()](RoomConfig.md#getstage)
    
    ???+ example "Example Code"
        ```lua
        local roomConfigStage = RoomConfig.GetStage(StbType.BASEMENT)
        ```

## Functions

### GetBackdrop () {: aria-label='Functions' }
#### [BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html?h=backdrop) GetBackdrop ( ) {: .copyable aria-label='Functions' }
返回该舞台默认房间使用的 `BackdropType`。

### GetBossSpot () {: aria-label='Functions' }
#### string GetBossSpot ( ) {: .copyable aria-label='Functions' }
返回 Boss 开场动画中使用的 Boss 位置精灵路径。

### GetDisplayName () {: aria-label='Functions' }
#### string GetDisplayName ( ) {: .copyable aria-label='Functions' }
返回舞台名称。

___
### GetXMLName () {: aria-label='Functions' }
#### string GetXMLName ( ) {: .copyable aria-label='Functions' }

___
### IsLoaded () {: aria-label='Functions' }
#### boolean IsLoaded ( int mode = 0 ) {: .copyable aria-label='Functions' }

___
### SetBackdrop () {: aria-label='Functions' }
#### void SetBackdrop ( [BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html?h=backdrop) Backdrop ) {: .copyable aria-label='Functions' }
设置该舞台默认房间使用的 `BackdropType`。

### SetBossSpot () {: aria-label='Functions' }
#### void SetBossSpot ( string PngFilename ) {: .copyable aria-label='Functions' }
设置 Boss 开场动画中使用的 Boss 位置精灵路径。

### SetDisplayName () {: aria-label='Functions' }
#### void SetDisplayName ( string Name ) {: .copyable aria-label='Functions' }
设置舞台名称。

### SetMusic () {: aria-label='Functions' }
#### void SetMusic ( [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html?h=music) Music ) {: .copyable aria-label='Functions' }
设置该舞台默认房间使用的 `Music`。

### SetPlayerSpot () {: aria-label='Functions' }
#### void SetPlayerSpot ( string PngFilename ) {: .copyable aria-label='Functions' }
设置 Boss 开场动画和梦魇过渡中使用的玩家位置精灵路径。

### SetSuffix () {: aria-label='Functions' }
#### void SetSuffix ( string Suffix ) {: .copyable aria-label='Functions' }
设置该舞台用于舞台专属精灵的后缀，例如 Boss/玩家位置精灵以及敌人的专属变体。

___
### SetXMLName () {: aria-label='Functions' }
#### void SetXMLName ( string name ) {: .copyable aria-label='Functions' }

___
### Unload () {: aria-label='Functions' }
#### void Unload ( ) {: .copyable aria-label='Functions' }

___
