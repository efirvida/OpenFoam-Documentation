# polyTopoChange 
## Class
Foam::polyTopoChange

## Description
Direct mesh changes based on v1.3 polyTopoChange syntax.

Instead of recording changes and executing them all in one go (as did
v1.3 polyTopoChange) this class actually holds the current
points/faces/cells and does the change immediately.
It can be asked to compress out all unused points/faces/cells and
renumber everything to be consistent.

Note:
- polyTopoChange can be copied.
- adding a face using non-existing cells causes all intermediate cells
to be added. So always first add cells/points and then faces.
(or set strict checking)
- strict checking:
        - any added/modified face can only use already existing vertices
        - any added face can only use already existing cells
        - no item can be removed more than once.
- removed cell: cell set to 0 faces.
- removed face: face set to 0 vertices.
- removed point: coordinate set to vector::max (VGREAT,VGREAT,VGREAT).
Note that this might give problems if this value is used already.
To see if point is equal to above value we don't use == (which might give
problems with roundoff error) but instead compare the individual component
with >.
- coupled patches: the reorderCoupledFaces routine (borrowed from
the couplePatches utility) reorders coupled patch faces and
uses the cyclicPolyPatch,processorPolyPatch functionality.

## SourceFiles
polyTopoChange.C
polyTopoChangeI.H
polyTopoChangeTemplates.C

