# calcEntry 
## Class
Foam::functionEntries::calcEntry

## Description
Uses dynamic compilation to provide calculating functionality
for entering dictionary entries.

E.g.

```
a 1.0;
b 3;
c #calc "$a/$b";
```

Note the explicit trailing 0 ('1.0') to force a to be read (and written)
as a floating point number.

## Note
Internally this is just a wrapper around codeStream functionality - the
#calc string gets used to construct a dictionary for codeStream.

## SourceFiles
calcEntry.C

