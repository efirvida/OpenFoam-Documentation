# codedFunctionObject 
## Class
Foam::codedFunctionObject

## Group
grpUtilitiesFunctionObjects

## Description
This function object provides a general interface to enable dynamic code
compilation.

The entries are
        codeInclude : include files
        codeOptions : include paths; inserted into EXE_INC in Make/options
        codeLibs    : link line; inserted into LIB_LIBS in Make/options
        codeData    : c++; local member data (null constructed);
        localCode   : c++; local static functions
        codeRead    : c++; upon functionObject::read();
        codeExecute : c++;upon functionObject::execute();
        codeWrite   : c++; upon functionObject::write()
        codeEnd     : c++; upon functionObject::end();

Example of function object specification:
```
difference
{
        libs ("libutilityFunctionObjects.so");

        type coded;
        // Name of on-the-fly generated functionObject
        name writeMagU;
        codeWrite
        #{
            // Lookup U
            const volVectorField& U = mesh().lookupObject<volVectorField>("U");
            // Write
            mag(U).write();
        }
}
```


## See also
Foam::functionObject
Foam::codedBase

## SourceFiles
codedFunctionObject.C

