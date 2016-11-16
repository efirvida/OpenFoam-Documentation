# fvMeshDistribute 
## Class
Foam::fvMeshDistribute

## Description
Sends/receives parts of mesh+fvfields to neighbouring processors.
Used in load balancing.

Input is per local cell the processor it should move to. Moves meshes
and volFields/surfaceFields and returns map which can be used to
distribute other.

Notes:
- does not handle cyclics. Will probably handle separated proc patches.
- if all cells move off processor also all its processor patches will
      get deleted so comms might be screwed up (since e.g. globalMeshData
      expects procPatches on all)
- initial mesh has to have procPatches last and all normal patches common
      to all processors and in the same order. This is checked.
- faces are matched topologically but points on the faces are not. So
      expect problems -on separated patches (cyclics?) -on zero sized processor
      edges.

## SourceFiles
fvMeshDistribute.C
fvMeshDistributeTemplates.C

