# greyMeanAbsorptionEmission 
## Class
Foam::radiation::greyMeanAbsorptionEmission

## Description
greyMeanAbsorptionEmission radiation absorption and emission coefficients
for continuous phase

The coefficients for the species in the Look up table have to be specified
for use in moles x P [atm], i.e. (k[i] = species[i]*p*9.869231e-6).

The coefficients for CO and soot or any other added are multiplied by the
respective mass fraction being solved

All the species in the dictionary need either to be in the look-up table or
being solved. Conversely, all the species solved do not need to be included
in the calculation of the absorption coefficient

The names of the species in the absorption dictionary must match exactly the
name in the look-up table or the name of the field being solved

The look-up table ("speciesTable") file should be in constant

i.e. dictionary
```
        LookUpTableFileName     "speciesTable";

        EhrrCoeff       0.0;

        CO2
        {
            Tcommon     300.;   // Common Temp
            invTemp     true;   // Is the polynomial using inverse temperature?
            Tlow        300.;   // Low Temp
            Thigh       2500.;  // High Temp

            loTcoeffs           // coeffs for T < Tcommon
            (
                0               //  a0            +
                0               //  a1*T          +
                0               //  a2*T^(+/-)2   +
                0               //  a3*T^(+/-)3   +
                0               //  a4*T^(+/-)4   +
                0               //  a5*T^(+/-)5   +
            );
            hiTcoeffs           // coeffs for T > Tcommon
            (
                18.741
                -121.31e3
                273.5e6
                -194.05e9
                56.31e12
                -5.8169e15
            );
        }
```

## SourceFiles
greyMeanAbsorptionEmission.C

