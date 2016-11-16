# multiDirRefinement 
## Class
Foam::multiDirRefinement

## Description
Does multiple pass refinement to refine cells in multiple directions.

Gets a list of cells to refine and vectorFields for the whole mesh.
It then tries to refine in one direction after the other the wanted cells.
After construction the mesh will have been refined in multiple directions.

Holds the list of cells to refine and the map from original to added for
every refinement level.

Gets constructed from a dictionary or from components.
Uses an undoableMeshCutter which does the actual cutting. Undo facility
is switched of unless constructed from external one which allows this.

The cut cells get stored in addedCells which is for every vectorField
to cut with the map from uncut to added cell (i.e. from master to slave).
Note: map is only valid for a given direction.

Parallel: should be ok. Uses 'reduce' whenever it needs to make a
local decision.

## SourceFiles
multiDirRefinement.C

