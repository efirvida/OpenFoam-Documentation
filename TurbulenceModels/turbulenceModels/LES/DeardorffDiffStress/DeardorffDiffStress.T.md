# DeardorffDiffStress.T 
## Class
Foam::LESModels::DeardorffDiffStress

## Group
grpLESTurbulence

## Description
Differential SGS Stress Equation Model for incompressible and
compressible flows

Reference:
```
        Deardorff, J. W. (1973).
        The use of subgrid transport equations in a three-dimensional model
        of atmospheric turbulence.
        Journal of Fluids Engineering, 95(3), 429-438.
```

This SGS model uses a full balance equation for the SGS stress tensor to
simulate the behaviour of B.

This implementation is as described in the above paper except that the
triple correlation model of Donaldson is replaced with the generalized
gradient diffusion model of Daly and Harlow:
```
        Daly, B. J., & Harlow, F. H. (1970).
        Transport equations in turbulence.
        Physics of Fluids (1958-1988), 13(11), 2634-2649.
```
with the default value for the coefficient Cs of 0.25 from
```
        Launder, B. E., Reece, G. J., & Rodi, W. (1975).
        Progress in the development of a Reynolds-stress turbulence closure.
        Journal of fluid mechanics, 68(03), 537-566.
```

## SourceFiles
DeardorffDiffStress.C

