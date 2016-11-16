# slidingInterface 
## Class
Foam::slidingInterface

## Description
Sliding interface mesh modifier.  Given two face zones, couple the
master and slave side using a cutting procedure.

The coupled faces are collected into the "coupled" zone and can become
either internal or placed into a master and slave coupled zone.  The
remaining faces (uncovered master or slave) are placed into the master
and slave patch.

The definition of the sliding interface can be either integral or partial.
Integral interface implies that the slave side completely covers
the master (i.e. no faces are uncovered); partial interface
implies that the uncovered part of master/slave face zone should
become boundary faces.

## SourceFiles
slidingInterface.C
coupleSlidingInterface.C
decoupleSlidingInterface.C
slidingInterfaceProjectPoints.C
slidingInterfaceAttachedAddressing.C
slidingInterfaceClearCouple.C

