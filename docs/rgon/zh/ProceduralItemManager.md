---
tags:
  - Global
  - Class
---
# Global Class "ProceduralItemManager"

???+ info
    You can get this class by using the `ProceduralItemManager` global table.

    **注意：调用这些函数时，必须使用 .（句点）而非 :（冒号）！**
    
    ???+ example "Example Code"
        ```lua
        local pItem = ProceduralItemManager.GetProceduralItem(0)
        ```

## Functions
### CreateProceduralItem () {: aria-label='Functions' }
#### int CreateProceduralItem ( int Seed, int Unknown ) {: .copyable aria-label='Functions' }
Returns the negative ID of the created item.
Creates a glitch item based on a given seed.

### GetProceduralItem () {: aria-label='Functions' }
#### [ProceduralItem](ProceduralItem.md) GetProceduralItem ( int Index ) {: .copyable aria-label='Functions' }
Get the glitch item at the given index.
### GetProceduralItemCount () {: aria-label='Functions' }
#### int GetProceduralItemCount ( ) {: .copyable aria-label='Functions' }
___