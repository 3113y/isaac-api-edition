---
tags:
  - File
---
# 文件 "cutscenes.xml"

此文件用于存储和定义游戏中的开场动画和各种结局动画。

**Resource-Folder**{: .xmlInfo }：在模组的resource文件夹中使用此文件尚未经过测试。

**Content-Folder**{: .xmlInfo }：在模组的content文件夹中使用此文件尚未经过测试。

## "cutscene" 标签

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|id|int|动画的ID|
|name|string|动画的名称|
|fadeout|bool|该动画是否淡出|
|fadecolor|string|如果启用淡出，淡出的颜色|

## "anm2part" 标签

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|anm2|string|该anm2part要播放的anm2文件路径|
|anim|string|该anm2part要播放的anm2中的动画名称|
|music|int|该anm2part要播放的音乐ID，定义在music.xml中|
|musicDelay|int|游戏在播放上述音乐前应等待的时间（如有）|
|width|int|anm2在屏幕上显示的宽度|
|height|int|anm2在屏幕上显示的高度|
|subtitles|string|字幕.srt文件的路径|
|letterbox|bool||

## "videopart" 标签

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|file|string|该videopart要播放的视频文件路径|
|subtitles|string|字幕.srt文件的路径|
|keepMusic|bool|播放该videopart时，anm2part定义的音乐是否继续播放|
