---
tags:
  - Class
---
# Class "GridEntitiesSaveStateVector"

Represents a vector of grid-entity save-state descriptions. Elements can be retrieved by index or grid-entity type, and the vector exposes its size.

## Functions
### Get () {: aria-label='Functions' }
#### [GridEntityDesc](https://wofsauge.github.io/IsaacDocs/rep/GridEntityDesc.html) Get ( int Index ) {: .copyable aria-label='Functions' }

Returns the grid-entity description at the specified index.

___
### GetByType () {: aria-label='Functions' }
#### [GridEntityDesc](https://wofsauge.github.io/IsaacDocs/rep/GridEntityDesc.html) GetByType ( [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) Type ) {: .copyable aria-label='Functions' }

Returns the grid-entity description for the specified grid-entity type.

___
### __len () {: aria-label='Operators' }
#### int __len ( ) {: .copyable aria-label='Operators' }

Returns the number of elements in the vector.

___
