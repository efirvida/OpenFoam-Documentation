# SmagorinskyZhang.T 
## Class
Foam::LESModels::SmagorinskyZhang

## Group
grpLESTurbulence

## Description
The Smagorinsky SGS model including bubble-generated turbulence

Reference:
```
        Zhang, D., Deen, N. G., & Kuipers, J. A. M. (2006).
        Numerical simulation of the dynamic flow behavior in a bubble column:
        a study of closures for turbulence and interface forces.
        Chemical Engineering Science, 61(23), 7593-7608.
```

The default model coefficients are
```
        SmagorinskyZhangCoeffs
        {
            Ck              0.094;
            Ce              1.048;
            Cmub            0.6;
        }
```

## SourceFiles
SmagorinskyZhang.C

