# pointPatchField 
## Class
Foam::pointPatchField

## Description
Abstract base class for point-mesh patch fields.

The base-field does not store values as they are part of the
"internal field".  There are derived classes to store constraint values
e.g. fixedValuePointPatchField derived from the generic
valuePointPatchField which ensures the values in the "internal field"
are reset to the fixed-values by applying the stored values.

## SourceFiles
pointPatchField.C
newPointPatchField.C

