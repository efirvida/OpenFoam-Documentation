# greyMeanSolidAbsorptionEmission 
## Class
Foam::radiation::greyMeanSolidAbsorptionEmission

## Description
greyMeanSolidAbsorptionEmission radiation absorption and emission
coefficients for continuous phase

The coefficients for the species in the Look up table have to be specified
for use in moles x P [atm], i.e. (k[i] = species[i]*p*9.869231e-6).

The coefficients for CO and soot or any other added are multiplied by the
respective mass fraction being solved

All the species in the dictionary need either to be in the look-up table or
being solved. Conversely, all the species solved do not need to be included
in the calculation of the absorption coefficient

The names of the species in the absorption dictionary must match exactly the
name in the look-up table or the name of the field being solved

## SourceFiles
greyMeanSolidAbsorptionEmission.C

