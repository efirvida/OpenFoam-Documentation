# Dual.T 
## Class
Foam::AveragingMethods::Dual

## Description
Dual-mesh lagrangian averaging procedure.

Point values are summed using the tetrahedral decomposition of the
computational cells. Summation is done in the cells, and also in the
terahedrons surrounding each point. The latter forms a type of dual mesh.
The interpolation is weighted by proximity to the cell centre or point, as
calculated by the barycentric coordinate within the tethrahedron.

Values are interpolated linearly across the tethrahedron. Gradients are
calculated directly from the point values using a first order finite
element basis. The computed gradient is assumed constant over the
tethrahedron.

## SourceFiles
Dual.C

