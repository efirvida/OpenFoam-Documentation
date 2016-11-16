# mixtureKEpsilon 
## Class
Foam::RASModels::mixtureKEpsilon

## Group
grpRASTurbulence

## Description
Mixture k-epsilon turbulence model for two-phase gas-liquid systems

The basic structure of the model is based on:
```
        Behzadi, A., Issa, R. I., & Rusche, H. (2004).
        Modelling of dispersed bubble and droplet flow at high phase fractions.
        Chemical Engineering Science, 59(4), 759-770.
```

but an effective density for the gas is used in the averaging and an
alternative model for bubble-generated turbulence from:
```
        Lahey Jr, R. T. (2005).
        The simulation of multidimensional multiphase flows.
        Nuclear Engineering and Design, 235(10), 1043-1060.
```

The default model coefficients are
```
        mixtureKEpsilonCoeffs
        {
            Cmu         0.09;
            C1          1.44;
            C2          1.92;
            C3          C2;
            sigmak      1.0;
            sigmaEps    1.3;
        }
```

## SourceFiles
mixtureKEpsilon.C

