# faceCollapser 
## Class
Foam::faceCollapser

## Description
Collapses faces into edges. Used to remove sliver faces (faces with small
area but non-zero span).

Passed in as
- face label
- the two indices in the face (fpA, fpB) which delimit the vertices to be
      kept.

Takes the vertices outside the range fpA..fpB and projects them onto the
kept edges (edges using kept vertices only).

Note:
- Use in combination with edge collapse to cleanup meshes.
- Can not remove cells so will mess up trying to remove a face on a tet.
- WIP. Should be combined with edge collapsing and cell collapsing into
      proper 'collapser'.
- Caller is responsible for making sure kept vertices (fpA..fpB) for one
      face are not the vertices to be removed for another face.

## SourceFiles
faceCollapser.C

