# cylindricalInletVelocityFvPatchVectorField 
## Class
Foam::cylindricalInletVelocityFvPatchVectorField

## Group
grpInletBoundaryConditions

## Description
This boundary condition describes an inlet vector boundary condition in
cylindrical co-ordinates given a central axis, central point, rpm, axial
and radial velocity.

## Usage

        Property     | Description             | Required    | Default value
        axis         | axis of rotation        | yes         |
        centre       | centre of rotation      | yes         |
        axialVelocity | axial velocity profile [m/s] | yes    |
        radialVelocity | radial velocity profile [m/s] | yes  |
        rpm          | rotational speed (revolutions per minute) | yes|


Example of the boundary condition specification:
```
<patchName>
{
        type            cylindricalInletVelocity;
        axis            (0 0 1);
        centre          (0 0 0);
        axialVelocity   constant 30;
        radialVelocity  constant -10;
        rpm             constant 100;
}
```

## Note
The \c axialVelocity, \c radialVelocity and \c rpm entries are Function1
types, able to describe time varying functions.  The example above gives
the usage for supplying constant values.

## See also
Foam::fixedValueFvPatchField
Foam::Function1Types

## SourceFiles
cylindricalInletVelocityFvPatchVectorField.C

