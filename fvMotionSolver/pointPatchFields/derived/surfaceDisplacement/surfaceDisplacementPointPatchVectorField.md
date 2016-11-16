# surfaceDisplacementPointPatchVectorField 
## Class
Foam::surfaceDisplacementPointPatchVectorField

## Description
Displacement fixed by projection onto triSurface.
Use in a displacementMotionSolver
as a bc on the pointDisplacement field.

Calculates the projection onto the surface according
to the projectMode
- NEAREST : nearest
- POINTNORMAL : intersection with point normal
- FIXEDNORMAL : intersection with fixed vector

This displacement is then clipped with the specified velocity * deltaT.

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
surfaceDisplacementPointPatchVectorField.C

