# directions 
## Class
Foam::directions

## Description
Set of directions for each cell in the mesh. Either uniform and size=1
or one set of directions per cell.

Used in splitting cells.
Either all cells have similar refinement direction ('global') or
direction is dependent on local cell geometry, or loads selected fields
by name ('fieldBased'). Controlled by dictionary.

## SourceFiles
directions.C

