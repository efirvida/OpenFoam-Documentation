# nutURoughWallFunctionFvPatchScalarField 
## Class
Foam::nutURoughWallFunctionFvPatchScalarField

## Group
grpWallFunctions

## Description
This boundary condition provides a turbulent kinematic viscosity condition
when using wall functions for rough walls, based on velocity.

## Usage

        Property     | Description             | Required    | Default value
        roughnessHeight | roughness height     | yes         |
        roughnessConstant | roughness constanr | yes         |
        roughnessFactor | scaling factor       | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            nutURoughWallFunction;
        roughnessHeight 1e-5;
        roughnessConstant 0.5;
        roughnessFactor 1;
}
```

## See also
Foam::nutWallFunctionFvPatchScalarField

## SourceFiles
nutURoughWallFunctionFvPatchScalarField.C

