# treeBoundBox 
## Class
Foam::treeBoundBox

## Description
Standard boundBox + extra functionality for use in octree.

Numbering of corner points is according to octant numbering.

On the back plane (z=0):

```
        Y
        ^
        |
        +--------+
        |2      3|
        |        |
        |        |
        |        |
        |0      1|
        +--------+->X
```

For the front plane add 4 to the point labels.


## SourceFiles
treeBoundBoxI.H
treeBoundBox.C
treeBoundBoxTemplates.C

