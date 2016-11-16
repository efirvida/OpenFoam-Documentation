# histogram 
## Class
Foam::functionObjects::histogram

## Group
grpFieldFunctionObjects

## Description
Write the volume-weighted histogram of a volScalarField.

Example:
```
histogram1
{
        type            histogram;

        libs ("libfieldFunctionObjects.so");

        field           p;
        nBins           100;
        min             -5;
        max             5;
        setFormat       gnuplot;
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | type name: histogram    | yes         |
        field        | Field to analyse        | yes         |
        nBins        | Number of bins for the histogram | yes|
        max          | Maximum value sampled   | yes         |
        min          | minimum value sampled   | no          | 0
        setFormat    | Output format           | yes         |


## See also
Foam::functionObject
Foam::functionObjects::writeFile

## SourceFiles
histogram.C

