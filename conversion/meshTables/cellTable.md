# cellTable 
## Class
Foam::cellTable

## Description
The cellTable persistent data saved as a Map<dictionary>.

The meshReader supports cellTable information.

The <tt>constant/cellTable</tt> file is an \c IOMap<dictionary> that is
used to save the information persistently. It contains the cellTable
information of the following form:

```
        (
            ID
            {
                Label           WORD;
                MaterialType    WORD;
                MaterialId      INT;
                PorosityId      INT;
                ColorIdx        INT;
                ...
            }
        ...
        )
```

If the \a Label is missing, a value <tt>cellTable_{ID}</tt> will be
inferred. If the \a MaterialType is missing, the value @a fluid will
be inferred.

## SourceFiles
cellTable.C

