# turbulentIntensityKineticEnergyInletFvPatchScalarField 
## Class
Foam::turbulentIntensityKineticEnergyInletFvPatchScalarField

## Group
grpInletBoundaryConditions

## Description
This boundary condition provides a turbulent kinetic energy condition,
based on user-supplied turbulence intensity, defined as a fraction of the
mean velocity:

        \f[
            k_p = 1.5 (I |U|)^2
        \f]

where

\vartable
        k_p     | kinetic energy at the patch
        I       | turbulence intensity
        U       | velocity field
\endvartable

In the event of reverse flow, a zero-gradient condition is applied.

## Usage

        Property     | Description             | Required    | Default value
        intensity    | fraction of mean field [0-1] | yes    |
        U            | velocity field name     | no          | U
        phi          | flux field name         | no          | phi


Example of the boundary condition specification:
```
<patchName>
{
        type        turbulentIntensityKineticEnergyInlet;
        intensity   0.05;           // 5% turbulence
        value       uniform 1;      // placeholder
}
```

## See also
Foam::inletOutletFvPatchField

## SourceFiles
turbulentIntensityKineticEnergyInletFvPatchScalarField.C

