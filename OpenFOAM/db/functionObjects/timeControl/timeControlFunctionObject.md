# timeControlFunctionObject 
## Class
Foam::functionObjects::timeControl

## Description

## Note
Since the timeIndex is used directly from Foam::Time, it is unaffected
by user-time conversions. For example, Foam::engineTime might cause \a
writeInterval to be degrees crank angle, but the functionObject
execution \a interval would still be in timestep.

## SourceFiles
timeControlFunctionObject.C

