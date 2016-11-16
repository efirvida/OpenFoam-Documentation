# zeroField 
## Class
Foam::zeroField

## Description
A class representing the concept of a field of 0 used to avoid unnecessary
manipulations for objects which are known to be zero at compile-time.

Used for example as the argument to a function in which certain terms are
optional, see source terms in the MULES solvers.

