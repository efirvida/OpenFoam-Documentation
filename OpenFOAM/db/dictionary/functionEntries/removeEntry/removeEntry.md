# removeEntry 
## Class
Foam::functionEntries::removeEntry

## Description
Remove a dictionary entry.

The \c \#remove directive takes a list or a single wordRe.
For example,
```
        #remove entry0
        #remove ( entry1 entry2 entry3 otherEntry )
        #remove "entry[1-3]"
        #remove ( "entry[1-3]" otherEntry )
```

The removal only occurs in the current context.
Removing sub-entries or parent entries is not supported.

## SourceFiles
removeEntry.C

