# fvOption 
## Class
Foam::fv::option

## Description
Finite volume options abstract base class.  Provides a base set of
controls, e.g.:
```
        type            scalarExplicitSource    // source type
        active          on;                     // on/off switch
```

## Note
On evaluation, source/sink options are to be added to the equation R.H.S.

## SourceFiles
fvOption.C
fvOptionIO.C

