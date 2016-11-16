# starcdSurfaceWriter 
## Class
Foam::starcdSurfaceWriter

## Description
A surfaceWriter for STARCD files.

The geometry is written via the MeshedSurfaceProxy, the fields
are written in a trivial ASCII format with ID and VALUE as
so-called user data. These \c .usr files can be read into proSTAR
with these types of commands. For element data:
```
        getuser FILENAME.usr cell scalar free
        getuser FILENAME.usr cell vector free
```
and for vertex data:
```
        getuser FILENAME.usr vertex scalar free
        getuser FILENAME.usr vertex vector free
```

## Note
Only scalar and vector fields are supported directly.
A sphericalTensor is written as a scalar.
Other field types are not written.

## SourceFiles
starcdSurfaceWriter.C

