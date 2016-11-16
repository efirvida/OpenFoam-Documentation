# attachDetach 
## Class
Foam::attachDetach

## Description
Attach/detach boundary mesh modifier.  This modifier takes a set of
internal faces and converts them into boundary faces and vice versa
based on the given activation switch.

The patch is oriented using the flip map in the face zone.  The
oriented faces are put into the master patch and their mirror
images into the slave.

## SourceFiles
attachDetach.C
attachInterface.C
detachInterface.C
attachDetachPointMatchMap.C

