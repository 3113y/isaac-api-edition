---
tags:
  - Class
---
# Class "Font"

## Modified Constructors

### Font () {: aria-label='Modified Constructors' }
#### [Font](Font.md),boolean Font ( string FontPath ) {: .copyable aria-label='Modified Constructors' }

Adds the optional "FontPath" argument and returns two values: a [Font](Font.md) object and a boolean indicating whether the font loaded successfully.
___
## Modified Functions

### DrawString () {: aria-label='Modified Functions' }
#### void DrawString ( string String, float PositionX, float PositionY, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) RenderColor, int BoxWidth = 0, boolean Center = false ) {: .copyable aria-label='Modified Functions' }
Same as the default function, but with improved input validation to prevent crashes.

___

### DrawStringScaled () {: aria-label='Modified Functions' }
#### void DrawStringScaled ( string String, float PositionX, float PositionY, float ScaleX, float ScaleY, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) RenderColor, int BoxWidth = 0, boolean Center = false ) {: .copyable aria-label='Modified Functions' }
Same as the default function, but with improved input validation to prevent crashes.

___
### DrawStringScaledUTF8 () {: aria-label='Modified Functions' }
#### void DrawStringScaledUTF8 ( string String, float PositionX, float PositionY, float ScaleX, float ScaleY, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) RenderColor, int BoxWidth = 0, boolean Center = false ) {: .copyable aria-label='Modified Functions' }
Same as the default function, but with improved input validation to prevent crashes.

___
### DrawStringUTF8 () {: aria-label='Modified Functions' }
#### void DrawStringUTF8 ( string String, float PositionX, float PositionY, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) RenderColor, int BoxWidth = 0, boolean Center = false ) {: .copyable aria-label='Modified Functions' }
Same as the default function, but with improved input validation to prevent crashes.

___
### GetStringWidth () {: aria-label='Modified Functions' }
#### int GetStringWidth ( string String ) {: .copyable aria-label='Modified Functions' }
Same as the default function, but with improved input validation to prevent crashes.

___
### GetStringWidthUTF8 () {: aria-label='Modified Functions' }
#### int GetStringWidthUTF8 ( string String ) {: .copyable aria-label='Modified Functions' }
Same as the default function, but with improved input validation to prevent crashes.

___
