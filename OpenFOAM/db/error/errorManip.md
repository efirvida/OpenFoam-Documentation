# errorManip 
## Class
Foam::errorManip

## Description
Error stream manipulators for exit and abort which may terminate the
program or throw an exception depending if the exception
handling has been switched on (off by default).

## Usage
\code
        error << "message1" << "message2" << FoamDataType << exit(error, errNo);
        error << "message1" << "message2" << FoamDataType << abort(error);
\endcode

