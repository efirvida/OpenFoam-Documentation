# plenumPressureFvPatchScalarField 
## Class
Foam::plenumPressureFvPatchScalarField

## Group
grpInletBoundaryConditions

## Description
This boundary condition provides a plenum pressure inlet condition. This
condition creates a zero-dimensional model of an enclosed volume of gas
upstream of the inlet. The pressure that the boundary condition exerts on
the inlet boundary is dependent on the thermodynamic state of the upstream
volume. The upstream plenum density and temperature are time-stepped along
with the rest of the simulation, and momentum is neglected. The plenum is
supplied with a user specified mass flow and temperature.

The result is a boundary condition which blends between a pressure inlet
condition condition and a fixed mass flow. The smaller the plenum
volume, the quicker the pressure responds to a deviation from the supply
mass flow, and the closer the model approximates a fixed mass flow. As
the plenum size increases, the model becomes more similar to a specified
pressure.

The expansion from the plenum to the inlet boundary is controlled by an
area ratio and a discharge coefficient. The area ratio can be used to
represent further acceleration between a sub-grid blockage such as fins.
The discharge coefficient represents a fractional deviation from an
ideal expansion process.

This condition is useful for simulating unsteady internal flow problems
for which both a mass flow boundary is unrealistic, and a pressure
boundary is susceptible to flow reversal. It was developed for use in
simulating confined combustion.

Reference:
```
        Bainbridge, W. (2013).
        The Numerical Simulation of Oscillations in Gas Turbine Combustion
        Chambers,
        PhD Thesis,
        Chapter 4, Section 4.3.1.2, 77-80.
```

## Usage

        Property        | Description                 | Required | Default value
        gamma           | ratio of specific heats     | yes      | none
        R               | specific gas constant       | yes      | none
        supplyMassFlowRate | flow rate into the plenum | yes     | none
        supplyTotalTemperature | temperature into the plenum | yes | none
        plenumVolume    | plenum volume               | yes      | none
        plenumDensity   | plenum density              | yes      | none
        plenumTemperature | plenum temperature        | yes      | none
        U               | velocity field name         | no       | U
        phi             | flux field name             | no       | phi
        rho             | inlet density               | no       | none
        inletAreaRatio  | inlet open fraction         | yes      | none
        inletDischargeCoefficient | inlet loss coefficient | yes | none
        timeScale       | relaxation time scale       | yes      | none


Example of the boundary condition specification:
```
<patchName>
{
        type            plenumPressure;
        gamma           1.4;
        R               287.04;
        supplyMassFlowRate 0.0001;
        supplyTotalTemperature 300;
        plenumVolume    0.000125;
        plenumDensity   1.1613;
        plenumTemperature 300;
        inletAreaRatio  1.0;
        inletDischargeCoefficient 0.8;
        timeScale       1e-4;
        value           uniform 1e5;
}
```

## SourceFiles
plenumPressureFvPatchScalarField.C

