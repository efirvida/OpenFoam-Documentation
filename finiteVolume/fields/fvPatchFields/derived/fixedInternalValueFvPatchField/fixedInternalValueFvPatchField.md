# fixedInternalValueFvPatchField 
## Class
Foam::fixedInternalValueFvPatchField

## Group
grpGenericBoundaryConditions

## Description
This boundary condition provides a mechanism to set boundary (cell) values
directly into a matrix, i.e. to set a constraint condition.  Default
behaviour is to act as a zero gradient condition.

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            fixedInternalValue;
        value           uniform 0;              // place holder
}
```

## Note
This is used as a base for conditions such as the turbulence \c epsilon
wall function, which applies a near-wall constraint for high Reynolds
number flows.

## See also
Foam::epsilonWallFunctionFvPatchScalarField

## SourceFiles
fixedInternalValueFvPatchField.C

