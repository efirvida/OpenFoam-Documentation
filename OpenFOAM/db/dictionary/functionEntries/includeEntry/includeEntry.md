# includeEntry 
## Class
Foam::functionEntries::includeEntry

## Description
Specify an include file when reading dictionaries, expects a
single string to follow.

An example of the \c \#include directive:
```
        #include "includeFile"
```

The usual expansion of environment variables and other constructs
(eg, the \c ~OpenFOAM/ expansion) is retained.

## See also
fileName, string::expand()

## SourceFiles
includeEntry.C

