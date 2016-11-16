# continuousGasKEpsilon 
## Class
Foam::RASModels::continuousGasKEpsilon

## Group
grpRASTurbulence

## Description
k-epsilon model for the gas-phase in a two-phase system
supporting phase-inversion.

In the limit that the gas-phase fraction approaches zero a contribution from
the other phase is blended into the k and epsilon equations up to the
phase-fraction of alphaInversion at which point phase-inversion is
considered to have occurred and the model reverts to the pure single-phase
form.

This model is unpublished and is provided as a stable numerical framework
on which a more physical model may be built.

The default model coefficients are
```
        continuousGasKEpsilonCoeffs
        {
            Cmu             0.09;
            C1              1.44;
            C2              1.92;
            C3              -0.33;
            sigmak          1.0;
            sigmaEps        1.3;
            alphaInversion  0.7;
        }
```

## SourceFiles
continuousGasKEpsilon.C

