# regionSplit 
## Class
Foam::regionSplit

## Description
This class separates the mesh into distinct unconnected regions,
each of which is then given a label according to globalNumbering().


Say 6 cells, 3 processors, with single baffle on proc1.

              baffle
                |
+---+---+---+---+---+---+
|   |   |   |   |   |   |
+---+---+---+---+---+---+
      proc0 | proc1 | proc2



1: determine local regions (uncoupled)

+---+---+---+---+---+---+
| 0 | 0 | 0 | 1 | 0 | 0 |
+---+---+---+---+---+---+
      proc0 | proc1 | proc2



2: make global

+---+---+---+---+---+---+
| 0 | 0 | 1 | 2 | 3 | 3 |
+---+---+---+---+---+---+
      proc0 | proc1 | proc2



3: merge connected across procs

+---+---+---+---+---+---+
| 0 | 0 | 0 | 2 | 2 | 2 |
+---+---+---+---+---+---+
      proc0 | proc1 | proc2



4. determine locally owner regions. determine compact numbering for the
local regions and send these to all processors that need them:

proc0 uses regions:
        - 0 which is local to it.
proc1 uses regions
        - 0 which originates from proc0
        - 2 which is local to it
proc2 uses regions
        - 2 which originates from proc1

So proc1 needs to get the compact number for region 0 from proc0 and proc2
needs to get the compact number for region 2 from proc1:

+---+---+---+---+---+---+
| 0 | 0 | 0 | 1 | 1 | 1 |
+---+---+---+---+---+---+
      proc0 | proc1 | proc2


Can optionally keep all regions local to the processor.


## SourceFiles
regionSplit.C

