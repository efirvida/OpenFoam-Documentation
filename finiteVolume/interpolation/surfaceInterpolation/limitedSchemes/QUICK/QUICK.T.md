# QUICK.T 
## Class
Foam::QUICKLimiter

## Description
Class with limiter function which returns the limiter for the
quadratic-upwind differencing scheme.

Note that the weighting factors are not bounded between upwind and
central-differencing, some downwind contribution is possible although
the interpolate is limited to be between the upwind and downwind cell
values.

Used in conjunction with the template class LimitedScheme.

## SourceFiles
QUICK.C

