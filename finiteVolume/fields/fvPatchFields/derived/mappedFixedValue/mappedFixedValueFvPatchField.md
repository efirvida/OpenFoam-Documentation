# mappedFixedValueFvPatchField 
## Class
Foam::mappedFixedValueFvPatchField

## Group
grpGenericBoundaryConditions grpCoupledBoundaryConditions

## Description
This boundary condition maps the value at a set of cells or patch faces
back to *this.

The sample mode is set by the underlying mapping engine, provided by the
mappedPatchBase class.

## Usage

        Property     | Description             | Required    | Default value
        fieldName    | name of field to be mapped | no       | this field name
        setAverage   | flag to activate setting of average value | yes |
        average      | average value to apply if \c setAverage = yes | yes |
        interpolationScheme | type of interpolation scheme | no |


Example of the boundary condition specification:
```
<patchName>
{
        type            mapped;
        fieldName       T;
        setAverage      no;
        average         0;
        interpolationScheme cell;
        value           uniform 0;
}
```

When employing the \c nearestCell sample mode, the user must also specify
the interpolation scheme using the \c interpolationScheme entry.

In case of interpolation (where scheme != cell) the limitation is that
there is only one value per cell.  For example, if you have a cell with two
boundary faces and both faces sample into the cell, both faces will get the
same value.

## Note
It is not possible to sample internal faces since volume fields are not
defined on faces.

## See also
Foam::mappedPatchBase
Foam::interpolation
Foam::fixedValueFvPatchField

## SourceFiles
mappedFixedValueFvPatchField.C

