---
tags:
  - Class
---
> Documentation prose polished by a constrained language model; API facts and signatures retain their upstream source.

# Class "ColorParams"

???+ info
    This class can be accessed through its constructor:
    ???+ example "Example Code"
        ```lua
        local fiveSecondRedColor = ColorParams(Color(1,0,0,1),255,150,false,false)
        ```

## Constructors

### ColorParams () {: aria-label='Constructors' }
#### [ColorParams](ColorParams.md) ColorParams ( [Color](Color.md) color, int priority, int duration1, int duration2, boolean fadeout, boolean shared ) {: .copyable aria-label='Constructors' }

___

## Functions

### GetColor () {: aria-label='Functions' }
#### [Color](Color.md) GetColor ( ) {: .copyable aria-label='Functions' }

___
### GetDuration () {: aria-label='Functions' }
#### int GetDuration ( ) {: .copyable aria-label='Functions' }
Defines how long these parameters should last in update frames. This does not affect the number of frames remaining, but it does affect the fadeout speed (calculated as `Lifespan / Duration`) when `Fadeout` is enabled.

___
### GetFadeout () {: aria-label='Functions' }
#### boolean GetFadeout ( ) {: .copyable aria-label='Functions' }

___
### GetLifespan () {: aria-label='Functions' }
#### int GetLifespan ( ) {: .copyable aria-label='Functions' }
Defines how many update frames remain before these parameters expire. This value is decremented by `1` on each non-interpolation update, at a rate of `30` updates per second. Changing it directly affects how many frames remain before these parameters expire.

___
### GetPriority () {: aria-label='Functions' }
#### int GetPriority ( ) {: .copyable aria-label='Functions' }

___
### GetShared () {: aria-label='Functions' }
#### boolean GetShared ( ) {: .copyable aria-label='Functions' }

___
### SetColor () {: aria-label='Functions' }
#### void SetColor ( [Color](Color.md) Color ) {: .copyable aria-label='Functions' }

___
### SetDuration () {: aria-label='Functions' }
#### void SetDuration ( int Duration ) {: .copyable aria-label='Functions' }

___
### SetFadeout () {: aria-label='Functions' }
#### void SetFadeout ( boolean Value ) {: .copyable aria-label='Functions' }

___
### SetLifespan () {: aria-label='Functions' }
#### void SetLifespan ( int Duration ) {: .copyable aria-label='Functions' }

___
### SetPriority () {: aria-label='Functions' }
#### void SetPriority ( int Priority ) {: .copyable aria-label='Functions' }

___
### SetShared () {: aria-label='Functions' }
#### void SetShared ( boolean Value ) {: .copyable aria-label='Functions' }

___
