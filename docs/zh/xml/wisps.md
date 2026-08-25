---
tags:
  - File
---
# 文件 "wisps.xml"
此文件用于定义由美德之书生成的魂火跟班的属性。

**Resource-Folder**{: .xmlInfo }：在模组的resource文件夹中使用此文件尚未经过测试。

**Content-Folder**{: .xmlInfo }：在模组的content文件夹中使用此文件尚未经过测试。

### "color" 节点
用于定义locust（蝗虫）可拥有的颜色。

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
| name | str | 颜色名称，在"locust"节点中引用 |
| r | int | 红色分量 |
| g | int | 绿色分量 |
| b | int | 蓝色分量 |
| or | int | 红色偏移量 |
| og | int | 蓝色偏移量 |
| ob | int | 绿色偏移量 |

### "wisp" 节点
| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
| id | string | 美德之书激活时，主动栏内收集物的ID |
| canShoot | bool | 若魂火跟班不能射击则设为false |
| coreColor | string | 魂火跟班核心使用的颜色名称 |
| coreGfx | string ||
| count | int | 生成的locust数量 |
| damage | int | 魂火跟班造成的伤害 |
| damageMultiplier2 | int ||
| fireDelay | int ||
| flameColor | string | 魂火火焰使用的颜色名称 |
| hp | int ||
| layer | int | 可用值：['-1', '0', '1', '2'] |
| priority | int | 可用值：['-1', '99'] |
| procChance | ['0.075', '0.05', '0.025', '0.1', '0.2', '0.3', '0.15', '0.33'] ||
| shotSpeed | int ||
| tearColor | string | 魂火眼泪使用的颜色名称 |
| tearColor2 | string | 魂火眼泪使用的颜色名称 |
| tearFlags | int ||
| tearFlags2 | int ||
| tearScale | int ||
| tearScale2 | string ||
| tearVariant | int ||
