# fixedGradientFvPatchField 
## Class
Foam::fixedGradientFvPatchField

## Group
grpGenericBoundaryConditions

## Description
This boundary condition supplies a fixed gradient condition, such that
the patch values are calculated using:

        \f[
            x_p = x_c + \frac{\nabla(x)}{\Delta}
        \f]

where
\vartable
        x_p      | patch values
        x_c      | internal field values
        \nabla(x)| gradient (user-specified)
        \Delta   | inverse distance from patch face centre to cell centre
\endvartable

## Usage

        Property     | Description             | Required    | Default value
        gradient     | gradient                | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            fixedGradient;
        gradient        uniform 0;
}
```

## SourceFiles
fixedGradientFvPatchField.C

