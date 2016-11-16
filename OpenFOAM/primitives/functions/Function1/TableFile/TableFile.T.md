# TableFile.T 
## Class
Foam::Function1Types::TableFile

## Description
Templated table container data entry where data is read from file.

```
        <entryName> tableFile;
        <entryName>Coeffs
        {
            fileName            dataFile;    // name of data file
            outOfBounds         clamp;       // optional out-of-bounds handling
            interpolationScheme linear;      // optional interpolation method
        }
```

Items are stored in a list of Tuple2's. First column is always stored as
scalar entries.  Data is read in the form, e.g. for an entry \<entryName\>
that is (scalar, vector):
```
        (
            (0.0 (1 2 3))
            (1.0 (4 5 6))
        );
```


## SourceFiles
TableFile.C

