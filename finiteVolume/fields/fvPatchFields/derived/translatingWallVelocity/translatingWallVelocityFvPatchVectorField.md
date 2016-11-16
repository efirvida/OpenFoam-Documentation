# translatingWallVelocityFvPatchVectorField 
## Class
Foam::translatingWallVelocityFvPatchVectorField

## Group
grpWallBoundaryConditions grpGenericBoundaryConditions

## Description
This boundary condition provides a velocity condition for translational
motion on walls.

## Usage

        Property     | Description             | Required    | Default value
        U            | translational velocity  | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            translatingWallVelocity;
        U               (100 0 0);
}
```

The \c U entry is a Function1 of time, see Foam::Function1Types.


## See also
Foam::fixedValueFvPatchField
Foam::Function1Types

## SourceFiles
translatingWallVelocityFvPatchVectorField.C

