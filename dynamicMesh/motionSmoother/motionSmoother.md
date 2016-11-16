# motionSmoother 
## Class
Foam::motionSmoother

## Description
Given a displacement moves the mesh by scaling the displacement back
until there are no more mesh errors.

Holds displacement field (read upon construction since need boundary
conditions) and scaling factor and optional patch number on which to
scale back displacement.

E.g.
```
        // Construct iterative mesh mover.
        motionSmoother meshMover(mesh, labelList(1, patchi));

        // Set desired displacement:
        meshMover.displacement() = ..

        for (label iter = 0; iter < maxIter; iter++)
        {
            if (meshMover.scaleMesh(true))
            {
                Info<< "Successfully moved mesh" << endl;
                return true;
            }
        }
```

## Note
- Shared points (parallel): a processor can have points which are part of
pp on another processor but have no pp itself (i.e. it has points
and/or edges but no faces of pp). Hence we have to be careful when e.g.
synchronising displacements that the value from the processor which has
faces of pp get priority. This is currently handled in setDisplacement
by resetting the internal displacement to zero before doing anything
else. The combine operator used will give preference to non-zero
values.

- Various routines take baffles. These are sets of boundary faces that
are treated as a single internal face. This is a hack used to apply
movement to internal faces.

- Mesh constraints are looked up from the supplied dictionary. (uses
recursive lookup)

## SourceFiles
motionSmoother.C

