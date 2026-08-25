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
Returns the `BackdropType` used in default rooms on the stage.

### GetBossSpot () {: aria-label='Functions' }
#### string GetBossSpot ( ) {: .copyable aria-label='Functions' }
Returns the sprite path for the boss spot used in the boss intro.

### GetDisplayName () {: aria-label='Functions' }
#### string GetDisplayName ( ) {: .copyable aria-label='Functions' }
Returns the name of the stage.

___
### GetXMLName () {: aria-label='Functions' }
#### string GetXMLName ( ) {: .copyable aria-label='Functions' }

___
### IsLoaded () {: aria-label='Functions' }
#### boolean IsLoaded ( int mode = 0 ) {: .copyable aria-label='Functions' }

___
### SetBackdrop () {: aria-label='Functions' }
#### void SetBackdrop ( [BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html?h=backdrop) Backdrop ) {: .copyable aria-label='Functions' }
Sets the `BackdropType` used in default rooms on the stage.

### SetBossSpot () {: aria-label='Functions' }
#### void SetBossSpot ( string PngFilename ) {: .copyable aria-label='Functions' }
Sets the sprite path for the boss spot used in the boss intro.

### SetDisplayName () {: aria-label='Functions' }
#### void SetDisplayName ( string Name ) {: .copyable aria-label='Functions' }
Sets the name of the stage.

### SetMusic () {: aria-label='Functions' }
#### void SetMusic ( [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html?h=music) Music ) {: .copyable aria-label='Functions' }
Sets the `Music` used in default rooms on the stage.

### SetPlayerSpot () {: aria-label='Functions' }
#### void SetPlayerSpot ( string PngFilename ) {: .copyable aria-label='Functions' }
Sets the sprite path for the player spot used in the boss intro and nightmare transition.

### SetSuffix () {: aria-label='Functions' }
#### void SetSuffix ( string Suffix ) {: .copyable aria-label='Functions' }
Sets the suffix used by the stage for stage-unique sprites, such as the boss/player spot and unique variants for enemies.

___
### SetXMLName () {: aria-label='Functions' }
#### void SetXMLName ( string name ) {: .copyable aria-label='Functions' }

___
### Unload () {: aria-label='Functions' }
#### void Unload ( ) {: .copyable aria-label='Functions' }

___
