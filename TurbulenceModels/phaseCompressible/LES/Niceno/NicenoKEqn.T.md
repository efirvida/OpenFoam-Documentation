# NicenoKEqn.T 
## Class
Foam::LESModels::NicenoKEqn

## Group
grpLESTurbulence

## Description
One-equation SGS model for the continuous phase in a two-phase system
including bubble-generated turbulence.

Reference:
```
        Niceno, B., Dhotre, M. T., & Deen, N. G. (2008).
        One-equation sub-grid scale (SGS) modelling for
        Euler–Euler large eddy simulation (EELES) of dispersed bubbly flow.
        Chemical Engineering Science, 63(15), 3923-3931.
```

The default model coefficients are:
```
        NicenoKEqnCoeffs
        {
            Ck              0.094;
            Ce              1.048;
            alphaInversion  0.3;
            Cp              Ck;
            Cmub            0.6;
        }
```

## SourceFiles
NicenoKEqn.C

