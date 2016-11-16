# uniformFixedGradientFvPatchField 
## Class
Foam::uniformFixedGradientFvPatchField

## Group
grpGenericBoundaryConditions

## Description
This boundary condition provides a uniform fixed gradient condition.

## Usage

        Property     | Description             | Required    | Default value
        uniformGradient | uniform gradient     | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            uniformFixedGradient;
        uniformGradient constant 0.2;
}
```

## Note
The uniformGradient entry is a Function1 type, able to describe time
varying functions.  The example above gives the usage for supplying a
constant value.

## See also
Foam::Function1Types
Foam::fixedGradientFvPatchField

## SourceFiles
uniformFixedGradientFvPatchField.C

