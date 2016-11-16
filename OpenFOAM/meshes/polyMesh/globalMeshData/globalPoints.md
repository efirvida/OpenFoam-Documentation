# globalPoints 
## Class
Foam::globalPoints

## Description
Calculates points shared by more than two processor patches or cyclic
patches.

Is used in globalMeshData. (this info is needed for point/edge
communication where processor swaps are not enough to exchange data)

Works purely topological and using local communication only.
Needs:
      - domain to be one single domain (i.e. all faces can be reached through
        face-cell walk).
      - patch face ordering to be ok
      - f[0] ordering on patch faces to be ok.

Works by constructing equivalence lists for all the points on processor
patches. These list are in globalIndexAndTransform numbering
E.g.
```
          ((7 93)(4 731)(3 114))
```

means point 93 on proc7 is connected to point 731 on proc4 and 114 on proc3.
It then assigns the lowest numbered processor to be the local 'master' and
constructs a mapDistribute to send all data to this master.

Algorithm:
        - get meshPoints of all my points on processor patches and initialize
          equivalence lists to this.
     loop
        - send to all neighbours in relative form:
            - patchFace
            - index in face
        - receive and convert into meshPoints. Add to to my equivalence lists.
        - mark meshPoints for which information changed.
        - send data for these meshPoints again
     endloop until nothing changes

At this point one will have complete point-point connectivity for all
points on processor patches. Now (optionally) remove point
equivalences of size 2. These are just normal points shared
between two neighbouring procPatches.

Note: the data held is either mesh point labels (construct from mesh only)
or patch point labels (construct from mesh and patch).

## SourceFiles
globalPoints.C

