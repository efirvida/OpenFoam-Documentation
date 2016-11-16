# slicedFvPatchField 
## Class
Foam::slicedFvPatchField

## Group
grpGenericBoundaryConditions

## Description
Specialization of fvPatchField which creates the underlying
fvPatchField as a slice of the given complete field.

The destructor is wrapped to avoid deallocation of the storage of the
complete fields when this is destroyed.

Should only used as a template argument for SlicedGeometricField.

## See also
Foam::fvPatchField

## SourceFiles
slicedFvPatchField.C

