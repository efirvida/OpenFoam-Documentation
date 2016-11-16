# timeActivatedFileUpdate 
## Class
Foam::functionObjects::timeActivatedFileUpdate

## Group
grpUtilitiesFunctionObjects

## Description
Performs a file copy/replacement once a specified time has been reached.

Example usage to update the fvSolution dictionary at various times
throughout the calculation:

```
fileUpdate1
{
        type              timeActivatedFileUpdate;
        libs ("libutilityFunctionObjects.so");
        writeControl     timeStep;
        writeInterval    1;
        fileToUpdate      "$FOAM_CASE/system/fvSolution";
        timeVsFile
        (
            (-1 "$FOAM_CASE/system/fvSolution.0")
            (0.10 "$FOAM_CASE/system/fvSolution.10")
            (0.20 "$FOAM_CASE/system/fvSolution.20")
            (0.35 "$FOAM_CASE/system/fvSolution.35")
        );
}
```

## SourceFiles
timeActivatedFileUpdate.C

