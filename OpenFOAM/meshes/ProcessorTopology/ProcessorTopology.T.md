# ProcessorTopology.T 
## Class
Foam::ProcessorTopology

## Description
Determines processor-processor connection. After instantiation contains
on all processors the processor-processor connection table.

*this[proci] gives the list of neighbouring processors.

TODO: This does not currently correctly support multiple processor
patches connecting two processors.

## SourceFiles
ProcessorTopology.C

