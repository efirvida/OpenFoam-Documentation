# ptscotchDecomp 
## Class
Foam::ptscotchDecomp

## Description
PTScotch domain decomposition.
For the main details about how to define the strategies, see scotchDecomp.

Nonetheless, when decomposing in parallel, using <tt>writeGraph=true</tt>
will write out \c .dgr files for debugging. For example, use these files
with \c dgpart as follows:

```
mpirun -np 4 dgpart 2 'region0_%r.dgr'
```

where:
      - %r gets replaced by current processor rank
      - it will decompose into 2 domains

## See also
Foam::scotchDecomp

## SourceFiles
ptscotchDecomp.C

