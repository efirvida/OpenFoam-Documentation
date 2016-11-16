# removeCells 
## Class
Foam::removeCells

## Description
Given list of cells to remove insert all the topology changes.

Works in two passes:
- get faces that will become boundary faces
- given these faces and the patches they have to go into make the
      changes.

## SourceFiles
removeCells.C

