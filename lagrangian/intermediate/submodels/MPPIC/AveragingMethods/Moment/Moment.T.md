# Moment.T 
## Class
Foam::AveragingMethods::Moment

## Description
Moment lagrangian averaging procedure.

Point values and moments from the cell centroid are summed over
computational cells. A linear function is generated which has the same
integrated moment as that of the point data.

The computed linear function is used to interpolate values within a cell.
The gradient is calculated from the coefficients of the function, and is
assumed constant over the cell.

## SourceFiles
Moment.C

