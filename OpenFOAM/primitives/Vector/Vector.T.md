# Vector.T 
## Class
Foam::Vector

## Description
Templated 3D Vector derived from VectorSpace adding construction from
3 components, element access using x(), y() and z() member functions and
the inner-product (dot-product) and cross product operators.

A centre() member function which returns the Vector for which it is called
is defined so that point which is a typedef to Vector\<scalar\> behaves as
other shapes in the shape hierachy.

## SourceFiles
VectorI.H

