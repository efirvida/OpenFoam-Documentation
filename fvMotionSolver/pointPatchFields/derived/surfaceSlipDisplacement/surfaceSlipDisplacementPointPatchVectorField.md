# surfaceSlipDisplacementPointPatchVectorField 
## Class
Foam::surfaceSlipDisplacementPointPatchVectorField

## Description
Displacement follows a triSurface. Use in a displacementMotionSolver
as a bc on the pointDisplacement field.
Following is done by calculating the projection onto the surface according
to the projectMode
- NEAREST : nearest
- POINTNORMAL : intersection with point normal
- FIXEDNORMAL : intersection with fixed vector

Optionally (intersection only) removes a component ("wedgePlane") to
stay in 2D.

Needs:
- geometry : dictionary with searchableSurfaces. (usually
      triSurfaceMeshes in constant/triSurface)
- projectMode : see above
- projectDirection : if projectMode = fixedNormal
- wedgePlane : -1 or component to knock out of intersection normal
- frozenPointsZone : empty or name of pointZone containing points
                         that do not move

## SourceFiles
surfaceSlipDisplacementPointPatchVectorField.C

