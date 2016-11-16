# lduMatrix 
## Class
Foam::lduMatrix

## Description
lduMatrix is a general matrix class in which the coefficients are
stored as three arrays, one for the upper triangle, one for the
lower triangle and a third for the diagonal.

Addressing arrays must be supplied for the upper and lower triangles.

It might be better if this class were organised as a hierachy starting
from an empty matrix, then deriving diagonal, symmetric and asymmetric
matrices.

## SourceFiles
lduMatrixATmul.C
lduMatrix.C
lduMatrixTemplates.C
lduMatrixOperations.C
lduMatrixSolver.C
lduMatrixPreconditioner.C
lduMatrixTests.C
lduMatrixUpdateMatrixInterfaces.C

