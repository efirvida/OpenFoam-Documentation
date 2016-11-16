# mapNearestMethod 
## Class
Foam::mapNearestMethod

## Description
Map nearest mesh-to-mesh interpolation class

Not volume conservative.
- cells outside other meshes bounding box do not get mapped
      (initial filtering)
- all remaining cells will be mapped (with weight 1!)
- so take care when mapping meshes with different bounding boxes!

## SourceFiles
mapNearestMethod.C

