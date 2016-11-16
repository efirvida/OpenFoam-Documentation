# displacementLayeredMotionMotionSolver 
## Class
Foam::displacementLayeredMotionMotionSolver

## Description
Mesh motion solver for an (multi-block) extruded fvMesh. Gets given the
structure of the mesh blocks and boundary conditions on these blocks.

The displacementLayeredMotionCoeffs subdict of dynamicMeshDict specifies
per region (=cellZone) the boundary conditions on two opposing patches
(=faceZones). It then interpolates the boundary values using topological
walking so requires the cellZone to be a layered mesh.

The boundary conditions on faceZones are currently:

follow: the faceZone follows the overall mesh displacement.
            Use this for faceZones on boundary faces (so it uses the
            proper boundary conditions on the pointDisplacement).

uniformFollow: like 'follow' but takes the average value of
            a specified 'patch' (which is not necessarily colocated)

fixedValue: fixed value.

timeVaryingUniformFixedValue: table-driven fixed value.

slip: the second of a pair of faceZones follows the tangential movement
          specified by the first faceZone. (= removes the normal component).

## SourceFiles
displacementLayeredMotionMotionSolver.C

