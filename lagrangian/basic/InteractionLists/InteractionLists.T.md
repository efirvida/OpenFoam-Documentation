# InteractionLists.T 
## Class
Foam::InteractionLists

## Description

Builds direct interaction list, specifying which local (real)
cells are potentially in range of each other.

Builds referred interaction list, specifying which cells are
required to provide interactions across coupled patches (cyclic or
processor).  Generates referred cells, and refers particles to the
correct processor, applying the appropriate transform.

Simultaneous communication and computation is possible using:

```
PstreamBuffers pBufs(Pstream::nonBlocking);
label startOfRequests = Pstream::nRequests();
il_.sendReferredData(cellOccupancy_, pBufs);
// Do other things
il_.receiveReferredData(pBufs, startOfRequests);
```

Requiring data:

```
List<DynamicList<typename CloudType::parcelType*>> cellOccupancy_;
```

## SourceFiles
InteractionListsI.H
InteractionLists.C
InteractionListsIO.C

