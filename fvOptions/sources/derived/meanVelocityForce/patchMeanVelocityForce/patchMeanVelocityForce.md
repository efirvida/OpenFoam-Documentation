# patchMeanVelocityForce 
## Class
Foam::fv::patchMeanVelocityForce

## Description
Calculates and applies the force necessary to maintain the specified mean
velocity averaged over the specified patch.

Note: Currently only handles kinematic pressure (incompressible solvers).

## Usage
Example usage:
```
patchMeanVelocityForceCoeffs
{
        selectionMode   all;                    // Apply force to all cells
        fieldNames      (U);                    // Name of velocity field
        patch           inlet;                  // Name of the patch
        Ubar            (10.0 0 0);             // Desired mean velocity
        relaxation      0.2;                    // Optional relaxation factor
}
```

## SourceFiles
patchMeanVelocityForce.C

