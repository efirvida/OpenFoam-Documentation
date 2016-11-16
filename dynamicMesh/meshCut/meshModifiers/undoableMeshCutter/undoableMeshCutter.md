# undoableMeshCutter 
## Class
Foam::undoableMeshCutter

## Description
The main refinement handler. Gets cellCuts which is structure that
describes which cells are to be cut and in what way. Maintains an undo
list (if told so during construction). Apart from undo list is just
wrapper around meshCutter.

Undo list: contains a refinement tree (of type splitCell; cell labels are
of no consequence) and a list of visible splitCells, i.e. the top of the
tree (where the cell labels are valid). Now every cell added gets put on
the tree and every updateMesh action updates the labels of visible
splitcells.

We can now ask this structure for a list of visible split cells or the list
of faces between these. These can be passed to removeFaces for actual
deletion and we delete the top splitCell and update the now newly visible
underlying cells for the new cell number (passed back from removeFaces).

NOTE: Undoing note properly tested. Expect it to fail if the faces to
be removed cause other faces to be additionally removed (i.e. removeFaces
adds additional faces to remove).

splitCell:
- original cell number.
- pointer to parent (null for first level splitCell)
- two pointers to splitCell children. Both null (unrefined=visible cell) or
      both non-null.

- live are:
        (-all unrefined cells (original cell without any splitCells))
        -all splitCells with null children

- liveSplitCells contains pointers to splitCells with null children.



## SourceFiles
undoableMeshCutter.C

