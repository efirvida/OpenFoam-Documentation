# externalWallHeatFluxTemperatureFvPatchScalarField 
## Class
Foam::externalWallHeatFluxTemperatureFvPatchScalarField

## Group
grpThermoBoundaryConditions grpWallBoundaryConditions

## Description
This boundary condition supplies a heat flux condition for temperature
on an external wall. Optional thin thermal layer resistances can be
specified through thicknessLayers and kappaLayers entries for the
fixed heat transfer coefficient mode.

The condition can operate in two modes:
      - fixed heat transfer coefficient: supply h and Ta
      - fixed heat flux: supply q

where:
\vartable
        h  | heat transfer coefficient [W/m^2/K]
        Ta | ambient temperature [K]
        q  | heat flux [W/m^2]
\endvartable

The thermal conductivity, \c kappa, can either be retrieved from the
mesh database using the \c lookup option, or from a \c solidThermo
thermophysical package.

## Usage

        Property     | Description                 | Required | Default value
        kappa        | thermal conductivity option | yes      |
        q            | heat flux [W/m^2]           | yes*     |
        Ta           | ambient temperature [K]     | yes*     |
        h            | heat transfer coefficient [W/m^2/K] | yes*|
        thicknessLayers | list of thicknesses per layer [m] | yes |
        kappaLayers  | list of thermal conductivites per layer [W/m/K] | yes |
        kappaName    | name of thermal conductivity field | yes  |
        Qr           | name of the radiative field | no | no
        relaxation   | relaxation factor for radiative field | no | 1


Example of the boundary condition specification:
```
<patchName>
{
        type            externalWallHeatFluxTemperature;
        kappa           fluidThermo;
        q               uniform 1000;
        Ta              uniform 300.0;
        h               uniform 10.0;
        thicknessLayers (0.1 0.2 0.3 0.4);
        kappaLayers     (1 2 3 4);
        value           uniform 300.0;
        kappaName       none;
        Qr              none;
        relaxation      1;
}
```

Note:
      - Only supply \c h and \c Ta, or \c q in the dictionary (see above)
      - \c kappa and \c kappaName are inherited from temperatureCoupledBase.

## See also
Foam::temperatureCoupledBase

## SourceFiles
externalWallHeatFluxTemperatureFvPatchScalarField.C

