# sampledPatchInternalField 
## Class
Foam::sampledPatchInternalField

## Description
Variation of sampledPatch that samples the internalField (at a given
normal distance from the patch) instead of the patchField.
Note:
- interpolate=false : get cell value on faces
- interpolate=true  : interpolate inside cell and interpolate to points
There is no option to get interpolated value inside the cell on the faces.

## SourceFiles
sampledPatchInternalField.C

