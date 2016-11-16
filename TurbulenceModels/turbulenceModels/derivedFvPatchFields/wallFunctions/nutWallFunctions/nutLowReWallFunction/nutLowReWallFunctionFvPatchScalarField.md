# nutLowReWallFunctionFvPatchScalarField 
## Class
Foam::nutLowReWallFunctionFvPatchScalarField

## Group
grpWallFunctions

## Description
This boundary condition provides a turbulent kinematic viscosity condition
for use with low Reynolds number models.  It sets \c nut to zero, and
provides an access function to calculate y+.

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            nutLowReWallFunction;
}
```

## See also
Foam::nutWallFunctionFvPatchScalarField

## SourceFiles
nutLowReWallFunctionFvPatchScalarField.C

