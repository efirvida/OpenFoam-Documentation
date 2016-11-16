# kqRWallFunctionFvPatchField 
## Class
Foam::kqRWallFunctionFvPatchField

## Group
grpWallFunctions

## Description
This boundary condition provides a suitable condition for turbulence
\c k, \c q, and \c R fields for the case of high Reynolds number flow using
wall functions.

It is a simple wrapper around the zero-gradient condition.

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            kqRWallFunction;
}
```

## See also
Foam::zeroGradientFvPatchField

## SourceFiles
kqRWallFunctionFvPatchField.C

