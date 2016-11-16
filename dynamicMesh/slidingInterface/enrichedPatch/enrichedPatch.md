# enrichedPatch 
## Class
Foam::enrichedPatch

## Description
The enriched patch contains a double set of faces from the two
sides of the sliding interface before the cutting.

The patch basically consists of two over-lapping sets of faces sitting
on a common point support, where every edge may be shared by more than
2 faces.  The patch points are collected in a map.  Additional
information needed for cutting is the point insertion into every edge
of master and slave.

Note:
If new points are created during master-slave edge cutting, they
should be registred with the pointMap.


## SourceFiles
enrichedPatch.C
enrichedPatchCutFaces.C
enrichedPatchFaces.C
enrichedPatchPointMap.C
enrichedPatchPointMergeMap.C
enrichedPatchPointPoints.C

