# HarrisCrighton 
## Class
Foam::ParticleStressModels::HarrisCrighton

## Description
Inter-particle stress model of Harris and Crighton

The stress value takes the following form:
\f[
        \frac{P_s \alpha^\beta}{ \mathrm{max} \left( \alpha_{pack} - \alpha ,
        \epsilon ( 1 - \alpha ) \right) }
\f]
Here, \f$\alpha\f$ is the volume fraction of the dispersed phase, and the
other values are modelling constants. A small value \f$\epsilon\f$ is used
to limit the denominator to ensure numerical stability.

Reference:
```
        "Solitons, solitary waves, and voidage disturbances in gas-fluidized
        beds"
        S Harris and D Crighton,
        Journal of Fluid Mechanics
        Volume 266, Pages 243-276, 1994
```

## SourceFiles
HarrisCrighton.C

