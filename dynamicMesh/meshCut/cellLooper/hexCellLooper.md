# hexCellLooper 
## Class
Foam::hexCellLooper

## Description
Implementation of cellLooper.

This one walks hexes in a topological way:
      - cross edge to other face
      - cross face by walking edge-point-edge across to reach the other side.
(edges are always cut through the middle)

For anything else (tet, prism, .. poly) it will use geomCellLooper
(which does a purely geometric cut using a plane through cell centre)

## SourceFiles
hexCellLooper.C

