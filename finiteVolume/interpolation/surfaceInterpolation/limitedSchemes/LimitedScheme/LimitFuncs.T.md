# LimitFuncs.T 
## Class
Foam::limitFuncs::LimitFuncs

## Description
Class to create NVD/TVD limited weighting-factors.

The particular differencing scheme class is supplied as a template
argument, the weight function of which is called by the weight function
of this class for the internal faces as well as faces of coupled
patches (e.g. processor-processor patches). The weight function is
supplied the central-differencing weighting factor, the face-flux, the
cell and face gradients (from which the normalised variable
distribution may be created) and the cell centre distance.

This code organisation is both neat and efficient, allowing for
convenient implementation of new schemes to run on parallelised cases.

## SourceFiles
LimitFuncs.C

