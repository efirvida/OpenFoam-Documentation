# rotatingWallVelocityFvPatchVectorField 
## Class
Foam::rotatingWallVelocityFvPatchVectorField

## Group
grpWallBoundaryConditions grpGenericBoundaryConditions

## Description
This boundary condition provides a rotational velocity condition.

## Usage

        Property     | Description             | Required    | Default value
        origin       | origin of rotation in Cartesian co-ordinates | yes|
        axis         | axis of rotation        | yes         |
        omega        | angular velocty of the frame [rad/s] | yes    |


Example of the boundary condition specification:
```
<patchName>
{
        type            rotatingWallVelocity;
        origin          (0 0 0);
        axis            (0 0 1);
        omega           100;
}
```

The \c omega entry is a Function1 of time, see Foam::Function1Types.

## See also
Foam::fixedValueFvPatchField
Foam::Function1Types

## SourceFiles
rotatingWallVelocityFvPatchVectorField.C

