---
tags:
  - Class
---
# Class "GenericPrompt"

???+ info

	你可以通过其构造函数获取此类 or using the following functions:

	* [Game:GetGenericPrompt()](Game.md#getgenericprompt)

	???+ example "Example Code"

		This code creates a generic popup that opens when pressing the "Minus"-button. It prints the selected option to the console and displays some dummy text. 

		```lua
		local myPrompt = GenericPrompt()
		myPrompt:Initialize()
		myPrompt:SetText("Some test text")

		local wasPromptDisplayed = false

		function mod:myRenderFunction(_)
			myPrompt:Render()
		end 
		mod:AddCallback(ModCallbacks.MC_POST_RENDER, mod.myRenderFunction)

		function mod:myUpdateFunction(_) 
			myPrompt:Update(true) -- true = Process user inputs
			if wasPromptDisplayed and not myPrompt:IsActive() then -- prompt was closed by user 
				print("User selected option: "..myPrompt:GetSubmittedSelection()) 
				wasPromptDisplayed = false 
			end
			if Input.IsButtonTriggered(Keyboard.KEY_MINUS, 0)  then -- on Pressing minus button will open prompt 
				myPrompt:Show() 
				wasPromptDisplayed = true 
			end 
		end 
		mod:AddCallback(ModCallbacks.MC_POST_UPDATE, mod.myUpdateFunction)
		```

## Constructors

### GenericPrompt () {: aria-label='Constructors' }
#### [GenericPrompt](GenericPrompt.md) GenericPrompt ( ) {: .copyable aria-label='Constructors' }
## 函数
返回一个 GenericPrompt 对象。允许渲染一个弹出式纸张，可选择包含文本并跟踪玩家的是/否决策输入。
返回玩家当前悬停的选择项。

???+ info "Return info"

	- `0` - 否
	- `1` - 是

___
### GetCurrentSelection () {: aria-label='Functions' }
#### int GetCurrentSelection ( ) {: .copyable aria-label='Functions' }
Returns what selection the player is currently hovering over.

???+ info "Return info"

	- `0` - No
	- `1` - Yes

___
### GetSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetSprite ( ) {: .copyable aria-label='Functions' }
返回提示框的纸张精灵图。

___
### GetSubmittedSelection () {: aria-label='Functions' }
#### int GetSubmittedSelection ( ) {: .copyable aria-label='Functions' }
返回所选的选项。

???+ info "Return info"

	- `0` - 无（如果玩家关闭提示框则返回此值）。
	- `1` - 是
	- `2` - 否

___
### Initialize () {: aria-label='Functions' }
#### void Initialize ( boolean SmallPrompt = false ) {: .copyable aria-label='Functions' }

___
### IsActive () {: aria-label='Functions' }
#### boolean IsActive ( ) {: .copyable aria-label='Functions' }
返回提示框是否处于激活状态。

___
### Render () {: aria-label='Functions' }
#### void Render ( ) {: .copyable aria-label='Functions' }
在屏幕上渲染提示框。将此函数放置在任何非实体特定的渲染回调中。

___
### SetImageToVictoryRun () {: aria-label='Functions' }
#### void SetImageToVictoryRun ( ) {: .copyable aria-label='Functions' }

___
### SetText () {: aria-label='Functions' }
#### void SetText ( string Text1 = "", string Text2 = "", string Text3 = "", string Text4 = "", string Text5 = "", ) {: .copyable aria-label='Functions' }
文本字符串与它们在提示框上从上到下的位置相关联。前两个字符串应用作标题文本，会加粗并使用较大的字体大小，其余的用作描述文本。
设置将显示在纸张上的文本。

___
### Show () {: aria-label='Functions' }
#### void Show ( ) {: .copyable aria-label='Functions' }
开始在屏幕上显示提示框。

___
### Update () {: aria-label='Functions' }
#### void Update ( boolean ProcessInput ) {: .copyable aria-label='Functions' }
更新提示框纸张的动画。将 `ProcessInput` 设置为 `true` 以跟踪玩家选择是/否的输入，设置为 `false` 则不跟踪。

___