# error 
## Class
Foam::error

## Description
Class to handle errors and exceptions in a simple, consistent stream-based
manner.

The error class is globally instantiated with a title string. Errors,
messages and other data are piped to the messageStream class in the
standard manner.  Manipulators are supplied for exit and abort which may
terminate the program or throw an exception depending on whether the
exception handling has been switched on (off by default).

## Usage
\code
        error << "message1" << "message2" << FoamDataType << exit(errNo);
        error << "message1" << "message2" << FoamDataType << abort();
\endcode

## SourceFiles
error.C

