# CrankNicolson 
## Class
Foam::sixDoFSolvers::CrankNicolson

## Description
Crank-Nicolson 2nd-order time-integrator for 6DoF solid-body motion.

The off-centering coefficients for acceleration (velocity integration) and
velocity (position/orientation integration) may be specified but default
values of 0.5 for each are used if they are not specified.  With the default
off-centering this scheme is equivalent to the Newmark scheme with default
coefficients.

Example specification in dynamicMeshDict:
```
solver
{
        type    CrankNicolson;
        aoc     0.5;    // Acceleration off-centering coefficient
        voc     0.5;    // Velocity off-centering coefficient
}
```

## See also
Foam::sixDoFSolvers::Newmark

## SourceFiles
CrankNicolson.C

