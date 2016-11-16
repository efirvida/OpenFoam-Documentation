# mapDistributeBase 
## Class
Foam::mapDistributeBase

## Description
Class containing processor-to-processor mapping information.

We store mapping from the bits-to-send to the complete starting list
(subXXXMap) and from the received bits to their location in the new
list (constructXXXMap).

## Note:
Schedule is a list of processor pairs (one send, one receive. One of
them will be myself) which forms a scheduled (i.e. non-buffered) exchange.
See distribute on how to use it.
Note2: number of items sent on one processor have to equal the number
of items received on the other processor.

To aid constructing these maps there are the constructors from global
numbering, either with or without transforms.

Constructors using compact numbering: layout is
- all my own elements first (whether used or not)
- followed by used-only remote elements sorted by remote processor.
So e.g 4 procs and on proc 1 the compact
table will first have all globalIndex.localSize() elements from proc1
followed by used-only elements of proc0, proc2, proc3.
The constructed mapDistributeBase sends the local elements from and
receives the remote elements into their compact position.
compactMap[proci] is the position of elements from proci in the compact
map. compactMap[myProcNo()] is empty since trivial addressing.

It rewrites the input global indices into indices into the constructed
data.

When constructing from components optionally a 'flip' on
the maps can be specified. This will interpret the map
values as index+flip, similar to e.g. faceProcAddressing. The flip
will only be applied to fieldTypes (scalar, vector, .. triad)


## SourceFiles
mapDistributeBase.C
mapDistributeBaseTemplates.C

