# outletInletFvPatchField 
## Class
Foam::outletInletFvPatchField

## Group
grpInletBoundaryConditions

## Description
This boundary condition provides a generic inflow condition, with
specified outflow for the case of reverse flow.

## Usage

        Property     | Description             | Required    | Default value
        phi          | Flux field name         | no          | phi
        outletValue  | Outlet value for reverse flow | yes   |


Example of the boundary condition specification:
```
<patchName>
{
        type            outletInlet;
        phi             phi;
        outletValue     uniform 0;
        value           uniform 0;
}
```

The mode of operation is determined by the sign of the flux across the
patch faces.

## Note
Sign conventions:
- Positive flux (out of domain): apply the "outletValue" fixed-value
- Negative flux (into of domain): apply zero-gradient condition

## See also
Foam::mixedFvPatchField
Foam::zeroGradientFvPatchField
Foam::inletOutletFvPatchField

## SourceFiles
outletInletFvPatchField.C

