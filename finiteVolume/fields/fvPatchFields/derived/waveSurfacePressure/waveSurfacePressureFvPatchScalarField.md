# waveSurfacePressureFvPatchScalarField 
## Class
Foam::waveSurfacePressureFvPatchScalarField

## Group
grpInletBoundaryConditions

## Description
This is a pressure boundary condition, whose value is calculated as
the hydrostatic pressure based on a given displacement:

        \f[
            p = -\rho*g*\zeta
        \f]

\vartable
        \rho  | density [kg/m3]
        g     | acceleration due to gravity [m/s2]
        \zeta | wave amplitude [m]
\endvartable

The wave amplitude is updated as part of the calculation, derived from the
local volumetric flux.

## Usage

        Property     | Description             | Required    | Default value
        phi          | flux field name         | no          | phi
        rho          | density field name      | no          | rho
        zeta         | wave amplitude field name | no        | zeta


Example of the boundary condition specification:
```
<patchName>
{
        type            waveSurfacePressure;
        phi             phi;
        rho             rho;
        zeta            zeta;
        value           uniform 0;  // place holder
}
```

The density field is only required if the flux is mass-based as opposed to
volumetric-based.

## See also
Foam::fixedValueFvPatchField

## SourceFiles
waveSurfacePressureFvPatchScalarField.C

