# STARCDMeshReader 
## Class
Foam::meshReaders::STARCD

## Description
Read pro-STAR vrt/cel/bnd files.
The protected data in meshReader are filled.

Starting with pro-STAR version 4, the files have become easier to read.
- vertices are space-delimited.
- the cell format is logical.
- trimmed and degenerate cells are saved as polyhedral.
- the boundaries corresponds to cells and their faces.

## SourceFiles
STARCDMeshReader.C

