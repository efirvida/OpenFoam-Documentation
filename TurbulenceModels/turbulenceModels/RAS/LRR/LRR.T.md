# LRR.T 
## Class
Foam::RASModels::LRR

## Group
grpRASTurbulence

## Description
Launder, Reece and Rodi Reynolds-stress turbulence model for
incompressible and compressible flows.

Reference:
```
        Launder, B. E., Reece, G. J., & Rodi, W. (1975).
        Progress in the development of a Reynolds-stress turbulence closure.
        Journal of fluid mechanics, 68(03), 537-566.
```

Including the recommended generalized gradient diffusion model of
Daly and Harlow:
```
        Daly, B. J., & Harlow, F. H. (1970).
        Transport equations in turbulence.
        Physics of Fluids (1958-1988), 13(11), 2634-2649.
```

Optional Gibson-Launder wall-reflection is also provided:
```
        Gibson, M. M., & Launder, B. E. (1978).
        Ground effects on pressure fluctuations in the
        atmospheric boundary layer.
        Journal of Fluid Mechanics, 86(03), 491-511.
```

The default model coefficients are:
```
        LRRCoeffs
        {
            Cmu             0.09;
            C1              1.8;
            C2              0.6;
            Ceps1           1.44;
            Ceps2           1.92;
            Cs              0.25;
            Ceps            0.15;

            wallReflection  yes;
            kappa           0.41
            Cref1           0.5;
            Cref2           0.3;

            couplingFactor  0.0;
        }
```

## SourceFiles
LRR.C

