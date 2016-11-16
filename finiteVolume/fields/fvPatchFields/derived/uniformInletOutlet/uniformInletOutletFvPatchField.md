# uniformInletOutletFvPatchField 
## Class
Foam::uniformInletOutletFvPatchField

## Group
grpOutletBoundaryConditions

## Description
Variant of inletOutlet boundary condition with uniform inletValue.

## Usage

        Property     | Description             | Required    | Default value
        phi          | flux field name         | no          | phi
        uniformInletValue   | inlet value for reverse flow | yes    |


Example of the boundary condition specification:
```
<patchName>
{
        type                uniformInletOutlet;
        phi                 phi;
        uniformInletValue   0;
        value               uniform 0;
}
```

The mode of operation is determined by the sign of the flux across the
patch faces.

## Note
Sign conventions:
- positive flux (out of domain): apply zero-gradient condition
- negative flux (into of domain): apply the user-specified fixed value

## See also
Foam::inletOutletFvPatchField
Foam::Function1Types

## SourceFiles
uniformInletOutletFvPatchField.C

