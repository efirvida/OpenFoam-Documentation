# uniformFixedValuePointPatchField 
## Class
Foam::uniformFixedValuePointPatchField

## Description
Enables the specification of a uniform fixed value boundary condition.

Example of the boundary condition specification:
```
inlet
{
        type            uniformFixedValue;
        uniformValue    constant 0.2;
}
```

The uniformValue entry is a Function1 type, able to describe time
varying functions.  The example above gives the usage for supplying a
constant value.

## SourceFiles
uniformFixedValuePointPatchField.C

