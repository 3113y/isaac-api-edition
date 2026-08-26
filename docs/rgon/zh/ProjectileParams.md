---
tags:
  - Global
  - Class
search:
  boost: 0.25
---
# Class "ProjectileParams"
## Variables
### Damage {: aria-label='Variables' }
#### float Damage {: .copyable aria-label='Variables'}

Damage dealt by the projectile, measured in half-hearts. This value cannot be negative.

???+ info
    This value ignores the full-heart damage modifier applied to projectiles with a [Scale](https://wofsauge.github.io/IsaacDocs/rep/ProjectileParams.html#scale) above `1.15`; however, non-boss champions still double it. See the warning below for a caveat.
    

???+ warning "Warning"
    Enemies with a [ChampionColorIdx](https://wofsauge.github.io/IsaacDocs/rep/enums/ChampionColor.html) greater than `-1` cap the damage at `2.0`.
___
