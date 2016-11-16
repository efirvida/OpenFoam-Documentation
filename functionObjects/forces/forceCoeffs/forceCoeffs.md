# forceCoeffs 
## Class
Foam::functionObjects::forceCoeffs

## Group
grpForcesFunctionObjects

## Description
This function object extends the Foam::forces function object by providing
lift, drag and moment coefficients.  The data can optionally be output into
bins, defined in a given direction.

Example of function object specification:
```
forceCoeffs1
{
        type        forceCoeffs;
        libs ("libforces.so");
        ...
        log         yes;
        patches     (walls);
        liftDir     (0 1 0);
        dragDir     (-1 0 0);
        pitchAxis   (0 0 1);
        magUInf     100;
        lRef        3.5;
        Aref        2.2;

        binData
        {
            nBin        20;
            direction   (1 0 0);
            cumulative  yes;
        }
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | type name: forces       | yes         |
        log          | write force data to standard output | no | no
        patches      | patches included in the forces calculation | yes |
        liftDir      | lift direction          | yes         |
        dragDir      | drag direction          | yes         |
        pitchAxis    | picth axis              | yes         |
        magUInf      | free stream velocity magnitude | yes  |
        lRef         | reference length scale for moment calculations | yes |
        Aref         | reference area          | yes |


Bin data is optional, but if the dictionary is present, the entries must
be defined according o

        nBin         | number of data bins     | yes         |
        direction    | direction along which bins are defined | yes |
        cumulative   | bin data accumulated with incresing distance | yes |


## See also
Foam::functionObject
Foam::functionObjects::timeControl
Foam::functionObjects::forces

## SourceFiles
forceCoeffs.C

