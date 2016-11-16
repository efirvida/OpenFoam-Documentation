# mappedPatchBase 
## Class
Foam::mappedPatchBase

## Description
Determines a mapping between patch face centres and mesh cell or face
centres and processors they're on.

If constructed from dictionary:
```
        // Region to sample (default is region0)
        sampleRegion region0;

        // What to sample:
        // - nearestCell         : sample cell containing point
        // - nearestOnlyCell     : nearest sample cell (even if not containing
        //                         point)
        // - nearestPatchFace    : nearest face on selected patch
        // - nearestPatchFaceAMI : nearest face on selected patch
                                   - patches need not conform
                                   - uses AMI interpolation
        // - nearestFace         : nearest boundary face on any patch
        // - nearestPatchPoint   : nearest patch point (for coupled points
        //                         this might be any of the points so you have
        //                         to guarantee the point data is synchronised
        //                         beforehand)
        sampleMode nearestCell;

        // If sampleMode is nearestPatchFace : patch to find faces of
        samplePatch movingWall;

        // If sampleMode is nearestPatchFace : specify patchgroup to find
        // samplePatch and sampleRegion (if not provided)
        coupleGroup baffleGroup;

        // How to supply offset (w.r.t. my patch face centres):
        // - uniform : single offset vector
        // - nonuniform : per-face offset vector
        // - normal : using supplied distance and face normal
        offsetMode uniform;

        // According to offsetMode (see above) supply one of
        // offset, offsets or distance
        offset  (1 0 0);
```

Note: if offsetMode is \c normal it uses outwards pointing normals. So
supply a negative distance if sampling inside the domain.


## Note
Storage is not optimal. It temporary collects all (patch)face centres
on all processors to keep the addressing calculation simple.

## SourceFiles
mappedPatchBase.C

