---
tags:
  - Class
---
# Class "ImGui"

An example mod using the ImGui class can be found [here.](./examples/ImGuiMenu.md)

???+ info

    You can get this class by using the global table "ImGui"

    ???+ example "Example Code"

        ```lua
        local isblind = ImGui.GetVisible("braillemenu")
        ```
    ### Reference

    对于元素类型，我们使用与 ImGui 本身相同的名称。查看 **[交互式 ImGui 示例](https://pthom.github.io/imgui_manual_online/manual/imgui_manual.html)**。
    
    ### Icons

    所有 ImGui 文本都支持使用图标。目前，我们使用 "FontAwesome 6"，它提供约 1400 个图标。你可以在此处搜索合适的图标：[https://fontawesome.com/search?o=r&m=free&s=solid](https://fontawesome.com/search?o=r&m=free&s=solid)

    **Lua 中的图标用法**：

    如果你想在小部件中添加图标，只需使用图标的 "Unicode" 表示形式，并将其放在 `\u{ }` 字符串中。你可以通过在 FontAwesome 页面上选择图标，然后查看弹出窗口的右上角来找到它。你可以像这样将其添加到元素中：

    `"\u{f0f9} My Text"`

    这将在文本 "My text" 前面添加 "truck-medical" 图标。

    输出: ":fontawesome-solid-truck-medical: My Text"

___
## Functions

### AddButton () {: aria-label='Functions' }
#### void AddButton ( string ParentId, string ElementId, string Label = "", function ClickCallback = nil, boolean IsSmall = false ) {: .copyable aria-label='Functions' }

___
### AddCallback () {: aria-label='Functions' }
#### void AddCallback ( string ElementId, [ImGuiCallback](enums/ImGuiCallback.md) Type, Function func ) {: .copyable aria-label='Functions' }
为 ImGui 元素添加回调。一个元素每种类型只能有一个回调。

### AddCheckbox () {: aria-label='Functions' }
#### void AddCheckbox ( string ParentId, string ElementId, string Label = "", function ChangeCallback = nil, boolean IsActive = false ) {: .copyable aria-label='Functions' }

___
### AddCombobox () {: aria-label='Functions' }
#### void AddCombobox ( string ParentId, string ElementId, string Label = "", function ChangeCallback = nil, table Options, int SelectedIndex = 0, boolean IsSlider = false ) {: .copyable aria-label='Functions' }
添加一个组合框元素，它表示一个单行元素，允许你从下拉菜单中选择一个值。如果 `isSlider` 设置为 true，则可以通过与滑块元素交互来选择值，而不是使用下拉菜单。

???+ example "示例代码"

    ```lua
    ImGui.AddCombobox("catInput", "combobox1", "Combobox", function(index, val) print(index, val) end, { "Item 1", "Item 2", "Item 3" }, 1)
    ```

___
### AddDragFloat () {: aria-label='Functions' }
#### void AddDragFloat ( string ParentId, string ElementId, string Label = "", function ChangeCallback = nil, float DefaultVal = 0, float Speed = 1, float Min = INTEGER_MIN, float Min = INTEGER_MAX, string Formatting = "%.3f" ) {: .copyable aria-label='Functions' }

___
### AddDragInteger () {: aria-label='Functions' }
#### void AddDragInteger ( string ParentId, string ElementId, string Label = "", function ChangeCallback = nil, int DefaultVal = 0, float Speed = 1, int Min = INTEGER_MIN, int Min = INTEGER_MAX, string Formatting = "%d%" ) {: .copyable aria-label='Functions' }

___
### AddElement () {: aria-label='Functions' }
#### void AddElement ( string ParentId, string ElementId = "", [ImGuiElement](enums/ImGuiElement.md) type, string Label = "" ) {: .copyable aria-label='Functions' }
向给定的父元素添加一个通用元素。对于添加像 "SameLine"、"Bullet" 或 "Text" 这样的控制元素很有用.

___
### AddInputColor () {: aria-label='Functions' }
#### void AddInputColor ( string ParentId, string ElementId, string Label = "", function ChangeCallback = nil, float r = 0, float g = 0, float b = 0) {: .copyable aria-label='Functions' }
添加一个颜色输入元素。如果设置了参数 `a`，则它作为 RGBA 输入。否则，它只是一个 RGB 输入。浮点值在 `0` 到 `1` 之间.

回调函数会分别传入 r、g、b 和 a 值作为参数.

???+ example "Example Code"

    ```lua
    ImGui.AddInputColor("catInput", "inputColorRGB", "RGB input", function(r, g, b) print(r, g, b) end, 1, 0.25, 0.45)
    ImGui.AddInputColor("catInput", "inputColorRGBA", "RGBA input", function(r, g, b, a) print(r, g, b, a) end, 0.5, 0.5, 0.5,0.5)
    ```
___
### AddInputController () {: aria-label='Functions' }
#### void AddInputController ( string ParentId, string ElementId, string ButtonLabel = "", function ChangeCallback = nil, float DefaultVal = 0 ) {: .copyable aria-label='Functions' }
回调函数会传入 [ButtonAction ID](https://wofsauge.github.io/IsaacDocs/rep/enums/ButtonAction.html) 和新按钮的 ImGuiKey 名称.

添加一个用于游戏手柄 / 控制器按钮的输入.

___
### AddInputFloat () {: aria-label='Functions' }
#### void AddInputFloat ( string ParentId, string ElementId, string Label = "", function ChangeCallback = nil, float DefaultVal = 0, float Step = 1, float StepFast = 100  ) {: .copyable aria-label='Functions' }

___
### AddInputInteger () {: aria-label='Functions' }
#### void AddInputInteger ( string ParentId, string ElementId, string Label = "", function ChangeCallback = nil, int DefaultVal = 0, int Step = 1, int StepFast = 100  ) {: .copyable aria-label='Functions' }

___
### AddInputKeyboard () {: aria-label='Functions' }
#### void AddInputKeyboard ( string ParentId, string ElementId, string ButtonLabel = "", function ChangeCallback = nil, float DefaultVal = 0 ) {: .copyable aria-label='Functions' }
添加一个用于键盘按钮的输入.

回调函数会传入 [Keyboard key ID](https://wofsauge.github.io/IsaacDocs/rep/enums/Keyboard.html) 和新按钮的 ImGuiKey 名称.

___
### AddInputText () {: aria-label='Functions' }
#### void AddInputText ( string ParentId, string ElementId, string Description = "", function ChangeCallback = nil, string DefaultVal = "", string HintText = "" ) {: .copyable aria-label='Functions' }
添加一个文本输入元素。如果元素的输入为空，`HintText` 中的文本将作为“占位符”显示在输入元素内。

___
### AddInputTextMultiline () {: aria-label='Functions' }
#### void AddInputTextMultiline ( string ParentId, string ElementId, string Description = "", function ChangeCallback = nil, string DefaultVal = "", float DisplayedLines = 6 ) {: .copyable aria-label='Functions' }
添加一个允许输入多行文本的文本输入元素。`displayedLines` 属性可用于更改元素的高度。

___
### AddPlotHistogram () {: aria-label='Functions' }
#### void AddPlotHistogram ( string ParentId, string ElementId, string Label = "", table Values, string OverlayText = "", float Minimum = FLT_MIN, float Maximum = FLT_MAX, float Height = 40 ) {: .copyable aria-label='Functions' }
添加一个柱状图，将给定的数据显示为垂直条形。默认情况下，最小值和最大值是“动态”设置的，使图表能够完美适配其内容。

___
### AddPlotLines () {: aria-label='Functions' }
#### void AddPlotLines ( string ParentId, string ElementId, string Label = "", table Values, string OverlayText = "", float Minimum = FLT_MIN, float Maximum = FLT_MAX, float Height = 40 ) {: .copyable aria-label='Functions' }
添加一个折线图，使用线条连接给定的值。默认情况下，最小值和最大值是“动态”设置的，使图表能够完美适配其内容。

___
### AddProgressBar () {: aria-label='Functions' }
#### void AddProgressBar ( string ParentId, string ElementId, string Label = "", float Progress = 0, string OverlayText = "__DEFAULT__" ) {: .copyable aria-label='Functions' }
添加一个进度条元素。`progress` 值定义了填充百分比（范围从 `0` 到 `1`）。
如果未定义 `overlayText`，进度条将在进度条内显示当前的填充状态百分比（例如，当 `progress` 设置为 0.5 时显示 50%）。

如果 `label` 为空，进度条将在父元素的整个宽度上渲染。

___
### AddRadioButtons () {: aria-label='Functions' }
#### void AddRadioButtons ( string ParentId, string ElementId, function ChangeCallback = nil, table options, int SelectedIndex = 0, boolean renderSameLine = true ) {: .copyable aria-label='Functions' }
???+ example "Example Code"

    ```lua
    ImGui.AddRadioButtons("catInput", "radioButtons", function(index) print(index) end, { "Radio 1", "Radio 2", "Radio 3" }, 1)
    ```

___
### AddSliderFloat () {: aria-label='Functions' }
#### void AddSliderFloat ( string ParentId, string ElementId, string Label = "", function ChangeCallback = nil, float DefaultVal = 0, float Min = INTEGER_MIN, float Max = INTEGER_MAX, string Formatting = "%.3f" ) {: .copyable aria-label='Functions' }

___
### AddSliderInteger () {: aria-label='Functions' }
#### void AddSliderInteger ( string ParentId, string ElementId, string Label = "", function ChangeCallback = nil, int DefaultVal = 0, int Min = INTEGER_MIN, int Max = INTEGER_MAX, string Formatting = "%d%" ) {: .copyable aria-label='Functions' }

___
### AddTab () {: aria-label='Functions' }
#### void AddTab ( string ParentId, string ElementId, string Label ) {: .copyable aria-label='Functions' }
父对象必须是一个标签栏（TabBar）。
标签（Tab）是一个可点击的区域，点击后会显示另一个页面或区域。

___
### AddTabBar () {: aria-label='Functions' }
#### void AddTabBar ( string ParentId, string ElementId ) {: .copyable aria-label='Functions' }
标签栏（TabBar）是一个用于存储标签（Tab）元素的容器。

___
### AddText () {: aria-label='Functions' }
#### void AddText ( string ParentId, string Text, boolean WrapText = false, string ElementId = "" ) {: .copyable aria-label='Functions' }
如果后续代码需要编辑该文本，也可以设置元素 ID。
创建一个文本元素。如果 `wrapText` 设置为 `true`，文本将在窗口边界处换行；如果设置为 `false`，窗口内容将扩展直到文本适应。

___
### CreateMenu () {: aria-label='Functions' }
#### void CreateMenu ( string ElementId, string Label = "" ) {: .copyable aria-label='Functions' }
在《以撒的结合：忏悔》拓展模组 REPOTOGON 的主菜单栏中创建一个条目。

___
### CreateWindow () {: aria-label='Functions' }
#### void CreateWindow ( string ElementId, string Title = "" ) {: .copyable aria-label='Functions' }
创建一个窗口对象。你需要使用 `LinkWindowToElement()` 或 `SetVisible()` 来切换窗口的可见性。

___
### ElementExists () {: aria-label='Functions' }
#### boolean ElementExists ( string ElementId ) {: .copyable aria-label='Functions' }
如果具有给定 ID 的元素已经存在，则返回 `true`。

___
### GetMousePosition () {: aria-label='Functions' }
#### void GetMousePosition ( ) {: .copyable aria-label='Functions' }
返回鼠标在屏幕坐标中的位置。
在使用 ImGui 时，请使用此函数代替 `Input.GetMousePosition()`！

___
### GetVisible () {: aria-label='Functions' }
#### boolean GetVisible ( string ElementId ) {: .copyable aria-label='Functions' }
获取窗口元素是否可见。

___
### GetWindowChildFlags () {: aria-label='Functions' }
#### [ImGuiChildFlags](enums/ImGuiChildFlags.md) GetWindowChildFlags ( ) {: .copyable aria-label='Functions' }
Get visual setting flags for the window, specific for its usecase as a child.
___
### GetWindowFlags () {: aria-label='Functions' }
#### [ImGuiWindowFlags](enums/ImGuiWindowFlags.md) GetWindowFlags ( ) {: .copyable aria-label='Functions' }
Get visual setting flags for the window.
___
### GetWindowPinned () {: aria-label='Functions' }
#### boolean GetWindowPinned ( string WindowId ) {: .copyable aria-label='Functions' }
获取窗口的固定状态。

___
### Hide () {: aria-label='Functions' }
#### void Hide ( ) {: .copyable aria-label='Functions' }
关闭 ImGui。

___
### ImGuiToWorld () {: aria-label='Functions' }
#### void ImGuiToWorld ( [Vector](Vector.md) Position ) {: .copyable aria-label='Functions' }
将 ImGui 坐标转换为世界坐标。

???+ bug "Bug"

    当游戏的缩放因子超过最大渲染缩放时，此函数无法正常工作。

___
### IsVisible () {: aria-label='Functions' }
#### boolean IsVisible ( ) {: .copyable aria-label='Functions' }
当玩家正在积极使用 ImGui 时调用。这不会由“固定”窗口触发。

___
### LinkWindowToElement () {: aria-label='Functions' }
#### void LinkWindowToElement ( string WindowId, string ElementId ) {: .copyable aria-label='Functions' }
将窗口或弹出元素连接到另一个元素，使该元素充当该窗口的“开关

???- example "示例代码"

    ```lua
    此代码创建一个新的菜单条目，其中包含一个菜单项，点击该菜单项会切换一个窗口
    ImGui.CreateMenu("myMenu", "Test Menu")
    ImGui.AddElement("myMenu", "myButton", ImGuiElement.MenuItem, "Some Text")
    ImGui.CreateWindow("myWindow", "Some Window title")
    ImGui.LinkWindowToElement("myWindow", "myButton")
    ```

___
### PushNotification () {: aria-label='Functions' }
#### void PushNotification ( string Text, [ImGuiNotificationType](enums/ImGuiNotificationType.md) notificationType = 0, int lifetime = 5000 ) {: .copyable aria-label='Functions' }        
以通知样式显示一个弹出消息窗口。

___
### RemoveCallback () {: aria-label='Functions' }
#### void RemoveCallback ( string ElementId, [ImGuiCallback](enums/ImGuiCallback.md) type ) {: .copyable aria-label='Functions' }
从元素中移除指定类型的回调函数。

___
### RemoveColor () {: aria-label='Functions' }
#### void RemoveColor ( string ElementId, [ImGuiColor](enums/ImGuiColor.md) colorType ) {: .copyable aria-label='Functions' }
从元素中移除指定类型的颜色修饰符。

___
### RemoveElement () {: aria-label='Functions' }
#### void RemoveElement ( string ElementId ) {: .copyable aria-label='Functions' }
用于移除任何类型元素的通用函数。

___
### RemoveMenu () {: aria-label='Functions' }
#### void RemoveMenu ( string ElementId ) {: .copyable aria-label='Functions' }

___
### RemoveWindow () {: aria-label='Functions' }
#### void RemoveWindow ( string ElementId ) {: .copyable aria-label='Functions' }

___
### Reset () {: aria-label='Functions' }
#### void Reset ( ) {: .copyable aria-label='Functions' }
移除所有自定义定义的 ImGui 元素，并将 ImGui 恢复到其原始状态。

___
### SetColor () {: aria-label='Functions' }
#### void SetColor ( string ElementId, [ImGuiColor](enums/ImGuiColor.md) ColorType, float r, float g, float b, float a = 1.0 ) {: .copyable aria-label='Functions' }
为指定元素添加颜色修饰符。

___
### SetHelpmarker () {: aria-label='Functions' }
#### void SetHelpmarker ( string ElementId, string Text ) {: .copyable aria-label='Functions' }
为指定元素添加一个帮助标记。帮助标记是一个显示在元素右侧的 `(?)` 元素，当鼠标悬停在其上时会显示一个工具提示。

___
### SetSize () {: aria-label='Functions' }
#### void SetSize ( string elementID, float width, float Height ) {: .copyable aria-label='Functions' }
Sets the width and height of an element in pixels. Most regular form-elements only allow for width changes. Windows, Buttons and Plots do allow for width and height changes.

If the width is equal 0, the element will try to fill all available space in the window (Default behavior). 

If the value is negative, the element will fill the full width of the window, minus the number of pixels defined.
Example: The window is 500px wide. A width of -75 will make the element 425px wide.
___
### SetTextColor () {: aria-label='Functions' }
#### void SetTextColor ( string ElementId, float r, float g, float b, float a = 1.0 ) {: .copyable aria-label='Functions' }
为指定元素的文本添加颜色修饰符的快捷函数。

___
### SetTooltip () {: aria-label='Functions' }
#### void SetTooltip ( string ElementId, string Text ) {: .copyable aria-label='Functions' }
为指定元素添加一个工具提示。当用户将鼠标悬停在该元素上时，工具提示将显示出来。

___
### SetVisible () {: aria-label='Functions' }
#### void SetVisible ( string ElementId, boolean Visible ) {: .copyable aria-label='Functions' }

___
### SetWindowChildFlags () {: aria-label='Functions' }
#### void SetWindowChildFlags ( [ImGuiChildFlags](enums/ImGuiChildFlags.md) newFlags ) {: .copyable aria-label='Functions' }
Set visual setting flags for the window, specific for its usecase as a child.
___
### SetWindowFlags () {: aria-label='Functions' }
#### void SetWindowFlags ( [ImGuiWindowFlags](enums/ImGuiWindowFlags.md) newFlags ) {: .copyable aria-label='Functions' }
Set visual setting flags for the window.
___
### SetWindowPinned () {: aria-label='Functions' }
#### void SetWindowPinned ( string WindowId, boolean Pinned ) {: .copyable aria-label='Functions' }
设置窗口的固定状态，使窗口在 ImGui 界面未激活时也保持可见。

___
### SetWindowPosition () {: aria-label='Functions' }
#### void SetWindowPosition ( string WindowId, float x, float y ) {: .copyable aria-label='Functions' }
在屏幕坐标中设置窗口的位置。

___
### SetWindowSize () {: aria-label='Functions' }
#### void SetWindowSize ( string WindowId, float width, float Height ) {: .copyable aria-label='Functions' }
Deprecated. Now does the same as [SetSize()](#setsize).
___
### Show () {: aria-label='Functions' }
#### void Show ( ) {: .copyable aria-label='Functions' }
打开 ImGui 界面。

___
### UpdateData () {: aria-label='Functions' }
#### void UpdateData ( string ElementId, [ImGuiData](enums/ImGuiData.md) DataType, int NewDataValue ) {: .copyable aria-label='Functions' }
更新指定元素的任意数据。有关可能更新的数据，请参阅 [ImGuiData](enums/ImGuiData.md)。

数据类型和预期的新数据值是针对每个元素进行评估的。因此，如果你尝试更新某个元素中未使用的数据，此函数将抛出错误。

___
### UpdateText () {: aria-label='Functions' }
#### void UpdateText ( string ElementId, string Text ) {: .copyable aria-label='Functions' }
更新元素文本或标签的快捷函数。

___
### WorldToImGui () {: aria-label='Functions' }
#### void WorldToImGui ( [Vector](Vector.md) Position ) {: .copyable aria-label='Functions' }
将世界坐标转换为 ImGui 坐标。

???+ bug "Bug"

    当游戏的缩放因子超过最大渲染缩放时，此函数无法正常工作。

___