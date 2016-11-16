# kOmega 
## Class
Foam::RASModels::kOmega

## Group
grpRASTurbulence

## Description
Standard high Reynolds-number k-omega turbulence model for
incompressible and compressible flows.

References:
```
        Wilcox, D. C. (1998).
        Turbulence modeling for CFD
        (Vol. 2, pp. 103-217). La Canada, CA: DCW industries.
```

The default model coefficients are
```
        kOmegaCoeffs
        {
            Cmu         0.09;  // Equivalent to betaStar
            alpha       0.52;
            beta        0.072;
            alphak      0.5;
            alphaOmega  0.5;
        }
```

## SourceFiles
kOmega.C

