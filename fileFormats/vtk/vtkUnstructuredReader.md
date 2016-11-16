# vtkUnstructuredReader 
## Class
Foam::vtkUnstructuredReader

## Description
Reader for vtk unstructured_grid legacy files. Supports single CELLS, POINTS
etc. entry only.

- all integer types (int, unsigned_int, long etc.) become Foam::label
- all real types (float, double) become Foam::scalar
- POINTS becomes OpenFOAM points
- CELLS gets split into OpenFOAM
        - cells
        - faces
        - lines
- CELL_DATA or POINT_DATA gets stored on the corresponding objectRegistry
      in original vtk numbering order so use e.g. faceMap() to go from entry
      in faces() back to vtk numbering.

## SourceFiles
vtkUnstructuredReader.C

