# syncTools 
## Class
Foam::syncTools

## Description
Various tools to aid synchronizing lists across coupled patches. WIP.

Require
- combineOperator (e.g. sumEqOp - not sumOp!) that is defined for the
      type and combineReduce(UList\<T\>, combineOperator) should be defined.
- null value which gets overridden by any valid value.
- transform function

## SourceFiles
syncTools.C
syncToolsTemplates.C

