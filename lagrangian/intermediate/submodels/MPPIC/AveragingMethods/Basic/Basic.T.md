# Basic.T 
## Class
Foam::AveragingMethods::Basic

## Description
Basic lagrangian averaging procedure.

This is a cell-volume based average. Point values are summed over the
computational cells and the result is divided by the cell volume.

Interpolation is done assuming a constant value over each cells. Cell
gradients are calculated by the default fvc::grad scheme, and are also
assumed constant when interpolated.

## SourceFiles
Basic.C

