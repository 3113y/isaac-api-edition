---
tags:
  - Class
---
# Class "Entity"

## Functions

### AddBaited () {: aria-label='Functions' }
#### void AddBaited ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, int Duration ) {: .copyable aria-label='Functions' }

___
### AddBleeding () {: aria-label='Functions' }
#### void AddBleeding ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, int Duration ) {: .copyable aria-label='Functions' }

___
### AddBrimstoneMark () {: aria-label='Functions' }
#### void AddBrimstoneMark ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, int Duration ) {: .copyable aria-label='Functions' }

___
### AddIce () {: aria-label='Functions' }
#### void AddIce ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, int Duration ) {: .copyable aria-label='Functions' }

___
### AddKnockback () 添加击退效果 {: aria-label='Functions' }
#### void AddKnockback ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, [Vector](Vector.md) PushDirection, int Duration, boolean TakeImpactDamage ) {: .copyable aria-label='Functions' }
???+ info "持续时间信息"

    持续时间最长为 0.5 秒/15 帧。

___
### AddMagnetized () {: aria-label='Functions' }
#### void AddMagnetized ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, int Duration ) {: .copyable aria-label='Functions' }

___
### AddWeakness () {: aria-label='Functions' }
#### void AddWeakness ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, int Duration ) {: .copyable aria-label='Functions' }

___
### CanDevolve () {: aria-label='Functions' }
#### boolean CanDevolve ( ) {: .copyable aria-label='Functions' }

___
### ClearHitList () {: aria-label='Functions' }
#### void ClearHitList ( ) {: .copyable aria-label='Functions' }
Clears the tear's hit list, allowing it to hit previously hit enemies again.

___
### ComputeStatusEffectDuration () {: aria-label='Functions' }
#### int ComputeStatusEffectDuration ( int InitialLength, [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source ) {: .copyable aria-label='Functions' }

___
### CopyStatusEffects () {: aria-label='Functions' }
#### void CopyStatusEffects ( [Entity](Entity.md) Target, boolean Overwrite = false ) {: .copyable aria-label='Functions' }
如果未指定 `Target`，则会将状态效果递归复制到所有 [子实体](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#child)。
`Overwrite` 还会移除目标的所有其他状态效果，并将现有效果的属性设置为与该实体匹配。

___
### ForceCollide () {: aria-label='Functions' }
#### boolean ForceCollide ( [Entity](Entity.md) Entity, boolean Force ) {: .copyable aria-label='Functions' }

如果应该 **跳过** 其余的碰撞逻辑，则返回 true；这可能是因为实体最初并未发生碰撞（如果 `Force` 为 false），

或者是因为其中一个实体的内部碰撞逻辑决定如此（这可能会受到 `PRE_COLLISION` 回调之一的影响）。

如果将 `Force` 设置为 false，那么游戏将在触发碰撞之前检查实体的 [EntityCollisionClass](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#entitycollisionclass) 是否兼容，以及两个实体是否都未 [Dead](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#isdead)。
???- warning "碰撞逻辑更改"

    某些实体类型在强制碰撞时，其碰撞逻辑会发生变化。
    例如：赌博机激活时不会让玩家支付常规费用。

___
### GetBaitedCountdown () {: aria-label='Functions' }
#### int GetBaitedCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetBleedingCountdown () {: aria-label='Functions' }
#### int GetBleedingCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetBossStatusEffectCooldown () {: aria-label='Functions' }
#### int GetBossStatusEffectCooldown ( ) {: .copyable aria-label='Functions' }

___
### GetBrimstoneMarkCountdown () {: aria-label='Functions' }
#### int GetBrimstoneMarkCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetBurnCountdown () {: aria-label='Functions' }
#### int GetBurnCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetBurnDamageTimer () {: aria-label='Functions' }
#### int GetBurnDamageTimer ( ) {: .copyable aria-label='Functions' }

___
### GetCharmedCountdown () {: aria-label='Functions' }
#### int GetCharmedCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetCollisionCapsule () {: aria-label='Functions' }
#### [Capsule](Capsule.md) GetCollisionCapsule ( [Vector](Vector.md) Vector ) {: .copyable aria-label='Functions' }

___
### GetColorParams () {: aria-label='Functions' }
#### [ColorParams](ColorParams.md)[] GetColorParams ( ) {: .copyable aria-label='Functions' }
返回由 `SetColor` 当前排队的所有颜色及其参数的表。

___
### GetConfusionCountdown () {: aria-label='Functions' }
#### int GetConfusionCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetDamageCountdown () {: aria-label='Functions' }
#### int GetDamageCountdown ( ) {: .copyable aria-label='Functions' }
请注意，这与玩家的 无敌帧数（`EntityPlayer:GetDamageCooldown()`） 不同。`DAMAGE_COUNTDOWN` [DamageFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html) 以及此关联的倒计时通常用于控制敌人从少数使用该标志的来源（如“彩虹独角兽”、“钉子”和“游戏掌机”的碰撞伤害效果）受到伤害的速度。

如果实体最近受到了带有 `DAMAGE_COUNTDOWN` [DamageFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html) 的伤害，则返回在它再次受到带有 `DAMAGE_COUNTDOWN` [DamageFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html) 的伤害之前还需要经过多少帧。

___
### GetDebugShape () {: aria-label='Functions' }
#### [Shape](renderer/Shape.md) GetDebugShape ( boolean Unknown ) {: .copyable aria-label='Functions' }

___
### GetEntityConfigEntity () {: aria-label='Functions' }
#### [EntityConfigEntity](EntityConfigEntity.md) GetEntityConfigEntity ( ) {: .copyable aria-label='Functions' }
返回此实体对应的 [EntityConfig](EntityConfig.md) 条目。

### GetFearCountdown () {: aria-label='Functions' }
#### int GetFearCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetFireDamageCooldown () {: aria-label='Functions' }
#### int GetFireDamageCooldown ( ) {: .copyable aria-label='Functions' }

___
### GetFreezeCountdown () {: aria-label='Functions' }
#### int GetFreezeCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetHitListIndex () {: aria-label='Functions' }
#### int GetHitListIndex ( ) {: .copyable aria-label='Functions' }
Returns an array of hit entities using their [Index](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#index) field.

___
### GetIceCountdown () {: aria-label='Functions' }
#### int GetIceCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetKnockbackCountdown () {: aria-label='Functions' }
#### int GetKnockbackCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetKnockbackDirection () {: aria-label='Functions' }
#### [Vector](Vector.md) GetKnockbackDirection ( ) {: .copyable aria-label='Functions' }

___
### GetMagnetizedCountdown () {: aria-label='Functions' }
#### int GetMagnetizedCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetMidasFreezeCountdown () {: aria-label='Functions' }
#### int GetMidasFreezeCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetMinecart () {: aria-label='Functions' }
#### [EntityNPC](EntityNPC.md) GetMinecart ( ) {: .copyable aria-label='Functions' }
返回实体所乘坐的矿车。

???+ note "返回行为"

    如果实体没有乘坐矿车，则此函数返回 `nil`。

___
### GetNullCapsule () {: aria-label='Functions' }
#### [Capsule](Capsule.md) GetNullCapsule ( string NullLayerName ) {: .copyable aria-label='Functions' }

___
### GetNullOffset () {: aria-label='Functions' }
#### [Vector](Vector.md) GetNullOffset ( string NullLayerName ) {: .copyable aria-label='Functions' }
返回空图层标记的位置。或者，如果图层不可见、当前动画没有可用帧或由于其他未知原因，则返回 `Vector.Zero`。

### GetPauseTime () {: aria-label='Functions' }
#### int GetPauseTime ( ) {: .copyable aria-label='Functions' }

___
### GetPoisonCountdown () {: aria-label='Functions' }
#### int GetPoisonCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetPoisonDamageTimer () {: aria-label='Functions' }
#### int GetPoisonDamageTimer ( ) {: .copyable aria-label='Functions' }

___
### GetPosVel () {: aria-label='Functions' }
#### [PosVel](https://wofsauge.github.io/IsaacDocs/rep/PlayerTypes_PosVel.html) GetPosVel ( ) {: .copyable aria-label='Functions' }
返回 2 个值，均为向量。第一个是实体的位置，第二个是实体的速度。

### GetPredictedTargetPosition () {: aria-label='Functions' }
#### [Vector](Vector.md) GetPredictedTargetPosition ( [Entity](Entity.md) Target, float Delay ) {: .copyable aria-label='Functions' }
预测值是目标的当前位置加上其速度乘以该实体与目标之间的距离。
`Delay` 用作预测提前量的乘数。例如，`1.0` 会预测目标的速度在下一次更新时会将其置于何处。

___
### GetShadowSize () {: aria-label='Functions' }
#### float GetShadowSize ( ) {: .copyable aria-label='Functions' }

___
### GetShrinkCountdown () {: aria-label='Functions' }
#### int GetShrinkCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetSlowingCountdown () {: aria-label='Functions' }
#### int GetSlowingCountdown ( ) {: .copyable aria-label='Functions' }

___
### GetSpeedMultiplier () {: aria-label='Functions' }
#### float GetSpeedMultiplier ( ) {: .copyable aria-label='Functions' }
???+ warning "弃用通知"

    此变量实际上是实体的时间缩放比例。未来版本中将添加一个命名更合适的替代函数。

___
### GetType () {: aria-label='Functions' }
#### [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) GetType ( ) {: .copyable aria-label='Functions' }

___
### GetWaterClipFlags () {: aria-label='Functions' }
#### [WaterClipFlag](enums/WaterClipFlag.md) GetWaterClipFlags ( ) {: .copyable aria-label='Functions' }
Gets a bitset that informs some of how this entity interacts with water, primarily rendering related (reflections, etc).

___
### GetWeaknessCountdown () {: aria-label='Functions' }
#### int GetWeaknessCountdown ( ) {: .copyable aria-label='Functions' }

___
### GiveMinecart () {: aria-label='Functions' }
#### [EntityNPC](EntityNPC.md) GiveMinecart ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity ) {: .copyable aria-label='Functions' }

___
### IgnoreEffectFromFriendly () {: aria-label='Functions' }
#### boolean IgnoreEffectFromFriendly ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source ) {: .copyable aria-label='Functions' }
用于确定此实体是否应忽略来自 `Source` 的任何状态效果。

___
### MakeBloodPoof () {: aria-label='Functions' }
#### [EntityEffect](EntityEffect.md) MakeBloodPoof ( [Vector](Vector.md) Position = self.Position, [Color](Color.md) Color = default, float Scale = 1.0 ) {: .copyable aria-label='Functions' }
此函数会生成两个子类型为 3 和 4 的血溅效果；返回的第二个效果将是第一个效果的子效果。

___
### MakeGroundPoof () {: aria-label='Functions' }
#### [EntityEffect](EntityEffect.md) MakeGroundPoof ( [Vector](Vector.md) Position = self.Position, [Color](Color.md) Color = default, float Scale = 1.0 ) {: .copyable aria-label='Functions' }
此函数会生成两个子类型为 1 和 2 的灰尘飞溅效果；返回的第二个效果将是第一个效果的子效果。

___
### ResetWaterClipFlags () {: aria-label='Functions' }
#### void ResetWaterClipFlags ( ) {: .copyable aria-label='Functions' }
Restores water rendering to the default vanilla state. See `SetWaterClipFlags()`.

___
### SetBaitedCountdown () {: aria-label='Functions' }
#### void SetBaitedCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SetBleedingCountdown () {: aria-label='Functions' }
#### void SetBleedingCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SetBossStatusEffectCooldown () {: aria-label='Functions' }
#### void SetBossStatusEffectCooldown ( int Cooldown ) {: .copyable aria-label='Functions' }

___
### SetBrimstoneMarkCountdown () {: aria-label='Functions' }
#### void SetBrimstoneMarkCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SetBurnCountdown () {: aria-label='Functions' }
#### void SetBurnCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SetBurnDamageTimer () {: aria-label='Functions' }
#### void SetBurnDamageTimer ( int Timer ) {: .copyable aria-label='Functions' }

___
### SetCharmedCountdown () {: aria-label='Functions' }
#### void SetCharmedCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SetColorParams () {: aria-label='Functions' }
#### void SetColorParams ( [ColorParams](ColorParams.md)[] Params ) {: .copyable aria-label='Functions' }
设置要使用的颜色及其参数。

___
### SetConfusionCountdown () {: aria-label='Functions' }
#### void SetConfusionCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SetDamageCountdown () {: aria-label='Functions' }
#### void SetDamageCountdown ( int countdown ) {: .copyable aria-label='Functions' }
请注意，这与玩家的无敌帧数（`EntityPlayer:GetDamageCooldown()`）不同。`DAMAGE_COUNTDOWN` [DamageFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html) 以及此关联的倒计时通常用于控制敌人从少数使用该标志的来源（如“彩虹独角兽”、“钉子”和“游戏掌机”的碰撞伤害效果）受到伤害的速度。

设置实体在受到带有 `DAMAGE_COUNTDOWN` [DamageFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html) 的伤害之前必须经过的帧数。

___
### SetDead () {: aria-label='Functions' }
#### void SetDead ( boolean IsDead ) {: .copyable aria-label='Functions' }

___
### SetFearCountdown () {: aria-label='Functions' }
#### void SetFearCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SetFireDamageCooldown () {: aria-label='Functions' }
#### void SetFireDamageCooldown ( int Cooldown ) {: .copyable aria-label='Functions' }

___
### SetFreezeCountdown () {: aria-label='Functions' }
#### void SetFreezeCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SetIceCountdown () {: aria-label='Functions' }
#### void SetIceCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SetInvincible () {: aria-label='Functions' }
#### void SetInvincible ( boolean IsInvincible ) {: .copyable aria-label='Functions' }

___
### SetKnockbackCountdown () {: aria-label='Functions' }
#### void SetKnockbackCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SetKnockbackDirection () {: aria-label='Functions' }
#### void SetKnockbackDirection ( [Vector](Vector.md) Direction ) {: .copyable aria-label='Functions' }

___
### SetMagnetizedCountdown () {: aria-label='Functions' }
#### void SetMagnetizedCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SetMidasFreezeCountdown () {: aria-label='Functions' }
#### void SetMidasFreezeCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SetPauseTime () {: aria-label='Functions' }
#### void SetPauseTime ( int Duration ) {: .copyable aria-label='Functions' }

___
### SetPoisonCountdown () {: aria-label='Functions' }
#### void SetPoisonCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SetPoisonDamageTimer () {: aria-label='Functions' }
#### void SetPoisonDamageTimer ( int Timer ) {: .copyable aria-label='Functions' }

___
### SetShadowSize () {: aria-label='Functions' }
#### float SetShadowSize ( float Size ) {: .copyable aria-label='Functions' }

___
### SetShrinkCountdown () {: aria-label='Functions' }
#### void SetShrinkCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SetSlowingCountdown () {: aria-label='Functions' }
#### void SetSlowingCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SetSpeedMultiplier () {: aria-label='Functions' }
#### void SetSpeedMultiplier ( float Amount ) {: .copyable aria-label='Functions' }
???+ warning "弃用通知"

    此变量实际上是实体的时间缩放比例。未来版本中将添加一个命名更合适的替代函数。

___
### SetWaterClipFlags () {: aria-label='Functions' }
#### void SetWaterClipFlags ( [WaterClipFlag](enums/WaterClipFlag.md) Flags ) {: .copyable aria-label='Functions' }
Allows modification of how this entity interacts with water, primarily rendering related behaviour such as reflections.

Note that this will also override/disable any natural vanilla changes to these flags, such as the player losing their reflection with Charm of the Vampire.

Vanilla state can be restored with `ResetWaterClipFlags()`.

___
### SetWeaknessCountdown () {: aria-label='Functions' }
#### void SetWeaknessCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
### SpawnBloodEffect () {: aria-label='Functions' }
#### [EntityEffect](EntityEffect.md) SpawnBloodEffect ( int SubType = 0, [Vector](Vector.md) position = self.Position, [Vector](Vector.md) Offset = Vector.Zero, [Color](Color.md) Color = Default, [Vector](Vector.md) Velocity = Vector.Zero ) {: .copyable aria-label='Functions' }

___
### SpawnWaterImpactEffects () {: aria-label='Functions' }
#### void SpawnWaterImpactEffects ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity = Vector.Zero, float Strength ) {: .copyable aria-label='Functions' }
???+ warning "Warning"

    仅当房间的 [水量](Room.md#getwateramount) 大于或等于 `0.2` 时，此函数才会生成效果。

___
### TeleportToRandomPosition () {: aria-label='Functions' }
#### void TeleportToRandomPosition ( ) {: .copyable aria-label='Functions' }

___
### ToDelirium () {: aria-label='Functions' }
#### [EntityDelirium](EntityDelirium.md) ToDelirium ( ) {: .copyable aria-label='Functions' }
将 [Entity](Entity.md) 用户数据转换为 [EntityDelirium](EntityDelirium.md) 用户数据。
仅当源实体是幻痛（以其正常形态或变形形态）的实例时，转换才会成功。

???+ note "返回行为"

    如果转换失败，此函数返回 `nil`。

___
### ToSlot () {: aria-label='Functions' }
#### [EntitySlot](EntitySlot.md) ToSlot ( ) {: .copyable aria-label='Functions' }
用于将 [Entity](Entity.md) 对象转换为 [EntitySlot](EntitySlot.md) 对象。

???+ note "返回行为"

    如果转换不成功，此函数返回 `nil`。

___
### TryThrow () {: aria-label='Functions' }
#### boolean TryThrow ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, [Vector](Vector.md) ThrowDirection, float Force ) {: .copyable aria-label='Functions' }

___
