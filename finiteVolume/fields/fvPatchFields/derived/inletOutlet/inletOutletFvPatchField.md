# inletOutletFvPatchField 
## Class
Foam::inletOutletFvPatchField

## Group
grpOutletBoundaryConditions

## Description
This boundary condition provides a generic outflow condition, with
specified inflow for the case of return flow.

## Usage

        Property     | Description             | Required    | Default value
        phi          | Flux field name         | no          | phi
        inletValue   | Inlet value for reverse flow | yes    |


Example of the boundary condition specification:
```
<patchName>
{
        type            inletOutlet;
        phi             phi;
        inletValue      uniform 0;
        value           uniform 0;
}
```

The mode of operation is determined by the sign of the flux across the
patch faces.

## Note
Sign conventions:
- Positive flux (out of domain): apply zero-gradient condition
- Negative flux (into of domain): apply the "inletValue" fixed-value

## See also
Foam::mixedFvPatchField
Foam::zeroGradientFvPatchField
Foam::outletInletFvPatchField

## SourceFiles
inletOutletFvPatchField.C

