# nutkWallFunctionFvPatchScalarField 
## Class
Foam::nutkWallFunctionFvPatchScalarField

## Group
grpWallFunctions

## Description
This boundary condition provides a turbulent kinematic viscosity condition
when using wall functions, based on turbulence kinetic energy.
- replicates OpenFOAM v1.5 (and earlier) behaviour

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            nutkWallFunction;
}
```

## See also
Foam::nutWallFunctionFvPatchScalarField

## SourceFiles
nutkWallFunctionFvPatchScalarField.C

