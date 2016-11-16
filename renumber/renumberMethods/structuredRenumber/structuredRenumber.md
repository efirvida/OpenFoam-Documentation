# structuredRenumber 
## Class
Foam::structuredRenumber

## Description
Renumbering according to mesh layers.
depthFirst = true:
        first column gets ids 0..nLayer-1,
        second nLayers..2*nLayers-1 etc.
depthFirst = false:
        first layer gets ids 0,1,2 etc.

## SourceFiles
structuredRenumber.C

