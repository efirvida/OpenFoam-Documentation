# prghTotalHydrostaticPressureFvPatchScalarField 
## Class
Foam::prghTotalHydrostaticPressureFvPatchScalarField

## Group
grpGenericBoundaryConditions

## Description
This boundary condition provides static pressure condition for p_rgh,
calculated as:

        \f[
            p_rgh = ph_rgh - 0.5 \rho |U|^2
        \f]

where
\vartable
        p_rgh   | Pressure - \rho g.(h - hRef) [Pa]
        ph_rgh  | Hydrostatic pressure - \rho g.(h - hRef) [Pa]
        h       | Height in the opposite direction to gravity
        hRef    | Reference height in the opposite direction to gravity
        \rho    | Density
        g       | Acceleration due to gravity [m/s^2]


## Usage

        Property     | Description             | Required    | Default value
        U            | Velocity field name     | no          | U
        phi          | Flux field name         | no          | phi
        rho          | Density field name      | no          | rho
        ph_rgh       | ph_rgh field name       | no          | ph_rgh
        value        | Patch face values       | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            prghTotalHydrostaticPressure;
        value           uniform 0;
}
```

## See also
Foam::fixedValueFvPatchScalarField
Foam::prghTotalPressureFvPatchScalarField

## SourceFiles
prghTotalHydrostaticPressureFvPatchScalarField.C

