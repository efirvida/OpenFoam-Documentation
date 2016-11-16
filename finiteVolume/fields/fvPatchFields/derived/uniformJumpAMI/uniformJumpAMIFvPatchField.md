# uniformJumpAMIFvPatchField 
## Class
Foam::uniformJumpAMIFvPatchField

## Group
grpCoupledBoundaryConditions

## Description
This boundary condition provides a jump condition, using the \c cyclicAMI
condition as a base.  The jump is specified as a time-varying uniform
value across the patch.

## Usage

        Property     | Description             | Required    | Default value
        patchType    | underlying patch type should be \c cyclicAMI| yes |
        jumpTable    | jump value              | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            uniformJumpAMI;
        patchType       cyclicAMI;
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
Foam::jumpCyclicAMIFvPatchField
Foam::Function1Types

## SourceFiles
uniformJumpAMIFvPatchField.C

