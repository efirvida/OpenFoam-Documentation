# totalTemperatureFvPatchScalarField 
## Class
Foam::totalTemperatureFvPatchScalarField

## Group
grpInletBoundaryConditions grpOutletBoundaryConditions

## Description
This boundary condition provides a total temperature condition.

## Usage

        Property     | Description             | Required    | Default value
        U            | Velocity field name     | no          | U
        phi          | Flux field name         | no          | phi
        psi          | Compressibility field name | no       | thermo:psi
        gamma        | ratio of specific heats (Cp/Cv) | yes |
        T0           | reference temperature   | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            totalTemperature;
        T0              uniform 300;
}
```

## SourceFiles
totalTemperatureFvPatchScalarField.C

## See also
Foam::fixedValueFvPatchField

