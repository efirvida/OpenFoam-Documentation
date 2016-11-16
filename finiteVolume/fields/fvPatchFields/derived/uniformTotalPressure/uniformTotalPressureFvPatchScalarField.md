# uniformTotalPressureFvPatchScalarField 
## Class
Foam::uniformTotalPressureFvPatchScalarField

## Group
grpInletBoundaryConditions grpOutletBoundaryConditions

## Description
This boundary condition provides a time-varying form of the uniform total
pressure boundary condition Foam::totalPressureFvPatchField.

## Usage

        Property     | Description                | Required    | Default value
        U            | Velocity field name        | no          | U
        phi          | Flux field name            | no          | phi
        rho          | Density field name         | no          | rho
        psi          | Compressibility field name | no          | none
        gamma        | (Cp/Cv)                    | no          | 1
        p0           | Total pressure as a function of time | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            uniformTotalPressure;
        p0              uniform 1e5;
}
```

The \c p0 entry is specified as a Function1 type, able to describe
time varying functions.

## See also
Foam::Function1Types
Foam::uniformFixedValueFvPatchField
Foam::totalPressureFvPatchField

## SourceFiles
uniformTotalPressureFvPatchScalarField.C

