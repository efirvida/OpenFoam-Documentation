# Table.T 
## Class
Foam::Function1Types::Table

## Description
Templated table container data entry. Items are stored in a list of
Tuple2's. First column is always stored as scalar entries. Data is read
in Tuple2 form, e.g. for an entry \<entryName\> that is (scalar, vector):

```
        <entryName>   table
        (
            (0.0 (1 2 3))
            (1.0 (4 5 6))
        );
```

## SourceFiles
Table.C

