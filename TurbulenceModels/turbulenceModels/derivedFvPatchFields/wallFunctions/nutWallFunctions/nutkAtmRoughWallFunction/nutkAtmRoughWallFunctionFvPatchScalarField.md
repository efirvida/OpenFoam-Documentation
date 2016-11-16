# nutkAtmRoughWallFunctionFvPatchScalarField 
## Class
Foam::nutkAtmRoughWallFunctionFvPatchScalarField

## Group
grpWallFunctions

## Description
This boundary condition provides a turbulent kinematic viscosity for
atmospheric velocity profiles.  It is desinged to be used in conjunction
with the atmBoundaryLayerInletVelocity boundary condition.  The values
are calculated using:

        \f[
            U = frac{U_f}{K} ln(\frac{z + z_0}{z_0})
        \f]

where

\vartable
        U_f | frictional velocity
        K   | Von Karman's constant
        z_0 | surface roughness length
        z   | vertical co-ordinate
\endvartable

## Usage

        Property     | Description             | Required    | Default value
        z0           | surface roughness length| yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            nutkAtmRoughWallFunction;
        z0              uniform 0;
}
```

## See also
Foam::nutkWallFunctionFvPatchField

## SourceFiles
nutkAtmRoughWallFunctionFvPatchScalarField.C

