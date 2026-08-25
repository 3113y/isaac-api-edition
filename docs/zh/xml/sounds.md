---
tags:
  - File
---
# 文件 "sounds.xml"

此文件用于存储游戏中使用的音效信息。

旧教程：[https://www.reddit.com/r/themoddingofisaac/comments/3ebqat/all_about_music_soundfiles/](https://www.reddit.com/r/themoddingofisaac/comments/3ebqat/all_about_music_soundfiles/)

**Resource-Folder**{: .xmlInfo .green}：将此文件放入模组的resource文件夹会替换原版文件。

**Content-Folder**{: .xmlInfo .green}：将此文件放入模组的content文件夹会添加新的音效。


## "sound" 节点
| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|name|string|音效名称|

## "sample" 节点
“sound”节点的子节点。一个“sound”节点可以包含多个“sample”节点，播放时会随机选择其中一个。

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|weight|float|被随机选中时的权重。<br>数值越小，被选中的概率越低|
|path|string|.wav 文件的路径|


## 说明
只能将“.wav”文件定义为音效。文件必须为16位编码，否则会出现高频杂音。比特率和声道数可自由选择。

# 文件转换
要将任意音频格式轻松转换为所需的“.wav”格式，可以使用许多音频编辑软件。

也可以使用如 [convertio.co](https://convertio.co/mp3-wav/) 这样的网站进行在线转换。**请确保保存为16位（示例Codec: "PCM_S16LE (Uncompressed)"）。**

## 示例

???+ example "示例代码"
    此代码添加了两个音效。一个为单一音效，另一个为包含3个可随机选择音效的组合。

    ```xml
    <sounds root="sounds/">
        <sound name="MySoundEffect1">
            <sample weight="1" path="some_Sound_file.wav" />
        </sound>
        <sound name="MySoundEffect2">
            <sample weight="1" path="sound_effect_variation_1.wav"/>
            <sample weight="1" path="sound_effect_variation_2.wav"/>
            <sample weight="1" path="sound_effect_variation_3.wav"/>
        </sound>
    </sounds>
    ```
