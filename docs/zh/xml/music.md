---
tags:
  - File
---
# 文件 "music.xml"

此文件用于存储和定义游戏播放的音乐曲目。这里只包含背景音乐，音效请见"sounds.xml"文件。

旧教程: [https://www.reddit.com/r/themoddingofisaac/comments/3ebqat/all_about_music_soundfiles/](https://www.reddit.com/r/themoddingofisaac/comments/3ebqat/all_about_music_soundfiles/)

**Resource-Folder**{: .xmlInfo .green }：将此文件放入你的模组 "resource" 文件夹会替换原始文件。

**Content-Folder**{: .xmlInfo }：在模组的content文件夹中使用此文件尚未经过测试。


| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|id|int|该音乐条目定义的音乐ID|
|name|string|曲目名称|
|intro|string|该曲目的前奏文件路径。只在歌曲开头播放一次|
|path|string|主音乐文件路径。前奏后播放|
|layerintro|string|该曲目前奏的分层文件路径|
|layer|string|该曲目的分层文件路径。当房间内敌人较多时，分层会叠加在主曲目上播放|
|loop|bool|主曲目是否无限循环播放。|
|layermode|int||
|layerfadespeed|float||
|mul|float||
|layermul|float||
