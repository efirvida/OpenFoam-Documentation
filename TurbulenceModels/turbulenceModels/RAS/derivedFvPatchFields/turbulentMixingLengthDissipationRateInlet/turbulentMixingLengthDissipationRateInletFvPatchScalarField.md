# turbulentMixingLengthDissipationRateInletFvPatchScalarField 
## Class
Foam::turbulentMixingLengthDissipationRateInletFvPatchScalarField

## Group
grpRASBoundaryConditions grpInletBoundaryConditions

## Description
This boundary condition provides a turbulence dissipation, \f$\epsilon\f$
(epsilon) inlet condition based on a specified mixing length.  The patch
values are calculated using:

        \f[
            \epsilon_p = \frac{C_{\mu}^{0.75} k^{1.5}}{L}
        \f]

where

\vartable
        \epsilon_p | patch epsilon values
        C_{\mu} | Model coefficient, set to 0.09
        k       | turbulence kinetic energy
        L       | length scale
\endvartable

## Usage

        Property     | Description             | Required    | Default value
        mixingLength | Length scale [m]        | yes         |
        phi          | flux field name         | no          | phi
        k            | turbulence kinetic energy field name | no | k


Example of the boundary condition specification:
```
<patchName>
{
        type            turbulentMixingLengthDissipationRateInlet;
        mixingLength    0.005;
        value           uniform 200;   // placeholder
}
```

## Note
In the event of reverse flow, a zero-gradient condition is applied

## See also
Foam::inletOutletFvPatchField

## SourceFiles
turbulentMixingLengthDissipationRateInletFvPatchScalarField.C

