# UIndirectList.T 
## Class
Foam::UIndirectList

## Description
A List with indirect addressing.

Like IndirectList but does not store addressing.

Note the const_cast of the completeList. This is so we can use it both
on const and non-const lists. Alternative would be to have a const_
variant etc.

## SourceFiles
UIndirectListI.H

