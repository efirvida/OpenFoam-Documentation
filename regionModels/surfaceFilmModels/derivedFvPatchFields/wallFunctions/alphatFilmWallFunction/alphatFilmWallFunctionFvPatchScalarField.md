# alphatFilmWallFunctionFvPatchScalarField 
## Class
Foam::compressible::RASModels::alphatFilmWallFunctionFvPatchScalarField

## Group
grpSurfaceFilmBoundaryConditions grpCmpWallFunctions

## Description
This boundary condition provides a turbulent thermal diffusivity condition
when using wall functions, for use with surface film models.  This
condition varies from the standard wall function by taking into account any
mass released from the film model.

## Usage

        Property     | Description             | Required    | Default value
        B            | model coefficient       | no          | 5.5
        yPlusCrit    | critical y+ for transition to turbulent flow | no|11.05
        Cmu          | model coefficient       | no          | 0.09
        kappa        | Von-Karman constant     | no          | 0.41
        Prt          | turbulent Prandtl number | no         | 0.85


Example of the boundary condition specification:
```
<patchName>
{
        type            alphatFilmWallFunction;
        B               5.5;
        yPlusCrit       11.05;
        Cmu             0.09;
        kappa           0.41;
        Prt             0.85;
        value           uniform 0;
}
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
alphatFilmWallFunctionFvPatchScalarField.C

