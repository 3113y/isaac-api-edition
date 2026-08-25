---
tags:
  - File
---
# 文件 "items_metadata.xml"
此文件用于为Collectibles或Trinkets定义附加信息，包括品质、特殊属性（如变身或玩法交互等）。

**Resource-Folder**{: .xmlInfo .red}：在模组的resource文件夹中使用此文件会替换原始文件。

**Content-Folder**{: .xmlInfo .green}：在模组的content文件夹中使用此文件会添加新物品。

???+ warning "警告！此文件其实不需要！"
  "items_metadata.xml" 文件是开发过程中的遗留产物。其所有功能（物品的品质和标签定义）都可以在 "items.xml" 文件中以更可靠的方式实现。

| 变量名 | 可能的值 | 描述 |
|:--|:--|:--|
| id | int | 对应Collectible或Trinket的ID|
| quality | int | 可能的值: ['0', '1', '2', '3', '4'] |
| tags | string | 多个标签需用空格分隔。<br>可能的值: ['', 'battery', 'bob', 'mushroom', 'nogreed', 'nolostbr', 'offensive', 'summonable', 'poop', 'tearsup', 'uniquefamiliar', 'mom', 'baby', 'quest', 'food', 'spider', 'monstermanual', 'devil', 'book', 'fly', 'stars', 'nokeeper', 'nocantrip', 'angel', 'syringe', 'dead', 'guppy', 'tech'] |
