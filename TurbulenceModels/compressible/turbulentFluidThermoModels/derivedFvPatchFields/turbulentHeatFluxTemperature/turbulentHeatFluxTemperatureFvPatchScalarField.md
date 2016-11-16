# turbulentHeatFluxTemperatureFvPatchScalarField 
## Class
Foam::compressible::turbulentHeatFluxTemperatureFvPatchScalarField

## Description
Fixed heat boundary condition to specify temperature gradient. Input
heat source either specified in terms of an absolute power [W], or as a
flux [W/m^2].

## Usage

        Property     | Description             | Required    | Default value
        heatSource   | 'power' [W] or 'flux' [W/m^2] | yes |
        q            | heat power or flux field      | yes |
        kappa        | inherited from temperatureCoupledBase | yes |
        kappaName    | inherited from temperatureCoupledBase | yes |
        Qr           | name of the radiative flux field | yes |
        value        | initial temperature value | no | calculated
        gradient     | initial gradient value | no | 0.0


Note: If needed, both 'value' and 'gradient' must be defined to be used.

Example usage:
```
hotWall
{
        type            compressible::turbulentHeatFluxTemperature;
        heatSource      flux;
        q               uniform 10;
        kappa           fluidThermo;
        kappaName       none;
        Qr              none;
}
```


## See also
Foam::temperatureCoupledBase

## SourceFiles
turbulentHeatFluxTemperatureFvPatchScalarField.C

