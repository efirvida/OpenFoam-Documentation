# absolute 
## Class
Foam::CorrectionLimitingMethods::absolute

## Description
Correction limiting method based on the absolute particle velocity.

This method that limits the velocity correction to that of a rebound with a
coefficient of restitution \f$e\f$. The absolute velocity of the particle
is used when calculating the magnitude of the limited correction.
The direction is calculated using the relative velocity.

## SourceFiles
absolute.C

