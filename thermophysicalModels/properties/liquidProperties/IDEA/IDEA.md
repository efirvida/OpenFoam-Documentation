# IDEA 
## Class
Foam::IDEA

## Description
The IDEA fuel is constructed by adding 30% alphaMethylNaphthalene
with 70% n-decane.

The new properties have been calculated by adding the values in these
proportions and making a least square fit, using the same NSRDS-eq.
so that Y = 0.3*Y_naphthalene + 0.7*Y_decane

The valid Temperature range for n-decane is normally 243.51 - 617.70 K
and for the naphthalene it is 242.67 - 772.04 K
The least square fit was done in the interval 244 - 617 K

The critical temperature was taken to be 618.074 K, since this
is the 'c'-value in the rho-equation, which corresponds to Tcrit,
This value was then used in the fit for the NSRDS6-eq, which uses Tcrit.
(important for the latent heat and surface tension)

The molecular weights are 142.20 and 142.285 and for the IDEA fuel
it is thus 142.26 ( approximately 0.3*142.2 + 0.7*142.285 )

Critical pressure was set to the lowest one (n-Decane)

Critical volume... also the lowest one (naphthalene) 0.523 m^3/kmol

Second Virial Coefficient is n-Decane

## SourceFiles
IDEA.C

