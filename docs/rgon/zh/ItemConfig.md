---
tags:
  - Class
---
# Class "ItemConfig"

## Functions

### CanRerollCollectible () {: aria-label='Functions' }
#### boolean CanRerollCollectible ( int ID ) {: .copyable aria-label='Functions' }
???- bug "Bug"
尽管该函数不是静态函数，但必须使用 `.` 调用，例如 `Isaac.GetItemConfig().CanRerollCollectible(1)`。
如果该收藏品可以重置，则返回 `true`。

### GetTaggedItems () {: aria-label='Functions' }
#### [ItemConfig_Item](ItemConfig_Item.md)[] GetTaggedItems ( int Tags ) {: .copyable aria-label='Functions' }
返回一个包含指定标签的 [ItemConfig_Item](ItemConfig_Item.md) 对象表。

___
### IsValidTrinket () {: aria-label='Functions' }
#### boolean IsValidTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) TrinketType ) {: .copyable aria-label='Functions' }
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

