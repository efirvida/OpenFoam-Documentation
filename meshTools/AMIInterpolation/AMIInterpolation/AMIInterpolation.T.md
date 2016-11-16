# AMIInterpolation.T 
## Class
Foam::AMIInterpolation

## Description
Interpolation class dealing with transfer of data between two
primitive patches with an arbitrary mesh interface (AMI).

Based on the algorithm given in:

        Conservative interpolation between volume meshes by local Galerkin
        projection, Farrell PE and Maddison JR, 2011, Comput. Methods Appl.
        Mech Engrg, Volume 200, Issues 1-4, pp 89-100

Interpolation requires that the two patches should have opposite
orientations (opposite normals).  The 'reverseTarget' flag can be used to
reverse the orientation of the target patch.


## SourceFiles
AMIInterpolation.C
AMIInterpolationName.C
AMIInterpolationParallelOps.C

