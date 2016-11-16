# PrandtlDelta 
## Class
Foam::PrandtlDelta

## Description
Apply Prandtl mixing-length based damping function to the specified
geometric delta to improve near-wall behavior or LES models.

```
        delta = min(geometricDelta, (kappa/Cdelta)*y)
```

Example specification in the turbulenceProperties dictionary:
```
    delta           Prandtl;

PrandtlCoeffs
{
        delta   cubeRootVol;

        cubeRootVolCoeffs
        {
            deltaCoeff      1;
        }

        // Default coefficients
        kappa           0.41;
        Cdelta          0.158;
}
```

## SourceFiles
PrandtlDelta.C

