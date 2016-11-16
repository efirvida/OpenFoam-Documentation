# fixedTemperatureConstraint 
## Class
Foam::fv::fixedTemperatureConstraint

## Description
Fixed temperature equation constraint

## Usage
```
fixedTemperature
{
        type            fixedTemperatureConstraint;
        active          yes;

        fixedTemperatureConstraintCoeffs
        {
            mode            uniform;      // uniform or lookup

            // For uniform option
            temperature     constant 500; // fixed temperature with time [K]

            // For lookup option
            // T            <Tname>;      // optional temperature field name
        }
}
```

## Note:
The 'uniform' option allows the use of a time-varying uniform temperature
by means of the Function1 type.

## SourceFiles
fvOption.C

