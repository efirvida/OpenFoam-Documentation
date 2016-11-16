# geometricZeroField 
## Class
Foam::geometricZeroField

## Description
A class representing the concept of a GeometricField of 1 used to avoid
unnecessary manipulations for objects which are known to be zero at
compile-time.

Used for example as the density argument to a function written for
compressible to be used for incompressible flow.

