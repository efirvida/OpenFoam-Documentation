# patchInjectionBase 
## Class
Foam::PatchInjectionBase

## Description
Base class for patch-based injection models.

Class handles injecting at a random point adjacent to the patch faces to
provide a more stochsatic view of the injection process.  Patch faces are
triangulated, and area fractions accumulated.  The fractional areas are
then applied to determine across which face a parcel is to be injected.

## SourceFiles
PatchInjectionBase.C

