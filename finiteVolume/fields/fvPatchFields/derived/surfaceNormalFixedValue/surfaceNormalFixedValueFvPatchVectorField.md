# surfaceNormalFixedValueFvPatchVectorField 
## Class
Foam::surfaceNormalFixedValueFvPatchVectorField

## Group
grpGenericBoundaryConditions grpInletBoundaryConditions

## Description
This boundary condition provides a surface-normal vector boundary condition
by its magnitude.

## Usage

        Property     | Description             | Required    | Default value
        refValue     | reference value         | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            surfaceNormalFixedValue;
        refValue        uniform -10;           // 10 INTO the domain
}
```

## Note
Sign conventions:
- the value is positive for outward-pointing vectors

## See also
Foam::fixedValueFvPatchField

## SourceFiles
surfaceNormalFixedValueFvPatchVectorField.C

