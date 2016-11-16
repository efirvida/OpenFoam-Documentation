# MatrixBlock.T 
## Class
Foam::MatrixBlock

## Description
A templated block of an (m x n) matrix of type \<MatrixType\>.

        Foam::ConstMatrixBlock: block of a const matrix
        Foam::MatrixBlock: block of a non-const matrix

The block may be assigned to a block of another matrix or to a VectorSpace
or MatrixSpace e.g. \c tensor.  Conversion of a column block to a \c
Field<T> is also provide.

## SourceFiles
MatrixBlock.C
MatrixBlockI.H

