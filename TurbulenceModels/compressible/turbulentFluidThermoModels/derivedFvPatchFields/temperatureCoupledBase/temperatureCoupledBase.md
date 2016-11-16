# temperatureCoupledBase 
## Class
Foam::temperatureCoupledBase

## Description
Common functions used in temperature coupled boundaries.

The thermal conductivity \c kappa may be obtained by the following methods:
      - 'lookup' : lookup volScalarField (or volSymmTensorField) with name
        defined by 'kappa'
      - 'fluidThermo' : use fluidThermo and default
        compressible::turbulenceModel to calculate kappa
      - 'solidThermo' : use solidThermo kappa()
      - 'directionalSolidThermo': uses look up for volSymmTensorField for
        transformed kappa vector. Field name definable in 'alphaAni',
        named 'Anialpha' in solid solver by default

\par Keywords provided by this class:

        Property     | Description                | Required    | Default value
        kappaMethod  | Thermal conductivity method        | yes |
        kappa        | Name of thermal conductivity field | no  | none
        alphaAni     | Name of the non-isotropic alpha    | no  | Anialpha


## Usage
```
nonIsotropicWall
{
        ...
        kappaMethod     directionalSolidThermo;
        kappa           none;
        alphaAni        Anialpha;
        ...
}
```

## SourceFiles
temperatureCoupledBase.C

