# fixedValueFvPatchField 
## Class
Foam::fixedValueFvPatchField

## Group
grpGenericBoundaryConditions

## Description
This boundary condition supplies a fixed value constraint, and is the base
class for a number of other boundary conditions.

## Usage

        Property     | Description             | Required    | Default value
        value        | Patch face values       | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            fixedValue;
        value           uniform 0;  // Example for scalar field usage
}
```

## SourceFiles
fixedValueFvPatchField.C

