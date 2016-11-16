# CrankNicolsonDdtScheme.T 
## Class
Foam::fv::CrankNicolsonDdtScheme

## Description
Second-oder Crank-Nicolson implicit ddt using the current and
previous time-step fields as well as the previous time-step ddt.

The Crank-Nicolson scheme is often unstable for complex flows in complex
geometries and it is necessary to "off-centre" the scheme to stabilize it
while retaining greater temporal accuracy than the first-order
Euler-implicit scheme.  Off-centering is specified via the mandatory
coefficient in the range [0,1] following the scheme name e.g.
```
ddtSchemes
{
        default         CrankNicolson 0.9;
}
```
With a coefficient of 1 the scheme is fully centred and second-order,
with a coefficient of 0 the scheme is equivalent to Euler-implicit.
A coefficient of 0.9 has been found to be suitable for a range of cases for
which higher-order accuracy in time is needed and provides similar accuracy
and stability to the backward scheme.  However, the backward scheme has
been found to be more robust and provides formal second-order accuracy in
time.

The advantage of the Crank-Nicolson scheme over backward is that only the
new and old-time values are needed, the additional terms relating to the
fluxes and sources are evaluated at the mid-point of the time-step which
provides the opportunity to limit the fluxes in such a way as to ensure
boundedness while maintaining greater accuracy in time compared to the
Euler-implicit scheme.  This approach is now used with MULES in the
interFoam family of solvers.  Boundedness cannot be guaranteed with the
backward scheme.

## Note
The Crank-Nicolson coefficient for the implicit part of the RHS is related
to the off-centering coefficient by
```
        cnCoeff = 1.0/(1.0 + ocCoeff);
```

## See also
Foam::Euler
Foam::backward

## SourceFiles
CrankNicolsonDdtScheme.C

