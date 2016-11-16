# codeStream 
## Class
Foam::functionEntries::codeStream

## Description
Dictionary entry that contains C++ OpenFOAM code that is compiled to
generate the entry itself. So
- codeStream reads three entries: 'code', 'codeInclude' (optional),
'codeOptions' (optional)
and uses those to generate library sources inside \c codeStream/
- these get compiled using 'wmake libso'
- the resulting library is loaded in executed with as arguments
\code
        (const dictionary& dict, Ostream& os)
\endcode
where the dictionary is the current dictionary.
- the code has to write into Ostream which is then used to construct
the actual dictionary entry.


E.g. to set the internal field of a field:

```
internalField  #codeStream
{
        code
        #{
            const IOdictionary& d = static_cast<const IOdictionary&>(dict);
            const fvMesh& mesh = refCast<const fvMesh>(d.db());
            scalarField fld(mesh.nCells(), 12.34);
            fld.writeEntry("", os);
        #};

        //- Optional:
        codeInclude
        #{
            #include "fvCFD.H"
        #};

        //- Optional:
        codeOptions
        #{
            -I$(LIB_SRC)/finiteVolume/lnInclude
        #};
};
```


Note the \c \#{ ... \c \#} syntax is a 'verbatim' input mode that allows
inputting strings with embedded newlines.

Limitations:
- '~' symbol not allowed inside the code sections.
- probably some other limitations (uses string::expand which expands
      \c \$ and \c ~ sequences)

## Note
The code to be compiled is stored under the local \c codeStream directory
with a subdirectory name corresponding to the SHA1 of the contents.

The corresponding library code is located under the local
\c codeStream/platforms/$WM_OPTIONS/lib directory in a library
\c libcodeStream_SHA1.so

## SourceFiles
codeStream.C

