# refinementIterator 
## Class
Foam::refinementIterator

## Description
Utility class to do iterating meshCutter until all requests satisfied.

Needed since cell cutting can only cut cell once in one go so if
refinement pattern is not compatible on a cell by cell basis it will
refuse to cut.

Parallel: communicates. All decisions done on 'reduce'd variable.

## SourceFiles
refinementIterator.C

