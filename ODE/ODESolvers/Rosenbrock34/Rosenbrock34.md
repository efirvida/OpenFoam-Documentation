# Rosenbrock34 
## Class
Foam::Rosenbrock34

## Description
L-stable embedded Rosenbrock ODE solver of order (3)4.

```
        "Solving Ordinary Differential Equations II: Stiff
         and Differential-Algebraic Problems, second edition",
        Hairer, E.,
        Nørsett, S.,
        Wanner, G.,
        Springer-Verlag, Berlin. 1996.
```

The default constants are from:
```
        "Implementation of Rosenbrock Methods"
        Shampine, L. F.,
        ACM Transactions on Mathematical Software, vol. 8, 1982, pp. 93–113.
```
with which the scheme is more accurate than with the L-Stable coefficients
for small step-size but less stable for large step-size.

The L-Stable scheme constants are provided commented-out in Rosenbrock34.C

## SourceFiles
Rosenbrock34.C

