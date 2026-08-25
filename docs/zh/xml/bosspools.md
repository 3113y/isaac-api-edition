---
tags:
  - File
---
# 文件 "bosspools.xml"
[ ](#){: .reporplus .tooltip .badge }

此文件用于存储某一关卡可生成Boss的信息。

此文件只能用于修改原版Boss。要添加自定义Boss，你需要使用第三方库，如 [StageAPI](https://github.com/Meowlala/BOIStageAPI15)。

**Resource-Folder**{: .xmlInfo .red}：将此文件放入你的模组 "resource" 文件夹没有任何效果！

**Content-Folder**{: .xmlInfo .red}：将此文件放入你的模组 "content" 文件夹没有任何效果！

## "pool" 标签

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|name|String|bosspool的名称|
|doubletrouble|int|用于Double Trouble房间的房间ID|

## "boss" 标签

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|id|int|Boss的ID|
|weight|float|遇到该Boss的概率权重|

## 示例

???+ example "示例代码"
    下面的代码描述了一个包含3个Boss的boss池。

    ```xml
    <bosspools>
        <pool name="basement">
            <boss id="1" weight="1" />		<!-- Monstro -->
            <boss id="17" weight="1" />		<!-- Gemini -->
            <boss id="2" weight="1" />		<!-- Larry Jr. -->
        </pool>
    </bosspools>
    ```
