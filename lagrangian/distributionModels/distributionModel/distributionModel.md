# distributionModel 
## Class
Foam::distributionModel

## Description
A library of runtime-selectable distribution models.

Returns a sampled value given the expectation (nu) and variance (sigma^2)

Current distribution models include:
- exponential
- fixedValue
- general
- multi-normal
- normal
- Rosin-Rammler
- uniform

The distributionModel is tabulated in equidistant nPoints, in an interval.
These values are integrated to obtain the cumulated distribution model,
which is then used to change the distribution from unifrom to
the actual distributionModel.

## SourceFiles
distributionModel.C
distributionModelNew.C

