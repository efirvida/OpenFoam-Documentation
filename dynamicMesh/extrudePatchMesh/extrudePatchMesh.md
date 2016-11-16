# extrudePatchMesh 
## Class
Foam::extrudePatchMesh

## Description
Mesh at a patch created on the fly. The following entry should be used
on the field boundary dictionary:

Example:
```
        // New Shell mesh data

        extrudeModel    linearNormal;
        linearNormalCoeffs
        {
            thickness       40e-6;
        }
        nLayers         50;
        expansionRatio  1;
        columnCells      true;

        // Patch information
        bottomCoeffs
        {
            name        "bottom";
            type        mappedWall;
            sampleMode  nearestPatchFace;
            samplePatch fixedWalls;
            offsetMode  uniform;
            offset      (0 0 0);
        }

        topCoeffs
        {
            name        "top";
            type        patch;
        }

        sideCoeffs
        {
            name        "side";
            type        empty;
        }
```

