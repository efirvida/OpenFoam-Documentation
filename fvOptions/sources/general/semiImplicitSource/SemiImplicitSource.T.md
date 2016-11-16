# SemiImplicitSource.T 
## Class
Foam::fv::SemiImplicitSource

## Description
Semi-implicit source, described using an input dictionary.  The injection
rate coefficients are specified as pairs of Su-Sp coefficients, i.e.

        \f[
            S(x) = S_u + S_p x
        \f]

where
\vartable
        S(x)    | net source for field 'x'
        S_u     | explicit source contribution
        S_p     | linearised implicit contribution
\endvartable

Example of the source specification:

```
<Type>SemiImplicitSourceCoeffs
{
        volumeMode      absolute; // specific
        injectionRateSuSp
        {
            k           (30.7 0);
            epsilon     (1.5  0);
        }
}
```

Valid options for the \c volumeMode entry include:
- absolute: values are given as \<quantity\>
- specific: values are given as \<quantity\>/m3

## See also
Foam::fvOption

## SourceFiles
SemiImplicitSource.C

