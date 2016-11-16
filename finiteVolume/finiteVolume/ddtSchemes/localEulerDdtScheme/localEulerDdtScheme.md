# localEulerDdtScheme 
## Class
Foam::fv::localEulerDdtScheme

## Description
Local time-step first-order Euler implicit/explicit ddt.

The reciprocal of the local time-step field is looked-up from the database.

This scheme should only be used for steady-state computations using
transient codes where local time-stepping is preferably to under-relaxation
for transport consistency reasons.

## See also
Foam::fv::CoEulerDdtScheme

## SourceFiles
localEulerDdt.C
localEulerDdtScheme.C
localEulerDdtSchemes.C

