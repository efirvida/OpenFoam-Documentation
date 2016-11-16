# topoCellLooper 
## Class
Foam::topoCellLooper

## Description
Implementation of cellLooper. This one recognizes splitHexes and tries
to make a cut such that if the neighbour was split (in a previous iteration)
this one also gets split in the same direction so that the result
will be a mesh without splitHexes.

'splitHexes' are cells of which the 'featureEdges'
(see cellFeatures class) form a hex. The remaining non-feature edges
are assumed to result from splitting the neighbour and this class tries
to start from one of these and cut through to an opposite edge.

The current set of cuts (vertIsCut, edgeIsCut, edgeWeight) are not being
used by this implementation.

All non-splitHexes are done by the parent classes.


## SourceFiles
topoCellLooper.C

