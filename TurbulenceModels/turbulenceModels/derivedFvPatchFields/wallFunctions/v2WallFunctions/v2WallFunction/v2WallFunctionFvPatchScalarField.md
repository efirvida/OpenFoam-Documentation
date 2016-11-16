# v2WallFunctionFvPatchScalarField 
## Class
Foam::RASModels::v2WallFunctionFvPatchScalarField

## Group
grpWallFunctions

## Description
This boundary condition provides a turbulence stress normal to streamlines
wall function condition for low- and high-Reynolds number, turbulent flow
cases.

The model operates in two modes, based on the computed laminar-to-turbulent
switch-over y+ value derived from kappa and E.


## Usage

        Property     | Description             | Required    | Default value
        Cmu          | model coefficient       | no          | 0.09
        kappa        | Von Karman constant     | no          | 0.41
        E            | model coefficient       | no          | 9.8


Example of the boundary condition specification:
```
<patchName>
{
        type            v2WallFunction;
}
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
v2WallFunctionFvPatchScalarField.C

