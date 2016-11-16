# SlicedGeometricField.T 
## Class
Foam::SlicedGeometricField

## Description
Specialization of GeometricField which holds slices of given complete
fields in a form that they act as a GeometricField.

The destructor is wrapped to avoid deallocation of the storage of the
complete fields when this is destroyed.

SlicedGeometricField can only be instantiated with a valid form of
SlicedPatchField to handle the slicing and storage deallocation of the
boundary field.

## SourceFiles
SlicedGeometricField.C

