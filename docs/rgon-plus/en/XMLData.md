---
tags:
  - Global
  - Class
---
# Global Class "XMLData"

???+ info
	A public table containing all functions related to gathering XML attributes across the different XMLs, with updated values that match the actual values.
    
    You can get this class by using the `XMLData` global table.

    **Note that to call these functions, you must use a `.` (period) instead of a `:` (colon)!**
    
    ???+ example "Example Code"
        ```lua
        local numEntries = XMLData.GetNumEntries(XMLNode.ENTITY)
        ```
        
???+ warning "Warning"
    XML attributes are converted to lowercase when parsed by REPENTOGON! This eliminates capitalization inconsistencies in vanilla tags, but may prevent attributes from being found when looked up by the names defined in the XML (e.g. `bossID` will return `nil`, so use `bossid` instead.)
        
## Functions

### GetBossColorByTypeVarSub () {: aria-label='Functions' }
#### table GetBossColorByTypeVarSub ( [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) Type, int Variant , int SubType) {: .copyable aria-label='Functions' }
Returns a table containing the attributes of the boss color in bosscolors.xml that match the given type, variant, and subtype.
???- info "Table usage"
	```lua
	print("Red Monstro's suffix:", XMLData.GetBossColorByTypeVarSub(20,0,1).suffix)
	```
___
### GetEntityByTypeVarSub () {: aria-label='Functions' }
#### table GetEntityByTypeVarSub ( [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) Type, int Variant = 0 , int SubType = 0, boolean Strict = false) {: .copyable aria-label='Functions' }
Returns a table containing the attributes of the entity in entities2.xml that match the given type, variant, and/or subtype. The strict parameter determines whether it returns a value only when all three attributes (type, variant, and subtype) match, or returns the type match while treating the remaining attributes as possible matches.
???- info "Table usage"
	```lua
	print("Monstro's BossID:", XMLData.GetEntityByTypeVarSub(20).bossid)
	```
???+ note "child nodes"
    Child nodes are returned as tables alongside the rest of the attributes. For example, if you want to access the samples of a sound entry, you can use `soundentry.sample[1]`.
___
### GetEntryById () {: aria-label='Functions' }
#### table GetEntryById ( [XMLNode](enums/XMLNode.md) NodeType, int Idx ) {: .copyable aria-label='Functions' }
Returns a table containing the attributes of the corresponding XML, matching the given NodeType (e.g. XMLNode.TRINKET returns trinket nodes from pocketitems.xml) and unique ID.
???- info "Table usage"
	```lua
	print("Sad Onion's description:", XMLData.GetEntryById(XMLNode.ITEM, 1).description)
	```
???+ note "child nodes"
    Child nodes are returned as tables alongside the rest of the attributes. For example, if you want to access the samples of a sound entry, you can use `soundentry.sample[1]`.
???+ note "id?"
    The ID usually matches the node's actual ID, except in files such as entities.xml where IDs are not unique; in those cases, the ID is the node's order and does not correspond to its actual ID. For XMLs without IDs, it is simply the node's order.
___
### GetEntryByName () {: aria-label='Functions' }
#### table GetEntryByName ( [XMLNode](enums/XMLNode.md) NodeType, string Name ) {: .copyable aria-label='Functions' }
Returns a table containing the attributes of the corresponding XML, matching the given NodeType (e.g. XMLNode.TRINKET returns trinket nodes from pocketitems.xml) and name.
???- info "Table usage"
	```lua
	print("Sad Onion's description:", XMLData.GetEntryByName(XMLNode.ITEM, "The Sad Onion").description)
	```
???+ note "child nodes"
    Child nodes are returned as tables alongside the rest of the attributes. For example, if you want to access the samples of a sound entry, you can use `soundentry.sample[1]`.
___
### GetEntryByOrder () {: aria-label='Functions' }
#### table GetEntryByOrder ( [XMLNode](enums/XMLNode.md) NodeType, int Order ) {: .copyable aria-label='Functions' }
Similar to GetEntryByName or GetEntryById, but returns the node based on its order in the XML (1 returns the first node, 2 the second, and so on). Useful for iterating through XMLs in combination with GetNumEntries, especially redundant XMLs such as entities.xml.
???- info "Table usage"
	```lua
	print("Sad Onion's description:", XMLData.GetEntryByOrder(XMLNode.ITEM, 1).description)
	```
???+ note "child nodes"
    Child nodes are returned as tables alongside the rest of the attributes. For example, if you want to access the samples of a sound entry, you can use `soundentry.sample[1]`.
???+ note "id?"
    The ID usually matches the node's actual ID, except in files such as entities.xml where IDs are not unique; in those cases, the ID is the node's order and does not correspond to its actual ID. For XMLs without IDs, it is simply the node's order.
___
### GetEntryFromEntity () {: aria-label='Functions' }
#### table GetEntryFromEntity ( [Entity](Entity.md) Entity, boolean AutoXMLPick = true, boolean Strict) {: .copyable aria-label='Functions' }
Returns a table containing the attributes of the provided entity. The `AutoXMLPick` parameter determines whether to use only entities2.xml or to select the XML matching the [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) (e.g. items.xml for pedestal collectibles). The strict parameter determines whether it returns a value only when the type, variant, and subtype attributes match, or returns the type match while treating the remaining attributes as possible matches.
???- info "Table usage"
	```lua
	print("Player's birthright:", XMLData.GetEntryFromEntity(Isaac.GetPlayer()).birthright)
	```
???+ note "child nodes"
    Child nodes are returned as tables alongside the rest of the attributes. For example, if you want to access the samples of a sound entry, you can use `soundentry.sample[1]`.
___
### GetModById () {: aria-label='Functions' }
#### table GetModById ( string modId ) {: .copyable aria-label='Functions' }
Returns a table containing the attributes of the metadata XML for the matching mod ID. Can be used with the `sourceid` attribute of other XML nodes to determine which mod they come from when they originate in a mod (most nodes have this attribute).
???- info "Table usage"
	```lua
	print("Car's mod name:", XMLData.GetModById("2788006730").name)
	```
???+ note "id?"
    The ID usually matches the mod's actual Workshop ID, except when the mod was downloaded illegally and tampered with or is an in-development mod. If the mod does not have an ID, its directory is used as the ID.
___
### GetNumEntries () {: aria-label='Functions' }
#### int GetNumEntries ( [XMLNode](enums/XMLNode.md) NodeType) {: .copyable aria-label='Functions' }
Returns the number of entries a given XMLNode structure has.
___
