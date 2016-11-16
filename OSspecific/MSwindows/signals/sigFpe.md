# sigFpe 
## Class
sigFpe

## Description
Sets up trapping for floating point exceptions (sigfpe).

Controlled by two env vars:
FOAM_SIGFPE : exception trapping
FOAM_SETNAN : initialization of all malloced memory to NaN. If also
                  FOAM_SIGFPE set this will cause usage of uninitialized scalars
                  to trigger an abort.

## SourceFiles
sigFpe.C

