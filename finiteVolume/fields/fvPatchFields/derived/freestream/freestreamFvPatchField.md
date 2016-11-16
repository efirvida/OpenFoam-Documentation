# freestreamFvPatchField 
## Class
Foam::freestreamFvPatchField

## Group
grpInletBoundaryConditions grpOutletBoundaryConditions

## Description
This boundary condition provides a free-stream condition.  It is a 'mixed'
condition derived from the \c inletOutlet condition, whereby the mode of
operation switches between fixed (free stream) value and zero gradient
based on the sign of the flux.

## Usage

        Property     | Description             | Required    | Default value
        freestreamValue   | freestream velocity          | yes         |
        phi          | flux field name         | no          | phi


Example of the boundary condition specification:
```
<patchName>
{
        type            freestream;
        phi             phi;
}
```

## See also
Foam::mixedFvPatchField
Foam::inletOutletFvPatchField

## SourceFiles
freestreamFvPatchField.C

