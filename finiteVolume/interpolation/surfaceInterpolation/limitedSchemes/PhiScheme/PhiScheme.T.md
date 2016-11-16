# PhiScheme.T 
## Class
Foam::PhiScheme

## Description
Class to create the weighting-factors based on the face-flux.

The particular differencing scheme class is supplied as a template
argument, the weight function of which is called by the weight function
of this class for the internal faces as well as faces of coupled
patches (e.g. processor-processor patches). The weight function is
supplied with the central-differencing weighting factor, the face-flux,
the face neighbour cell values and the face area.

This code organisation is both neat and efficient, allowing for
convenient implementation of new schemes to run on parallelised cases.

## SourceFiles
PhiScheme.C

