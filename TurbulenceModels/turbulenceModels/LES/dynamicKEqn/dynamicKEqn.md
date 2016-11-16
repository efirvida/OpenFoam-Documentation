# dynamicKEqn 
## Class
     Foam::LESModels::dynamicKEqn

## Group
grpLESTurbulence

## Description
Dynamic one equation eddy-viscosity model

Eddy viscosity SGS model using a modeled balance equation to simulate
the behaviour of k in which a dynamic procedure is applied to evaluate the
coefficients.

Reference:
```
        Kim, W and Menon, S. (1995).
        A new dynamic one-equation subgrid-scale model for
        large eddy simulation.
        In 33rd Aerospace Sciences Meeting and Exhibit, Reno, NV, 1995.
```

There are no default model coefficients but the filter used for KK must be
supplied, e.g.
```
        dynamicKEqnCoeffs
        {
            filter simple;
        }
```

## SourceFiles
dynamicKEqn.C

