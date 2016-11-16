# mapDistribute 
## Class
Foam::mapDistribute

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

- without transforms:
Constructors using compact numbering: layout is
- all my own elements first (whether used or not)
- followed by used-only remote elements sorted by remote processor.
So e.g 4 procs and on proc 1 the compact
table will first have all globalIndex.localSize() elements from proc1
followed by used-only elements of proc0, proc2, proc3.
The constructed mapDistribute sends the local elements from and
receives the remote elements into their compact position.
compactMap[proci] is the position of elements from proci in the compact
map. compactMap[myProcNo()] is empty since trivial addressing.

It rewrites the input global indices into indices into the constructed
data.


- with transforms:
This requires the precalculated set of possible transforms
(globalIndexAndTransform). These are given as permutations (+, -, or none)
of up to 3 independent transforms.
The layout of the data is
- all my own elements first (whether used or not)
- followed by used-only remote elements sorted by remote processor.
- followed by - for each transformation index - the set of local or
remote elements with that transformation.
The inputs for the constructor are
- the set of untransformed local or remote indices in globalIndex
numbering. These get rewritten to be indices into the layout of the data.
- the set of transformed local or remote indices in globalIndexAndTransform
encoding. These are labelPairs.

Any distribute with transforms is now done as:
1. exchange data with other processors and receive these into the
slots for that processor
2. for all transformations transform a subset of the data according
to transformElements_[transformI] and store this starting from
transformStart_[transformI]

In the same way a reverse distribute will
1. apply the inverse transform to the data starting at
transformStart_[transformI] and copy the result back into the
transformElements_[transformI]. These might be local or remote slots.
2. the data in the remote slots will now be sent back to the correct
location in the originating processor.

E.g. a map to handle
- mesh points on a mesh with
- 1 cyclic so 3 permutations (+,-,none) will have layout
- on e.g. processor 1 out of 2:

        +------+ <- transformStart[2]
        |      |
        |      | <- transform2 applied to data in local or remote slots
        |      |
        +------+ <- transformStart[1]
        |      |
        |      | <- transform1 applied to data in local or remote slots
        |      |
        +------+ <- transformStart[1]
        |      |
        |      | <- transform0 applied to data in local or remote slots
        |      |
        +------+ <- transformStart[0]
        |      |
        |      | <- data from proc2
        |      |
        +------+
        |      |
        |      | <- data from proc0
        |      |
        +------+ <- mesh.nPoints()
        |      |
        |      |
        |      |
        +------+ 0


When constructing from components optionally a 'flip' on
the maps can be specified. This will interpret the map
values as index+flip, similar to e.g. faceProcAddressing. The flip
will only be applied to fieldTypes (scalar, vector, .. triad)


## SourceFiles
mapDistribute.C
mapDistributeTemplates.C

