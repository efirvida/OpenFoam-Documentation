# LaheyKEpsilon.T 
## Class
Foam::RASModels::LaheyKEpsilon

## Group
grpRASTurbulence

## Description
Continuous-phase k-epsilon model including bubble-generated turbulence.

Reference:
```
        Lahey Jr, R. T. (2005).
        The simulation of multidimensional multiphase flows.
        Nuclear Engineering and Design, 235(10), 1043-1060.
```

The default model coefficients are
```
        LaheyKEpsilonCoeffs
        {
            Cmu             0.09;
            C1              1.44;
            C2              1.92;
            C3              -0.33;
            sigmak          1.0;
            sigmaEps        1.3;
            Cp              0.25;
            Cmub            0.6;
            alphaInversion  0.3;
        }
```

## SourceFiles
LaheyKEpsilon.C

