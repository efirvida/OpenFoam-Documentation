# filteredLinear2V 
## Class
Foam::filteredLinear2VLimiter

## Description
Class to generate weighting factors for the filteredLinear2V
differencing scheme.

The aim is to remove high-frequency modes with "staggering"
characteristics from vector fields by comparing the face gradient in
the direction of maximum gradient with both neighbouring cell gradients
and introduce small amounts of upwind in order to damp these modes.

Used in conjunction with the template class LimitedScheme.

## SourceFiles
filteredLinear2V.C

