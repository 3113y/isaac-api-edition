# Enum "ModCallbacks"

This is a list of all new callbacks added by REPENTOGON.

## Modified Old Callbacks
### MC_USE_PILL

`MC_USE_PILL` 现在会将 `PillColor` 作为参数传递。
不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|10 |MC_USE_PILL {: .copyable } | ([PillEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/PillEffect.html) Effect, [EntityPlayer](../EntityPlayer.md) Player, [UseFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/UseFlags.html) Flags, [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) Color) | [PillEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/PillEffect.html) | void |

### MC_POST_PICKUP_SELECTION

`MC_POST_PICKUP_COLLISION` 现在会传递 **请求的变体** 和 **请求的子类型** 以及 **随机数生成器（RNG）**。
**请求的变体** 和 **请求的子类型** 表示生成实体时设置的变体和子类型。

返回表中添加了第三个可选的 `Continue` 参数。
如果设置为 `true`，回调将用指定的值替换 `Variant` 和 `SubType` 参数并继续运行。

这些更改旨在使此回调成为处理拾取物池的可行选项。

???+ info "使用方法"
    在内部，游戏总是尝试对生成的拾取物的变体和子类型进行随机化，即使重新进入已经访问过的房间也是如此，但是有一些检查机制确保只有当这些值最初设置为 0 时才会进行随机化。

    因此，任何回调在尝试进行任何修改之前都应该检查 `if RequestedVariant == 0 or RequestedSubType == 0`。

    除非期望的效果类似于愚人节的“所有镍币都是粘性镍币”效果，该效果无论上述限制如何都会应用。

???+ info "Requested Variant == 0"
    当 **请求的变体** 等于 0 时，游戏将对拾取物的 `Variant` 和 `SubType` 进行随机化。在这种情况下，**请求的子类型** 的值将用作变体黑名单。

    这个黑名单列在 [NullPickupSubType](NullPickupSubType.md) 枚举中。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|37 |MC_POST_PICKUP_SELECTION {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup, <br>[PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) Variant, <br>int SubType, <br>[PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) RequestedVariant, <br>int RequestedSubType, <br>[RNG](../RNG.md) RNG ) | - | table |

### MC_PRE_PLAYER_COLLISION

现在可以选择返回一个表，该表可以包含以下任意组合的字段：

* `Collide`：设置为 `true` 以强制实体进行物理碰撞（相互推开），除非“碰撞者”忽略碰撞。设置为 `false` 以忽略物理碰撞，但不一定跳过碰撞效果。
* `SkipCollisionEffects`：设置为 `true` 以跳过此实体的碰撞代码，例如造成碰撞伤害。不影响物理碰撞。不会跳过“碰撞者”的碰撞代码。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|33 |MC_PRE_PLAYER_COLLISION {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [Entity](../Entity.md) Collider, boolean Low) | [PlayerVariant](PlayerVariant.md) | boolean or table |

### MC_PRE_TEAR_COLLISION

现在可以选择返回一个表，该表可以包含以下任意组合的字段：

* `Collide`：设置为 `true` 以强制实体进行物理碰撞（相互推开），除非“碰撞者”忽略碰撞。设置为 `false` 以忽略物理碰撞，但不一定跳过碰撞效果。
* `SkipCollisionEffects`：设置为 `true` 以跳过此实体的碰撞代码，例如造成碰撞伤害。不影响物理碰撞。不会跳过“碰撞者”的碰撞代码。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|42 |MC_PRE_TEAR_COLLISION {: .copyable } | ([EntityTear](../EntityTear.md) Tear, [Entity](../Entity.md) Collider, boolean Low) | [TearVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/TearVariant.html) | boolean or table |

### MC_PRE_FAMILIAR_COLLISION

现在可以选择返回一个表，该表可以包含以下任意组合的字段：

* `Collide`：设置为 `true` 以强制实体进行物理碰撞（相互推开），除非“碰撞者”忽略碰撞。设置为 `false` 以忽略物理碰撞，但不一定跳过碰撞效果。
* `SkipCollisionEffects`：设置为 `true` 以跳过此实体的碰撞代码，例如造成碰撞伤害。不影响物理碰撞。不会跳过“碰撞者”的碰撞代码。

例如，你可以返回 `{ Collide=true }` 以使一个跟班与某物（如敌人，通常跟班不会与敌人进行物理碰撞）进行物理碰撞，而不跳过碰撞代码（如果你返回 `false` 则会跳过）。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|26 |MC_PRE_FAMILIAR_COLLISION {: .copyable } | ([EntityFamiliar](../EntityFamiliar.md) Familiar, [Entity](../Entity.md) Collider, boolean Low) | [FamiliarVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/FamiliarVariant.html) | boolean or table |

### MC_PRE_BOMB_COLLISION

现在可以选择返回一个表，该表可以包含以下任意组合的字段：

* `Collide`：设置为 `true` 以强制实体进行物理碰撞（相互推开），除非“碰撞者”忽略碰撞。设置为 `false` 以忽略物理碰撞，但不一定跳过碰撞效果。
* `SkipCollisionEffects`：设置为 `true` 以跳过此实体的碰撞代码，例如造成碰撞伤害。不影响物理碰撞。不会跳过“碰撞者”的碰撞代码。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|60 |MC_PRE_BOMB_COLLISION {: .copyable } | ([EntityBomb](../EntityBomb.md) Bomb, [Entity](../Entity.md) Collider, boolean Low) | [BombVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/BombVariant.html) | boolean or table |

### MC_PRE_PICKUP_COLLISION

现在可以选择返回一个表，该表可以包含以下任意组合的字段：

* `Collide`：设置为 `true` 以强制实体进行物理碰撞（相互推开），除非“碰撞者”忽略碰撞。设置为 `false` 以忽略物理碰撞，但不一定跳过碰撞效果。
* `SkipCollisionEffects`：设置为 `true` 以跳过此实体的碰撞代码，例如造成碰撞伤害。不影响物理碰撞。不会跳过“碰撞者”的碰撞代码。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|38 |MC_PRE_PICKUP_COLLISION {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup, [Entity](../Entity.md) Collider, boolean Low) | [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) | boolean or table |

### MC_PRE_KNIFE_COLLISION

现在可以选择返回一个表，该表可以包含以下任意组合的字段：

* `Collide`：设置为 `true` 以强制实体进行物理碰撞（相互推开），除非“碰撞者”忽略碰撞。设置为 `false` 以忽略物理碰撞，但不一定跳过碰撞效果。
* `SkipCollisionEffects`：设置为 `true` 以跳过此实体的碰撞代码，例如造成碰撞伤害。不影响物理碰撞。不会跳过“碰撞者”的碰撞代码。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|53 |MC_PRE_KNIFE_COLLISION {: .copyable } | ([EntityKnife](../EntityKnife.md) Knife, [Entity](../Entity.md) Collider, boolean Low) | [KnifeSubType](KnifeSubType.md) | boolean or table |

### MC_PRE_PROJECTILE_COLLISION

现在可以选择返回一个表，该表可以包含以下任意组合的字段：

* `Collide`：设置为 `true` 以强制实体进行物理碰撞（相互推开），除非“碰撞者”忽略碰撞。设置为 `false` 以忽略物理碰撞，但不一定跳过碰撞效果。
* `SkipCollisionEffects`：设置为 `true` 以跳过此实体的碰撞代码，例如造成碰撞伤害。不影响物理碰撞。不会跳过“碰撞者”的碰撞代码。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|46 |MC_PRE_PROJECTILE_COLLISION {: .copyable } | ([EntityProjectile](../EntityProjectile.md) Projectile, [Entity](../Entity.md) Collider, boolean Low) | [ProjectileVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/ProjectileVariant.html) | boolean or table |

### MC_PRE_NPC_COLLISION

现在可以选择返回一个表，该表可以包含以下任意组合的字段：

* `Collide`：设置为 `true` 以强制实体进行物理碰撞（相互推开），除非“碰撞者”忽略碰撞。设置为 `false` 以忽略物理碰撞，但不一定跳过碰撞效果。
* `SkipCollisionEffects`：设置为 `true` 以跳过此实体的碰撞代码，例如造成碰撞伤害。不影响物理碰撞。不会跳过“碰撞者”的碰撞代码。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|30 |MC_PRE_NPC_COLLISION {: .copyable } | ([EntityNPC](../EntityNPC.md) NPC, [Entity](../Entity.md) Collider, boolean Low) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | boolean or table |

### MC_ENTITY_TAKE_DMG

现在可以选择返回一个表，该表可以包含以下任意组合的字段，以覆盖相应的参数：

* `Damage`
* `DamageFlags`
* `DamageCountdown`

修改后的值将传递给其余的回调。返回 `false` 以取消伤害仍然会跳过其余的回调。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|11 |MC_ENTITY_TAKE_DMG {: .copyable } | ([Entity](../Entity.md) Entity, float Damage, [DamageFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html) DamageFlags, [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, int DamageCountdown) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | boolean or table |

### MC_PRE_MOD_UNLOAD
Added boolean argument that identifies if it is running due to game shutdown.

Now runs earlier during shutdown, so code is less likely to crash.

|DLC|Value|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|:--|
|73 |MC_PRE_MOD_UNLOAD {: .copyable } | table Mod, boolean ShuttingDown | - | void |

### MC_GET_PILL_EFFECT
Now passes EntityPlayer as an argument.

|DLC|Value|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|:--|
|65 |MC_GET_PILL_EFFECT {: .copyable } | ([PillEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/PillEffect.html) SelectedPillEffect, [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) PillColor, [EntityPlayer](../EntityPlayer.md) Player) | - | [PillEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/PillEffect.html) |

### MC_POST_ENTITY_KILL
Now passes **Kill Source** as an argument.

|DLC|Value|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|:--|
|68 |MC_POST_ENTITY_KILL {: .copyable } | ([Entity](../Entity.md) Entity, [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) KillSource) | - | void |

## New Callbacks
### MC_PRE_ADD_COLLECTIBLE {: .copyable }

接受一个参数表：`{Type, Charge, FirstTime, Slot, VarData}`

或者接受一个 [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) 以在不更改任何其他参数的情况下更改类型，或者接受一个布尔值以完全取消添加（`false`）或强制添加发生并跳过后续回调（`true`）。

???- example "示例代码"
    这段代码将在玩家拾取任何道具时将其转换为“金钱即力量”。
    ```lua
    function mod:myFunction(Type, Charge, FirstTime, Slot, VarData, Player)
        return CollectibleType.COLLECTIBLE_MONEY_EQUALS_POWER
    end
    mod:AddCallback(ModCallbacks.MC_PRE_ADD_COLLECTIBLE, mod.myFunction)

    这段代码将强制主动道具在拾取时不充能。
    ```lua
    function mod:myFunction(Type, Charge, FirstTime, Slot, VarData, Player)
        return {Type, 0, FirstTime, Slot, VarData}
    end
    mod:AddCallback(ModCallbacks.MC_PRE_ADD_COLLECTIBLE, mod.myFunction)
    ```

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1004 |MC_PRE_ADD_COLLECTIBLE {: .copyable } | ([CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Type, <br>int Charge, <br>boolean FirstTime, <br>int Slot, <br>int VarData, <br>[EntityPlayer](../EntityPlayer.md) Player) | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | table or [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) |

### MC_POST_ADD_COLLECTIBLE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1005 |MC_POST_ADD_COLLECTIBLE {: .copyable } | ([CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Type, <br>int Charge, <br>boolean FirstTime, <br>int Slot, <br>int VarData, <br>[EntityPlayer](../EntityPlayer.md) Player) | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | void |

### MC_PRE_ADD_TRINKET {: .copyable }
Return `false` to cancel, or a different [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) to change the trinket being added.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1014 |MC_PRE_ADD_TRINKET {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket, boolean FirstTime) | [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) | boolean or [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) |

### MC_POST_BACKDROP_PRE_RENDER_WALLS {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1109 | MC_POST_BACKDROP_PRE_RENDER_WALLS {: .copyable } | void | - | void |

### MC_PRE_BACKDROP_CHANGE {: .copyable }

接受一个 `整数` 来更改 [BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html)。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1141 | MC_PRE_BACKDROP_CHANGE {: .copyable } | ([BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html) Type) | - | ([BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html) Type) |

### MC_POST_BACKDROP_CHANGE {: .copyable }
Fires after the backdrop changes.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1142 | MC_POST_BACKDROP_CHANGE {: .copyable } | ([BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html) Type) | [BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html) | void |

### MC_PRE_BACKDROP_RENDER_FLOOR {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1107 | MC_PRE_BACKDROP_RENDER_FLOOR {: .copyable } | ([Color](../Color.md) Color) | - | void |

### MC_PRE_BACKDROP_RENDER_WALLS {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1106 | MC_PRE_BACKDROP_RENDER_WALLS {: .copyable } | ([Color](../Color.md) Color) | - | void |

### MC_PRE_BACKDROP_RENDER_WATER {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1108 | MC_PRE_BACKDROP_RENDER_WATER {: .copyable } | void | - | void |

### MC_POST_BOMB_COLLISION {: .copyable }

假设实体的碰撞后代码未被跳过，则在该代码运行后触发。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1237 |MC_POST_BOMB_COLLISION {: .copyable } | ([EntityBomb](../EntityBomb.md) Bomb, <br>[Entity](../Entity.md) Collider, <br>boolean Low) | [BombVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/BombVariant.html) | void |

### MC_PRE_BOMB_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移

或者接受 `false` 以取消渲染

???- info "阴影"
    取消此回调不会停止实体阴影的渲染。目前正在对此进行调查，在此期间，请在 `MC_POST_UPDATE` 中对实体调用 `SetShadowSize(0)`。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1088 |MC_PRE_BOMB_RENDER {: .copyable } | ([EntityBomb](../EntityBomb.md) Bomb, <br>[Vector](../Vector.md) Offset) | [BombVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/BombVariant.md) | [Vector](../Vector.md) or boolean |

### MC_PRE_CHALLENGE_DONE {: .copyable }

在挑战被标记为完成之前调用。

返回 `false` 将阻止挑战完成跟踪函数的进一步执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1471 | MC_PRE_CHALLENGE_DONE {: .copyable } | ([Challenge](https://wofsauge.github.io/IsaacDocs/rep/enums/Challenge.html), <br>EntityPlayer [EntityPlayer](../EntityPlayer.md)) | [Challenge](https://wofsauge.github.io/IsaacDocs/rep/enums/Challenge.html) | boolean |

### MC_POST_CHALLENGE_DONE {: .copyable }

在挑战被标记为完成之后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1472 | MC_POST_CHALLENGE_DONE {: .copyable } | ([Challenge](https://wofsauge.github.io/IsaacDocs/rep/enums/Challenge.html)) | [Challenge](https://wofsauge.github.io/IsaacDocs/rep/enums/Challenge.html) | void |

### MC_PRE_CHANGE_ROOM {: .copyable }

接受一个参数表：`{TargetRoomIdx, Dimension}`

???+ bug

    当 `TargetRoomIdx` 为当前房间的索引时：

        当进入下一个未进入过的房间时：

            - 会传送回当前房间

        当进入下一个已进入过的房间时：

            - 如果该方向上，此房间后面还有第二个房间，就传送到那个房间（无论是否进去过，即隔一个房间传送）
            
            - 如果没有第二个房间，就传送回当前房间

    注：以上规则仅在小房间场景下测试验证过

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1061 |MC_PRE_CHANGE_ROOM {: .copyable } | (int TargetRoomIdx, <br>int Dimension) | - | table |

### MC_POST_ACHIEVEMENT_UNLOCK {: .copyable }

在成就解锁后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1476 |MC_POST_ACHIEVEMENT_UNLOCK {: .copyable } | ([Achievement](Achievement.md) AchievementID) | [Achievement](Achievement.md) | void |

### MC_PRE_COMPLETION_EVENT {: .copyable }

可以返回一个新的 [CompletionType](CompletionType.md) 或 `false` 以取消完成事件。取消该事件将阻止所有标记和与完成事件相关的内容为所有玩家触发。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1049 |MC_PRE_COMPLETION_EVENT {: .copyable } | ([CompletionType](CompletionType.md) Completion) | - | [CompletionType](CompletionType.md), boolean |

### MC_POST_COMPLETION_EVENT {: .copyable }

在记录完成事件时调用，例如击败最终boss或解锁受污染角色时。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1052 |MC_POST_COMPLETION_EVENT {: .copyable } | ([CompletionType](CompletionType.md) Completion) | - | void |

### MC_PRE_COMPLETION_MARKS_RENDER {: .copyable }

可以返回 `false` 以阻止完成标记的渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1216 |MC_PRE_COMPLETION_MARKS_RENDER {: .copyable } | ([Sprite](../Sprite.md) CompletionMarksSprite, <br>[Vector](../Vector.md) RenderPos, <br>[Vector](../Vector.md) RenderScale, <br>int PlayerType) | - | void |

### MC_POST_COMPLETION_MARKS_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1217 |MC_POST_COMPLETION_MARKS_RENDER {: .copyable } | ([Sprite](../Sprite.md) CompletionMarksSprite, <br>[Vector](../Vector.md) RenderPos, <br>[Vector](../Vector.md) RenderScale, <br>int PlayerType) | - | void |

### MC_COMPLETION_MARK_GET {: .copyable }

可以返回 `false` 以取消完成标记。

在玩家获得完成标记时调用，将标记的代码和玩家类型作为参数传入。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1047 |MC_COMPLETION_MARK_GET {: .copyable } | ([CompletionType](CompletionType.md) Completion, <br>int [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html)) | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | void or false |

### MC_POST_COMPLETION_MARK_GET {: .copyable }

在玩家获得完成标记之后调用，将标记的代码和玩家类型作为参数传入。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1048 |MC_POST_COMPLETION_MARK_GET {: .copyable } | ([CompletionType](CompletionType.md) Completion, <br>int [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html)) | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | void |

### MC_CONSOLE_AUTOCOMPLETE {: .copyable }

每当在控制台中输入具有 CUSTOM [AutocompleteType](AutocompleteType.md) 枚举的函数时调用。每次控制台输入更改时都会调用。

接受一个表。该表可以包含字符串值，这些值将作为命令自动补全的参数添加，也可以包含一个由两个字符串组成的表，该表将第一个字符串作为参数添加，第二个字符串作为描述添加。描述也可以在自动补全中使用，但是按下 TAB 键将使用 ID 进行正确的自动补全，而不是描述（例如 `giveitem` 命令，`c1` 是 “悲伤洋葱” 的 “参数”，“悲伤洋葱” 是 “描述”，两者都可以使用。按下 TAB 键将把命令转换为 `give c1`）。

REPENTOGON 会处理仅显示与给定输入相关的选项 - 只需返回一个选项表，REPENTOGON 将处理其余部分。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1120 |MC_CONSOLE_AUTOCOMPLETE {: .copyable } | (string Command, <br>string Params) | string Command | table |

### MC_PRE_DEVIL_APPLY_ITEMS {: .copyable }

当游戏开始计算传统物品以进行恶魔交易计算时，会运行此回调。这在阶段惩罚之前调用。

大多数影响恶魔交易几率的物品会在此处进行更改。

接受一个 `浮点数` 来修改此计算步骤中的几率。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1130 | MC_PRE_DEVIL_APPLY_ITEMS {: .copyable } | (float Chance) | - | float |

### MC_PRE_DEVIL_APPLY_SPECIAL_ITEMS {: .copyable }

接下来，游戏会应用 “特殊” 物品，这些物品可以绕过阶段惩罚，如山羊头和圣餐。

接受一个 `浮点数` 来修改此计算步骤中的几率。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1132 | MC_PRE_DEVIL_APPLY_SPECIAL_ITEMS {: .copyable } | (float Chance) | - | float |

### MC_PRE_DEVIL_APPLY_STAGE_PENALTY {: .copyable }

接下来，游戏会计算阶段惩罚。如果在前两层的任何地方生成了一笔交易，游戏会根据已接受的交易数量将最终几率衰减 50% 或 25%。

需要注意的是，即使游戏显示 50% 和 25% 的值分别约为 66% 或 33%，这是因为恶魔几率 *没有* 被限制在 0 到 1 之间，并且没有物品时 “100%” 通常意味着约 133% 的值。

接受一个 `布尔值`。返回 `false` 以绕过阶段惩罚。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1131 |MC_PRE_DEVIL_APPLY_STAGE_PENALTY {: .copyable } | void | - | boolean |

### MC_POST_DEVIL_CALCULATE {: .copyable }

这将覆盖 *所有* 之前的计算值，最终决定恶魔几率。

接受一个 `浮点数` 来修改几率。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1133 |MC_POST_DEVIL_CALCULATE {: .copyable } | (float Chance) | - | float |

### MC_PRE_EFFECT_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移

或者接受 `false` 以取消渲染

???- info "阴影"
    取消此回调不会停止实体阴影的渲染。目前正在对此进行调查，在此期间，请在 `MC_POST_UPDATE` 中对实体调用 `SetShadowSize(0)`。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1087 |MC_PRE_EFFECT_RENDER {: .copyable } | ([EntityEffect](https://wofsauge.github.io/IsaacDocs/rep/Entityeffect.html) Effect, <br>[Vector](../Vector.md) Offset) | [EffectVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/EffectVariant.md) | [Vector](../Vector.md) or boolean |

### MC_POST_ENTITY_TAKE_DMG {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1006 |MC_POST_ENTITY_TAKE_DMG {: .copyable } | ([Entity](../Entity.md) Entity, <br>float Damage, <br>[DamageFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html) DamageFlags, <br>[EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, <br>int DamageCountdown) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | void |

### MC_PRE_ENTITY_THROW {: .copyable }

接受一个 [Vector](../Vector.md)，它将修改被投掷实体的速度。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1040 |MC_PRE_ENTITY_THROW {: .copyable } | ([EntityPlayer](../EntityPlayer.md) ThrowingPlayer, <br>[Entity](../Entity.md) HeldEntity, <br>[Vector](../Vector.md) Velocity) | - | [Vector](../Vector.md) |

### MC_POST_ENTITY_THROW {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1041 |MC_POST_ENTITY_THROW {: .copyable } | ([EntityPlayer](../EntityPlayer.md) ThrowingPlayer, <br>[Entity](../Entity.md) ThrownEntity, <br>[Vector](../Vector.md) Velocity) | - | void |

### MC_POST_FAMILIAR_COLLISION {: .copyable }

假设实体的碰撞后代码未被跳过，则在该代码运行后触发。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1235 |MC_POST_FAMILIAR_COLLISION {: .copyable } | ([EntityFamiliar](../EntityFamiliar.md) Familiar, <br>[Entity](../Entity.md) Collider, <br>boolean Low) | [FamiliarVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/FamiliarVariant.html) | void |

### MC_POST_FAMILIAR_FIRE_BRIMSTONE {: .copyable }

当跟班发射硫磺激光时调用。

返回任何值都不会影响后续回调的执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1261 |MC_POST_FAMILIAR_FIRE_BRIMSTONE {: .copyable } | ([EntityLaser](../EntityLaser.md) Laser) | [FamiliarVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/FamiliarVariant.html) | void |

### MC_POST_FAMILIAR_FIRE_PROJECTILE {: .copyable }

当跟班发射眼泪时调用。

返回任何值都不会影响后续回调的执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1252 |MC_POST_FAMILIAR_FIRE_PROJECTILE {: .copyable } | ([EntityTear](../EntityTear.md) Tear) | [FamiliarVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/FamiliarVariant.html) | void |

### MC_POST_FAMILIAR_FIRE_TECH_LASER {: .copyable }

当跟班发射科技激光时调用。

返回任何值都不会影响后续回调的执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1262 |MC_POST_FAMILIAR_FIRE_TECH_LASER {: .copyable } | ([EntityLaser](../EntityLaser.md) Laser) | [FamiliarVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/FamiliarVariant.html) | void |

### MC_PRE_FAMILIAR_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移

或者接受 `false` 以取消渲染

???- info "阴影"
    取消此回调不会停止实体阴影的渲染。目前正在对此进行调查，在此期间，请在 `MC_POST_UPDATE` 中对实体调用 `SetShadowSize(0)`。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1080 |MC_PRE_FAMILIAR_RENDER {: .copyable } | ([EntityFamiliar](../EntityFamiliar.md) Familiar, <br>[Vector](../Vector.md) Offset) | [FamiliarVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/FamiliarVariant.html) | [Vector](../Vector.md) or boolean |

### MC_POST_FIRE_BOMB {: .copyable }

当玩家发射胎儿博士炸弹时调用。

返回任何值都不会影响后续回调的执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1253 |MC_POST_FIRE_BOMB {: .copyable } | ([EntityBomb](../EntityBomb.md) Bomb) | - | void |

### MC_POST_FIRE_BONE_CLUB {: .copyable }

当玩家发射遗忘者的骨棒时调用。

仅在骨棒最初生成时调用，而不是在挥舞或蓄力发射时调用。

返回任何值都不会影响后续回调的执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1254 |MC_POST_FIRE_BONE_CLUB {: .copyable } | ([EntityKnife](../EntityKnife.md) Knife) | - | void |

### MC_POST_FIRE_BRIMSTONE_BALL {: .copyable }

当玩家发射硫磺球时调用。

返回任何值都不会影响后续回调的执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1256 |MC_POST_FIRE_BRIMSTONE_BALL {: .copyable } | ([EntityEffect](../EntityEffect.md) Effect) | - | void |

### MC_POST_FIRE_BRIMSTONE {: .copyable }

当玩家发射硫磺激光时调用。

这也适用于延迟硫磺激光。

返回任何值都不会影响后续回调的执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1255 |MC_POST_FIRE_BRIMSTONE {: .copyable } | ([EntityLaser](../EntityLaser.md) Laser) | - | void |

### MC_POST_FIRE_KNIFE {: .copyable }

当玩家从妈妈的刀发射刀时调用。

仅在刀最初生成时调用，而不是在蓄力发射时调用。

返回任何值都不会影响后续回调的执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1257 |MC_POST_FIRE_KNIFE {: .copyable } | ([EntityKnife](../EntityKnife.md) Knife) | - | void |

### MC_POST_FIRE_SPLIT_TEAR {: .copyable }
Called when a tear is fired from an existing tear/laser/knife.

This includes various vanilla effects such as Cricket's Body, The Parasite, Mucormycosis, etc. The originating effect is identified by the [SplitTearType](SplitTearType.md) value.

For mods, this callback also runs when a tear is fired via [EntityTear:FireSplitTear()](../EntityTear.md#firesplittear), [EntityLaser:FireSplitTear()](../EntityLaser.md#firesplittear), or [EntityKnife:FireSplitTear()](../EntityKnife.md#firesplittear). The `FireSplitTear` functions allow for a string to be passed in place of a [SplitTearType](SplitTearType.md), and that string will also appear in place of the [SplitTearType](SplitTearType.md) in this callback.

Returning any value will have no effect on later callback executions.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1258 |MC_POST_FIRE_SPLIT_TEAR {: .copyable } | ([EntityTear](../EntityTear.md) Tear, [Entity](../Entity.md) SourceEntity, [SplitTearType](SplitTearType.md) or string) | [SplitTearType](SplitTearType.md) or string | void |

### MC_POST_FIRE_SWORD {: .copyable }

当玩家挥舞灵剑时调用。

返回任何值都不会影响后续回调的执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1258 |MC_POST_FIRE_SWORD {: .copyable } | ([EntityKnife](../EntityKnife.md) Knife) | - | void |

### MC_POST_FIRE_TECH_LASER {: .copyable }

当玩家发射科技激光时调用。

返回任何值都不会影响后续回调的执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1259 |MC_POST_FIRE_TECH_LASER {: .copyable } | ([EntityLaser](../EntityKnife.md) Laser) | - | void |

### MC_POST_FIRE_TECH_X_LASER {: .copyable }

当玩家发射科技X激光时调用。

返回任何值都不会影响后续回调的执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1260 |MC_POST_FIRE_TECH_X_LASER {: .copyable } | ([EntityLaser](../EntityKnife.md) Laser) | - | void |

### MC_GET_FOLLOWER_PRIORITY {: .copyable }

接受 [FollowerPriority](FollowerPriority.md) 来赋予跟班优先级。可以接受任何整数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1063 |MC_GET_FOLLOWER_PRIORITY {: .copyable } | ([EntityFamiliar](../EntityFamiliar.md) Familiar) | [FamiliarVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/FamiliarVariant.md) | [FollowerPriority](FollowerPriority.md) or int |

### MC_PRE_GET_LIGHTING_ALPHA {: .copyable }

接受一个 `浮点数` 来修改光照透明度。通常这个值在 0 到 1 之间，但实际上你可以设置更高的值。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1150 |MC_PRE_GET_LIGHTING_ALPHA {: .copyable } | (float OriginalAlpha) | - | float |

### MC_GET_SHOP_ITEM_PRICE {: .copyable }

在计算商店物品的价格后调用。
返回一个整数或 [PickupPrice](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupPrice.html) 来更改物品的价格。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1066 |MC_GET_SHOP_ITEM_PRICE {: .copyable } | (int [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html), <br>int PickupSubType, <br>int ShopItemID, <br>int Price) | int | [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) |

### MC_PRE_GRID_ENTITY_DECORATION_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移或 `false` 以取消渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1444 |MC_PRE_GRID_ENTITY_DECORATION_RENDER {: .copyable } | ([GridEntityDecoration](../GridEntityDecoration.md) Decoration, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_POST_GRID_ENTITY_DECORATION_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1445 |MC_POST_GRID_ENTITY_DECORATION_RENDER {: .copyable } | ([GridEntityDecoration](../GridEntityDecoration.md) Decoration) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_DECORATION_UPDATE {: .copyable }

接受 `false` 以取消更新。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1400 |MC_PRE_GRID_ENTITY_DECORATION_UPDATE {: .copyable } | ([GridEntityDecoration](../GridEntityDecoration.md) Decoration) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_DECORATION_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1401 |MC_POST_GRID_ENTITY_DECORATION_UPDATE {: .copyable } | ([GridEntityDecoration](../GridEntityDecoration.md) Decoration) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_DOOR_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移或 `false` 以取消渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1446 |MC_PRE_GRID_ENTITY_DOOR_RENDER {: .copyable } | ([GridEntityDoor](../GridEntityDoor.md) Door, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_POST_GRID_ENTITY_DOOR_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1447 |MC_POST_GRID_ENTITY_DOOR_RENDER {: .copyable } | ([GridEntityDoor](../GridEntityDoor.md) Door) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_DOOR_UPDATE {: .copyable }

接受 `false` 以取消更新。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1402 |MC_PRE_GRID_ENTITY_DOOR_UPDATE {: .copyable } | ([GridEntityDoor](../GridEntityDoor.md) Door) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_DOOR_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1403 |MC_POST_GRID_ENTITY_DOOR_UPDATE {: .copyable } | ([GridEntityDoor](../GridEntityDoor.md) Door) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_FIRE_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移或 `false` 以取消渲染。

???+ warning "警告"
    火焰网格实体在很大程度上未被使用，在大多数情况下，你可能想针对 [EntityNPC](../EntityNPC.md) 壁炉。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1448 |MC_PRE_GRID_ENTITY_FIRE_RENDER {: .copyable } | ([GridEntityFire](../GridEntityFire.md) Fire, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_POST_GRID_ENTITY_FIRE_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1449 |MC_POST_GRID_ENTITY_FIRE_RENDER {: .copyable } | ([GridEntityFire](../GridEntityFire.md) Fire) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_FIRE_UPDATE {: .copyable }

接受 `false` 以取消更新。

???+ warning "警告"
    火焰网格实体在很大程度上未被使用，在大多数情况下，你可能想针对 [EntityNPC](../EntityNPC.md) 壁炉。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1404 |MC_PRE_GRID_ENTITY_FIRE_UPDATE {: .copyable } | ([GridEntityFire](../GridEntityFire.md) Fire) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_FIRE_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1405 |MC_POST_GRID_ENTITY_FIRE_UPDATE {: .copyable } | ([GridEntityFire](../GridEntityFire.md) Fire) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_GRAVITY_UPDATE {: .copyable }

接受 `false` 以取消更新。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1406 |MC_PRE_GRID_ENTITY_GRAVITY_UPDATE {: .copyable } | ([GridEntityGravity](../GridEntityGravity.md) Gravity) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_GRAVITY_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1407 |MC_POST_GRID_ENTITY_GRAVITY_UPDATE {: .copyable } | ([GridEntityGravity](../GridEntityGravity.md) Gravity) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_LOCK_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移或 `false` 以取消渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1450 |MC_PRE_GRID_ENTITY_LOCK_RENDER {: .copyable } | ([GridEntityLock](https://wofsauge.github.io/IsaacDocs/rep/GridEntityLock.html) Lock, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_POST_GRID_ENTITY_LOCK_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1451 |MC_POST_GRID_ENTITY_LOCK_RENDER {: .copyable } | ([GridEntityLock](https://wofsauge.github.io/IsaacDocs/rep/GridEntityLock.html) Lock) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_LOCK_UPDATE {: .copyable }

接受 `false` 以取消更新。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1408 |MC_PRE_GRID_ENTITY_LOCK_UPDATE {: .copyable } | ([GridEntityLock](https://wofsauge.github.io/IsaacDocs/rep/GridEntityLock.html) Lock) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_LOCK_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1409 |MC_POST_GRID_ENTITY_LOCK_UPDATE {: .copyable } | ([GridEntityLock](https://wofsauge.github.io/IsaacDocs/rep/GridEntityLock.html) Lock) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_PIT_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移或 `false` 以取消渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1454 |MC_PRE_GRID_ENTITY_PIT_RENDER {: .copyable } | ([GridEntityPit](https://wofsauge.github.io/IsaacDocs/rep/GridEntityPit.html) Pit, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_POST_GRID_ENTITY_PIT_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1455 |MC_POST_GRID_ENTITY_PIT_RENDER {: .copyable } | ([GridEntityPit](https://wofsauge.github.io/IsaacDocs/rep/GridEntityPit.html) Pit) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_PIT_UPDATE {: .copyable }

接受 `false` 以取消更新。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1410 |MC_PRE_GRID_ENTITY_PIT_UPDATE {: .copyable } | ([GridEntityPit](https://wofsauge.github.io/IsaacDocs/rep/GridEntityPit.html) Pit) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_PIT_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1411 |MC_POST_GRID_ENTITY_PIT_UPDATE {: .copyable } | ([GridEntityPit](https://wofsauge.github.io/IsaacDocs/rep/GridEntityPit.html) Pit) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_POOP_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移或 `false` 以取消渲染。

???- warning "警告"
    此回调不包括受污染的 ??? 使用的 [EntityNPC](../EntityNPC.md) 便便。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1456 |MC_PRE_GRID_ENTITY_POOP_RENDER {: .copyable } | ([GridEntityPoop](https://wofsauge.github.io/IsaacDocs/rep/GridEntityPoop.html) Poop, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_POST_GRID_ENTITY_POOP_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1457 |MC_POST_GRID_ENTITY_POOP_RENDER {: .copyable } | ([GridEntityPoop](https://wofsauge.github.io/IsaacDocs/rep/GridEntityPoop.html) Poop) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_POOP_UPDATE {: .copyable }

接受 `false` 以取消更新。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1412 |MC_PRE_GRID_ENTITY_POOP_UPDATE {: .copyable } | ([GridEntityPoop](https://wofsauge.github.io/IsaacDocs/rep/GridEntityPoop.html) Poop) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_POOP_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1413 |MC_POST_GRID_ENTITY_POOP_UPDATE {: .copyable } | ([GridEntityPoop](https://wofsauge.github.io/IsaacDocs/rep/GridEntityPoop.html) Poop) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_PRESSUREPLATE_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移或 `false` 以取消渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1460 |MC_PRE_GRID_ENTITY_PRESSUREPLATE_RENDER {: .copyable } | ([GridEntityPressurePlate](../GridEntityPressurePlate.md) PressurePlate, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_POST_GRID_ENTITY_PRESSUREPLATE_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1461 |MC_POST_GRID_ENTITY_PRESSUREPLATE_RENDER {: .copyable } | ([GridEntityPressurePlate](../GridEntityPressurePlate.md) PressurePlate) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_PRESSUREPLATE_UPDATE {: .copyable }

接受 `false` 以取消更新。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1414 |MC_PRE_GRID_ENTITY_PRESSUREPLATE_UPDATE {: .copyable } | ([GridEntityPressurePlate](../GridEntityPressurePlate.md) PressurePlate) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_PRESSUREPLATE_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1415 |MC_POST_GRID_ENTITY_PRESSUREPLATE_UPDATE {: .copyable } | ([GridEntityPressurePlate](../GridEntityPressurePlate.md) PressurePlate) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_ROCK_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移或 `false` 以取消渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1458 |MC_PRE_GRID_ENTITY_ROCK_RENDER {: .copyable } | ([GridEntityRock](../GridEntityRock.md) Rock, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_POST_GRID_ENTITY_ROCK_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1459 |MC_POST_GRID_ENTITY_ROCK_RENDER {: .copyable } | ([GridEntityRock](../GridEntityRock.md) Rock) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_ROCK_UPDATE {: .copyable }

接受 `false` 以取消更新。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1416 |MC_PRE_GRID_ENTITY_ROCK_UPDATE {: .copyable } | ([GridEntityRock](../GridEntityRock.md) Rock) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_ROCK_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1417 |MC_POST_GRID_ENTITY_ROCK_UPDATE {: .copyable } | ([GridEntityRock](../GridEntityRock.md) Rock) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_SPAWN {: .copyable }

当 [GridEntity](../GridEntity.md) 在房间初始化之外生成时调用。

接受 `false` 以取消生成网格，接受一个 `{Type, Variant, Vardata, SpawnSeed}` 表来修改它，或接受一个 [GridEntityDesc](https://wofsauge.github.io/IsaacDocs/rep/GridEntityDesc.html) 来完全覆盖它。

???+ warning "警告"
    `Desc` 在大多数情况下将为 `nil`。例外情况是鼹鼠NPC生成的便便、[TurnGold](https://wofsauge.github.io/IsaacDocs/rep/Room.html#void-turngold) 生成的网格，或使用新的 `SpawnGridEntity(int GridIndex, GridEntityDesc Descriptor)` 重载调用的Lua生成。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1100 |MC_PRE_GRID_ENTITY_SPAWN {: .copyable } | ([GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) Type, <br>int Variant, <br>int VarData, <br>int GridIdx, <br>int SpawnSeed, <br>[GridEntityDesc](https://wofsauge.github.io/IsaacDocs/rep/GridEntityDesc.html) Desc) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) Type | boolean, table, or [GridEntityDesc](https://wofsauge.github.io/IsaacDocs/rep/GridEntityDesc.html) |

### MC_POST_GRID_ENTITY_SPAWN {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1101 |MC_POST_GRID_ENTITY_SPAWN {: .copyable } | ([GridEntity](../GridEntity.md) Grid) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) Type | void |

### MC_PRE_GRID_ENTITY_SPIKES_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移或 `false` 以取消渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1432 |MC_PRE_GRID_ENTITY_SPIKES_RENDER {: .copyable } | ([GridEntitySpikes](https://wofsauge.github.io/IsaacDocs/rep/GridEntitySpikes.html) Grid, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_POST_GRID_ENTITY_SPIKES_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1433 |MC_POST_GRID_ENTITY_SPIKES_RENDER {: .copyable } | ([GridEntitySpikes](https://wofsauge.github.io/IsaacDocs/rep/GridEntitySpikes.html) Grid) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_SPIKES_UPDATE {: .copyable }

接受 `false` 以取消更新。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1418 |MC_PRE_GRID_ENTITY_SPIKES_UPDATE {: .copyable } | ([GridEntitySpikes](https://wofsauge.github.io/IsaacDocs/rep/GridEntitySpikes.html) Spikes) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_SPIKES_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1419 |MC_POST_GRID_ENTITY_SPIKES_UPDATE {: .copyable } | ([GridEntitySpikes](https://wofsauge.github.io/IsaacDocs/rep/GridEntitySpikes.html) Spikes) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_STAIRCASE_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移或 `false` 以取消渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1440 |MC_PRE_GRID_ENTITY_STAIRCASE_RENDER {: .copyable } | ([GridEntityStairs](../GridEntityStairs.md) Staircase, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_POST_GRID_ENTITY_STAIRCASE_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1441 |MC_POST_GRID_ENTITY_STAIRCASE_RENDER {: .copyable } | ([GridEntityStairs](../GridEntityStairs.md) Staircase) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_STAIRCASE_UPDATE {: .copyable }

接受 `false` 以取消更新。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1420 |MC_PRE_GRID_ENTITY_STAIRCASE_UPDATE {: .copyable } | ([GridEntityStairs](../GridEntityStairs.md) Staircase) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_STAIRCASE_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1421 |MC_POST_GRID_ENTITY_STAIRCASE_UPDATE {: .copyable } | ([GridEntityStairs](../GridEntityStairs.md) Staircase) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_STATUE_UPDATE {: .copyable }

接受 `false` 以取消更新。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1422 |MC_PRE_GRID_ENTITY_STATUE_UPDATE {: .copyable } | ([GridEntityStatue](../GridEntityStatue.md) Statue) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_STATUE_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1423 |MC_POST_GRID_ENTITY_STATUE_UPDATE {: .copyable } | ([GridEntityStatue](../GridEntityStatue.md) Statue) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_TELEPORTER_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移或 `false` 以取消渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1452 |MC_PRE_GRID_ENTITY_TELEPORTER_RENDER {: .copyable } | ([GridEntityTeleporter](https://wofsauge.github.io/IsaacDocs/rep/GridEntityTeleporter.html) Teleporter, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_POST_GRID_ENTITY_TELEPORTER_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1453 |MC_POST_GRID_ENTITY_TELEPORTER_RENDER {: .copyable } | ([GridEntityTeleporter](https://wofsauge.github.io/IsaacDocs/rep/GridEntityTeleporter.html) Teleporter) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_TELEPORTER_UPDATE {: .copyable }

接受 `false` 以取消更新。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1424 |MC_PRE_GRID_ENTITY_TELEPORTER_UPDATE {: .copyable } | ([GridEntityTeleporter](../GridEntityTeleporter.md) Teleporter) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_TELEPORTER_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1425 |MC_POST_GRID_ENTITY_TELEPORTER_UPDATE {: .copyable } | ([GridEntityTeleporter](../GridEntityTeleporter.md) Teleporter) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_TNT_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移或 `false` 以取消渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1436 |MC_PRE_GRID_ENTITY_TNT_RENDER {: .copyable } | ([GridEntityTNT](https://wofsauge.github.io/IsaacDocs/rep/GridEntityTNT.html) TNT, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_POST_GRID_ENTITY_TNT_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1437 |MC_POST_GRID_ENTITY_TNT_RENDER {: .copyable } | ([GridEntityTNT](https://wofsauge.github.io/IsaacDocs/rep/GridEntityTNT.html) TNT) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_TNT_UPDATE {: .copyable }

接受 `false` 以取消更新。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1430 |MC_PRE_GRID_ENTITY_TNT_UPDATE {: .copyable } | ([GridEntityTNT](https://wofsauge.github.io/IsaacDocs/rep/GridEntityTNT.html) TNT) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_TNT_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1431 |MC_POST_GRID_ENTITY_TNT_UPDATE {: .copyable } | ([GridEntityTNT](https://wofsauge.github.io/IsaacDocs/rep/GridEntityTNT.html) TNT) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_TRAPDOOR_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移或 `false` 以取消渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1438 |MC_PRE_GRID_ENTITY_TRAPDOOR_RENDER {: .copyable } | ([GridEntityTrapDoor](../GridEntityTrapDoor.md) TrapDoor, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_POST_GRID_ENTITY_TRAPDOOR_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1439 |MC_POST_GRID_ENTITY_TRAPDOOR_RENDER {: .copyable } | ([GridEntityTrapDoor](../GridEntityTrapDoor.md) TrapDoor) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_TRAPDOOR_UPDATE {: .copyable }

接受 `false` 以取消更新。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1426 |MC_PRE_GRID_ENTITY_TRAPDOOR_UPDATE {: .copyable } | ([GridEntityTrapDoor](../GridEntityTrapDoor.md) TrapDoor) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_TRAPDOOR_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1427 |MC_POST_GRID_ENTITY_TRAPDOOR_UPDATE {: .copyable } | ([GridEntityTrapDoor](../GridEntityTrapDoor.md) TrapDoor) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_WALL_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移或 `false` 以取消渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1462 |MC_PRE_GRID_ENTITY_WALL_RENDER {: .copyable } | ([GridEntityWall](../GridEntityWall.md) Wall, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_POST_GRID_ENTITY_WALL_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1463 |MC_POST_GRID_ENTITY_WALL_RENDER {: .copyable } | ([GridEntityWall](../GridEntityWall.md) Wall) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_WEB_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移或 `false` 以取消渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1434 |MC_PRE_GRID_ENTITY_WEB_RENDER {: .copyable } | ([GridEntityWeb](../GridEntityWeb.md) Web, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_POST_GRID_ENTITY_WEB_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1435 |MC_POST_GRID_ENTITY_WEB_RENDER {: .copyable } | ([GridEntityWeb](../GridEntityWeb.md) Web) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_PRE_GRID_ENTITY_WEB_UPDATE {: .copyable }

接受 `false` 以取消更新。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1428 |MC_PRE_GRID_ENTITY_WEB_UPDATE {: .copyable } | ([GridEntityWeb](../GridEntityWeb.md) Web) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_ENTITY_WEB_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1429 |MC_POST_GRID_ENTITY_WEB_UPDATE {: .copyable } | ([GridEntityWeb](../GridEntityWeb.md) Web) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_GRID_HURT_DAMAGE {: .copyable }

在网格实体试图对一个实体造成伤害之前调用。

如果实体或玩家应该忽略该伤害，则返回 `false`。

>>>>>>> upstream/main
|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1012 |MC_GRID_HURT_DAMAGE {: .copyable } | ([GridEntity](../GridEntity.md) GridEntity, <br>[Entity](../Entity.md) Entity, <br>int PlayerDamageAmount, <br>[DamageFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html) DamageFlags, <br>float DamageAmount, boolean IgnoreGridCollisionClass) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | boolean |

### MC_POST_GRID_HURT_DAMAGE {: .copyable }

在网格实体试图对一个实体造成伤害之后调用。请注意，这并不保证实体实际受到了伤害（例如，如果玩家当前处于无敌状态）。

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1013 |MC_POST_GRID_HURT_DAMAGE {: .copyable } | ([GridEntity](../GridEntity.md) GridEntity, <br>[Entity](../Entity.md) Entity, <br>int PlayerDamageAmount, <br>[DamageFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html) DamageFlags, <br>float DamageAmount, boolean IgnoreGridCollisionClass) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_POST_GRID_ROCK_DESTROY {: .copyable }

不接受返回参数。

???+ note
	`Source` can be `nil` if [GridEntity:Destroy](https://wofsauge.github.io/IsaacDocs/rep/GridEntity.html#destroy) is called instead of [GridEntity:DestroyWithSource](https://wofsauge.github.io/IsaacDocs/rep/GridEntity.html#destroywithsource).

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1011 |MC_POST_GRID_ROCK_DESTROY {: .copyable } | ([GridEntityRock](https://wofsauge.github.io/IsaacDocs/rep/GridEntityRock.html) Rock, <br>[GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) Type, <br>boolean Immediate, <br>[EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | void |

### MC_HUD_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1022 |MC_HUD_RENDER {: .copyable } | void | - | void |

### MC_POST_HUD_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1024 |MC_POST_HUD_RENDER {: .copyable } | void | - | void |

### MC_HUD_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1020 |MC_HUD_UPDATE {: .copyable } | void | - | void |

### MC_POST_HUD_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1021 |MC_POST_HUD_UPDATE {: .copyable } | void | - | void |

### MC_IS_PERSISTENT_ROOM_ENTITY {: .copyable }

返回 `true` 允许实体重生。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1263 |MC_IS_PERSISTENT_ROOM_ENTITY {: .copyable } | ([EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) Type, <br>int Variant) | - | boolean |

### MC_PRE_ITEM_OVERLAY_SHOW {: .copyable }

接受一个整数来更改 [Giantbook](Giantbook.md)

或者接受 `true` 以取消物品叠加显示

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1076 |MC_PRE_ITEM_OVERLAY_SHOW {: .copyable } | ([Giantbook](Giantbook.md) GiantbookID, <br>int Delay, <br>[EntityPlayer](../EntityPlayer.md) Player) | [Giantbook](Giantbook.md) | [Giantbook](Giantbook.md) or boolean |

### MC_POST_ITEM_OVERLAY_SHOW {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1134 |MC_POST_ITEM_OVERLAY_SHOW {: .copyable } | ([Giantbook](Giantbook.md) GiantbookID, <br>int Delay, <br>[EntityPlayer](../EntityPlayer.md) Player) | [Giantbook](Giantbook.md) | void |

### MC_POST_ITEM_OVERLAY_UPDATE {: .copyable }
`SkipAnimation` returns `true` if the item overlay was skipped, `false` otherwise.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1075 |MC_POST_ITEM_OVERLAY_UPDATE {: .copyable } | ([Giantbook](Giantbook.md) GiantbookID, <br>bool SkipAnimation) | [Giantbook](Giantbook.md) | void |

### MC_POST_KNIFE_COLLISION {: .copyable }

假设实体的碰撞后代码未被跳过，则在该代码运行后触发。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1243 |MC_POST_KNIFE_COLLISION {: .copyable } | ([EntityKnife](../EntityKnife.md) Knife, <br>[Entity](../Entity.md) Collider, <br>boolean Low) | [KnifeSubType](KnifeSubType.md) | void |

### MC_PRE_KNIFE_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移

或者接受 `false` 以取消渲染

???- info "阴影"
    取消此回调不会停止实体阴影的渲染。目前正在对此进行调查，在此期间，请在 `MC_POST_UPDATE` 中对实体调用 `SetShadowSize(0)`。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1086 |MC_PRE_KNIFE_RENDER {: .copyable } | ([EntityKnife](../EntityKnife.md) Knife, <br>[Vector](../Vector.md) Offset) | [KnifeVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/KnifeVariant.md) | [Vector](../Vector.md) or boolean |

### MC_PRE_LASER_COLLISION {: .copyable }

在激光击中实体之前立即触发。返回 `true` 以忽略碰撞。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1248 |MC_PRE_LASER_COLLISION {: .copyable } | ([EntityLaser](../EntityLaser.md) Laser, <br>[Entity](../Entity.md) Collider) | [LaserVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/LaserVariant.html) | boolean |

### MC_POST_LASER_COLLISION {: .copyable }

在激光击中实体之后触发。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1249 |MC_POST_LASER_COLLISION {: .copyable } | ([EntityLaser](../EntityLaser.md) Laser, <br>[Entity](../Entity.md) Collider) | [LaserVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/LaserVariant.html) | void |

### MC_PRE_LEVEL_INIT {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1060 |MC_PRE_LEVEL_INIT {: .copyable } | void | - | void |

### MC_POST_LEVEL_LAYOUT_GENERATED {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1099 |MC_POST_LEVEL_LAYOUT_GENERATED {: .copyable } | ([LevelGenerator](../LevelGenerator.md) LevelGenerator) | - | void |

### MC_PRE_LEVEL_PLACE_ROOM {: .copyable }

返回一个房间配置以替换将要放置的房间

???+ warning "警告"
    新房间的形状必须相同，并且新的可用门插槽必须与原始房间的门兼容。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1137 |MC_PRE_LEVEL_PLACE_ROOM {: .copyable } | ([LevelGeneratorRoom](../LevelGeneratorRoom.md) Slot, <br>[RoomConfigRoom](https://wofsauge.github.io/IsaacDocs/rep/RoomConfig_Room.html) RoomConfig, <br>int Seed) | - | [RoomConfigRoom](https://wofsauge.github.io/IsaacDocs/rep/RoomConfig_Room.html) Config |

### MC_PRE_LEVEL_SELECT {: .copyable }

当游戏选择要加载的关卡（也称为阶段）时，通常是当玩家进入活板门时，会触发此回调。
该回调接受两个参数：

* `Level`：游戏选择的关卡，如 [LevelStage](https://wofsauge.github.io/IsaacDocs/rep/enums/LevelStage.html) 枚举中所定义。
* `Type`：游戏选择的关卡类型，如 [StageType](https://wofsauge.github.io/IsaacDocs/rep/enums/StageType.html) 枚举中所定义。

此回调可以返回 `nil` 或一个表。

* `nil`：让游戏继续使用它选择的关卡阶段 / 阶段类型对；
* 表：必须包含两个字段（匿名）。第一个字段是所需的关卡阶段，第二个字段是所需的阶段类型。

如果你返回一个表，REPENTOGON 将检查这些值是否落在关卡阶段和阶段类型的允许范围内。

???+ warn "值范围"
    请记住，普通 / 困难模式和贪婪 / 更贪婪模式的关卡类型范围是不同的。

    还要记住，自《以撒的结合：忏悔》以来，阶段类型值 3 已被弃用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1104 | MC_PRE_LEVEL_SELECT {: .copyable } | ([LevelStage](https://wofsauge.github.io/IsaacDocs/rep/enums/LevelStage.html) Level, <br>[StageType](https://wofsauge.github.io/IsaacDocs/rep/enums/StageType.html) Type) | - | void

### MC_MAIN_MENU_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1023 |MC_MAIN_MENU_RENDER {: .copyable } | void | - | void |

### MC_PRE_MEGA_SATAN_ENDING {: .copyable }

在超级撒旦强制结束游戏之前立即调用。

* 接受 `true` 以抑制结束画面，保证出现通往虚空的传送门，同时保留该角色的完成标记。
* `false` 或 `nil` 将没有效果。我可能会考虑让 `false` 保证一个结束画面？

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1201 |MC_PRE_MEGA_SATAN_ENDING {: .copyable } | void | - | boolean |

### MC_MENU_INPUT_ACTION {: .copyable }

与 `MC_INPUT_ACTION` 相同，但仅在主菜单中有效。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1464 | MC_MENU_INPUT_ACTION {: .copyable } | ([Entity](../Entity.md), <br>[InputHook](https://wofsauge.github.io/IsaacDocs/rep/enums/InputHook.html), <br>[ButtonAction](https://wofsauge.github.io/IsaacDocs/rep/enums/ButtonAction.html))|[InputHook](https://wofsauge.github.io/IsaacDocs/rep/enums/InputHook.html) | boolean or float |

### MC_PRE_STATUS_EFFECT_APPLY {: .copyable }
Triggers before applying a status effect to an Entity.

Return `false` to cancel it.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1465 | MC_PRE_STATUS_EFFECT_APPLY {: .copyable } | ([StatusEffect](StatusEffect.md) StatusID, <br>[Entity](../Entity.md) Entity, <br>[EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, <br>int duration) | [StatusEffect](StatusEffect.md) | boolean |

### MC_POST_STATUS_EFFECT_APPLY {: .copyable }
Triggers after applying a status effect to an Entity.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1466 | MC_POST_STATUS_EFFECT_APPLY {: .copyable } | ([StatusEffect](StatusEffect.md) StatusID, <br>[Entity](../Entity.md) Entity, <br>[EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, <br>int duration) | [StatusEffect](StatusEffect.md) | void |

### MC_POST_MODS_LOADED {: .copyable }

在所有Lua脚本加载完成后调用。非常适合运行那些期望在所有模组初始化后运行的代码，而无需考虑加载顺序的问题！

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1210 |MC_POST_MODS_LOADED {: .copyable } | void | - | void |

### MC_PRE_MUSIC_LAYER_TOGGLE {: .copyable }

接受一个音乐层ID（枚举待定）来更改层，或接受一个布尔值来更改层的状态：`true` 以保持其运行，`false` 以停止它。

`CurrentState` 在层即将 **启用** 时返回 `true`，在层即将 **禁用** 时返回 `false`。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1035 |MC_PRE_MUSIC_LAYER_TOGGLE {: .copyable } | (int ID, <br>boolean CurrentState) | int | int or boolean |

### MC_PRE_MUSIC_PLAY_JINGLE {: .copyable }

接受一个 [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) 来更改曲目

或者接受 `false` 以取消曲目

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1094 |MC_PRE_MUSIC_PLAY_JINGLE {: .copyable } | ([Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) MusicID) | [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) | [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) or boolean |

### MC_PRE_MUSIC_PLAY {: .copyable }

接受一个参数表：`{ID, Volume OR FadeRate}`

或者接受一个 [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) 来更改曲目而不更改音量或淡入淡出速率

或者接受 `false` 以取消曲目

???- info "音量与淡入淡出速率"
    此回调在 `MusicManager::Play` 和 `MusicManager::Crossfade` 时都会被调用！提供 `IsFade` 以区分两者。

???- example "示例代码"
    此代码将把所有音乐曲目替换为水淹洞穴主题（不管好坏）。
    ```lua
    function mod:myFunction(ID, Volume, IsFade)
        return Music.MUSIC_FLOODED_CAVES
    end
    mod:AddCallback(ModCallbacks.MC_PRE_MUSIC_PLAY, mod.myFunction)
    ```

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1034 |MC_PRE_MUSIC_PLAY {: .copyable } | (int ID, <br>float Volume OR float FadeRate, <br>boolean IsFade) | [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) | table or [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) or boolean |

### MC_PRE_M_MORPH_ACTIVE {: .copyable }

当主动道具被 “M”（饰品ID 138）重铸时，此回调会触发，并允许覆盖其默认行为。

* 接受一个 [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) 类型的值，以覆盖重铸后的道具ID；或者接受 `false`，以完全阻止主动道具重铸。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1190 |MC_PRE_M_MORPH_ACTIVE {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>[CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible) | - | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) |

### MC_PRE_NEW_ROOM {: .copyable }

不接受返回参数。

???+ warning "警告"
    虽然此回调提供了一个房间对象，且该房间对象本身没有问题，但此回调会在 **房间完全初始化之前** 触发。因此，围绕房间对象的操作应被视为不稳定且不可靠的，使用时需自行斟酌。一些看似友好的函数（如 GetCenterPos）在这个回调中使用时已知会引发问题。所以，请尽量将与房间对象相关的操作移至在此回调之后触发的其他回调中。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1200 |MC_PRE_NEW_ROOM {: .copyable } | ([Room](https://wofsauge.github.io/IsaacDocs/rep/Room) Room, <br>[RoomDescriptor](https://wofsauge.github.io/IsaacDocs/rep/RoomDescriptor) Descriptor) | - | void |

### MC_POST_NIGHTMARE_SCENE_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1102 |MC_POST_NIGHTMARE_SCENE_RENDER {: .copyable } | void | - | void |

### MC_POST_NIGHTMARE_SCENE_SHOW {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1103 |MC_POST_NIGHTMARE_SCENE_SHOW {: .copyable } | (boolean IsDogmaNightmare) | - | void |

### MC_POST_NPC_COLLISION {: .copyable }

假设实体的碰撞后代码未被跳过，则在该代码运行之后执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1247 |MC_POST_NPC_COLLISION {: .copyable } | ([EntityNPC](../EntityNPC.md) NPC, <br>[Entity](../Entity.md) Collider, <br>boolean Low) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | void |

### MC_PRE_NPC_MORPH {: .copyable }

接受一个参数表：`{EntityType, Variant, SubType, Championid}` 或者仅 `{EntityType, Variant, SubType}`。

返回 `false` 可取消变形。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1212 |MC_PRE_NPC_MORPH {: .copyable } | ([EntityNPC](../EntityNPC.md) NPC, <br>int EntityType, <br>int Variant, <br>int SubType, <br>int Championid) | - | table or boolean |

### MC_POST_NPC_MORPH {: .copyable }

在变形已经发生之后运行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1214 |MC_POST_NPC_MORPH {: .copyable } | ([EntityNPC](../EntityNPC.md) NPC, <br>int PreviousType, <br>int PreviousVariant, <br>int PreviousSubType) | - | void |

### MC_NPC_PICK_TARGET {: .copyable }

每当一个 EntityNPC 选择其目标时调用，例如当调用 EntityNPC:GetPlayerTarget() 时。

返回一个实体，可使 NPC 改为以该实体为目标。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1222 |MC_NPC_PICK_TARGET {: .copyable } | ([EntityNPC](../EntityNPC.md) NPC, <br>[Entity](../Entity.md) CurrentTarget) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | [Entity](../Entity.md) |

### MC_POST_NPC_DARK_RED_CHAMPION_REGEN {: .copyable }

在暗红色冠军怪从黏液形态重生后立即运行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1223 |MC_POST_NPC_DARK_RED_CHAMPION_REGEN {: .copyable } | ([EntityNPC](../EntityNPC.md) NPC) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | void |

### MC_EVALUATE_CUSTOM_CACHE {: .copyable }

当评估自定义缓存时调用（参见 [items.xml](../xml/items.md)）。返回一个数字以修改该值。修改后的值会传递给下一个回调。

初始值始终为 0。可以随时使用 `player:GetCustomCacheValue("mycustomcache")` 获取最新结果。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1224 |MC_EVALUATE_CUSTOM_CACHE {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, CustomCacheTag string, float Value) | string CustomCacheTag | void |

### MC_EVALUATE_FAMILIAR_MULTIPLIER {: .copyable }

当需要重新评估跟班的缓存乘数时调用。返回一个数字以修改乘数。修改后的值会传递给下一个回调。

像 BFFs 或蜂巢思维等效果在此时已经应用。

请注意，此回调的结果会被缓存，因此仅在需要时运行。如果添加/移除了带有 `familiarmultiplier` “自定义缓存” 的道具（参见 [items.xml](../xml/items.md)），或者调用了 `familiar:InvalidateCachedMultiplier()`，则会触发此回调。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1225 |MC_EVALUATE_FAMILIAR_MULTIPLIER {: .copyable } | ([EntityFamiliar](../EntityFamiliar.md) Familiar, float Mult, [EntityPlayer](../EntityPlayer.md) Player) | [FamiliarVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/FamiliarVariant.html) | void |

### MC_EVALUATE_STAT {: .copyable }
Used to modify intermediate values of player stat calculations.

???+ note "Note"
	Unless you need to perform complicated conditions/calculations, it is strongly reccomended that you use the new XML item stats features instead of this callback! See [items.xml](../xml/items.md) for more details.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1226 |MC_EVALUATE_STAT {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [EvaluateStatStage](EvaluateStatStage.md) Stat, float CurrentValue) | [EvaluateStatStage](EvaluateStatStage.md) | void |

### MC_PRE_NPC_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 类型的值以修改渲染偏移。

或者接受 `false` 以取消渲染。

???- info "阴影"
    取消此回调不会停止实体阴影的渲染。此问题正在调查中，在此期间，请在 MC_POST_UPDATE 中调用 SetShadowSize(0) 来处理实体阴影。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1081 |MC_PRE_NPC_RENDER {: .copyable } | ([EntityNPC](../EntityNPC.md) NPC, <br>[Vector](../Vector.md) Offset) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | [Vector](../Vector.md) or boolean |

### MC_PRE_NPC_SPLIT {: .copyable }

当游戏即将决定一个 [EntityNPC](../EntityNPC.md) 是否可以分裂时调用，例如肉刀效果。

返回 `true` 可阻止分裂，返回 `false` 可允许分裂（即使该 NPC 在黑名单中），返回 `nil` 则继续默认行为。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1191 |MC_PRE_NPC_SPLIT {: .copyable } | ([EntityNPC](../EntityNPC.md) NPC, <br>boolean IsBlacklisted) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | boolean |

### MC_PRE_OPENGL_RENDER {: .copyable }

在 Manager::Render() 函数调用之前立即调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1136 | MC_PRE_OPENGL_RENDER {: .copyable } | (VertexBuffer, <br>int shaderId, <br>RenderContext) | - | ? |

### MC_PRE_PAUSE_SCREEN_RENDER {: .copyable }

可以返回 `false` 以阻止暂停屏幕的渲染。这样做也会阻止屏幕变暗。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1218 |MC_PRE_PAUSE_SCREEN_RENDER {: .copyable } | ([Sprite](../Sprite.md) PauseBody, <br>[Sprite](../Sprite.md) PauseStats) | - | boolean |

### MC_POST_PAUSE_SCREEN_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1219 |MC_POST_PAUSE_SCREEN_RENDER {: .copyable } | ([Sprite](../Sprite.md) PauseBody, <br>[Sprite](../Sprite.md) PauseStats) | - | void |

### MC_POST_PICKUP_COLLISION {: .copyable }

假设实体的碰撞后代码未被跳过，则在该代码运行之后执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1239 |MC_POST_PICKUP_COLLISION {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup, <br>[Entity](../Entity.md) Collider, <br>boolean Low) | [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) | void |

### MC_PRE_PICKUP_COMPOSTED {: .copyable }

当拾取物被堆肥效果消耗时调用此回调。
接受 `false` 以取消拾取物被消耗。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1267 |MC_PRE_PICKUP_VOIDED {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup) | [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) | boolean |

### MC_PICKUP_GET_COIN_VALUE {: .copyable }

接受 `int` 类型的 CoinValue，以修改拾取硬币时可获得的硬币数量。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1250 |MC_PICKUP_GET_COIN_VALUE {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup) | [CoinSubType](https://wofsauge.github.io/IsaacDocs/rep/enums/CoinSubType.html) | int CoinValue |

### MC_PRE_PICKUP_MORPH {: .copyable }

接受一个参数表：`{EntityType, Variant, SubType, KeepPrice, KeepSeed, IgnoreModifiers}` 或者仅 `{EntityType, Variant, SubType}`。

返回 `false` 可取消变形。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1213 |MC_PRE_PICKUP_MORPH {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup, <br>int EntityType, <br>int Variant, <br>int SubType, <br>boolean KeepPrice, <br>boolean KeepSeed, <br>boolean IgnoreModifiers) | - | table or boolean |

### MC_POST_PICKUP_MORPH {: .copyable }

在变形已经发生之后运行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1215 |MC_POST_PICKUP_MORPH {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup, <br>int PreviousType, <br>int PreviousVariant, <br>int SubType, <br>boolean KeptPrice, <br>boolean KeptSeed, <br>boolean IgnoredModifiers) | - | void |

### MC_PRE_PICKUP_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 类型的值以修改渲染偏移。

或者接受 `false` 以取消渲染。

???- info "阴影"
    取消此回调不会停止实体阴影的渲染。此问题正在调查中，在此期间，请在 MC_POST_UPDATE 中调用 SetShadowSize(0) 来处理实体阴影。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1083 |MC_PRE_PICKUP_RENDER {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup, <br>[Vector](../Vector.md) Offset) | [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.md) | [Vector](../Vector.md) or boolean |

### MC_POST_PICKUP_SHOP_PURCHASE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1062 |MC_POST_PICKUP_SHOP_PURCHASE {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup, <br>[EntityPlayer](../EntityPlayer.md) Player, <br>int MoneySpent) | [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.md) | void |

### MC_PRE_PICKUP_VOIDED_ABYSS {: .copyable }

当拾取物被深渊效果消耗时调用此回调。
接受 `false` 以取消拾取物被消耗。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1266 |MC_PRE_PICKUP_VOIDED_ABYSS {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup) | [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) | boolean |

### MC_PRE_PICKUP_VOIDED {: .copyable }

当拾取物被虚空效果或黑符文消耗时调用此回调。`IsBlackRune` 参数表示消耗源。
如果使用了黑符文，此回调会针对基座道具和变成苍蝇的小拾取物都触发。
接受 `false` 以取消拾取物被消耗。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1265 |MC_PRE_PICKUP_VOIDED {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup, <br>boolean IsBlackRune) | [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) | boolean |

### MC_PRE_PLANETARIUM_APPLY_ITEMS {: .copyable }

在检查进入的宝藏房间数量后，游戏会应用固定的道具出现几率。这是水晶球、魔法 8 球和香肠的几率增加的地方，以及望远镜镜片额外 15% 几率的应用处。

如果你想添加像望远镜镜片这样修改 *基础* 几率的道具，请查看 MC_PRE_PLANETARIUM_APPLY_TELESCOPE_LENS。

接受一个 `float` 类型的值，以修改此计算步骤中的几率。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1113 |MC_PRE_PLANETARIUM_APPLY_ITEMS {: .copyable } | (float Chance) | - | float |

### MC_PRE_PLANETARIUM_APPLY_PLANETARIUM_PENALTY {: .copyable }

在确保当前楼层有效后，游戏会检查之前是否进入过天象馆。如果是，则几率将锁定为 1%（使用望远镜镜片时为 10%）。

如果你想添加像望远镜镜片这样修改 *基础* 几率的道具，请查看 MC_PRE_PLANETARIUM_APPLY_TELESCOPE_LENS。

接受一个 `boolean` 类型的值。返回 `false` 可绕过天象馆进入惩罚。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1111 |MC_PRE_PLANETARIUM_APPLY_PLANETARIUM_PENALTY {: .copyable } | void | - | boolean |

### MC_PRE_PLANETARIUM_APPLY_STAGE_PENALTY {: .copyable }

此回调在天象馆计算开始时运行。在进行计算之前，游戏首先会检查当前楼层是否可以生成天象馆。如果当前楼层无效，则所有后续计算（以及因此所有后续回调）将被取消。

默认情况下，天象馆不能在深牢二层之后生成（使用望远镜镜片时为子宫二层）。

此回调可用于，例如，在自定义楼层上添加自定义的天象馆生成规则，或者添加像望远镜镜片这样可以增强规则的新道具。

接受一个 `boolean` 类型的值。返回 `false` 可绕过天象馆楼层惩罚。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1110 |MC_PRE_PLANETARIUM_APPLY_STAGE_PENALTY {: .copyable } | void | - | boolean |

### MC_PRE_PLANETARIUM_APPLY_TELESCOPE_LENS {: .copyable }

最后，在检查完上述所有条件后，望远镜镜片会在基础概率上额外增加 9% 的概率，使基础生成概率达到 10%。

接受一个 `float` 类型的值，用于修改此计算步骤中的概率。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1114 |MC_PRE_PLANETARIUM_APPLY_TELESCOPE_LENS {: .copyable } | (float Chance) | - | float |

### MC_PRE_PLANETARIUM_APPLY_TREASURE_PENALTY {: .copyable }

在确保之前没有进入过天象馆后，游戏会检查已经进入过多少个宝藏房。如果进入的宝藏房数量大于或等于当前关卡编号，概率将被锁定为 1%（使用望远镜镜片时为 10%）。

如果你想添加一个像望远镜镜片这样修改 *基础* 概率的物品，请查看 `MC_PRE_PLANETARIUM_APPLY_TELESCOPE_LENS`。

接受一个 `boolean` 类型的值。返回 `false` 可以完全绕过天象馆宝藏房惩罚，即游戏会认为没有进入过任何宝藏房。

或者接受一个 `int` 类型的值，用于修改游戏认为已经进入过的宝藏房数量。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1112 |MC_PRE_PLANETARIUM_APPLY_TREASURE_PENALTY {: .copyable } | (int TreasureRoomsVisited) | - | boolean or int |

### MC_POST_PLANETARIUM_CALCULATE {: .copyable }

这将覆盖 *所有* 之前的计算值，最终决定天象馆的生成概率。

接受一个 `float` 类型的值，用于修改概率。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1115 |MC_POST_PLANETARIUM_CALCULATE {: .copyable } | (float Chance) | - | float |

### MC_PRE_PLAYERHUD_RENDER_ACTIVE_ITEM {: .copyable }

接受 `true` 以取消渲染。

If a table is returned instead of a boolean, the following fields can be set to a non-nil value for extra functionality:

* HideItem: Boolean. Determines whether the item should be hidden from the active slot or not.
* HideOutline: Boolean. Deterimins if item outline should be hidden or not.
* HideChargeBar: Boolean. Deterimins if item chargebar should be hidden or not.
* CropOffset: Vector. Deterimins rectangle area of the active item image that will rendered in active slot.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1119 |MC_PRE_PLAYERHUD_RENDER_ACTIVE_ITEM {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>[ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot, <br>[Vector](../Vector.md) Offset, <br>float Alpha, <br>float Scale, <br>[Vector](../Vector.md) ChargeBarOffset) | - | boolean or table |

### MC_POST_PLAYERHUD_RENDER_ACTIVE_ITEM {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1079 |MC_POST_PLAYERHUD_RENDER_ACTIVE_ITEM {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>[ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot, <br>[Vector](../Vector.md) Offset, <br>float Alpha, <br>float Scale, <br>[Vector](../Vector.md) ChargeBarOffset) | - | void |

### MC_PRE_PLAYERHUD_RENDER_HEARTS {: .copyable }

返回 `true` 以取消红心 HUD 的渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1118 |MC_PRE_PLAYERHUD_RENDER_HEARTS {: .copyable } | ([Vector](../Vector.md) Offset, <br>[Sprite](../Sprite.md) HeartsSprite, <br>[Vector](../Vector.md) Position, <br>float SpriteScale, <br>[EntityPlayer](../EntityPlayer.md) Player) | - | boolean |

### MC_POST_PLAYERHUD_RENDER_HEARTS {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1091 |MC_POST_PLAYERHUD_RENDER_HEARTS {: .copyable } | ([Vector](../Vector.md) Offset, <br>[Sprite](../Sprite.md) HeartsSprite, <br>[Vector](../Vector.md) Position, <br>float SpriteScale, <br>[EntityPlayer](../EntityPlayer.md) Player) | - | void |

### MC_PRE_PLAYERHUD_TRINKET_RENDER {: .copyable }

接受返回一个表，该表可以包含以下任意组合的字段：

* Position - 改变饰品的位置。
* Scale - 改变饰品的缩放比例。
* CropOffset - 改变精灵图在其精灵表上的裁剪位置。通过这种方式可以为同一个饰品渲染不同的精灵图，例如猴爪。

或者接受 `true`，这将取消饰品的渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1264 |MC_PRE_PLAYERHUD_TRINKET_RENDER {: .copyable } | (int Slot, <br>[Vector](../Vector.md) Position, <br>float Scale, <br>[EntityPlayer](../EntityPlayer.md) Player, <br>[Vector](../Vector.md) CropOffset) | int Slot | table or boolean |

### MC_PRE_PLAYER_APPLY_INNATE_COLLECTIBLE_NUM {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1092 |MC_PRE_PLAYER_APPLY_INNATE_COLLECTIBLE_NUM {: .copyable } | (int ModCount, <br>[EntityPlayer](../EntityPlayer.md) Player, <br>[CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Type, <br>boolean OnlyCountTrueItems) | - | int |

### MC_POST_PLAYER_COLLISION {: .copyable }

假设该实体的碰撞代码没有被跳过，则在其碰撞代码运行后执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1231 |MC_POST_PLAYER_COLLISION {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>[Entity](../Entity.md) Collider, <br>boolean Low) | [PlayerVariant](PlayerVariant.md) | void |

### MC_PLAYER_GET_ACTIVE_MAX_CHARGE {: .copyable }

接受一个整数，用于更改主动物品的能量条。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1072 |MC_PLAYER_GET_ACTIVE_MAX_CHARGE {: .copyable } | ([CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, <br>[EntityPlayer](../EntityPlayer.md) Player, <br>int VarData, <br>int CurrentMaxCharge) | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | int |

### MC_PLAYER_GET_ACTIVE_MIN_USABLE_CHARGE {: .copyable }

接受一个整数，用于更改使用主动物品所需的最小能量。如果物品当前拥有最小能量，它还会显示白色轮廓。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1073 |MC_PLAYER_GET_ACTIVE_MIN_USABLE_CHARGE {: .copyable } | ([ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot, [EntityPlayer](../EntityPlayer.md) Player, int CurrentMinUsableCharge) | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | int |

### MC_PLAYER_GET_HEALTH_TYPE {: .copyable }

接受一个 [HealthType](HealthType.md) 类型的值，用于更改角色的生命值类型。

???+ warning "Warning"
    Using this callback is often not the most efficient option. For setting a players' default health type, prefer to set their `healthtype` in [players.xml](../xml/players.md). For items, effects and the like, prefer to use the ["healthtype" items.xml customcache](../xml/items.md).

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1067 |MC_PLAYER_GET_HEALTH_TYPE {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [HealthType](HealthType.md) CurrentHealthType, [HealthType](HealthType.md) DefaultHealthType) | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | [HealthType](HealthType.md) |

### MC_PLAYER_HEALTH_TYPE_CHANGE {: .copyable }
Called when a player's health type changes, but before their existing health is corrected to fit their new health type.

After this callback is finished, if the player's new health type does not support red heart containers, they will automatically be converted to an appropriate type (such as to soul hearts or bone hearts).

You may modify the player's health differently within this callback if you so wish, such as removing the heart containers entirely. Just take care not to leave them with no health!

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1128 |MC_PLAYER_HEALTH_TYPE_CHANGE {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [HealthType](HealthType.md) NewHealthType, [HealthType](HealthType.md) PreviousHealthType, [HealthType](HealthType.md) DefaultHealthType) | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | void |

### MC_PLAYER_GET_HEART_LIMIT {: .copyable }

接受一个覆盖值 `integer`，用于设置红心上限。

???- info
    你可以将上限设置为任意值，但游戏在 HUD 中最多只能渲染 4 行红心。不过，即使它们不可见，红心仍然能正常工作。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1074 |MC_PLAYER_GET_HEART_LIMIT {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>int HeartLimit, <br>boolean IsKeeper) | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | int |

### MC_EVALUATE_MULTI_SHOT_PARAMS {: .copyable }
Return a [MultiShotParams](../MultiShotParams.md) object to change the properties of the players shooting behavior in regards to the MultiShotParams object properties. Modified values will be passed along to the remaining callbacks.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1289 |MC_EVALUATE_MULTI_SHOT_PARAMS {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player), [MultiShotParams](../MultiShotParams.md), [WeaponType](https://wofsauge.github.io/IsaacDocs/rep/enums/WeaponType.html) | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | [MultiShotParams](../MultiShotParams.md) |

### MC_PLAYER_INIT_POST_LEVEL_INIT_STATS {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1042 |MC_PLAYER_INIT_POST_LEVEL_INIT_STATS {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player) | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | void |

### MC_PLAYER_INIT_PRE_LEVEL_INIT_STATS {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1127 |MC_PLAYER_INIT_PRE_LEVEL_INIT_STATS {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player) | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | void |

### MC_POST_FORCE_ADD_PILL_EFFECT {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1129 |MC_POST_FORCE_ADD_PILL_EFFECT {: .copyable } | [PillEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/PillEffect.html), [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) | - | void |

### MC_POST_PLAYER_NEW_LEVEL {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1078 |MC_POST_PLAYER_NEW_LEVEL {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, bool FromPlayerUpdate, bool PostLevelInitFinished) | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | void |

### MC_POST_PLAYER_NEW_ROOM_TEMP_EFFECTS {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1077 |MC_POST_PLAYER_NEW_ROOM_TEMP_EFFECTS {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player) | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | void |

### MC_PRE_PLAYER_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 类型的值，用于修改渲染偏移量。

或者接受 `false` 以取消渲染。

???- info "阴影"
    取消此回调不会停止实体阴影的渲染。目前正在对此进行调查，在此期间，请在 `MC_POST_UPDATE` 中对实体调用 `SetShadowSize(0)`。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1082 |MC_PRE_PLAYER_RENDER {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>[Vector](../Vector.md) Offset) | [PlayerVariant](PlayerVariant.md) | [Vector](../Vector.md) or boolean |

### MC_PRE_PLAYER_TAKE_DMG {: .copyable }

比 `MC_ENTITY_TAKE_DMG` 更早运行，即使玩家被认为是无敌的或拥有神圣披风也会触发。

仅接受返回 `false` 以取消伤害。这适用于让玩家获得比其他伤害抵消效果（如神圣披风）更优先的无敌效果。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1008 |MC_PRE_PLAYER_TAKE_DMG {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>float Damage, <br>[DamageFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html) DamageFlags, <br>[EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, <br>int DamageCountdown) | [PlayerVariant](PlayerVariant.md) | boolean |

### MC_PRE_PLAYER_ADD_HEARTS {: .copyable }

在 `Add(...)Hearts` 函数之前运行，允许返回一个值来更改给予的生命值数量。包含参数的函数（例如 `AddMaxHearts` 中的 `ignoreKeeper`）会使用 `OptionalArg` 提供该值。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1009 |MC_PRE_PLAYER_ADD_HEARTS {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>int Amount, <br>[AddHealthType](AddHealthType.md) AddHealthType, <br>boolean OptionalArg) | [AddHealthType](AddHealthType.md) | int |

### MC_POST_PLAYER_ADD_HEARTS {: .copyable }

在 `Add(...)Hearts` 函数和 `MC_PRE_PLAYER_ADD_HEARTS` 回调之后运行。包含参数的函数（例如 `AddMaxHearts` 中的 `ignoreKeeper`）会使用 `OptionalArg` 提供该值。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1010 |MC_POST_PLAYER_ADD_HEARTS {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>int Amount, <br>[AddHealthType](AddHealthType.md) AddHealthType, <br>boolean OptionalArg) | [AddHealthType](AddHealthType.md) | void |

### MC_PRE_PLAYER_TRIGGER_ROOM_CLEAR {: .copyable }

接受 `false` 以取消触发效果。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1069 |MC_PRE_PLAYER_TRIGGER_ROOM_CLEAR {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player) | [PlayerVariant](PlayerVariant.md) | boolean |

### MC_POST_PLAYER_TRIGGER_ROOM_CLEAR {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1138 |MC_POST_PLAYER_TRIGGER_ROOM_CLEAR {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player) | [PlayerVariant](PlayerVariant.md) | void |

### MC_PRE_PLAYER_USE_BOMB {: .copyable }

返回 `false` 以阻止玩家使用炸弹。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1020 |MC_PRE_PLAYER_USE_BOMB {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player) | [PlayerVariant](PlayerVariant.md) | boolean |

### MC_POST_PLAYER_USE_BOMB {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1021 |MC_POST_PLAYER_USE_BOMB {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>[EntityBomb](../EntityBomb.md) Bomb) | [PlayerVariant](PlayerVariant.md) | void |

### MC_POST_BOMB_DAMAGE {: .copyable }
Called after [Game():BombDamage()](https://wofsauge.github.io/IsaacDocs/rep/Game.html#bombdamage) is called, used by the game to damage entities within a radius for explosions and similar effects.

The optional parameter is the [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) of the Source entity, if one exists (the Source can be `nil`).

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1275 |MC_POST_BOMB_DAMAGE {: .copyable } | (Vector Position, float Damage, float Radius, bool LineCheck, [Entity](../Entity.md) Source, [TearFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/TearFlags.html) TearFlags, [DamageFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html) DamageFlags, bool DamageSource) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | void |

### MC_POST_BOMB_TEARFLAG_EFFECTS {: .copyable }
Called after [Game():BombTearflagEffects()](https://wofsauge.github.io/IsaacDocs/rep/Game.html#bombtearflageffects) is called, used by the game when [TearFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/TearFlags.html)-based effects are triggered from an explosion.

The optional parameter is the [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) of the Source entity, if one exists (the Source can be `nil`).

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1276 |MC_POST_BOMB_TEARFLAG_EFFECTS {: .copyable } | (Vector Position, float Radius, [TearFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/TearFlags.html) TearFlags, [Entity](../Entity.md) Source, float RadiusMult) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | void |

### MC_POST_PROJECTILE_COLLISION {: .copyable }

假设该实体的碰撞代码没有被跳过，则在其碰撞代码运行后执行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1245 |MC_POST_PROJECTILE_COLLISION {: .copyable } | ([EntityProjectile](../EntityProjectile.md) Projectile, <br>[Entity](../Entity.md) Collider, <br>boolean Low) | [ProjectileVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/ProjectileVariant.html) | void |

### MC_PRE_PROJECTILE_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 类型的值，用于修改渲染偏移量。

或者接受 `false` 以取消渲染。

???- info "阴影"
    取消此回调不会停止实体阴影的渲染。目前正在对此进行调查，在此期间，请在 `MC_POST_UPDATE` 中对实体调用 `SetShadowSize(0)`。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1085 |MC_PRE_PROJECTILE_RENDER {: .copyable } | ([EntityProjectile](../EntityProjectile.md) Projectile, <br>[Vector](../Vector.md) Offset) | [ProjectileVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/ProjectileVariant.md) | [Vector](../Vector.md) or boolean |

### MC_PRE_RENDER_CUSTOM_CHARACTER_MENU {: .copyable }

不接受返回参数。

???- info "执行信息"
    此回调仅在选择自定义角色时触发，在常规角色上不会触发。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1333 |MC_PRE_RENDER_CUSTOM_CHARACTER_MENU {: .copyable } | ([PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) PlayerType, <br>[Vector](../Vector.md) RenderPos, <br>[Sprite](../Sprite.md) DefaultSprite) | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | void |

### MC_PRE_RENDER_ENTITY_LIGHTING {: .copyable }

接受一个覆盖值 [Vector](../Vector.md)，用于设置偏移量。

或者接受 `false` 以停止渲染。

|:--|:--|:--|:--|:--|
|1152 |MC_PRE_RENDER_ENTITY_LIGHTING {: .copyable } | ([Entity](../Entity.md) Entity, <br>[Vector](../Vector.md) Offset) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | [Vector](../Vector.md) or boolean |

### MC_PRE_RENDER_GRID_LIGHTING {: .copyable }

接受一个覆盖值 [Vector](../Vector.md)，用于设置偏移量。

或者接受 `false` 以停止渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1151 |MC_PRE_RENDER_GRID_LIGHTING {: .copyable } | ([GridEntity](../GridEntity.md) GridEntity, <br>[Vector](../Vector.md) Offset) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) | [Vector](../Vector.md) or boolean |

### MC_PRE_RENDER_PLAYER_BODY {: .copyable }

接受一个覆盖值 `vector`，用于设置渲染位置。

或者接受 `false` 以停止渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1039 |MC_PRE_RENDER_PLAYER_BODY {: .copyable } | ([EntityPlayer](../EntityPlayer.md) player, <br>[Vector](../Vector.md) RenderPos) | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | [Vector](../Vector.md) or boolean |

### MC_PRE_RENDER_PLAYER_HEAD {: .copyable }

接受一个覆盖值 [Vector](../Vector.md)，用于设置渲染位置。

或者接受 `false` 以停止渲染。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1038 |MC_PRE_RENDER_PLAYER_HEAD {: .copyable } | ([EntityPlayer](../EntityPlayer.md) player, <br>[Vector](../Vector.md) RenderPos) | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | [Vector](../Vector.md) or boolean |

### MC_PRE_RENDER {: .copyable }

在 `Manager::Render()` 函数调用之前调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1135 | MC_PRE_RENDER {: .copyable } | void | - | void |

### MC_PRE_REPLACE_SPRITESHEET {: .copyable }

接受一个参数表：`{int LayerID, string PNGFilename}`

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1116 |MC_PRE_REPLACE_SPRITESHEET {: .copyable } | (int LayerID, <br>string PNGFilename) | string ANM2Filename | table |

### MC_POST_REPLACE_SPRITESHEET {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1117 |MC_POST_REPLACE_SPRITESHEET {: .copyable } | (int LayerID, <br>string PNGFilename) | string ANM2Filename | void |

### MC_PRE_RESTOCK_SHOP {: .copyable }

接受 `false` 以取消补货，阻止商店通过补货机重新补货或完全阻止 `Restock` 补货。

???- info "部分补货"
    此回调在 `Room::ShopRestockFull` 和 `Room::ShopRestockPartial` 时都会被调用！`Partial` 用于区分这两种情况。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1070 |MC_PRE_RESTOCK_SHOP {: .copyable } | (boolean Partial) | - | void |

### MC_POST_RESTOCK_SHOP {: .copyable }

不接受返回参数。

???- info "部分补货"
    此回调在 `Room::ShopRestockFull` 和 `Room::ShopRestockPartial` 时都会被调用！`Partial` 用于区分这两种情况。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1071 |MC_POST_RESTOCK_SHOP {: .copyable } | (boolean Partial) | - | void |

### MC_PRE_ROOM_EXIT {: .copyable }

不接受返回参数。

???- info "新关卡"
    当进入新关卡或结束一次游戏时，`NewLevel` 返回 `true`。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1043 |MC_PRE_ROOM_EXIT {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>boolean NewLevel) | - | void |

### MC_POST_ROOM_RENDER_ENTITIES {: .copyable }
Runs after all entities & grid entities in the room have been rendered, but BEFORE effects like overlays, shockwaves, and the mirror world effect are applied.

Rendering done on this callback is also preserved in room transition animations.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1044 |MC_POST_ROOM_RENDER_ENTITIES {: .copyable } | void | - | void |

### MC_PRE_ROOM_GRID_ENTITY_SPAWN {: .copyable }

在房间初始化期间，当布局中的 [GridEntities](../GridEntity.md) 正在生成时调用。

接受 `false` 以取消生成网格，或接受一个表 `{Type, Variant, Vardata, SpawnSeed}` 以修改它。

???+ warning "警告"
    此回调 *不会* 为游戏随机生成的装饰触发！对于这些情况，请使用 `MC_PRE_GRID_ENTITY_SPAWN`。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1192 |MC_PRE_ROOM_GRID_ENTITY_SPAWN {: .copyable } | ([GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) Type, <br>int Variant, <br>int VarData, <br>int GridIdx, <br>int SpawnSeed) | [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) Type | boolean or table |

### MC_PRE_ROOM_TRIGGER_CLEAR {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1068 |MC_PRE_ROOM_TRIGGER_CLEAR {: .copyable } | (boolean PlaySound) | - | void |

### MC_POST_SAVESLOT_LOAD {: .copyable }

每当游戏加载存档槽时调用。

这是你应该用来处理存档数据加载的回调，理想情况下，从正常的 `Mod::LoadData` 到忏悔者标记/成就检查，因为它是在加载这些内容时触发的回调。

第一个参数是你应该关注的存档槽，第二个参数（`isslotselected`）表示正在加载的存档槽是否实际上是从存档菜单屏幕中选择的（如果你想更精细地处理，可以将存档处理限制在此为 `true` 时），第三个参数（`rawslot`）是游戏实际使用的存档槽（不是 API 使用的那个，因为它可能是 0！）。

???+ warning "警告"
    在开始一次游戏之前，此回调会被多次调用，可能是因为自然地切换存档槽，也可能是因为游戏没有正确处理，所以代码需要考虑到这一点，必要时清除之前的数据。
    第三个参数实际上仅用于检查 0 存档槽状态，这是游戏在玩家实际加载存档槽之前默认的状态。在此状态下，模组数据和游戏数据 *不会同步*（模组数据是存档槽 1，而原版游戏数据是存档槽 3）。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1470 |MC_POST_SAVESLOT_LOAD {: .copyable } | (int saveslot, <br>boolean isslotselected, <br>int rawslot) | void | - | void |

### MC_PRE_SFX_PLAY {: .copyable }

接受一个参数表：`{ID, Volume, FrameDelay, Loop, Pitch, Pan}`

或者接受 `false` 以取消声音播放。

???- example "示例代码"
    此代码将强制循环每个声音（无论好坏）。
    ```lua
    function mod:myFunction(ID, Volume, FrameDelay, Loop, Pitch, Pan)
        return {ID, Volume, FrameDelay, true, Pitch, Pan}
    end
    mod:AddCallback(ModCallbacks.MC_PRE_SFX_PLAY, mod.myFunction)
    ```

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1030 |MC_PRE_SFX_PLAY {: .copyable } | (int ID, <br>float Volume, <br>int FrameDelay, <br>boolean Loop, <br>float Pitch, <br>float Pan) | [SoundEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/SoundEffect.html) | table or boolean |

### MC_POST_SFX_PLAY {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1031 |MC_POST_SFX_PLAY {: .copyable } | (int ID, <br>float Volume, <br>int FrameDelay, <br>boolean Loop, <br>float Pitch, <br>float Pan) | [SoundEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/SoundEffect.html) | void |

### MC_PRE_SLOT_COLLISION {: .copyable }

就像原版API中的碰撞回调一样，如果实体先与碰撞器发生碰撞，则低值为true；反之则为false。

返回 `true` 以忽略碰撞，返回 `false` 以发生碰撞但不执行内部代码。

也接受返回一个表，该表可以包含以下任意字段组合：

* Collide: 设置为true可强制实体发生物理碰撞（相互推开），除非“碰撞器”忽略碰撞。设置为false可忽略物理碰撞，但不一定跳过碰撞效果。
* SkipCollisionEffects: 设置为true可跳过此实体的碰撞代码。不影响物理碰撞。不会跳过“碰撞器”的碰撞代码。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1240 |MC_PRE_SLOT_COLLISION {: .copyable } | ([EntitySlot](../EntitySlot.md), <br>[Entity](../Entity.md) Collider, <br>boolean Low) | [SlotVariant](SlotVariant.md) | boolean |

### MC_POST_SLOT_COLLISION {: .copyable }

假设此实体的碰撞代码未被跳过，则在其执行后运行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1241 |MC_POST_SLOT_COLLISION {: .copyable } | ([EntitySlot](../EntitySlot.md), <br>[Entity](../Entity.md) Collider, <br>boolean Low) | [SlotVariant](SlotVariant.md) | void |

### MC_PRE_SLOT_CREATE_EXPLOSION_DROPS {: .copyable }

返回 `false` 可阻止爆炸掉落标准消耗品。例如，这对于允许自定义插槽在爆炸时掉落自己的战利品很有用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1123 |MC_PRE_SLOT_CREATE_EXPLOSION_DROPS {: .copyable } | ([EntitySlot](../EntitySlot.md)) | [SlotVariant](SlotVariant.md) | boolean |

### MC_POST_SLOT_CREATE_EXPLOSION_DROPS {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1124 |MC_POST_SLOT_CREATE_EXPLOSION_DROPS {: .copyable } | ([EntitySlot](../EntitySlot.md)) | [SlotVariant](SlotVariant.md) | void |

### MC_POST_SLOT_INIT {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1121 |MC_POST_SLOT_INIT {: .copyable } | ([EntitySlot](../EntitySlot.md)) | [SlotVariant](SlotVariant.md) | void |

### MC_PRE_SLOT_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移。

或者接受 `false` 以取消渲染。

???- info "阴影"
    取消此回调不会停止实体阴影的渲染。目前正在对此进行调查，在此期间，请在MC_POST_UPDATE中对实体调用SetShadowSize(0)。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1089 |MC_PRE_SLOT_RENDER {: .copyable } | ([EntitySlot](../EntitySlot.md) Slot, <br>[Vector](../Vector.md) Offset) | [SlotVariant](SlotVariant.md) | [Vector](../Vector.md) or boolean |

### MC_POST_SLOT_RENDER {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1090 |MC_POST_SLOT_RENDER {: .copyable } | ([EntitySlot](../EntitySlot.md) Slot, <br>[Vector](../Vector.md) Offset) | [SlotVariant](SlotVariant.md) | void |

### MC_PRE_SLOT_SET_PRIZE_COLLECTIBLE {: .copyable }

由贝壳游戏、地狱游戏和起重机游戏使用。

接受一个 [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) 来覆盖游戏将支付的物品。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1125 |MC_PRE_SLOT_SET_PRIZE_COLLECTIBLE {: .copyable } | ([EntitySlot](../EntitySlot.md), <br>[CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Type) | [SlotVariant](SlotVariant.md) | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) |

### MC_POST_SLOT_SET_PRIZE_COLLECTIBLE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1126 |MC_POST_SLOT_SET_PRIZE_COLLECTIBLE {: .copyable } | ([EntitySlot](../EntitySlot.md), <br>[CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Type) | [SlotVariant](SlotVariant.md) | void |

### MC_PRE_SLOT_UPDATE {: .copyable }

在更新此实体之前调用。

如果应忽略内部AI，则返回 `true`；否则返回 `false` 或 `nil`/不返回任何内容。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1169 |MC_PRE_SLOT_UPDATE {: .copyable } | ([EntitySlot](../EntitySlot.md) Slot) | [SlotVariant](SlotVariant.md) | boolean |

### MC_POST_SLOT_UPDATE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1122 |MC_POST_SLOT_UPDATE {: .copyable } | ([EntitySlot](../EntitySlot.md)) | [SlotVariant](SlotVariant.md) | void |

### MC_POST_TEAR_COLLISION {: .copyable }

假设此实体的碰撞代码未被跳过，则在其执行后运行。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1233 |MC_POST_TEAR_COLLISION {: .copyable } | ([EntityTear](../EntityTear.md) Tear, <br>[Entity](../Entity.md) Collider, <br>boolean Low) | [TearVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/TearVariant.html) | void |

### MC_PRE_TEAR_RENDER {: .copyable }

接受一个 [Vector](../Vector.md) 来修改渲染偏移。

或者接受 `false` 以取消渲染。

???- info "阴影"
    取消此回调不会停止实体阴影的渲染。目前正在对此进行调查，在此期间，请在MC_POST_UPDATE中对实体调用SetShadowSize(0)。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1084 |MC_PRE_TEAR_RENDER {: .copyable } | ([EntityTear](../EntityTear.md) Tear, <br>[Vector](../Vector.md) Offset) | [TearVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/TearVariant.md) | [Vector](../Vector.md) or boolean |

### MC_POST_TRIGGER_COLLECTIBLE_REMOVED {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1095 |MC_POST_TRIGGER_COLLECTIBLE_REMOVED {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>[CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Type, <br>boolean RemoveFromPlayerForm, <br>boolean Wisp ) | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | void |

### MC_PRE_TRIGGER_PLAYER_DEATH {: .copyable }

在游戏结束屏幕出现之前触发，但在游戏检查像1UP这样的原版复活效果之前。

返回 `false` 或调用 `player:Revive()` 可取消死亡，使玩家在原地以半颗心复活。这也将阻止后续回调运行。

???- warning "警告"
    返回false或调用 `player:Revive()` 可能会使当前游戏无法保存。这是因为如果没有待处理的复活，游戏会在死亡动画期间立即删除保存文件，而此回调触发的速度不够快，无法在死亡时注册复活，因为它是在游戏结束屏幕出现之前触发的。

    为了防止这种情况，只有在玩家拥有带有REPENTOGON的“revive”自定义标签的物品或效果时，才尝试让玩家复活，该标签允许物品/效果在HUD上计为额外生命，并防止游戏在玩家死亡时删除游戏保存。有关更多信息和一些示例XML/代码，请参阅 [items.xml](../xml/items.md) 页面。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1050 |MC_PRE_TRIGGER_PLAYER_DEATH {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player) | - | boolean |

### MC_TRIGGER_PLAYER_DEATH_POST_CHECK_REVIVES {: .copyable }

在游戏结束屏幕出现之前触发，但在游戏检查像1UP这样的原版复活效果之后。

返回 `false` 或调用 `player:Revive()` 可取消死亡，使玩家在原地以半颗心复活。这也将阻止后续回调运行。

???- warning "警告"
    返回false或调用 `player:Revive()` 可能会使当前游戏无法保存。这是因为如果没有待处理的复活，游戏会在死亡动画期间立即删除保存文件，而此回调触发的速度不够快，无法在死亡时注册复活，因为它是在游戏结束屏幕出现之前触发的。

    为了防止这种情况，只有在玩家拥有带有REPENTOGON的“revive”自定义标签的物品或效果时，才尝试让玩家复活，该标签允许物品/效果在HUD上计为额外生命，并防止游戏在玩家死亡时删除游戏保存。有关更多信息和一些示例XML/代码，请参阅 [items.xml](../xml/items.md) 页面。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1051 |MC_TRIGGER_PLAYER_DEATH_POST_CHECK_REVIVES {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player) | - | boolean |

### MC_PRE_PLAYER_REVIVE {: .copyable }

在玩家复活之前调用。

返回 `false` 以取消复活。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1481 |MC_PRE_PLAYER_REVIVE {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player) | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | boolean |

### MC_POST_PLAYER_REVIVE {: .copyable }

假设复活未被取消，则在玩家复活后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1482 |MC_POST_PLAYER_REVIVE {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player) | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | void |

### MC_POST_TRIGGER_TRINKET_ADDED {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1096 |MC_POST_TRIGGER_TRINKET_ADDED {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>[TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Type, <br>boolean FirstTimePickingUp) | [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) | void |

### MC_POST_TRIGGER_TRINKET_REMOVED {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1097 |MC_POST_TRIGGER_TRINKET_REMOVED {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>[TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Type) | [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) | void |

### MC_POST_TRIGGER_WEAPON_FIRED {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1098 |MC_POST_TRIGGER_WEAPON_FIRED {: .copyable } | ([Vector](../Vector.md) FireDirection, <br>int FireAmount, <br>[Entity](../Entity.md) Owner, <br>[Weapon](../Weapon.md) Weapon) | [WeaponType](https://wofsauge.github.io/IsaacDocs/rep/enums/WeaponType.html) | void |

### MC_PRE_USE_CARD {: .copyable }

接受 `true` 以取消卡片使用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1064 |MC_PRE_USE_CARD {: .copyable } | ([Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.md) ID, <br>[EntityPlayer](../EntityPlayer.md) Player, <br>int UseFlag) | - | boolean |

### MC_PRE_USE_PILL {: .copyable }

接受 `true` 以取消药丸使用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1065 |MC_PRE_USE_PILL {: .copyable } | ([PillEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/PillEffect.md) ID, <br>[PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.md) PillColor, <br>[EntityPlayer](../EntityPlayer.md) Player, <br>int UseFlag) | - | boolean |

### MC_POST_WEAPON_FIRE {: .copyable }

不接受返回参数。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1105 |MC_POST_WEAPON_FIRE {: .copyable } | ([Weapon](../Weapon.md) Weapon, <br>[Vector](../Vector.md) FireDirection, <br>boolean IsShooting, <br>boolean IsInterpolated) | [WeaponType](https://wofsauge.github.io/IsaacDocs/rep/enums/WeaponType.html) | void |

### MC_PRE_PICKUP_GET_LOOT_LIST {: .copyable }

在拾取物确定其战利品内容之前调用。接受一个 [LootList](../LootList.md) 来更改战利品内容。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1334 |MC_PRE_PICKUP_GET_LOOT_LIST {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup, <br>boolean ShouldAdvance) | - | [LootList](../LootList.md) |

### MC_PRE_PICKUP_UPDATE_GHOST_PICKUPS {: .copyable }

在将战利品内容的幽灵拾取物应用到拾取物之前调用。返回 `true` 以将拾取物幽灵应用到你的拾取物实体，返回 `false` 以取消它。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1335 |MC_PRE_PICKUP_UPDATE_GHOST_PICKUPS {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup | void | boolean |

### MC_POST_PLAYER_ADD_EFFECT {: .copyable }
Called after the [TemporaryEffect](https://wofsauge.github.io/IsaacDocs/rep/TemporaryEffect.html) of an [ItemConfigItem](../ItemConfig_Item.md) is added to a player.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1273 |MC_POST_PLAYER_ADD_EFFECT {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>[ItemConfigItem](../ItemConfig_Item.md), <br>boolean addCostume, int Count) | [ItemConfigItem](../ItemConfig_Item.md) | void |

### MC_POST_ROOM_ADD_EFFECT {: .copyable }
Called after the [TemporaryEffect](https://wofsauge.github.io/IsaacDocs/rep/TemporaryEffect.html) of an [ItemConfigItem](../ItemConfig_Item.md) is added to the room.

[Room](../Room.md) has its own [TemporaryEffects](https://wofsauge.github.io/IsaacDocs/rep/TemporaryEffects.html) that are accessed through [Room::GetEffects()](../Room.md#geteffects)

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1274 |MC_POST_ROOM_ADD_EFFECT {: .copyable } | ([ItemConfigItem](../ItemConfig_Item.md)) | [ItemConfigItem](../ItemConfig_Item.md) | void |

### MC_POST_PLAYER_TRIGGER_EFFECT_REMOVED {: .copyable }
Called after the [TemporaryEffect](https://wofsauge.github.io/IsaacDocs/rep/TemporaryEffect.html) of an [ItemConfigItem](../ItemConfig_Item.md) is removed from a player.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1268 |MC_POST_PLAYER_TRIGGER_EFFECT_REMOVED {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>[ItemConfigItem](../ItemConfig_Item.md), <br>int Count) | [ItemConfigItem](../ItemConfig_Item.md) | void |

### MC_POST_ROOM_TRIGGER_EFFECT_REMOVED {: .copyable }
Called after the [TemporaryEffect](https://wofsauge.github.io/IsaacDocs/rep/TemporaryEffect.html) of an [ItemConfigItem](../ItemConfig_Item.md) is removed from the room.

[Room](../Room.md) has its own [TemporaryEffects](https://wofsauge.github.io/IsaacDocs/rep/TemporaryEffects.html) that are accessed through [Room::GetEffects()](../Room.md#geteffects).

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1269 |MC_POST_ROOM_TRIGGER_EFFECT_REMOVED {: .copyable } | ([ItemConfigItem](../ItemConfig_Item.md)) | [ItemConfigItem](../ItemConfig_Item.md) | void |

### MC_PRE_PLAYER_GRID_COLLISION {: .copyable }

在该实体与 [GridEntity](../GridEntity.md) 或其他实心网格方块碰撞之前调用。

返回 `true` 以忽略碰撞。

???+ warning "警告"
    `GridEntity` 可能为nil，因为如果 [GridPath](https://wofsauge.github.io/IsaacDocs/rep/Room.html#getgridpath) 值 >= 1000，实体可能会与“空”网格索引发生碰撞。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1171 |MC_PRE_PLAYER_GRID_COLLISION {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, int GridIndex, [GridEntity](../GridEntity.md) GridEntity) | [PlayerVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerVariant.html) | boolean |

### MC_PLAYER_GRID_COLLISION {: .copyable }

假设碰撞未被跳过，则在该实体与网格碰撞时调用。

???+ warning "警告"
    `GridEntity` 可能为nil，因为如果 [GridPath](https://wofsauge.github.io/IsaacDocs/rep/Room.html#getgridpath) 值 >= 1000，实体可能会与“空”网格索引发生碰撞。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1172 |MC_PLAYER_GRID_COLLISION {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, int GridIndex, [GridEntity](../GridEntity.md) GridEntity) | [PlayerVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerVariant.html) | boolean |

### MC_PRE_TEAR_GRID_COLLISION {: .copyable }

在该实体与 [GridEntity](../GridEntity.md) 或其他实心网格方块碰撞之前调用。

返回 `true` 以忽略碰撞。

???+ warning "警告"
    `GridEntity` 可能为nil，因为如果 [GridPath](https://wofsauge.github.io/IsaacDocs/rep/Room.html#getgridpath) 值 >= 1000，实体可能会与“空”网格索引发生碰撞。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1173 |MC_PRE_TEAR_GRID_COLLISION {: .copyable } | ([EntityTear](../EntityTear.md) Tear, int GridIndex, [GridEntity](../GridEntity.md) GridEntity) | [TearVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/TearVariant.html) | boolean |

### MC_TEAR_GRID_COLLISION {: .copyable }

假设碰撞未被跳过，则在该实体与网格碰撞时调用。

???+ warning "警告"
    `GridEntity` 可能为nil，因为如果 [GridPath](https://wofsauge.github.io/IsaacDocs/rep/Room.html#getgridpath) 值 >= 1000，实体可能会与“空”网格索引发生碰撞。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1174 |MC_TEAR_GRID_COLLISION {: .copyable } | ([EntityTear](../EntityTear.md) Tear, int GridIndex, [GridEntity](../GridEntity.md) GridEntity) | [TearVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/TearVariant.html) | boolean |

### MC_PRE_FAMILIAR_GRID_COLLISION {: .copyable }

在该实体与 [GridEntity](../GridEntity.md) 或其他实心网格方块碰撞之前调用。

返回 `true` 以忽略碰撞。

???+ warning "警告"
    `GridEntity` 可能为nil，因为如果 [GridPath](https://wofsauge.github.io/IsaacDocs/rep/Room.html#getgridpath) 值 >= 1000，实体可能会与“空”网格索引发生碰撞。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1175 |MC_PRE_FAMILIAR_GRID_COLLISION {: .copyable } | ([EntityFamiliar](../EntityFamiliar.md) Familiar, int GridIndex, [GridEntity](../GridEntity.md) GridEntity) | [FamiliarVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/FamiliarVariant.html) | boolean |

### MC_FAMILIAR_GRID_COLLISION {: .copyable }

假设碰撞未被跳过，则在该实体与网格碰撞时调用。

???+ warning "警告"
    `GridEntity` 可能为nil，因为如果 [GridPath](https://wofsauge.github.io/IsaacDocs/rep/Room.html#getgridpath) 值 >= 1000，实体可能会与“空”网格索引发生碰撞。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1176 |MC_FAMILIAR_GRID_COLLISION {: .copyable } | ([EntityFamiliar](../EntityFamiliar.md) Familiar, int GridIndex, [GridEntity](../GridEntity.md) GridEntity) | [FamiliarVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/FamiliarVariant.html) | boolean |

### MC_PRE_BOMB_GRID_COLLISION {: .copyable }

在该实体与 [GridEntity](../GridEntity.md) 或其他实心网格方块碰撞之前调用。

返回 `true` 以忽略碰撞。

???+ warning "警告"
    `GridEntity` 可能为nil，因为如果 [GridPath](https://wofsauge.github.io/IsaacDocs/rep/Room.html#getgridpath) 值 >= 1000，实体可能会与“空”网格索引发生碰撞。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1177 |MC_PRE_BOMB_GRID_COLLISION {: .copyable } | ([EntityBomb](../EntityBomb.md) Bomb, int GridIndex, [GridEntity](../GridEntity.md) GridEntity) | [BombVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/BombVariant.html) | boolean |

### MC_BOMB_GRID_COLLISION {: .copyable }

假设碰撞未被跳过，则在该实体与网格碰撞时调用。

???+ warning "警告"
    `GridEntity` 可能为nil，因为如果 [GridPath](https://wofsauge.github.io/IsaacDocs/rep/Room.html#getgridpath) 值 >= 1000，实体可能会与“空”网格索引发生碰撞。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1178 |MC_BOMB_GRID_COLLISION {: .copyable } | ([EntityBomb](../EntityBomb.md) Bomb, int GridIndex, [GridEntity](../GridEntity.md) GridEntity) | [BombVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/BombVariant.html) | boolean |

### MC_PRE_PICKUP_GRID_COLLISION {: .copyable }

在该实体与 [GridEntity](../GridEntity.md) 或其他实心网格方块碰撞之前调用。

返回 `true` 以忽略碰撞。

???+ warning "警告"
    `GridEntity` 可能为nil，因为如果 [GridPath](https://wofsauge.github.io/IsaacDocs/rep/Room.html#getgridpath) 值 >= 1000，实体可能会与“空”网格索引发生碰撞。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1179 |MC_PRE_PICKUP_GRID_COLLISION {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup, int GridIndex, [GridEntity](../GridEntity.md) GridEntity) | [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) | boolean |

### MC_PICKUP_GRID_COLLISION {: .copyable }

假设碰撞未被跳过，则在该实体与网格碰撞时调用。

???+ warning "警告"
    `GridEntity` 可能为nil，因为如果 [GridPath](https://wofsauge.github.io/IsaacDocs/rep/Room.html#getgridpath) 值 >= 1000，实体可能会与“空”网格索引发生碰撞。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1180 |MC_PICKUP_GRID_COLLISION {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup, int GridIndex, [GridEntity](../GridEntity.md) GridEntity) | [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) | boolean |

### MC_PRE_PROJECTILE_GRID_COLLISION {: .copyable }

在该实体与 [GridEntity](../GridEntity.md) 或其他实心网格方块碰撞之前调用。

返回 `true` 以忽略碰撞。

???+ warning "警告"
    `GridEntity` 可能为nil，因为如果 [GridPath](https://wofsauge.github.io/IsaacDocs/rep/Room.html#getgridpath) 值 >= 1000，实体可能会与“空”网格索引发生碰撞。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1181 |MC_PRE_PROJECTILE_GRID_COLLISION {: .copyable } | ([EntityProjectile](../EntityProjectile.md) Projectile, int GridIndex, [GridEntity](../GridEntity.md) GridEntity) | [ProjectileVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/ProjectileVariant.html) | boolean |

### MC_PROJECTILE_GRID_COLLISION {: .copyable }

假设碰撞未被跳过，则在该实体与网格碰撞时调用。

???+ warning "警告"
    `GridEntity` 可能为nil，因为如果 [GridPath](https://wofsauge.github.io/IsaacDocs/rep/Room.html#getgridpath) 值 >= 1000，实体可能会与“空”网格索引发生碰撞。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1182 |MC_PROJECTILE_GRID_COLLISION {: .copyable } | ([EntityProjectile](../EntityProjectile.md) Projectile, int GridIndex, [GridEntity](../GridEntity.md) GridEntity) | [ProjectileVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/ProjectileVariant.html) | boolean |

### MC_PRE_NPC_GRID_COLLISION {: .copyable }

在该实体与 [GridEntity](../GridEntity.md) 或其他实心网格方块碰撞之前调用。

返回 `true` 以忽略碰撞。

???+ warning "警告"
    `GridEntity` 可能为nil，因为如果 [GridPath](https://wofsauge.github.io/IsaacDocs/rep/Room.html#getgridpath) 值 >= 1000，实体可能会与“空”网格索引发生碰撞。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1183 |MC_PRE_NPC_GRID_COLLISION {: .copyable } | ([EntityNPC](../EntityNPC.md) NPC, int GridIndex, [GridEntity](../GridEntity.md) GridEntity) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | boolean |

### MC_NPC_GRID_COLLISION {: .copyable }

假设碰撞未被跳过，则在该实体与网格碰撞时调用。

???+ warning "警告"
    `GridEntity` 可能为nil，因为如果 [GridPath](https://wofsauge.github.io/IsaacDocs/rep/Room.html#getgridpath) 值 >= 1000，实体可能会与“空”网格索引发生碰撞。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1184 |MC_NPC_GRID_COLLISION {: .copyable } | ([EntityNPC](../EntityNPC.md) NPC, int GridIndex, [GridEntity](../GridEntity.md) GridEntity) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | boolean |

### MC_POST_PROJECTILE_DEATH {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1032 |MC_POST_PROJECTILE_DEATH {: .copyable } | ([EntityProjectile](../EntityProjectile.md) Projectile) | [ProjectileVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/ProjectileVariant.html) | void |

### MC_POST_TEAR_DEATH {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1033 |MC_POST_TEAR_DEATH {: .copyable } | ([EntityTear](../EntityTear.md) Tear) | [TearVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/TearVariant.html) | void |

### MC_POST_BOSS_INTRO_SHOW {: .copyable }

不接受返回参数。

在BOSS介绍初始化后立即调用。`BossID2` 用于双人组合BOSS。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1270 |MC_POST_BOSS_INTRO_SHOW {: .copyable } | ([BossType](BossType.md) BossID1, [BossType](BossType.md) BossID2) | - | void |

### MC_POST_ROOM_TRANSITION_UPDATE {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1271 |MC_POST_ROOM_TRANSITION_UPDATE {: .copyable } | void | int TransitionMode | void |

### MC_POST_ROOM_TRANSITION_RENDER {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1272 |MC_POST_ROOM_TRANSITION_RENDER {: .copyable } | void | int TransitionMode | void |

### MC_PRE_PLAYER_ADD_COSTUME {: .copyable }

在将服装添加到玩家之前调用。返回 [ItemConfigItem](../ItemConfig_Item.md) 以替换服装，或返回 `true` 以完全取消添加。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1281 |MC_PRE_PLAYER_ADD_COSTUME {: .copyable } | ([ItemConfigItem](../ItemConfig_Item.md) ItemConfig, [EntityPlayer](../EntityPlayer.md) Player, boolean ItemStateOnly) | - | [ItemConfigItem](../ItemConfig_Item.md) ItemConfig or boolean |

### MC_PRE_PLAYER_REMOVE_COSTUME {: .copyable }
Called before the costume is removed to the player. Return `true` to cancel the removal.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1282 |MC_PRE_PLAYER_ADD_COSTUME {: .copyable } | ([ItemConfigItem](../ItemConfig_Item.md) ItemConfig, [EntityPlayer](../EntityPlayer.md) Player, boolean ItemStateOnly) | - | boolean |

### MC_POST_PLAYER_ADD_COSTUME {: .copyable }

假设添加未被跳过，则在将服装添加到玩家之后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1283 |MC_POST_PLAYER_ADD_COSTUME {: .copyable } | ([ItemConfigItem](../ItemConfig_Item.md) ItemConfig, [EntityPlayer](../EntityPlayer.md) Player, boolean ItemStateOnly) | - | void |

### MC_POST_PLAYER_REMOVE_COSTUME {: .copyable }

假设移除未被跳过，则在从玩家移除服装之后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1284 |MC_POST_PLAYER_ADD_COSTUME {: .copyable } | ([ItemConfigItem](../ItemConfig_Item.md) ItemConfig, [EntityPlayer](../EntityPlayer.md) Player, boolean ItemStateOnly) | - | void |

### MC_PRE_TRIGGER_BED_SLEEP_EFFECT {: .copyable }
Called if Bed target (bed.Target) is set to player and "SleepFillHP" item overlay sprite's event is triggered, and before the hearts addition is applied.

Return `true` to cancel vanilla behavior.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1285 |MC_PRE_TRIGGER_BED_SLEEP_EFFECT {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>[EntityPickup](../EntityPickup.md) Bed) | - | boolean |

### MC_POST_TRIGGER_BED_SLEEP_EFFECT {: .copyable }
Called if Bed target (bed.Target) is set to player and "SleepFillHP" item overlay sprite's event is triggered, and after the hearts addition is applied.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1286 |MC_POST_TRIGGER_BED_SLEEP_EFFECT {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>[EntityPickup](../EntityPickup.md) Bed) | - | void |

### MC_PRE_PLAYER_POCKET_ITEMS_SWAP {: .copyable }
Called when the player swaps their pocket items using the action drop button (even if they are empty).

Return `true` to cancel pocket item swap.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1287 |MC_PRE_PLAYER_POCKET_ITEMS_SWAP {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player) | - | boolean |

### MC_PRE_BED_SLEEP {: .copyable }
Triggers on bed collision and before playing sleep sequence.

Return `true` to cancel vanilla behavior.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1288 |MC_PRE_BED_SLEEP {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, <br>[EntityPickup](../EntityPickup.md) Bed) | - | boolean |

### MC_PRE_PLAYER_UPDATE {: .copyable }

在更新此实体之前调用。

如果应忽略内部AI，则返回 `true`；否则返回 `false` 或 `nil`/不返回任何内容。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1160 |MC_PRE_PLAYER_UPDATE {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player) | [PlayerVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerVariant.html) | boolean |

### MC_PRE_TEAR_UPDATE {: .copyable }

在更新此实体之前调用。

如果应忽略内部AI，则返回 `true`；否则返回 `false` 或 `nil`/不返回任何内容。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1161 |MC_PRE_TEAR_UPDATE {: .copyable } | ([EntityTear](../EntityTear.md) Tear) | [TearVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/TearVariant.html) | boolean |

### MC_PRE_FAMILIAR_UPDATE {: .copyable }

在更新此实体之前调用。

如果应忽略内部AI，则返回 `true`；否则返回 `false` 或 `nil`/不返回任何内容。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1162 |MC_PRE_FAMILIAR_UPDATE {: .copyable } | ([EntityFamiliar](../EntityFamiliar.md) Familiar) | [FamiliarVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/FamiliarVariant.html) | boolean |

### MC_PRE_BOMB_UPDATE {: .copyable }

在更新此实体之前调用。

如果应忽略内部AI，则返回 `true`；否则返回 `false` 或 `nil`/不返回任何内容。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1163 |MC_PRE_BOMB_UPDATE {: .copyable } | ([EntityBomb](../EntityBomb.md) Bomb) | [BombVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/BombVariant.html) | boolean |

### MC_PRE_PICKUP_UPDATE {: .copyable }

在更新此实体之前调用。

如果应忽略内部AI，则返回 `true`；否则返回 `false` 或 `nil`/不返回任何内容。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1164 |MC_PRE_PICKUP_UPDATE {: .copyable } | ([EntityPickup](../EntityPickup.md) Pickup) | [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) | boolean |

### MC_PRE_KNIFE_UPDATE {: .copyable }

在更新此实体之前调用。

如果应忽略内部AI，则返回 `true`；否则返回 `false` 或 `nil`/不返回任何内容。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1165 |MC_PRE_KNIFE_UPDATE {: .copyable } | ([EntityKnife](../EntityKnife.md) Knife) | [KnifeSubType](KnifeSubType.md) | boolean |

### MC_PRE_PROJECTILE_UPDATE {: .copyable }

在更新此实体之前调用。

如果应忽略内部AI，则返回 `true`；否则返回 `false` 或 `nil`/不返回任何内容。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1166 |MC_PRE_PROJECTILE_UPDATE {: .copyable } | ([EntityProjectile](../EntityProjectile.md) Projectile) | [ProjectileVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/ProjectileVariant.html) | boolean |

### MC_PRE_LASER_UPDATE {: .copyable }

在更新此实体之前调用。

如果应忽略内部AI，则返回 `true`；否则返回 `false` 或 `nil`/不返回任何内容。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1167 |MC_PRE_LASER_UPDATE {: .copyable } | ([EntityLaser](../EntityLaser.md) Laser) | [LaserVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/LaserVariant.html) | boolean |

### MC_PRE_EFFECT_UPDATE {: .copyable }

在更新此实体之前调用。

如果应忽略内部AI，则返回 `true`；否则返回 `false` 或 `nil`/不返回任何内容。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1168 |MC_PRE_EFFECT_UPDATE {: .copyable } | ([EntityEffect](../EntityEffect.md) Effect) | [EffectVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/EffectVariant.html) | boolean |

### MC_PRE_FORTUNE_DISPLAY {: .copyable }

在显示运势之前调用。

返回 `false` 以取消显示运势。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1483 |MC_PRE_FORTUNE_DISPLAY {: .copyable } | void | - | boolean |

### MC_PRE_ITEM_TEXT_DISPLAY {: .copyable }

在显示物品文本之前调用。

`IsSticky` 为 `true` 表示物品文本会在屏幕上无限期停留，即按住地图键时。`IsCurseDisplay` 为 `true` 表示文本用于显示诅咒。

返回 `false` 以取消显示物品文本。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1484 |MC_PRE_ITEM_TEXT_DISPLAY {: .copyable } | (string Title, string Subtitle, boolean IsSticky, boolean IsCurseDisplay) | - | boolean |

### MC_GET_STATUS_EFFECT_TARGET {: .copyable }
Return an [Entity](../Entity.md) to change targets

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1485 |MC_GET_STATUS_EFFECT_TARGET {: .copyable } | ([Entity](../Entity.md) Entity) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | [Entity](../Entity.md) |

### MC_PRE_ENTITY_SET_COLOR {: .copyable }
Fires when Entity:SetColor is called

Return a color to override the color. The overridden color is passed into MC_POST_ENTITY_SET_COLOR.
Return `false` to cancel the color change. Prevents MC_POST_ENTITY_SET_COLOR from firing.

This only fires for [Entity:SetColor](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#setcolor) and does not fire when changing the entity's color directly.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1486 |MC_PRE_ENTITY_SET_COLOR {: .copyable } | ([Entity](../Entity.md) Entity, <br>[Color](../Color.md) Color, <br>int Duration, <br>int Priority, <br>boolean FadeOut, <br>boolean Share) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | boolean OR [Color](../Color.md) |

### MC_POST_ENTITY_SET_COLOR {: .copyable }
Fires when Entity:SetColor is called

This only fires for [Entity:SetColor](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#setcolor) and does not fire when changing the entity's color directly.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1487 |MC_POST_ENTITY_SET_COLOR {: .copyable } | ([Entity](../Entity.md) Entity, <br>[Color](../Color.md) Color, <br>int Duration, <br>int Priority, <br>boolean FadeOut, <br>boolean Share) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | void |

### MC_POST_START_AMBUSH_WAVE {: .copyable }
Fires at the start of a challenge/boss rush room wave.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1488 |MC_POST_START_AMBUSH_WAVE {: .copyable } | (boolean BossAmbush) | - | void |

### MC_POST_START_GREED_WAVE {: .copyable }
Fires at the start of a Greed Mode wave.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1489 |MC_POST_START_GREED_WAVE {: .copyable } | void | - | void |

### MC_EVALUATE_TEAR_HIT_PARAMS {: .copyable }
Used to modify mutable TearParams object.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1490 |MC_EVALUATE_TEAR_HIT_PARAMS {: .copyable } | [EntityPlayer](../EntityPlayer.md),<br>[TearParams](https://wofsauge.github.io/IsaacDocs/rep/TearParams.html),<br>[WeaponType](https://wofsauge.github.io/IsaacDocs/rep/enums/WeaponType.html),<br>float DamageScale,<br>integer TearDisplacement,<br>[Entity](../Entity.md) Source | [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) | void |

### MC_PRE_GET_RANDOM_ROOM_INDEX {: .copyable }

当游戏希望在楼层上获取一个随机可用房间索引时调用。

返回一个整数以覆盖目标房间索引。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1290 |MC_PRE_GET_RANDOM_ROOM_INDEX {: .copyable } | (int RoomIndex, bool IAmErrorRoom, int Seed) | - | int |

### MC_PRE_GLOWING_HOURGLASS_SAVE {: .copyable }

在保存发光沙漏状态后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1302 |MC_PRE_GLOWING_HOURGLASS_SAVE {: .copyable } | (int Slot) | - | void |

### MC_POST_GLOWING_HOURGLASS_SAVE {: .copyable }

在保存发光沙漏状态后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1300 |MC_POST_GLOWING_HOURGLASS_SAVE {: .copyable } | (int Slot) | - | void |

### MC_PRE_GLOWING_HOURGLASS_LOAD {: .copyable }

在加载发光沙漏状态后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1303 |MC_PRE_GLOWING_HOURGLASS_LOAD {: .copyable } | (int Slot) | - | void |

### MC_POST_GLOWING_HOURGLASS_LOAD {: .copyable }

在加载发光沙漏状态后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1301 |MC_POST_GLOWING_HOURGLASS_LOAD {: .copyable } | (int Slot) | - | void |

### MC_PRE_ROOM_RESTORE_STATE {: .copyable }
Fires before the room respawns all saved entities.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1305 |MC_PRE_ROOM_RESTORE_STATE {: .copyable } | [Room](../Room.md), [RoomDescriptor](../RoomDescriptor.md) | - | void |

### MC_POST_ROOM_SAVE_STATE {: .copyable }
Fires after the room saves all entities and grid entities.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1304 |MC_POST_ROOM_SAVE_STATE {: .copyable } | [Room](../Room.md), [RoomDescriptor](../RoomDescriptor.md) | - | void |

### MC_POST_SWAP_ROOMS {: .copyable }
Fires after two rooms have been swapped, due to Curse of the Maze.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1306 |MC_POST_SWAP_ROOMS {: .copyable } | [RoomDescriptor](../RoomDescriptor.md), [RoomDescriptor](../RoomDescriptor.md) | - | void |

### MC_POST_BACKWARDS_ROOM_SAVE {: .copyable }
Fires after a room has been saved; to then be restored when generating the Ascent.
The string key (e.g. "boss_0", "treasure_0") identifies which slot the room was saved in.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1307 |MC_POST_BACKWARDS_ROOM_SAVE {: .copyable } | [LevelStage](https://wofsauge.github.io/IsaacDocs/rep/enums/LevelStage.html), [RoomDescriptor](../RoomDescriptor.md), string Key | - | void |

### MC_POST_BACKWARDS_ROOM_RESTORE {: .copyable }
Fires when generating the Ascent layout and one of the previously saved rooms is restored.
The string key (e.g. "boss_0", "treasure_0") identifies which slot the room was saved into.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1308 |MC_POST_BACKWARDS_ROOM_RESTORE {: .copyable } | [LevelStage](https://wofsauge.github.io/IsaacDocs/rep/enums/LevelStage.html), [RoomDescriptor](../RoomDescriptor.md), string Key | - | void |

### MC_PRE_PLAYER_ADD_CARD {: .copyable }

在将卡片添加到玩家库存之前调用。

返回 [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html) 以更改要添加的卡片，或返回 `false` 以完全取消添加。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1350 |MC_PRE_PLAYER_ADD_CARD {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html) CardID, [PillCardSlot](PillCardSlot.md) Slot) | [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html) | boolean or int |

### MC_POST_PLAYER_ADD_CARD {: .copyable }

在将卡片添加到玩家库存之后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1351 |MC_POST_PLAYER_ADD_CARD {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html) CardID, [PillCardSlot](PillCardSlot.md) Slot) | [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html) | void |

### MC_PRE_PLAYER_ADD_PILL {: .copyable }

在将药丸添加到玩家库存之前调用。

返回 [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) 以更改要添加的药丸，或返回 `false` 以完全取消添加。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1352 |MC_PRE_PLAYER_ADD_PILL {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) PillColor, [PillCardSlot](PillCardSlot.md) Slot) | [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) | boolean or int |

### MC_POST_PLAYER_ADD_PILL {: .copyable }

在将药丸添加到玩家库存之后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1353 |MC_POST_PLAYER_ADD_PILL {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) PillColor, [PillCardSlot](PillCardSlot.md) Slot) | [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) | void |

### MC_POST_PLAYER_REMOVE_CARD {: .copyable }

在通过任何方式（丢弃、直接移除、使用等）从玩家库存中移除卡片后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1354 |MC_POST_PLAYER_REMOVE_CARD {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html) CardID, [PillCardSlot](PillCardSlot.md) Slot) | [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html) | void |

### MC_POST_PLAYER_REMOVE_PILL {: .copyable }

在通过任何方式（丢弃、直接移除、使用等）从玩家库存中移除药丸后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1355 |MC_POST_PLAYER_REMOVE_PILL {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) CardID, [PillCardSlot](PillCardSlot.md) Slot) | [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) | void |

### MC_PRE_PLAYER_COLLECT_CARD {: .copyable }

在玩家从地上捡起卡片之前调用。

返回 `false` 以阻止捡起卡片。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1356 |MC_PRE_PLAYER_COLLECT_CARD {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [EntityPickup](../EntityPickup.md) Pickup) | [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html) | boolean |

### MC_POST_PLAYER_COLLECT_CARD {: .copyable }

在玩家从地上捡起卡片之后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1357 |MC_POST_PLAYER_COLLECT_CARD {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [EntityPickup](../EntityPickup.md) Pickup) | [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html) | void |

### MC_PRE_PLAYER_COLLECT_PILL {: .copyable }

在玩家从地上捡起药丸之前调用。

返回 `false` 以阻止捡起药丸。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1358 |MC_PRE_PLAYER_COLLECT_PILL {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [EntityPickup](../EntityPickup.md) Pickup) | [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) | boolean |

### MC_POST_PLAYER_COLLECT_PILL {: .copyable }

在玩家从地上捡起药丸之后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1359 |MC_POST_PLAYER_COLLECT_PILL {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [EntityPickup](../EntityPickup.md) Pickup) | [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) | void |

### MC_POST_PLAYER_DROP_CARD {: .copyable }

在玩家从库存中丢弃卡片到地上之后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1360 |MC_POST_PLAYER_DROP_CARD {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [EntityPickup](../EntityPickup.md) Pickup, [PillCardSlot](PillCardSlot.md) Slot) | [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html) | void |

### MC_POST_PLAYER_DROP_PILL {: .copyable }

在玩家从库存中丢弃药丸到地上之后调用。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1361 |MC_POST_PLAYER_DROP_PILL {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [EntityPickup](../EntityPickup.md) Pickup, [PillCardSlot](PillCardSlot.md) Slot) | [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) | void |

### MC_POST_PLAYER_DROP_TRINKET {: .copyable }
Called after a player drops a trinket onto the ground from their inventory.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1144 |MC_POST_PLAYER_DROP_TRINKET {: .copyable } | ([TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html), [Vector](../Vector.md) DropPos, [EntityPlayer](../EntityPlayer.md) Player, boolean IsGoldenTrinket, boolean ReplaceTick) | [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) | void |

### MC_PRE_FAMILIAR_CAN_CHARM {: .copyable }
Fires when `EntityFamiliar:CanCharm` is called. This is typically used by Siren's familiar charm attack.

Return `false` to prevent the familiar from being charmed.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1473 |MC_PRE_FAMILIAR_CAN_CHARM {: .copyable } | ([EntityFamiliar](../EntityFamiliar.md) Familiar) | [FamiliarVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/FamiliarVariant.html) | boolean |

### MC_PRE_PLAYER_GIVE_BIRTH_CAMBION {: .copyable }

在玩家受到伤害后，该回调在Cambion Conception（该物品效果为受伤后概率生成一个跟班）生成跟班之前调用。

返回 `false` 以阻止添加跟班。

请注意，如果取消此操作，游戏在达到下一次所需的伤害量之前不会尝试生成另一个跟班，并且在此处取消生成仍会计入Cambion Conception通常的4次跟班生成限制。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1474 |MC_PRE_PLAYER_GIVE_BIRTH_CAMBION {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [ConceptionFamiliarFlag](ConceptionFamiliarFlag.md)) | [ConceptionFamiliarFlag](ConceptionFamiliarFlag.md) | boolean |

### MC_PRE_PLAYER_GIVE_BIRTH_IMMACULATE {: .copyable }

在玩家受到伤害后，该回调在Immaculate Conception（该物品效果为收集一定数量的心后生成一个跟班）生成跟班之前调用。

返回 `false` 以阻止添加跟班。

请注意，如果取消此操作，游戏在再收集15颗心之前不会尝试生成另一个跟班。与Cambion Conception不同，Immaculate Conception在所有可用的原版跟班都已获得之前不会停止尝试生成跟班。

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1475 |MC_PRE_PLAYER_GIVE_BIRTH_IMMACULATE {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [ConceptionFamiliarFlag](ConceptionFamiliarFlag.md)) | [ConceptionFamiliarFlag](ConceptionFamiliarFlag.md) | boolean |

### MC_PRE_APPLY_TEARFLAG_EFFECTS {: .copyable }
Called before the effects of [TearFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/TearFlags.html) are applied to an enemy upon being hit or damaged by virtually any source entity (tears, lasers, certain effects, etc). Note that the source can also be `nil`.

Can be triggered by mods using [EntityNPC::ApplyTearflagEffects()](../EntityNPC.md#applytearflageffects).

Return `false` to prevent application of effects, or return a table to modify certain values:

* Position
* TearFlags
* Damage

Please note that the optional parameter is the [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) of the **Source** entity.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1277 |MC_PRE_APPLY_TEARFLAG_EFFECTS {: .copyable } | ([EntityNPC](../EntityNPC.md) NPC, [Vector](../Vector.md) Position, [TearFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/TearFlags.html) TearFlags, [Entity](../Entity.md) Source, float Damage) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | boolean or table |

### MC_POST_APPLY_TEARFLAG_EFFECTS {: .copyable }
Called after the effects of [TearFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/TearFlags.html) are applied to an enemy upon being hit or damaged by virtually any source entity (tears, lasers, certain effects, etc). Great for on-hit effects! Note that the source can be `nil`.

Can be triggered by mods using [EntityNPC::ApplyTearflagEffects()](../EntityNPC.md#applytearflageffects).

Please note that the optional parameter is the [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) of the **Source** entity.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1278 |MC_POST_APPLY_TEARFLAG_EFFECTS {: .copyable } | ([EntityNPC](../EntityNPC.md) NPC, [Vector](../Vector.md) Position, [TearFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/TearFlags.html) TearFlags, [Entity](../Entity.md) Source, float Damage) | [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) | void |

### MC_TRY_ADD_TO_BAG_OF_CRAFTING {: .copyable }
Called before a pickup is "added" to the player's Bag of Crafting.

The provided table contains the [BagOfCraftingPickups](BagOfCraftingPickup.md) that would be added to the bag. **Note that this table can be empty**, if the pickup would not normally provide any pickups!

Return false to prevent the pickup from being added. Return a different table of [BagOfCraftingPickups](BagOfCraftingPickup.md) to modify what is going to be added.

If false is returned, or the pickup does not provide any [BagOfCraftingPickups](BagOfCraftingPickup.md), it will be knocked away instead of "collected".

???+ note "Note"
	For custom pickups, please prefer to set their `bagofcrafting` attribute in [entities2.xml](../xml/entities.md) instead!

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1015 |MC_TRY_ADD_TO_BAG_OF_CRAFTING {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [EntityPickup](../EntityPickup.md) Pickup, [BagOfCraftingPickup](BagOfCraftingPickup.md)[] BagOfCraftingPickupsTable) | [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) | boolean or table |

### MC_POST_ADD_TO_BAG_OF_CRAFTING {: .copyable }
Called after a pickup is successfully "added" to the player's Bag of Crafting.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1016 |MC_POST_ADD_TO_BAG_OF_CRAFTING {: .copyable } | ([EntityPlayer](../EntityPlayer.md) Player, [EntityPickup](../EntityPickup.md) Pickup) | [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) PickupVariant | void |

### MC_POST_ITEM_OVERLAY_RENDER {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1139 |MC_POST_ITEM_OVERLAY_RENDER  {: .copyable } | ([Giantbook](Giantbook.md) Giantbook) | [Giantbook](Giantbook.md) | void |

### MC_POST_DISCHARGE_ACTIVE_ITEM {: .copyable }

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1140 |MC_POST_DISCHARGE_ACTIVE_ITEM {: .copyable } | ([CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, boolean CollectibleRemoved, [EntityPlayer](../EntityPlayer.md) Player, [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html?h=activeslot) slot) | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | void |

### MC_PRE_OPEN_CHEST {: .copyable }
Fires before a chest is opened. Return false to prevent it from opening.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1491 |MC_PRE_OPEN_CHEST  {: .copyable } | ([PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) PickupVariant, [EntityPlayer](../EntityPlayer.md) Player) | [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) | boolean |

### MC_POST_OPEN_CHEST {: .copyable }
Fires after a chest opened.

|ID|Name|Function Args|Optional Args|Return Type|
|:--|:--|:--|:--|:--|
|1492 |MC_POST_OPEN_CHEST  {: .copyable } | ([PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) PickupVariant, [EntityPlayer](../EntityPlayer.md) Player) | [PickupVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/PickupVariant.html) | void |

