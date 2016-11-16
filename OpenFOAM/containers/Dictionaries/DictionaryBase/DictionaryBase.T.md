# DictionaryBase.T 
## Class
Foam::DictionaryBase

## Description
Base dictionary class templated on both the form of doubly-linked list
it uses as well as the type it holds.

The double templating allows for the instantiation of forms with or
without storage management.

## Note
The IDLListType parameter should itself be a template but this confused
gcc 2.95.2 so it has to be instantiated for T when an instantiation of
DictionaryBase is requested

## See also
Dictionary and UDictionary

## SourceFiles
DictionaryBase.C
DictionaryBaseIO.C

