# createShellMesh 
## Class
Foam::createShellMesh

## Description
Creates mesh by extruding a patch.

## SourceFiles
createShellMesh.C

Extrudes into thickness direction.
- bottom faces originate from reversed original faces (have turning index)
- top faces originate from original faces (no turning index)

