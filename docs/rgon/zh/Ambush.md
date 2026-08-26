---
tags:
  - Global
  - Class
---
# Global Class "Ambush"

???+ info

    你可以通过 `Ambush` 全局表访问此类。

    **注意：调用这些函数时，必须使用 `.`（句点）而非 `:`（冒号）！**
    
    ???+ example "Example Code"

        ```lua
        local currwave = Ambush.GetCurrentWave()
        ```
        
## Functions

### GetCurrentWave () {: aria-label='Functions' }
#### int GetCurrentWave ( ) {: .copyable aria-label='Functions' }
返回当前挑战房或 Boss 冲刺房的波数。

___
### GetMaxBossChallengeWaves () {: aria-label='Functions' }
#### int GetMaxBossChallengeWaves ( ) {: .copyable aria-label='Functions' }
返回 Boss 挑战房的最大波数。

默认情况下，Boss 挑战房的最大波数为 `2`。模组可以修改此最大值。

___
### GetMaxBossrushWaves () {: aria-label='Functions' }
#### int GetMaxBossrushWaves ( ) {: .copyable aria-label='Functions' }
返回 Boss 冲刺的最大波数。

默认情况下，Boss 冲刺的最大波数为 `15`。模组可以修改此最大值。

___
### GetMaxChallengeWaves () {: aria-label='Functions' }
#### int GetMaxChallengeWaves ( ) {: .copyable aria-label='Functions' }
返回挑战房的最大波数。

默认情况下，挑战房的最大波数为 `3`。模组可以修改此最大值。

___
### GetNextWave () {: aria-label='Functions' }
#### [RoomConfigRoom](RoomConfigRoom.md) GetNextWave ( ) {: .copyable aria-label='Functions' }
返回下一波挑战房的 [RoomConfigRoom](RoomConfigRoom.md)。在挑战房外调用此函数将导致错误。

___
### GetNextWaves () {: aria-label='Functions' }
#### [RoomConfigRoom](RoomConfigRoom.md)[] GetNextWaves ( ) {: .copyable aria-label='Functions' }
返回一个包含接下来几波挑战房 [RoomConfigRoom](RoomConfigRoom.md) 的表。

___
### SetMaxBossChallengeWaves () {: aria-label='Functions' }
#### void SetMaxBossChallengeWaves ( int Waves ) {: .copyable aria-label='Functions' }
设置Boss挑战房的最大波数。

???+ bug "Bug"

    目前，此值在游戏重启时不会重置。一旦我们弄清楚如何在C++端的初始化时干净利落地运行代码，这个问题就会得到修复！

### SetMaxBossrushWaves () {: aria-label='Functions' }
#### void SetMaxBossrushWaves ( int Waves ) {: .copyable aria-label='Functions' }
设置Boss冲刺的最大波数。截至目前，最大波数上限为 `25` 波。

___
### SetMaxChallengeWaves () {: aria-label='Functions' }
#### void SetMaxChallengeWaves ( int Waves ) {: .copyable aria-label='Functions' }
设置挑战房的最大波数。

???+ bug "Bug"

    目前，此值在游戏重启时不会重置。一旦我们弄清楚如何在C++端的初始化时干净利落地运行代码，这个问题就会得到修复！

___
### SpawnBossrushWave () {: aria-label='Functions' }
#### void SpawnBossrushWave ( ) {: .copyable aria-label='Functions' }
在当前房间生成一波Boss冲刺。

???+ bug "Bug"

    除非在当前游戏会话中至少触发过一次Boss冲刺，否则调用此函数将不会有任何效果。

___
### SpawnWave () {: aria-label='Functions' }
#### void SpawnWave ( ) {: .copyable aria-label='Functions' }
生成与当前楼层相关的挑战房波次。

???+ bug "Bug"

    如果当前楼层是蓝子宫，游戏也会崩溃。
    如果当前游戏模式是贪婪模式或更贪婪模式，调用此函数会导致游戏崩溃。

___
### StartChallenge () {: aria-label='Functions' }
#### void StartChallenge ( ) {: .copyable aria-label='Functions' }
触发挑战房或Boss冲刺。

???+ bug "Bug"

    在Boss冲刺房或挑战房外调用此函数除了会永久关闭门之外不会有任何效果，从而导致软锁定。

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
