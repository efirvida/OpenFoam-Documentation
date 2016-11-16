# messageStream 
## Class
Foam::messageStream

## Description
Class to handle messaging in a simple, consistent stream-based
manner.

The messageStream class is globaly instantiated with a title string a
given severity, which controls the program termination, and a number of
errors before termination.  Errors, messages and other data are piped to
the messageStream class in the standard manner.

## Usage
\code
        messageStream
            << "message1" << "message2" << FoamDataType << endl;
\endcode

## SourceFiles
messageStream.C

