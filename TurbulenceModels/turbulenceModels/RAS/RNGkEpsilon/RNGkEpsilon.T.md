# RNGkEpsilon.T 
## Class
Foam::RASModels::RNGkEpsilon

## Group
grpRASTurbulence

## Description
Renormalization group k-epsilon turbulence model for incompressible and
compressible flows.

Reference:
```
        Yakhot, V., Orszag, S. A., Thangam, S.,
        Gatski, T. B., & Speziale, C. G. (1992).
        Development of turbulence models for shear flows
        by a double expansion technique.
        Physics of Fluids A: Fluid Dynamics (1989-1993), 4(7), 1510-1520.

For the RDT-based compression term:
        El Tahry, S. H. (1983).
        k-epsilon equation for compressible reciprocating engine flows.
        Journal of Energy, 7(4), 345-353.
```

The default model coefficients are
```
        RNGkEpsilonCoeffs
        {
            Cmu         0.0845;
            C1          1.42;
            C2          1.68;
            C3          -0.33;
            sigmak      0.71942;
            sigmaEps    0.71942;
            eta0        4.38;
            beta        0.012;
        }
```

## SourceFiles
RNGkEpsilon.C

