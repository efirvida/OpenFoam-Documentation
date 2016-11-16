# WALE.T 
## Class
Foam::LESModels::WALE

## Group
grpLESTurbulence

## Description
The Wall-adapting local eddy-viscosity (WALE) SGS model.

Reference:
```
        Nicoud, F., & Ducros, F. (1999).
        Subgrid-scale stress modelling based on the square of the velocity
        gradient tensor.
        Flow, Turbulence and Combustion, 62(3), 183-200.
```

The default model coefficients are
```
        WALECoeffs
        {
            Ck                  0.094;
            Ce                  1.048;e
            Cw                  0.325;
        }
```

## See also
Foam::LESModels::Smagorinsky

## SourceFiles
WALE.C

