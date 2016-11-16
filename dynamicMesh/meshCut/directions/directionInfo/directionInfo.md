# directionInfo 
## Class
Foam::directionInfo

## Description
Holds direction in which to split cell (in fact a local coordinate axes).
Information is a label and a direction.

The direction is the normal
direction to cut in. The label's meaning depends on whether the info
is on a cell or on a face:
        - in cell: edge that is being cut. (determines for hex how cut is)
        - in face: local face point that is being cut or -1.
            -# (-1)  : cut is tangential to plane
            -# (>= 0): edge fp..fp+1 is cut

            (has to be facepoint, not vertex since vertex not valid across
             processors whereas f[0] should correspond to f[0] on other side)

The rule is that if the label is set (-1 or higher) it is used
(topological information only), otherwise the vector is used. This makes
sure that we use topological information as much as possible and so a
hex mesh is cut purely topologically. All other shapes are cut
geometrically.

## SourceFiles
directionInfoI.H
directionInfo.C

