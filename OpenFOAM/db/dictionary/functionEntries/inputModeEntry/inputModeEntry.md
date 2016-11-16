# inputModeEntry 
## Class
Foam::functionEntries::inputModeEntry

## Description
Specify the input mode when reading dictionaries, expects
a single word to follow.

An example of \c \#inputMode directive:
```
        #inputMode merge
```

The possible input modes:
      - \par merge      merge sub-dictionaries when possible
      - \par overwrite  keep last entry and silently remove previous ones
      - \par protect    keep initial entry and silently ignore subsequent ones
      - \par warn       keep initial entry and warn about subsequent ones
      - \par error      issue a FatalError for duplicate entries
      - \par default    currently identical to merge

## SourceFiles
inputModeEntry.C

