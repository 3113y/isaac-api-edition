---
tags:
  - Class
---
# Class "GridEntitiesSaveStateVector"

表示网格实体保存状态描述集合的向量，可按索引或网格实体类型读取元素，并支持获取元素数量。

## Functions
### Get () {: aria-label='Functions' }
#### [GridEntityDesc](https://wofsauge.github.io/IsaacDocs/rep/GridEntityDesc.html) Get ( int Index ) {: .copyable aria-label='Functions' }

按索引返回对应的网格实体描述。

___
### GetByType () {: aria-label='Functions' }
#### [GridEntityDesc](https://wofsauge.github.io/IsaacDocs/rep/GridEntityDesc.html) GetByType ( [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) Type ) {: .copyable aria-label='Functions' }

按网格实体类型返回对应的网格实体描述。

___
### __len () {: aria-label='Operators' }
#### int __len ( ) {: .copyable aria-label='Operators' }

返回向量中的元素数量。

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
