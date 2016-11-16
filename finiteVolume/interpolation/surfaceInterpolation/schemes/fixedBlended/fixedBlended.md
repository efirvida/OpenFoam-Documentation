# fixedBlended 
## Class
Foam::fixedBlended

## Description
Two-scheme fixed-blending differencing scheme.

Similar to localBlended but uses a single (global) constant blending
factor. The factor applies to the first scheme and 1-factor to the
second scheme.

## Note
Although a blending factor of 0 and 1 is permitted, it is more efficient
just to use the underlying scheme directly.

## SourceFiles
fixedBlended.C

