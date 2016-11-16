# prghTotalPressureFvPatchScalarField 
## Class
Foam::prghTotalPressureFvPatchScalarField

## Group
grpGenericBoundaryConditions

## Description
This boundary condition provides static pressure condition for p_rgh,
calculated as:

        \f[
            p_rgh = p - \rho g.(h - hRef)
            p = p0 - 0.5 \rho |U|^2
        \f]

where
\vartable
        p_rgh   | Pseudo hydrostatic pressure [Pa]
        p       | Static pressure [Pa]
        p0      | Total pressure [Pa]
        h       | Height in the opposite direction to gravity
        hRef    | Reference height in the opposite direction to gravity
        \rho    | Density
        g       | Acceleration due to gravity [m/s^2]


## Usage

        Property     | Description             | Required    | Default value
        U            | Velocity field name     | no          | U
        phi          | Flux field name         | no          | phi
        rho          | Density field name      | no          | rho
        p0           | Total pressure          | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            prghTotalPressure;
        p0              uniform 0;
}
```

## See also
Foam::fixedValueFvPatchScalarField

## SourceFiles
prghTotalPressureFvPatchScalarField.C

