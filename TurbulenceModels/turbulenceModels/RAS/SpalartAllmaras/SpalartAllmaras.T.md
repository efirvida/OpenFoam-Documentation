# SpalartAllmaras.T 
## Class
Foam::RASModels::SpalartAllmaras

## Group
grpRASTurbulence

## Description
Spalart-Allmaras one-eqn mixing-length model for incompressible and
compressible external flows.

Reference:
```
        Spalart, P.R., & Allmaras, S.R. (1994).
        A one-equation turbulence model for aerodynamic flows.
        La Recherche Aerospatiale, 1, 5-21.
```

The model is implemented without the trip-term and hence the ft2 term is
not needed.

It is necessary to limit the Stilda generation term as the model generates
unphysical results if this term becomes negative which occurs for complex
flow.  Several approaches have been proposed to limit Stilda but it is not
clear which is the most appropriate.  Here the limiter proposed by Spalart
is implemented in which Stilda is clipped at Cs*Omega with the default value
of Cs = 0.3.

The default model coefficients are
```
        SpalartAllmarasCoeffs
        {
            Cb1         0.1355;
            Cb2         0.622;
            Cw2         0.3;
            Cw3         2.0;
            Cv1         7.1;
            Cs          0.3;
            sigmaNut    0.66666;
            kappa       0.41;
        }
```

## SourceFiles
SpalartAllmaras.C

