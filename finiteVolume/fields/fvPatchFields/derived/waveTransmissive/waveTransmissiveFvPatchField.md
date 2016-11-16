# waveTransmissiveFvPatchField 
## Class
Foam::waveTransmissiveFvPatchField

## Group
grpOutletBoundaryConditions

## Description
This boundary condition provides a wave transmissive outflow condition,
based onsolving DDt(psi, U) = 0 at the boundary.

The wave speed is calculated using:

        \f[
            x_p = \frac{\phi_p}{|Sf|} + \sqrt{\frac{\gamma}{\psi_p}}
        \f]

where

\vartable
        x_p     | patch values
        \phi_p  | patch face flux
        \psi_p  | patch compressibility
        Sf      | patch face area vector
        \gamma  | ratio of specific heats
\endvartable

## Usage

        Property     | Description             | Required    | Default value
        phi          | flux field name         | no          | phi
        rho          | density field name      | no          | rho
        psi          | compressibility field name | no       | psi
        gamma        | ratio of specific heats (Cp/Cv) | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            waveTransmissive;
        phi             phi;
        psi             psi;
        gamma           1.4;
}
```

## See also
Foam::advectiveFvPatchField

## SourceFiles
waveTransmissiveFvPatchField.C

