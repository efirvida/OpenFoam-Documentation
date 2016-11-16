# mappedFixedInternalValueFvPatchField 
## Class
Foam::mappedFixedInternalValueFvPatchField

## Group
grpGenericBoundaryConditions grpCoupledBoundaryConditions

## Description
This boundary condition maps the boundary and internal values of a
neighbour patch field to the boundary and internal values of *this.

## Usage

        Property     | Description             | Required    | Default value
        fieldName    | name of field to be mapped | no       | this field name
        setAverage   | flag to activate setting of average value | yes |
        average      | average value to apply if \c setAverage = yes | yes |


```
<patchName>
{
        type            mappedFixedInternalValue;
        fieldName       T;
        setAverage      no;
        average         0;
        value           uniform 0;
}
```

## Note
This boundary condition can only be applied to patches that are of
the \c mappedPolyPatch type.

## See also
Foam::mappedPatchBase
Foam::mappedPolyPatch
Foam::mappedFvPatch
Foam::mappedFixedValueFvPatchField

## SourceFiles
mappedFixedInternalValueFvPatchField.C

