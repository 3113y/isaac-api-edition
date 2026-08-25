---
tags:
  - Class
---
# Class "EntityTear"

## Class Diagram
--8<-- "rgon/zh/snippets/EntityClassDiagram_NewFunkyMode.md"
## Modified Functions

### ResetSpriteScale () {: aria-label='Modified Functions' }
#### void ResetSpriteScale ( boolean Force = false ) {: .copyable aria-label='Modified Functions' }
现在接受一个 `Force` 参数，用于强制眼泪重新评估应该播放哪种眼泪缩放动画。

___
## Functions

### FireSplitTear () {: aria-label='Functions' }
#### [EntityTear](EntityTear.md) FireSplitTear ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity, float DamageMultiplier = 0.5, float SizeMultiplier = 0.6, int Variant = 0, [SplitTearType](enums/SplitTearType.md) splitType = SplitTearType.SPLIT_GENERIC ) {: .copyable aria-label='Functions' }
Fire a new tear that inherits many attributes from this tear (flags, damage, size, color, etc).

This will also trigger the `MC_POST_FIRE_SPLIT_TEAR` callback. For custom effects, a string may be passed in place of the [SplitTearType](enums/SplitTearType.md).

___
### GetDeadEyeIntensity () {: aria-label='Functions' }
#### float GetDeadEyeIntensity ( ) {: .copyable aria-label='Functions' }
返回眼泪因“死亡之眼”道具产生的强度值，该值介于 `0` 和 `1` 之间。

___
### GetDeadEyeSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetDeadEyeSprite ( ) {: .copyable aria-label='Functions' }
返回“死亡之眼”道具使用的红色光环精灵图。

___
### GetHitList () {: aria-label='Functions' }
#### int[] GetHitList ( ) {: .copyable aria-label='Functions' }
Returns an array of hit entities using their [Index](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#index) field.


___
### GetTearEffectSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetTearEffectSprite ( ) {: .copyable aria-label='Functions' }
返回像“火焰意志”和“神秘液体”等眼泪变体所使用的眼泪特效精灵图。

___
### GetTearHaloSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetTearHaloSprite ( ) {: .copyable aria-label='Functions' }
返回“神性”眼泪所使用的眼泪光晕精灵图。

___
### IsMultidimensionalTouched () {: aria-label='Functions' }
#### boolean IsMultidimensionalTouched ( ) {: .copyable aria-label='Functions' }
返回该眼泪是否是通过“多维宝宝”效果创建的。

___
### IsPrismTouched () {: aria-label='Functions' }
#### boolean IsPrismTouched ( ) {: .copyable aria-label='Functions' }
返回该眼泪是否是通过“天使棱镜”效果创建的。

___
### MakeMultidimensionalCopy () {: aria-label='Functions' }
#### [EntityTear](EntityTear.md) MakeMultidimensionalCopy ( ) {: .copyable aria-label='Functions' }
复制该眼泪并为其应用黑白效果，此效果与“多维宝宝”跟班所使用的效果相同。

___
### SetMultidimensionalTouched () {: aria-label='Functions' }
#### void SetMultidimensionalTouched ( boolean IsTouched ) {: .copyable aria-label='Functions' }
设置该眼泪是否是通过“天使棱镜”效果创建的。

___
### SetPrismTouched () {: aria-label='Functions' }
#### void SetPrismTouched ( boolean IsTouched ) {: .copyable aria-label='Functions' }
设置该眼泪是否是通过“天使棱镜”效果创建的。

___
### SetInitSound () {: aria-label='Functions' }
#### void SetInitSound ( [SoundEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/SoundEffect.html) SoundID ) {: .copyable aria-label='Functions' }
Sets the sound that will be automatically played when the tear is spawned. Can be set to `SoundEffect.SOUND_NULL` to make no sound play.

Should be set on [MC_POST_TEAR_INIT](https://wofsauge.github.io/IsaacDocs/rep/enums/ModCallbacks.html#mc_post_tear_init) or at any point prior to the tear's first Update, otherwise it will have no effect.

???-info "Example"
    ```lua
      ---Makes all tears play the Fart Sound on spawn
      ---@param tear EntityTear
      function mod:TearInit(tear)
          tear:SetInitSound(SoundEffect.SOUND_FART)
      end

      mod:AddCallback(ModCallbacks.MC_POST_TEAR_INIT, mod.TearInit)
    ```

___