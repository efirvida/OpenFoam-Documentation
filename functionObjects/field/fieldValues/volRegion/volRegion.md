# volRegion 
## Class
Foam::functionObjects::fieldValues::volRegion

## Group
grpFieldFunctionObjects

## Description
This function object provides a 'cell region' variant of the fieldValues
function object.  Given a list of user-specified fields and a selection
of mesh cells, a number of operations can be performed, such as sums,
averages and integrations.


Example of function object specification:
```
volRegion1
{
        type            volRegion;
        libs ("libfieldFunctionObjects.so");
        ...
        log             true;
        writeFields     true;
        regionType      cellZone;
        name            c0;
        operation       volAverage;
        weightField     alpha1;
        fields
        (
            p
            U
        );
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | Type name: volRegion   | yes         |
        log          | Write data to standard output | no    | no
        writeFields  | Write the region field values  | yes     |
        writeVolume  | Write the volume of the volRegion | no |
        regionType   | cell regionType: see below  | yes         |
        name         | name of cell regionType if required  | no |
        operation    | operation to perform    | yes         |
        weightField  | name of field to apply weighting | no |
        fields       | list of fields to operate on | yes    |


Where \c regionType is defined by
\plaintable
        cellZone     | requires a 'name' entry to specify the cellZone
        all          | all cells
\endplaintable

The \c operation is one of:
\plaintable
       none          | no operation
       sum           | sum
       sumMag        | sum of component magnitudes
       average       | ensemble average
       weightedAverage | weighted average
       volAverage    | volume weighted average
       weightedVolAverage | weighted volume average
       volIntegrate  | volume integral
       min           | minimum
       max           | maximum
       CoV           | coefficient of variation: standard deviation/mean
\endplaintable

## See also
Foam::fieldValues
Foam::functionObject

## SourceFiles
volRegion.C

