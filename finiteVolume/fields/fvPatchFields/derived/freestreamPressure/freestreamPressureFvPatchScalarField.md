# freestreamPressureFvPatchScalarField 
## Class
Foam::freestreamPressureFvPatchScalarField

## Group
grpInletBoundaryConditions grpOutletBoundaryConditions

## Description
This boundary condition provides a free-stream condition for pressure.
It is a zero-gradient condition that constrains the flux across the patch
based on the free-stream velocity.

## Usage

        Property     | Description             | Required    | Default value
        U            | velocity field name     | no          | U
        phi          | flux field name         | no          | phi
        rho          | density field name      | no          | none


Example of the boundary condition specification:
```
<patchName>
{
        type            freestreamPressure;
}
```

## Note
This condition is designed to operate with a freestream velocity condition

## See also
Foam::zeroGradientFvPatchField
Foam::freestreamFvPatchField

## SourceFiles
freestreamPressureFvPatchScalarField.C

