# rotatingTotalPressureFvPatchScalarField 
## Class
Foam::rotatingTotalPressureFvPatchScalarField

## Group
grpInletBoundaryConditions grpOutletBoundaryConditions

## Description
This boundary condition provides a total pressure condition for patches
in a rotating frame.

## Usage

        Property     | Description             | Required    | Default value
        U            | velocity field name     | no          | U
        phi          | flux field name         | no          | phi
        rho          | density field name      | no          | none
        psi          | compressibility field name | no       | none
        gamma        | ratio of specific heats (Cp/Cv) | yes |
        p0           | static pressure reference | yes       |
        omega        | angular velocty of the frame [rad/s] | yes    |


Example of the boundary condition specification:
```
<patchName>
{
        type            rotatingTotalPressure;
        U               U;
        phi             phi;
        rho             rho;
        psi             psi;
        gamma           1.4;
        p0              uniform 1e5;
        omega           100;
}
```

The \c omega entry is a Function1 type, able to describe time varying
functions.

## See also
Foam::totalPressureFvPatchScalarField
Foam::Function1Types

## SourceFiles
rotatingTotalPressureFvPatchScalarField.C

