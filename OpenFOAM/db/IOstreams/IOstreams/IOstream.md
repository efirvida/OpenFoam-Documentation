# IOstream 
## Class
Foam::IOstream

## Description
An IOstream is an abstract base class for all input/output systems; be
they streams, files, token lists etc.

The basic operations are construct, close, read token, read primitive
and read binary block.  In addition version control and line number
counting is incorporated.  Usually one would use the read primitive
member functions, but if one were reading a stream on unknown data
sequence one can read token by token, and then analyse.

## SourceFiles
IOstream.C

