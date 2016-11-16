# outletMappedUniformInletFvPatchField 
## Class
Foam::outletMappedUniformInletFvPatchField

## Group
grpInletBoundaryConditions

## Description
This boundary conditon averages the field over the "outlet" patch specified
by name "outletPatchName" and applies this as the uniform value of the
field over this patch.

## Usage

        Property        | Description             | Required    | Default value
        outletPatchName | name of outlet patch    | yes         |
        phi             | flux field name         | no          | phi


Example of the boundary condition specification:
```
<patchName>
{
        type            outletMappedUniformInlet;
        outletPatchName aPatch;
        phi             phi;
        value           uniform 0;
}
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
outletMappedUniformInletFvPatchField.C

