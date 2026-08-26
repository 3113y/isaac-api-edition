---
tags:
  - Global
---
# 全局变量“REPENTOGON”

此全局变量提供与 Repentogon 相关的函数和变量，例如当前版本和更新日志等。它是一个**表**。

可在任意位置访问此变量。

## 函数

表中的所有函数都是静态函数：使用点号（`.`）运算符访问，而不是冒号（`:`）运算符。

### MeetsVersion () {: aria-label='Functions' }
#### boolean MeetsVersion ( string version ) {: .copyable aria-label='Functions' }

检查指定的 `version` 是否小于或等于当前安装的 Repentogon 版本。换言之，如果满足指定版本，则返回 `true`。

函数会在数字边界处分割 `version`，并将生成的令牌与当前 `REPENTOGON.Version` 中的对应令牌逐一比较，满足以下任一条件时立即返回：指定版本令牌更低时返回 `true`，更高时返回 `false`；所有令牌都相等时返回 `true`。版本中的字母会被静默丢弃；如果 `REPENTOGON.Version` 为 `"dev build"`，函数始终返回 `true`。

???+ bug
    在 Repentogon 1.0.10b 之前，此函数存在缺陷，会始终返回 `true`。

___
