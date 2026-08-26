---
tags:
  - Class
---
# Class "WeightedOutcomePicker"

有关 WeightedOutcomePicker 类的使用示例，请参阅[此模组示例](./examples/WeightedOutcomes.md)。

???+ info
    This class can be obtained using its constructor:
    ???+ example "Example Code"
        ```lua
        local wop = WeightedOutcomePicker()
        ```

## Constructors

### WeightedOutcomePicker () {: aria-label='Constructors' }
#### [WeightedOutcomePicker](WeightedOutcomePicker.md) WeightedOutcomePicker ( ) {: .copyable aria-label='Constructors' }
___
    
## Functions

### AddOutcomeFloat () {: aria-label='Functions' }
#### void AddOutcomeFloat ( int Value, float Weight, int ScaleFactor = 100 ) {: .copyable aria-label='Functions' }
picker:AddOutcomeFloat(3, 0.2) -- ~9%
使用指定的 `Weight` 向选择器添加一个结果。内部权重仍为整数，计算方式为 `fWeight * scaleFactor`；其中 `ScaleFactor` 是最大权重（相当于 1.0）。
picker:AddOutcomeFloat(2, 1.0) -- ~45%
local picker = WeightedOutcomePicker()
```lua
???+ example "Example Code"
```
picker:AddOutcomeFloat(1, 1.0) -- ~45%

### AddOutcomeWeight () {: aria-label='Functions' }
#### void AddOutcomeWeight ( int Value, int Weight ) {: .copyable aria-label='Functions' }
picker:AddOutcomeWeight(3, 5) -- 5%
picker:AddOutcomeWeight(1, 65) -- 65%
local picker = WeightedOutcomePicker()
```lua
picker:AddOutcomeWeight(2, 30) -- 30%
使用指定的 `Weight` 向选择器添加一个结果。
???+ example "Example Code"
```

### ClearOutcomes () {: aria-label='Functions' }
#### void ClearOutcomes ( ) {: .copyable aria-label='Functions' }
清除选择器中的所有结果。

### GetNumOutcomes () {: aria-label='Functions' }
#### int GetNumOutcomes ( ) {: .copyable aria-label='Functions' }
返回选择器中的结果数量。

### GetOutcomes () {: aria-label='Functions' }
#### table[] GetOutcomes ( ) {: .copyable aria-label='Functions' }
返回一个包含选择器中所有结果的表。
print(outcome.Value, outcome.Weight)
end
```lua
* Weight: weight of the outcome
- The returned table contains a list of outcomes, where each outcome is a table containing the following fields:
* Value: value of the outcome
???- info "Table structure & usage"
for i, outcome in ipairs(p:GetOutcomes()) do
```

### PickOutcome () {: aria-label='Functions' }
#### int PickOutcome ( [RNG](RNG.md) RNG ) {: .copyable aria-label='Functions' }
从 WeightedOutcomePicker 的结果列表中随机返回一个结果。接受 [RNG](RNG.md)。

### RemoveOutcome () {: aria-label='Functions' }
#### void RemoveOutcome ( int Value ) {: .copyable aria-label='Functions' }
从选择器中移除 `Value` 指定的结果。
