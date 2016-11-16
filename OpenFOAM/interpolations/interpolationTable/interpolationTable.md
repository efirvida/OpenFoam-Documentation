# interpolationTable 
## Class
Foam::interpolationTable

## Description
An interpolation/look-up table of scalar vs \<Type\> values.
The reference scalar values must be monotonically increasing.

The handling of out-of-bounds values depends on the current setting
of \c outOfBounds.

If \c repeat is chosen for the out-of-bounds handling, the final time
value is treated as being equivalent to time=0 for the following periods.


The construct from dictionary reads a filename from a dictionary and
has an optional readerType. Default is to read OpenFOAM format. The only
other format is csv (comma separated values):

Read csv format:
```
        readerType      csv;
        fileName        "$FOAM_CASE/constant/p0vsTime.csv";
        hasHeaderLine   true;   // skip first line
        timeColumn      0;      // time is in column 0
        valueColumns    (1);    // value starts in column 1
```


## Note
- Accessing an empty list results in an error.
- Accessing a list with a single element always returns the same value.

## SourceFiles
interpolationTable.C

