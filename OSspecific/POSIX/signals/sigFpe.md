# sigFpe 
## Class
Foam::sigFpe

## Description
Set up trapping for floating point exceptions (signal FPE).

Controlled by two env vars:
      - \par FOAM_SIGFPE
        Exception trapping
      - \par FOAM_SETNAN
        Initialization of all malloced memory to NaN. If FOAM_SIGFPE
        also set, this will cause usage of uninitialized scalars to trigger
        an abort.

## SourceFiles
sigFpe.C

