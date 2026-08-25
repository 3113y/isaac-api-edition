---
tags:
  - Class
---
# Class "EntityDelirium"

## Functions

### GetTeleportationTimer () {: aria-label='Functions' }
#### int GetTeleportationTimer ( ) {: .copyable aria-label='Functions' }
返回精神错乱（Delirium）变身前的帧数.

___
### IsRedMode () {: aria-label='Functions' }
#### boolean IsRedMode ( ) {: .copyable aria-label='Functions' }
返回一个布尔值，指示精神错乱是否“变红”.

???+ info "About red mode"

    红色模式是精神错乱战斗中的一种机制，在该模式下，精神错乱的精灵会被染成红色，详见 [Wiki](https://isaac.huijiwiki.com/wiki/%E5%AE%9E%E4%BD%93/412#412.0.0).

___
### SetRedMode () {: aria-label='Functions' }
#### void SetRedMode ( boolean On ) {: .copyable aria-label='Functions' }
根据参数 `on` 启用或禁用红色模式.

???+ info "About red mode"

    有关红色模式的解释，请参考 [IsRedMode](EntityDelirium.md) 文档中的注释.

___
### SetTeleportationTimer () {: aria-label='Functions' }
#### void SetTeleportationTimer ( int Timer ) {: .copyable aria-label='Functions' }
设置精神错乱传送前的帧数。不允许使用负值.

___
### Transform () {: aria-label='Functions' }
#### void Transform ( int Type, int Variant = 0 ) {: .copyable aria-label='Functions' }
将精神错乱转变为具有指定`type`和`variant`的实体.

???+ warn "Warning"

    类型和变体的验证强度仅与游戏尝试转变精神错乱时所执行的验证强度相同。
    换句话说，这与游戏本身尝试转变精神错乱的行为完全相同，包括指定实体无效时所隐含的一切情况。

???+ warn "Warning"

    为了正确处理转变，我们使用了精神错乱的原生转变机制。 
    因此，转变不会立即生效，而是在下一帧生效。 
    从内部实现来看，此函数会将转变计时器强制设置为 1 帧，并让精神错乱的 AI 按需更新。

___
### Angle {: aria-label='Variables' }
#### int8 Angle {: .copyable aria-label='Variables' }
精神错乱发射的弹幕的角度. 

???+ warn "Geometric system"

    此变量是一个 8 位整数，因此允许的值是从 0 到 255（含）的整数。
    你可以使用 \[0: 255] 和 \[0: 360] 范围之间的线性插值，将角度从度数转换为这个系统。

???+ info "WTH"

    精神错乱的所有弹幕地狱模式都可以受此变量影响。与大多数首领不同，精神错乱不会将其弹幕瞄准玩家，而是向随机方向发射（有一定控制以防止出现“荒谬”的模式）。
    例如，如果精神错乱在其周围发射 8 颗眼泪，并且 `Angle` 设置为 0，则这 8 颗眼泪将沿基本方向和斜向方向发射。如果 `Angle` 设置为 32，则所有眼泪将旋转 45°。
    我不知道为什么 Nicalis 使用 8 位整数来表示角度（对精神错乱的内存布局进行分析表明，使用 32 位浮点数不会有任何区别）。

___
### AttackID {: aria-label='Variables' }
#### int AttackID {: .copyable aria-label='Variables' }
精神错乱用于识别其当前正在执行的弹幕地狱模式的内部 [I1](https://wofsauge.github.io/IsaacDocs/rep/EntityNPC.html#I1) 值。

___
### BossType {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge }
#### const int BossType {: .copyable aria-label='Variables' }
精神错乱当前所转变为的首领的 [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html).

___
### BossVariant {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge }
#### const int BossVariant {: .copyable aria-label='Variables' }
精神错乱当前所转变为的首领的 Variant.

___
### Cycle {: aria-label='Variables' }
#### int Cycle {: .copyable aria-label='Variables' }
精神错乱用于识别红色模式是否激活以及传送前剩余时间的内部 [I2](https://wofsauge.github.io/IsaacDocs/rep/EntityNPC.html#I2) 值。
你不应直接使用此变量，而应依赖 [GetTeleportationTimer](EntityDelirium.md#getteleportationtimer)、[SetTeleportationTimer](EntityDelirium.md#setteleportationtimer)、[IsRedMode](EntityDelirium.md#isredmode) 和 [SetRedMode](EntityDelirium.md#setredmode) 函数。
直接使用此变量的唯一原因是，如果你想将其冻结为一个你知道会产生预期效果的值（例如，禁用红色模式并防止传送）。

???+ info "Format of the variable"

    此变量为 32 位宽，结构如下：第 0 到 6 位（含）未知，第 7 到 14 位（含）指示红色模式是否激活（如果任何一位被设置，则表示激活），第 15 到 25 位（含）是传送计时器。


???+ info "Preservation of state"

    上述用于操作此变量的方法会保留与所执行操作无关的变量位。
    例如，启用或禁用红色模式不会更改转变计时器。 

___
### RemainingAttacks {: aria-label='Variables' }
#### int RemainingAttacks {: .copyable aria-label='Variables' }
精神错乱转变为另一个首领之前剩余的攻击次数.

???+ info "About remaining attacks" 

    此变量是 Nicalis 为防止精神错乱在转变为另一个首领之前作为单个首领执行过多攻击而采取的措施。
    在某些条件下，游戏会将此值减 1。如果该值达到 0，则无论转变计时器的值如何，精神错乱都会转变。
    必须同时满足的条件是：当前帧的 [StateFrame](https://wofsauge.github.io/IsaacDocs/rep/EntityNPC.html#stateframe) 变量必须为 1，并且 [State](https://wofsauge.github.io/IsaacDocs/rep/EntityNPC.md#state) 变量必须设置为任何攻击状态。
    这就是为什么精神错乱有时会作为一个首领发起攻击并立即转变的原因。 
    你可以参考 [首领 AI 配置的完整明细](https://wofsauge.github.io/IsaacDocs/rep/customData/bosses.xlsx) 来查看每个攻击的 AI 配置。

___
### StateD {: aria-label='Variables' }
#### [NpcState](https://wofsauge.github.io/IsaacDocs/rep/enums/NpcState.html) StateD {: .copyable aria-label='Variables' }
精神错乱的内部 [State](https://wofsauge.github.io/IsaacDocs/rep/EntityNPC.html#State)。

___
### TransformationTimer {: aria-label='Variables' }
#### int TransformationTimer {: .copyable aria-label='Variables' }
获取或设置精神错乱转变为另一个首领之前的剩余时间。

???+ warn "On transformations" 

    精神错乱可以在两种情况下转变：要么此值达到 0，要么 [RemainingAttacks](EntityDelirium.md#remainingattacks) 的值达到 0。 
    有关该机制的更详细解释，请参考 [RemainingAttacks](EntityDelirium.md#remainingattacks) 的文档
    
___