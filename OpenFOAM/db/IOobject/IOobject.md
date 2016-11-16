# IOobject 
## Class
Foam::IOobject

## Description
IOobject defines the attributes of an object for which implicit
objectRegistry management is supported, and provides the infrastructure
for performing stream I/O.

An IOobject is constructed with an object name, a class name, an instance
path, a reference to a objectRegistry, and parameters determining its
storage status.

\par Read options

Define what is done on object construction and explicit reads:
      - \par MUST_READ
        Object must be read from Istream on construction. \n
        Error if Istream does not exist or can't be read.
        Does not check timestamp or re-read.
      - \par MUST_READ_IF_MODIFIED
        Object must be read from Istream on construction. \n
        Error if Istream does not exist or can't be read. If object is
        registered its timestamp will be checked every timestep and possibly
        re-read.
      - \par READ_IF_PRESENT
        Read object from Istream if Istream exists, otherwise don't. \n
        Error only if Istream exists but can't be read.
        Does not check timestamp or re-read.
      - \par NO_READ
        Don't read

\par Write options

Define what is done on object destruction and explicit writes:
      - \par AUTO_WRITE
        Object is written automatically when requested to by the
        objectRegistry.
      - \par NO_WRITE
        No automatic write on destruction but can be written explicitly

## SourceFiles
IOobject.C
IOobjectReadHeader.C
IOobjectWriteHeader.C
IOobjectPrint.C

