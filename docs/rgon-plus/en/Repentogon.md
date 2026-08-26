---
tags:
  - Global
---
> Documentation prose polished by a constrained language model; API facts and signatures retain their upstream source.

# Global Variable "REPENTOGON"

This global variable exposes Repentogon-related functions and variables, such as
the current version and changelog. It is a **table**.

This variable can be accessed from anywhere.

## Functions

All functions in the table are static: access them with the dot (`.`) operator
rather than the colon (`:`) operator.

### MeetsVersion () {: aria-label='Functions' }
#### boolean MeetsVersion ( string version ) {: .copyable aria-label='Functions' }
Checks whether the specified `version` is less than or equal to the currently
installed Repentogon version. In other words, it returns `true` when the
specified version requirement is met.

???+ bug
    Until Repentogon version 1.0.10b, this function was bugged and always
    returned `true`.

___
