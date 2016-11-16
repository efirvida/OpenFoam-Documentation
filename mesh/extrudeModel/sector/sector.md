# sector 
## Class
Foam::extrudeModels::sector

## Description
Extrudes by rotating a surface around an axis
- extrusion is opposite the surface/patch normal so inwards the source
      mesh
- axis direction has to be consistent with this.
- use -mergeFaces option if doing full 360 and want to merge front and back
- note direction of axis. This should be consistent with rotating against
      the patch normal direction. If you get it wrong you'll see all cells
      with extreme aspect ratio and internal faces wrong way around in
      checkMesh

