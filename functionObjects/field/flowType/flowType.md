# flowType 
## Class
Foam::functionObjects::flowType

## Group
grpFieldFunctionObjects

## Description
This function object calculates and writes the flowType of a velocity field.

The flow type parameter is obtained according to the following equation:
```
                 |D| - |Omega|
        lambda = -------------
                 |D| + |Omega|

        -1 = rotational flow
         0 = simple shear flow
         1 = planar extensional flow
```

## See also
Foam::functionObjects::fieldExpression
Foam::functionObjects::fvMeshFunctionObject

## SourceFiles
flowType.C

