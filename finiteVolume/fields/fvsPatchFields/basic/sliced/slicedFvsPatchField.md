# slicedFvsPatchField 
## Class
Foam::slicedFvsPatchField

## Description
Specialization of fvsPatchField which creates the underlying
fvsPatchField as a slice of the given complete field.

The destructor is wrapped to avoid deallocation of the storage of the
complete fields when this is destroyed.

Should only used as a template argument for SlicedGeometricField.

## SourceFiles
slicedFvsPatchField.C

