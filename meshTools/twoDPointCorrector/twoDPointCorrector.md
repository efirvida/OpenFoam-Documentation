# twoDPointCorrector 
## Class
Foam::twoDPointCorrector

## Description
Class applies a two-dimensional correction to mesh motion point field.

The correction guarantees that the mesh does not get twisted during motion
and thus introduce a third dimension into a 2-D problem.

The operation is performed by looping through all edges approximately
normal to the plane and enforcing their orthogonality onto the plane by
adjusting points on their ends.

## SourceFiles
twoDPointCorrector.C

