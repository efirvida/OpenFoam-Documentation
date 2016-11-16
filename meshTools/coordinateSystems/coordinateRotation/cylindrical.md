# cylindrical 
## Class
Foam::cylindrical

## Description
A local coordinate rotation.

The cell based rotational field can be created in two ways:
      -# Each rotational tensor is defined with two vectors (\c dir and \c e3)
         where <tt>dir =  cellC - origin</tt> and \c e3 is the rotation axis.
          Per each cell an axesRotation type of rotation is created
          (cylindrical coordinates). For example:
```
          cylindrical
          {
              type        localAxes;
              e3          (0 0 1);
          }
```

      -# The rotational tensor field is provided at construction.

## SourceFiles
cylindrical.C

