# alphatWallFunctionFvPatchScalarField 
## Class
Foam::compressible::alphatWallFunctionFvPatchScalarField

## Group
grpCmpWallFunctions

## Description
This boundary condition provides a turbulent thermal diffusivity conditon
when using wall functions
- replicates OpenFOAM v1.5 (and earlier) behaviour

The turbulent thermal diffusivity calculated using:

        \f[
            \alpha_t = \frac{\mu_t}{Pr_t}
        \f]

where

\vartable
        \alpha_t| turblence thermal diffusivity
        \mu_t   | turblence viscosity
        Pr_t    | turblent Prandtl number
\endvartable

## Usage

        Property     | Description             | Required    | Default value
        nut          | turbulence viscosity field name | no  | nut
        Prt          | turbulent Prandtl number | no          | 0.85


Example of the boundary condition specification:
```
<patchName>
{
        type            alphatWallFunction;
        nut             nut;
        Prt             0.85;
        value           uniform 0; // optional value entry
}
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
alphatWallFunctionFvPatchScalarField.C

