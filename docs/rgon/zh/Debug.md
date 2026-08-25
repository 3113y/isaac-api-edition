---
tags:
  - Global
  - Class
---
# Global Class "Debug"

???+ info

    你可以通过 `Debug` 全局表获取这个类.

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
返回已加载到 LUA 环境中的所有文件的列表。

___