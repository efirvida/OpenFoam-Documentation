# boundaryRegion 
## Class
Foam::boundaryRegion

## Description
The boundaryRegion persistent data saved as a Map<dictionary>.

The meshReader supports boundaryRegion information.

The <tt>constant/boundaryRegion</tt> file is an \c IOMap<dictionary>
that is used to save the information persistently.
It contains the boundaryRegion information of the following form:

```
        (
            INT
            {
                BoundaryType    WORD;
                Label           WORD;
            }
            ...
        )
```

## SourceFiles
boundaryRegion.C

