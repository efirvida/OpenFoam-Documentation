# SubField.T 
## Class
Foam::SubField

## Description
SubField is a Field obtained as a section of another Field.

Thus it is itself unallocated so that no storage is allocated or
deallocated during its use.  To achieve this behaviour, SubField is
derived from a SubList rather than a List.

## SourceFiles
SubFieldI.H

