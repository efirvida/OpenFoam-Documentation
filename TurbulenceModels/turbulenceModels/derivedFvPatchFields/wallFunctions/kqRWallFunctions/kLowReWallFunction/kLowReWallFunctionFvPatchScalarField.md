# kLowReWallFunctionFvPatchScalarField 
## Class
Foam::kLowReWallFunctionFvPatchScalarField

## Group
grpWallFunctions

## Description
This boundary condition provides a turbulence kinetic energy wall function
condition for low- and high-Reynolds number turbulent flow cases.

The model operates in two modes, based on the computed laminar-to-turbulent
switch-over y+ value derived from kappa and E.

## Usage

        Property     | Description             | Required    | Default value
        Cmu          | model coefficient       | no          | 0.09
        kappa        | Von Karman constant     | no          | 0.41
        E            | model coefficient       | no          | 9.8
        Ceps2        | model coefficient       | no          | 1.9


Example of the boundary condition specification:
```
<patchName>
{
        type            kLowReWallFunction;
}
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
kLowReWallFunctionFvPatchScalarField.C

