# fileName 
## Class
Foam::fileName

## Description
A class for handling file names.

A fileName is a string of characters without whitespace or quotes.
A fileName can be
      - constructed from a char*, a string or a word
      - concatenated by adding a '/' separator
      - decomposed into the path, name or component list
      - interrogated for type and access mode

The string::expand() method expands environment variables, etc,

## SourceFiles
fileName.C
fileNameIO.C

