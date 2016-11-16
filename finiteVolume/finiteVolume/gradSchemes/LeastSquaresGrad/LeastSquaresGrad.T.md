# LeastSquaresGrad.T 
## Class
Foam::fv::LeastSquaresGrad

## Description
Gradient calculated using weighted least-squares on an arbitrary stencil.
The stencil type is provided via a template argument and any cell-based
stencil is supported:


        Stencil                     | Connections     | Scheme name
        centredCFCCellToCellStencil | cell-face-cell  | Not Instantiated
        centredCPCCellToCellStencil | cell-point-cell | pointCellsLeastSquares
        centredCECCellToCellStencil | cell-edge-cell  | edgeCellsLeastSquares


The first of these is not instantiated by default as the standard
leastSquaresGrad is equivalent and more efficient.

## Usage
Example of the gradient specification:
```
gradSchemes
{
        default         pointCellsLeastSquares;
}
```

## See also
Foam::fv::LeastSquaresVectors
Foam::fv::leastSquaresGrad

## SourceFiles
LeastSquaresGrad.C
LeastSquaresVectors.H
LeastSquaresVectors.C

