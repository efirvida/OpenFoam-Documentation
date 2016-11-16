# extrapolatedCalculatedFvPatchField 
## Class
Foam::extrapolatedCalculatedFvPatchField

## Group
grpGenericBoundaryConditions

## Description
This boundary condition applies a zero-gradient condition from the patch
internal field onto the patch faces when \c evaluated but may also be
assigned.  \c snGrad returns the patch gradient evaluated from the current
internal and patch field values rather than returning zero.

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            extrapolatedCalculated;
}
```

## SourceFiles
extrapolatedCalculatedFvPatchField.C

