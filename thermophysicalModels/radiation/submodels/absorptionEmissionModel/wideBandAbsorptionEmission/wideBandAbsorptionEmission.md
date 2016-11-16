# wideBandAbsorptionEmission 
## Class
Foam::radiation::wideBandAbsorptionEmission

## Description

wideBandAbsorptionEmission radiation absorption and emission coefficients
for continuous phase.

All the bands should have the same number of species and have to be entered
in the same order.

There is no check of continuity of the bands. They should not ovelap or
have gaps.

The emission constant proportionality is specified per band (EhrrCoeff).

The coefficients for the species in the lookup table have to be specified
for use in moles x P [atm].i.e. (k[i] = species[i]*p*9.869231e-6).

The coefficients for CO and soot or any other added are multiplied by the
respective mass fraction being solved.

The look Up table file should be in the constant directory.

band dictionary:
```
        band0
        {
            bandLimits (1.0e-6 2.63e-6);
            EhrrCoeff       0.0;
            species
            {
                CH4
                {
                    Tcommon         300.;
                    Tlow            300.;
                    Thigh           2500.;
                    invTemp         false;
                    loTcoeffs (0 0 0 0 0 0) ;
                    hiTcoeffs (.1 0 0 0 0 0);
                }
                CO2
                {
                    Tcommon         300.;
                    Tlow            300.;
                    Thigh           2500.;
                    invTemp         false;
                    loTcoeffs (0 0 0 0 0 0) ;
                    hiTcoeffs (.1 0 0 0 0 0);
                }
                H2O
                {
                    Tcommon         300.;
                    Tlow            300.;
                    Thigh           2500.;
                    invTemp         false;
                    loTcoeffs (0 0 0 0 0 0) ;
                    hiTcoeffs (.1 0 0 0 0 0);
                }
                Ysoot
                {
                    Tcommon         300.;
                    Tlow            300.;
                    Thigh           2500.;
                    invTemp         false;
                    loTcoeffs (0 0 0 0 0 0) ;
                    hiTcoeffs (.1 0 0 0 0 0);
                }
            }
        }
```


## SourceFiles
wideBandAbsorptionEmission.C

