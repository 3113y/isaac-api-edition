---
tags:
  - Class
---
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
# Class "MusicManager"

## Modified Functions
### Crossfade () {: aria-label='Modified Functions' }
#### void Crossfade ( [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) MusicId, float FadeRate = 0.08 ) {: .copyable aria-label='Modified Functions' }
现在会验证音乐 ID，以避免崩溃。

### Fadein () {: aria-label='Modified Functions' }
#### void Fadein ( [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) MusicId, float Volume = 1, float Volume = 0.08 ) {: .copyable aria-label='Modified Functions' }
现在会验证音乐 ID，以避免崩溃。

### Play () {: aria-label='Modified Functions' }
#### void Play ( [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) MusicId, int Volume = -1 ) {: .copyable aria-label='Modified Functions' }
现在会验证音乐 ID，以避免崩溃。
### GetCurrentPitch () {: aria-label='Functions' }
#### float GetCurrentPitch ( ) {: .copyable aria-label='Functions' }

___
### PlayJingle () {: aria-label='Functions' }
#### void PlayJingle ( [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) MusicId, int Duration = 140 ) {: .copyable aria-label='Functions' }

___
### SetCurrentPitch () {: aria-label='Functions' }
#### void SetCurrentPitch ( float Pitch ) {: .copyable aria-label='Functions' }

___
### StopJingle () {: aria-label='Functions' }
#### void StopJingle ( ) {: .copyable aria-label='Functions' }

___
