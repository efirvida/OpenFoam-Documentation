# nutkFilmWallFunctionFvPatchScalarField 
## Class
Foam::compressible::RASModels::nutkFilmWallFunctionFvPatchScalarField

## Group
grpSurfaceFilmBoundaryConditions grpCmpWallFunctions

## Description
This boundary condition provides a turbulent viscosity condition when
using wall functions, based on turbulence kinetic energy, for use with
surface film models.

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            nutkFilmWallFunction;
        value           uniform 0;
}
```

## See also
Foam::nutkWallFunctionFvPatchScalarField

## SourceFiles
nutkFilmWallFunctionFvPatchScalarField.C

