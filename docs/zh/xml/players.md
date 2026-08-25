---
tags:
  - File
---
# 文件 "players.xml"

本页面需要补充内容。你可以使用编辑按钮进行贡献！

**Resource-Folder**{: .xmlInfo .red}：在模组的resource文件夹中使用此文件会替换原始文件。

**Content-Folder**{: .xmlInfo .green }：在content文件夹中使用会添加新角色。

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
|name|string|角色名称（需与CharacterMenu.anm2中的一致）|
|skin|string|角色spritesheet路径|
|skinColor|int|角色默认皮肤色（-1=全部，0=白，1=黑，2=蓝，3=红，4=绿，5=灰）|
|nameimage|string|vs界面用名称图片|
|portrait|string|vs界面用立绘|
|extraportrait|string|vs界面上与portrait属性图片一同显示的.anm2文件|
|hp|int|初始红心（1=半颗心）|
|armor|int|初始魂心（1=半颗魂心）|
|black|int|初始黑心（1=半颗黑心）|
|items|int|初始物品ID（用逗号分隔可添加多个）|
|trinket|int|初始饰品ID|
|costume|int||
|costumeSuffix|string|角色专属costume目录的后缀。例如The Forgotten的costumeSuffix为`_forgotten`，其目录为`C:\Program Files (x86)\Steam\steamapps\common\The Binding of Isaac Rebirth\resources-dlc3\gfx\characters\costumes_forgotten`。|
|bombs|int|初始炸弹数|
|keys|int|初始钥匙数|
|coins|int|初始金币数|
|card|int|初始卡牌ID|
|pill|int||
|canShoot|bool|False=蒙眼|
|achievement|int|与原版成就绑定的角色|
|broken|int|初始破碎心数量[ ](#){: .reporplus .tooltip .badge }|
|pocketActive|int|初始pocket主动道具ID[ ](#){: .reporplus .tooltip .badge }|
|birthright|string|拾取Birthright时的提示信息[ ](#){: .reporplus .tooltip .badge }|
|bSkinParent|string|你的tainted角色对应的普通角色名称[ ](#){: .reporplus .tooltip .badge }|
|hidden|bool|True=该角色不会出现在选择界面[ ](#){: .reporplus .tooltip .badge }|


players.xml 文件示例：
```xml
<players root="gfx/characters/costumes/"
         portraitroot="gfx/ui/boss/"
         nameimageroot="gfx/ui/boss/">
	<player name="Bob" skin="character_Bob.png" hp="4"
          black="4" pocketActive="712" items="1,4" keys="3"
          nameimage="playername_Bob.png"
          portrait="playerportrait_Bob.png"
          skinColor="-1" canShoot="false"
          birthright="You are now a gamer"/>
</players>
```
