# convectiveHeatTransferFvPatchScalarField 
## Class
Foam::compressible::convectiveHeatTransferFvPatchScalarField

## Group
grpCmpBoundaryConditions

## Description
This boundary condition provides a convective heat transfer coefficient
condition

if Re > 500000
\f[
        htc_p = \frac{0.664 Re^{0.5} Pr^{0.333} \kappa_p}{L}
\f]
else
\f[
        htc_p = \frac{0.037 Re^{0.8} Pr^{0.333} \kappa_p}{L}
\f]

where

\vartable
        htc_p   | patch convective heat transfer coefficient
        Re      | Reynolds number
        Pr      | Prandtl number
        \kappa_p | thermal conductivity
        L       | length scale
\endvartable

## Usage

        Property     | Description             | Required    | Default value
        L            | Length scale [m]        | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            convectiveHeatTransfer;
        L               0.1;
}
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
convectiveHeatTransferFvPatchScalarField.C

