# cellCoBlended 
## Class
Foam::cellCoBlended

## Description
Two-scheme cell-based Courant number based blending differencing scheme.

This scheme is equivalent to the CoBlended scheme except that the Courant
number is evaluated for cells using the same approach as use in the
finite-volume solvers and then interpolated to the faces rather than being
estimated directly at the faces based on the flux.  This is a more
consistent method for evaluating the Courant number but suffers from the
need to interpolate which introduces a degree of freedom.  However, the
interpolation scheme for "Co" is run-time selected and may be specified in
"interpolationSchemes" and "localMax" might be most appropriate.

Example of the cellCoBlended scheme specification using LUST for Courant
numbers less than 1 and linearUpwind for Courant numbers greater than 10:
```
divSchemes
{
        .
        .
        div(phi,U)  Gauss cellCoBlended 1 LUST grad(U) 10 linearUpwind grad(U);
        .
        .
}

interpolationSchemes
{
        .
        .
        interpolate(Co) localMax;
        .
        .
}
```

## See also
Foam::CoBlended
Foam::localBlended

## SourceFiles
cellCoBlended.C

