---
tags:
  - Class
---
# Class "EntitySlot"

It's Real.

## Class Diagram
--8<-- "rgon/zh/snippets/EntityClassDiagram_NewFunkyMode.md"
## Functions

### CreateDropsFromExplosion () {: aria-label='Functions' }
#### void CreateDropsFromExplosion ( ) {: .copyable aria-label='Functions' }
这会强制实体可互动实体（EntitySlot）掉落其在被炸时通常会掉落的物品。

___
### GetDonationValue () {: aria-label='Functions' }
#### int GetDonationValue ( ) {: .copyable aria-label='Functions' }
返回给予乞丐的硬币数量。返回的数字会根据乞丐的不同而有所变化。

???- info "Return info"

    - 普通乞丐：已捐赠的硬币数量。
    - 恶魔乞丐：已捐赠的红心数量。
    - 电池乞丐、腐烂乞丐：每次支付时随机增加，最多增加到3，在给予奖励或支付报酬后重置为0。
    - 所有其他可互动实体：保持为0。

___
### GetPrizeCollectible () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetPrizeCollectible ( ) {: .copyable aria-label='Functions' }
似乎仅由夹娃娃机和赌命乞丐使用。获取获胜时作为奖品颁发的收藏品。

___
### GetPrizeType () {: aria-label='Functions' }
#### int GetPrizeType ( ) {: .copyable aria-label='Functions' }
返回一个根据赌博机不同而变化的整数。

???- info "Return info"

    - 赌博机：返回一个介于`3` - `24`之间的数字。`3` - `12`会使可互动实体吐出奖励。
        - `3`：苍蝇或漂亮苍蝇。
        - `4`：炸弹。
        - `5` - `6`：红心。
        - `7`：钥匙。
        - `8`：药丸。
        - `9`：未知。此值似乎从未被使用过。
        - `10` - `12`：1 - 2枚硬币。
        - `13` - `24`：无奖励。
    - 赌博乞丐和赌命乞丐：返回潜在奖品的`拾取物变体（PickupVariant）`。 
    - 炸弹乞丐：根据其输出的奖品类型返回一个介于`1` - `3`之间的数字。
        - `1`：硬币。
        - `2`：红心。
        - `3`：收藏品。

___
### GetShellGameAnimationIndex () {: aria-label='Functions' }
#### int GetShellGameAnimationIndex ( ) {: .copyable aria-label='Functions' }
返回赌博乞丐和赌命乞丐用于确定播放哪个奖品动画的索引。

___
### GetState () {: aria-label='Functions' }
#### [SlotState](enums/SlotState.md) GetState ( ) {: .copyable aria-label='Functions' }
返回可互动实体的当前状态。

???+ info "Return info"

    所有可互动实体都有一个基于其当前行为的一致状态，具体如下：
    - `1`：闲置。
    - `2`：奖励（赌博乞丐和赌命乞丐：闲置奖励状态）
    - `3`：被炸
    - `4`：支付报酬
    - `5`：奖励（仅适用于赌博乞丐和赌命乞丐）

___
### GetTimeout () {: aria-label='Functions' }
#### int GetTimeout ( ) {: .copyable aria-label='Functions' }
返回可互动实体确定其奖品之前的超时帧数。并非所有可互动实体都会使用此功能。

???- info "Return info"

    - 除炸弹乞丐外的所有乞丐：每次支付时随机增加，返回`1 << 16`、`1 << 17`或它们的和，在给予奖励后重置为0。
    - 夹娃娃机：第一次成功支付报酬时，最小超时时间为`1 << 16`，仍会增加30并开始倒计时。第二次支付报酬时为`1 << 17`。第三次支付报酬时为`1 << 16` + `1 << 17`。
    - 所有其他可互动实体：保持为0。

___
### GetTouch () {: aria-label='Functions' }
#### int GetTouch ( ) {: .copyable aria-label='Functions' }
返回可互动实体的触摸计数器。当玩家触摸可互动实体时，触摸计数器每帧增加1，当没有玩家触摸时重置。

___
### GetTriggerTimerNum () {: aria-label='Functions' }
#### int GetTriggerTimerNum ( ) {: .copyable aria-label='Functions' }
返回炸弹乞丐和补货机使用的一个数字。

???+ note "Return info"

    炸炸弹乞丐时，此值会被设置为`30`。
    补货机每次成功生效时将此值增加`1`。被炸时，有机会将其设置为11并重新生成另一个物品。

___
### RandomCoinJamAnim () {: aria-label='Functions' }
#### string RandomCoinJamAnim ( ) {: .copyable aria-label='Functions' }
从以下选项中返回一个随机字符串：`CoinJam`、`CoinJam2`、`CoinJam3`、`CoinJam4`。推测仅用于捐赠可互动实体。

___
### SetDonationValue () {: aria-label='Functions' }
#### void SetDonationValue ( int DonationValue ) {: .copyable aria-label='Functions' }
设置可互动实体的捐赠值。更多信息请参阅[GetDonationValue](EntitySlot.md#getdonationvalue)。

___
### SetPrizeCollectible () {: aria-label='Functions' }
#### void SetPrizeCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) {: .copyable aria-label='Functions' }
似乎仅由夹娃娃机和赌命乞丐使用。此函数设置游戏将支付的收藏品，并相应地更新渲染的收藏品。

___
### SetPrizeType () {: aria-label='Functions' }
#### void SetPrizeType ( int PrizeType ) {: .copyable aria-label='Functions' }
设置可互动实体的奖品类型。更多信息请参阅[GetPrizeType](EntitySlot.md#getprizetype)。

___
### SetShellGameAnimationIndex () {: aria-label='Functions' }
#### void SetShellGameAnimationIndex ( int index ) {: .copyable aria-label='Functions' }
设置赌博乞丐和赌命乞丐用于确定播放哪个奖品动画的索引。

___
### SetState () {: aria-label='Functions' }
#### void SetState ( [SlotState](enums/SlotState.md) State ) {: .copyable aria-label='Functions' }
设置可互动实体的状态。更多信息请参阅[GetState](EntitySlot.md#getstate)。

___
### SetTimeout () {: aria-label='Functions' }
#### void SetTimeout ( int Timeout ) {: .copyable aria-label='Functions' }
设置可互动实体的超时时间。更多信息请参阅[GetTimeout](EntitySlot.md#gettimeout)。

___
### SetTouch () {: aria-label='Functions' }
#### void SetTouch ( int Touch ) {: .copyable aria-label='Functions' }
设置可互动实体的触摸计数器。当玩家触摸可互动实体时，触摸计数器每帧增加1，当没有玩家触摸时重置为0。

___
### SetTriggerTimerNum () {: aria-label='Functions' }
#### void SetTriggerTimerNum ( int num ) {: .copyable aria-label='Functions' }
返回炸弹乞丐和补货机使用的一个数字。

???+ note "More Info"

    补货机每次成功生效时将此值增加`1`。被炸时，有机会将其设置为11并重新生成另一个物品。
    轰炸炸弹乞丐时，此值会被设置为`30`。

___