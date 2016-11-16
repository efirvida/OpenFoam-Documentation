# globalMeshData 
## Class
Foam::globalMeshData

## Description
Various mesh related information for a parallel run. Upon construction,
constructs all info using parallel communication.

Requires:
- all processor patches to have correct ordering.
- all processorPatches to have their transforms set.

The shared point and edge addressing calculates addressing for points
and edges on coupled patches.  In the 'old' way a distinction was made
between points/edges that are only on two processors and those that are
on multiple processors.  The problem is that those on multiple processors
do not allow any transformations and require a global reduction on the
master processor.

The alternative is to have an exchange schedule (through a 'mapDistribute')
which sends all point/edge data (no distinction is made between
those on two and those on more than two coupled patches) to the local
'master'.  This master then does any calculation and sends
the result back to the 'slave' points/edges.  This only needs to be done
on points on coupled faces.  Any transformation is done using a
predetermined set of transformations - since transformations have to be
space filling only a certain number of transformation is supported.

The exchange needs
- a field of data
- a mapDistribute which does all parallel exchange and transformations
      This appends remote data to the end of the field.
- a set of indices which indicate where to get untransformed data in the
      field
- a set of indices which indicate where to get transformed data in the
      field

## Note
- compared to 17x nTotalFaces, nTotalPoints do not compensate for
      shared points since this would trigger full connectivity analysis
- most calculation is demand driven and uses parallel communication
      so make sure to invoke on all processors at the same time
- old sharedEdge calculation: currently an edge is considered shared
      if it uses two shared points and is used more than once.  This is not
      correct on processor patches but it only slightly overestimates the number
      of shared edges.  Doing full analysis of how many patches use the edge
      would be too complicated

## See also
mapDistribute
globalIndexAndTransform


## SourceFiles
globalMeshData.C
globalMeshDataTemplates.C

