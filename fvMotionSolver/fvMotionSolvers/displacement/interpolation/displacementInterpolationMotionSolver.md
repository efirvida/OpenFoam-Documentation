# displacementInterpolationMotionSolver 
## Class
Foam::displacementInterpolationMotionSolver

## Description
Mesh motion solver for an fvMesh.

Scales inbetween motion prescribed on faceZones. Works out per point
the distance between the bounding face zones (in all three directions)
at the start and then every time step
- moves the faceZones based on tables
- interpolates the displacement of all points based on the
      faceZone motion.

Tables are in the \a constant/tables directory.

## SourceFiles
displacementInterpolationMotionSolver.C

