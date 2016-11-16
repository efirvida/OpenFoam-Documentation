# FitData.T 
## Class
Foam::FitData

## Description
Data for the upwinded and centred polynomial fit interpolation schemes.
The linearCorrection_ determines whether the fit is for a corrected
linear scheme (first two coefficients are corrections for owner and
neighbour) or a pure upwind scheme (first coefficient is correction for
owner; weight on face taken as 1).

## SourceFiles
FitData.C

