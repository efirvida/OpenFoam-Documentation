# Q 
## Class
Foam::functionObjects::Q

## Group
grpFieldFunctionObjects

## Description
This function object calculates and outputs the second invariant of the
velocity gradient tensor [1/s^2].

\f[
        Q = 0.5(sqr(tr(\nabla U)) - tr(((\nabla U) \cdot (\nabla U))))
\f]

## See also
Foam::functionObjects::fieldExpression
Foam::functionObjects::fvMeshFunctionObject

## SourceFiles
Q.C

