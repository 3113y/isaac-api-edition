---
tags:
  - Global
  - Class
---
# Global Class "Console"

???+ info

    You can get this class by using the `Console` global table.

    **注意：调用这些函数时，必须使用 .（句点）而非 :（冒号）！**
    
    ???+ example "Example Code"

        ```lua
        local cmdhistory = Console.GetCommandHistory()
        ```
        
        
## Functions

### GetCommandHistory () {: aria-label='Functions' }
#### string[] GetCommandHistory ( ) {: .copyable aria-label='Functions' }
返回一个包含当前命令历史记录的表格。

___
### GetHistory () {: aria-label='Functions' }
#### string[] GetHistory ( ) {: .copyable aria-label='Functions' }
返回一个包含本次游戏运行期间所有先前打印到控制台条目的表格。
该表格的排列顺序是从最新到最旧 —— 第一个条目将是当前等待用户输入的空白行，接着是上一次打印的内容，依此类推。最后一行始终是 `忏悔版控制台`。

___
### PopHistory () {: aria-label='Functions' }
#### void PopHistory ( int Amount = 1 ) {: .copyable aria-label='Functions' }
从历史记录中移除先前的行。可以选择使用 `amount` 参数来指定应移除多少个条目。控制台中当前等待用户输入的行算作历史记录的一部分，但在 C++ 端已经对此进行了处理。

___
### PrintError () {: aria-label='Functions' }
#### void PrintError ( string Error ) {: .copyable aria-label='Functions' }
将错误信息打印到控制台，错误信息以红色文本显示。

___
### PrintWarning () {: aria-label='Functions' }
#### void PrintWarning ( string Warning ) {: .copyable aria-label='Functions' }
将Warning信息打印到控制台，Warning信息以黄色文本显示。

___
### RegisterCommand () {: aria-label='Functions' }
#### void RegisterCommand ( string Name, string Desc, string HelpText, boolean ShowOnMenu, [AutocompleteType](enums/AutocompleteType.md) Type ) {: .copyable aria-label='Functions' }
在新控制台中注册一个命令。这些命令将显示在新控制台的自动补全列表中。
* 输入 `help` 命令时将显示 `Desc`（描述）。
* 输入 `help (Name)` 时将显示 `HelpText`（帮助文本）。
* `AutocompleteType`（自动补全类型）将使该命令继承该自动补全类型。如果该命令不属于任何标准类型，请使用 `CUSTOM`（自定义）并结合 [MC_CONSOLE_AUTOCOMPLETE](enums/ModCallbacks.md#mc_console_autocomplete) 为此命令创建一个定制的自动补全类型。

___
### RegisterMacro () {: aria-label='Functions' }
#### void RegisterMacro ( string Name, string[] Commands ) {: .copyable aria-label='Functions' }
* `Commands`（命令）是一个字符串表格，包含应按顺序执行的命令。
在新控制台中注册一个宏。这些宏将显示在新控制台 `macro` 命令的自动补全列表中。

___