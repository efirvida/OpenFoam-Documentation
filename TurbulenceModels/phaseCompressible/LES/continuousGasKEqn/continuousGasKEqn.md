# continuousGasKEqn 
## Class
Foam::LESModels::continuousGasKEqn

## Group
grpLESTurbulence

## Description
One-equation SGS model for the gas-phase in a two-phase system
supporting phase-inversion.

In the limit that the gas-phase fraction approaches zero a contribution from
the other phase is blended into the k-equation up to the phase-fraction of
alphaInversion at which point phase-inversion is considered to have occurred
and the model reverts to the pure single-phase form.

This model is unpublished and is provided as a stable numerical framework
on which a more physical model may be built.

The default model coefficients are
```
        continuousKEqnCoeffs
        {
            Ck              0.094;
            Ce              1.048;
            alphaInversion  0.7;
        }
```

## SourceFiles
continuousGasKEqn.C

