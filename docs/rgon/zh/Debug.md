---
tags:
  - Global
  - Class
---
# Global Class "Debug"

???+ info

    可通过 `Debug` 全局表访问此类。

    **注意：调用这些函数时，必须使用 .（句点）而非 :（冒号）！**
    
    ???+ example "Example Code"
    
        ```lua
        local loadedFiles = Debug.ListLoadedFiles()
        ```
        
## Functions

### ForceUnload () {: aria-label='Functions' }
#### void ForceUnload ( string ModuleName ) {: .copyable aria-label='Functions' }

___
### GetSignature () {: aria-label='Functions' }
#### string GetSignature ( int Address ) {: .copyable aria-label='Functions' }

___
### ListLoadedFiles () {: aria-label='Functions' }
#### string[] ListLoadedFiles ( ) {: .copyable aria-label='Functions' }
返回所有已加载至 Lua 环境的文件列表。

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
