# residuals 
## Class
Foam::functionObjects::residuals

## Group
grpUtilitiesFunctionObjects

## Description
This function object writes out the initial residual for specified fields.

Example of function object specification:
```
residuals
{
        type            residuals;
        writeControl   timeStep;
        writeInterval  1;
        fields
        (
            U
            p
        );
}
```

Output data is written to the dir postProcessing/residuals/\<timeDir\>/
For vector/tensor fields, e.g. U, where an equation is solved for each
component, the largest residual of each component is written out.

## See also
Foam::functionObject
Foam::functionObjects::writeFiles
Foam::functionObjects::timeControl

## SourceFiles
residuals.C

