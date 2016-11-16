# fixedPressureCompressibleDensityFvPatchScalarField 
## Class
Foam::fixedPressureCompressibleDensityFvPatchScalarField

## Group
grpInletBoundaryConditions

## Description
This boundary condition calculates a (liquid) compressible density as a
function of pressure and fluid properties:

        \f[
            \rho = \rho_{l,sat} + \psi_l*(p - p_{sat})
        \f]

where

\vartable
        \rho    | density [kg/m3]
        \rho_{l,sat} | saturation liquid density [kg/m3]
        \psi_l  | liquid compressibility
        p       | pressure [Pa]
        p_{sat} | saturation pressure [Pa]
\endvartable

The variables \c rholSat, \c pSat and \c psil are retrieved from the
\c thermodynamicProperties dictionary.

## Usage

        Property     | Description             | Required    | Default value
        p            | pressure field name     | no          | p


Example of the boundary condition specification:
```
<patchName>
{
        type        fixedPressureCompressibleDensity;
        p           p;
        value       uniform 1;
}
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
fixedPressureCompressibleDensityFvPatchScalarField.C

