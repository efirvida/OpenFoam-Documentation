# commSchedule 
## Class
Foam::commSchedule

## Description
Determines the order in which a set of processors should communicate
with one another.

The communication order should
      - have maximum overlap
      - allow blocking communication without deadlock

Does a very simple scheduling which assumes same time for all operations.

After construction:
      - schedule() gives the order in which the input communication should occur
      - procSchedule()[proci] gives per proci

Does not care whether 'talking' is first send, second receive or maybe
full swap. This is all responsability of caller. See ProcessorTopology
class for use in scheduling processor boundary swaps.

## SourceFiles
commSchedule.C

