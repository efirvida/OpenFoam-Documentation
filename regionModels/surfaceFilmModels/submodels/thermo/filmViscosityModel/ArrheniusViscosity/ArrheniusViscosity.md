# ArrheniusViscosity 
## Class
Foam::ArrheniusViscosity

## Description
The Arrhenius temperature-dependent viscosity model multiplies the viscosity
of a base model by an Arrhenius-type temperature function:

        mu = mu0*exp(k1*(1/(T + k2) - 1/(Tref + k2)))

Where:
        mu0 is the base-model viscosity
        k1 and k2 are Arrhenius coefficients
        T is the local temperature
        Tref is the reference temperature

## SourceFiles
ArrheniusViscosity.C

