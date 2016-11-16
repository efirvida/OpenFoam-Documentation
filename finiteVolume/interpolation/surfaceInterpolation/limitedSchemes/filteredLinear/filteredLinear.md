# filteredLinear 
## Class
Foam::filteredLinearLimiter

## Description
Class to generate weighting factors for the filteredLinear
differencing scheme.

The aim is to remove high-frequency modes with "staggering"
characteristics by comparing the face gradient relative to the
background distribution represented by the neighbouring cell gradients
with those gradients and introduce small amounts of upwind in order to
damp these modes.

Used in conjunction with the template class LimitedScheme.

## SourceFiles
filteredLinear.C

