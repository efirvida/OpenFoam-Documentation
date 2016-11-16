# hPowerThermo 
## Class
Foam::hPowerThermo

## Description
Power-function based thermodynamics package templated on EquationOfState.

In this thermodynamics package the heat capacity is a simple power of
temperature:

        Cp(T) = c0*(T/Tref)^n0;

which is particularly suitable for solids.

## SourceFiles
hPowerThermoI.H
hPowerThermo.C

