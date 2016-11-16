# CoBlended.T 
## Class
Foam::CoBlended

## Description
Two-scheme Courant number based blending differencing scheme.

Similar to localBlended but uses a blending factor computed from the
face-based Courant number and the lower and upper Courant number limits
supplied:
\f[
        weight = 1 - max(min((Co - Co1)/(Co2 - Co1), 1), 0)
\f]
where
\vartable
        Co1 | Courant number below which scheme1 is used
        Co2 | Courant number above which scheme2 is used
\endvartable

The weight applies to the first scheme and 1-weight to the second scheme.

Example of the CoBlended scheme specification using LUST for Courant numbers
less than 1 and linearUpwind for Courant numbers greater than 10:
```
divSchemes
{
        .
        .
        div(phi,U)      Gauss CoBlended 1 LUST grad(U) 10 linearUpwind grad(U);
        .
        .
}
```

## SourceFiles
CoBlended.C

