# kEpsilon 
## Class
Foam::RASModels::kEpsilon

## Group
grpRASTurbulence

## Description
Standard k-epsilon turbulence model for incompressible and compressible
flows including rapid distortion theory (RDT) based compression term.

Reference:
```
        Standard model:
            Launder, B. E., & Spalding, D. B. (1972).
            Lectures in mathematical models of turbulence.

            Launder, B. E., & Spalding, D. B. (1974).
            The numerical computation of turbulent flows.
            Computer methods in applied mechanics and engineering,
            3(2), 269-289.

        For the RDT-based compression term:
            El Tahry, S. H. (1983).
            k-epsilon equation for compressible reciprocating engine flows.
            Journal of Energy, 7(4), 345-353.
```

The default model coefficients are
```
        kEpsilonCoeffs
        {
            Cmu         0.09;
            C1          1.44;
            C2          1.92;
            C3          -0.33;
            sigmak      1.0;
            sigmaEps    1.3;
        }
```

## SourceFiles
kEpsilon.C

