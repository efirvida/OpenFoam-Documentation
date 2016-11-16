# LUST.T 
## Class
Foam::LUST

## Description
LUST: Linear-upwind stabilised transport.

Interpolation scheme class derived from linearUpwind which returns blended
linear/linear-upwind weighting factors and also applies a explicit
gradient-based correction obtained from the linearUpwind scheme.  The
blending-factor is set to 0.75 linear which optimises the balance between
accuracy and stability on a range of LES cases with a range of mesh quality.

## SourceFiles
LUST.C

