# nutkRoughWallFunctionFvPatchScalarField 
## Class
Foam::nutkRoughWallFunctionFvPatchScalarField

## Group
grpWallFunctions

## Description
This boundary condition provides a turbulent kinematic viscosity condition
when using wall functions for rough walls, based on turbulence kinetic
energy.  The condition manipulates the E parameter to account for roughness
effects.

Parameter ranges
- roughness height = sand-grain roughness (0 for smooth walls)
- roughness constant = 0.5-1.0

## Usage

        Property     | Description             | Required    | Default value
        Ks           | sand-grain roughness height | yes     |
        Cs           | roughness constant      | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            nutkRoughWallFunction;
        Ks              uniform 0;
        Cs              uniform 0.5;
}
```

## See also
Foam::nutkRoughWallFunctionFvPatchScalarField

## SourceFiles
nutkRoughWallFunctionFvPatchScalarField.C

