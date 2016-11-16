# Newmark 
## Class
Foam::RBD::rigidBodySolvers::Newmark

## Description
Newmark 2nd-order time-integrator for 6DoF solid-body motion.

Reference:
```
        Newmark, N. M. (1959).
        A method of computation for structural dynamics.
        Journal of the Engineering Mechanics Division, 85(3), 67-94.
```

Example specification in dynamicMeshDict:
```
solver
{
        type    Newmark;
        gamma   0.5;    // Velocity integration coefficient
        beta    0.25;   // Position integration coefficient
}
```

## SourceFiles
Newmark.C

