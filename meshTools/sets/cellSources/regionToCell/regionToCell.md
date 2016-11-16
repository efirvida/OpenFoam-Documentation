# regionToCell 
## Class
Foam::regionToCell

## Description
TopoSetSource. Select cells belonging to topological connected region
(that contains given points)

In dictionary input:

        // optional name of cellSet delimiting search
        set         c0;

        //- Number of cell layers to erode mesh to detect holes in the mesh
        //  Set to 0 if not used.
        nErode 3;

        // points inside region to select
        insidePoints ((1 2 3));


## SourceFiles
regionToCell.C

