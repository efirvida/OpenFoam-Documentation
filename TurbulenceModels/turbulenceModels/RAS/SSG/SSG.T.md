# SSG.T 
## Class
Foam::RASModels::SSG

## Group
grpRASTurbulence

## Description
Speziale, Sarkar and Gatski Reynolds-stress turbulence model for
incompressible and compressible flows.

Reference:
```
        Speziale, C. G., Sarkar, S., & Gatski, T. B. (1991).
        Modelling the pressure–strain correlation of turbulence:
        an invariant dynamical systems approach.
        Journal of Fluid Mechanics, 227, 245-272.
```

Including the generalized gradient diffusion model of
Daly and Harlow:
```
        Daly, B. J., & Harlow, F. H. (1970).
        Transport equations in turbulence.
        Physics of Fluids (1958-1988), 13(11), 2634-2649.
```

The default model coefficients are:
```
        SSGCoeffs
        {
            Cmu             0.09;

            C1              3.4;
            C1s             1.8;
            C2              4.2;
            C3              0.8;
            C3s             1.3;
            C4              1.25;
            C5              0.4;

            Ceps1           1.44;
            Ceps2           1.92;
            Cs              0.25;
            Ceps            0.15;

            couplingFactor  0.0;
        }
```

## SourceFiles
SSG.C

