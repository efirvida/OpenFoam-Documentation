# CoEulerDdtScheme.T 
## Class
Foam::fv::CoEulerDdtScheme

## Description
Courant number limited first-order Euler implicit/explicit ddt.

The time-step is adjusted locally so that the local Courant number
does not exceed the specified value.

This scheme should only be used for steady-state computations
using transient codes where local time-stepping is preferable to
under-relaxation for transport consistency reasons.

## SourceFiles
CoEulerDdtScheme.C

