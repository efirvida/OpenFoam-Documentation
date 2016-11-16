# fanFvPatchField 
## Class
Foam::fanFvPatchField

## Group
grpCoupledBoundaryConditions

## Description
This boundary condition provides a jump condition, using the \c cyclic
condition as a base.

The jump is specified as a \c Function1 type, to enable the use of, e.g.
contant, polynomial, table values.

## Usage

        Property     | Description             | Required    | Default value
        patchType    | underlying patch type should be \c cyclic| yes |
        jumpTable    | jump data, e.g. \c csvFile | yes      |
        phi          | flux field name         | no          | phi
        rho          | density field name      | no          | none


Example of the boundary condition specification:
```
<patchName>
{
        type            fan;
        patchType       cyclic;
        jumpTable       csvFile;
        csvFileCoeffs
        {
            hasHeaderLine   1;
            refColumn       0;
            componentColumns 1(1);
            separator       ",";
            fileName        "$FOAM_CASE/constant/pressureVsU";
        }
        value           uniform 0;
}
```

The above example shows the use of a comma separated (CSV) file to specify
the jump condition.

## Note
     The underlying \c patchType should be set to \c cyclic

## See also
Foam::Function1Types

## SourceFiles
fanFvPatchField.C
fanFvPatchFields.H
fanFvPatchFields.C
fanFvPatchFieldsFwd.H

