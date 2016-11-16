# kOmegaSSTSAS 
## Class
Foam::RASModels::kOmegaSSTSAS

## Group
grpLESTurbulence

## Description
Scale-adaptive URAS model based on the k-omega-SST RAS model.

References:
```
        Egorov, Y., & Menter F.R. (2008).
        Development and Application of SST-SAS Model in the DESIDER Project.
        Advances in Hybrid RANS-LES Modelling,
        Notes on Num. Fluid Mech. And Multidisciplinary Design,
        Volume 97, 261-270.
```

The model coefficients are
```
        kOmegaSSTSASCoeffs
        {
            // Default SST coefficients
            alphaK1     0.85;
            alphaK2     1.0;
            alphaOmega1 0.5;
            alphaOmega2 0.856;
            beta1       0.075;
            beta2       0.0828;
            betaStar    0.09;
            gamma1      5/9;
            gamma2      0.44;
            a1          0.31;
            b1          1.0;
            c1          10.0;
            F3          no;

            // Default SAS coefficients
            Cs          0.11;
            kappa       0.41;
            zeta2       3.51;
            sigmaPhi    2.0/3.0;
            C           2;

            // Delta must be specified for SAS e.g.
            delta cubeRootVol;

            cubeRootVolCoeffs
            {}
        }
```

## SourceFiles
kOmegaSSTSAS.C

