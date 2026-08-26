---
tags:
  - Class
---
> Documentation prose polished by a constrained language model; API facts and signatures retain their upstream source.

# Class "RNG"

## Modified Constructors

### RNG () {: aria-label='Modified Constructors' }
#### [RNG](RNG.md) RNG ( int seed = 2853650767, int shiftIdx = 35 ) { :.copyable aria-label='Modified Constructors' }
Accepts an optional seed and shiftIdx.
This avoids having to construct the RNG object separately from calling SetSeed.

Both the seed and shift index are validated.

___
## Modified Functions

### RandomInt () {: aria-label='Modified Functions' }
#### int RandomInt ( int Min, int Max ) {: .copyable aria-label='Modified Functions' }
Can emulate `math.random` by accepting a second argument and generating an inclusive value between the two arguments. Negative values are supported in this mode, and the result is correctly bounded by `min` and `max` regardless of their signs.

___
### SetSeed () {: aria-label='Modified Functions' }
#### void SetSeed ( int Seed, int ShiftIdx = 35 ) {: .copyable aria-label='Modified Functions' }
Throws an error when Seed is negative.

Throws an error when ShiftIdx is outside the inclusive range 0–80.

ShiftIdx is optional and defaults to 35.

___
## Functions 

### GetShiftIdx () {: aria-label='Functions' }
#### int GetShiftIdx ( ) {: .copyable aria-label='Functions' }

___
### PhantomFloat () {: aria-label='Functions' }
#### float PhantomFloat ( ) {: .copyable aria-label='Functions' }
Generates a random float from `0` (inclusive) to `1` (exclusive).

Does not advance the RNG object's internal state.

___
### PhantomInt () {: aria-label='Functions' }
#### int PhantomInt ( int Max ) {: .copyable aria-label='Functions' }
Behaves like RandomInt without advancing the RNG object's internal state.

___
### PhantomNext () {: aria-label='Functions' }
#### int PhantomNext ( ) {: .copyable aria-label='Functions' }

___
### PhantomPrevious () {: aria-label='Functions' }
#### int PhantomPrevious ( ) {: .copyable aria-label='Functions' }

___
### PhantomVector () {: aria-label='Functions' }
#### [Vector](Vector.md) PhantomVector ( ) {: .copyable aria-label='Functions' }
Returns a random vector of length `1`; multiply it by a number to obtain a larger random vector.

Does not advance the RNG object's internal state.

___
### Previous () {: aria-label='Functions' }
#### int Previous ( ) {: .copyable aria-label='Functions' }

___
### RandomVector () {: aria-label='Functions' }
#### [Vector](Vector.md) RandomVector ( ) {: .copyable aria-label='Functions' }
Returns a random vector of length `1`; multiply it by a number to obtain a larger random vector.

___
