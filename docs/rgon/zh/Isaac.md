---
tags:
  - Global
  - Class
---
# Global Class "Isaac"

## Modified Functions

### FindByType () {: aria-label='Modified Functions' }

#### [Entity](Entity.md)[] FindByType ( [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) Type, int Variant = -1, int SubType = -1, boolean Cache = false, boolean IgnoreFriendly = false ) {: .copyable aria-label='Modified Functions' }

与原版功能相同，但速度快得多。

___

### FindInRadius () {: aria-label='Modified Functions' }

#### [Entity](Entity.md)[] FindInRadius ( [Vector](Vector.md) Position, float Radius, [EntityPartition](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityPartition.html) Partitions = 0xFFFFFFFF  ) {: .copyable aria-label='Modified Functions' }

与原版功能相同，但速度快得多，并且修复了效果搜索的问题。

___

### GetRoomEntities () {: aria-label='Modified Functions' }

#### [Entity](Entity.md)[] GetRoomEntities ( ) {: .copyable aria-label='Modified Functions' }

与原版功能相同，但速度快得多。

___

### AllMarksFilled () {: aria-label='Functions' }

#### int AllMarksFilled ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character) {: .copyable aria-label='Functions' }

检查给定角色是否已完成所有标记，并返回一个整数，表示完成这些标记的最高难度。
???- info "Note"

  难度等级如下：
  - `0` - 未完成
  - `1` - 普通
  - `2` - 困难

___

### AllTaintedCompletion () {: aria-label='Functions' }

#### int AllTaintedCompletion ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character, [TaintedMarksGroup](enums/TaintedMarksGroup.md) Group) {: .copyable aria-label='Functions' }

检查给定角色是否已完成所有与受污染解锁相关的标记，并返回一个整数，表示完成这些标记的最高难度。

???- info "Note"

  难度等级如下：
  - `0` - 未完成
  - `1` - 普通
  - `2` - 困难

___

### CanStartTrueCoop () {: aria-label='Functions' }

#### boolean CanStartTrueCoop ( ) {: .copyable aria-label='Functions' }

___

### CenterCursor () {: aria-label='Functions' }

#### void CenterCursor ( ) {: .copyable aria-label='Functions' }

将窗口鼠标光标移动到游戏窗口的中心。这是一个非常小众但很有用的功能，如果您想使用光标控制进行任何奇特的操作并完全控制它。如果 Isaac.exe 失去焦点，它不会移动光标。

???- info "Note"

    请记住，屏幕中心不一定是房间的中心，它只是游戏窗口的中心（如果您处于全屏模式，则是实际屏幕的中心）。

___

### ClearBossHazards () {: aria-label='Functions' }

#### void ClearBossHazards ( boolean IgnoreNPCs = false ) {: .copyable aria-label='Functions' }

清除所有弹幕。如果 `IgnoreNPCs` 为 false，还会清除所有能够关闭门的非友方 NPC。

___

### ClearChallenge () {: aria-label='Functions' }

#### void ClearChallenge ( int challengeid) {: .copyable aria-label='Functions' }

将相应 `challengeid` 的挑战标记为已完成。

___

### ClearCompletionMarks () {: aria-label='Functions' }

#### void ClearCompletionMarks ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character) {: .copyable aria-label='Functions' }

删除给定角色的所有完成标记。

___

### CreateTimer () {: aria-label='Functions' }

#### [EntityEffect](https://wofsauge.github.io/IsaacDocs/rep/EntityEffect.html) CreateTimer ( function Function, int Interval, int Times, boolean Persistent ) {: .copyable aria-label='Functions' }

此计时器在每次游戏更新时调用。这意味着计时器仅考虑游戏正在积极运行且未暂停的帧，并使用更新帧作为其延迟参数（每秒 30 帧）。
生成一个计时器实体效果。该实体将在 `Interval` 帧后开始运行 `Function` 函数，并将重复执行 `Times` 次。`Persistent` 控制此计时器是在当前房间“死亡”，还是跨房间持续存在。

???- info "计时器行为"

    如果您的用例需要计时器考虑暂停时间，请使用在 RENDER 回调上运行的自定义计时器。

___

### CreateWeapon () {: aria-label='Functions' }

#### [Weapon](Weapon.md) CreateWeapon ( [WeaponType](https://wofsauge.github.io/IsaacDocs/rep/enums/WeaponType.html) Type, [Entity](Entity.md) Owner ) {: .copyable aria-label='Functions' }

创建并返回一个 [Weapon](Weapon.md) 对象。它不会自动被 `owner` 使用，必须与 `Isaac.SetWeaponType` 一起使用。

___

### DestroyWeapon () {: aria-label='Functions' }

#### void DestroyWeapon ( [Weapon](Weapon.md) Weapon ) {: .copyable aria-label='Functions' }

销毁提供的 [Weapon](Weapon.md) 对象。

___

### DrawLine () {: aria-label='Functions' }

#### void DrawLine ( [Vector](Vector.md) StartPos, [Vector](Vector.md) EndPos, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor) StartColor, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor) EndColor, int Thickness ) {: .copyable aria-label='Functions' }

在当前渲染帧中，在两个给定位置之间绘制一条线。

___

### DrawQuad () {: aria-label='Functions' }

#### void DrawQuad ( [Vector](Vector.md) TopLeftPos, [Vector](Vector.md) TopRightPos, [Vector](Vector.md) BottomLeftPos, [Vector](Vector.md) BottomRightPos, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor) Color, int Thickness ) {: .copyable aria-label='Functions' }

在当前渲染帧中，在两个给定位置之间绘制一条线。游戏内部使用自己的结构体 DestinationQuad 来实现此功能，但我还没有将其添加到 Lua 中 :crocodile:

___

### FillCompletionMarks () {: aria-label='Functions' }

#### void FillCompletionMarks ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character) {: .copyable aria-label='Functions' }

完成给定角色的所有完成标记。

___

### FindInCapsule () {: aria-label='Functions' }

#### [Entity](Entity.md)[] FindInCapsule ( [Capsule](Capsule.md) Capsule, [EntityPartitions](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityPartition.html) Partitions = -1 ) {: .copyable aria-label='Functions' }

返回给定胶囊内的实体，并根据分区掩码进行过滤。

___

### FindTargetPit () {: aria-label='Functions' }

#### int FindTargetPit ( [Vector](Vector.md) Position, [Vector](Vector.md) TargetPosition, int PitIndex = -1 ) {: .copyable aria-label='Functions' }

___

### GetAchievementIdByName () {: aria-label='Functions' }

#### int GetAchievementIdByName ( string Name ) {: .copyable aria-label='Functions' }

按名称获取成就 ID。

___

### GetAllowedDoorsMaskForRoomShape () {: aria-label='Functions' }
#### [DoorMask](enums/DoorMask.md) GetAllowedDoorsMaskForRoomShape ( [RoomShape](https://wofsauge.github.io/IsaacDocs/rep/enums/RoomShape.html) RoomShape ) {: .copyable aria-label='Functions' }
Returns a [DoorMask](enums/DoorMask.md) representing all [DoorSlots](https://wofsauge.github.io/IsaacDocs/rep/enums/DoorSlot.html) allowed for the given [RoomShape](https://wofsauge.github.io/IsaacDocs/rep/enums/RoomShape.html).

___
### GetAxisAlignedUnitVectorFromDir () {: aria-label='Functions' }

#### [Vector](Vector.md) GetAxisAlignedUnitVectorFromDir ( [Direction](https://wofsauge.github.io/IsaacDocs/rep/enums/Direction.html) Direction = -1 ) {: .copyable aria-label='Functions' }

___

### GetBackdropIdByName () {: aria-label='Functions' }

#### int GetBackdropIdByName ( string BackdropName ) {: .copyable aria-label='Functions' }

___

### GetBossColorIdxByName () {: aria-label='Functions' }

#### int GetBossColorIdxByName ( string Name ) {: .copyable aria-label='Functions' }

按名称获取 boss 颜色索引，该索引通常是 boss 变为所需颜色所需的子类型。当然，您实际上需要在 xml 中为您的颜色条目命名，此功能才能正常工作（后缀通常不起作用，因为它不是必需的）。

___

### GetButtonsSprite () {: aria-label='Modified Functions' }
#### [Sprite](Sprite.md) GetButtonsSprite ( ) {: .copyable aria-label='Functions' }
Controllers buttons sprite

___
### GetClipboard () {: aria-label='Functions' }

#### string GetClipboard ( ) {: .copyable aria-label='Functions' }

获取剪贴板的内容，前提是它们是文本形式，否则将返回 nil。

___

### GetCollectibleSpawnPosition () {: aria-label='Functions' }

#### [Vector](Vector.md) GetCollectibleSpawnPosition ( [Vector](Vector.md) Position ) {: .copyable aria-label='Functions' }

___

### GetCompletionMark () {: aria-label='Functions' }

#### int GetCompletionMark ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character, [CompletionType](enums/CompletionType.md) Mark) {: .copyable aria-label='Functions' }

获取特定角色的完成标记值，值范围从 `0` 到 `2`（0 = 未完成，1 = 普通，2 = 困难.

___

### GetCompletionMarks () {: aria-label='Functions' }

#### table GetCompletionMarks ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character) {: .copyable aria-label='Functions' }

返回一个包含给定角色所有标记的表

???- info "Table structure & usage"

    该表具有以下字段

    - 角色类型（PlayerType）：包含与标记相关的 [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html).
    - MomsHeart: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Isaac: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Satan: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - BossRush: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - BlueBaby: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Lamb: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - MegaSatan: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - UltraGreed: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Hush: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - UltraGreedier: 困难贪婪模式,值2 ，大多冗余，无需设置
    - Delirium: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Mother: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Beast: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况

    ```lua
    local marks = Isaac.GetCompletionMarks(0)
    if (marks.MomsHeart > 0) then
        print("got mom")
    end
    if (marks.Lamb >= 2) then
        print("GOATED ON H4RD")
    end
    if (Isaac.GetCompletionMarks(0).Delirium > 0) then --doing it the lazy way, fitting deliriums theme
        print("Got Deli")
    end
    ```

___

### GetCurrentStageConfigId () {: aria-label='Functions' }

#### [StbType](enums/StbType.md) GetCurrentStageConfigId ( ) {: .copyable aria-label='Functions' }

获取当前阶段的当前 stageconfigId/stbType，或者您想称呼的 stages.xml 的 ID。

___

### GetCursorSprite () {: aria-label='Functions' }

#### [Sprite](Sprite.md) GetCursorSprite ( ) {: .copyable aria-label='Functions' }

当 `Options.MouseControl` 设置为 true 时，返回渲染的光标精灵。

___

### GetCutsceneIdByName () {: aria-label='Functions' }

#### table GetCutsceneIdByName ( string Name ) {: .copyable aria-label='Functions' }

按名称获取过场动画 ID。

___

### GetDwmWindowAttribute () {: aria-label='Functions' }

#### [DwmWindowAttribute](enums/DwmWindowAttribute.md) GetDwmWindowAttribute ( ) {: .copyable aria-label='Functions' }

___

### GetEntitySubTypeByName () {: aria-label='Functions' }

#### int GetEntitySubTypeByName ( string Name ) {: .copyable aria-label='Functions' }

按实体名称获取实体子类型。

___

### GetGiantBookIdByName () {: aria-label='Functions' }

#### int GetGiantBookIdByName ( string Name ) {: .copyable aria-label='Functions' }

按名称获取巨型书籍 ID。对于原版巨型书籍，gfx xml 属性中的 png 文件名用作巨型书籍名称。

___

### GetLoadedModules () {: aria-label='Functions' }

#### table GetLoadedModules ( ) {: .copyable aria-label='Functions' }

返回一个键值表，包含所有已加载的脚本文件，其中键是给定脚本文件的名称或路径，值是加载该文件后的返回值（在大多数情况下是 true 或一个表）。

___

### GetLocalizedString () {: aria-label='Functions' }

#### string GetLocalizedString ( string Category, string Key, int Language ) {: .copyable aria-label='Functions' }

返回给定类别中与给定键关联的翻译字符串。翻译以作为参数给出的语言 ID/语言代码提供。

___

### GetModChallengeClearCount () {: aria-label='Functions' }

#### int GetModChallengeClearCount ( int challengeid ) {: .copyable aria-label='Functions' }

返回自定义挑战被通关的次数。如果该挑战被设置为未完成，则该次数将重置。

___
### GetNanoTime () {: aria-label='Functions'}
#### int GetNanoTime ( ) {: .copyable aria-label='Functions' }
Returns a high-resolution timestamp in nanoseconds. Useful for evaluating the performance cost of functions in a non-test environment or for high-precision clocks.

???- info "Note"
	The clock is precise enough to detect the time that passed between two subsequent calls of `Isaac.GetNanoTime()`

___
### GetNullItemIdByName () {: aria-label='Functions' }

#### int GetNullItemIdByName ( string NullItemName ) {: .copyable aria-label='Functions' }

___

### GetPersistentGameData () {: aria-label='Functions' }

#### [PersistentGameData](PersistentGameData.md) GetPersistentGameData ( ) {: .copyable aria-label='Functions' }

___

### GetPoolIdByName () {: aria-label='Functions' }

#### [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) GetPoolIdByName ( string PoolName ) {: .copyable aria-label='Functions' }

返回给定自定义池的 ID。如果未找到该池，则返回 `-1`。

___

### GetRenderPosition () {: aria-label='Functions' }

#### [Vector](Vector.md) GetRenderPosition ( [Vector](Vector.md) Position, boolean Scale = true ) {: .copyable aria-label='Functions' }

___

### GetString () {: aria-label='Functions' }

#### string GetString ( string Category, string Key ) {: .copyable aria-label='Functions' }

返回给定类别中与给定键关联的翻译字符串。翻译以当前选定的语言提供。

___

### GetWindowTitle () {: aria-label='Functions' }

#### string GetWindowTitle ( ) {: .copyable aria-label='Functions' }

返回游戏窗口标题上附加的文本。

___

### IsChallengeDone () {: aria-label='Functions' }

#### boolean IsChallengeDone ( int challengeid ) {: .copyable aria-label='Functions' }

如果相应 challengeid 的挑战已完成，则返回 `true`。

___

### IsInGame () {: aria-label='Functions' }

#### boolean IsInGame ( ) {: .copyable aria-label='Functions' }

如果 `Game` 不为 nil 且当前状态正确，则返回 `true`。

___

### LevelGeneratorEntry () {: aria-label='Functions' }

#### [LevelGeneratorEntry](LevelGeneratorEntry.md) LevelGeneratorEntry ( ) {: .copyable aria-label='Functions' }

创建一个新的空白 [LevelGeneratorEntry](LevelGeneratorEntry.md) 对象。

___

### MarkChallengeAsNotDone () {: aria-label='Functions' }

#### void MarkChallengeAsNotDone ( int challengeid ) {: .copyable aria-label='Functions' }

将挑战标记为未完成。

___

### PlayCutscene () {: aria-label='Functions' }

#### int PlayCutscene ( int ID, boolean ClearGameState = false ) {: .copyable aria-label='Functions' }

播放提供的 ID 对应的过场动画。使用 Isaac.GetCutsceneIdByName 来获取 ID，或者如果您愿意，也可以使用原版的枚举。

___
### RenderCollectionItem () {: aria-label='Functions' }
#### void RenderCollectionItem ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, [Vector](Vector.md) Position, [Vector](Vector.md) Scale = Vector.One, [Color](Color.md) Color = Color.Default ) {: .copyable aria-label='Functions' }
Renders item collection sprite from collection menu/death screen. 
___
### ReworkBirthright () {: aria-label='Functions' }
#### void ReworkBirthright ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) playerType ) {: .copyable aria-label='Functions' }
Marks the player's birthright as reworked, making the game not execute the item's original passive logic.
Can only be set during mod load.

___
### ReworkCollectible () {: aria-label='Functions' }
#### void ReworkCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) collectible ) {: .copyable aria-label='Functions' }
Marks the collectible as reworked, making the game not execute the item's original passive logic.
Can only be set during mod load.
**NOTE** Does not prevent the UseActiveItem logic from running.

___
### ReworkTrinket () {: aria-label='Functions' }
#### void ReworkTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) trinket ) {: .copyable aria-label='Functions' }
Marks the trinket as reworked, making the game not execute the trinket's original passive logic.
Can only be set during mod load.

___
### SetClipboard () {: aria-label='Functions' }

#### boolean SetClipboard ( string ClipboardData ) {: .copyable aria-label='Functions' }

将剪贴板的内容设置为提供的字符串。

___

### SetCompletionMark () {: aria-label='Functions' }

#### void SetCompletionMark ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character, [CompletionType](enums/CompletionType.md) Mark, int Value) {: .copyable aria-label='Functions' }

将角色的完成标记设置为匹配从 `0` 到 `2` 的特定值（0 = 未完成，1 = 普通，2 = 困难）。

___

### SetCompletionMarks () {: aria-label='Functions' }

#### void SetCompletionMarks ( table Marks ) {: .copyable aria-label='Functions' }

将角色的完成标记设置为匹配输入表。需要一个包含该角色所有标记的表，为了方便起见，建议从 [GetCompletionMarks](Isaac.md#getcompletionmarks) 获取该表。

???- info "Table structure & usage"

    该表具有以下字段:

    - PlayerType: containing the [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) asociated to the marks

    - Delirium: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - MegaSatan: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Mother: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - UltraGreed: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - BlueBaby: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - UltraGreedier: 困难贪婪模式,值2 ，大多冗余，无需设置
    - BossRush: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Beast: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Isaac: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Lamb: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - MomsHeart: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Hush: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Satan: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况

    ```lua
    local marks = Isaac.GetCompletionMarks(0) --getting the current table
    marks.MomsHeart = 2 --Isaac now will have the hard mark on MHeart
    marks.Satan = 1 --Isaac will now have the normal mark on Satan
    marks.BlueBaby = 0 --Removes the BlueBaby Mark if its present
    Isaac.SetCompletionMarks(marks) --Impacts the changes on the player
    ```

___

### SetCurrentFloorBackdrop () {: aria-label='Functions' }

#### void SetCurrentFloorBackdrop ( int BackdropId ) {: .copyable aria-label='Functions' }

将当前楼层的默认房间背景更改为匹配输入的 ID。此更改在保存/继续游戏时不会保留，因此请确保考虑到这一点。

___

### SetCurrentFloorMusic () {: aria-label='Functions' }

#### void SetCurrentFloorMusic ( int MusicId ) {: .copyable aria-label='Functions' }

将当前楼层的音乐曲目更改为匹配输入的 ID。此更改在保存/继续游戏时不会保留，因此请确保考虑到这一点。

___

### SetCurrentFloorName () {: aria-label='Functions' }

#### void SetCurrentFloorName ( string Name ) {: .copyable aria-label='Functions' }

将当前楼层的显示名称更改为匹配输入的 ID。此更改在保存/继续游戏时不会保留，因此请确保考虑到这一点。

### SetDwmWindowAttribute () {: aria-label='Functions' }

#### void SetDwmWindowAttribute ( [DwmWindowAttribute](enums/DwmWindowAttribute.md) Attribute ) {: .copyable aria-label='Functions' }

___

### SetIcon () {: aria-label='Functions' }

#### void SetIcon ( int IsaacIcon OR string IconPath, boolean BypassSize) {: .copyable aria-label='Functions' }

设置游戏窗口上的 16x16 图标。不会更新其他地方的图标，例如任务栏。
`IsaacIcon` 为 `0` 表示正常图标，`1` 表示受污染图标。
`IconPath` 接受一个 .ico 文件的路径。
`BypassSize` 绕过 16x16 分辨率限制。

___


### SetWindowTitle () {: aria-label='Functions' }

#### void SetWindowTitle ( string Title ) {: .copyable aria-label='Functions' }

设置游戏窗口标题上附加的文本。

___


### ShowErrorDialog () {: aria-label='Functions' }

#### [DialogReturn](enums/DialogReturn.md) ShowErrorDialog ( string Title, string Text, [DialogIcons](enums/DialogIcons.md) Icon = DialogIcons.ERROR, [DialogButtons](enums/DialogButtons.md) Buttons = DialogButtons.OK ) {: .copyable aria-label='Functions' }

显示一个 Win32 消息框。可以使用 `icon` 和 `buttons` 参数进行控制。返回一个 [`DialogReturn`](enums/DialogReturn.md) 值，表示按下的按钮。

???- info "Note"

    请记住，游戏手柄对此弹出窗口不起作用，您需要使用鼠标/键盘或触摸屏，并且在某些环境（如 Steam Deck）中窗口标题可能不会显示，因此不要过于依赖它。

___
### SpawnBoss () {: aria-label='Functions' }
#### [EntityNPC](EntityNPC.md) SpawnBoss ( int Type, int Variant, int SubType, [Vector](Vector.md) Position, [Vector](Vector.md) Velocity, [Entity](Entity.md) Spawner, int Seed = ? ) {: .copyable aria-label='Functions' }
Spawns an NPC forcing it to be a Boss, returning true for IsBoss(), giving it a boss bar, playing the boss end single on kill in appropiate rooms and other qualities that you may expect from a boss entity, even if the entity is normally not a Boss.

___
### StartNewGame () {: aria-label='Functions' }

#### void StartNewGame ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character, [Challenge](https://wofsauge.github.io/IsaacDocs/rep/enums/Challenge.html) Challenge = ChallengeType.CHALLENGE_NULL, [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) Mode = Difficulty.DIFFICULTY_NORMAL, int Seed = Random ) {: .copyable aria-label='Functions' }

使用指定的参数开始新游戏。可以从主菜单使用。

___

### TriggerWindowResize () {: aria-label='Functions' }

#### void TriggerWindowResize ( ) {: .copyable aria-label='Functions' }

模拟窗口大小调整，对于刷新一些选项更改（如 `MaxRenderScale`）很有用。

___
### UnClearChallenge () {: aria-label='Functions' }
#### void UnClearChallenge ( int challengeid) {: .copyable aria-label='Functions' }
Sets the challenge of the corresponding `challengeid` to not completed. While it does work with vanilla challenges, it is not recommended to use it on those, as there are no instances of challenges being uncompleted in vanilla, so it could lead to unexpected behaviour in specific scenarios. 

___
### WorldToMenuPosition () {: aria-label='Functions' }

#### [Vector](Vector.md) WorldToMenuPosition ( [MainMenu](enums/MainMenuType.md) MenuId, [Vector](Vector.md) Position ) {: .copyable aria-label='Functions' }

将输入的世界位置转换为固定的主菜单位置，该位置根据所选的枚举而变化。重要的是要像 WorldToRender 一样，每一帧都重新转换此位置，以便在菜单更改或窗口大小调整时正确渲染。

___