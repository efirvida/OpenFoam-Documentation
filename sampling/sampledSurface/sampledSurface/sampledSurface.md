# sampledSurface 
## Class
Foam::sampledSurface

## Group
grpUtilitiesFunctionObjects

## Description
An abstract class for surfaces with sampling.

The constructors for the derived classes should generally start in a
'expired' condition (ie, needsUpdate() == true) and rely on a
subsequent call to the update() method to complete the initialization.
Delaying the final construction as late as possible allows the
construction of surfaces that may depend on intermediate calculation
results (eg, iso-surfaces) and also avoids the unnecessary
reconstruction of surfaces between sampling intervals.

It is the responsibility of the caller to ensure that the surface
update() is called before the surface is used.  The update() method
implementation should do nothing when the surface is already
up-to-date.

## SourceFiles
sampledSurface.C
sampledSurfaceTemplates.C

