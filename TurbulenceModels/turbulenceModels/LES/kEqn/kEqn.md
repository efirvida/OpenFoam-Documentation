# kEqn 
## Class
Foam::LESModels::kEqn

## Group
grpLESTurbulence

## Description
One equation eddy-viscosity model

Eddy viscosity SGS model using a modeled balance equation to simulate the
behaviour of k.

Reference:
```
        Yoshizawa, A. (1986).
        Statistical theory for compressible turbulent shear flows,
        with the application to subgrid modeling.
        Physics of Fluids (1958-1988), 29(7), 2152-2164.
```

The default model coefficients are
```
        kEqnCoeffs
        {
            Ck                  0.094;
            Ce                  1.048;
        }
```

## SourceFiles
kEqn.C

