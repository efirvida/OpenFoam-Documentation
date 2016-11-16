# Smagorinsky.T 
## Class
Foam::LESModels::Smagorinsky

## Group
grpLESTurbulence

## Description
The Smagorinsky SGS model.

Reference:
```
        Smagorinsky, J. (1963).
        General circulation experiments with the primitive equations: I.
        The basic experiment*.
        Monthly weather review, 91(3), 99-164.
```

The form of the Smagorinsky model implemented is obtained from the
k-equation model assuming local equilibrium which provides estimates of both
k and epsilon separate from the sub-grid scale viscosity:

```
        B = 2/3*k*I - 2*nuSgs*dev(D)

where

        D = symm(grad(U));
        k from D:B + Ce*k^3/2/delta = 0
        nuSgs = Ck*sqrt(k)*delta
```

The default model coefficients are
```
        SmagorinskyCoeffs
        {
            Ck                  0.094;
            Ce                  1.048;
        }
```

## See also
Foam::LESModels::kEqn

## SourceFiles
Smagorinsky.C

