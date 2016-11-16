# RaviPetersen 
## Class
Foam::laminarFlameSpeedModels::RaviPetersen

## Description
Laminar flame speed obtained from Ravi and Petersen's correlation.

The correlation for the laminar flame speed \f$Su\f$ is of the following
form:
\f[
        Su = \left( \sum \alpha_i \phi^i \right)
        \left( \frac{T}{T_{ref}} \right)^{\left( \sum \beta_j \phi^j \right)}
\f]

Where \f$\phi\f$ is the equivalence ratio, and \f$\alpha\f$ and \f$\beta\f$
are polynomial coefficients given for a number of pressure and equivalence
ratio points.

## SourceFiles
RaviPetersen.C

