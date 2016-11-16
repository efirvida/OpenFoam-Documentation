# SubDimensionedField.T 
## Class
Foam::SubDimensionedField

## Description
SubDimensionedField is a DimensionedField obtained as a section of another
DimensionedField.

Thus it is itself unallocated so that no storage is allocated or
deallocated during its use.  To achieve this behaviour,
SubDimensionedField is derived from SubField rather than Field.

## SourceFiles
SubDimensionedFieldI.H

