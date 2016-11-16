# uniformFixedValueFvPatchField 
## Class
Foam::uniformFixedValueFvPatchField

## Group
grpGenericBoundaryConditions

## Description
This boundary condition provides a uniform fixed value condition.

## Usage

        Property     | Description             | Required    | Default value
        uniformValue | uniform value           |         yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            uniformFixedValue;
        uniformValue    constant 0.2;
}
```

## Note
The uniformValue entry is a Function1 type, able to describe time
varying functions.  The example above gives the usage for supplying a
constant value.

## See also
Foam::Function1Types
Foam::fixedValueFvPatchField

## SourceFiles
uniformFixedValueFvPatchField.C

