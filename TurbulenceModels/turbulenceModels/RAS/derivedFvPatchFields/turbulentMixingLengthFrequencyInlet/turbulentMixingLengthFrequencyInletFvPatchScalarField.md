# turbulentMixingLengthFrequencyInletFvPatchScalarField 
## Class
Foam::turbulentMixingLengthFrequencyInletFvPatchScalarField

## Group
grpRASBoundaryConditions grpInletBoundaryConditions

## Description
This boundary condition provides a turbulence specific dissipation,
\f$\omega\f$ (omega) inlet condition based on a specified mixing length.
The patch values are calculated using:

        \f[
            \omega_p = \frac{k^{0.5}}{C_{\mu}^{0.25} L}
        \f]

where

\vartable
        \omega_p | patch omega values
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
        type            turbulentMixingLengthFrequencyInlet;
        mixingLength    0.005;
        value           uniform 200;   // placeholder
}
```

## Note
In the event of reverse flow, a zero-gradient condition is applied

## See also
Foam::inletOutletFvPatchField


## SourceFiles
turbulentMixingLengthFrequencyInletFvPatchScalarField.C

