# setTimeStepFunctionObject 
## Class
Foam::functionObjects::setTimeStepFunctionObject

## Group
grpUtilitiesFunctionObjects

## Description
Overrides the timeStep. Can only be used with
solvers with adjustTimeStep control (e.g. pimpleFoam). Makes no attempt
to cooperate with other timeStep 'controllers' (maxCo, other
functionObjects). Supports 'enabled' flag but none of othe other ones
'timeStart', 'timeEnd', 'writeControl' etc.

## SourceFiles
setTimeStepFunctionObject.C

