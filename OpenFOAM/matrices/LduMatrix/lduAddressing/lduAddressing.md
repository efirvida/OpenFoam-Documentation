# lduAddressing 
## Class
Foam::lduAddressing

## Description
The class contains the addressing required by the lduMatrix: upper, lower
and losort.

The addressing can be created in two ways: either with references to
upper and lower in which case it stores references or from labelLists,
in which case it stores the addressing itself. Additionally, the losort
addressing belongs to the class is as on lazy evaluation.

The ordering of owner addresses is such that the labels are in
increasing order, with groups of identical labels for edges "owned" by
the same point. The neighbour labels are also ordered in ascending
order but only for groups of edges belonging to each point. An example
is given below:
```
        owner     neighbour
        0         1
        0         20
        1         2
        1         21
        2         3
        2         22
        3         4
        3         23
        4         5
        4         24
        5         6
        5         25
        6         7
        6         26
        7         8
        7         27
        8         9
        8         28
        9         10
        9         29
```

There exists an alternative way of addressing the owner
list: instead of repeating the same label in the owner list, it is
possible to address the start of each point neighbours in the
neighbour list. This reduces the size of owner addressing from a list
over all edges to a list over all points + 1:

```
        Owner start list: 0 2 4 6 8 10 12 14 16 18
```

We shall use the second form of the addressing for fast lookup
of edge label from the known owner and neighbour, using the following
algorithm:
-# take the owner label and position the start of lookup
       using the owner start list
-# loop through all neighbours of this owner (ending at the start of
      lookup of owner + 1) until the match with current neighbour is found.
      The index used on the neighbour list for the match is the edge index.

While owner start addressing allows us to find the edge owned by the
points, it is also necessary to find the edges for which the point is
a neighbour. Losort addressing lists the edges neighboured by the
point and we shall use the same trick as above to address into this
list. Thus, for every point the losort start gives the address of the
first face to neighbour this point.

## SourceFiles
lduAddressing.C

