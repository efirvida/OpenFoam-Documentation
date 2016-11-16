# LduMatrix.T 
## Class
Foam::LduMatrix

## Description
LduMatrix is a general matrix class in which the coefficients are
stored as three arrays, one for the upper triangle, one for the
lower triangle and a third for the diagonal.

Addressing arrays must be supplied for the upper and lower triangles.

## Note
It might be better if this class were organised as a hierachy starting
from an empty matrix, then deriving diagonal, symmetric and asymmetric
matrices.

## SourceFiles
LduMatrixATmul.C
LduMatrix.C
LduMatrixOperations.C
LduMatrixSolver.C
LduMatrixPreconditioner.C
LduMatrixTests.C
LduMatrixUpdateMatrixInterfaces.C

