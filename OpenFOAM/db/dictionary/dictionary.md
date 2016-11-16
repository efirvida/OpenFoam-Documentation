# dictionary 
## Class
Foam::dictionary

## Description
A list of keyword definitions, which are a keyword followed by any number
of values (e.g. words and numbers). The keywords can represent patterns
which are matched using Posix regular expressions. The general order for
searching is as follows:
- exact match
- pattern match (in reverse order)
- optional recursion into the enclosing (parent) dictionaries

The dictionary class is the base class for IOdictionary.
It also serves as a bootstrap dictionary for the objectRegistry data
dictionaries since, unlike the IOdictionary class, it does not use an
objectRegistry itself to work.

To add - a merge() member function with a non-const dictionary parameter?
This would avoid unnecessary cloning in the add(entry*, bool) method.

## SourceFiles
dictionary.C
dictionaryIO.C

