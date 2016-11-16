# mappedFieldFvPatchField 
## Class
Foam::mappedFieldFvPatchField

## Group
grpGenericBoundaryConditions grpCoupledBoundaryConditions

## Description
This boundary condition provides a self-contained version of the \c mapped
condition.  It does not use information on the patch; instead it holds
thr data locally.

## Usage

        Property     | Description             | Required    | Default value
        fieldName    | name of field to be mapped | no       | this field name
        setAverage   | flag to activate setting of average value | yes |
        average      | average value to apply if \c setAverage = yes | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            mappedField;
        fieldName       T;              // optional field name
        setAverage      no;             // apply an average value
        average         0;              // average to apply if setAverage
        value           uniform 0;      // place holder
}
```

## Note
Since this condition can be applied on a per-field and per-patch basis,
it is possible to duplicate the mapping information.  If possible, employ
the \c mapped condition in preference to avoid this situation, and only
employ this condition if it is not possible to change the underlying
geometric (poly) patch type to \c mapped.

## See also
Foam::mappedPatchBase
Foam::mappedPolyPatch
Foam::mappedFvPatch
Foam::fixedValueFvPatchField

## SourceFiles
mappedFieldFvPatchField.C

