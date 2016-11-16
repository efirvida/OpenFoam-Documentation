# uniformJumpFvPatchField 
## Class
Foam::uniformJumpFvPatchField

## Group
grpCoupledBoundaryConditions

## Description
This boundary condition provides a jump condition, using the \c cyclic
condition as a base.  The jump is specified as a time-varying uniform
value across the patch.

## Usage

        Property     | Description             | Required    | Default value
        patchType    | underlying patch type should be \c cyclic| yes |
        jumpTable    | jump value              | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            uniformJump;
        patchType       cyclic;
        jumpTable       constant 10;
}
```

The above example shows the use of a fixed jump of '10'.

## Note
The uniformValue entry is a Function1 type, able to describe time
varying functions.  The example above gives the usage for supplying a
constant value.

The underlying \c patchType should be set to \c cyclic

## See also
Foam::fixedJumpFvPatchField
Foam::Function1Types

## SourceFiles
uniformJumpFvPatchField.C

