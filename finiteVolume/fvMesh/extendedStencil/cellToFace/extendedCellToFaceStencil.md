# extendedCellToFaceStencil 
## Class
Foam::extendedCellToFaceStencil

## Description
Calculates/constains the extended cell-to-face stencil.

The stencil is a list of indices into either cells or boundary faces
in a compact way. (element 0 is owner, 1 is neighbour). The index numbering
is
- cells first
- then all (non-empty patch) boundary faces

When used in evaluation is a two stage process:
- collect the data (cell data and non-empty boundaries) into a
single field
- (parallel) distribute the field
- sum the weights*field.

## SourceFiles
extendedCellToFaceStencil.C
extendedCellToFaceStencilTemplates.C

