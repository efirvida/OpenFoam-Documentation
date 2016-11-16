# fvMeshSubset 
## Class
Foam::fvMeshSubset

## Description
Post-processing mesh subset tool.  Given the original mesh and the
list of selected cells, it creates the mesh consisting only of the
desired cells, with the mapping list for points, faces, and cells.

Puts all exposed internal faces into either
- a user supplied patch
- a newly created patch "oldInternalFaces"

- setCellSubset is for small subsets. Uses Maps to minimize memory.
- setLargeCellSubset is for largish subsets (>10% of mesh).
      Uses labelLists instead.

- setLargeCellSubset does coupled patch subsetting as well. If it detects
      a face on a coupled patch 'losing' its neighbour it will move the
      face into the oldInternalFaces patch.

- if a user supplied patch is used it is up to the destination
      patchField to handle exposed internal faces (mapping from face -1).
      If not provided the default is to assign the internalField. All the
      basic patch field types (e.g. fixedValue) will give a warning and
      preferably derived patch field types should be used that know how to
      handle exposed faces (e.g. use uniformFixedValue instead of fixedValue)

## SourceFiles
fvMeshSubset.C

