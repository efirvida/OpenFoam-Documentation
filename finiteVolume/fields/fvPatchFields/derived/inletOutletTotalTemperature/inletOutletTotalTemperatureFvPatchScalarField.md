# inletOutletTotalTemperatureFvPatchScalarField 
## Class
Foam::inletOutletTotalTemperatureFvPatchScalarField

## Group
grpOutletBoundaryConditions

## Description
This boundary condition provides an outflow condition for total
temperature for use with supersonic cases, where a user-specified
value is applied in the case of reverse flow.

## Usage

        Property     | Description             | Required    | Default value
        U            | velocity field name     | no          | U
        phi          | flux field name         | no          | phi
        psi          | compressibility field name |  no      | psi
        gamma        | heat capacity ration (Cp/Cv) | yes    |
        inletValue   | reverse flow (inlet) value | yes      |
        T0           | static temperature [K]  | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            inletOutletTotalTemperature;
        U               U;
        phi             phi;
        psi             psi;
        gamma           gamma;
        inletValue      uniform 0;
        T0              uniform 0;
        value           uniform 0;
}
```

## See also
Foam::inletOutletFvPatchField

## SourceFiles
inletOutletTotalTemperatureFvPatchScalarField.C

