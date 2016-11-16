# realizableKE 
## Class
Foam::RASModels::realizableKE

## Group
grpRASTurbulence

## Description
Realizable k-epsilon turbulence model for incompressible and compressible
flows.

References:
```
        Shih, T. H., Liou, W. W., Shabbir, A., Yang, Z., & Zhu, J. (1994).
        A new k-epsilon eddy viscosity model for high Reynolds number
        turbulent flows: Model development and validation.
        NASA STI/Recon Technical Report N, 95, 11442.

        Shih, T. H., Liou, W. W., Shabbir, A., Yang, Z., & Zhu, J. (1995).
        A New k-epsilon Eddy Viscosity Model for High Reynolds Number
        Turbulent Flows.
        Computers and Fluids, 24(3), 227-238.
```

The default model coefficients are
```
        realizableKECoeffs
        {
            Cmu         0.09;
            A0          4.0;
            C2          1.9;
            sigmak      1.0;
            sigmaEps    1.2;
        }
```

## SourceFiles
realizableKE.C

