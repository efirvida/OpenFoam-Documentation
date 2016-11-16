# CSV.T 
## Class
Foam::Function1Types::CSV

## Description
Templated CSV container data entry.  Reference column is always a scalar,
e.g. time

```
        <entryName> csvFile;
        <entryName>Coeffs
        {
            nHeaderLine         4;          // number of header lines
            refColumn           0;          // reference column index
            componentColumns    (1 2 3);    // component column indices
            separator           ",";        // optional (defaults to ",")
            mergeSeparators     no;         // merge multiple separators
            fileName            "fileXYZ";  // name of csv data file
            outOfBounds         clamp;      // optional out-of-bounds handling
            interpolationScheme linear;     // optional interpolation scheme
        }
```

## SourceFiles
CSV.C

