# meanVelocityForce 
## Class
Foam::fv::meanVelocityForce

## Description
Calculates and applies the force necessary to maintain the specified mean
velocity.

Note: Currently only handles kinematic pressure (incompressible solvers).

## Usage
Example usage:
```
meanVelocityForceCoeffs
{
        selectionMode   all;                    // Apply force to all cells
        fieldNames      (U);                    // Name of velocity field
        Ubar            (10.0 0 0);             // Desired mean velocity
        relaxation      0.2;                    // Optional relaxation factor
}
```

## SourceFiles
meanVelocityForce.C

