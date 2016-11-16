# cellMatcher 
## Class
Foam::cellMatcher

## Description
Base class for cellshape matchers (hexMatch, prismMatch, etc.). These are
classes which given a mesh and cell number find out the orientation of
the cellShape and construct cell-vertex to mesh-vertex mapping and
cell-face to mesh-face mapping.

For example,
```
        hexMatcher hex(mesh);
        cellShape shape;
        ..
        bool isHex = hex.match(celli, shape);
```
Now shape is set to the correct Hex cellShape (if \a isHex is true)

Alternatively there is direct access to the vertex and face mapping:
```
        const labelList& hexVertLabels = hex.vertLabels();
        const labelList& hexFaceLabels = hex.faceLabels();
```
Now
      - \c hexVertLabels[n] is vertex label of hex vertex n
      - \c hexFaceLabels[n] is face   label of hex vertex n

Process of cellShape recognition consists of following steps:
- renumber vertices of cell to local vertex numbers
- construct (local to cell) addressing edge-to-faces
- construct (local to cell) addressing vertex and face to index in face
- find most unique face shape (e.g. triangle for prism)
- walk (following either vertices in face or jumping from face to other
      face) to other faces and checking face sizes.
- if necessary try other rotations of this face
      (only necessary for wedge, tet-wedge)
- if necessary try other faces which most unique face shape
      (never necessary for hex degenerates)

The whole calculation is done such that no lists are allocated during
cell checking. E.g. localFaces_ are always sized to hold max. number
of possible face vertices and a separate list is filled which holds
the actusl face sizes.

For now all hex-degenerates implemented. Numbering taken from picture in
demoGuide.

## SourceFiles
cellMatcherI.H
cellMatcher.C

