# fWallFunctionFvPatchScalarField 
## Class
Foam::RASModels::fWallFunctionFvPatchScalarField

## Group
grpWallFunctions

## Description
This boundary condition provides a turbulence damping function, f, wall
function condition for low- and high Reynolds number, turbulent flow cases

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
        type            fWallFunction;
}
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
fWallFunctionFvPatchScalarField.C

