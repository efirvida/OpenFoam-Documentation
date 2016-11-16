# LaunderSharmaKE.T 
## Class
Foam::RASModels::LaunderSharmaKE

## Group
grpRASTurbulence

## Description
Launder and Sharma low-Reynolds k-epsilon turbulence model for
incompressible and compressible and combusting flows including
rapid distortion theory (RDT) based compression term.

References:
```
        Launder, B. E., & Sharma, B. I. (1974).
        Application of the energy-dissipation model of turbulence to the
        calculation of flow near a spinning disc.
        Letters in heat and mass transfer, 1(2), 131-137.

        For the RDT-based compression term:
        El Tahry, S. H. (1983).
        k-epsilon equation for compressible reciprocating engine flows.
        Journal of Energy, 7(4), 345-353.
```

The default model coefficients are
```
        LaunderSharmaKECoeffs
        {
            Cmu         0.09;
            C1          1.44;
            C2          1.92;
            C3          -0.33;
            alphah      1.0;    // only for compressible
            alphahk     1.0;    // only for compressible
            alphaEps    0.76923;
        }
```

## SourceFiles
LaunderSharmaKE.C

