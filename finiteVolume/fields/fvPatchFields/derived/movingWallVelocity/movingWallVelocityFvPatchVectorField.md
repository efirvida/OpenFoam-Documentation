# movingWallVelocityFvPatchVectorField 
## Class
Foam::movingWallVelocityFvPatchVectorField

## Group
grpWallBoundaryConditions

## Description
This boundary condition provides a velocity condition for cases with
moving walls.  In addition, it should also be applied to 'moving' walls
for moving reference frame (MRF) calculations.

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            movingWallVelocity;
        value           uniform (0 0 0);    // Initial value
}
```

## See also
Foam::fixedValueFvPatchVectorField
Foam::MRFZone

## SourceFiles
movingWallVelocityFvPatchVectorField.C

