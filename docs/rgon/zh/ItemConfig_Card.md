---
tags:
  - Class
---
# Class "ItemConfigCard"

## Functions

### SetAvailabilityCondition

#### void SetAvailabilityCondition ( function AvailabilityCondition ) {: .copyable aria-label='Modified Functions' }

Sets an additional function that runs when [IsAvailable()](https://wofsauge.github.io/IsaacDocs/rep/ItemConfig_Card.html#isavailable) is called, internally or through the Lua API.

The function must return a boolean that determines whether or not the card is available.

This function is only checked after the GreedModeAllowed, Achievement, and Hidden checks have all passed, so it cannot be used to override those checks.

???+ warning "Function Errors"
    If the function errors at any point while it is being executed, it is treated as though `true` was returned.

    If this is not the intended behavior, wrap your actual function in a `pcall` or `xpcall` and return `false` if the call fails.


    ```lua
    local function AvailabilityCondition()
        -- Your code here
    end


    local function AvailabilityWrapper()
        -- Call function with pcall to catch errors
        local success, result = pcall(AvailabilityCondition)

        if success then
            return result  -- Return result if no error
        else
            local errorMessage = 'Error whilst checking Availability of card "Your Card": ' .. result
            Console.PrintError(errorMessage) -- Print the error message
            Isaac.DebugString(errorMessage) -- Log the error message
            return false
        end
    end

    Isaac.GetItemConfig():GetCard(YourCardId):SetAvailabilityCondition(AvailabilityWrapper)
    ```
___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

### ClearAvailabilityCondition

#### void ClearAvailabilityCondition ( ) {: .copyable aria-label='Modified Functions' }

Sets the availability condition to `nil`, which is useful when the condition is no longer needed and can improve performance.
___

### GetAvailabilityCondition

#### function GetAvailabilityCondition ( ) {: .copyable aria-label='Modified Functions' }

Returns `nil` if no AvailabilityCondition is set or if it has been cleared.
___

## Variables

### Hidden {: aria-label='Variables' }

#### const boolean Hidden {: .copyable aria-label='Variables' }

___

### InitialWeight {: aria-label='Variables' }

#### const float InitialWeight {: .copyable aria-label='Variables' }

___

### ModdedCardFront {: aria-label='Variables' }

#### [Sprite](Sprite.md) ModdedCardFront {: .copyable aria-label='Variables' }

___

### Weight {: aria-label='Variables' }

#### float Weight {: .copyable aria-label='Variables' }

Can be set to a value to increase or decrease the chance of this card being randomly picked
___
