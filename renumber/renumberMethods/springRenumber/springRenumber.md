# springRenumber 
## Class
Foam::springRenumber

## Description
Use spring analogy - attract neighbouring cells according to the distance
of their cell indices.

// Maximum jump of cell indices. Is fraction of number of cells
maxCo 0.1;

// Limit the amount of movement; the fraction maxCo gets decreased
// with every iteration.
freezeFraction 0.9;

// Maximum number of iterations
maxIter 1000;

## SourceFiles
springRenumber.C

