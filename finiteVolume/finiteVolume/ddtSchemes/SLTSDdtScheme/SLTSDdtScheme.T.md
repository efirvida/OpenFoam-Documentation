# SLTSDdtScheme.T 
## Class
Foam::fv::SLTSDdtScheme

## Description
Stabilised local time-step first-order Euler implicit/explicit ddt.
The time-step is adjusted locally so that an advective equations remains
diagonally dominant.

This scheme should only be used for steady-state computations
using transient codes where local time-stepping is preferably to
under-relaxation for transport consistency reasons.

## See also
Foam::fv::CoEulerDdtScheme

## SourceFiles
SLTSDdtScheme.C

